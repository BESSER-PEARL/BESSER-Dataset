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

    def __init__(self, firstname: str, lastname: str, emailAddress: str, id: int, login: str, password: str, isBan: bool, cart1: "ShoppingCart" = None, account3: "Account" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.emailAddress = emailAddress
        self.id = id
        self.login = login
        self.password = password
        self.isBan = isBan
        self.cart1 = cart1
        self.account3 = account3
        
        pass
    @property
    def lastname(self):
        return self.__lastname
    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def emailAddress(self):
        return self.__emailAddress
    @emailAddress.setter
    def emailAddress(self, emailAddress: str):
        self.__emailAddress = emailAddress

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
    def account3(self):
        return self.__account3
    @account3.setter
    def account3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__account3", None)
        self.__account3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer2"):
                opp_val = getattr(old_value, "customer2", None)
                if opp_val == self:
                    setattr(old_value, "customer2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer2"):
                opp_val = getattr(value, "customer2", None)
                setattr(value, "customer2", self)

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

    def __init__(self, id: int, shippingAddress: str, finalTotal: float, status: OrderStatus, payment8: "Payment" = None):
        self.id = id
        self.shippingAddress = shippingAddress
        self.finalTotal = finalTotal
        self.status = status
        self.payment8 = payment8
        
        pass
    @property
    def finalTotal(self):
        return self.__finalTotal
    @finalTotal.setter
    def finalTotal(self, finalTotal: float):
        self.__finalTotal = finalTotal

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: OrderStatus):
        self.__status = status

    @property
    def shippingAddress(self):
        return self.__shippingAddress
    @shippingAddress.setter
    def shippingAddress(self, shippingAddress: str):
        self.__shippingAddress = shippingAddress

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def payment8(self):
        return self.__payment8
    @payment8.setter
    def payment8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment8", None)
        self.__payment8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order9"):
                opp_val = getattr(old_value, "order9", None)
                if opp_val == self:
                    setattr(old_value, "order9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order9"):
                opp_val = getattr(value, "order9", None)
                setattr(value, "order9", self)



class Payment:

    def __init__(self, id: int, total: int, comments: str, acc6: "Account" = None, order9: "Order" = None):
        self.id = id
        self.total = total
        self.comments = comments
        self.acc6 = acc6
        self.order9 = order9
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: int):
        self.__total = total

    @property
    def comments(self):
        return self.__comments
    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def order9(self):
        return self.__order9
    @order9.setter
    def order9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order9", None)
        self.__order9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment8"):
                opp_val = getattr(old_value, "payment8", None)
                if opp_val == self:
                    setattr(old_value, "payment8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment8"):
                opp_val = getattr(value, "payment8", None)
                setattr(value, "payment8", self)

    @property
    def acc6(self):
        return self.__acc6
    @acc6.setter
    def acc6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__acc6", None)
        self.__acc6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment7"):
                opp_val = getattr(old_value, "payment7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment7"):
                opp_val = getattr(value, "payment7", None)
                if opp_val is None:
                    setattr(value, "payment7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Account:

    def __init__(self, id: int, openDate: date, billingAddress: str, customer2: "Customer" = None, shoppingcart5: "ShoppingCart" = None, payment7: set["Payment"] = None):
        self.id = id
        self.openDate = openDate
        self.billingAddress = billingAddress
        self.customer2 = customer2
        self.shoppingcart5 = shoppingcart5
        self.payment7 = payment7 if payment7 is not None else set()
        
        pass
    @property
    def openDate(self):
        return self.__openDate
    @openDate.setter
    def openDate(self, openDate: date):
        self.__openDate = openDate

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
    def payment7(self):
        return self.__payment7
    @payment7.setter
    def payment7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__payment7", None)
        self.__payment7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "acc6"):
                    opp_val = getattr(item, "acc6", None)
                    
                    if opp_val == self:
                        setattr(item, "acc6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "acc6"):
                    opp_val = getattr(item, "acc6", None)
                    
                    setattr(item, "acc6", self)
                    

    @property
    def shoppingcart5(self):
        return self.__shoppingcart5
    @shoppingcart5.setter
    def shoppingcart5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__shoppingcart5", None)
        self.__shoppingcart5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accnt4"):
                opp_val = getattr(old_value, "accnt4", None)
                if opp_val == self:
                    setattr(old_value, "accnt4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accnt4"):
                opp_val = getattr(value, "accnt4", None)
                setattr(value, "accnt4", self)

    @property
    def customer2(self):
        return self.__customer2
    @customer2.setter
    def customer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__customer2", None)
        self.__customer2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account3"):
                opp_val = getattr(old_value, "account3", None)
                if opp_val == self:
                    setattr(old_value, "account3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account3"):
                opp_val = getattr(value, "account3", None)
                setattr(value, "account3", self)



class Product:

    def __init__(self, name: str, id: int, description: str, item12: set["Item"] = None):
        self.name = name
        self.id = id
        self.description = description
        self.item12 = item12 if item12 is not None else set()
        
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
    def item12(self):
        return self.__item12
    @item12.setter
    def item12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__item12", None)
        self.__item12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product13"):
                    opp_val = getattr(item, "product13", None)
                    
                    if opp_val == self:
                        setattr(item, "product13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product13"):
                    opp_val = getattr(item, "product13", None)
                    
                    setattr(item, "product13", self)
                    



class Item:

    def __init__(self, quantity: int, price: float, id: int, shoppingcart10: "ShoppingCart" = None, product13: "Product" = None):
        self.quantity = quantity
        self.price = price
        self.id = id
        self.shoppingcart10 = shoppingcart10
        self.product13 = product13
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

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
    def shoppingcart10(self):
        return self.__shoppingcart10
    @shoppingcart10.setter
    def shoppingcart10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__shoppingcart10", None)
        self.__shoppingcart10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item11"):
                opp_val = getattr(old_value, "item11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item11"):
                opp_val = getattr(value, "item11", None)
                if opp_val is None:
                    setattr(value, "item11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product13(self):
        return self.__product13
    @product13.setter
    def product13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__product13", None)
        self.__product13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item12"):
                opp_val = getattr(old_value, "item12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item12"):
                opp_val = getattr(value, "item12", None)
                if opp_val is None:
                    setattr(value, "item12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ShoppingCart:

    def __init__(self, id: int, creationDate: date, c0: "Customer" = None, accnt4: "Account" = None, item11: set["Item"] = None):
        self.id = id
        self.creationDate = creationDate
        self.c0 = c0
        self.accnt4 = accnt4
        self.item11 = item11 if item11 is not None else set()
        
        pass
    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def item11(self):
        return self.__item11
    @item11.setter
    def item11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__item11", None)
        self.__item11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shoppingcart10"):
                    opp_val = getattr(item, "shoppingcart10", None)
                    
                    if opp_val == self:
                        setattr(item, "shoppingcart10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shoppingcart10"):
                    opp_val = getattr(item, "shoppingcart10", None)
                    
                    setattr(item, "shoppingcart10", self)
                    

    @property
    def accnt4(self):
        return self.__accnt4
    @accnt4.setter
    def accnt4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__accnt4", None)
        self.__accnt4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingcart5"):
                opp_val = getattr(old_value, "shoppingcart5", None)
                if opp_val == self:
                    setattr(old_value, "shoppingcart5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingcart5"):
                opp_val = getattr(value, "shoppingcart5", None)
                setattr(value, "shoppingcart5", self)

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

