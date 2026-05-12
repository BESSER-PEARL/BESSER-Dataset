from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class ATM_Transactions:

    def __init__(self, transation_ID: str, date: str, type: str, amount: str, post_balance: str, account1: "Account" = None):
        self.transation_ID = transation_ID
        self.date = date
        self.type = type
        self.amount = amount
        self.post_balance = post_balance
        self.account1 = account1
        
        pass
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def post_balance(self):
        return self.__post_balance
    @post_balance.setter
    def post_balance(self, post_balance: str):
        self.__post_balance = post_balance

    @property
    def transation_ID(self):
        return self.__transation_ID
    @transation_ID.setter
    def transation_ID(self, transation_ID: str):
        self.__transation_ID = transation_ID

    @property
    def account1(self):
        return self.__account1
    @account1.setter
    def account1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATM_Transactions__account1", None)
        self.__account1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aTM_Transactions0"):
                opp_val = getattr(old_value, "aTM_Transactions0", None)
                if opp_val == self:
                    setattr(old_value, "aTM_Transactions0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aTM_Transactions0"):
                opp_val = getattr(value, "aTM_Transactions0", None)
                setattr(value, "aTM_Transactions0", self)



class Savings_Account:

    pass


class Checking_Account:

    pass


class Account:

    def __init__(self, number: str, balance: str, aTM_Transactions0: "ATM_Transactions" = None, bank5: "Bank" = None, customer7: "Customer" = None):
        self.number = number
        self.balance = balance
        self.aTM_Transactions0 = aTM_Transactions0
        self.bank5 = bank5
        self.customer7 = customer7
        
        pass
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: str):
        self.__balance = balance

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def customer7(self):
        return self.__customer7
    @customer7.setter
    def customer7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__customer7", None)
        self.__customer7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account6"):
                opp_val = getattr(old_value, "account6", None)
                if opp_val == self:
                    setattr(old_value, "account6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account6"):
                opp_val = getattr(value, "account6", None)
                setattr(value, "account6", self)

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
                if opp_val == self:
                    setattr(old_value, "account4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account4"):
                opp_val = getattr(value, "account4", None)
                setattr(value, "account4", self)

    @property
    def aTM_Transactions0(self):
        return self.__aTM_Transactions0
    @aTM_Transactions0.setter
    def aTM_Transactions0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__aTM_Transactions0", None)
        self.__aTM_Transactions0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account1"):
                opp_val = getattr(old_value, "account1", None)
                if opp_val == self:
                    setattr(old_value, "account1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account1"):
                opp_val = getattr(value, "account1", None)
                setattr(value, "account1", self)



class Customer:

    def __init__(self, name: str, address: str, dob: str, card_number: str, pin: str, account6: "Account" = None):
        self.name = name
        self.address = address
        self.dob = dob
        self.card_number = card_number
        self.pin = pin
        self.account6 = account6
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def card_number(self):
        return self.__card_number
    @card_number.setter
    def card_number(self, card_number: str):
        self.__card_number = card_number

    @property
    def dob(self):
        return self.__dob
    @dob.setter
    def dob(self, dob: str):
        self.__dob = dob

    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def account6(self):
        return self.__account6
    @account6.setter
    def account6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__account6", None)
        self.__account6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer7"):
                opp_val = getattr(old_value, "customer7", None)
                if opp_val == self:
                    setattr(old_value, "customer7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer7"):
                opp_val = getattr(value, "customer7", None)
                setattr(value, "customer7", self)



class ATM:

    def __init__(self, location: str, managedby: str, bank3: "Bank" = None):
        self.location = location
        self.managedby = managedby
        self.bank3 = bank3
        
        pass
    @property
    def managedby(self):
        return self.__managedby
    @managedby.setter
    def managedby(self, managedby: str):
        self.__managedby = managedby

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def bank3(self):
        return self.__bank3
    @bank3.setter
    def bank3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATM__bank3", None)
        self.__bank3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aTM2"):
                opp_val = getattr(old_value, "aTM2", None)
                if opp_val == self:
                    setattr(old_value, "aTM2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aTM2"):
                opp_val = getattr(value, "aTM2", None)
                setattr(value, "aTM2", self)



class Bank:

    def __init__(self, code: str, address: str, aTM2: "ATM" = None, account4: "Account" = None):
        self.code = code
        self.address = address
        self.aTM2 = aTM2
        self.account4 = account4
        
        pass
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, code: str):
        self.__code = code

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
        old_value = getattr(self, f"_Bank__account4", None)
        self.__account4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank5"):
                opp_val = getattr(old_value, "bank5", None)
                if opp_val == self:
                    setattr(old_value, "bank5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank5"):
                opp_val = getattr(value, "bank5", None)
                setattr(value, "bank5", self)

    @property
    def aTM2(self):
        return self.__aTM2
    @aTM2.setter
    def aTM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bank__aTM2", None)
        self.__aTM2 = value
        
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

