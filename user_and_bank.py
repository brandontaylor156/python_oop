class User:
    all_accounts = []

    def __init__(self, first_name, last_name, email, age, int_rate = .02, balance = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.account = BankAccount(int_rate, balance)

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        self.account.display_account_info()

    def display_info(self):
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nAge: {self.age}")
        print("\n")
        return self


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
myUser.display_user_balance()