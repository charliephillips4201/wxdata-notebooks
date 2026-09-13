"""Focused failure checks: python -m unittest discover -s scripts -p 'test_*.py'."""

import csv
import importlib.util
import itertools
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("check_release", Path(__file__).with_name("check_release.py"))
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class ReleaseCheckFailures(unittest.TestCase):
    def test_tagged_cell_error_is_rejected_and_executed_notebook_is_retained(self):
        import nbformat

        with tempfile.TemporaryDirectory(prefix="wxc-test-") as temporary:
            root = Path(temporary)
            source = root / "notebooks" / "analysis" / "miso_monthly_event_counts.ipynb"
            source.parent.mkdir(parents=True)
            notebook = nbformat.v4.new_notebook(cells=[nbformat.v4.new_code_cell(
                "raise RuntimeError('deliberate tagged error')",
                metadata={"tags": ["raises-exception"]})])
            nbformat.write(notebook, source)
            output = root / "report"
            output.mkdir()
            report = {"notebooks": []}
            with patch.object(CHECK, "ROOT", root):
                with self.assertRaisesRegex(ValueError, "error output"):
                    CHECK.execute_notebook("miso_monthly_event_counts", root / "stage", output, report,
                                           [(root, "<test>")])
            self.assertEqual(report["notebooks"][0]["status"], "fail")
            executed = nbformat.read(output / report["notebooks"][0]["executed_notebook"], as_version=4)
            self.assertTrue(any(item.output_type == "error" for item in executed.cells[0].outputs))

    def test_corrupt_archive_stops_before_execution_and_retains_failure_report(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            rows = []
            for name in ("README_DATASET.md", "LICENSE_DATA.txt", *CHECK.ARCHIVES):
                path = root / name
                path.write_bytes(b"original file")
                rows.append({"record_type": "archive" if name.endswith(".zip") else "loose_file",
                             "relative_path": name, "size_bytes": path.stat().st_size,
                             "sha256": CHECK.sha256(path), "validation_status": "pass"})
            # Same byte length so checksum verification, rather than size, catches corruption.
            (root / CHECK.ARCHIVES[0]).write_bytes(b"corrupt! file")
            with (root / "RELEASE_MANIFEST.csv").open("w", newline="", encoding="utf-8") as stream:
                writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
                writer.writeheader()
                writer.writerows(rows)
            with patch.object(CHECK, "provenance", return_value={}), patch.object(CHECK, "execute_notebook") as execute:
                result = CHECK.main(["--archive-dir", str(root), "--output-dir", str(root / "report")])
            self.assertEqual(result, 1)
            execute.assert_not_called()
            report = json.loads((root / "report" / "report.json").read_text(encoding="utf-8"))
            self.assertEqual(report["status"], "fail")
            self.assertIn("SHA-256 mismatch", report["error"])
            self.assertNotIn(str(root), (root / "report" / "REPORT.md").read_text(encoding="utf-8"))

    def test_incomplete_or_invalid_summary_is_rejected(self):
        import pandas as pd

        rows = [{"scenario": scenario, "scenario_label": scenario,
                 "stress_metric": metric, "stress_metric_label": metric,
                 "planning_period": period, "season": season, "stress_hours": 1}
                for scenario, metric, period, season in itertools.product(
                    sorted(CHECK.SCENARIOS), ["net_load_p95", "renew_cf_10pct"],
                    ["2000_2019", "2020_2039", "2040_2059", "2060_2079", "2080_2099"],
                    ["Dec/Jan/Feb", "Mar/Apr/May", "Jun/Jul/Aug", "Sep/Oct/Nov"])]
        table = pd.DataFrame(rows, columns=CHECK.SUMMARY_COLUMNS)
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "summary.csv"
            table.to_csv(path, index=False)
            self.assertEqual(CHECK.validate_summary(path)["rows"], 240)
            table.iloc[:-1].to_csv(path, index=False)
            with self.assertRaisesRegex(ValueError, "240 complete rows"):
                CHECK.validate_summary(path)
            invalid = table.copy()
            invalid.iloc[0] = invalid.iloc[1]
            invalid.to_csv(path, index=False)
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                CHECK.validate_summary(path)
            for count in (-1, 1.5):
                invalid = table.copy()
                invalid["stress_hours"] = invalid["stress_hours"].astype(float)
                invalid.loc[0, "stress_hours"] = count
                invalid.to_csv(path, index=False)
                with self.assertRaisesRegex(ValueError, "nonnegative integers"):
                    CHECK.validate_summary(path)


if __name__ == "__main__":
    unittest.main()
