# Copilot Instructions for arts_dashboard

## Project Overview
This project is a FastAPI-based dashboard for Canadian arts organizations, integrating data from Wikidata and storing it in MongoDB. The main components are:
- `scripts/main.py`: FastAPI app exposing endpoints for organization data.
- `scripts/fetch_wikidata.py`: Script to fetch and process Wikidata SPARQL results, storing them in MongoDB.
- `scripts/config.py`: Centralized configuration for MongoDB connection details.

## Architecture & Data Flow
- Data is fetched from Wikidata using SPARQL in `fetch_wikidata.py`.
- Results are processed into a pandas DataFrame and inserted into MongoDB (`arts_db.organizations`).
- The FastAPI app (`main.py`) reads from MongoDB and serves organization data via HTTP endpoints.

## Developer Workflows
- **Run FastAPI server:**
  ```powershell
  cd scripts; uvicorn main:app --reload
  ```
- **Fetch and update Wikidata:**
  ```powershell
  cd scripts; python fetch_wikidata.py
  ```
- MongoDB must be running locally on default port (27017).

## Project-Specific Patterns
- All MongoDB connection details are set in `config.py` and imported elsewhere.
- Data fetched from Wikidata is normalized into a consistent schema before insertion.
- External dependencies: `fastapi`, `pymongo`, `pandas`, `requests`.
- No test suite or build system detected; scripts are run directly.

## Integration Points
- Wikidata SPARQL endpoint for organization data.
- Local MongoDB instance for persistent storage.
- FastAPI for serving data to clients.

## Conventions
- All scripts reside in the `scripts/` directory.
- Configuration is centralized in `config.py`.
- Data schema for organizations includes: `wikidata_id`, `name`, `type`, `location`, `website`, `fetched_at`.

## Example Usage
- To update the database, run `fetch_wikidata.py`.
- To serve data, run the FastAPI app in `main.py`.

---
For questions or missing details, review the scripts in the `scripts/` directory or update this file as new workflows emerge.
