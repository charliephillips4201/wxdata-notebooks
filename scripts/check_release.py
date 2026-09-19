"""Check the v0.1.0 data archives against two companion notebooks.

Run with the Python interpreter from environment.yml. Files must already be
downloaded; --source-kind zenodo labels those files and does not contact Zenodo.
"""

from __future__ import annotations

import argparse
import base64
import csv
from datetime import datetime, timezone
import hashlib
from importlib import metadata
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import uuid
import zipfile


ROOT = Path(__file__).resolve().parents[1]
ARCHIVES = (
    "wxdata_wtk_bchrrr_nsrdb_2007_2023.zip",
    "wxdata_sup3rcc_taiesm1_curated_2000_2099.zip",
)
NOTEBOOKS = {
    "miso_monthly_event_counts": (
        ARCHIVES[0],
        "wtk_bchrrr_nsrdb_2007_2023/ba_stress_event_catalog/"
        "MISO_wtk_bchrrr_nsrdb_2007_2023_events.csv",
    ),
    "state_seasonal_risk_hours": (
        ARCHIVES[1],
        "taiesm1_historical_ssp245_v022_2000_2099/state_scenario_metrics/"
        "IA_taiesm1_historical_ssp245_v022_2000_2099_scenario_metrics.parquet",
    ),
}
SCENARIOS = {
    "installed_2024", "split_w00_s100", "split_w25_s75",
    "split_w50_s50", "split_w75_s25", "split_w100_s00",
}
SUMMARY_COLUMNS = [
    "scenario", "scenario_label", "stress_metric", "stress_metric_label",
    "planning_period", "season", "stress_hours",
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_file(path, row):
    require(row["validation_status"] == "pass", f"Unvalidated manifest row: {row['relative_path']}")
    require(path.is_file(), f"Missing input: {row['relative_path']}")
    require(path.stat().st_size == int(row["size_bytes"]), f"Size mismatch: {row['relative_path']}")
    digest = sha256(path)
    require(digest == row["sha256"], f"SHA-256 mismatch: {row['relative_path']}")
    return {"path": row["relative_path"], "size_bytes": path.stat().st_size,
            "sha256": digest, "record_type": row["record_type"], "status": "pass"}


def one_row(rows, record_type, relative_path):
    matches = [row for row in rows if row["record_type"] == record_type
               and row["relative_path"] == relative_path]
    require(len(matches) == 1, f"Expected one {record_type} manifest row: {relative_path}")
    return matches[0]


def prepare_inputs(archive_dir, stage, report):
    manifest = archive_dir / "RELEASE_MANIFEST.csv"
    report["manifest_sha256"] = sha256(manifest)
    with manifest.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    require({row["relative_path"] for row in rows if row["record_type"] == "archive"}
            == set(ARCHIVES), "Manifest must name exactly the two v0.1.0 archives")
    for name in ("README_DATASET.md", "LICENSE_DATA.txt", *ARCHIVES):
        kind = "archive" if name.endswith(".zip") else "loose_file"
        row = one_row(rows, kind, name)
        print(f"Verifying {name}", flush=True)
        report["verified_files"].append(verify_file(archive_dir / name, row))
    for archive_name, member in NOTEBOOKS.values():
        row = one_row(rows, "data_file", member)
        require(row["archive_name"] == archive_name, f"Wrong archive for {member}")
        target = stage / "data_inputs" / member
        target.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(archive_dir / archive_name) as archive:
            require(archive.namelist().count(member) == 1, f"Expected one ZIP member: {member}")
            require(archive.getinfo(member).file_size == int(row["size_bytes"]),
                    f"ZIP member size mismatch: {member}")
            with archive.open(member) as source, target.open("wb") as output:
                shutil.copyfileobj(source, output, 8 * 1024 * 1024)
        report["verified_files"].append(verify_file(target, row))


def validate_summary(path):
    import pandas as pd

    table = pd.read_csv(path)
    require(list(table.columns) == SUMMARY_COLUMNS, "Unexpected Iowa summary columns")
    require(len(table) == 240 and not table.isna().any().any(), "Iowa summary must have 240 complete rows")
    groups = ["scenario", "stress_metric", "planning_period", "season"]
    require(not table.duplicated(groups).any(), "Duplicate Iowa summary groups")
    expected = [SCENARIOS, {"net_load_p95", "renew_cf_10pct"},
                {"2000_2019", "2020_2039", "2040_2059", "2060_2079", "2080_2099"},
                {"Dec/Jan/Feb", "Mar/Apr/May", "Jun/Jul/Aug", "Sep/Oct/Nov"}]
    for column, values in zip(groups, expected):
        require(set(table[column]) == values, f"Unexpected Iowa {column}")
    require(pd.api.types.is_integer_dtype(table["stress_hours"])
            and table["stress_hours"].ge(0).all(), "Stress hours must be nonnegative integers")
    return {"rows": len(table), "columns": len(table.columns), "unique_groups": True,
            "nonnegative_integer_counts": True}


def validate_png(path):
    require(path.is_file() and path.stat().st_size > 8, f"Missing or empty figure: {path.name}")
    with path.open("rb") as stream:
        require(stream.read(8) == b"\x89PNG\r\n\x1a\n", f"Invalid PNG: {path.name}")


def portable(value, replacements):
    if isinstance(value, str):
        for path, label in replacements:
            value = value.replace(str(path), label).replace(path.as_posix(), label)
        return value
    if isinstance(value, list):
        return [portable(item, replacements) for item in value]
    if isinstance(value, dict):
        return {key: portable(item, replacements) for key, item in value.items()}
    return value


def execute_notebook(name, stage, output_dir, report, replacements):
    import nbformat
    from jupyter_client import KernelManager
    from jupyter_client.kernelspec import KernelSpec, KernelSpecManager
    from nbclient import NotebookClient

    # A private kernelspec avoids relying on an installed kernel named "wxdata".
    class CurrentPythonKernelSpecManager(KernelSpecManager):
        def get_kernel_spec(self, kernel_name):
            return KernelSpec(
                argv=[sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
                display_name="Release check Python", language="python",
                env={"MPLBACKEND": "module://matplotlib_inline.backend_inline",
                     "MPLCONFIGDIR": str(stage / "mpl"), "IPYTHONDIR": str(stage / "ipython")},
            )

    source = ROOT / "notebooks" / "analysis" / f"{name}.ipynb"
    notebook = nbformat.read(source, as_version=4)
    for cell in notebook.cells:
        if cell.cell_type == "code":
            cell.outputs = []
            cell.execution_count = None
    notebook.metadata["kernelspec"] = {
        "display_name": "Release check Python", "language": "python", "name": "release-check"}
    workdir = stage / "notebooks" / "analysis"
    workdir.mkdir(parents=True, exist_ok=True)
    nbformat.write(notebook, workdir / source.name)
    relative_output = f"notebooks/analysis/{name}.executed.ipynb"
    entry = {"notebook": f"notebooks/analysis/{name}.ipynb", "source_sha256": sha256(source),
             "executed_notebook": relative_output, "status": "fail"}
    report["notebooks"].append(entry)
    manager = KernelManager(kernel_name="release-check", kernel_spec_manager=CurrentPythonKernelSpecManager())
    client = NotebookClient(notebook, km=manager, timeout=600, allow_errors=False,
                            resources={"metadata": {"path": str(workdir)}})
    start = time.perf_counter()
    print(f"Executing {source.name} in a fresh kernel", flush=True)
    try:
        # Supplying a manager makes nbclient leave shutdown to its caller.
        client.execute()
        code = [cell for cell in notebook.cells if cell.cell_type == "code"]
        require(all(cell.execution_count is not None for cell in code), "An input code cell was not executed")
        require(not any(item.output_type == "error" for cell in code for item in cell.outputs),
                "A notebook produced an error output, including an allowed raises-exception tag")
        if name == "miso_monthly_event_counts":
            images = [item["data"]["image/png"] for cell in code for item in cell.outputs
                      if "image/png" in item.get("data", {})]
            require(len(images) == 1, "Expected exactly one fresh embedded MISO PNG")
            figure = output_dir / "miso_monthly_event_counts.png"
            figure.write_bytes(base64.b64decode(images[0]))
            validate_png(figure)
            entry["outputs"] = {"embedded_figures": 1, "figure": figure.name,
                                "existing_notebook_assertions": "pass"}
        else:
            folder = stage / "data_outputs" / "analysis" / name
            summary = validate_summary(folder / "iowa_seasonal_risk_hours.csv")
            expected = {f"iowa_{scenario}_seasonal_risk_hours.png" for scenario in SCENARIOS}
            require({path.name for path in folder.glob("*.png")} == expected, "Expected six named Iowa figures")
            for filename in sorted(expected):
                validate_png(folder / filename)
            entry["outputs"] = {**summary, "figures": sorted(expected),
                                "directory": f"data_outputs/analysis/{name}",
                                "existing_notebook_assertions": "pass"}
        entry["status"] = "pass"
    finally:
        entry["execution_seconds"] = round(time.perf_counter() - start, 3)
        try:
            destination = output_dir / relative_output
            destination.parent.mkdir(parents=True, exist_ok=True)
            nbformat.write(nbformat.from_dict(portable(notebook, replacements)), destination)
            generated = stage / "data_outputs" / "analysis" / name
            if generated.exists():
                shutil.copytree(generated, output_dir / "data_outputs" / "analysis" / name)
        finally:
            if client.kc is not None:
                client.kc.stop_channels()
            if manager.has_kernel:
                manager.shutdown_kernel(now=True)


def provenance():
    def git(*args):
        process = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True)
        return process.stdout.strip()

    result = {"python": platform.python_version(), "platform": platform.system(),
              "machine": platform.machine(),
              "packages": dict(sorted((dist.metadata["Name"], dist.version)
                                      for dist in metadata.distributions() if dist.metadata["Name"]))}
    try:
        result["git_commit"] = git("rev-parse", "HEAD")
        result["git_dirty"] = bool(git("status", "--porcelain", "--untracked-files=normal"))
    except (OSError, subprocess.CalledProcessError):
        result.update(git_commit=None, git_dirty=None)
    for filename in ("environment.yml", "scripts/check_release.py"):
        result[f"{filename}_sha256"] = sha256(ROOT / filename)
    return result


def write_report(output_dir, report, replacements):
    report = portable(report, replacements)
    (output_dir / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    lines = ["# Dataset and notebook release check", "", f"Result: **{report['status'].upper()}**.", "",
             f"Started (UTC): {report['started_utc']}. Source: **{report['source_kind']}**.", "",
             "Dataset target: **0.1.0**. Notebook commit: "
             f"`{report['environment'].get('git_commit')}`; dirty checkout: "
             f"`{report['environment'].get('git_dirty')}`.", "",
             f"Manifest SHA-256: `{report.get('manifest_sha256', 'not available')}`.", "",
             "| Notebook | Result | Seconds |", "|---|---|---:|"]
    for notebook in report["notebooks"]:
        lines.append(f"| [{Path(notebook['notebook']).stem}]({notebook['executed_notebook']}) "
                     f"| {notebook['status'].upper()} | {notebook.get('execution_seconds', '')} |")
    lines += ["", "Successful checks verify both archive hashes and sizes, loose README/license metadata, "
              "and the hashes of the two selected extracted inputs. Each notebook runs in a fresh kernel "
              "using this command's Python interpreter and only those staged dataset inputs.", "",
              "The MISO check requires its existing coverage/count assertions and one fresh embedded PNG. "
              "The Iowa check requires its existing hourly/count assertions, a complete 240-row, seven-column "
              "summary with unique groups and nonnegative integer counts, and six named PNGs.", "",
              "This is a two-notebook compatibility check. It does not validate all released products, "
              "all notebooks, or scientific correctness. The known Iowa pressure discrepancy remains "
              "a separate scientific review item. Source kind `zenodo` means the operator supplied "
              "downloaded files; this command does not download or authenticate them. Environment versions "
              "are recorded, but environment installation itself is not performed by this command.", ""]
    if "error" in report:
        lines += ["Failure:", "", "```text", report["error"], "```", ""]
    if report["status"] == "pass":
        lines += ["[MISO figure](miso_monthly_event_counts.png) · "
                  "[Iowa summary](data_outputs/analysis/state_seasonal_risk_hours/iowa_seasonal_risk_hours.csv)", ""]
    lines += ["[Detailed provenance, checks, outputs, and package versions](report.json)", ""]
    (output_dir / "REPORT.md").write_text("\n".join(lines), encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive-dir", required=True, type=Path)
    parser.add_argument("--output-dir", type=Path, help="New directory for reports and generated outputs")
    parser.add_argument("--source-kind", choices=("local", "zenodo"), default="local")
    args = parser.parse_args(argv)
    archive_dir = args.archive_dir.resolve()
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "_" + uuid.uuid4().hex[:8]
    output_dir = (args.output_dir or ROOT / "data_outputs" / "release_check" / run_id).resolve()
    # Refuse reuse so stale output files can never satisfy this run's checks.
    output_dir.mkdir(parents=True, exist_ok=False)
    report = {"status": "fail", "started_utc": datetime.now(timezone.utc).isoformat(),
              "source_kind": args.source_kind, "dataset_version": "0.1.0",
              "verified_files": [], "notebooks": [], "environment": {}}
    replacements = [(output_dir, "<output>"), (archive_dir, "<archives>"), (ROOT, "<repository>"),
                    (Path.home(), "<home>")]
    start = time.perf_counter()
    try:
        report["environment"] = provenance()
        with tempfile.TemporaryDirectory(prefix="wxc-") as temporary:
            stage = Path(temporary).resolve()
            replacements.insert(0, (stage, "<staging>"))
            prepare_inputs(archive_dir, stage, report)
            for name in NOTEBOOKS:
                execute_notebook(name, stage, output_dir, report, replacements)
        report["status"] = "pass"
    except Exception as error:
        report["error"] = f"{type(error).__name__}: {error}"
        report["traceback"] = traceback.format_exc()
    finally:
        report["total_seconds"] = round(time.perf_counter() - start, 3)
        write_report(output_dir, report, replacements)
    print(f"{report['status'].upper()}: {output_dir / 'REPORT.md'}", flush=True)
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
