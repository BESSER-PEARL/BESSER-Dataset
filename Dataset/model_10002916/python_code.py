from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class transaction_TransactionType(Enum):
    pass
class account_AccountType(Enum):
    pass

############################################
# Definition of Classes
############################################










class OPT_AuthenticationProcessor:

    def __init__(self, UserEmail: str, Authentication_Result: bool):
        self.UserEmail = UserEmail
        self.Authentication_Result = Authentication_Result
        
        pass
    @property
    def Authentication_Result(self):
        return self.__Authentication_Result
    @Authentication_Result.setter
    def Authentication_Result(self, Authentication_Result: bool):
        self.__Authentication_Result = Authentication_Result

    @property
    def UserEmail(self):
        return self.__UserEmail
    @UserEmail.setter
    def UserEmail(self, UserEmail: str):
        self.__UserEmail = UserEmail



class Database:

    pass


class LoginAuthenticationProcessor:

    def __init__(self, UserPassWord: str, UserID: str, Authentication_Result: bool):
        self.UserPassWord = UserPassWord
        self.UserID = UserID
        self.Authentication_Result = Authentication_Result
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: str):
        self.__UserID = UserID

    @property
    def UserPassWord(self):
        return self.__UserPassWord
    @UserPassWord.setter
    def UserPassWord(self, UserPassWord: str):
        self.__UserPassWord = UserPassWord

    @property
    def Authentication_Result(self):
        return self.__Authentication_Result
    @Authentication_Result.setter
    def Authentication_Result(self, Authentication_Result: bool):
        self.__Authentication_Result = Authentication_Result



class Authentication:

    def __init__(self, UserID: str, UserPassWord: str, UserEmail: str, Authentication_Result: bool, AuthenticationType: int, UserPassWord1: str, database7: "Database" = None):
        self.UserID = UserID
        self.UserPassWord = UserPassWord
        self.UserEmail = UserEmail
        self.Authentication_Result = Authentication_Result
        self.AuthenticationType = AuthenticationType
        self.UserPassWord1 = UserPassWord1
        self.database7 = database7
        
        pass
    @property
    def UserPassWord1(self):
        return self.__UserPassWord1
    @UserPassWord1.setter
    def UserPassWord1(self, UserPassWord1: str):
        self.__UserPassWord1 = UserPassWord1

    @property
    def Authentication_Result(self):
        return self.__Authentication_Result
    @Authentication_Result.setter
    def Authentication_Result(self, Authentication_Result: bool):
        self.__Authentication_Result = Authentication_Result

    @property
    def UserPassWord(self):
        return self.__UserPassWord
    @UserPassWord.setter
    def UserPassWord(self, UserPassWord: str):
        self.__UserPassWord = UserPassWord

    @property
    def UserEmail(self):
        return self.__UserEmail
    @UserEmail.setter
    def UserEmail(self, UserEmail: str):
        self.__UserEmail = UserEmail

    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: str):
        self.__UserID = UserID

    @property
    def AuthenticationType(self):
        return self.__AuthenticationType
    @AuthenticationType.setter
    def AuthenticationType(self, AuthenticationType: int):
        self.__AuthenticationType = AuthenticationType

    @property
    def database7(self):
        return self.__database7
    @database7.setter
    def database7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Authentication__database7", None)
        self.__database7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "authentication6"):
                opp_val = getattr(old_value, "authentication6", None)
                if opp_val == self:
                    setattr(old_value, "authentication6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authentication6"):
                opp_val = getattr(value, "authentication6", None)
                setattr(value, "authentication6", self)



class RequestOTPAuthentication:

    def __init__(self, UserID: str, UserEmail: str):
        self.UserID = UserID
        self.UserEmail = UserEmail
        
        pass
    @property
    def UserEmail(self):
        return self.__UserEmail
    @UserEmail.setter
    def UserEmail(self, UserEmail: str):
        self.__UserEmail = UserEmail

    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: str):
        self.__UserID = UserID



class LOGIN:

    def __init__(self, UserID: str, UserPassWord: str):
        self.UserID = UserID
        self.UserPassWord = UserPassWord
        
        pass
    @property
    def UserPassWord(self):
        return self.__UserPassWord
    @UserPassWord.setter
    def UserPassWord(self, UserPassWord: str):
        self.__UserPassWord = UserPassWord

    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: str):
        self.__UserID = UserID



class account_Account:

    def __init__(self, accountNo: str, type: account_AccountType, balance: float, customer0: "Customer" = None, transactions2: set["transaction_Transaction"] = None):
        self.accountNo = accountNo
        self.type = type
        self.balance = balance
        self.customer0 = customer0
        self.transactions2 = transactions2 if transactions2 is not None else set()
        
        pass
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: account_AccountType):
        self.__type = type

    @property
    def accountNo(self):
        return self.__accountNo
    @accountNo.setter
    def accountNo(self, accountNo: str):
        self.__accountNo = accountNo

    @property
    def transactions2(self):
        return self.__transactions2
    @transactions2.setter
    def transactions2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_account_Account__transactions2", None)
        self.__transactions2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account3"):
                    opp_val = getattr(item, "account3", None)
                    
                    if opp_val == self:
                        setattr(item, "account3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account3"):
                    opp_val = getattr(item, "account3", None)
                    
                    setattr(item, "account3", self)
                    

    @property
    def customer0(self):
        return self.__customer0
    @customer0.setter
    def customer0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_account_Account__customer0", None)
        self.__customer0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a1"):
                opp_val = getattr(old_value, "a1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a1"):
                opp_val = getattr(value, "a1", None)
                if opp_val is None:
                    setattr(value, "a1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class account_CheckingAccount:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class account_CertificatesOfDepositAccount:

    def __init__(self, timePeriod: int, interestRate: float):
        self.timePeriod = timePeriod
        self.interestRate = interestRate
        
        pass
    @property
    def interestRate(self):
        return self.__interestRate
    @interestRate.setter
    def interestRate(self, interestRate: float):
        self.__interestRate = interestRate

    @property
    def timePeriod(self):
        return self.__timePeriod
    @timePeriod.setter
    def timePeriod(self, timePeriod: int):
        self.__timePeriod = timePeriod



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



class transaction_TransferTransaction:

    def __init__(self, targetAccount: account_Account, sourceAccount: account_Account):
        self.targetAccount = targetAccount
        self.sourceAccount = sourceAccount
        
        pass
    @property
    def targetAccount(self):
        return self.__targetAccount
    @targetAccount.setter
    def targetAccount(self, targetAccount: account_Account):
        self.__targetAccount = targetAccount

    @property
    def sourceAccount(self):
        return self.__sourceAccount
    @sourceAccount.setter
    def sourceAccount(self, sourceAccount: account_Account):
        self.__sourceAccount = sourceAccount



class transaction_WithdrawTransaction:

    pass


class transaction_DepositTransaction:

    pass


class transaction_Transaction:

    def __init__(self, amount: float, id: int, type: transaction_TransactionType, transactionTime: date, account3: "account_Account" = None):
        self.amount = amount
        self.id = id
        self.type = type
        self.transactionTime = transactionTime
        self.account3 = account3
        
        pass
    @property
    def transactionTime(self):
        return self.__transactionTime
    @transactionTime.setter
    def transactionTime(self, transactionTime: date):
        self.__transactionTime = transactionTime

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: transaction_TransactionType):
        self.__type = type

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def account3(self):
        return self.__account3
    @account3.setter
    def account3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transaction_Transaction__account3", None)
        self.__account3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transactions2"):
                opp_val = getattr(old_value, "transactions2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transactions2"):
                opp_val = getattr(value, "transactions2", None)
                if opp_val is None:
                    setattr(value, "transactions2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Login:

    def __init__(self, username: str, securityAnswer: str, password: str, securityQuestion: str, lastLoginTime: date, customer5: "Customer" = None):
        self.username = username
        self.securityAnswer = securityAnswer
        self.password = password
        self.securityQuestion = securityQuestion
        self.lastLoginTime = lastLoginTime
        self.customer5 = customer5
        
        pass
    @property
    def securityAnswer(self):
        return self.__securityAnswer
    @securityAnswer.setter
    def securityAnswer(self, securityAnswer: str):
        self.__securityAnswer = securityAnswer

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def securityQuestion(self):
        return self.__securityQuestion
    @securityQuestion.setter
    def securityQuestion(self, securityQuestion: str):
        self.__securityQuestion = securityQuestion

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def lastLoginTime(self):
        return self.__lastLoginTime
    @lastLoginTime.setter
    def lastLoginTime(self, lastLoginTime: date):
        self.__lastLoginTime = lastLoginTime

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__customer5", None)
        self.__customer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login4"):
                opp_val = getattr(old_value, "login4", None)
                if opp_val == self:
                    setattr(old_value, "login4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login4"):
                opp_val = getattr(value, "login4", None)
                setattr(value, "login4", self)



class Customer:

    def __init__(self, name: str, dateOfBirth: date, address: str, phoneNumber: str, emailAddress: str, a1: set["account_Account"] = None, login4: "Login" = None):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.address = address
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.a1 = a1 if a1 is not None else set()
        self.login4 = login4
        
        pass
    @property
    def emailAddress(self):
        return self.__emailAddress
    @emailAddress.setter
    def emailAddress(self, emailAddress: str):
        self.__emailAddress = emailAddress

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def a1(self):
        return self.__a1
    @a1.setter
    def a1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__a1", None)
        self.__a1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer0"):
                    opp_val = getattr(item, "customer0", None)
                    
                    if opp_val == self:
                        setattr(item, "customer0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer0"):
                    opp_val = getattr(item, "customer0", None)
                    
                    setattr(item, "customer0", self)
                    

    @property
    def login4(self):
        return self.__login4
    @login4.setter
    def login4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__login4", None)
        self.__login4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer5"):
                opp_val = getattr(old_value, "customer5", None)
                if opp_val == self:
                    setattr(old_value, "customer5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer5"):
                opp_val = getattr(value, "customer5", None)
                setattr(value, "customer5", self)

