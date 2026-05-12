from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TransactionType2(Enum):
    pass
class TransactionType(Enum):
    pass

############################################
# Definition of Classes
############################################










class DepositTransaction2:

    pass


class TransferTransaction2:

    def __init__(self, targetAccount: str, sourceAccount: str):
        self.targetAccount = targetAccount
        self.sourceAccount = sourceAccount
        
        pass
    @property
    def targetAccount(self):
        return self.__targetAccount
    @targetAccount.setter
    def targetAccount(self, targetAccount: str):
        self.__targetAccount = targetAccount

    @property
    def sourceAccount(self):
        return self.__sourceAccount
    @sourceAccount.setter
    def sourceAccount(self, sourceAccount: str):
        self.__sourceAccount = sourceAccount



class WithdrawTransaction2:

    pass


class ATM_Card2:

    def __init__(self, cardNumber: str, pin: str):
        self.cardNumber = cardNumber
        self.pin = pin
        
        pass
    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def cardNumber(self):
        return self.__cardNumber
    @cardNumber.setter
    def cardNumber(self, cardNumber: str):
        self.__cardNumber = cardNumber



class Transaction2:

    def __init__(self, id: int, type: TransactionType, transactionTime: date, amount: float):
        self.id = id
        self.type = type
        self.transactionTime = transactionTime
        self.amount = amount
        
        pass
    @property
    def transactionTime(self):
        return self.__transactionTime
    @transactionTime.setter
    def transactionTime(self, transactionTime: date):
        self.__transactionTime = transactionTime

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: TransactionType):
        self.__type = type

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id



class Bank2:

    def __init__(self, code: str, address: str):
        self.code = code
        self.address = address
        
        pass
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address



class Savings_Account2:

    def __init__(self, accountNumber: str, balance: int):
        self.accountNumber = accountNumber
        self.balance = balance
        
        pass
    @property
    def accountNumber(self):
        return self.__accountNumber
    @accountNumber.setter
    def accountNumber(self, accountNumber: str):
        self.__accountNumber = accountNumber

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: int):
        self.__balance = balance



class Account2_Interface:

    pass


class Customer2:

    def __init__(self, name: str, dateOfBirth: date, address: str, phoneNumber: str, emailAddress: str):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.address = address
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        
        pass
    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def dateOfBirth(self):
        return self.__dateOfBirth
    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def emailAddress(self):
        return self.__emailAddress
    @emailAddress.setter
    def emailAddress(self, emailAddress: str):
        self.__emailAddress = emailAddress



class DepositTransaction:

    pass


class TransferTransaction:

    def __init__(self, targetAccount: str, sourceAccount: str):
        self.targetAccount = targetAccount
        self.sourceAccount = sourceAccount
        
        pass
    @property
    def targetAccount(self):
        return self.__targetAccount
    @targetAccount.setter
    def targetAccount(self, targetAccount: str):
        self.__targetAccount = targetAccount

    @property
    def sourceAccount(self):
        return self.__sourceAccount
    @sourceAccount.setter
    def sourceAccount(self, sourceAccount: str):
        self.__sourceAccount = sourceAccount



class WithdrawTransaction:

    pass


class ATM_Card:

    def __init__(self, cardNumber: str, pin: str):
        self.cardNumber = cardNumber
        self.pin = pin
        
        pass
    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def cardNumber(self):
        return self.__cardNumber
    @cardNumber.setter
    def cardNumber(self, cardNumber: str):
        self.__cardNumber = cardNumber



class Transaction:

    def __init__(self, id: int, type: TransactionType, transactionTime: date, amount: float):
        self.id = id
        self.type = type
        self.transactionTime = transactionTime
        self.amount = amount
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: TransactionType):
        self.__type = type

    @property
    def transactionTime(self):
        return self.__transactionTime
    @transactionTime.setter
    def transactionTime(self, transactionTime: date):
        self.__transactionTime = transactionTime

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount



class Bank:

    def __init__(self, code: str, address: str):
        self.code = code
        self.address = address
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, code: str):
        self.__code = code



class Savings_Account:

    def __init__(self, accountNumber: str, balance: int):
        self.accountNumber = accountNumber
        self.balance = balance
        
        pass
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: int):
        self.__balance = balance

    @property
    def accountNumber(self):
        return self.__accountNumber
    @accountNumber.setter
    def accountNumber(self, accountNumber: str):
        self.__accountNumber = accountNumber



class Account_Interface:

    pass


class Customer:

    def __init__(self, name: str, dateOfBirth: date, address: str, phoneNumber: str, emailAddress: str):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.address = address
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def dateOfBirth(self):
        return self.__dateOfBirth
    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def emailAddress(self):
        return self.__emailAddress
    @emailAddress.setter
    def emailAddress(self, emailAddress: str):
        self.__emailAddress = emailAddress

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

