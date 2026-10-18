# Property Data Validation Demo

**Status:** In development  
**Data:** Synthetic examples only

This Python demonstration will check property records for:

- Missing required fields
- Duplicate property IDs
- Invalid accommodation capacity
- Coordinates outside valid geographic ranges

The planned output is a validation report identifying the affected records and explaining each issue.

This is an independent portfolio example inspired by my experience with data quality. It does not contain FairVisit source code, company data or internal validation rules.

## Planned files

- `sample_properties.csv` — synthetic input records
- `validate_properties.py` — validation script
- `validation_report.csv` — generated results
