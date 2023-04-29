import mysql.connector

def display_welcome_message():
    print("Welcome to the Online Banking System!")
    print("************************************\n")

def display_menu():
    print("Please select an option:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Create Account")
    print("5. Close Account")
    print("6. Modify Account")
    print("0. Exit")

def main():
    display_welcome_message()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Perform check balance operation
            print("Check Balance selected.\n")
        elif choice == "2":
            # Perform deposit operation
            print("Deposit selected.\n")
        elif choice == "3":
            # Perform withdraw operation
            print("Withdraw selected.\n")
        elif choice == "4":
            # Perform create account operation
            print("Create Account selected.\n")
        elif choice == "5":
            # Perform close account operation
            print("Close Account selected.\n")
        elif choice == "6":
            # Perform modify account operation
            print("Modify Account selected.\n")
        elif choice == "0":
            print("Thank you for using the Online Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="banking_app"
)

def check_balance(account_number):
    cursor = connection.cursor()
    query = "SELECT balance FROM accounts WHERE account_number = %s"
    params = (account_number,)
    cursor.execute(query, params)
    result = cursor.fetchone()

    if result:
        print(f"Balance for Account {account_number}: ${result[0]:.2f}")
    else:
        print(f"Account {account_number} not found.")

    cursor.close()


def deposit(account_number, amount):
    cursor = connection.cursor()
    query = "UPDATE accounts SET balance = balance + %s WHERE account_number = %s"
    params = (amount, account_number)
    cursor.execute(query, params)
    connection.commit()

    if cursor.rowcount > 0:
        print(f"Deposit of ${amount:.2f} successful for Account {account_number}.")
    else:
        print(f"Account {account_number} not found.")

    cursor.close()

def withdraw(account_number, amount):
    cursor = connection.cursor()
    query = "UPDATE accounts SET balance = balance - %s WHERE account_number = %s AND balance >= %s"
    params = (amount, account_number, amount)
    cursor.execute(query, params)
    connection.commit()

    if cursor.rowcount > 0:
        print(f"Withdrawal of ${amount:.2f} successful from Account {account_number}.")
    else:
        print(f"Insufficient balance or account {account_number} not found.")

    cursor.close()

def create_account(pin, name, initial_balance):
    cursor = connection.cursor()
    query = "INSERT INTO accounts (pin, name, balance) VALUES (%s, %s, %s)"
    params = (pin, name, initial_balance)
    cursor.execute(query, params)
    connection.commit()

    account_number = cursor.lastrowid
    print(f"Account {account_number} created successfully.")

    cursor.close()

def delete_account(account_number):
    cursor = connection.cursor()
    query = "DELETE FROM accounts WHERE account_number = %s"
    params = (account_number,)
    cursor.execute(query, params)
    connection.commit()

    if cursor.rowcount > 0:
        print(f"Account {account_number} deleted successfully.")
    else:
        print(f"Account {account_number} not found.")

    cursor.close()

def modify_account(account_number, name=None, pin=None):
    cursor = connection.cursor()
    query = "UPDATE accounts SET"
    params = []

    if name:
        query += " name = %s,"
        params.append(name)

    if pin:
        query += " pin = %s,"
        params.append(pin)

    # Remove the trailing comma from the query
    query = query.rstrip(",")

    query += " WHERE account_number = %s"
    params.append(account_number)

    if not params:
        print("No modifications specified.")
        return

    cursor.execute(query, tuple(params))
    connection.commit()

    if cursor.rowcount > 0:
        print(f"Account {account_number} modified successfully.")
    else:
        print(f"Account {account_number} not found.")

    cursor.close()


if __name__ == "__main__":
    main()
