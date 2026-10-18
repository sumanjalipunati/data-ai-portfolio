"""Validate synthetic property records and generate an issue report."""

import csv
import math
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "sample_properties.csv"
OUTPUT_FILE = BASE_DIR / "validation_report.csv"

REQUIRED_FIELDS = (
    "property_id",
    "name",
    "city",
    "capacity",
    "latitude",
    "longitude",
)


def validate_records(records):
    """Return one report entry per validation issue."""
    id_counts = Counter(
        record["property_id"]
        for record in records
        if record["property_id"]
    )
    issues = []

    for row_number, record in enumerate(records, start=2):
        def report(field, message):
            issues.append({
                "csv_row": row_number,
                "property_id": record["property_id"],
                "field": field,
                "value": record[field],
                "issue": message,
            })

        for field in REQUIRED_FIELDS:
            if not record[field]:
                report(field, "Required value is missing")

        property_id = record["property_id"]
        if property_id and id_counts[property_id] > 1:
            report("property_id", "Duplicate property ID")

        if record["capacity"]:
            try:
                capacity = int(record["capacity"])
            except ValueError:
                report("capacity", "Capacity must be a whole number")
            else:
                if capacity <= 0:
                    report("capacity", "Capacity must be greater than zero")

        for field, minimum, maximum in (
            ("latitude", -90, 90),
            ("longitude", -180, 180),
        ):
            if not record[field]:
                continue

            try:
                value = float(record[field])
            except ValueError:
                report(field, "Coordinate must be numeric")
                continue

            if not math.isfinite(value):
                report(field, "Coordinate must be a finite number")
            elif not minimum <= value <= maximum:
                report(
                    field,
                    f"Coordinate must be between {minimum} and {maximum}",
                )

    return issues


def main():
    with INPUT_FILE.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)

        missing_columns = set(REQUIRED_FIELDS) - set(reader.fieldnames or [])
        if missing_columns:
            raise ValueError(
                f"Missing CSV columns: {', '.join(sorted(missing_columns))}"
            )

        records = [
            {
                field: (row.get(field) or "").strip()
                for field in REQUIRED_FIELDS
            }
            for row in reader
        ]

    issues = validate_records(records)

    with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as destination:
        writer = csv.DictWriter(
            destination,
            fieldnames=["csv_row", "property_id", "field", "value", "issue"],
        )
        writer.writeheader()
        writer.writerows(issues)

    affected_rows = len({issue["csv_row"] for issue in issues})

    print(f"Records checked: {len(records)}")
    print(f"Records with issues: {affected_rows}")
    print(f"Validation issues: {len(issues)}")
    print(f"Report saved to: {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
