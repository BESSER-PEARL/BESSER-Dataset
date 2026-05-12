from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Student:

    def __init__(self, name: str, checking1: "Checking" = None, savings3: "Savings" = None):
        self.name = name
        self.checking1 = checking1
        self.savings3 = savings3
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def savings3(self):
        return self.__savings3
    @savings3.setter
    def savings3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__savings3", None)
        self.__savings3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student2"):
                opp_val = getattr(old_value, "student2", None)
                if opp_val == self:
                    setattr(old_value, "student2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student2"):
                opp_val = getattr(value, "student2", None)
                setattr(value, "student2", self)

    @property
    def checking1(self):
        return self.__checking1
    @checking1.setter
    def checking1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__checking1", None)
        self.__checking1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student0"):
                opp_val = getattr(old_value, "student0", None)
                if opp_val == self:
                    setattr(old_value, "student0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student0"):
                opp_val = getattr(value, "student0", None)
                setattr(value, "student0", self)



class Savings:

    pass


class Main:

    pass


class Instructor:

    def __init__(self, name: str, savings7: "Savings" = None, checking5: "Checking" = None):
        self.name = name
        self.savings7 = savings7
        self.checking5 = checking5
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def checking5(self):
        return self.__checking5
    @checking5.setter
    def checking5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Instructor__checking5", None)
        self.__checking5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "instructor4"):
                opp_val = getattr(old_value, "instructor4", None)
                if opp_val == self:
                    setattr(old_value, "instructor4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "instructor4"):
                opp_val = getattr(value, "instructor4", None)
                setattr(value, "instructor4", self)

    @property
    def savings7(self):
        return self.__savings7
    @savings7.setter
    def savings7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Instructor__savings7", None)
        self.__savings7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "instructor6"):
                opp_val = getattr(old_value, "instructor6", None)
                if opp_val == self:
                    setattr(old_value, "instructor6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "instructor6"):
                opp_val = getattr(value, "instructor6", None)
                setattr(value, "instructor6", self)



class Checking:

    def __init__(self, OVERDRAFT_LIMIT: float, OVERDRAFT_FEE: float, isActive: bool, student0: "Student" = None, instructor4: "Instructor" = None):
        self.OVERDRAFT_LIMIT = OVERDRAFT_LIMIT
        self.OVERDRAFT_FEE = OVERDRAFT_FEE
        self.isActive = isActive
        self.student0 = student0
        self.instructor4 = instructor4
        
        pass
    @property
    def isActive(self):
        return self.__isActive
    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def OVERDRAFT_FEE(self):
        return self.__OVERDRAFT_FEE
    @OVERDRAFT_FEE.setter
    def OVERDRAFT_FEE(self, OVERDRAFT_FEE: float):
        self.__OVERDRAFT_FEE = OVERDRAFT_FEE

    @property
    def OVERDRAFT_LIMIT(self):
        return self.__OVERDRAFT_LIMIT
    @OVERDRAFT_LIMIT.setter
    def OVERDRAFT_LIMIT(self, OVERDRAFT_LIMIT: float):
        self.__OVERDRAFT_LIMIT = OVERDRAFT_LIMIT

    @property
    def student0(self):
        return self.__student0
    @student0.setter
    def student0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Checking__student0", None)
        self.__student0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checking1"):
                opp_val = getattr(old_value, "checking1", None)
                if opp_val == self:
                    setattr(old_value, "checking1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checking1"):
                opp_val = getattr(value, "checking1", None)
                setattr(value, "checking1", self)

    @property
    def instructor4(self):
        return self.__instructor4
    @instructor4.setter
    def instructor4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Checking__instructor4", None)
        self.__instructor4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checking5"):
                opp_val = getattr(old_value, "checking5", None)
                if opp_val == self:
                    setattr(old_value, "checking5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checking5"):
                opp_val = getattr(value, "checking5", None)
                setattr(value, "checking5", self)



class BankAccount:

    def __init__(self, numOfTransactions: int, TRANSACTION_FEE: int, FREE_TRANSACTIONS: int, balance: float, minimumBalance: float, isActive: bool):
        self.numOfTransactions = numOfTransactions
        self.TRANSACTION_FEE = TRANSACTION_FEE
        self.FREE_TRANSACTIONS = FREE_TRANSACTIONS
        self.balance = balance
        self.minimumBalance = minimumBalance
        self.isActive = isActive
        
        pass
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance

    @property
    def TRANSACTION_FEE(self):
        return self.__TRANSACTION_FEE
    @TRANSACTION_FEE.setter
    def TRANSACTION_FEE(self, TRANSACTION_FEE: int):
        self.__TRANSACTION_FEE = TRANSACTION_FEE

    @property
    def FREE_TRANSACTIONS(self):
        return self.__FREE_TRANSACTIONS
    @FREE_TRANSACTIONS.setter
    def FREE_TRANSACTIONS(self, FREE_TRANSACTIONS: int):
        self.__FREE_TRANSACTIONS = FREE_TRANSACTIONS

    @property
    def numOfTransactions(self):
        return self.__numOfTransactions
    @numOfTransactions.setter
    def numOfTransactions(self, numOfTransactions: int):
        self.__numOfTransactions = numOfTransactions

    @property
    def minimumBalance(self):
        return self.__minimumBalance
    @minimumBalance.setter
    def minimumBalance(self, minimumBalance: float):
        self.__minimumBalance = minimumBalance

    @property
    def isActive(self):
        return self.__isActive
    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

