from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Product:

    def __init__(self, name: str, description: str, lineItems4: set["Product_View"] = None):
        self.name = name
        self.description = description
        self.lineItems4 = lineItems4 if lineItems4 is not None else set()
        
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
    def lineItems4(self):
        return self.__lineItems4
    @lineItems4.setter
    def lineItems4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__lineItems4", None)
        self.__lineItems4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product5"):
                    opp_val = getattr(item, "product5", None)
                    
                    if opp_val == self:
                        setattr(item, "product5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product5"):
                    opp_val = getattr(item, "product5", None)
                    
                    setattr(item, "product5", self)
                    



class Product_View:

    def __init__(self, quantity: int, price: float, sc3: "ShoppingCart" = None, product5: "Product" = None, order7: "Order" = None):
        self.quantity = quantity
        self.price = price
        self.sc3 = sc3
        self.product5 = product5
        self.order7 = order7
        
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
    def sc3(self):
        return self.__sc3
    @sc3.setter
    def sc3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product_View__sc3", None)
        self.__sc3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items2"):
                opp_val = getattr(old_value, "items2", None)
                if opp_val == self:
                    setattr(old_value, "items2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items2"):
                opp_val = getattr(value, "items2", None)
                setattr(value, "items2", self)

    @property
    def order7(self):
        return self.__order7
    @order7.setter
    def order7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product_View__order7", None)
        self.__order7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items6"):
                opp_val = getattr(old_value, "items6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items6"):
                opp_val = getattr(value, "items6", None)
                if opp_val is None:
                    setattr(value, "items6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product5(self):
        return self.__product5
    @product5.setter
    def product5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product_View__product5", None)
        self.__product5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lineItems4"):
                opp_val = getattr(old_value, "lineItems4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lineItems4"):
                opp_val = getattr(value, "lineItems4", None)
                if opp_val is None:
                    setattr(value, "lineItems4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order:

    def __init__(self, number: int, ordered: date, Address: str, total: float, status: str, items6: set["Product_View"] = None):
        self.number = number
        self.ordered = ordered
        self.Address = Address
        self.total = total
        self.status = status
        self.items6 = items6 if items6 is not None else set()
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

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
    def status(self, status: str):
        self.__status = status

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
    def items6(self):
        return self.__items6
    @items6.setter
    def items6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__items6", None)
        self.__items6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order7"):
                    opp_val = getattr(item, "order7", None)
                    
                    if opp_val == self:
                        setattr(item, "order7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order7"):
                    opp_val = getattr(item, "order7", None)
                    
                    setattr(item, "order7", self)
                    



class WebUser:

    def __init__(self, login: str, password: str, shoppingCart0: "ShoppingCart" = None):
        self.login = login
        self.password = password
        self.shoppingCart0 = shoppingCart0
        
        pass
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
    def shoppingCart0(self):
        return self.__shoppingCart0
    @shoppingCart0.setter
    def shoppingCart0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebUser__shoppingCart0", None)
        self.__shoppingCart0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webUser1"):
                opp_val = getattr(old_value, "webUser1", None)
                if opp_val == self:
                    setattr(old_value, "webUser1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webUser1"):
                opp_val = getattr(value, "webUser1", None)
                setattr(value, "webUser1", self)



class ShoppingCart:

    def __init__(self, creationDate: date, items2: "Product_View" = None, webUser1: "WebUser" = None):
        self.creationDate = creationDate
        self.items2 = items2
        self.webUser1 = webUser1
        
        pass
    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def items2(self):
        return self.__items2
    @items2.setter
    def items2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__items2", None)
        self.__items2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sc3"):
                opp_val = getattr(old_value, "sc3", None)
                if opp_val == self:
                    setattr(old_value, "sc3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sc3"):
                opp_val = getattr(value, "sc3", None)
                setattr(value, "sc3", self)

    @property
    def webUser1(self):
        return self.__webUser1
    @webUser1.setter
    def webUser1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__webUser1", None)
        self.__webUser1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart0"):
                opp_val = getattr(old_value, "shoppingCart0", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart0"):
                opp_val = getattr(value, "shoppingCart0", None)
                setattr(value, "shoppingCart0", self)

