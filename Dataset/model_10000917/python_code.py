from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class FixedAccount:

    def __init__(self, chequeBookNo: str):
        self.chequeBookNo = chequeBookNo
        
        pass
    @property
    def chequeBookNo(self):
        return self.__chequeBookNo
    @chequeBookNo.setter
    def chequeBookNo(self, chequeBookNo: str):
        self.__chequeBookNo = chequeBookNo



class SavingsAccount:

    def __init__(self, interestRate: float, noticeGiven: bool):
        self.interestRate = interestRate
        self.noticeGiven = noticeGiven
        
        pass
    @property
    def interestRate(self):
        return self.__interestRate
    @interestRate.setter
    def interestRate(self, interestRate: float):
        self.__interestRate = interestRate

    @property
    def noticeGiven(self):
        return self.__noticeGiven
    @noticeGiven.setter
    def noticeGiven(self, noticeGiven: bool):
        self.__noticeGiven = noticeGiven



class BankAccount:

    def __init__(self, accountNumber: int, accountHolder: str, balance: float, bank1: "Bank" = None):
        self.accountNumber = accountNumber
        self.accountHolder = accountHolder
        self.balance = balance
        self.bank1 = bank1
        
        pass
    @property
    def accountNumber(self):
        return self.__accountNumber
    @accountNumber.setter
    def accountNumber(self, accountNumber: int):
        self.__accountNumber = accountNumber

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance

    @property
    def accountHolder(self):
        return self.__accountHolder
    @accountHolder.setter
    def accountHolder(self, accountHolder: str):
        self.__accountHolder = accountHolder

    @property
    def bank1(self):
        return self.__bank1
    @bank1.setter
    def bank1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankAccount__bank1", None)
        self.__bank1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bankAccount0"):
                opp_val = getattr(old_value, "bankAccount0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bankAccount0"):
                opp_val = getattr(value, "bankAccount0", None)
                if opp_val is None:
                    setattr(value, "bankAccount0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Bank:

    def __init__(self, name: str, bankAccount0: set["BankAccount"] = None):
        self.name = name
        self.bankAccount0 = bankAccount0 if bankAccount0 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bankAccount0(self):
        return self.__bankAccount0
    @bankAccount0.setter
    def bankAccount0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bank__bankAccount0", None)
        self.__bankAccount0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bank1"):
                    opp_val = getattr(item, "bank1", None)
                    
                    if opp_val == self:
                        setattr(item, "bank1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bank1"):
                    opp_val = getattr(item, "bank1", None)
                    
                    setattr(item, "bank1", self)
                    

