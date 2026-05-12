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










class account_Account:

    def __init__(self, type: account_AccountType, balance: float, accountNo: str, transactions0: set["transaction_Transaction"] = None):
        self.type = type
        self.balance = balance
        self.accountNo = accountNo
        self.transactions0 = transactions0 if transactions0 is not None else set()
        
        pass
    @property
    def accountNo(self):
        return self.__accountNo
    @accountNo.setter
    def accountNo(self, accountNo: str):
        self.__accountNo = accountNo

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

    def __init__(self, id: int, type: transaction_TransactionType, transactionTime: date, amount: float, account1: "account_Account" = None):
        self.id = id
        self.type = type
        self.transactionTime = transactionTime
        self.amount = amount
        self.account1 = account1
        
        pass
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



class Login:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        
        pass
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

