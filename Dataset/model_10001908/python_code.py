from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class genmymodelreverse_java_util_Date:

    pass


class genmymodelreverse_C2:

    pass


class genmymodelreverse_C1:

    pass


class genmymodelreverse_java_util_HashMap:

    pass


class genmymodelreverse_org_springframework_ui_Model_Interface(ABC):

    pass


class TestAccountChain:

    pass


class model_Withdrawal:

    pass


class model_Transaction:

    def __init__(self, date: genmymodelreverse_java_util_Date, ammount: float):
        self.date = date
        self.ammount = ammount
        
        pass
    @property
    def ammount(self):
        return self.__ammount
    @ammount.setter
    def ammount(self, ammount: float):
        self.__ammount = ammount

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: genmymodelreverse_java_util_Date):
        self.__date = date



class model_SavingsAccount:

    def __init__(self, interestRate: float, type: str):
        self.interestRate = interestRate
        self.type = type
        
        pass
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
    def type(self, type: str):
        self.__type = type



class model_OpenAccount:

    pass


class model_MakePayment:

    pass


class model_Loan:

    def __init__(self, interestRate: float, minPayment: float, paymentDueDate: str, type: str):
        self.interestRate = interestRate
        self.minPayment = minPayment
        self.paymentDueDate = paymentDueDate
        self.type = type
        
        pass
    @property
    def minPayment(self):
        return self.__minPayment
    @minPayment.setter
    def minPayment(self, minPayment: float):
        self.__minPayment = minPayment

    @property
    def paymentDueDate(self):
        return self.__paymentDueDate
    @paymentDueDate.setter
    def paymentDueDate(self, paymentDueDate: str):
        self.__paymentDueDate = paymentDueDate

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
    def type(self, type: str):
        self.__type = type



class model_Deposit:

    pass


class model_Customer:

    def __init__(self, name: str, address: str, password: str, dob: str, accounts: str, username: str, id: int, owns0: set["model_Account"] = None, requests2: set["model_AccountAction"] = None, bank12: "model_Bank" = None):
        self.name = name
        self.address = address
        self.password = password
        self.dob = dob
        self.accounts = accounts
        self.username = username
        self.id = id
        self.owns0 = owns0 if owns0 is not None else set()
        self.requests2 = requests2 if requests2 is not None else set()
        self.bank12 = bank12
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def accounts(self):
        return self.__accounts
    @accounts.setter
    def accounts(self, accounts: str):
        self.__accounts = accounts

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def dob(self):
        return self.__dob
    @dob.setter
    def dob(self, dob: str):
        self.__dob = dob

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def owns0(self):
        return self.__owns0
    @owns0.setter
    def owns0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Customer__owns0", None)
        self.__owns0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has1"):
                    opp_val = getattr(item, "has1", None)
                    
                    if opp_val == self:
                        setattr(item, "has1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has1"):
                    opp_val = getattr(item, "has1", None)
                    
                    setattr(item, "has1", self)
                    

    @property
    def bank12(self):
        return self.__bank12
    @bank12.setter
    def bank12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Customer__bank12", None)
        self.__bank12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer13"):
                opp_val = getattr(old_value, "customer13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer13"):
                opp_val = getattr(value, "customer13", None)
                if opp_val is None:
                    setattr(value, "customer13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requests2(self):
        return self.__requests2
    @requests2.setter
    def requests2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Customer__requests2", None)
        self.__requests2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer3"):
                    opp_val = getattr(item, "customer3", None)
                    
                    if opp_val == self:
                        setattr(item, "customer3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer3"):
                    opp_val = getattr(item, "customer3", None)
                    
                    setattr(item, "customer3", self)
                    



class model_CreditAccount:

    def __init__(self, minPayment: float, interestRate: float, paymentDueDate: str, type: str):
        self.minPayment = minPayment
        self.interestRate = interestRate
        self.paymentDueDate = paymentDueDate
        self.type = type
        
        pass
    @property
    def interestRate(self):
        return self.__interestRate
    @interestRate.setter
    def interestRate(self, interestRate: float):
        self.__interestRate = interestRate

    @property
    def minPayment(self):
        return self.__minPayment
    @minPayment.setter
    def minPayment(self, minPayment: float):
        self.__minPayment = minPayment

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def paymentDueDate(self):
        return self.__paymentDueDate
    @paymentDueDate.setter
    def paymentDueDate(self, paymentDueDate: str):
        self.__paymentDueDate = paymentDueDate



class model_CloseAccount:

    pass


class model_CheckingAccount:

    def __init__(self, interestRate: float, type: str):
        self.interestRate = interestRate
        self.type = type
        
        pass
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
    def type(self, type: str):
        self.__type = type



class model_Bank:

    def __init__(self, name: str, address: str, customerMap: str, customer13: set["model_Customer"] = None, accounts15: set["model_Account"] = None):
        self.name = name
        self.address = address
        self.customerMap = customerMap
        self.customer13 = customer13 if customer13 is not None else set()
        self.accounts15 = accounts15 if accounts15 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def customerMap(self):
        return self.__customerMap
    @customerMap.setter
    def customerMap(self, customerMap: str):
        self.__customerMap = customerMap

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def accounts15(self):
        return self.__accounts15
    @accounts15.setter
    def accounts15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Bank__accounts15", None)
        self.__accounts15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bank14"):
                    opp_val = getattr(item, "bank14", None)
                    
                    if opp_val == self:
                        setattr(item, "bank14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bank14"):
                    opp_val = getattr(item, "bank14", None)
                    
                    setattr(item, "bank14", self)
                    

    @property
    def customer13(self):
        return self.__customer13
    @customer13.setter
    def customer13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Bank__customer13", None)
        self.__customer13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bank12"):
                    opp_val = getattr(item, "bank12", None)
                    
                    if opp_val == self:
                        setattr(item, "bank12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bank12"):
                    opp_val = getattr(item, "bank12", None)
                    
                    setattr(item, "bank12", self)
                    



class model_AccountHandler:

    pass


class model_AccountChain_Interface:

    pass


class model_AccountAction:

    def __init__(self, action: str, amount: float, success: bool, customer3: "model_Customer" = None, account7: set["model_Account"] = None):
        self.action = action
        self.amount = amount
        self.success = success
        self.customer3 = customer3
        self.account7 = account7 if account7 is not None else set()
        
        pass
    @property
    def success(self):
        return self.__success
    @success.setter
    def success(self, success: bool):
        self.__success = success

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def action(self):
        return self.__action
    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def customer3(self):
        return self.__customer3
    @customer3.setter
    def customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AccountAction__customer3", None)
        self.__customer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requests2"):
                opp_val = getattr(old_value, "requests2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requests2"):
                opp_val = getattr(value, "requests2", None)
                if opp_val is None:
                    setattr(value, "requests2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def account7(self):
        return self.__account7
    @account7.setter
    def account7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AccountAction__account7", None)
        self.__account7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "accountAction6"):
                    opp_val = getattr(item, "accountAction6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accountAction6"):
                    opp_val = getattr(item, "accountAction6", None)
                    
                    if opp_val is None:
                        setattr(item, "accountAction6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class model_Account(ABC):

    def __init__(self, customerId: int, accountNumber: int, balance: float, type: str, has1: "model_Customer" = None, accountAction6: set["model_AccountAction"] = None, bank14: "model_Bank" = None):
        self.customerId = customerId
        self.accountNumber = accountNumber
        self.balance = balance
        self.type = type
        self.has1 = has1
        self.accountAction6 = accountAction6 if accountAction6 is not None else set()
        self.bank14 = bank14
        
        pass
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance

    @property
    def customerId(self):
        return self.__customerId
    @customerId.setter
    def customerId(self, customerId: int):
        self.__customerId = customerId

    @property
    def accountNumber(self):
        return self.__accountNumber
    @accountNumber.setter
    def accountNumber(self, accountNumber: int):
        self.__accountNumber = accountNumber

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def bank14(self):
        return self.__bank14
    @bank14.setter
    def bank14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Account__bank14", None)
        self.__bank14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounts15"):
                opp_val = getattr(old_value, "accounts15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounts15"):
                opp_val = getattr(value, "accounts15", None)
                if opp_val is None:
                    setattr(value, "accounts15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def accountAction6(self):
        return self.__accountAction6
    @accountAction6.setter
    def accountAction6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Account__accountAction6", None)
        self.__accountAction6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account7"):
                    opp_val = getattr(item, "account7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account7"):
                    opp_val = getattr(item, "account7", None)
                    
                    if opp_val is None:
                        setattr(item, "account7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def has1(self):
        return self.__has1
    @has1.setter
    def has1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Account__has1", None)
        self.__has1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owns0"):
                opp_val = getattr(old_value, "owns0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owns0"):
                opp_val = getattr(value, "owns0", None)
                if opp_val is None:
                    setattr(value, "owns0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class data_CustomerProfileRepository:

    def __init__(self, numAccounts: int, customerProfiles: str):
        self.numAccounts = numAccounts
        self.customerProfiles = customerProfiles
        
        pass
    @property
    def customerProfiles(self):
        return self.__customerProfiles
    @customerProfiles.setter
    def customerProfiles(self, customerProfiles: str):
        self.__customerProfiles = customerProfiles

    @property
    def numAccounts(self):
        return self.__numAccounts
    @numAccounts.setter
    def numAccounts(self, numAccounts: int):
        self.__numAccounts = numAccounts



class OnlineBanking_AppConfig:

    pass
