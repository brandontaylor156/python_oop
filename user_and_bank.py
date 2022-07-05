class User:
    def __init__(self, first_name, last_name, email, age, int_rate = .02, balance = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.accounts = [BankAccount(int_rate, balance)]

    def addAccount(self, int_rate = .02, balance = 0):
        self.accounts.append(BankAccount(int_rate, balance))
        pass

    def make_deposit(self, amount, accountNumber):
        self.accounts[accountNumber-1].deposit(amount)

    def make_withdrawal(self, amount, accountNumber):
        self.accounts[accountNumber-1].withdraw(amount)

    def display_user_balance(self, accountNumber):
        self.accounts[accountNumber-1].display_account_info()

    def display_user_info(self):
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nAge: {self.age}\nAccounts: {len(self.accounts)}")
        print("\n")
        return self

    def printAllAccountsForUser(self):
        print(f"Printing all accounts for {self.first_name} {self.last_name}:")
        for accountNumber in range(len(self.accounts)):
             print(f"Account {accountNumber+1} - Interest Rate: {self.accounts[accountNumber].int_rate} - Balance: {'${:,.2f}'.format(self.accounts[accountNumber].balance)}")
        print("\n", end="")

    def transferMoney(self, amount, accountNumber, otherUser, otherAccountNumber):
        self.accounts[accountNumber-1].withdraw(amount)
        otherUser.accounts[otherAccountNumber-1].deposit(amount)

class BankAccount:
    all_accounts = []

    def __init__(self, int_rate = .01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append([self.int_rate, self.balance])

    @classmethod
    def printAllAccounts(cls):
        for interest, balance in cls.all_accounts:
            print(interest, '${:,.2f}'.format(balance))

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print('${:,.2f}'.format(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

myUser = User("Brandon", "Taylor", "brandon.david4@outlook.com", 26, .02, 500)
myUser.addAccount(.05, 1000)
myUser.addAccount(.10, 20000)
myUser.printAllAccountsForUser()

transferUser = User("Kobe", "Bryant", "kobe@gmail.com", 24, .99, 24000000)
transferUser.addAccount(.5, 9999999999)
transferUser.addAccount(.4, 8888888888)
transferUser.addAccount(.99, 24)

transferUser.transferMoney(3333, 2, myUser, 1)
myUser.printAllAccountsForUser()
transferUser.printAllAccountsForUser()

