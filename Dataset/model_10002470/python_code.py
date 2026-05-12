from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class transaction_TransactionType(Enum):
    pass
class Medical_Record_AccountType(Enum):
    pass

############################################
# Definition of Classes
############################################










class MyInterface_Interface:

    pass


class Medical_Record_NHS_Number:

    def __init__(self, accountNo: str, type: Medical_Record_AccountType, balance: float, Patient0: "Patient" = None, record_search2: set["transaction_Interface"] = None):
        self.accountNo = accountNo
        self.type = type
        self.balance = balance
        self.Patient0 = Patient0
        self.record_search2 = record_search2 if record_search2 is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: Medical_Record_AccountType):
        self.__type = type

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance

    @property
    def accountNo(self):
        return self.__accountNo
    @accountNo.setter
    def accountNo(self, accountNo: str):
        self.__accountNo = accountNo

    @property
    def record_search2(self):
        return self.__record_search2
    @record_search2.setter
    def record_search2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medical_Record_NHS_Number__record_search2", None)
        self.__record_search2 = value if value is not None else set()
        
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
    def Patient0(self):
        return self.__Patient0
    @Patient0.setter
    def Patient0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medical_Record_NHS_Number__Patient0", None)
        self.__Patient0 = value
        
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



class Medical_Record_CheckingAccount:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class Medical_Record_CertificatesOfDepositAccount:

    def __init__(self, timePeriod: int, interestRate: float):
        self.timePeriod = timePeriod
        self.interestRate = interestRate
        
        pass
    @property
    def timePeriod(self):
        return self.__timePeriod
    @timePeriod.setter
    def timePeriod(self, timePeriod: int):
        self.__timePeriod = timePeriod

    @property
    def interestRate(self):
        return self.__interestRate
    @interestRate.setter
    def interestRate(self, interestRate: float):
        self.__interestRate = interestRate



class Medical_Record_SavingsAccount:

    def __init__(self, interestRate: float):
        self.interestRate = interestRate
        
        pass
    @property
    def interestRate(self):
        return self.__interestRate
    @interestRate.setter
    def interestRate(self, interestRate: float):
        self.__interestRate = interestRate



class transaction_Community_Hospital:

    def __init__(self, targetAccount: Medical_Record_NHS_Number, sourceAccount: Medical_Record_NHS_Number):
        self.targetAccount = targetAccount
        self.sourceAccount = sourceAccount
        
        pass
    @property
    def targetAccount(self):
        return self.__targetAccount
    @targetAccount.setter
    def targetAccount(self, targetAccount: Medical_Record_NHS_Number):
        self.__targetAccount = targetAccount

    @property
    def sourceAccount(self):
        return self.__sourceAccount
    @sourceAccount.setter
    def sourceAccount(self, sourceAccount: Medical_Record_NHS_Number):
        self.__sourceAccount = sourceAccount



class transaction_Acute_Hospital:

    pass


class transaction_Mental_Health_Trust:

    pass


class transaction_Interface:

    def __init__(self, id: int, type: transaction_TransactionType, transactionTime: date, amount: float, account3: "Medical_Record_NHS_Number" = None):
        self.id = id
        self.type = type
        self.transactionTime = transactionTime
        self.amount = amount
        self.account3 = account3
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

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
    def type(self, type: transaction_TransactionType):
        self.__type = type

    @property
    def transactionTime(self):
        return self.__transactionTime
    @transactionTime.setter
    def transactionTime(self, transactionTime: date):
        self.__transactionTime = transactionTime

    @property
    def account3(self):
        return self.__account3
    @account3.setter
    def account3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transaction_Interface__account3", None)
        self.__account3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "record_search2"):
                opp_val = getattr(old_value, "record_search2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "record_search2"):
                opp_val = getattr(value, "record_search2", None)
                if opp_val is None:
                    setattr(value, "record_search2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Login:

    def __init__(self, username: str, securityAnswer: str, password: str, securityQuestion: str, lastLoginTime: date, customer5: "Patient" = None):
        self.username = username
        self.securityAnswer = securityAnswer
        self.password = password
        self.securityQuestion = securityQuestion
        self.lastLoginTime = lastLoginTime
        self.customer5 = customer5
        
        pass
    @property
    def lastLoginTime(self):
        return self.__lastLoginTime
    @lastLoginTime.setter
    def lastLoginTime(self, lastLoginTime: date):
        self.__lastLoginTime = lastLoginTime

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
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def securityQuestion(self):
        return self.__securityQuestion
    @securityQuestion.setter
    def securityQuestion(self, securityQuestion: str):
        self.__securityQuestion = securityQuestion

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



class Patient:

    def __init__(self, name: str, dateOfBirth: date, address: str, phoneNumber: str, emailAddress: str, GP_Address: str, a1: set["Medical_Record_NHS_Number"] = None, login4: "Login" = None):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.address = address
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.GP_Address = GP_Address
        self.a1 = a1 if a1 is not None else set()
        self.login4 = login4
        
        pass
    @property
    def dateOfBirth(self):
        return self.__dateOfBirth
    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def GP_Address(self):
        return self.__GP_Address
    @GP_Address.setter
    def GP_Address(self, GP_Address: str):
        self.__GP_Address = GP_Address

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def emailAddress(self):
        return self.__emailAddress
    @emailAddress.setter
    def emailAddress(self, emailAddress: str):
        self.__emailAddress = emailAddress

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def a1(self):
        return self.__a1
    @a1.setter
    def a1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__a1", None)
        self.__a1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Patient0"):
                    opp_val = getattr(item, "Patient0", None)
                    
                    if opp_val == self:
                        setattr(item, "Patient0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Patient0"):
                    opp_val = getattr(item, "Patient0", None)
                    
                    setattr(item, "Patient0", self)
                    

    @property
    def login4(self):
        return self.__login4
    @login4.setter
    def login4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__login4", None)
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

