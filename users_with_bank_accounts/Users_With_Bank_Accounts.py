class BankAccount:
    # this is an object (bank account). it has an interest rate and balance.
    def __init__(self, interest_rate, balance=0):
        self.interest_rate = interest_rate
        self.balance = balance

    # this tracks account deposits
    def deposit(self, amount):
        self.balance += amount

    # this tracks withdraws with a $5 overdraft charge
    def withdraw(self, amount):
        if amount > self.balance:
            print("Acount Overdraft: $5 Overdraft Charge")
            self.balance -= 5
        else:
            self.balance -= amount

    # this is the account balance
    def display_account_info(self):
        print(f"Balance: ${self.balance:.2f}")

    # this is the interest that the account holds
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate

class User:
    # accounts name and email for the user
    def __init__(self, name, email):
        self.name = name
        self.email = email
    #allowing an user to make multiple bank accounts, this keeps track of the accounts.
        self.accounts = []

   #create account
    def create_account(self, interest_rate, balance=0):
        new_account = BankAccount(interest_rate, balance)
        self.accounts.append(new_account)
        return new_account

    # deposit money
    def make_deposit(self, amount, account_index=0):
        if 0 <= account_index < len(self.accounts):
            self.accounts[account_index].deposit(amount)

    # withdraw money
    def make_withdrawal(self, amount, account_index=0):
        if 0 <= account_index < len(self.accounts):
            self.accounts[account_index].withdraw(amount)

    # display balance
    def display_user_balance(self, account_index=0):
        if 0 <= account_index < len(self.accounts):
            print(f"User: {self.name}, Email: {self.email}")
            self.accounts[account_index].display_account_info()

    # user transfer service. (transfer money from one account to any other account)
    def transfer_money(self, amount, other_user, sender_account_index=0, receiver_account_index=0):
        if (0 <= sender_account_index < len(self.accounts) and
                0 <= receiver_account_index < len(other_user.accounts)):
            sender_account = self.accounts[sender_account_index]
            receiver_account = other_user.accounts[receiver_account_index]
            if sender_account.balance >= amount:
                sender_account.withdraw(amount)
                receiver_account.deposit(amount)
                print("Transfer Completed!")
            else:
                print("Insufficient Balance: You do not have enough for this transfer.")

            # account info (name, email, password)
            #couldnt get code to run, had to take out password, i believe it has to do with it not being included in the class
            user1 = User("Johnny", "johnny@example.com")
            user2 = User("Josh", "josh@example.com")

            #create accounts and add balance
            account1 = user1.create_account(interest_rate=0.02, balance=100)
            account2 = user2.create_account(interest_rate=0.02, balance=50)

            # transfer $25
            user1.transfer_money(amount=25, other_user=user2)

            #display current balance
            user1.display_user_balance()
            user2.display_user_balance()
