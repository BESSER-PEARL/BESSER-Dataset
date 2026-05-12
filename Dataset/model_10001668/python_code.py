from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Inventory:

    def __init__(self, SuperMarket: str, list: str, product2: set["Product"] = None, payment9: "Payment" = None):
        self.SuperMarket = SuperMarket
        self.list = list
        self.product2 = product2 if product2 is not None else set()
        self.payment9 = payment9
        
        pass
    @property
    def SuperMarket(self):
        return self.__SuperMarket
    @SuperMarket.setter
    def SuperMarket(self, SuperMarket: str):
        self.__SuperMarket = SuperMarket

    @property
    def list(self):
        return self.__list
    @list.setter
    def list(self, list: str):
        self.__list = list

    @property
    def product2(self):
        return self.__product2
    @product2.setter
    def product2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Inventory__product2", None)
        self.__product2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "inventory3"):
                    opp_val = getattr(item, "inventory3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "inventory3"):
                    opp_val = getattr(item, "inventory3", None)
                    
                    if opp_val is None:
                        setattr(item, "inventory3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def payment9(self):
        return self.__payment9
    @payment9.setter
    def payment9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Inventory__payment9", None)
        self.__payment9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inventory8"):
                opp_val = getattr(old_value, "inventory8", None)
                if opp_val == self:
                    setattr(old_value, "inventory8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inventory8"):
                opp_val = getattr(value, "inventory8", None)
                setattr(value, "inventory8", self)



class Product:

    def __init__(self, ID: int, qty: int, Name: str, type: str, price: str, amount: str, blgl: bool, attribute: str, inventory3: set["Inventory"] = None, customer4: set["Customer"] = None, payment6: "Payment" = None):
        self.ID = ID
        self.qty = qty
        self.Name = Name
        self.type = type
        self.price = price
        self.amount = amount
        self.blgl = blgl
        self.attribute = attribute
        self.inventory3 = inventory3 if inventory3 is not None else set()
        self.customer4 = customer4 if customer4 is not None else set()
        self.payment6 = payment6
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def qty(self):
        return self.__qty
    @qty.setter
    def qty(self, qty: int):
        self.__qty = qty

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def blgl(self):
        return self.__blgl
    @blgl.setter
    def blgl(self, blgl: bool):
        self.__blgl = blgl

    @property
    def customer4(self):
        return self.__customer4
    @customer4.setter
    def customer4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__customer4", None)
        self.__customer4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product5"):
                    opp_val = getattr(item, "product5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product5"):
                    opp_val = getattr(item, "product5", None)
                    
                    if opp_val is None:
                        setattr(item, "product5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def inventory3(self):
        return self.__inventory3
    @inventory3.setter
    def inventory3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__inventory3", None)
        self.__inventory3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product2"):
                    opp_val = getattr(item, "product2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product2"):
                    opp_val = getattr(item, "product2", None)
                    
                    if opp_val is None:
                        setattr(item, "product2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def payment6(self):
        return self.__payment6
    @payment6.setter
    def payment6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__payment6", None)
        self.__payment6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product7"):
                opp_val = getattr(old_value, "product7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product7"):
                opp_val = getattr(value, "product7", None)
                if opp_val is None:
                    setattr(value, "product7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Payment:

    def __init__(self, quantity: int, ID: int, list: str, totalamount: str, finalamount: str, discountamount: str, amount__: str, Imtiaz: str, customer1: "Customer" = None, product7: set["Product"] = None, inventory8: "Inventory" = None):
        self.quantity = quantity
        self.ID = ID
        self.list = list
        self.totalamount = totalamount
        self.finalamount = finalamount
        self.discountamount = discountamount
        self.amount__ = amount__
        self.Imtiaz = Imtiaz
        self.customer1 = customer1
        self.product7 = product7 if product7 is not None else set()
        self.inventory8 = inventory8
        
        pass
    @property
    def finalamount(self):
        return self.__finalamount
    @finalamount.setter
    def finalamount(self, finalamount: str):
        self.__finalamount = finalamount

    @property
    def discountamount(self):
        return self.__discountamount
    @discountamount.setter
    def discountamount(self, discountamount: str):
        self.__discountamount = discountamount

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def amount__(self):
        return self.__amount__
    @amount__.setter
    def amount__(self, amount__: str):
        self.__amount__ = amount__

    @property
    def list(self):
        return self.__list
    @list.setter
    def list(self, list: str):
        self.__list = list

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def totalamount(self):
        return self.__totalamount
    @totalamount.setter
    def totalamount(self, totalamount: str):
        self.__totalamount = totalamount

    @property
    def Imtiaz(self):
        return self.__Imtiaz
    @Imtiaz.setter
    def Imtiaz(self, Imtiaz: str):
        self.__Imtiaz = Imtiaz

    @property
    def product7(self):
        return self.__product7
    @product7.setter
    def product7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__product7", None)
        self.__product7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "payment6"):
                    opp_val = getattr(item, "payment6", None)
                    
                    if opp_val == self:
                        setattr(item, "payment6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "payment6"):
                    opp_val = getattr(item, "payment6", None)
                    
                    setattr(item, "payment6", self)
                    

    @property
    def inventory8(self):
        return self.__inventory8
    @inventory8.setter
    def inventory8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__inventory8", None)
        self.__inventory8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment9"):
                opp_val = getattr(old_value, "payment9", None)
                if opp_val == self:
                    setattr(old_value, "payment9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment9"):
                opp_val = getattr(value, "payment9", None)
                setattr(value, "payment9", self)

    @property
    def customer1(self):
        return self.__customer1
    @customer1.setter
    def customer1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__customer1", None)
        self.__customer1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment0"):
                opp_val = getattr(old_value, "payment0", None)
                if opp_val == self:
                    setattr(old_value, "payment0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment0"):
                opp_val = getattr(value, "payment0", None)
                setattr(value, "payment0", self)



class Customer:

    def __init__(self, type: str, royalty: bool, payment0: "Payment" = None, product5: set["Product"] = None):
        self.type = type
        self.royalty = royalty
        self.payment0 = payment0
        self.product5 = product5 if product5 is not None else set()
        
        pass
    @property
    def royalty(self):
        return self.__royalty
    @royalty.setter
    def royalty(self, royalty: bool):
        self.__royalty = royalty

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def payment0(self):
        return self.__payment0
    @payment0.setter
    def payment0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__payment0", None)
        self.__payment0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer1"):
                opp_val = getattr(old_value, "customer1", None)
                if opp_val == self:
                    setattr(old_value, "customer1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer1"):
                opp_val = getattr(value, "customer1", None)
                setattr(value, "customer1", self)

    @property
    def product5(self):
        return self.__product5
    @product5.setter
    def product5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__product5", None)
        self.__product5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer4"):
                    opp_val = getattr(item, "customer4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer4"):
                    opp_val = getattr(item, "customer4", None)
                    
                    if opp_val is None:
                        setattr(item, "customer4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

