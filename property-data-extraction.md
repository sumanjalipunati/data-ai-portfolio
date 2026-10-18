# Property Data Extraction and Validation

**Context:** AI Engineering Internship at FairVisit  
**Status:** Ongoing  
**Focus:** Python pipelines, data quality and background processing

## The problem

Accommodation listings contain information in different formats. Importing this information requires extracting relevant fields, standardizing their structure and checking incomplete or conflicting values.

## My contribution

- Developed specialized extraction pipelines for Airbnb and Booking.com using Python, Playwright and BeautifulSoup.
- Parsed structured source data and normalized it into a consistent format.
- Evaluated field availability and identified gaps against the target database schema.
- Built an asynchronous FastAPI prototype that returns a job ID and processes extraction in the background.
- Defined API behavior for URL validation, job status, structured errors, idempotency and queue limits.
- Created automated contract and worker tests.
- Documented field mappings and source provenance.

## Validation approach

I compared extracted fields with source evidence, checked missing and conflicting information, and tested failure scenarios such as incomplete pages and browser or network errors.

Uncertain values were omitted or flagged rather than invented. Processing success and field accuracy were evaluated separately.

## Technologies

Python, Playwright, BeautifulSoup, FastAPI, Pydantic, REST APIs, JSON and LLM-assisted mapping.

## What I learned

Reliable extraction requires more than collecting information. It also requires clear data contracts, traceable sources, systematic validation and predictable failure handling.

## Publication note

This page summarizes my contribution. Company source code, datasets and internal system details are not included.
