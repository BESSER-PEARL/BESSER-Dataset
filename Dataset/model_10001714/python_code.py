from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TransactionType(Enum):
    pass
class EnumAccountType(Enum):
    pass

############################################
# Definition of Classes
############################################










class Account:

    def __init__(self, accountNo: int, PIN: int, accountType: EnumAccountType, openedDate: str, availableBalance: str):
        self.accountNo = accountNo
        self.PIN = PIN
        self.accountType = accountType
        self.openedDate = openedDate
        self.availableBalance = availableBalance
        
        pass
    @property
    def accountType(self):
        return self.__accountType
    @accountType.setter
    def accountType(self, accountType: EnumAccountType):
        self.__accountType = accountType

    @property
    def accountNo(self):
        return self.__accountNo
    @accountNo.setter
    def accountNo(self, accountNo: int):
        self.__accountNo = accountNo

    @property
    def PIN(self):
        return self.__PIN
    @PIN.setter
    def PIN(self, PIN: int):
        self.__PIN = PIN

    @property
    def availableBalance(self):
        return self.__availableBalance
    @availableBalance.setter
    def availableBalance(self, availableBalance: str):
        self.__availableBalance = availableBalance

    @property
    def openedDate(self):
        return self.__openedDate
    @openedDate.setter
    def openedDate(self, openedDate: str):
        self.__openedDate = openedDate



class IcalculateExtraFee_Interface:

    pass


class savingAccount:

    def __init__(self, annualInterestRate: str, annualGain: str, extraFee: str):
        self.annualInterestRate = annualInterestRate
        self.annualGain = annualGain
        self.extraFee = extraFee
        
        pass
    @property
    def annualGain(self):
        return self.__annualGain
    @annualGain.setter
    def annualGain(self, annualGain: str):
        self.__annualGain = annualGain

    @property
    def extraFee(self):
        return self.__extraFee
    @extraFee.setter
    def extraFee(self, extraFee: str):
        self.__extraFee = extraFee

    @property
    def annualInterestRate(self):
        return self.__annualInterestRate
    @annualInterestRate.setter
    def annualInterestRate(self, annualInterestRate: str):
        self.__annualInterestRate = annualInterestRate



class checkingAccount:

    def __init__(self, accountNo: int, noOfTransactions: int):
        self.accountNo = accountNo
        self.noOfTransactions = noOfTransactions
        
        pass
    @property
    def noOfTransactions(self):
        return self.__noOfTransactions
    @noOfTransactions.setter
    def noOfTransactions(self, noOfTransactions: int):
        self.__noOfTransactions = noOfTransactions

    @property
    def accountNo(self):
        return self.__accountNo
    @accountNo.setter
    def accountNo(self, accountNo: int):
        self.__accountNo = accountNo



class Transaction:

    def __init__(self, accountNo: int, transactionId: int, description: str, transactionDate: str, amount: str, transactionType: TransactionType):
        self.accountNo = accountNo
        self.transactionId = transactionId
        self.description = description
        self.transactionDate = transactionDate
        self.amount = amount
        self.transactionType = transactionType
        
        pass
    @property
    def transactionId(self):
        return self.__transactionId
    @transactionId.setter
    def transactionId(self, transactionId: int):
        self.__transactionId = transactionId

    @property
    def transactionDate(self):
        return self.__transactionDate
    @transactionDate.setter
    def transactionDate(self, transactionDate: str):
        self.__transactionDate = transactionDate

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def accountNo(self):
        return self.__accountNo
    @accountNo.setter
    def accountNo(self, accountNo: int):
        self.__accountNo = accountNo

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def transactionType(self):
        return self.__transactionType
    @transactionType.setter
    def transactionType(self, transactionType: TransactionType):
        self.__transactionType = transactionType



class Customer:

    def __init__(self, custId: int, accountNo: int, firstName: str, lastName: str, address: str):
        self.custId = custId
        self.accountNo = accountNo
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        
        pass
    @property
    def lastName(self):
        return self.__lastName
    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def custId(self):
        return self.__custId
    @custId.setter
    def custId(self, custId: int):
        self.__custId = custId

    @property
    def firstName(self):
        return self.__firstName
    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def accountNo(self):
        return self.__accountNo
    @accountNo.setter
    def accountNo(self, accountNo: int):
        self.__accountNo = accountNo

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

