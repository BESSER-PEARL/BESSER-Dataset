from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class UserState(Enum):
    pass

############################################
# Definition of Classes
############################################










class Product:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class Order:

    def __init__(self, number: int, ordered: date, shipped: bool, shipTo: str, total: float, status: str, payment1: "Payment" = None):
        self.number = number
        self.ordered = ordered
        self.shipped = shipped
        self.shipTo = shipTo
        self.total = total
        self.status = status
        self.payment1 = payment1
        
        pass
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def ordered(self):
        return self.__ordered
    @ordered.setter
    def ordered(self, ordered: date):
        self.__ordered = ordered

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def shipped(self):
        return self.__shipped
    @shipped.setter
    def shipped(self, shipped: bool):
        self.__shipped = shipped

    @property
    def shipTo(self):
        return self.__shipTo
    @shipTo.setter
    def shipTo(self, shipTo: str):
        self.__shipTo = shipTo

    @property
    def payment1(self):
        return self.__payment1
    @payment1.setter
    def payment1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment1", None)
        self.__payment1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order0"):
                opp_val = getattr(old_value, "order0", None)
                if opp_val == self:
                    setattr(old_value, "order0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order0"):
                opp_val = getattr(value, "order0", None)
                setattr(value, "order0", self)



class ShoppingCart:

    def __init__(self, creationDate: date):
        self.creationDate = creationDate
        
        pass
    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate



class Payment:

    def __init__(self, paidDate: date, total: float, details: str, order0: "Order" = None):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        self.order0 = order0
        
        pass
    @property
    def paidDate(self):
        return self.__paidDate
    @paidDate.setter
    def paidDate(self, paidDate: date):
        self.__paidDate = paidDate

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def details(self):
        return self.__details
    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def order0(self):
        return self.__order0
    @order0.setter
    def order0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order0", None)
        self.__order0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment1"):
                opp_val = getattr(old_value, "payment1", None)
                if opp_val == self:
                    setattr(old_value, "payment1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment1"):
                opp_val = getattr(value, "payment1", None)
                setattr(value, "payment1", self)



class Customer:

    def __init__(self, address: str, phone: str, email: str):
        self.address = address
        self.phone = phone
        self.email = email
        
        pass
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

