from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class account_AccountType(Enum):
    pass
class transaction_TransactionType(Enum):
    pass

############################################
# Definition of Classes
############################################










class transaction_DepositTransaction:

    pass


class transaction_Transaction:

    def __init__(self, type: transaction_TransactionType, time: str, amount: float, sourceAccountNum: str, destinationAccountNum: str, description: str, comment: str, transactionID: str, account0: "account_Account" = None):
        self.type = type
        self.time = time
        self.amount = amount
        self.sourceAccountNum = sourceAccountNum
        self.destinationAccountNum = destinationAccountNum
        self.description = description
        self.comment = comment
        self.transactionID = transactionID
        self.account0 = account0
        
        pass
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
    def comment(self):
        return self.__comment
    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def destinationAccountNum(self):
        return self.__destinationAccountNum
    @destinationAccountNum.setter
    def destinationAccountNum(self, destinationAccountNum: str):
        self.__destinationAccountNum = destinationAccountNum

    @property
    def transactionID(self):
        return self.__transactionID
    @transactionID.setter
    def transactionID(self, transactionID: str):
        self.__transactionID = transactionID

    @property
    def sourceAccountNum(self):
        return self.__sourceAccountNum
    @sourceAccountNum.setter
    def sourceAccountNum(self, sourceAccountNum: str):
        self.__sourceAccountNum = sourceAccountNum

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: transaction_TransactionType):
        self.__type = type

    @property
    def account0(self):
        return self.__account0
    @account0.setter
    def account0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transaction_Transaction__account0", None)
        self.__account0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transaction1"):
                opp_val = getattr(old_value, "transaction1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transaction1"):
                opp_val = getattr(value, "transaction1", None)
                if opp_val is None:
                    setattr(value, "transaction1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class User:

    def __init__(self, userID: str, username: str, password: str, lastLoginTime: str, profile7: "Profile" = None):
        self.userID = userID
        self.username = username
        self.password = password
        self.lastLoginTime = lastLoginTime
        self.profile7 = profile7
        
        pass
    @property
    def lastLoginTime(self):
        return self.__lastLoginTime
    @lastLoginTime.setter
    def lastLoginTime(self, lastLoginTime: str):
        self.__lastLoginTime = lastLoginTime

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def profile7(self):
        return self.__profile7
    @profile7.setter
    def profile7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__profile7", None)
        self.__profile7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user6"):
                opp_val = getattr(old_value, "user6", None)
                if opp_val == self:
                    setattr(old_value, "user6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user6"):
                opp_val = getattr(value, "user6", None)
                setattr(value, "user6", self)



class Profile:

    def __init__(self, userID: str, firstname: str, lastname: str, dateOfBirth: date, address1: str, address2: str, city: str, state: str, country: str, zipcode: str, phoneNumber: str, email: str, IDType: int, IDNum: str, user6: "User" = None, account8: set["account_Account"] = None):
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
        self.user6 = user6
        self.account8 = account8 if account8 is not None else set()
        
        pass
    @property
    def IDType(self):
        return self.__IDType
    @IDType.setter
    def IDType(self, IDType: int):
        self.__IDType = IDType

    @property
    def address1(self):
        return self.__address1
    @address1.setter
    def address1(self, address1: str):
        self.__address1 = address1

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def firstname(self):
        return self.__firstname
    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def zipcode(self):
        return self.__zipcode
    @zipcode.setter
    def zipcode(self, zipcode: str):
        self.__zipcode = zipcode

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID

    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def lastname(self):
        return self.__lastname
    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def IDNum(self):
        return self.__IDNum
    @IDNum.setter
    def IDNum(self, IDNum: str):
        self.__IDNum = IDNum

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def address2(self):
        return self.__address2
    @address2.setter
    def address2(self, address2: str):
        self.__address2 = address2

    @property
    def dateOfBirth(self):
        return self.__dateOfBirth
    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def user6(self):
        return self.__user6
    @user6.setter
    def user6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Profile__user6", None)
        self.__user6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile7"):
                opp_val = getattr(old_value, "profile7", None)
                if opp_val == self:
                    setattr(old_value, "profile7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile7"):
                opp_val = getattr(value, "profile7", None)
                setattr(value, "profile7", self)

    @property
    def account8(self):
        return self.__account8
    @account8.setter
    def account8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Profile__account8", None)
        self.__account8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "profile9"):
                    opp_val = getattr(item, "profile9", None)
                    
                    if opp_val == self:
                        setattr(item, "profile9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "profile9"):
                    opp_val = getattr(item, "profile9", None)
                    
                    setattr(item, "profile9", self)
                    



class account_Account:

    def __init__(self, userID: str, accountNum: str, type: account_AccountType, pin: str, balance: float, transaction1: set["transaction_Transaction"] = None, profile9: "Profile" = None):
        self.userID = userID
        self.accountNum = accountNum
        self.type = type
        self.pin = pin
        self.balance = balance
        self.transaction1 = transaction1 if transaction1 is not None else set()
        self.profile9 = profile9
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: account_AccountType):
        self.__type = type

    @property
    def accountNum(self):
        return self.__accountNum
    @accountNum.setter
    def accountNum(self, accountNum: str):
        self.__accountNum = accountNum

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID

    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def transaction1(self):
        return self.__transaction1
    @transaction1.setter
    def transaction1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_account_Account__transaction1", None)
        self.__transaction1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account0"):
                    opp_val = getattr(item, "account0", None)
                    
                    if opp_val == self:
                        setattr(item, "account0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account0"):
                    opp_val = getattr(item, "account0", None)
                    
                    setattr(item, "account0", self)
                    

    @property
    def profile9(self):
        return self.__profile9
    @profile9.setter
    def profile9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_account_Account__profile9", None)
        self.__profile9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account8"):
                opp_val = getattr(old_value, "account8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account8"):
                opp_val = getattr(value, "account8", None)
                if opp_val is None:
                    setattr(value, "account8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



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

    def __init__(self, accountNum: str, name: str, address1: str, address2: str, city: str, state: str, country: str, zipcode: str, phoneNum: str, email: str, paybillsTransaction5: set["transaction_PaybillsTransaction"] = None):
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
        self.paybillsTransaction5 = paybillsTransaction5 if paybillsTransaction5 is not None else set()
        
        pass
    @property
    def phoneNum(self):
        return self.__phoneNum
    @phoneNum.setter
    def phoneNum(self, phoneNum: str):
        self.__phoneNum = phoneNum

    @property
    def accountNum(self):
        return self.__accountNum
    @accountNum.setter
    def accountNum(self, accountNum: str):
        self.__accountNum = accountNum

    @property
    def address2(self):
        return self.__address2
    @address2.setter
    def address2(self, address2: str):
        self.__address2 = address2

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def zipcode(self):
        return self.__zipcode
    @zipcode.setter
    def zipcode(self, zipcode: str):
        self.__zipcode = zipcode

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def address1(self):
        return self.__address1
    @address1.setter
    def address1(self, address1: str):
        self.__address1 = address1

    @property
    def paybillsTransaction5(self):
        return self.__paybillsTransaction5
    @paybillsTransaction5.setter
    def paybillsTransaction5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transaction_Payee__paybillsTransaction5", None)
        self.__paybillsTransaction5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "payee4"):
                    opp_val = getattr(item, "payee4", None)
                    
                    if opp_val == self:
                        setattr(item, "payee4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "payee4"):
                    opp_val = getattr(item, "payee4", None)
                    
                    setattr(item, "payee4", self)
                    



class transaction_ExternalAccount:

    def __init__(self, routingNum: str, accountNum: str, associatedAccount: str, transferTransaction3: set["transaction_TransferTransaction"] = None):
        self.routingNum = routingNum
        self.accountNum = accountNum
        self.associatedAccount = associatedAccount
        self.transferTransaction3 = transferTransaction3 if transferTransaction3 is not None else set()
        
        pass
    @property
    def associatedAccount(self):
        return self.__associatedAccount
    @associatedAccount.setter
    def associatedAccount(self, associatedAccount: str):
        self.__associatedAccount = associatedAccount

    @property
    def routingNum(self):
        return self.__routingNum
    @routingNum.setter
    def routingNum(self, routingNum: str):
        self.__routingNum = routingNum

    @property
    def accountNum(self):
        return self.__accountNum
    @accountNum.setter
    def accountNum(self, accountNum: str):
        self.__accountNum = accountNum

    @property
    def transferTransaction3(self):
        return self.__transferTransaction3
    @transferTransaction3.setter
    def transferTransaction3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transaction_ExternalAccount__transferTransaction3", None)
        self.__transferTransaction3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "externalAccount2"):
                    opp_val = getattr(item, "externalAccount2", None)
                    
                    if opp_val == self:
                        setattr(item, "externalAccount2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "externalAccount2"):
                    opp_val = getattr(item, "externalAccount2", None)
                    
                    setattr(item, "externalAccount2", self)
                    



class transaction_PaybillsTransaction:

    pass


class transaction_TransferTransaction:

    pass
