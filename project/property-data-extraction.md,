# From Property Listings to Reliable Structured Data

**Context:** AI Engineering Internship at FairVisit  
**Status:** Ongoing  
**Focus:** Python extraction pipelines, data validation and asynchronous processing

## The problem behind the project

An accommodation listing contains information a property platform needs: descriptions, addresses, amenities, room details and photos.

However, this information is presented differently across websites. Some values are available in structured data, others appear within the page, and some are missing or inconsistent.

My work at FairVisit focuses on turning supported property-listing URLs into structured, validated information that can be mapped to the platform’s database.

The challenge extends beyond extracting text. The system also needs to recognize when the available evidence is incomplete and avoid creating misleading property records.

## Building specialized extraction pipelines

I developed Python extraction pipelines for Airbnb and Booking.com using Playwright, BeautifulSoup and structured-data parsing.

The pipelines collect relevant information and normalize it into consistent fields. These include property descriptions, location details, accommodation capacity, amenities, house rules, room options and photos.

Working with separate readers for each platform helped account for differences in how the websites organize and expose their information.

## Making data quality part of the workflow

A pipeline can complete successfully while still returning incomplete or incorrect fields.

I therefore investigated field availability and compared extracted values with source evidence. This helped identify missing information, mapping gaps and cases where different source elements conflicted.

I also worked on address parsing and normalization, including separating street names and house numbers.

My approach was to preserve uncertainty: when a value could not be supported reliably, the system should omit or flag it rather than invent an answer.

## Combining deterministic extraction with AI assistance

The workflow combines deterministic parsing and normalization with LLM-assisted mapping.

Deterministic rules handle information that can be extracted consistently. AI assistance helps map information into the required structure, while validation remains necessary to check the resulting fields.

This work strengthened my understanding of where AI can help and where explicit rules and source evidence are essential.

## Moving extraction into background processing

Extraction can take time and may encounter browser failures, network problems or platform verification pages.

I built an asynchronous FastAPI prototype that returns a job ID and processes extraction in the background. This separates the initial request from the longer extraction task.

I defined API behavior for:

- URL validation
- Job status reporting
- Structured errors
- Idempotency
- Queue limits
- JSON result delivery

The purpose was to make processing easier to track and failures easier to understand.

## Testing expected and unexpected behavior

I created automated contract and worker tests covering successful processing and failure scenarios.

The validation work also included regression checks to investigate whether extraction changes affected previously supported fields.

Platform verification pages, incomplete source data and browser or network failures needed explicit handling so that unsuccessful extraction would not be mistaken for a valid property import.

## Documenting how information moves

I documented source-to-schema mappings using the platform’s field names, along with rules for missing values and source provenance.

This documentation makes the transformation easier to understand and review. It also provides a clearer basis for extending the pipeline without changing the meaning of existing fields unintentionally.

## What this work has taught me

This project has strengthened my ability to:

- Build Python workflows around inconsistent external data.
- Separate processing success from data accuracy.
- Investigate failures using source evidence.
- Design APIs for tasks that run in the background.
- Use automated tests to check expected behavior.
- Apply AI assistance while keeping outputs traceable.

It has also shaped my interest in data engineering and AI systems: reliable results depend on careful decisions throughout the pipeline, from collection to validation and delivery.

## Current stage

The work is ongoing. Further activities include broader validation, improved field mapping, persistent job processing, monitoring and integration testing.

The background-processing service described here is a prototype; this page does not claim that the complete system has been deployed to production.

## Technologies

Python · Playwright · BeautifulSoup · FastAPI · Pydantic · REST APIs · JSON · LLM-assisted mapping

## Publication note

This case study summarizes my contribution. Company source code, private datasets, credentials and internal infrastructure details are not included.
