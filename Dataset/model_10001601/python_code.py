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

    def __init__(self, name: str, description: str, lineItems6: set["LineItem"] = None):
        self.name = name
        self.description = description
        self.lineItems6 = lineItems6 if lineItems6 is not None else set()
        
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
    def lineItems6(self):
        return self.__lineItems6
    @lineItems6.setter
    def lineItems6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__lineItems6", None)
        self.__lineItems6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product7"):
                    opp_val = getattr(item, "product7", None)
                    
                    if opp_val == self:
                        setattr(item, "product7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product7"):
                    opp_val = getattr(item, "product7", None)
                    
                    setattr(item, "product7", self)
                    



class LineItem:

    def __init__(self, quantity: int, price: float, sc5: "ShoppingCart" = None, product7: "Product" = None, order9: "Order" = None):
        self.quantity = quantity
        self.price = price
        self.sc5 = sc5
        self.product7 = product7
        self.order9 = order9
        
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
    def order9(self):
        return self.__order9
    @order9.setter
    def order9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__order9", None)
        self.__order9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items8"):
                opp_val = getattr(old_value, "items8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items8"):
                opp_val = getattr(value, "items8", None)
                if opp_val is None:
                    setattr(value, "items8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product7(self):
        return self.__product7
    @product7.setter
    def product7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__product7", None)
        self.__product7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lineItems6"):
                opp_val = getattr(old_value, "lineItems6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lineItems6"):
                opp_val = getattr(value, "lineItems6", None)
                if opp_val is None:
                    setattr(value, "lineItems6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sc5(self):
        return self.__sc5
    @sc5.setter
    def sc5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__sc5", None)
        self.__sc5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items4"):
                opp_val = getattr(old_value, "items4", None)
                if opp_val == self:
                    setattr(old_value, "items4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items4"):
                opp_val = getattr(value, "items4", None)
                setattr(value, "items4", self)



class Order:

    def __init__(self, number: int, ordered: date, shipped: bool, shipTo: str, total: float, status: OrderStatus, items8: set["LineItem"] = None, account11: "ShoppingCart1" = None, payment13: "Payment" = None):
        self.number = number
        self.ordered = ordered
        self.shipped = shipped
        self.shipTo = shipTo
        self.total = total
        self.status = status
        self.items8 = items8 if items8 is not None else set()
        self.account11 = account11
        self.payment13 = payment13
        
        pass
    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

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
    def account11(self):
        return self.__account11
    @account11.setter
    def account11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__account11", None)
        self.__account11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order10"):
                opp_val = getattr(old_value, "order10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order10"):
                opp_val = getattr(value, "order10", None)
                if opp_val is None:
                    setattr(value, "order10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def items8(self):
        return self.__items8
    @items8.setter
    def items8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__items8", None)
        self.__items8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order9"):
                    opp_val = getattr(item, "order9", None)
                    
                    if opp_val == self:
                        setattr(item, "order9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order9"):
                    opp_val = getattr(item, "order9", None)
                    
                    setattr(item, "order9", self)
                    

    @property
    def payment13(self):
        return self.__payment13
    @payment13.setter
    def payment13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment13", None)
        self.__payment13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order12"):
                opp_val = getattr(old_value, "order12", None)
                if opp_val == self:
                    setattr(old_value, "order12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order12"):
                opp_val = getattr(value, "order12", None)
                setattr(value, "order12", self)



class ShoppingCart1:

    def __init__(self, itemCount: int, totalPrice: int, closed: date, isClosed: bool, p0: set["Payment"] = None, cart2: "ShoppingCart" = None, order10: set["Order"] = None):
        self.itemCount = itemCount
        self.totalPrice = totalPrice
        self.closed = closed
        self.isClosed = isClosed
        self.p0 = p0 if p0 is not None else set()
        self.cart2 = cart2
        self.order10 = order10 if order10 is not None else set()
        
        pass
    @property
    def totalPrice(self):
        return self.__totalPrice
    @totalPrice.setter
    def totalPrice(self, totalPrice: int):
        self.__totalPrice = totalPrice

    @property
    def closed(self):
        return self.__closed
    @closed.setter
    def closed(self, closed: date):
        self.__closed = closed

    @property
    def itemCount(self):
        return self.__itemCount
    @itemCount.setter
    def itemCount(self, itemCount: int):
        self.__itemCount = itemCount

    @property
    def isClosed(self):
        return self.__isClosed
    @isClosed.setter
    def isClosed(self, isClosed: bool):
        self.__isClosed = isClosed

    @property
    def cart2(self):
        return self.__cart2
    @cart2.setter
    def cart2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart1__cart2", None)
        self.__cart2 = value
        
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

    @property
    def p0(self):
        return self.__p0
    @p0.setter
    def p0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart1__p0", None)
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
    def order10(self):
        return self.__order10
    @order10.setter
    def order10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart1__order10", None)
        self.__order10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account11"):
                    opp_val = getattr(item, "account11", None)
                    
                    if opp_val == self:
                        setattr(item, "account11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account11"):
                    opp_val = getattr(item, "account11", None)
                    
                    setattr(item, "account11", self)
                    



class ShoppingCart:

    def __init__(self, creationDate: date, account3: "ShoppingCart1" = None, items4: "LineItem" = None):
        self.creationDate = creationDate
        self.account3 = account3
        self.items4 = items4
        
        pass
    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def account3(self):
        return self.__account3
    @account3.setter
    def account3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__account3", None)
        self.__account3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart2"):
                opp_val = getattr(old_value, "cart2", None)
                if opp_val == self:
                    setattr(old_value, "cart2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart2"):
                opp_val = getattr(value, "cart2", None)
                setattr(value, "cart2", self)

    @property
    def items4(self):
        return self.__items4
    @items4.setter
    def items4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__items4", None)
        self.__items4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sc5"):
                opp_val = getattr(old_value, "sc5", None)
                if opp_val == self:
                    setattr(old_value, "sc5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sc5"):
                opp_val = getattr(value, "sc5", None)
                setattr(value, "sc5", self)



class Payment:

    def __init__(self, paidDate: date, total: float, details: str, acc1: "ShoppingCart1" = None, order12: "Order" = None):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        self.acc1 = acc1
        self.order12 = order12
        
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
    def order12(self):
        return self.__order12
    @order12.setter
    def order12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order12", None)
        self.__order12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment13"):
                opp_val = getattr(old_value, "payment13", None)
                if opp_val == self:
                    setattr(old_value, "payment13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment13"):
                opp_val = getattr(value, "payment13", None)
                setattr(value, "payment13", self)

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

