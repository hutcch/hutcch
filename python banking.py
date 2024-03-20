import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self):
        self.accounts = {}  # Dictionary to store accounts

    def add_account(self, account_number, account_holder, balance=0):
        # Create a new account and add it to the dictionary
        account = {
            "account_number": account_number,
            "account_holder": account_holder,
            "balance": balance
        }
        self.accounts[account_number] = account

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            if amount > 0:
                self.accounts[account_number]["balance"] += amount
                return f"Deposited {amount} CAD. New balance: {self.accounts[account_number]['balance']} CAD"
            else:
                return "Invalid deposit amount. Please enter a positive value."
        else:
            return "Account not found."

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount > 0 and amount <= self.accounts[account_number]["balance"]:
                self.accounts[account_number]["balance"] -= amount
                return f"Withdrew {amount} CAD. New balance: {self.accounts[account_number]['balance']} CAD"
            else:
                return "Invalid withdrawal amount. Insufficient balance."
        else:
            return "Account not found."

    def display_balance(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            return f"Account holder: {account['account_holder']}\nAccount number: {account['account_number']}\nCurrent balance: {account['balance']} CAD"
        else:
            return "Account not found."

class BankingAppUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Banking Application")
        self.root.geometry("400x300")

        self.account = BankAccount()

        self.label = tk.Label(root, text="Welcome to Simple Banking App", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.create_button = tk.Button(root, text="Create Account", command=self.create_account)
        self.create_button.pack()

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

        self.balance_button = tk.Button(root, text="Display Balance", command=self.display_balance)
        self.balance_button.pack()

    def create_account(self):
        account_number = input("Enter account number: ")
        account_holder = input("Enter account holder name: ")
        initial_balance = float(input("Enter initial balance: "))
        self.account.add_account(account_number, account_holder, initial_balance)
        messagebox.showinfo("Account Created", f"Account {account_number} created successfully!")

    def deposit(self):
        account_number = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        result = self.account.deposit(account_number, amount)
        messagebox.showinfo("Deposit Result", result)

    def withdraw(self):
        account_number = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))
        result = self.account.withdraw(account_number, amount)
        messagebox.showinfo("Withdrawal Result", result)

    def display_balance(self):
        account_number = input("Enter account number: ")
        result = self.account.display_balance(account_number)
        messagebox.showinfo("Account Details", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingAppUI(root)
    root.mainloop()


