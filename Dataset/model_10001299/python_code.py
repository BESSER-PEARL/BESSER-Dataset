from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class CheckingAccount:

    pass


class SavingAccount:

    pass


class CoDTransaction:

    def __init__(self, startDate: str, endDate: str, interestRate: str):
        self.startDate = startDate
        self.endDate = endDate
        self.interestRate = interestRate
        
        pass
    @property
    def interestRate(self):
        return self.__interestRate
    @interestRate.setter
    def interestRate(self, interestRate: str):
        self.__interestRate = interestRate

    @property
    def endDate(self):
        return self.__endDate
    @endDate.setter
    def endDate(self, endDate: str):
        self.__endDate = endDate

    @property
    def startDate(self):
        return self.__startDate
    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate



class CheckTransaction:

    def __init__(self, memo: str):
        self.memo = memo
        
        pass
    @property
    def memo(self):
        return self.__memo
    @memo.setter
    def memo(self, memo: str):
        self.__memo = memo



class Transaction:

    def __init__(self, transactionDate: str, holder: Customer, transactionType: str, transactionAmount: str, account3: set["Account"] = None):
        self.transactionDate = transactionDate
        self.holder = holder
        self.transactionType = transactionType
        self.transactionAmount = transactionAmount
        self.account3 = account3 if account3 is not None else set()
        
        pass
    @property
    def transactionAmount(self):
        return self.__transactionAmount
    @transactionAmount.setter
    def transactionAmount(self, transactionAmount: str):
        self.__transactionAmount = transactionAmount

    @property
    def transactionType(self):
        return self.__transactionType
    @transactionType.setter
    def transactionType(self, transactionType: str):
        self.__transactionType = transactionType

    @property
    def holder(self):
        return self.__holder
    @holder.setter
    def holder(self, holder: Customer):
        self.__holder = holder

    @property
    def transactionDate(self):
        return self.__transactionDate
    @transactionDate.setter
    def transactionDate(self, transactionDate: str):
        self.__transactionDate = transactionDate

    @property
    def account3(self):
        return self.__account3
    @account3.setter
    def account3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Transaction__account3", None)
        self.__account3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "transaction2"):
                    opp_val = getattr(item, "transaction2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "transaction2"):
                    opp_val = getattr(item, "transaction2", None)
                    
                    if opp_val is None:
                        setattr(item, "transaction2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Account(ABC):

    def __init__(self, accId: str, accNumber: str, openDate: str, balance: str, MAX_HOLDERS: str, transaction2: set["Transaction"] = None, bank5: "Bank" = None, customer7: set["Customer"] = None):
        self.accId = accId
        self.accNumber = accNumber
        self.openDate = openDate
        self.balance = balance
        self.MAX_HOLDERS = MAX_HOLDERS
        self.transaction2 = transaction2 if transaction2 is not None else set()
        self.bank5 = bank5
        self.customer7 = customer7 if customer7 is not None else set()
        
        pass
    @property
    def accNumber(self):
        return self.__accNumber
    @accNumber.setter
    def accNumber(self, accNumber: str):
        self.__accNumber = accNumber

    @property
    def MAX_HOLDERS(self):
        return self.__MAX_HOLDERS
    @MAX_HOLDERS.setter
    def MAX_HOLDERS(self, MAX_HOLDERS: str):
        self.__MAX_HOLDERS = MAX_HOLDERS

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: str):
        self.__balance = balance

    @property
    def accId(self):
        return self.__accId
    @accId.setter
    def accId(self, accId: str):
        self.__accId = accId

    @property
    def openDate(self):
        return self.__openDate
    @openDate.setter
    def openDate(self, openDate: str):
        self.__openDate = openDate

    @property
    def transaction2(self):
        return self.__transaction2
    @transaction2.setter
    def transaction2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__transaction2", None)
        self.__transaction2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account3"):
                    opp_val = getattr(item, "account3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account3"):
                    opp_val = getattr(item, "account3", None)
                    
                    if opp_val is None:
                        setattr(item, "account3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def bank5(self):
        return self.__bank5
    @bank5.setter
    def bank5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__bank5", None)
        self.__bank5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account4"):
                opp_val = getattr(old_value, "account4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account4"):
                opp_val = getattr(value, "account4", None)
                if opp_val is None:
                    setattr(value, "account4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer7(self):
        return self.__customer7
    @customer7.setter
    def customer7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__customer7", None)
        self.__customer7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account6"):
                    opp_val = getattr(item, "account6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account6"):
                    opp_val = getattr(item, "account6", None)
                    
                    if opp_val is None:
                        setattr(item, "account6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Customer:

    def __init__(self, taxId: str, name: str, bank1: "Bank" = None, account6: set["Account"] = None):
        self.taxId = taxId
        self.name = name
        self.bank1 = bank1
        self.account6 = account6 if account6 is not None else set()
        
        pass
    @property
    def taxId(self):
        return self.__taxId
    @taxId.setter
    def taxId(self, taxId: str):
        self.__taxId = taxId

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def account6(self):
        return self.__account6
    @account6.setter
    def account6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__account6", None)
        self.__account6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer7"):
                    opp_val = getattr(item, "customer7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer7"):
                    opp_val = getattr(item, "customer7", None)
                    
                    if opp_val is None:
                        setattr(item, "customer7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def bank1(self):
        return self.__bank1
    @bank1.setter
    def bank1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__bank1", None)
        self.__bank1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer0"):
                opp_val = getattr(old_value, "customer0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer0"):
                opp_val = getattr(value, "customer0", None)
                if opp_val is None:
                    setattr(value, "customer0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Bank:

    pass
