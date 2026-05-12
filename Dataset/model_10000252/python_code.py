from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class OrderStatus(Enum):
    pass

############################################
# Definition of Classes
############################################










class Customer:

    def __init__(self, firstname: str, lastname: str, emailAddress: str, id: int, login: str, password: str, isBan: bool, cart1: "ShoppingCart" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.emailAddress = emailAddress
        self.id = id
        self.login = login
        self.password = password
        self.isBan = isBan
        self.cart1 = cart1
        
        pass
    @property
    def lastname(self):
        return self.__lastname
    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def isBan(self):
        return self.__isBan
    @isBan.setter
    def isBan(self, isBan: bool):
        self.__isBan = isBan

    @property
    def firstname(self):
        return self.__firstname
    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def emailAddress(self):
        return self.__emailAddress
    @emailAddress.setter
    def emailAddress(self, emailAddress: str):
        self.__emailAddress = emailAddress

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def cart1(self):
        return self.__cart1
    @cart1.setter
    def cart1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__cart1", None)
        self.__cart1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c0"):
                opp_val = getattr(old_value, "c0", None)
                if opp_val == self:
                    setattr(old_value, "c0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c0"):
                opp_val = getattr(value, "c0", None)
                setattr(value, "c0", self)



class Order:

    def __init__(self, id: int, shippingAddress: str, finalTotal: float, status: OrderStatus):
        self.id = id
        self.shippingAddress = shippingAddress
        self.finalTotal = finalTotal
        self.status = status
        
        pass
    @property
    def finalTotal(self):
        return self.__finalTotal
    @finalTotal.setter
    def finalTotal(self, finalTotal: float):
        self.__finalTotal = finalTotal

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def shippingAddress(self):
        return self.__shippingAddress
    @shippingAddress.setter
    def shippingAddress(self, shippingAddress: str):
        self.__shippingAddress = shippingAddress

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: OrderStatus):
        self.__status = status



class Payment:

    def __init__(self, id: int, total: int, comments: str):
        self.id = id
        self.total = total
        self.comments = comments
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def comments(self):
        return self.__comments
    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: int):
        self.__total = total



class Account:

    def __init__(self, id: int, openDate: date, billingAddress: str):
        self.id = id
        self.openDate = openDate
        self.billingAddress = billingAddress
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def billingAddress(self):
        return self.__billingAddress
    @billingAddress.setter
    def billingAddress(self, billingAddress: str):
        self.__billingAddress = billingAddress

    @property
    def openDate(self):
        return self.__openDate
    @openDate.setter
    def openDate(self, openDate: date):
        self.__openDate = openDate



class Product:

    def __init__(self, name: str, id: int, description: str, item2: set["Item"] = None):
        self.name = name
        self.id = id
        self.description = description
        self.item2 = item2 if item2 is not None else set()
        
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

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def item2(self):
        return self.__item2
    @item2.setter
    def item2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__item2", None)
        self.__item2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product3"):
                    opp_val = getattr(item, "product3", None)
                    
                    if opp_val == self:
                        setattr(item, "product3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product3"):
                    opp_val = getattr(item, "product3", None)
                    
                    setattr(item, "product3", self)
                    



class Item:

    def __init__(self, quantity: int, price: float, id: int, product3: "Product" = None):
        self.quantity = quantity
        self.price = price
        self.id = id
        self.product3 = product3
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def product3(self):
        return self.__product3
    @product3.setter
    def product3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__product3", None)
        self.__product3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item2"):
                opp_val = getattr(old_value, "item2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item2"):
                opp_val = getattr(value, "item2", None)
                if opp_val is None:
                    setattr(value, "item2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ShoppingCart:

    def __init__(self, id: int, creationDate: date, c0: "Customer" = None):
        self.id = id
        self.creationDate = creationDate
        self.c0 = c0
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def c0(self):
        return self.__c0
    @c0.setter
    def c0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__c0", None)
        self.__c0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart1"):
                opp_val = getattr(old_value, "cart1", None)
                if opp_val == self:
                    setattr(old_value, "cart1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart1"):
                opp_val = getattr(value, "cart1", None)
                setattr(value, "cart1", self)

