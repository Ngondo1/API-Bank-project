from datetime import datetime

class Account:
    def __init__(self, account_id, balance):
        self.balance = balance
        self.account_id = account_id
        
def test_account():
    account = Account(100)
    assert account.balance == 100
    
def deposit(account, amount):
    account.balance += amount
    
def test_deposit():
    account = Account(100)
    deposit(account, 55)
    assert account.balance == 155
    
def withdraw(self, amount):
    if self.balance >= amount:
        self.balance -= amount
    else:
        raise ValueError("Insufficient funds")


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
        
class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_id, balance):
        if account_id in self.accounts:
            raise ValueError("Account already exists")
        self.accounts[account_id] = Account(account_id, balance)

    def update_account(self, account_id, balance):
        if account_id not in self.accounts:
            raise ValueError("Account does not exist")
        self.accounts[account_id].balance = balance

    def delete_account(self, account_id):
        if account_id in self.accounts:
            del self.accounts[account_id]
        else:
            raise ValueError("Account does not exist")

    def get_account(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id]
        else:
            raise ValueError("Account does not exist")

    def withdraw_from_account(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id].withdraw(amount)
        else:
            raise ValueError("Account does not exist")

    def __str__(self):
        return "\n".join(str(account) for account in self.accounts.values())

# Example usage
bank = Bank()
bank.add_account("123", 1000)
bank.add_account("456", 2000)
print(bank)
bank.update_account("123", 1500)
print(bank)
bank.delete_account("456")
print(bank)

# exception handling for withdrawal
try:
    bank.withdraw_from_account("123", 2000)
except ValueError as e:
    print(e)
    
            
def main():
    bank = Bank()

    running = True

    while running:
        print("\n1. Add Account")
        print("\n2. Update Account")
        print("\n3. Delete Account")
        print("\n4. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                account_id = input("Enter account ID: ")
                balance = float(input("Enter initial balance: "))
                bank.add_account(account_id, balance)
            elif choice == '2':
                account_id = input("Enter account ID: ")
                balance = float(input("Enter new balance: "))
                bank.update_account(account_id, balance)
            elif choice == '3':
                account_id = input("Enter account ID: ")
                bank.delete_account(account_id)
            elif choice == '4':
                running = False
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()