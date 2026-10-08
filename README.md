# Kedar Finance Co-op Bank

A simple **CLI-based Banking System built with Python and Object-Oriented Programming (OOP)**.

This project is designed as a beginner-level Python project to practice **classes, objects, methods, lists, loops, conditions, and user input**.

> **Location:** Jalgaon, Maharashtra
> **Project Type:** Python CLI Application
> **Main File:** `bank.py`

---

## 📌 Project Overview

**Kedar Finance Co-op Bank** is a simple command-line banking application.

The application allows users to:

* Create new bank accounts
* Deposit money
* Withdraw money
* Check account details
* View all account holders
* Exit the application

The project uses basic **Object-Oriented Programming concepts** to represent the bank and its customers.

---

## ✨ Features

### 1. Create Account

Users can create a new bank account by entering:

* Account holder name
* Account number

Example:

```text
Enter account holder name: Kedar
Enter account number: 1001

ACCOUNT CREATED SUCCESSFULLY
Account Holder : Kedar
Account Number : 1001
Initial Balance: ₹0.00
```

The program also checks whether the account number already exists.

---

### 2. Deposit Money

Users can deposit money into their account.

Example:

```text
Enter account number: 1001
Enter deposit amount: ₹50000

Money deposited successfully.
Deposited Amount : ₹50000.00
Current Balance  : ₹50000.00
```

---

### 3. Withdraw Money

Users can withdraw money from their account.

The program checks whether the account has sufficient balance.

Example:

```text
Enter account number: 1001
Enter withdrawal amount: ₹5000

Money withdrawn successfully.
Withdrawn Amount : ₹5000.00
Current Balance  : ₹45000.00
```

If the user tries to withdraw more money than the available balance:

```text
Insufficient balance.
Available Balance : ₹45000.00
```

---

### 4. Show Account Details

Users can search for an account using the account number.

Example:

```text
Enter account number: 1001

----------------------------------------
          ACCOUNT DETAILS
----------------------------------------
Account Holder : Kedar
Account Number : 1001
Balance        : ₹45000.00
----------------------------------------
```

---

### 5. Show All Accounts

The application can display all accounts currently created during the program execution.

Example:

```text
========================================
          ALL ACCOUNT HOLDERS
========================================

Account #1
----------------------------------------
Account Holder : Kedar
Account Number : 1001
Balance        : ₹45000.00

Account #2
----------------------------------------
Account Holder : Rahul
Account Number : 1002
Balance        : ₹25000.00

========================================
Total Accounts : 2
========================================
```

---

## 🏦 Main Menu

When the application starts, it displays:

```text
==============================================
   Welcome to Kedar Finance Co-op Bank
          Jalgaon, Maharashtra
==============================================

==============================================
        KEDAR FINANCE CO-OP BANK
           Jalgaon, Maharashtra
==============================================
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Show Account Details
5. Show All Accounts
6. Exit
==============================================
```

---

# 🧑‍💻 OOP Concepts Used

This project uses basic Object-Oriented Programming concepts.

## 1. Class

Two main classes are used:

```python
class AccountHolder:
```

and

```python
class Bank:
```

---

## 2. Object

A bank object is created:

```python
bank = Bank()
```

An account holder object is created when a new account is registered:

```python
account = AccountHolder(name, account_number)
```

---

## 3. Constructor

The `__init__()` method initializes the object.

Example:

```python
def __init__(self, name, account_number, balance=0):
    self.name = name
    self.account_number = account_number
    self.balance = balance
```

---

## 4. Methods

The `AccountHolder` class contains methods such as:

```python
deposit()
withdraw()
show_details()
```

The `Bank` class contains methods such as:

```python
create_account()
find_account()
deposit_money()
withdraw_money()
show_account()
show_all_accounts()
```

---

## 5. List of Objects

The bank stores all account holder objects inside a list:

```python
self.account_holders = []
```

When a new account is created:

```python
self.account_holders.append(account)
```

This allows the application to manage multiple customers.

---

# 📂 Project Structure

The project currently contains one Python file:

```text
Kedar-Finance-Co-op-Bank/
│
├── bank.py
│
└── README.md
```

### `bank.py`

Contains the complete banking application.

### `README.md`

Contains project documentation and instructions.

---

# ⚙️ Requirements

You only need:

* Python 3.x
* Command Prompt / Terminal

No external Python libraries are required.

---

# 🚀 Installation & Setup

## Step 1: Install Python

Make sure Python is installed.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## Step 2: Download or Clone the Project

Place these files in the same folder:

```text
bank.py
README.md
```

---

## Step 3: Open Terminal

Navigate to the project folder.

For example:

```bash
cd Kedar-Finance-Co-op-Bank
```

---

## Step 4: Run the Application

Run:

```bash
python bank.py
```

On some systems:

```bash
python3 bank.py
```

---

# 🧪 Example Workflow

### Create an account

```text
1. Create Account

Enter account holder name: Kedar
Enter account number: 1001
```

### Deposit money

```text
2. Deposit Money

Enter account number: 1001
Enter deposit amount: ₹50000
```

### Withdraw money

```text
3. Withdraw Money

Enter account number: 1001
Enter withdrawal amount: ₹5000
```

### Check account

```text
4. Show Account Details

Enter account number: 1001
```

### View all customers

```text
5. Show All Accounts
```

### Exit

```text
6. Exit
```

---

# 🔐 Current Limitations

This is an **educational OOP project**, not a real banking application.

Currently:

* Account data is stored only in memory.
* Data is lost when the program is closed.
* There is no password or PIN authentication.
* There is no database.
* There is no transaction history.
* There is no money transfer functionality.
* There is no interest calculation.
* There is no admin/customer login system.

---

# 🔮 Future Improvements

The project can be expanded with:

### Level 1

* [ ] Customer PIN
* [ ] Login system
* [ ] Transaction history
* [ ] Change PIN
* [ ] Delete account

### Level 2

* [ ] Transfer money between accounts
* [ ] Account types such as Savings and Current
* [ ] Minimum balance
* [ ] Interest calculation
* [ ] Transaction receipt

### Level 3

* [ ] Save data using JSON
* [ ] SQLite database
* [ ] Database-backed customer management
* [ ] Admin login
* [ ] Customer login
* [ ] Generate bank statements

---

# 🎯 Learning Objectives

This project is useful for practicing:

```text
Python
  │
  ├── Variables
  ├── Input / Output
  ├── if / elif / else
  ├── for loops
  ├── while loops
  ├── Lists
  ├── Functions
  │
  └── Object-Oriented Programming
        │
        ├── Classes
        ├── Objects
        ├── __init__()
        ├── self
        ├── Methods
        └── Objects inside Lists
```

---

# 👨‍💻 Author

**Kedar**

Project:

**Kedar Finance Co-op Bank**

Location:

**Jalgaon, Maharashtra**

---

# ⚠️ Disclaimer

This project is created for **learning and educational purposes only**.

It is a simple demonstration of Python OOP concepts and should **not be used to manage real banking accounts, real customer money, or sensitive financial information**.

---

## 📜 License

This project is intended for educational and personal learning purposes.
