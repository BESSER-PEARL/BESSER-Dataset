from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class loan_ApplicationStatus(Enum):
    pass
class TransactionType(Enum):
    pass
class account_AccountType(Enum):
    pass
class transaction_TransactionType(Enum):
    pass
class loan_LoanStatus(Enum):
    pass
class loan_LoanType(Enum):
    pass

############################################
# Definition of Classes
############################################










class transaction_ExternalAccount:

    def __init__(self, routingNum: str, accountNum: str, associatedAccount: str, transferTransaction3: set["transaction_TransferTransaction"] = None):
        self.routingNum = routingNum
        self.accountNum = accountNum
        self.associatedAccount = associatedAccount
        self.transferTransaction3 = transferTransaction3 if transferTransaction3 is not None else set()
        
        pass
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
    def associatedAccount(self):
        return self.__associatedAccount
    @associatedAccount.setter
    def associatedAccount(self, associatedAccount: str):
        self.__associatedAccount = associatedAccount

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


class transaction_DepositTransaction:

    pass


class transaction_Transaction:

    def __init__(self, transactionID: str, type: transaction_TransactionType, time: str, amount: float, sourceAccountNum: str, destinationAccountNum: str, description: str, comment: str, account0: "account_Account" = None):
        self.transactionID = transactionID
        self.type = type
        self.time = time
        self.amount = amount
        self.sourceAccountNum = sourceAccountNum
        self.destinationAccountNum = destinationAccountNum
        self.description = description
        self.comment = comment
        self.account0 = account0
        
        pass
    @property
    def destinationAccountNum(self):
        return self.__destinationAccountNum
    @destinationAccountNum.setter
    def destinationAccountNum(self, destinationAccountNum: str):
        self.__destinationAccountNum = destinationAccountNum

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
    def sourceAccountNum(self):
        return self.__sourceAccountNum
    @sourceAccountNum.setter
    def sourceAccountNum(self, sourceAccountNum: str):
        self.__sourceAccountNum = sourceAccountNum

    @property
    def transactionID(self):
        return self.__transactionID
    @transactionID.setter
    def transactionID(self, transactionID: str):
        self.__transactionID = transactionID

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

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
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

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

    def __init__(self, userID: str, firstname: str, lastname: str, dateOfBirth: date, address1: str, address2: str, city: str, state: str, country: str, zipcode: str, phoneNumber: str, email: str, IDType: int, IDNum: str, user6: "User" = None, account8: set["account_Account"] = None, loanApplication14: set["loan_LoanApplication"] = None):
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
        self.loanApplication14 = loanApplication14 if loanApplication14 is not None else set()
        
        pass
    @property
    def IDNum(self):
        return self.__IDNum
    @IDNum.setter
    def IDNum(self, IDNum: str):
        self.__IDNum = IDNum

    @property
    def zipcode(self):
        return self.__zipcode
    @zipcode.setter
    def zipcode(self, zipcode: str):
        self.__zipcode = zipcode

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: str):
        self.__state = state

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
    def dateOfBirth(self):
        return self.__dateOfBirth
    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def IDType(self):
        return self.__IDType
    @IDType.setter
    def IDType(self, IDType: int):
        self.__IDType = IDType

    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def address1(self):
        return self.__address1
    @address1.setter
    def address1(self, address1: str):
        self.__address1 = address1

    @property
    def address2(self):
        return self.__address2
    @address2.setter
    def address2(self, address2: str):
        self.__address2 = address2

    @property
    def loanApplication14(self):
        return self.__loanApplication14
    @loanApplication14.setter
    def loanApplication14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Profile__loanApplication14", None)
        self.__loanApplication14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "profile15"):
                    opp_val = getattr(item, "profile15", None)
                    
                    if opp_val == self:
                        setattr(item, "profile15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "profile15"):
                    opp_val = getattr(item, "profile15", None)
                    
                    setattr(item, "profile15", self)
                    

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
                    



class ExternalAccount:

    def __init__(self, routingNum: str, accountNum: str, associatedAccount: str, transferTransaction20: set["TransferTransaction"] = None, account22: "Account2" = None):
        self.routingNum = routingNum
        self.accountNum = accountNum
        self.associatedAccount = associatedAccount
        self.transferTransaction20 = transferTransaction20 if transferTransaction20 is not None else set()
        self.account22 = account22
        
        pass
    @property
    def associatedAccount(self):
        return self.__associatedAccount
    @associatedAccount.setter
    def associatedAccount(self, associatedAccount: str):
        self.__associatedAccount = associatedAccount

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
    def transferTransaction20(self):
        return self.__transferTransaction20
    @transferTransaction20.setter
    def transferTransaction20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ExternalAccount__transferTransaction20", None)
        self.__transferTransaction20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "externalAccount21"):
                    opp_val = getattr(item, "externalAccount21", None)
                    
                    if opp_val == self:
                        setattr(item, "externalAccount21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "externalAccount21"):
                    opp_val = getattr(item, "externalAccount21", None)
                    
                    setattr(item, "externalAccount21", self)
                    

    @property
    def account22(self):
        return self.__account22
    @account22.setter
    def account22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ExternalAccount__account22", None)
        self.__account22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "externalAccount23"):
                opp_val = getattr(old_value, "externalAccount23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "externalAccount23"):
                opp_val = getattr(value, "externalAccount23", None)
                if opp_val is None:
                    setattr(value, "externalAccount23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class TransferTransaction:

    pass


class Transaction3:

    def __init__(self, amount: float, sourceAccountNum: str, destinationAccountNum: str, description: str, comment: str, transactionID: str, type: transaction_TransactionType, time: str, account18: "Account2" = None):
        self.amount = amount
        self.sourceAccountNum = sourceAccountNum
        self.destinationAccountNum = destinationAccountNum
        self.description = description
        self.comment = comment
        self.transactionID = transactionID
        self.type = type
        self.time = time
        self.account18 = account18
        
        pass
    @property
    def destinationAccountNum(self):
        return self.__destinationAccountNum
    @destinationAccountNum.setter
    def destinationAccountNum(self, destinationAccountNum: str):
        self.__destinationAccountNum = destinationAccountNum

    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def sourceAccountNum(self):
        return self.__sourceAccountNum
    @sourceAccountNum.setter
    def sourceAccountNum(self, sourceAccountNum: str):
        self.__sourceAccountNum = sourceAccountNum

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
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def transactionID(self):
        return self.__transactionID
    @transactionID.setter
    def transactionID(self, transactionID: str):
        self.__transactionID = transactionID

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: transaction_TransactionType):
        self.__type = type

    @property
    def account18(self):
        return self.__account18
    @account18.setter
    def account18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Transaction3__account18", None)
        self.__account18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transaction19"):
                opp_val = getattr(old_value, "transaction19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transaction19"):
                opp_val = getattr(value, "transaction19", None)
                if opp_val is None:
                    setattr(value, "transaction19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Account2:

    def __init__(self, userID: str, accountNum: str, type: account_AccountType, pin: str, balance: float, transaction19: set["Transaction3"] = None, externalAccount23: set["ExternalAccount"] = None):
        self.userID = userID
        self.accountNum = accountNum
        self.type = type
        self.pin = pin
        self.balance = balance
        self.transaction19 = transaction19 if transaction19 is not None else set()
        self.externalAccount23 = externalAccount23 if externalAccount23 is not None else set()
        
        pass
    @property
    def accountNum(self):
        return self.__accountNum
    @accountNum.setter
    def accountNum(self, accountNum: str):
        self.__accountNum = accountNum

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: account_AccountType):
        self.__type = type

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance

    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID

    @property
    def transaction19(self):
        return self.__transaction19
    @transaction19.setter
    def transaction19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account2__transaction19", None)
        self.__transaction19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account18"):
                    opp_val = getattr(item, "account18", None)
                    
                    if opp_val == self:
                        setattr(item, "account18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account18"):
                    opp_val = getattr(item, "account18", None)
                    
                    setattr(item, "account18", self)
                    

    @property
    def externalAccount23(self):
        return self.__externalAccount23
    @externalAccount23.setter
    def externalAccount23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account2__externalAccount23", None)
        self.__externalAccount23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account22"):
                    opp_val = getattr(item, "account22", None)
                    
                    if opp_val == self:
                        setattr(item, "account22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account22"):
                    opp_val = getattr(item, "account22", None)
                    
                    setattr(item, "account22", self)
                    



class Transaction1:

    def __init__(self, transactionID: str, type: transaction_TransactionType, time: str, amount: float, sourceAccountNum: str, destinationAccountNum: str, description: str, comment: str, account16: "Account1" = None):
        self.transactionID = transactionID
        self.type = type
        self.time = time
        self.amount = amount
        self.sourceAccountNum = sourceAccountNum
        self.destinationAccountNum = destinationAccountNum
        self.description = description
        self.comment = comment
        self.account16 = account16
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: transaction_TransactionType):
        self.__type = type

    @property
    def transactionID(self):
        return self.__transactionID
    @transactionID.setter
    def transactionID(self, transactionID: str):
        self.__transactionID = transactionID

    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

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
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def destinationAccountNum(self):
        return self.__destinationAccountNum
    @destinationAccountNum.setter
    def destinationAccountNum(self, destinationAccountNum: str):
        self.__destinationAccountNum = destinationAccountNum

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def account16(self):
        return self.__account16
    @account16.setter
    def account16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Transaction1__account16", None)
        self.__account16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transaction17"):
                opp_val = getattr(old_value, "transaction17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transaction17"):
                opp_val = getattr(value, "transaction17", None)
                if opp_val is None:
                    setattr(value, "transaction17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Account1:

    def __init__(self, userID: str, accountNum: str, type: account_AccountType, pin: str, balance: float, transaction17: set["Transaction1"] = None):
        self.userID = userID
        self.accountNum = accountNum
        self.type = type
        self.pin = pin
        self.balance = balance
        self.transaction17 = transaction17 if transaction17 is not None else set()
        
        pass
    @property
    def accountNum(self):
        return self.__accountNum
    @accountNum.setter
    def accountNum(self, accountNum: str):
        self.__accountNum = accountNum

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: account_AccountType):
        self.__type = type

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance

    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def transaction17(self):
        return self.__transaction17
    @transaction17.setter
    def transaction17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account1__transaction17", None)
        self.__transaction17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account16"):
                    opp_val = getattr(item, "account16", None)
                    
                    if opp_val == self:
                        setattr(item, "account16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account16"):
                    opp_val = getattr(item, "account16", None)
                    
                    setattr(item, "account16", self)
                    



class Transaction2:

    def __init__(self, type: transaction_TransactionType, time: str, amount: float, sourceAccountNum: str, destinationAccountNum: str, description: str, comment: str, transactionID: str):
        self.type = type
        self.time = time
        self.amount = amount
        self.sourceAccountNum = sourceAccountNum
        self.destinationAccountNum = destinationAccountNum
        self.description = description
        self.comment = comment
        self.transactionID = transactionID
        
        pass
    @property
    def sourceAccountNum(self):
        return self.__sourceAccountNum
    @sourceAccountNum.setter
    def sourceAccountNum(self, sourceAccountNum: str):
        self.__sourceAccountNum = sourceAccountNum

    @property
    def transactionID(self):
        return self.__transactionID
    @transactionID.setter
    def transactionID(self, transactionID: str):
        self.__transactionID = transactionID

    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: transaction_TransactionType):
        self.__type = type

    @property
    def destinationAccountNum(self):
        return self.__destinationAccountNum
    @destinationAccountNum.setter
    def destinationAccountNum(self, destinationAccountNum: str):
        self.__destinationAccountNum = destinationAccountNum

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



class Transaction:

    def __init__(self, transactionID: str, type: transaction_TransactionType, time: str, amount: float, sourceAccountNum: str, destinationAccountNum: str, description: str, comment: str):
        self.transactionID = transactionID
        self.type = type
        self.time = time
        self.amount = amount
        self.sourceAccountNum = sourceAccountNum
        self.destinationAccountNum = destinationAccountNum
        self.description = description
        self.comment = comment
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: transaction_TransactionType):
        self.__type = type

    @property
    def transactionID(self):
        return self.__transactionID
    @transactionID.setter
    def transactionID(self, transactionID: str):
        self.__transactionID = transactionID

    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

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
    def sourceAccountNum(self):
        return self.__sourceAccountNum
    @sourceAccountNum.setter
    def sourceAccountNum(self, sourceAccountNum: str):
        self.__sourceAccountNum = sourceAccountNum

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def destinationAccountNum(self):
        return self.__destinationAccountNum
    @destinationAccountNum.setter
    def destinationAccountNum(self, destinationAccountNum: str):
        self.__destinationAccountNum = destinationAccountNum



class Account:

    def __init__(self, userID: str, accountNum: str, type: account_AccountType, pin: str, balance: float):
        self.userID = userID
        self.accountNum = accountNum
        self.type = type
        self.pin = pin
        self.balance = balance
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: account_AccountType):
        self.__type = type

    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

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



class String:

    pass


class loan_LoanApplicationFile:

    def __init__(self, fileID: str, applicationID: str, loanApplication11: "loan_LoanApplication" = None):
        self.fileID = fileID
        self.applicationID = applicationID
        self.loanApplication11 = loanApplication11
        
        pass
    @property
    def applicationID(self):
        return self.__applicationID
    @applicationID.setter
    def applicationID(self, applicationID: str):
        self.__applicationID = applicationID

    @property
    def fileID(self):
        return self.__fileID
    @fileID.setter
    def fileID(self, fileID: str):
        self.__fileID = fileID

    @property
    def loanApplication11(self):
        return self.__loanApplication11
    @loanApplication11.setter
    def loanApplication11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_loan_LoanApplicationFile__loanApplication11", None)
        self.__loanApplication11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "loanApplicationFile10"):
                opp_val = getattr(old_value, "loanApplicationFile10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "loanApplicationFile10"):
                opp_val = getattr(value, "loanApplicationFile10", None)
                if opp_val is None:
                    setattr(value, "loanApplicationFile10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class loan_Loan:

    def __init__(self, loanID: str, amount: float, term: int, interestRate: float, status: loan_ApplicationStatus, submissionTime: str, type: loan_LoanStatus, userID: str, loanApplication13: "loan_LoanApplication" = None):
        self.loanID = loanID
        self.amount = amount
        self.term = term
        self.interestRate = interestRate
        self.status = status
        self.submissionTime = submissionTime
        self.type = type
        self.userID = userID
        self.loanApplication13 = loanApplication13
        
        pass
    @property
    def loanID(self):
        return self.__loanID
    @loanID.setter
    def loanID(self, loanID: str):
        self.__loanID = loanID

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: loan_ApplicationStatus):
        self.__status = status

    @property
    def term(self):
        return self.__term
    @term.setter
    def term(self, term: int):
        self.__term = term

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def submissionTime(self):
        return self.__submissionTime
    @submissionTime.setter
    def submissionTime(self, submissionTime: str):
        self.__submissionTime = submissionTime

    @property
    def interestRate(self):
        return self.__interestRate
    @interestRate.setter
    def interestRate(self, interestRate: float):
        self.__interestRate = interestRate

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: loan_LoanStatus):
        self.__type = type

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID

    @property
    def loanApplication13(self):
        return self.__loanApplication13
    @loanApplication13.setter
    def loanApplication13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_loan_Loan__loanApplication13", None)
        self.__loanApplication13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "loan12"):
                opp_val = getattr(old_value, "loan12", None)
                if opp_val == self:
                    setattr(old_value, "loan12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "loan12"):
                opp_val = getattr(value, "loan12", None)
                setattr(value, "loan12", self)



class loan_LoanApplication:

    def __init__(self, applicationID: str, amount: float, term: int, interestRate: float, status: loan_ApplicationStatus, submissionTime: str, type: loan_LoanType, userID: str, loanApplicationFile10: set["loan_LoanApplicationFile"] = None, loan12: "loan_Loan" = None, profile15: "Profile" = None):
        self.applicationID = applicationID
        self.amount = amount
        self.term = term
        self.interestRate = interestRate
        self.status = status
        self.submissionTime = submissionTime
        self.type = type
        self.userID = userID
        self.loanApplicationFile10 = loanApplicationFile10 if loanApplicationFile10 is not None else set()
        self.loan12 = loan12
        self.profile15 = profile15
        
        pass
    @property
    def submissionTime(self):
        return self.__submissionTime
    @submissionTime.setter
    def submissionTime(self, submissionTime: str):
        self.__submissionTime = submissionTime

    @property
    def interestRate(self):
        return self.__interestRate
    @interestRate.setter
    def interestRate(self, interestRate: float):
        self.__interestRate = interestRate

    @property
    def term(self):
        return self.__term
    @term.setter
    def term(self, term: int):
        self.__term = term

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: loan_ApplicationStatus):
        self.__status = status

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: loan_LoanType):
        self.__type = type

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID

    @property
    def applicationID(self):
        return self.__applicationID
    @applicationID.setter
    def applicationID(self, applicationID: str):
        self.__applicationID = applicationID

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def loan12(self):
        return self.__loan12
    @loan12.setter
    def loan12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_loan_LoanApplication__loan12", None)
        self.__loan12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "loanApplication13"):
                opp_val = getattr(old_value, "loanApplication13", None)
                if opp_val == self:
                    setattr(old_value, "loanApplication13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "loanApplication13"):
                opp_val = getattr(value, "loanApplication13", None)
                setattr(value, "loanApplication13", self)

    @property
    def loanApplicationFile10(self):
        return self.__loanApplicationFile10
    @loanApplicationFile10.setter
    def loanApplicationFile10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_loan_LoanApplication__loanApplicationFile10", None)
        self.__loanApplicationFile10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "loanApplication11"):
                    opp_val = getattr(item, "loanApplication11", None)
                    
                    if opp_val == self:
                        setattr(item, "loanApplication11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "loanApplication11"):
                    opp_val = getattr(item, "loanApplication11", None)
                    
                    setattr(item, "loanApplication11", self)
                    

    @property
    def profile15(self):
        return self.__profile15
    @profile15.setter
    def profile15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_loan_LoanApplication__profile15", None)
        self.__profile15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "loanApplication14"):
                opp_val = getattr(old_value, "loanApplication14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "loanApplication14"):
                opp_val = getattr(value, "loanApplication14", None)
                if opp_val is None:
                    setattr(value, "loanApplication14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



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
    def accountNum(self):
        return self.__accountNum
    @accountNum.setter
    def accountNum(self, accountNum: str):
        self.__accountNum = accountNum

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: account_AccountType):
        self.__type = type

    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance

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



class transaction_LoanPayment:

    def __init__(self, principal: float, interest: float, loanID: str):
        self.principal = principal
        self.interest = interest
        self.loanID = loanID
        
        pass
    @property
    def interest(self):
        return self.__interest
    @interest.setter
    def interest(self, interest: float):
        self.__interest = interest

    @property
    def principal(self):
        return self.__principal
    @principal.setter
    def principal(self, principal: float):
        self.__principal = principal

    @property
    def loanID(self):
        return self.__loanID
    @loanID.setter
    def loanID(self, loanID: str):
        self.__loanID = loanID



class transaction_Payee:

    def __init__(self, accountNum: str, name: str, address1: str, address2: str, city: str, state: str, country: str, zipcode: str, phoneNum: str, email: str, userID: str, paybillsTransaction5: set["transaction_PaybillsTransaction"] = None):
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
        self.userID = userID
        self.paybillsTransaction5 = paybillsTransaction5 if paybillsTransaction5 is not None else set()
        
        pass
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
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID

    @property
    def accountNum(self):
        return self.__accountNum
    @accountNum.setter
    def accountNum(self, accountNum: str):
        self.__accountNum = accountNum

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
    def address2(self):
        return self.__address2
    @address2.setter
    def address2(self, address2: str):
        self.__address2 = address2

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

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
                    

