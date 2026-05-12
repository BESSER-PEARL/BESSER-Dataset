from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class account_AccountType(Enum):
    pass
class UserGroup(Enum):
    pass
class transaction_TransactionType(Enum):
    pass

############################################
# Definition of Classes
############################################










class account_Account:

    def __init__(self, userID: str, accountNum: str, type: account_AccountType, pin: str, balance: float, transactions0: set["transaction_Transaction"] = None):
        self.userID = userID
        self.accountNum = accountNum
        self.type = type
        self.pin = pin
        self.balance = balance
        self.transactions0 = transactions0 if transactions0 is not None else set()
        
        pass
    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: account_AccountType):
        self.__type = type

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance

    @property
    def accountNum(self):
        return self.__accountNum
    @accountNum.setter
    def accountNum(self, accountNum: str):
        self.__accountNum = accountNum

    @property
    def transactions0(self):
        return self.__transactions0
    @transactions0.setter
    def transactions0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_account_Account__transactions0", None)
        self.__transactions0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account1"):
                    opp_val = getattr(item, "account1", None)
                    
                    if opp_val == self:
                        setattr(item, "account1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account1"):
                    opp_val = getattr(item, "account1", None)
                    
                    setattr(item, "account1", self)
                    



class account_SavingsAccount:

    def __init__(self, interestRate: float):
        self.interestRate = interestRate
        
        pass
    @property
    def interestRate(self):
        return self.__interestRate
    @interestRate.setter
    def interestRate(self, interestRate: float):
        self.__interestRate = interestRate



class transaction_Payee:

    def __init__(self, accountNum: str, name: str, address1: str, address2: str, city: str, state: str, country: str, zipcode: str, phoneNum: str, email: str):
        self.accountNum = accountNum
        self.name = name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode
        self.phoneNum = phoneNum
        self.email = email
        
        pass
    @property
    def address2(self):
        return self.__address2
    @address2.setter
    def address2(self, address2: str):
        self.__address2 = address2

    @property
    def accountNum(self):
        return self.__accountNum
    @accountNum.setter
    def accountNum(self, accountNum: str):
        self.__accountNum = accountNum

    @property
    def address1(self):
        return self.__address1
    @address1.setter
    def address1(self, address1: str):
        self.__address1 = address1

    @property
    def zipcode(self):
        return self.__zipcode
    @zipcode.setter
    def zipcode(self, zipcode: str):
        self.__zipcode = zipcode

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def phoneNum(self):
        return self.__phoneNum
    @phoneNum.setter
    def phoneNum(self, phoneNum: str):
        self.__phoneNum = phoneNum

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class transaction_ExternalAccount:

    def __init__(self, routingNum: str, accountNum: str, associatedAccount: str):
        self.routingNum = routingNum
        self.accountNum = accountNum
        self.associatedAccount = associatedAccount
        
        pass
    @property
    def accountNum(self):
        return self.__accountNum
    @accountNum.setter
    def accountNum(self, accountNum: str):
        self.__accountNum = accountNum

    @property
    def routingNum(self):
        return self.__routingNum
    @routingNum.setter
    def routingNum(self, routingNum: str):
        self.__routingNum = routingNum

    @property
    def associatedAccount(self):
        return self.__associatedAccount
    @associatedAccount.setter
    def associatedAccount(self, associatedAccount: str):
        self.__associatedAccount = associatedAccount



class transaction_PaybillsTransaction:

    pass


class transaction_TransferTransaction:

    pass


class transaction_DepositTransaction:

    pass


class transaction_Transaction:

    def __init__(self, transactionID: str, type: transaction_TransactionType, time: str, amount: float, sourceAccountNum: str, destinationAccountNum: str, description: str, comment: str, account1: "account_Account" = None):
        self.transactionID = transactionID
        self.type = type
        self.time = time
        self.amount = amount
        self.sourceAccountNum = sourceAccountNum
        self.destinationAccountNum = destinationAccountNum
        self.description = description
        self.comment = comment
        self.account1 = account1
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: transaction_TransactionType):
        self.__type = type

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def destinationAccountNum(self):
        return self.__destinationAccountNum
    @destinationAccountNum.setter
    def destinationAccountNum(self, destinationAccountNum: str):
        self.__destinationAccountNum = destinationAccountNum

    @property
    def sourceAccountNum(self):
        return self.__sourceAccountNum
    @sourceAccountNum.setter
    def sourceAccountNum(self, sourceAccountNum: str):
        self.__sourceAccountNum = sourceAccountNum

    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def transactionID(self):
        return self.__transactionID
    @transactionID.setter
    def transactionID(self, transactionID: str):
        self.__transactionID = transactionID

    @property
    def account1(self):
        return self.__account1
    @account1.setter
    def account1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transaction_Transaction__account1", None)
        self.__account1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transactions0"):
                opp_val = getattr(old_value, "transactions0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transactions0"):
                opp_val = getattr(value, "transactions0", None)
                if opp_val is None:
                    setattr(value, "transactions0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class User:

    def __init__(self, userID: str, username: str, password: str, lastLoginTime: str, userRole: str):
        self.userID = userID
        self.username = username
        self.password = password
        self.lastLoginTime = lastLoginTime
        self.userRole = userRole
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID

    @property
    def lastLoginTime(self):
        return self.__lastLoginTime
    @lastLoginTime.setter
    def lastLoginTime(self, lastLoginTime: str):
        self.__lastLoginTime = lastLoginTime

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def userRole(self):
        return self.__userRole
    @userRole.setter
    def userRole(self, userRole: str):
        self.__userRole = userRole



class Profile:

    def __init__(self, userID: str, firstname: str, lastname: str, dateOfBirth: date, address1: str, address2: str, city: str, state: str, country: str, zipcode: str, phoneNumber: str, email: str, IDType: int, IDNum: str):
        self.userID = userID
        self.firstname = firstname
        self.lastname = lastname
        self.dateOfBirth = dateOfBirth
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode
        self.phoneNumber = phoneNumber
        self.email = email
        self.IDType = IDType
        self.IDNum = IDNum
        
        pass
    @property
    def zipcode(self):
        return self.__zipcode
    @zipcode.setter
    def zipcode(self, zipcode: str):
        self.__zipcode = zipcode

    @property
    def firstname(self):
        return self.__firstname
    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def lastname(self):
        return self.__lastname
    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID

    @property
    def address1(self):
        return self.__address1
    @address1.setter
    def address1(self, address1: str):
        self.__address1 = address1

    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def IDType(self):
        return self.__IDType
    @IDType.setter
    def IDType(self, IDType: int):
        self.__IDType = IDType

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def dateOfBirth(self):
        return self.__dateOfBirth
    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def IDNum(self):
        return self.__IDNum
    @IDNum.setter
    def IDNum(self, IDNum: str):
        self.__IDNum = IDNum

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def address2(self):
        return self.__address2
    @address2.setter
    def address2(self, address2: str):
        self.__address2 = address2

