```python
# ============================================================
# KEDAR FINANCE CO-OP BANK
# Jalgaon, Maharashtra
# Simple OOP Banking System
# ============================================================


# ------------------------------------------------------------
# ACCOUNT HOLDER CLASS
# ------------------------------------------------------------

class AccountHolder:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    # --------------------------------------------------------
    # Deposit Money
    # --------------------------------------------------------

    def deposit(self, amount):

        if amount <= 0:
            print("Invalid deposit amount.")

        else:
            self.balance = self.balance + amount

            print("\nMoney deposited successfully.")
            print(f"Deposited Amount : ₹{amount:.2f}")
            print(f"Current Balance  : ₹{self.balance:.2f}")

    # --------------------------------------------------------
    # Withdraw Money
    # --------------------------------------------------------

    def withdraw(self, amount):

        if amount <= 0:

            print("Invalid withdrawal amount.")

        elif amount > self.balance:

            print("Insufficient balance.")
            print(f"Available Balance : ₹{self.balance:.2f}")

        else:

            self.balance = self.balance - amount

            print("\nMoney withdrawn successfully.")
            print(f"Withdrawn Amount : ₹{amount:.2f}")
            print(f"Current Balance  : ₹{self.balance:.2f}")

    # --------------------------------------------------------
    # Show Account Details
    # --------------------------------------------------------

    def show_details(self):

        print("\n----------------------------------------")
        print("          ACCOUNT DETAILS")
        print("----------------------------------------")
        print(f"Account Holder : {self.name}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : ₹{self.balance:.2f}")
        print("----------------------------------------")


# ------------------------------------------------------------
# BANK CLASS
# ------------------------------------------------------------

class Bank:

    def __init__(self):

        self.bank_name = "Kedar Finance Co-op Bank"
        self.location = "Jalgaon, Maharashtra"

        # List to store account objects
        self.account_holders = []

    # --------------------------------------------------------
    # Create Account
    # --------------------------------------------------------

    def create_account(self):

        print("\n========================================")
        print("          CREATE NEW ACCOUNT")
        print("========================================")

        name = input("Enter account holder name: ").strip()

        if name == "":
            print("Name cannot be empty.")
            return

        account_number = input("Enter account number: ").strip()

        if account_number == "":
            print("Account number cannot be empty.")
            return

        # Check duplicate account number
        for account in self.account_holders:

            if account.account_number == account_number:

                print("\nAccount number already exists.")
                print("Please use a different account number.")

                return

        # Create AccountHolder object
        account = AccountHolder(
            name,
            account_number
        )

        # Store account object in list
        self.account_holders.append(account)

        print("\n========================================")
        print("       ACCOUNT CREATED SUCCESSFULLY")
        print("========================================")
        print(f"Account Holder : {name}")
        print(f"Account Number : {account_number}")
        print("Initial Balance: ₹0.00")
        print("========================================")

    # --------------------------------------------------------
    # Find Account
    # --------------------------------------------------------

    def find_account(self, account_number):

        for account in self.account_holders:

            if account.account_number == account_number:

                return account

        return None

    # --------------------------------------------------------
    # Deposit Money
    # --------------------------------------------------------

    def deposit_money(self):

        print("\n========================================")
        print("             DEPOSIT MONEY")
        print("========================================")

        if len(self.account_holders) == 0:

            print("No accounts available.")
            print("Please create an account first.")

            return

        account_number = input(
            "Enter account number: "
        ).strip()

        account = self.find_account(account_number)

        if account is None:

            print("\nAccount not found.")

            return

        try:

            amount = float(
                input("Enter deposit amount: ₹")
            )

            account.deposit(amount)

        except ValueError:

            print("Please enter a valid amount.")

    # --------------------------------------------------------
    # Withdraw Money
    # --------------------------------------------------------

    def withdraw_money(self):

        print("\n========================================")
        print("            WITHDRAW MONEY")
        print("========================================")

        if len(self.account_holders) == 0:

            print("No accounts available.")
            print("Please create an account first.")

            return

        account_number = input(
            "Enter account number: "
        ).strip()

        account = self.find_account(account_number)

        if account is None:

            print("\nAccount not found.")

            return

        try:

            amount = float(
                input("Enter withdrawal amount: ₹")
            )

            account.withdraw(amount)

        except ValueError:

            print("Please enter a valid amount.")

    # --------------------------------------------------------
    # Show One Account
    # --------------------------------------------------------

    def show_account(self):

        print("\n========================================")
        print("            SEARCH ACCOUNT")
        print("========================================")

        if len(self.account_holders) == 0:

            print("No accounts available.")

            return

        account_number = input(
            "Enter account number: "
        ).strip()

        account = self.find_account(account_number)

        if account:

            account.show_details()

        else:

            print("\nAccount not found.")

    # --------------------------------------------------------
    # Show ALL Accounts
    # --------------------------------------------------------

    def show_all_accounts(self):

        print("\n========================================")
        print("          ALL ACCOUNT HOLDERS")
        print("========================================")

        # Check whether accounts exist
        if not self.account_holders:

            print("No accounts found.")
            print("Please create an account first.")

            return

        # Counter
        count = 1

        # Loop through every account
        for account in self.account_holders:

            print(f"\nAccount #{count}")
            print("----------------------------------------")
            print(f"Account Holder : {account.name}")
            print(f"Account Number : {account.account_number}")
            print(f"Balance        : ₹{account.balance:.2f}")

            count = count + 1

        print("\n========================================")
        print(f"Total Accounts : {len(self.account_holders)}")
        print("========================================")


# ------------------------------------------------------------
# MAIN FUNCTION
# ------------------------------------------------------------

def main():

    # Create Bank object
    bank = Bank()

    # --------------------------------------------------------
    # Welcome Message
    # --------------------------------------------------------

    print("\n")
    print("==============================================")
    print("   Welcome to Kedar Finance Co-op Bank")
    print("          Jalgaon, Maharashtra")
    print("==============================================")

    # --------------------------------------------------------
    # Main Menu
    # --------------------------------------------------------

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

        choice = input("Enter your choice: ").strip()

        # ----------------------------------------------------
        # OPTION 1 - CREATE ACCOUNT
        # ----------------------------------------------------

        if choice == "1":

            bank.create_account()

        # ----------------------------------------------------
        # OPTION 2 - DEPOSIT
        # ----------------------------------------------------

        elif choice == "2":

            bank.deposit_money()

        # ----------------------------------------------------
        # OPTION 3 - WITHDRAW
        # ----------------------------------------------------

        elif choice == "3":

            bank.withdraw_money()

        # ----------------------------------------------------
        # OPTION 4 - SHOW ACCOUNT
        # ----------------------------------------------------

        elif choice == "4":

            bank.show_account()

        # ----------------------------------------------------
        # OPTION 5 - SHOW ALL ACCOUNTS
        # ----------------------------------------------------

        elif choice == "5":

            bank.show_all_accounts()

        # ----------------------------------------------------
        # OPTION 6 - EXIT
        # ----------------------------------------------------

        elif choice == "6":

            print("\n")
            print("==============================================")
            print("Thank you for using")
            print("Kedar Finance Co-op Bank")
            print("Jalgaon, Maharashtra")
            print("==============================================")

            break

        # ----------------------------------------------------
        # INVALID OPTION
        # ----------------------------------------------------

        else:

            print("\nInvalid choice.")
            print("Please enter a number between 1 and 6.")


# ------------------------------------------------------------
# START PROGRAM
# ------------------------------------------------------------

if __name__ == "__main__":

    main()
```
