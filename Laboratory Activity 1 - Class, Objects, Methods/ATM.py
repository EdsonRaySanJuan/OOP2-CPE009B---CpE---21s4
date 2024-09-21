"""
        ATM.py
"""

class ATM():
    def __init__(self, serial_number):  # Constructor Function
        self.serial_number = serial_number
        self.transaction_log = []  # List to store transaction summaries
    
    def deposit(self, account, amount):
        account.current_balance = account.current_balance + amount
        self.transaction_log.append(f"{account.account_number} Deposited Amount: {amount}")
        print(f"\nAccount {account.account_number} Deposit Complete")
        print("Amount: ", amount)
        
    def withdraw(self, account, amount):
        if account.current_balance >= amount:
            account.current_balance = account.current_balance - amount
            self.transaction_log.append(f"{account.account_number} Withdraw Amount: {amount}")
            print(f"\nAccount {account.account_number} Withdraw Complete")
            print("Amount: ", amount)
        else:
            print(f"Account {account.account_number} Insufficient Balance.")
    
    def check_currentbalance(self, account):
        self.transaction_log.append(f"{account.account_number} New Balance: {account.current_balance}")
        
    def view_transactionsummary(self, account):
        print(f"\n{account.account_number} Transaction History:")
        if self.transaction_log:
            for transaction in self.transaction_log:
                print(transaction)
        else:
            print("No Transaction History")
            
            