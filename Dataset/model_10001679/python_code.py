from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class SavingAccount:

    def __init__(self, accountNo: int, balance: int, currentAccount9: "CurrentAccount" = None):
        self.accountNo = accountNo
        self.balance = balance
        self.currentAccount9 = currentAccount9
        
        pass
    @property
    def accountNo(self):
        return self.__accountNo
    @accountNo.setter
    def accountNo(self, accountNo: int):
        self.__accountNo = accountNo

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: int):
        self.__balance = balance

    @property
    def currentAccount9(self):
        return self.__currentAccount9
    @currentAccount9.setter
    def currentAccount9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SavingAccount__currentAccount9", None)
        self.__currentAccount9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "savingchecking8"):
                opp_val = getattr(old_value, "savingchecking8", None)
                if opp_val == self:
                    setattr(old_value, "savingchecking8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "savingchecking8"):
                opp_val = getattr(value, "savingchecking8", None)
                setattr(value, "savingchecking8", self)



class CurrentAccount:

    def __init__(self, accountNo: int, balance: int, savingchecking8: "SavingAccount" = None):
        self.accountNo = accountNo
        self.balance = balance
        self.savingchecking8 = savingchecking8
        
        pass
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: int):
        self.__balance = balance

    @property
    def accountNo(self):
        return self.__accountNo
    @accountNo.setter
    def accountNo(self, accountNo: int):
        self.__accountNo = accountNo

    @property
    def savingchecking8(self):
        return self.__savingchecking8
    @savingchecking8.setter
    def savingchecking8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CurrentAccount__savingchecking8", None)
        self.__savingchecking8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "currentAccount9"):
                opp_val = getattr(old_value, "currentAccount9", None)
                if opp_val == self:
                    setattr(old_value, "currentAccount9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "currentAccount9"):
                opp_val = getattr(value, "currentAccount9", None)
                setattr(value, "currentAccount9", self)



class ATMTransactions:

    def __init__(self, transactionid: int, date: str, type: str, amount: int, postBalance: int, account7: "Account" = None):
        self.transactionid = transactionid
        self.date = date
        self.type = type
        self.amount = amount
        self.postBalance = postBalance
        self.account7 = account7
        
        pass
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def postBalance(self):
        return self.__postBalance
    @postBalance.setter
    def postBalance(self, postBalance: int):
        self.__postBalance = postBalance

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

    @property
    def transactionid(self):
        return self.__transactionid
    @transactionid.setter
    def transactionid(self, transactionid: int):
        self.__transactionid = transactionid

    @property
    def account7(self):
        return self.__account7
    @account7.setter
    def account7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATMTransactions__account7", None)
        self.__account7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATMTransactions6"):
                opp_val = getattr(old_value, "ATMTransactions6", None)
                if opp_val == self:
                    setattr(old_value, "ATMTransactions6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATMTransactions6"):
                opp_val = getattr(value, "ATMTransactions6", None)
                setattr(value, "ATMTransactions6", self)



class ATM:

    def __init__(self, location: str, managedBy: str, bank1: "Bank" = None):
        self.location = location
        self.managedBy = managedBy
        self.bank1 = bank1
        
        pass
    @property
    def managedBy(self):
        return self.__managedBy
    @managedBy.setter
    def managedBy(self, managedBy: str):
        self.__managedBy = managedBy

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def bank1(self):
        return self.__bank1
    @bank1.setter
    def bank1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATM__bank1", None)
        self.__bank1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aTM0"):
                opp_val = getattr(old_value, "aTM0", None)
                if opp_val == self:
                    setattr(old_value, "aTM0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aTM0"):
                opp_val = getattr(value, "aTM0", None)
                setattr(value, "aTM0", self)



class Account:

    def __init__(self, number: int, balance: int, customer5: "Customer" = None, ATMTransactions6: "ATMTransactions" = None, bank3: "Bank" = None):
        self.number = number
        self.balance = balance
        self.customer5 = customer5
        self.ATMTransactions6 = ATMTransactions6
        self.bank3 = bank3
        
        pass
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: int):
        self.__balance = balance

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def bank3(self):
        return self.__bank3
    @bank3.setter
    def bank3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__bank3", None)
        self.__bank3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account2"):
                opp_val = getattr(old_value, "account2", None)
                if opp_val == self:
                    setattr(old_value, "account2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account2"):
                opp_val = getattr(value, "account2", None)
                setattr(value, "account2", self)

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__customer5", None)
        self.__customer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account4"):
                opp_val = getattr(old_value, "account4", None)
                if opp_val == self:
                    setattr(old_value, "account4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account4"):
                opp_val = getattr(value, "account4", None)
                setattr(value, "account4", self)

    @property
    def ATMTransactions6(self):
        return self.__ATMTransactions6
    @ATMTransactions6.setter
    def ATMTransactions6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__ATMTransactions6", None)
        self.__ATMTransactions6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account7"):
                opp_val = getattr(old_value, "account7", None)
                if opp_val == self:
                    setattr(old_value, "account7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account7"):
                opp_val = getattr(value, "account7", None)
                setattr(value, "account7", self)



class Customer:

    def __init__(self, name: str, address: str, dob: str, cardno: int, pin: int, account4: "Account" = None):
        self.name = name
        self.address = address
        self.dob = dob
        self.cardno = cardno
        self.pin = pin
        self.account4 = account4
        
        pass
    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def pin(self, pin: int):
        self.__pin = pin

    @property
    def dob(self):
        return self.__dob
    @dob.setter
    def dob(self, dob: str):
        self.__dob = dob

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cardno(self):
        return self.__cardno
    @cardno.setter
    def cardno(self, cardno: int):
        self.__cardno = cardno

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def account4(self):
        return self.__account4
    @account4.setter
    def account4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__account4", None)
        self.__account4 = value
        
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



class Bank:

    def __init__(self, code: int, address: str, aTM0: "ATM" = None, account2: "Account" = None):
        self.code = code
        self.address = address
        self.aTM0 = aTM0
        self.account2 = account2
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, code: int):
        self.__code = code

    @property
    def aTM0(self):
        return self.__aTM0
    @aTM0.setter
    def aTM0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bank__aTM0", None)
        self.__aTM0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank1"):
                opp_val = getattr(old_value, "bank1", None)
                if opp_val == self:
                    setattr(old_value, "bank1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank1"):
                opp_val = getattr(value, "bank1", None)
                setattr(value, "bank1", self)

    @property
    def account2(self):
        return self.__account2
    @account2.setter
    def account2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bank__account2", None)
        self.__account2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank3"):
                opp_val = getattr(old_value, "bank3", None)
                if opp_val == self:
                    setattr(old_value, "bank3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank3"):
                opp_val = getattr(value, "bank3", None)
                setattr(value, "bank3", self)

