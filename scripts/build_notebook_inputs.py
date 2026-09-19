"""Rebuild the bundled notebook inputs from the extracted v0.1.0 datasets.

The manifest records the original release hashes and each notebook's required
columns, years, and scenarios. CSV values are copied as text, without rounding.
Parquet values retain their original Arrow types and precision.
"""

import argparse
import csv
import gzip
import hashlib
import io
from pathlib import Path

import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifests/notebook_inputs.csv"


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_csv(source, target, columns, first_year, last_year, scenarios):
    row_count = 0
    with source.open(encoding="utf-8-sig", newline="") as input_stream:
        reader = csv.reader(input_stream)
        header = next(reader)
        positions = [header.index(column) for column in columns]
        time_position = header.index("time_utc") if first_year else None
        scenario_position = header.index("scenario") if scenarios else None
        with target.open("wb") as output_stream:
            # No filename or timestamp in the gzip header: rebuilding is deterministic.
            with gzip.GzipFile(filename="", fileobj=output_stream, mode="wb", compresslevel=6, mtime=0) as compressed:
                with io.TextIOWrapper(compressed, encoding="utf-8", newline="") as text_stream:
                    writer = csv.writer(text_stream, lineterminator="\n")
                    writer.writerow(columns)
                    for row in reader:
                        if first_year and not first_year <= int(row[time_position][:4]) <= last_year:
                            continue
                        if scenarios and row[scenario_position] not in scenarios:
                            continue
                        writer.writerow([row[position] for position in positions])
                        row_count += 1
    return row_count


def build_parquet(source, target, columns, first_year, last_year, scenarios):
    table = pq.read_table(source, columns=columns)
    if first_year:
        years = pc.year(table["time_utc"])
        table = table.filter(pc.and_(pc.greater_equal(years, first_year), pc.less_equal(years, last_year)))
    if scenarios:
        table = table.filter(pc.is_in(table["scenario"], value_set=pa.array(sorted(scenarios))))
    dictionary_columns = []
    encodings = {}
    for field in table.schema:
        if pa.types.is_string(field.type) or pa.types.is_dictionary(field.type):
            dictionary_columns.append(field.name)
        elif pa.types.is_timestamp(field.type):
            encodings[field.name] = "DELTA_BINARY_PACKED"
        elif pa.types.is_floating(field.type):
            encodings[field.name] = "BYTE_STREAM_SPLIT"
    pq.write_table(table, target, compression="zstd", compression_level=9, use_dictionary=dictionary_columns, column_encoding=encodings)
    if not table.equals(pq.read_table(target)):
        raise ValueError(f"Parquet values changed: {target.name}")
    return table.num_rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", required=True, type=Path, help="Folder containing the two extracted dataset directories")
    args = parser.parse_args()
    with MANIFEST.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        fields = reader.fieldnames
        entries = list(reader)
    for number, entry in enumerate(entries, 1):
        source = args.source_dir / entry["source_path"]
        if sha256(source) != entry["source_sha256"]:
            raise ValueError(f"Input does not match the release: {source}")
        target = ROOT / entry["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        columns = entry["columns"].split("|")
        first_year = int(entry["first_year"]) if entry["first_year"] else None
        last_year = int(entry["last_year"]) if entry["last_year"] else None
        scenarios = set(entry["scenarios"].split("|")) if entry["scenarios"] else set()
        if source.suffix == ".csv":
            rows = build_csv(source, target, columns, first_year, last_year, scenarios)
        else:
            rows = build_parquet(source, target, columns, first_year, last_year, scenarios)
        size = target.stat().st_size
        if size >= 100 * 1024 * 1024:
            raise ValueError(f"Bundled file exceeds GitHub's ordinary file limit: {target}")
        entry.update(rows=str(rows), size_bytes=str(size), sha256=sha256(target))
        print(f"{number}/{len(entries)}: {target.name} ({rows:,} rows; {size / 1_000_000:.2f} MB)", flush=True)
    with MANIFEST.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(entries)
    print(f"Bundled {len(entries)} files: {sum(int(entry['size_bytes']) for entry in entries) / 1_000_000:.1f} MB.")


if __name__ == "__main__":
    main()
