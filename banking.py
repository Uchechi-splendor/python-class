"""
Bank-Name == AfrikMoney
Transaction
Withdrawl
Transfer
Deposit
Bills

Customer Service
Check account balance
Open account
Statement of Account
ATM/Cheque
"""

class Afrikmoney:
    greet ='welcome to AFRIKMONEY'
    def __init__(self, greet, acc_name):
        self.greet = greet
        self.acc_name = acc_name
class Afrikmoney:
    greet ='welcome to AFRIKMONEY'
    print(greet)

class Customer_service(Afrikmoney):
    def open_account(self):
        first_name = input('enter your first Name:')
        last = input('enter your last Name:')
        Phone_Number = int(input('enter your  phone Number:'))
        if len(Phone_Number) == 11:
            print('✅')
        else:
            print('Invalid Phone Number.')
            return Phone_Number()
        address = input('enter your adress:')
        d_o_b = input('enter your date of birth:')
        age = int(input('enter your age'))
        if age >=18:
            print('procced to the next step.')
        else:
            print("you're not eligible to open an account")
            exit()
david = Afrikmoney
print(david.greet)
david =Customer_service
david.open_account



