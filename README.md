# Day API

## Scenario

You've been commissioned to complete a project begun by another developer. The project aim is to create an API that simplifies dealing with dates and times.

While the project is incomplete, there is already a lot of work for you to build on. The utility functions required by the API all have existing function signatures, and the code for the API itself (though not the actual routes) has been created. Most importantly, this project has a large test suite to verify that everything is functioning as required.

Your task is threefold:

- [Complete the utility functions](./days_api/date_functions.py)
- [Build the required API routes](./README.md#api-documentation)
- Ensure that **all tests are passing** and that the code is of a high standard

## Setup and installation

1. Navigate to the `days_api` folder
2. Create and activate a new virtual environment
3. Run `pip3 install -r requirements.txt` to install the required libraries

## Development

Run the server with `python3 app.py`; you can access the API on port `8080`.

## Quality assurance

Check the code quality with `pylint *.py`.

Run tests with `pytest -v`

## API documentation

The API is JSON-based; **all responses should be in JSON format** only.

| Route | Method | Data | Example response | Purpose |
| --- | --- | --- | --- | --- |
| `/` | `GET` | None | `{ "message": "Welcome to the Days API." }` | API welcome message |
| `/between` | `POST` | A request body with the following keys:<br />- `first` (string in the format `DD.MM.YYYY`)<br />- `last` (string in the format `DD.MM.YYYY`) | `{ "days": 17 }` | Returns the number of days between two dates |
| `/weekday` | `POST` | A request body with the following key:<br />- `date` (string in the format `DD.MM.YYYY`) | `{ "weekday": "Monday" }` | Returns the day of the week a specific date is |
| `/history` | `GET` | Optional query parameter:<br />- `number` (the number of requests to return; default 5, 1<=number<=20) | `[{"method": "POST", "at": "12/02/2023 18:36", "route": "weekday"}, {"method": "POST", "at": "12/02/2023 18:39", "route": "weekday"}]` | Returns details on the last `number` of requests to the API |
| `/history` | `DELETE` | None | `{ "status": "History cleared" }` | Returns details on the last `number` of requests to the API |

## Marking

This assessment is marked in two ways:

- Tests passing (90%)
- Pylint score (10%)
