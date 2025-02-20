#Define the user class
class User:
    def __init__(self, user_id,name,phone):
        self.user_id = user_id #Initialize user account
        self.name = name #init username
        self.phone = phone #init phone no
        self.account=Account(self) #creating an account for the user
    def __repr__(self):
        return f"User({self.user_id},{self.name},{self.phone})"  #representation of the user object
#define account class
class Account:
    def __init__(self, user):
        self.user = user
        self.balance = 0.0
    def deposit(self, amount):
        if amount > 0:                    #check if the deposit is more than zero
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposited Amount must be positive")

    def withdraw(self, amount):
        if 0< amount <=self.balance:  #Check if the withdrawal amount is valid
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient Funds or Invalid amount")

    def __repr__(self):
        return f"Account({self.user.name}, Balance {self.balance})" #Representation of account object
#Define the transaction class
class Transaction:
    def __init__(self, account,amount,transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
    def process(self):
        if self.transaction_type == 'deposit':
            self.account.deposit(self.amount)
        elif self.transaction_type == 'withdraw':
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type")
    def report(self):
        return f"Transaction(Account: {self.account.user.name},Amount : {self.amount}, Type : {self.transaction_type})"


#Example usage // object
user1=User(1, "Robin Murithi",793714666)
print(user1)

#Deposit Amount
user1.account.deposit(1000)

user1.account.withdraw(500)

transaction1=Transaction(user1.account,200, 'deposit')
transaction1.process()


transaction2=Transaction(user1.account,100, 'withdraw')
transaction2.process()

print(user1.account)

user2=User(2, "Alice Naitore",7855555541)
print(user2)
user2.account.deposit(49000)
transaction3=Transaction(user2.account,47000, 'withdraw')
transaction3.process()

print(user2.account)
