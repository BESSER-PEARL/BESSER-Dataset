from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class MAINTAINS_THE_PRODUCTS_SERVICES_UseCase:

    pass


class ADMINISTRATOR_Actor:

    pass


class WEB_DEVELOPER_Actor:

    pass


class SUPPORT_AND_FEEDBACK_UseCase:

    pass


class DELIVERS_THE_PRODUCT_UseCase:

    pass


class PAYS_THE_BILL_UseCase:

    pass


class SELECTS_THE_MODE_OF_PAYMENT_UseCase:

    pass


class ADDS_ITEMS_SERVICE_TO_CART_UseCase:

    pass


class SELECTS_THE_ITEMS_SERVICE_UseCase:

    pass


class CREATES_THE_WEBSITE_UseCase:

    pass


class VISITS_THE_WEBSITE_UseCase:

    pass


class CUSTOMER_Actor:

    pass





class Customer:

    def __init__(self, name: str, id: int, mailid: str, address: str):
        self.name = name
        self.id = id
        self.mailid = mailid
        self.address = address
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def mailid(self):
        return self.__mailid
    @mailid.setter
    def mailid(self, mailid: str):
        self.__mailid = mailid

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class Cancelorder:

    def __init__(self, item: str):
        self.item = item
        
        pass
    @property
    def item(self):
        return self.__item
    @item.setter
    def item(self, item: str):
        self.__item = item



class Shipment:

    def __init__(self, packing: str, warehouse27: set["Warehouse"] = None):
        self.packing = packing
        self.warehouse27 = warehouse27 if warehouse27 is not None else set()
        
        pass
    @property
    def packing(self):
        return self.__packing
    @packing.setter
    def packing(self, packing: str):
        self.__packing = packing

    @property
    def warehouse27(self):
        return self.__warehouse27
    @warehouse27.setter
    def warehouse27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shipment__warehouse27", None)
        self.__warehouse27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shipment26"):
                    opp_val = getattr(item, "shipment26", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shipment26"):
                    opp_val = getattr(item, "shipment26", None)
                    
                    if opp_val is None:
                        setattr(item, "shipment26", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Feedback:

    def __init__(self, cashondelivery: int, debitcard: int, creditcard: int):
        self.cashondelivery = cashondelivery
        self.debitcard = debitcard
        self.creditcard = creditcard
        
        pass
    @property
    def creditcard(self):
        return self.__creditcard
    @creditcard.setter
    def creditcard(self, creditcard: int):
        self.__creditcard = creditcard

    @property
    def debitcard(self):
        return self.__debitcard
    @debitcard.setter
    def debitcard(self, debitcard: int):
        self.__debitcard = debitcard

    @property
    def cashondelivery(self):
        return self.__cashondelivery
    @cashondelivery.setter
    def cashondelivery(self, cashondelivery: int):
        self.__cashondelivery = cashondelivery



class Warehouse:

    def __init__(self, database: str, location: str, shipment26: set["Shipment"] = None, product29: set["Product"] = None):
        self.database = database
        self.location = location
        self.shipment26 = shipment26 if shipment26 is not None else set()
        self.product29 = product29 if product29 is not None else set()
        
        pass
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def database(self):
        return self.__database
    @database.setter
    def database(self, database: str):
        self.__database = database

    @property
    def product29(self):
        return self.__product29
    @product29.setter
    def product29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Warehouse__product29", None)
        self.__product29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "warehouse28"):
                    opp_val = getattr(item, "warehouse28", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "warehouse28"):
                    opp_val = getattr(item, "warehouse28", None)
                    
                    if opp_val is None:
                        setattr(item, "warehouse28", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def shipment26(self):
        return self.__shipment26
    @shipment26.setter
    def shipment26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Warehouse__shipment26", None)
        self.__shipment26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "warehouse27"):
                    opp_val = getattr(item, "warehouse27", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "warehouse27"):
                    opp_val = getattr(item, "warehouse27", None)
                    
                    if opp_val is None:
                        setattr(item, "warehouse27", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Product:

    def __init__(self, name: str, id: int, Order25: set["Order"] = None, warehouse28: set["Warehouse"] = None):
        self.name = name
        self.id = id
        self.Order25 = Order25 if Order25 is not None else set()
        self.warehouse28 = warehouse28 if warehouse28 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Order25(self):
        return self.__Order25
    @Order25.setter
    def Order25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__Order25", None)
        self.__Order25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Product24"):
                    opp_val = getattr(item, "Product24", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Product24"):
                    opp_val = getattr(item, "Product24", None)
                    
                    if opp_val is None:
                        setattr(item, "Product24", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def warehouse28(self):
        return self.__warehouse28
    @warehouse28.setter
    def warehouse28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__warehouse28", None)
        self.__warehouse28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product29"):
                    opp_val = getattr(item, "product29", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product29"):
                    opp_val = getattr(item, "product29", None)
                    
                    if opp_val is None:
                        setattr(item, "product29", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Order:

    def __init__(self, item: str, quantity: int, list: str, Product24: set["Product"] = None):
        self.item = item
        self.quantity = quantity
        self.list = list
        self.Product24 = Product24 if Product24 is not None else set()
        
        pass
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def item(self):
        return self.__item
    @item.setter
    def item(self, item: str):
        self.__item = item

    @property
    def list(self):
        return self.__list
    @list.setter
    def list(self, list: str):
        self.__list = list

    @property
    def Product24(self):
        return self.__Product24
    @Product24.setter
    def Product24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__Product24", None)
        self.__Product24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Order25"):
                    opp_val = getattr(item, "Order25", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Order25"):
                    opp_val = getattr(item, "Order25", None)
                    
                    if opp_val is None:
                        setattr(item, "Order25", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

