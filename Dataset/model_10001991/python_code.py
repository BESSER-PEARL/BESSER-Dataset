from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class OrderStatus(Enum):
    pass
class UserState(Enum):
    pass

############################################
# Definition of Classes
############################################







class AjoutProduit_UseCase:

    pass


class Webuser_Actor:

    pass


class Admin_Actor:

    pass


class MyActor_Actor:

    pass





class Product:

    def __init__(self, name: str, description: str, item12: set["LineItem"] = None):
        self.name = name
        self.description = description
        self.item12 = item12 if item12 is not None else set()
        
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
                    



class LineItem:

    def __init__(self, quantity: int, price: float, lineitem15: set["Order"] = None, sc19: "ShoppinCart" = None, product13: "Product" = None):
        self.quantity = quantity
        self.price = price
        self.lineitem15 = lineitem15 if lineitem15 is not None else set()
        self.sc19 = sc19
        self.product13 = product13
        
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
    def sc19(self):
        return self.__sc19
    @sc19.setter
    def sc19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__sc19", None)
        self.__sc19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items18"):
                opp_val = getattr(old_value, "items18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items18"):
                opp_val = getattr(value, "items18", None)
                if opp_val is None:
                    setattr(value, "items18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lineitem15(self):
        return self.__lineitem15
    @lineitem15.setter
    def lineitem15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__lineitem15", None)
        self.__lineitem15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "items14"):
                    opp_val = getattr(item, "items14", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "items14"):
                    opp_val = getattr(item, "items14", None)
                    
                    if opp_val is None:
                        setattr(item, "items14", set([self]))
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



class Order:

    def __init__(self, number: int, ordered: date, shipped: bool, shipTo: str, total: float, status: OrderStatus, items14: set["LineItem"] = None, order3: set["Payment"] = None, account5: "Account" = None):
        self.number = number
        self.ordered = ordered
        self.shipped = shipped
        self.shipTo = shipTo
        self.total = total
        self.status = status
        self.items14 = items14 if items14 is not None else set()
        self.order3 = order3 if order3 is not None else set()
        self.account5 = account5
        
        pass
    @property
    def shipTo(self):
        return self.__shipTo
    @shipTo.setter
    def shipTo(self, shipTo: str):
        self.__shipTo = shipTo

    @property
    def shipped(self):
        return self.__shipped
    @shipped.setter
    def shipped(self, shipped: bool):
        self.__shipped = shipped

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
    def status(self, status: OrderStatus):
        self.__status = status

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
                if hasattr(item, "lineitem15"):
                    opp_val = getattr(item, "lineitem15", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lineitem15"):
                    opp_val = getattr(item, "lineitem15", None)
                    
                    if opp_val is None:
                        setattr(item, "lineitem15", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def order3(self):
        return self.__order3
    @order3.setter
    def order3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__order3", None)
        self.__order3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order2"):
                    opp_val = getattr(item, "order2", None)
                    
                    if opp_val == self:
                        setattr(item, "order2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order2"):
                    opp_val = getattr(item, "order2", None)
                    
                    setattr(item, "order2", self)
                    

    @property
    def account5(self):
        return self.__account5
    @account5.setter
    def account5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__account5", None)
        self.__account5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order4"):
                opp_val = getattr(old_value, "order4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order4"):
                opp_val = getattr(value, "order4", None)
                if opp_val is None:
                    setattr(value, "order4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class WebUser:

    def __init__(self, state: UserState, login: str, password: str, customer6: "Customer" = None, shoppincart9: "ShoppinCart" = None):
        self.state = state
        self.login = login
        self.password = password
        self.customer6 = customer6
        self.shoppincart9 = shoppincart9
        
        pass
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
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def customer6(self):
        return self.__customer6
    @customer6.setter
    def customer6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebUser__customer6", None)
        self.__customer6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webuser7"):
                opp_val = getattr(old_value, "webuser7", None)
                if opp_val == self:
                    setattr(old_value, "webuser7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webuser7"):
                opp_val = getattr(value, "webuser7", None)
                setattr(value, "webuser7", self)

    @property
    def shoppincart9(self):
        return self.__shoppincart9
    @shoppincart9.setter
    def shoppincart9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebUser__shoppincart9", None)
        self.__shoppincart9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webuser8"):
                opp_val = getattr(old_value, "webuser8", None)
                if opp_val == self:
                    setattr(old_value, "webuser8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webuser8"):
                opp_val = getattr(value, "webuser8", None)
                setattr(value, "webuser8", self)



class Account:

    def __init__(self, billingAddress: str, open: date, closed: date, isClosed: bool, cart16: "ShoppinCart" = None, payment0: set["Payment"] = None, order4: set["Order"] = None, customer11: "Customer" = None):
        self.billingAddress = billingAddress
        self.open = open
        self.closed = closed
        self.isClosed = isClosed
        self.cart16 = cart16
        self.payment0 = payment0 if payment0 is not None else set()
        self.order4 = order4 if order4 is not None else set()
        self.customer11 = customer11
        
        pass
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
    def open(self):
        return self.__open
    @open.setter
    def open(self, open: date):
        self.__open = open

    @property
    def closed(self):
        return self.__closed
    @closed.setter
    def closed(self, closed: date):
        self.__closed = closed

    @property
    def customer11(self):
        return self.__customer11
    @customer11.setter
    def customer11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__customer11", None)
        self.__customer11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "acc10"):
                opp_val = getattr(old_value, "acc10", None)
                if opp_val == self:
                    setattr(old_value, "acc10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "acc10"):
                opp_val = getattr(value, "acc10", None)
                setattr(value, "acc10", self)

    @property
    def cart16(self):
        return self.__cart16
    @cart16.setter
    def cart16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__cart16", None)
        self.__cart16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account17"):
                opp_val = getattr(old_value, "account17", None)
                if opp_val == self:
                    setattr(old_value, "account17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account17"):
                opp_val = getattr(value, "account17", None)
                setattr(value, "account17", self)

    @property
    def order4(self):
        return self.__order4
    @order4.setter
    def order4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__order4", None)
        self.__order4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account5"):
                    opp_val = getattr(item, "account5", None)
                    
                    if opp_val == self:
                        setattr(item, "account5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account5"):
                    opp_val = getattr(item, "account5", None)
                    
                    setattr(item, "account5", self)
                    

    @property
    def payment0(self):
        return self.__payment0
    @payment0.setter
    def payment0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__payment0", None)
        self.__payment0 = value if value is not None else set()
        
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
                    



class ShoppinCart:

    def __init__(self, creationDate: date, account17: "Account" = None, items18: set["LineItem"] = None, webuser8: "WebUser" = None):
        self.creationDate = creationDate
        self.account17 = account17
        self.items18 = items18 if items18 is not None else set()
        self.webuser8 = webuser8
        
        pass
    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def items18(self):
        return self.__items18
    @items18.setter
    def items18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppinCart__items18", None)
        self.__items18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sc19"):
                    opp_val = getattr(item, "sc19", None)
                    
                    if opp_val == self:
                        setattr(item, "sc19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sc19"):
                    opp_val = getattr(item, "sc19", None)
                    
                    setattr(item, "sc19", self)
                    

    @property
    def webuser8(self):
        return self.__webuser8
    @webuser8.setter
    def webuser8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppinCart__webuser8", None)
        self.__webuser8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppincart9"):
                opp_val = getattr(old_value, "shoppincart9", None)
                if opp_val == self:
                    setattr(old_value, "shoppincart9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppincart9"):
                opp_val = getattr(value, "shoppincart9", None)
                setattr(value, "shoppincart9", self)

    @property
    def account17(self):
        return self.__account17
    @account17.setter
    def account17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppinCart__account17", None)
        self.__account17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart16"):
                opp_val = getattr(old_value, "cart16", None)
                if opp_val == self:
                    setattr(old_value, "cart16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart16"):
                opp_val = getattr(value, "cart16", None)
                setattr(value, "cart16", self)



class Payment:

    def __init__(self, paidDate: date, total: float, details: str, account1: "Account" = None, order2: "Order" = None):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        self.account1 = account1
        self.order2 = order2
        
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
    def order2(self):
        return self.__order2
    @order2.setter
    def order2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order2", None)
        self.__order2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order3"):
                opp_val = getattr(old_value, "order3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order3"):
                opp_val = getattr(value, "order3", None)
                if opp_val is None:
                    setattr(value, "order3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def account1(self):
        return self.__account1
    @account1.setter
    def account1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__account1", None)
        self.__account1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment0"):
                opp_val = getattr(old_value, "payment0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment0"):
                opp_val = getattr(value, "payment0", None)
                if opp_val is None:
                    setattr(value, "payment0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Customer:

    def __init__(self, address: str, phone: str, email: str, webuser7: "WebUser" = None, acc10: "Account" = None):
        self.address = address
        self.phone = phone
        self.email = email
        self.webuser7 = webuser7
        self.acc10 = acc10
        
        pass
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

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def acc10(self):
        return self.__acc10
    @acc10.setter
    def acc10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__acc10", None)
        self.__acc10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer11"):
                opp_val = getattr(old_value, "customer11", None)
                if opp_val == self:
                    setattr(old_value, "customer11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer11"):
                opp_val = getattr(value, "customer11", None)
                setattr(value, "customer11", self)

    @property
    def webuser7(self):
        return self.__webuser7
    @webuser7.setter
    def webuser7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__webuser7", None)
        self.__webuser7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer6"):
                opp_val = getattr(old_value, "customer6", None)
                if opp_val == self:
                    setattr(old_value, "customer6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer6"):
                opp_val = getattr(value, "customer6", None)
                setattr(value, "customer6", self)

