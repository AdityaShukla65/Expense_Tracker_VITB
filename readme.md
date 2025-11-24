# Expense Tracker (simple)
This is a simple expense tracker project built with basic Python and SQLite.

## What it does
- Add, view, edit, delete expenses
- Simple monthly summary and category summary
- Data stored in local SQLite file `expenses.db`

## Run
1. Make sure you have Python 3.8+ installed.
2. (Optional) Create a virtualenv: `python -m venv venv` and activate it.
3. Install deps: `pip install -r requirements.txt` (only `tabulate` is used; optional)
4. Run: `python app.py`

## Project files
- app.py : main program (CLI)
- db.py : db setup and helper functions
- transactions.py : functions to add/edit/delete/list
- reports.py : summary reports

## Notes
- This is intentionally simple, matching course-level Python.
- Use the menu options in app to try features.