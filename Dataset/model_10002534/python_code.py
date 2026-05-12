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










class Payment:

    def __init__(self, paidDate: date, total: float, details: str, acc1: "Account" = None, order16: "Order" = None):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        self.acc1 = acc1
        self.order16 = order16
        
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
    def order16(self):
        return self.__order16
    @order16.setter
    def order16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order16", None)
        self.__order16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment17"):
                opp_val = getattr(old_value, "payment17", None)
                if opp_val == self:
                    setattr(old_value, "payment17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment17"):
                opp_val = getattr(value, "payment17", None)
                setattr(value, "payment17", self)



class Customer:

    def __init__(self, address: str, phone: str, email: str, webUser3: "SinhVien" = None, account4: "Account" = None):
        self.address = address
        self.phone = phone
        self.email = email
        self.webUser3 = webUser3
        self.account4 = account4
        
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

    @property
    def webUser3(self):
        return self.__webUser3
    @webUser3.setter
    def webUser3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__webUser3", None)
        self.__webUser3 = value
        
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



class Product:

    def __init__(self, name: str, description: str, lineItems10: set["LineItem"] = None):
        self.name = name
        self.description = description
        self.lineItems10 = lineItems10 if lineItems10 is not None else set()
        
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
    def lineItems10(self):
        return self.__lineItems10
    @lineItems10.setter
    def lineItems10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__lineItems10", None)
        self.__lineItems10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product11"):
                    opp_val = getattr(item, "product11", None)
                    
                    if opp_val == self:
                        setattr(item, "product11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product11"):
                    opp_val = getattr(item, "product11", None)
                    
                    setattr(item, "product11", self)
                    



class LineItem:

    def __init__(self, quantity: int, price: float, sc9: "ConNguoi" = None, product11: "Product" = None, order13: "Order" = None):
        self.quantity = quantity
        self.price = price
        self.sc9 = sc9
        self.product11 = product11
        self.order13 = order13
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def product11(self):
        return self.__product11
    @product11.setter
    def product11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__product11", None)
        self.__product11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lineItems10"):
                opp_val = getattr(old_value, "lineItems10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lineItems10"):
                opp_val = getattr(value, "lineItems10", None)
                if opp_val is None:
                    setattr(value, "lineItems10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order13(self):
        return self.__order13
    @order13.setter
    def order13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__order13", None)
        self.__order13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items12"):
                opp_val = getattr(old_value, "items12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items12"):
                opp_val = getattr(value, "items12", None)
                if opp_val is None:
                    setattr(value, "items12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sc9(self):
        return self.__sc9
    @sc9.setter
    def sc9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__sc9", None)
        self.__sc9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items8"):
                opp_val = getattr(old_value, "items8", None)
                if opp_val == self:
                    setattr(old_value, "items8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items8"):
                opp_val = getattr(value, "items8", None)
                setattr(value, "items8", self)



class Order:

    def __init__(self, number: int, ordered: date, shipped: bool, shipTo: str, total: float, status: OrderStatus, items12: set["LineItem"] = None, account15: "Account" = None, payment17: "Payment" = None):
        self.number = number
        self.ordered = ordered
        self.shipped = shipped
        self.shipTo = shipTo
        self.total = total
        self.status = status
        self.items12 = items12 if items12 is not None else set()
        self.account15 = account15
        self.payment17 = payment17
        
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
    def shipped(self):
        return self.__shipped
    @shipped.setter
    def shipped(self, shipped: bool):
        self.__shipped = shipped

    @property
    def items12(self):
        return self.__items12
    @items12.setter
    def items12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__items12", None)
        self.__items12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order13"):
                    opp_val = getattr(item, "order13", None)
                    
                    if opp_val == self:
                        setattr(item, "order13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order13"):
                    opp_val = getattr(item, "order13", None)
                    
                    setattr(item, "order13", self)
                    

    @property
    def payment17(self):
        return self.__payment17
    @payment17.setter
    def payment17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment17", None)
        self.__payment17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order16"):
                opp_val = getattr(old_value, "order16", None)
                if opp_val == self:
                    setattr(old_value, "order16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order16"):
                opp_val = getattr(value, "order16", None)
                setattr(value, "order16", self)

    @property
    def account15(self):
        return self.__account15
    @account15.setter
    def account15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__account15", None)
        self.__account15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order14"):
                opp_val = getattr(old_value, "order14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order14"):
                opp_val = getattr(value, "order14", None)
                if opp_val is None:
                    setattr(value, "order14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class SinhVien:

    def __init__(self, login: str, password: str, state: UserState, customer2: "Customer" = None):
        self.login = login
        self.password = password
        self.state = state
        self.customer2 = customer2
        
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
    def customer2(self):
        return self.__customer2
    @customer2.setter
    def customer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SinhVien__customer2", None)
        self.__customer2 = value
        
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

    def __init__(self, billingAddress: str, open: date, closed: date, isClosed: bool, p0: set["Payment"] = None, customer5: "Customer" = None, cart6: "ConNguoi" = None, order14: set["Order"] = None):
        self.billingAddress = billingAddress
        self.open = open
        self.closed = closed
        self.isClosed = isClosed
        self.p0 = p0 if p0 is not None else set()
        self.customer5 = customer5
        self.cart6 = cart6
        self.order14 = order14 if order14 is not None else set()
        
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
    def closed(self):
        return self.__closed
    @closed.setter
    def closed(self, closed: date):
        self.__closed = closed

    @property
    def open(self):
        return self.__open
    @open.setter
    def open(self, open: date):
        self.__open = open

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
    def order14(self):
        return self.__order14
    @order14.setter
    def order14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__order14", None)
        self.__order14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account15"):
                    opp_val = getattr(item, "account15", None)
                    
                    if opp_val == self:
                        setattr(item, "account15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account15"):
                    opp_val = getattr(item, "account15", None)
                    
                    setattr(item, "account15", self)
                    

    @property
    def cart6(self):
        return self.__cart6
    @cart6.setter
    def cart6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__cart6", None)
        self.__cart6 = value
        
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



class ConNguoi:

    def __init__(self, CMND: str, attribute: str, attribute2: str, attribute3: str, attribute4: str, attribute5: str, attribute6: str, account7: "Account" = None, items8: "LineItem" = None):
        self.CMND = CMND
        self.attribute = attribute
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.attribute4 = attribute4
        self.attribute5 = attribute5
        self.attribute6 = attribute6
        self.account7 = account7
        self.items8 = items8
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute3(self):
        return self.__attribute3
    @attribute3.setter
    def attribute3(self, attribute3: str):
        self.__attribute3 = attribute3

    @property
    def CMND(self):
        return self.__CMND
    @CMND.setter
    def CMND(self, CMND: str):
        self.__CMND = CMND

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def attribute5(self):
        return self.__attribute5
    @attribute5.setter
    def attribute5(self, attribute5: str):
        self.__attribute5 = attribute5

    @property
    def attribute4(self):
        return self.__attribute4
    @attribute4.setter
    def attribute4(self, attribute4: str):
        self.__attribute4 = attribute4

    @property
    def attribute6(self):
        return self.__attribute6
    @attribute6.setter
    def attribute6(self, attribute6: str):
        self.__attribute6 = attribute6

    @property
    def items8(self):
        return self.__items8
    @items8.setter
    def items8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConNguoi__items8", None)
        self.__items8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sc9"):
                opp_val = getattr(old_value, "sc9", None)
                if opp_val == self:
                    setattr(old_value, "sc9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sc9"):
                opp_val = getattr(value, "sc9", None)
                setattr(value, "sc9", self)

    @property
    def account7(self):
        return self.__account7
    @account7.setter
    def account7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConNguoi__account7", None)
        self.__account7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart6"):
                opp_val = getattr(old_value, "cart6", None)
                if opp_val == self:
                    setattr(old_value, "cart6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart6"):
                opp_val = getattr(value, "cart6", None)
                setattr(value, "cart6", self)

