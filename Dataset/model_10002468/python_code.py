from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class UserState(Enum):
    pass
class OrderStatus(Enum):
    pass

############################################
# Definition of Classes
############################################










class Product:

    def __init__(self, name: str, description: str, lineItems12: set["LineItem"] = None):
        self.name = name
        self.description = description
        self.lineItems12 = lineItems12 if lineItems12 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def lineItems12(self):
        return self.__lineItems12
    @lineItems12.setter
    def lineItems12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__lineItems12", None)
        self.__lineItems12 = value if value is not None else set()
        
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
                    



class LineItem:

    def __init__(self, quantity: int, price: float, sc11: "ShoppingCart" = None, product13: "Product" = None, order15: "Order" = None):
        self.quantity = quantity
        self.price = price
        self.sc11 = sc11
        self.product13 = product13
        self.order15 = order15
        
        pass
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
    def sc11(self):
        return self.__sc11
    @sc11.setter
    def sc11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__sc11", None)
        self.__sc11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items10"):
                opp_val = getattr(old_value, "items10", None)
                if opp_val == self:
                    setattr(old_value, "items10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items10"):
                opp_val = getattr(value, "items10", None)
                setattr(value, "items10", self)

    @property
    def order15(self):
        return self.__order15
    @order15.setter
    def order15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__order15", None)
        self.__order15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items14"):
                opp_val = getattr(old_value, "items14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items14"):
                opp_val = getattr(value, "items14", None)
                if opp_val is None:
                    setattr(value, "items14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product13(self):
        return self.__product13
    @product13.setter
    def product13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__product13", None)
        self.__product13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lineItems12"):
                opp_val = getattr(old_value, "lineItems12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lineItems12"):
                opp_val = getattr(value, "lineItems12", None)
                if opp_val is None:
                    setattr(value, "lineItems12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order:

    def __init__(self, number: int, ordered: date, shipped: bool, shipTo: str, total: float, status: OrderStatus, items14: set["LineItem"] = None, account17: "Account" = None, payment19: "Payment" = None):
        self.number = number
        self.ordered = ordered
        self.shipped = shipped
        self.shipTo = shipTo
        self.total = total
        self.status = status
        self.items14 = items14 if items14 is not None else set()
        self.account17 = account17
        self.payment19 = payment19
        
        pass
    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def shipTo(self):
        return self.__shipTo
    @shipTo.setter
    def shipTo(self, shipTo: str):
        self.__shipTo = shipTo

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
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: OrderStatus):
        self.__status = status

    @property
    def shipped(self):
        return self.__shipped
    @shipped.setter
    def shipped(self, shipped: bool):
        self.__shipped = shipped

    @property
    def payment19(self):
        return self.__payment19
    @payment19.setter
    def payment19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment19", None)
        self.__payment19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order18"):
                opp_val = getattr(old_value, "order18", None)
                if opp_val == self:
                    setattr(old_value, "order18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order18"):
                opp_val = getattr(value, "order18", None)
                setattr(value, "order18", self)

    @property
    def account17(self):
        return self.__account17
    @account17.setter
    def account17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__account17", None)
        self.__account17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order16"):
                opp_val = getattr(old_value, "order16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order16"):
                opp_val = getattr(value, "order16", None)
                if opp_val is None:
                    setattr(value, "order16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def items14(self):
        return self.__items14
    @items14.setter
    def items14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__items14", None)
        self.__items14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order15"):
                    opp_val = getattr(item, "order15", None)
                    
                    if opp_val == self:
                        setattr(item, "order15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order15"):
                    opp_val = getattr(item, "order15", None)
                    
                    setattr(item, "order15", self)
                    



class WebUser:

    def __init__(self, login: str, password: str, state: UserState, shoppingCart2: "ShoppingCart" = None, customer4: "Customer" = None):
        self.login = login
        self.password = password
        self.state = state
        self.shoppingCart2 = shoppingCart2
        self.customer4 = customer4
        
        pass
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
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: UserState):
        self.__state = state

    @property
    def customer4(self):
        return self.__customer4
    @customer4.setter
    def customer4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebUser__customer4", None)
        self.__customer4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webUser5"):
                opp_val = getattr(old_value, "webUser5", None)
                if opp_val == self:
                    setattr(old_value, "webUser5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webUser5"):
                opp_val = getattr(value, "webUser5", None)
                setattr(value, "webUser5", self)

    @property
    def shoppingCart2(self):
        return self.__shoppingCart2
    @shoppingCart2.setter
    def shoppingCart2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebUser__shoppingCart2", None)
        self.__shoppingCart2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webUser3"):
                opp_val = getattr(old_value, "webUser3", None)
                if opp_val == self:
                    setattr(old_value, "webUser3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webUser3"):
                opp_val = getattr(value, "webUser3", None)
                setattr(value, "webUser3", self)



class Account:

    def __init__(self, billingAddress: str, open: date, closed: date, isClosed: bool, order16: set["Order"] = None, p0: set["Payment"] = None, customer7: "Customer" = None, cart8: "ShoppingCart" = None):
        self.billingAddress = billingAddress
        self.open = open
        self.closed = closed
        self.isClosed = isClosed
        self.order16 = order16 if order16 is not None else set()
        self.p0 = p0 if p0 is not None else set()
        self.customer7 = customer7
        self.cart8 = cart8
        
        pass
    @property
    def open(self):
        return self.__open
    @open.setter
    def open(self, open: date):
        self.__open = open

    @property
    def billingAddress(self):
        return self.__billingAddress
    @billingAddress.setter
    def billingAddress(self, billingAddress: str):
        self.__billingAddress = billingAddress

    @property
    def isClosed(self):
        return self.__isClosed
    @isClosed.setter
    def isClosed(self, isClosed: bool):
        self.__isClosed = isClosed

    @property
    def closed(self):
        return self.__closed
    @closed.setter
    def closed(self, closed: date):
        self.__closed = closed

    @property
    def p0(self):
        return self.__p0
    @p0.setter
    def p0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__p0", None)
        self.__p0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "acc1"):
                    opp_val = getattr(item, "acc1", None)
                    
                    if opp_val == self:
                        setattr(item, "acc1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "acc1"):
                    opp_val = getattr(item, "acc1", None)
                    
                    setattr(item, "acc1", self)
                    

    @property
    def order16(self):
        return self.__order16
    @order16.setter
    def order16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__order16", None)
        self.__order16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account17"):
                    opp_val = getattr(item, "account17", None)
                    
                    if opp_val == self:
                        setattr(item, "account17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account17"):
                    opp_val = getattr(item, "account17", None)
                    
                    setattr(item, "account17", self)
                    

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
    def cart8(self):
        return self.__cart8
    @cart8.setter
    def cart8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__cart8", None)
        self.__cart8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account9"):
                opp_val = getattr(old_value, "account9", None)
                if opp_val == self:
                    setattr(old_value, "account9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account9"):
                opp_val = getattr(value, "account9", None)
                setattr(value, "account9", self)



class ShoppingCart:

    def __init__(self, creationDate: date, items10: "LineItem" = None, webUser3: "WebUser" = None, account9: "Account" = None):
        self.creationDate = creationDate
        self.items10 = items10
        self.webUser3 = webUser3
        self.account9 = account9
        
        pass
    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def webUser3(self):
        return self.__webUser3
    @webUser3.setter
    def webUser3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__webUser3", None)
        self.__webUser3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart2"):
                opp_val = getattr(old_value, "shoppingCart2", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart2"):
                opp_val = getattr(value, "shoppingCart2", None)
                setattr(value, "shoppingCart2", self)

    @property
    def items10(self):
        return self.__items10
    @items10.setter
    def items10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__items10", None)
        self.__items10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sc11"):
                opp_val = getattr(old_value, "sc11", None)
                if opp_val == self:
                    setattr(old_value, "sc11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sc11"):
                opp_val = getattr(value, "sc11", None)
                setattr(value, "sc11", self)

    @property
    def account9(self):
        return self.__account9
    @account9.setter
    def account9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__account9", None)
        self.__account9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart8"):
                opp_val = getattr(old_value, "cart8", None)
                if opp_val == self:
                    setattr(old_value, "cart8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart8"):
                opp_val = getattr(value, "cart8", None)
                setattr(value, "cart8", self)



class Payment:

    def __init__(self, paidDate: date, total: float, details: str, order18: "Order" = None, acc1: "Account" = None):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        self.order18 = order18
        self.acc1 = acc1
        
        pass
    @property
    def details(self):
        return self.__details
    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def paidDate(self):
        return self.__paidDate
    @paidDate.setter
    def paidDate(self, paidDate: date):
        self.__paidDate = paidDate

    @property
    def acc1(self):
        return self.__acc1
    @acc1.setter
    def acc1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__acc1", None)
        self.__acc1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p0"):
                opp_val = getattr(old_value, "p0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p0"):
                opp_val = getattr(value, "p0", None)
                if opp_val is None:
                    setattr(value, "p0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order18(self):
        return self.__order18
    @order18.setter
    def order18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order18", None)
        self.__order18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment19"):
                opp_val = getattr(old_value, "payment19", None)
                if opp_val == self:
                    setattr(old_value, "payment19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment19"):
                opp_val = getattr(value, "payment19", None)
                setattr(value, "payment19", self)



class Customer:

    def __init__(self, address: str, phone: str, email: str, webUser5: "WebUser" = None, account6: "Account" = None):
        self.address = address
        self.phone = phone
        self.email = email
        self.webUser5 = webUser5
        self.account6 = account6
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def webUser5(self):
        return self.__webUser5
    @webUser5.setter
    def webUser5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__webUser5", None)
        self.__webUser5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer4"):
                opp_val = getattr(old_value, "customer4", None)
                if opp_val == self:
                    setattr(old_value, "customer4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer4"):
                opp_val = getattr(value, "customer4", None)
                setattr(value, "customer4", self)

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

