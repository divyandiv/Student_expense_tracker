import json

def save_expenses(expenses, filename="expenses.json"):
    with open(filename, "w") as f:
        json.dump(expenses, f, indent=4)
    print("Data saved successfully!")
def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def delete_expense(expenses, index):
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Removed: {removed['category']} - ₹{removed['amount']}")
        return True
    print("Invalid index!")
    return False
