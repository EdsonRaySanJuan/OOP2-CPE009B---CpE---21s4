"""
        main.py
"""

import Accounts
import ATM

Account1 = Accounts.Accounts(account_number = 123456, account_firstname = "Royce",
                             account_lastname = "Chua", current_balance = 1000,
                             address = "Silver Street Quezon City",
                             email = "roycechua123@gmail.com") #create the instance/object

print("Account 1")
print(Account1.account_firstname)
print(Account1.account_lastname)
print(Account1.current_balance)
print(Account1.address)
print(Account1.email)

print()

Account2 = Accounts.Accounts(account_number = 654321, account_firstname = "John",
                             account_lastname = "Doe", current_balance = 2000,
                             address = "Gold Street Quezon City",
                             email = "johndoe@yahoo.com") #create the instance/object

print("Account 2")
print(Account2.account_firstname)
print(Account2.account_lastname)
print(Account2.current_balance)
print(Account2.address)
print(Account2.email)

# Creating and use an ATM object 
ATM1 = ATM.ATM(serial_number = 9384500000) # 9384500000 is a serial number
ATM1.deposit(Account1, 500)
ATM1.check_currentbalance(Account1)

ATM2 = ATM.ATM(serial_number = 2373100000) # 2373100000 is a serial number
ATM2.deposit(Account2, 500)
ATM2.check_currentbalance(Account2)

ATM1.view_transactionsummary(Account1)
ATM2.view_transactionsummary(Account2)

print('\n')
print(f"{Account1.account_number} Serial Number: ", ATM1.serial_number)
print(f"{Account2.account_number} Serial Number: ", ATM2.serial_number)