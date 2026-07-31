# Smart Expense Tracker API

A REST API built using Flask to manage personal expenses. The API allows users to add, view, filter, calculate totals, update, and delete expenses.

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate total expenses by category
- Update an existing expense
- Delete an expense
- JSON file based storage

## Tech Stack

- Python
- Flask
- JSON (File Storage)
- Pytest

## Project Structure

```
expense_tracker_api/
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
├── expenses.json
│
├── src/
│   ├── main.py
│   ├── routes.py
│   └── storage.py
│
└── tests/
    └── test_api.py
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Manaswini-web985/expense_tracker_api.git
cd expense_tracker_api
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Server

```bash
python src/main.py
```

The server starts at:

```
http://127.0.0.1:5000/
```

## Run Tests

```bash
pytest
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API status |
| POST | `/expenses` | Add a new expense |
| GET | `/expenses` | View all expenses |
| GET | `/expenses/category/<category>` | Filter expenses by category |
| GET | `/expenses/total` | Get total expenses |
| GET | `/expenses/total/<category>` | Get total by category |
| PUT | `/expenses/<id>` | Update an expense |
| DELETE | `/expenses/<id>` | Delete an expense |

## Storage

This application stores expense data in a local `expenses.json` file. No database is required.