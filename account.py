from datetime import datetime

class Account:
    def __init__(self, balance):
        self.balance = balance
        
def test_account():
    account = Account(100)
    assert account.balance == 100
    
def deposit(account, amount):
    account.balance += amount
    
def test_deposit():
    account = Account(100)
    deposit(account, 55)
    assert account.balance == 155
    
def withdraw(account, amount):
    account.balance -= amount

def test_withdraw():
    account = Account(100)
    withdraw(account, 55)
    assert account.balance ==45
    
def get_balance(self):
    return self.balance
    
    
class savingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
        
    def add_interest(self):
        self.balance += self.balance * self.interest_rate
        
    def automatic_deposit(self, source_account, amount):
        if source_account.balance >= amount:
            source_account.withdraw(amount)
            self>deposit(amount)
            print(f"Automatically deposited {amount} from source account")
        else:
            print(" Transfer failed: insufficient funds")
            
    def withdraw(self, amount):
        if  self.balance >= amount:
            super().withdraw(amount)
        else:
            print("Withdraw failed: insufficient funds")
            
    def deposit(self, amount):
        super().deposit(amount)
        self.transactions.append(f"Deposited:{amount}")
               
    def get_transaction_history(self):
        return self.transactions
    # polymorphism
    def get_balance(self):
        return f"Savings Account Balance: {self.balance}"
    
class Transaction:
    def __init__ (self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()
        
    def process(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
 
class CheckingAccount(Account):
    def __init__(self, balance, overdraft_limit):
         super().__init__(balance)  
         self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
        else:
            print("Withdraw failed: insufficient funds")
            
    def get_balance(self):
        return f"Checking Account Balance: {self.balance}"
    
    # function to print balance using polymorphism
    def print_balance(account):
        print(account.get_balance())
        
        
running = True
while running:
    # create instances of the classes based on user input
    savings_balance = float(input("Enter the initial balance for the savings account: "))
    savings_interest_rate = float(input("Enter the interest rate for the savings account: "))
    savings = savingsAccount(savings_balance, savings_interest_rate)

    checking_balance = float(input("Enter the initial balance for the checking account: "))
    checking_overdraft_limit = float(input("Enter the overdraft limit for the checking account: "))
    checking = CheckingAccount(checking_balance, checking_overdraft_limit)

    # using polymorphism
    checking.print_balance()
    savings.print_balance() 

    print("1. Test account")
    print("2. Test deposit")
    print("3. Test withdraw")
    print("4. Exit")

    choice = input("Enter your choice:")
    
    if choice == '1':
        test_account()
        print("Test account passed")
        
    elif choice == '2':
        test_deposit()
        print("Test deposit passed")
        
    elif choice == '3':
        test_withdraw()
        print("Test withdraw passed")
        
    elif choice == '4':
        running = False
        
    else:
        print("invalid choice")

    

    
    