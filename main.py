from expense_manager import ExpenseManager
from reports import generate_reports

def main():
    manager = ExpenseManager()

    while True:
        print("\n1. Add Expense\n2. View All\n3. Generate Report\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Category: ")
            amount = float(input("Amount: "))
            desc = input("Description: ")
            manager.add_expense(category, amount, desc)
            print("✅ Expense Added!")
        elif choice == '2':
            for row in manager.get_expenses():
                print(row)
        elif choice == '3':
            generate_reports()
        elif choice == '4':
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
