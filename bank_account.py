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

account1 = BankAccount(.02, 500)
account2 = BankAccount(.01, 3)

account1.deposit(500).deposit(500).deposit(500).withdraw(200).yield_interest().display_account_info()
account2.deposit(10).deposit(10).withdraw(5).withdraw(5).withdraw(10).withdraw(5).yield_interest().display_account_info()

BankAccount.printAllAccounts()