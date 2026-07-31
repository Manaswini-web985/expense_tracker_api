from flask import jsonify, request
from storage import load_expenses, save_expenses

def register_routes(app):

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "message": "Expense Tracker API is running!"
        })

    @app.route("/expenses", methods=["POST"])
    def add_expense():

        
        data = request.get_json()

        
        expenses = load_expenses()

        
        new_id = 1
        if expenses:
            new_id = max(expense["id"] for expense in expenses) + 1

        
        new_expense = {
            "id": new_id,
            "title": data["title"],
            "amount": data["amount"],
            "category": data["category"],
            "date": data["date"]
        }

        
        expenses.append(new_expense)
        save_expenses(expenses)

        return jsonify({
            "message": "Expense added successfully",
            "expense": new_expense
        }), 201


    @app.route("/expenses", methods=["GET"])
    def get_expenses():
        expenses = load_expenses()
        return jsonify(expenses), 200
    @app.route("/expenses/category/<category>", methods=["GET"])
    def get_expenses_by_category(category):
        expenses = load_expenses()

        filtered = [
            expense for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

        return jsonify(filtered), 200
    @app.route("/expenses/total", methods=["GET"])
    def total_expenses():
        expenses = load_expenses()

        total = sum(expense["amount"] for expense in expenses)

        return jsonify({
            "total": total
        }), 200


    @app.route("/expenses/total/<category>", methods=["GET"])
    def total_by_category(category):
        expenses = load_expenses()

        total = sum(
            expense["amount"]
            for expense in expenses
            if expense["category"].lower() == category.lower()
        )

        return jsonify({
            "category": category,
            "total": total
        }), 200
    
    @app.route("/expenses/<int:id>", methods=["PUT"])
    def update_expense(id):
        expenses = load_expenses()

        for expense in expenses:
            if expense["id"] == id:

                data = request.get_json()

                expense["title"] = data.get("title", expense["title"])
                expense["amount"] = data.get("amount", expense["amount"])
                expense["category"] = data.get("category", expense["category"])
                expense["date"] = data.get("date", expense["date"])

                save_expenses(expenses)

                return jsonify({
                    "message": "Expense updated successfully",
                    "expense": expense
                }), 200

        return jsonify({
            "message": "Expense not found"
        }), 404

    @app.route("/expenses/<int:id>", methods=["DELETE"])
    def delete_expense(id):
        expenses = load_expenses()

        for expense in expenses:
            if expense["id"] == id:

                expenses.remove(expense)

                save_expenses(expenses)

                return jsonify({
                    "message": "Expense deleted successfully"
                }), 200

        return jsonify({
            "message": "Expense not found"
        }), 404