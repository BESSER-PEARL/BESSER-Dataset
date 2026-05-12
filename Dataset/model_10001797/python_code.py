from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class FixedAccount:

    pass


class SavingsAccount:

    pass


class BankAccount:

    def __init__(self, balance: float, accountHolderName: str):
        self.balance = balance
        self.accountHolderName = accountHolderName
        
        pass
    @property
    def accountHolderName(self):
        return self.__accountHolderName
    @accountHolderName.setter
    def accountHolderName(self, accountHolderName: str):
        self.__accountHolderName = accountHolderName

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance

