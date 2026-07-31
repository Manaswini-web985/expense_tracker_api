import json
import os


FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "expenses.json")


def load_expenses():
    """Load all expenses from the JSON file."""
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_expenses(expenses):
    """Save the expense list back to the JSON file."""
    print("Saving to:", os.path.abspath(FILE_PATH))

    with open(FILE_PATH, "w") as file:
        json.dump(expenses, file, indent=4)