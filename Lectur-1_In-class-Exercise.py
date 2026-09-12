from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Not enough balance")

    def balance(self):
        return self.__balance

    @abstractmethod
    def benefit(self):
        pass


class SavingsAccount(Account):

    def benefit(self):
        return self.balance() * 0.05


class CurrentAccount(Account):

    def benefit(self):
        return 10


# Create accounts
a1 = SavingsAccount("Ahmad", 1000)
a2 = CurrentAccount("Ali", 2000)

# Deposit and Withdraw
a1.deposit(500)
a2.withdraw(300)

# Polymorphism
accounts = [a1, a2]

for account in accounts:
    print(account.name)
    print("Balance:", account.balance())
    print("Benefit:", account.benefit())
    print()