#keeping track of accounts, line 3.
class BankAccount:
    accounts = []

    def __init__(self, interest_rate, balance=0):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount

    def display_account_info(self):
        print("Balance: $" + "{:.2f}".format(self.balance))

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            print("Interest Rate:", account.interest_rate)
            account.display_account_info()
            print()

# Create two accounts
account_one = BankAccount(interest_rate=0.01, balance=10)
account_two = BankAccount(interest_rate=0.05, balance=50)

#account one transactions
account_one.deposit(10)
account_one.deposit(10)
account_one.deposit(10)
account_one.withdraw(1)
account_one.yield_interest()
account_one.display_account_info()

#account two transactions
account_two.deposit(20)
account_two.deposit(20)
# Withdraw 4 times
for _ in range(4):
    account_two.withdraw(4)
account_two.yield_interest()
account_two.display_account_info()

# Print all accounts (ninja bonus?)
BankAccount.print_all_accounts()
