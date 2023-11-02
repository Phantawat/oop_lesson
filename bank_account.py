class BankAccount:
    def __init__(self, accountID, balance):
        self.account_ID = accountID
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount and amount > 0:
            self.balance -= amount
        else:
            raise ValueError

    def __str__(self):
        return f'ID: {self.account_ID}, Balance: {self.balance:.2f}'
