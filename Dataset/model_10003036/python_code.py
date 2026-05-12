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







class AjoutProduit_UseCase:

    pass


class Webuser_Actor:

    pass


class Admin_Actor:

    pass


class MyActor_Actor:

    pass





class Product:

    def __init__(self, name: str, description: str, item7: set["LineItem"] = None):
        self.name = name
        self.description = description
        self.item7 = item7 if item7 is not None else set()
        
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
    def item7(self):
        return self.__item7
    @item7.setter
    def item7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__item7", None)
        self.__item7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product6"):
                    opp_val = getattr(item, "product6", None)
                    
                    if opp_val == self:
                        setattr(item, "product6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product6"):
                    opp_val = getattr(item, "product6", None)
                    
                    setattr(item, "product6", self)
                    



class LineItem:

    def __init__(self, quantity: int, price: float, sc3: "ShoppingCart" = None, product6: "Product" = None, order15: "Order" = None):
        self.quantity = quantity
        self.price = price
        self.sc3 = sc3
        self.product6 = product6
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
    def sc3(self):
        return self.__sc3
    @sc3.setter
    def sc3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__sc3", None)
        self.__sc3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items2"):
                opp_val = getattr(old_value, "items2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items2"):
                opp_val = getattr(value, "items2", None)
                if opp_val is None:
                    setattr(value, "items2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product6(self):
        return self.__product6
    @product6.setter
    def product6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__product6", None)
        self.__product6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item7"):
                opp_val = getattr(old_value, "item7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item7"):
                opp_val = getattr(value, "item7", None)
                if opp_val is None:
                    setattr(value, "item7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order:

    def __init__(self, number: int, ordered: date, shipped: bool, shipTo: str, total: float, status: OrderStatus, items14: set["LineItem"] = None, accnt17: "Account" = None, payment21: "Payment" = None):
        self.number = number
        self.ordered = ordered
        self.shipped = shipped
        self.shipTo = shipTo
        self.total = total
        self.status = status
        self.items14 = items14 if items14 is not None else set()
        self.accnt17 = accnt17
        self.payment21 = payment21
        
        pass
    @property
    def ordered(self):
        return self.__ordered
    @ordered.setter
    def ordered(self, ordered: date):
        self.__ordered = ordered

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
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: OrderStatus):
        self.__status = status

    @property
    def shipTo(self):
        return self.__shipTo
    @shipTo.setter
    def shipTo(self, shipTo: str):
        self.__shipTo = shipTo

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

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
                    

    @property
    def payment21(self):
        return self.__payment21
    @payment21.setter
    def payment21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment21", None)
        self.__payment21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order20"):
                opp_val = getattr(old_value, "order20", None)
                if opp_val == self:
                    setattr(old_value, "order20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order20"):
                opp_val = getattr(value, "order20", None)
                setattr(value, "order20", self)

    @property
    def accnt17(self):
        return self.__accnt17
    @accnt17.setter
    def accnt17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__accnt17", None)
        self.__accnt17 = value
        
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



class WebUser:

    def __init__(self, login: str, password: str, state: UserState, shoppingCart8: "ShoppingCart" = None, customer10: "Customer" = None):
        self.login = login
        self.password = password
        self.state = state
        self.shoppingCart8 = shoppingCart8
        self.customer10 = customer10
        
        pass
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
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def customer10(self):
        return self.__customer10
    @customer10.setter
    def customer10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebUser__customer10", None)
        self.__customer10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webUser11"):
                opp_val = getattr(old_value, "webUser11", None)
                if opp_val == self:
                    setattr(old_value, "webUser11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webUser11"):
                opp_val = getattr(value, "webUser11", None)
                setattr(value, "webUser11", self)

    @property
    def shoppingCart8(self):
        return self.__shoppingCart8
    @shoppingCart8.setter
    def shoppingCart8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebUser__shoppingCart8", None)
        self.__shoppingCart8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webUser9"):
                opp_val = getattr(old_value, "webUser9", None)
                if opp_val == self:
                    setattr(old_value, "webUser9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webUser9"):
                opp_val = getattr(value, "webUser9", None)
                setattr(value, "webUser9", self)



class Account:

    def __init__(self, billingAddress: str, open: date, closed: date, isClosed: bool, cart4: "ShoppingCart" = None, customer13: "Customer" = None, order16: set["Order"] = None, payment18: set["Payment"] = None):
        self.billingAddress = billingAddress
        self.open = open
        self.closed = closed
        self.isClosed = isClosed
        self.cart4 = cart4
        self.customer13 = customer13
        self.order16 = order16 if order16 is not None else set()
        self.payment18 = payment18 if payment18 is not None else set()
        
        pass
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
    def cart4(self):
        return self.__cart4
    @cart4.setter
    def cart4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__cart4", None)
        self.__cart4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account5"):
                opp_val = getattr(old_value, "account5", None)
                if opp_val == self:
                    setattr(old_value, "account5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account5"):
                opp_val = getattr(value, "account5", None)
                setattr(value, "account5", self)

    @property
    def payment18(self):
        return self.__payment18
    @payment18.setter
    def payment18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__payment18", None)
        self.__payment18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account19"):
                    opp_val = getattr(item, "account19", None)
                    
                    if opp_val == self:
                        setattr(item, "account19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account19"):
                    opp_val = getattr(item, "account19", None)
                    
                    setattr(item, "account19", self)
                    

    @property
    def customer13(self):
        return self.__customer13
    @customer13.setter
    def customer13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__customer13", None)
        self.__customer13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "acc12"):
                opp_val = getattr(old_value, "acc12", None)
                if opp_val == self:
                    setattr(old_value, "acc12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "acc12"):
                opp_val = getattr(value, "acc12", None)
                setattr(value, "acc12", self)

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
                if hasattr(item, "accnt17"):
                    opp_val = getattr(item, "accnt17", None)
                    
                    if opp_val == self:
                        setattr(item, "accnt17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accnt17"):
                    opp_val = getattr(item, "accnt17", None)
                    
                    setattr(item, "accnt17", self)
                    



class ShoppingCart:

    def __init__(self, creationDate: date, items2: set["LineItem"] = None, account5: "Account" = None, webUser9: "WebUser" = None):
        self.creationDate = creationDate
        self.items2 = items2 if items2 is not None else set()
        self.account5 = account5
        self.webUser9 = webUser9
        
        pass
    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def account5(self):
        return self.__account5
    @account5.setter
    def account5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__account5", None)
        self.__account5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart4"):
                opp_val = getattr(old_value, "cart4", None)
                if opp_val == self:
                    setattr(old_value, "cart4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart4"):
                opp_val = getattr(value, "cart4", None)
                setattr(value, "cart4", self)

    @property
    def items2(self):
        return self.__items2
    @items2.setter
    def items2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__items2", None)
        self.__items2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sc3"):
                    opp_val = getattr(item, "sc3", None)
                    
                    if opp_val == self:
                        setattr(item, "sc3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sc3"):
                    opp_val = getattr(item, "sc3", None)
                    
                    setattr(item, "sc3", self)
                    

    @property
    def webUser9(self):
        return self.__webUser9
    @webUser9.setter
    def webUser9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__webUser9", None)
        self.__webUser9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart8"):
                opp_val = getattr(old_value, "shoppingCart8", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart8"):
                opp_val = getattr(value, "shoppingCart8", None)
                setattr(value, "shoppingCart8", self)



class Payment:

    def __init__(self, paidDate: date, total: float, details: str, account19: "Account" = None, order20: "Order" = None):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        self.account19 = account19
        self.order20 = order20
        
        pass
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
    def details(self):
        return self.__details
    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def account19(self):
        return self.__account19
    @account19.setter
    def account19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__account19", None)
        self.__account19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment18"):
                opp_val = getattr(old_value, "payment18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment18"):
                opp_val = getattr(value, "payment18", None)
                if opp_val is None:
                    setattr(value, "payment18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order20(self):
        return self.__order20
    @order20.setter
    def order20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order20", None)
        self.__order20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment21"):
                opp_val = getattr(old_value, "payment21", None)
                if opp_val == self:
                    setattr(old_value, "payment21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment21"):
                opp_val = getattr(value, "payment21", None)
                setattr(value, "payment21", self)



class Customer:

    def __init__(self, address: str, phone: str, email: str, webUser11: "WebUser" = None, acc12: "Account" = None):
        self.address = address
        self.phone = phone
        self.email = email
        self.webUser11 = webUser11
        self.acc12 = acc12
        
        pass
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
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def webUser11(self):
        return self.__webUser11
    @webUser11.setter
    def webUser11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__webUser11", None)
        self.__webUser11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer10"):
                opp_val = getattr(old_value, "customer10", None)
                if opp_val == self:
                    setattr(old_value, "customer10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer10"):
                opp_val = getattr(value, "customer10", None)
                setattr(value, "customer10", self)

    @property
    def acc12(self):
        return self.__acc12
    @acc12.setter
    def acc12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__acc12", None)
        self.__acc12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer13"):
                opp_val = getattr(old_value, "customer13", None)
                if opp_val == self:
                    setattr(old_value, "customer13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer13"):
                opp_val = getattr(value, "customer13", None)
                setattr(value, "customer13", self)

