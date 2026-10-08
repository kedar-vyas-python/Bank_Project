
# ============================================================
# KEDAR FINANCE CO-OP BANK
# Jalgaon, Maharashtra
# Simple OOP Banking System
# ============================================================


# ------------------------------------------------------------
# AccountHolder Class
# ------------------------------------------------------------

class AccountHolder:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    # Deposit money
    def deposit(self, amount):

        if amount > 0:
            self.balance = self.balance + amount
            print(f"₹{amount:.2f} deposited successfully.")
            print(f"Current Balance: ₹{self.balance:.2f}")

        else:
            print("Invalid deposit amount.")

    # Withdraw money
    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal amount.")

        elif amount > self.balance:
            print("Insufficient balance.")

        else:
            self.balance = self.balance - amount
            print(f"₹{amount:.2f} withdrawn successfully.")
            print(f"Current Balance: ₹{self.balance:.2f}")

    # Show account details
    def show_details(self):

        print("\n--------------------------------")
        print("       ACCOUNT DETAILS")
        print("--------------------------------")
        print(f"Account Holder : {self.name}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : ₹{self.balance:.2f}")
        print("--------------------------------")


# ------------------------------------------------------------
# Bank Class
# ------------------------------------------------------------

class Bank:

    def __init__(self):

        self.bank_name = "Kedar Finance Co-op Bank"
        self.location = "Jalgaon, Maharashtra"

        # Store all account holders
        self.account_holders = []

    # Create new account
    def create_account(self):

        print("\n================================")
        print("       CREATE NEW ACCOUNT")
        print("================================")

        name = input("Enter account holder name: ")
        account_number = input("Enter account number: ")

        # Check if account number already exists
        for account in self.account_holders:

            if account.account_number == account_number:
                print("Account number already exists.")
                return

        # Create AccountHolder object
        account = AccountHolder(name, account_number)

        # Add account to bank
        self.account_holders.append(account)

        print("\nAccount created successfully!")
        print(f"Account Holder : {name}")
        print(f"Account Number : {account_number}")

    # Find account
    def find_account(self, account_number):

        for account in self.account_holders:

            if account.account_number == account_number:
                return account

        return None

    # Deposit money
    def deposit_money(self):

        print("\n================================")
        print("          DEPOSIT MONEY")
        print("================================")

        account_number = input("Enter account number: ")

        account = self.find_account(account_number)

        if account:

            try:
                amount = float(input("Enter deposit amount: ₹"))
                account.deposit(amount)

            except ValueError:
                print("Please enter a valid number.")

        else:
            print("Account not found.")

    # Withdraw money
    def withdraw_money(self):

        print("\n================================")
        print("         WITHDRAW MONEY")
        print("================================")

        account_number = input("Enter account number: ")

        account = self.find_account(account_number)

        if account:

            try:
                amount = float(input("Enter withdrawal amount: ₹"))
                account.withdraw(amount)

            except ValueError:
                print("Please enter a valid number.")

        else:
            print("Account not found.")

    # Show account details
    def show_account(self):

        print("\n================================")
        print("       SEARCH ACCOUNT")
        print("================================")

        account_number = input("Enter account number: ")

        account = self.find_account(account_number)

        if account:
            account.show_details()

        else:
            print("Account not found.")

    # Show all accounts
    def show_all_accounts(self):

        print("\n================================")
        print("        ALL ACCOUNT HOLDERS")
        print("================================")

        if len(self.account_holders) == 0:

            print("No accounts found.")

        else:

            for account in self.account_holders:

                print("--------------------------------")
                print(f"Name           : {account.name}")
                print(f"Account Number : {account.account_number}")
                print(f"Balance        : ₹{account.balance:.2f}")

        print("--------------------------------")


# ------------------------------------------------------------
# Main Function
# ------------------------------------------------------------

def main():

    # Create Bank object
    bank = Bank()

    # Welcome message
    print("\n")
    print("==============================================")
    print("   Welcome to Kedar Finance Co-op Bank")
    print("          Jalgaon, Maharashtra")
    print("==============================================")

    while True:

        print("\n")
        print("==============================================")
        print("        KEDAR FINANCE CO-OP BANK")
        print("           Jalgaon, Maharashtra")
        print("==============================================")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Show Account Details")
        print("5. Show All Accounts")
        print("6. Exit")
        print("==============================================")

        choice = input("Enter your choice: ")

        # Create account
        if choice == "1":

            bank.create_account()

        # Deposit
        elif choice == "2":

            bank.deposit_money()

        # Withdraw
        elif choice == "3":

            bank.withdraw_money()

        # Show account
        elif choice == "4":

            bank.show_account()

        # Show all accounts
        elif choice == "5":

            bank.show_all_accounts()

        # Exit
        elif choice == "6":

            print("\n==============================================")
            print("Thank you for using")
            print("Kedar Finance Co-op Bank")
            print("Jalgaon, Maharashtra")
            print("==============================================")

            break

        # Invalid choice
        else:

            print("Invalid choice. Please select 1 to 6.")


# ------------------------------------------------------------
# Program starts here
# ------------------------------------------------------------

if __name__ == "__main__":
    main()

