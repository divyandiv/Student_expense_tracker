import storage

def main():
    expenses = storage.load_expenses()
    while True:
        print("\n=== Student Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("6. Exit") # Leaving gaps for Student 2's options

        choice = input("Enter choice: ")
        if choice == "1":
            amount = float(input("Amount: "))
            category = input("Category (Food/Books/Travel): ")
            expenses.append({"amount": amount, "category": category})
            storage.save_expenses(expenses)
        elif choice == "2":
            for idx, exp in enumerate(expenses):
                print(f"{idx}. {exp['category']}: ₹{exp['amount']}")
        elif choice == "3":
            idx = int(input("Enter index to delete: "))
            if storage.delete_expense(expenses, idx):
                storage.save_expenses(expenses)
        elif choice == "6":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
