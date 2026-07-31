import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from main import app

import pytest


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == "Expense Tracker API is running!"


def test_add_expense(client):

    expense = {
        "title": "Lunch",
        "amount": 200,
        "category": "Food",
        "date": "2026-07-31"
    }

    response = client.post("/expenses", json=expense)

    assert response.status_code == 201
    assert response.json["expense"]["title"] == "Lunch"


def test_get_expenses(client):

    response = client.get("/expenses")

    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_filter_category(client):

    response = client.get("/expenses?category=Food")

    assert response.status_code == 200


def test_total_expenses(client):

    response = client.get("/expenses/total")

    assert response.status_code == 200