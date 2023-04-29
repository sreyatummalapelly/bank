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

if __name__ == "__main__":
    main()
