from datetime import datetime

class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account {self.account_id}: Balance = {self.balance}"

def test_account():
    account = Account("001", 100)
    assert account.balance == 100

def test_deposit():
    account = Account("001", 100)
    account.deposit(55)
    assert account.balance == 155

def test_withdraw():
    account = Account("001", 100)
    account.withdraw(55)
    assert account.balance == 45
    
account = Account(account_id="001", balance=1000)

class SavingsAccount(Account):
    def __init__(self, account_id, balance, interest_rate):
        super().__init__(account_id, balance)
        self.interest_rate = interest_rate
        self.transactions = []

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Interest added: {interest}")

    def automatic_deposit(self, source_account, amount):
        if source_account.balance >= amount:
            source_account.withdraw(amount)
            self.deposit(amount)
            print(f"Automatically deposited {amount} from source account")
        else:
            print("Transfer failed: insufficient funds")

    def get_transaction_history(self):
        return self.transactions

    def get_balance(self):
        return f"Savings Account Balance: {self.balance}"
    
nyakio = SavingsAccount(account_id="001", balance=1000, interest_rate=0.05)
ngondo = SavingsAccount(account_id="002", balance=2000, interest_rate=0.05)

class CheckingAccount(Account):
    def __init__(self, account_id, balance, overdraft_limit):
        super().__init__(account_id, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
        else:
            print("Withdrawal failed: insufficient funds")

    def get_balance(self):
        return f"Checking Account Balance: {self.balance}"

class Transaction(Account):
    def __init__(self, account_id, balance, amount, transaction_type):
        super().__init__(account_id, balance)
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def process(self):
        if self.transaction_type == "deposit":
            account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            account.withdraw(self.amount)
        else:
            raise ValueError("Invalid transaction type")
transaction = Transaction(account_id="001", balance=1000, amount=500, transaction_type="withdraw")

class Bank(Account):
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

# Exception handling for withdrawal
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
        print("\n4. Transact")
        print("\n5. Exit")

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
            elif choice == '5':
                running = False
            elif choice == '4':
                account_id = input("Enter account ID for transaction: ")
                amount = float(input("Enter amount for transaction: "))
                transaction_type = input("Enter transaction type (deposit/withdraw): ")
                
                if account_id not in bank.accounts:
                    print("Account does not exist.")
                    continue
                
                account = bank.get_account(account_id)
                transaction = Transaction(account_id=account_id, balance=account.get_balance(), amount=amount, transaction_type=transaction_type)
                
                try:
                    transaction.process()
                    print(f"Transaction successful. New balance: {account.get_balance()}")
                except ValueError as e:
                    print(e)

                
            
                
                
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
