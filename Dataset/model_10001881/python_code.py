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

    def __init__(self, name: str, description: str, item8: set["LineItem"] = None):
        self.name = name
        self.description = description
        self.item8 = item8 if item8 is not None else set()
        
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
    def item8(self):
        return self.__item8
    @item8.setter
    def item8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__item8", None)
        self.__item8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product9"):
                    opp_val = getattr(item, "product9", None)
                    
                    if opp_val == self:
                        setattr(item, "product9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product9"):
                    opp_val = getattr(item, "product9", None)
                    
                    setattr(item, "product9", self)
                    



class LineItem:

    def __init__(self, quantity: int, price: float, product9: "Product" = None, lineitem11: set["Order_Compute_Price"] = None, sc15: "ShoppinCart" = None):
        self.quantity = quantity
        self.price = price
        self.product9 = product9
        self.lineitem11 = lineitem11 if lineitem11 is not None else set()
        self.sc15 = sc15
        
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
    def sc15(self):
        return self.__sc15
    @sc15.setter
    def sc15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__sc15", None)
        self.__sc15 = value
        
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
    def lineitem11(self):
        return self.__lineitem11
    @lineitem11.setter
    def lineitem11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__lineitem11", None)
        self.__lineitem11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "items10"):
                    opp_val = getattr(item, "items10", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "items10"):
                    opp_val = getattr(item, "items10", None)
                    
                    if opp_val is None:
                        setattr(item, "items10", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def product9(self):
        return self.__product9
    @product9.setter
    def product9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__product9", None)
        self.__product9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item8"):
                opp_val = getattr(old_value, "item8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item8"):
                opp_val = getattr(value, "item8", None)
                if opp_val is None:
                    setattr(value, "item8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order_Compute_Price:

    def __init__(self, number: int, ordered: date, shipped: bool, shipTo: str, total: float, status: OrderStatus, order3: set["Payment"] = None, account5: "Account" = None, items10: set["LineItem"] = None):
        self.number = number
        self.ordered = ordered
        self.shipped = shipped
        self.shipTo = shipTo
        self.total = total
        self.status = status
        self.order3 = order3 if order3 is not None else set()
        self.account5 = account5
        self.items10 = items10 if items10 is not None else set()
        
        pass
    @property
    def shipped(self):
        return self.__shipped
    @shipped.setter
    def shipped(self, shipped: bool):
        self.__shipped = shipped

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: OrderStatus):
        self.__status = status

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

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
    def ordered(self):
        return self.__ordered
    @ordered.setter
    def ordered(self, ordered: date):
        self.__ordered = ordered

    @property
    def items10(self):
        return self.__items10
    @items10.setter
    def items10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order_Compute_Price__items10", None)
        self.__items10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lineitem11"):
                    opp_val = getattr(item, "lineitem11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lineitem11"):
                    opp_val = getattr(item, "lineitem11", None)
                    
                    if opp_val is None:
                        setattr(item, "lineitem11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def account5(self):
        return self.__account5
    @account5.setter
    def account5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order_Compute_Price__account5", None)
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

    @property
    def order3(self):
        return self.__order3
    @order3.setter
    def order3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order_Compute_Price__order3", None)
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
                    



class Account:

    def __init__(self, billingAddress: str, open: date, closed: date, isClosed: bool, payment0: set["Payment"] = None, order4: set["Order_Compute_Price"] = None, customer7: "Customer" = None, cart12: "ShoppinCart" = None):
        self.billingAddress = billingAddress
        self.open = open
        self.closed = closed
        self.isClosed = isClosed
        self.payment0 = payment0 if payment0 is not None else set()
        self.order4 = order4 if order4 is not None else set()
        self.customer7 = customer7
        self.cart12 = cart12
        
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
    def isClosed(self):
        return self.__isClosed
    @isClosed.setter
    def isClosed(self, isClosed: bool):
        self.__isClosed = isClosed

    @property
    def billingAddress(self):
        return self.__billingAddress
    @billingAddress.setter
    def billingAddress(self, billingAddress: str):
        self.__billingAddress = billingAddress

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
    def cart12(self):
        return self.__cart12
    @cart12.setter
    def cart12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__cart12", None)
        self.__cart12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account13"):
                opp_val = getattr(old_value, "account13", None)
                if opp_val == self:
                    setattr(old_value, "account13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account13"):
                opp_val = getattr(value, "account13", None)
                setattr(value, "account13", self)

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
            if hasattr(old_value, "acc6"):
                opp_val = getattr(old_value, "acc6", None)
                if opp_val == self:
                    setattr(old_value, "acc6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "acc6"):
                opp_val = getattr(value, "acc6", None)
                setattr(value, "acc6", self)



class ShoppinCart:

    def __init__(self, creationDate: date, account13: "Account" = None, items14: set["LineItem"] = None):
        self.creationDate = creationDate
        self.account13 = account13
        self.items14 = items14 if items14 is not None else set()
        
        pass
    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def items14(self):
        return self.__items14
    @items14.setter
    def items14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppinCart__items14", None)
        self.__items14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sc15"):
                    opp_val = getattr(item, "sc15", None)
                    
                    if opp_val == self:
                        setattr(item, "sc15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sc15"):
                    opp_val = getattr(item, "sc15", None)
                    
                    setattr(item, "sc15", self)
                    

    @property
    def account13(self):
        return self.__account13
    @account13.setter
    def account13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppinCart__account13", None)
        self.__account13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart12"):
                opp_val = getattr(old_value, "cart12", None)
                if opp_val == self:
                    setattr(old_value, "cart12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart12"):
                opp_val = getattr(value, "cart12", None)
                setattr(value, "cart12", self)



class Payment:

    def __init__(self, paidDate: date, total: float, details: str, account1: "Account" = None, order2: "Order_Compute_Price" = None):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        self.account1 = account1
        self.order2 = order2
        
        pass
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
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

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

    def __init__(self, address: str, phone: str, email: str, acc6: "Account" = None):
        self.address = address
        self.phone = phone
        self.email = email
        self.acc6 = acc6
        
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
    def acc6(self):
        return self.__acc6
    @acc6.setter
    def acc6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__acc6", None)
        self.__acc6 = value
        
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

