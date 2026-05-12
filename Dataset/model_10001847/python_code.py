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










class LZUser2:

    def __init__(self, populate: str, password: str, state: UserState):
        self.populate = populate
        self.password = password
        self.state = state
        
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
    def populate(self):
        return self.__populate
    @populate.setter
    def populate(self, populate: str):
        self.__populate = populate



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

    def __init__(self, quantity: int, price: float, sc9: "ShoppingCart" = None, product11: "Product" = None, order13: "Order" = None):
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

    def __init__(self, number: int, ordered: date, shipped: bool, shipTo: str, total: float, status: OrderStatus, items12: set["LineItem"] = None, account15: "Redis" = None, payment17: "Payment" = None):
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
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: OrderStatus):
        self.__status = status

    @property
    def ordered(self):
        return self.__ordered
    @ordered.setter
    def ordered(self, ordered: date):
        self.__ordered = ordered

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

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
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

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



class RadixClient:

    def __init__(self, populate: str, password: str, state: UserState, shoppingCart2: "ShoppingCart" = None):
        self.populate = populate
        self.password = password
        self.state = state
        self.shoppingCart2 = shoppingCart2
        
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
    def populate(self):
        return self.__populate
    @populate.setter
    def populate(self, populate: str):
        self.__populate = populate

    @property
    def shoppingCart2(self):
        return self.__shoppingCart2
    @shoppingCart2.setter
    def shoppingCart2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RadixClient__shoppingCart2", None)
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



class Redis:

    pass


class ShoppingCart:

    def __init__(self, creationDate: date, account7: "Redis" = None, items8: "LineItem" = None, webUser3: "RadixClient" = None):
        self.creationDate = creationDate
        self.account7 = account7
        self.items8 = items8
        self.webUser3 = webUser3
        
        pass
    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def items8(self):
        return self.__items8
    @items8.setter
    def items8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__items8", None)
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
    def account7(self):
        return self.__account7
    @account7.setter
    def account7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__account7", None)
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



class Payment:

    def __init__(self, paidDate: date, total: float, details: str, order16: "Order" = None, acc1: "Redis" = None):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        self.order16 = order16
        self.acc1 = acc1
        
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



class RedisClient:

    def __init__(self, RadixClient: str, log: str, email: str, account4: "Redis" = None):
        self.RadixClient = RadixClient
        self.log = log
        self.email = email
        self.account4 = account4
        
        pass
    @property
    def RadixClient(self):
        return self.__RadixClient
    @RadixClient.setter
    def RadixClient(self, RadixClient: str):
        self.__RadixClient = RadixClient

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def log(self):
        return self.__log
    @log.setter
    def log(self, log: str):
        self.__log = log

    @property
    def account4(self):
        return self.__account4
    @account4.setter
    def account4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RedisClient__account4", None)
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

