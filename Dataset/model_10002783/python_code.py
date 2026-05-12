from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class ShoppingCartExample_Account:

    def __init__(self, id: int, cart4: "ShoppingCartExample_ShoppingCart" = None, customer6: "ShoppingCartExample_Customer" = None):
        self.id = id
        self.cart4 = cart4
        self.customer6 = customer6
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def customer6(self):
        return self.__customer6
    @customer6.setter
    def customer6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCartExample_Account__customer6", None)
        self.__customer6 = value
        
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

    @property
    def cart4(self):
        return self.__cart4
    @cart4.setter
    def cart4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCartExample_Account__cart4", None)
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



class ShoppingCartExample_LineItem:

    def __init__(self, quantity: int, price: int, order1: "ShoppingCartExample_Order" = None):
        self.quantity = quantity
        self.price = price
        self.order1 = order1
        
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
    def price(self, price: int):
        self.__price = price

    @property
    def order1(self):
        return self.__order1
    @order1.setter
    def order1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCartExample_LineItem__order1", None)
        self.__order1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items0"):
                opp_val = getattr(old_value, "items0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items0"):
                opp_val = getattr(value, "items0", None)
                if opp_val is None:
                    setattr(value, "items0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ShoppingCartExample_Order:

    def __init__(self, id: int, items0: set["ShoppingCartExample_LineItem"] = None, c3: "ShoppingCartExample_ShoppingCart" = None):
        self.id = id
        self.items0 = items0 if items0 is not None else set()
        self.c3 = c3
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def c3(self):
        return self.__c3
    @c3.setter
    def c3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCartExample_Order__c3", None)
        self.__c3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order2"):
                opp_val = getattr(old_value, "order2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order2"):
                opp_val = getattr(value, "order2", None)
                if opp_val is None:
                    setattr(value, "order2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def items0(self):
        return self.__items0
    @items0.setter
    def items0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCartExample_Order__items0", None)
        self.__items0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order1"):
                    opp_val = getattr(item, "order1", None)
                    
                    if opp_val == self:
                        setattr(item, "order1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order1"):
                    opp_val = getattr(item, "order1", None)
                    
                    setattr(item, "order1", self)
                    



class ShoppingCartExample_ShoppingCart:

    def __init__(self, creationDate: date, order2: set["ShoppingCartExample_Order"] = None, account5: "ShoppingCartExample_Account" = None):
        self.creationDate = creationDate
        self.order2 = order2 if order2 is not None else set()
        self.account5 = account5
        
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
        old_value = getattr(self, f"_ShoppingCartExample_ShoppingCart__account5", None)
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
    def order2(self):
        return self.__order2
    @order2.setter
    def order2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCartExample_ShoppingCart__order2", None)
        self.__order2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "c3"):
                    opp_val = getattr(item, "c3", None)
                    
                    if opp_val == self:
                        setattr(item, "c3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "c3"):
                    opp_val = getattr(item, "c3", None)
                    
                    setattr(item, "c3", self)
                    



class ShoppingCartExample_Customer:

    pass
