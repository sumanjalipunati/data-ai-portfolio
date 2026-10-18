# Property Data Validation Demo

A small Python tool that checks property records and generates a CSV report explaining data-quality issues.

**Status:** Implemented and manually checked against the included synthetic sample.

## Why I built it

Data pipelines need to identify invalid or incomplete records before those records are used elsewhere.

This example demonstrates validation techniques related to my experience with property-data processing. It is an independent portfolio demonstration, not FairVisit company code.

## Checks included

- Missing required values
- Duplicate property IDs, flagging every occurrence
- Capacity values that are not positive whole numbers
- Non-numeric or non-finite coordinates
- Latitude outside -90 to 90
- Longitude outside -180 to 180

## Requirements

Python 3. No additional packages are required.

## How to run

Download and extract the repository. Open a terminal in this folder and run:

```powershell
py validate_properties.py
```

Alternatively:

```bash
python validate_properties.py
```

The script reads `sample_properties.csv` and creates or overwrites `validation_report.csv` in the same folder.

## Verified sample results

```text
Records checked: 10
Records with issues: 9
Validation issues: 9
Report saved to: validation_report.csv
```

I inspected the generated report and confirmed that it identified all nine deliberate issues in this sample, including both occurrences of the duplicate ID.

This is a sample verification, not a comprehensive test suite.

## Files

- `sample_properties.csv` — fictional records with deliberate errors
- `validate_properties.py` — validation script
- `validation_report.csv` — generated sample output

## Limitations

These checks assess completeness, basic numeric validity and ID uniqueness.

They do not verify whether a property exists, whether its coordinates match its address, or whether its details are factually accurate. Unique records that pass these checks may still contain incorrect information.

## Data and ownership

All included records are synthetic. No company source code, private datasets or credentials are included.
