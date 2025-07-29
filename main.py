from auth import create_user_table, register, login, log_history, delete_action, login_action
from tracker import create_transaction_tb, add_trans, view_trans, list_trans, update_trans, delete_trans, set_budget, budget_table, budget_warning
from reports import gen_month_report, gen_year_report
import shutil
import os

def main():
    create_user_table()
    create_transaction_tb()
    budget_table()
    log_history()

    while True:
        print("----------------------------------")
        print("     Personal Finance Manager    ")
        print("----------------------------------")
        print(" 1. Register\n 2. Login\n 3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            register(username, password)

        elif choice == "2":
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            if login(username, password):
                user_menu(username, password)

        elif choice == "3":
            print("Exiting App.")
            break

        else:
            print("Invalid choice. Try again.")

def user_menu(username, password):

    while True:
        print("----------------------------------")
        print(f"         Welcome {username} ")
        print("----------------------------------")
        print("  1. Add Income \n  2. Add Expense \n  3. View Transactions \n  4. Update Transaction \n  5. Delete Transaction \n  6. Monthly Report \n  7. Yearly Report \n  8. Set Budget \n  9. Delete Account \n 10. Backup Data \n 11. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Income category (ex Salary, Bonus etc..): ")
            amount = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD): ")
            description = input("Describe Category: ")
            add_trans(username, "Income", category, amount, date, description)

        elif choice == "2":
            category = input("Expense category (ex Food, Shopping etc..): ")
            amount = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD): ")
            description = input("Describe Category: ")
            add_trans(username, "Expense", category, amount, date, description)
            # if type == "Expense":
            month = date.split("-")[1]
            year = date.split("-")[0]
            budget_warning(username, category, month, year)

        elif choice == "3":
            view_trans(username)

        elif choice == "4":
            list_trans(username)
            trans_id = int(input("Enter Transaction ID to Update: "))
            field = input("Which field to update? (Category/Amount/Date/Description): ").lower()
            new_value = input("Enter new Value: ")
            if field == "amount":
                new_value = float(new_value)
            update_trans(trans_id, username, field, new_value)

        elif choice == "5":
            list_trans(username)
            trans_id = int(input("Enter Transaction ID to Delete: "))
            delete_trans(trans_id, username)

        elif choice == "6":
            month = input("Enter month (MM): ")
            year = input("Enter year (YYYY): ")
            gen_month_report(username, month, year)

        elif choice == "7":
            year = input("Enter year (YYYY): ")
            gen_year_report(username, year)

        elif choice == "8":
            category = input("Enter Category to set Budget: ")
            month = input("Enter Month (MM): ")
            year = input("Enter Year (YYYY): ")
            amount = float(input("Enter Budget amount: "))
            set_budget(username, category, month, year, amount)

        elif choice == "9":
            confirm = input("Are you sure you want to Delete your account? (yes/no): ").lower()
            if confirm == "yes":
                delete_action(username)
                login_action(username, "Account Deleted")
                break
            else:
                print("Account Delete canceled.")

        elif choice == "10":
            backup_db(username)

        elif choice == "11":
            print("Logged Out.")
            break

        else:
            print("Invalid choice, Try again.")

def backup_db(username):
    if os.path.exists('finance.db'):
        backup_name = f"{username}.db"
        shutil.copy('finance.db', backup_name)
        print(f"Backup file backed up successfully as '{backup_name}'")

    else:
        print("Backup file not found.")

if __name__ == "__main__":
    main();

