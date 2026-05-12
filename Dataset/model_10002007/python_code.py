from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Customer:

    def __init__(self, name: str, address: str, dob: str, cardnumber: int, pin: int, account4: "Account" = None):
        self.name = name
        self.address = address
        self.dob = dob
        self.cardnumber = cardnumber
        self.pin = pin
        self.account4 = account4
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dob(self):
        return self.__dob
    @dob.setter
    def dob(self, dob: str):
        self.__dob = dob

    @property
    def cardnumber(self):
        return self.__cardnumber
    @cardnumber.setter
    def cardnumber(self, cardnumber: int):
        self.__cardnumber = cardnumber

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def pin(self, pin: int):
        self.__pin = pin

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



class Account:

    def __init__(self, number: int, balance: int, bank3: "Bank" = None, customer5: "Customer" = None):
        self.number = number
        self.balance = balance
        self.bank3 = bank3
        self.customer5 = customer5
        
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



class ATM:

    def __init__(self, location: str, managedby: str, bank1: "Bank" = None):
        self.location = location
        self.managedby = managedby
        self.bank1 = bank1
        
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

