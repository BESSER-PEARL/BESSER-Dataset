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





class Cancelorder:

    def __init__(self, item: str, quantity: int):
        self.item = item
        self.quantity = quantity
        
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



class Feedback:

    def __init__(self, customername: str, id: int, phoneno: int):
        self.customername = customername
        self.id = id
        self.phoneno = phoneno
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def customername(self):
        return self.__customername
    @customername.setter
    def customername(self, customername: str):
        self.__customername = customername

    @property
    def phoneno(self):
        return self.__phoneno
    @phoneno.setter
    def phoneno(self, phoneno: int):
        self.__phoneno = phoneno



class Customercare:

    def __init__(self, no: int, address: str, customer27: set["Customer"] = None):
        self.no = no
        self.address = address
        self.customer27 = customer27 if customer27 is not None else set()
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self, no: int):
        self.__no = no

    @property
    def customer27(self):
        return self.__customer27
    @customer27.setter
    def customer27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customercare__customer27", None)
        self.__customer27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customercare26"):
                    opp_val = getattr(item, "customercare26", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customercare26"):
                    opp_val = getattr(item, "customercare26", None)
                    
                    if opp_val is None:
                        setattr(item, "customercare26", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Shipment:

    def __init__(self, packing: str, warehouse29: set["Warehouse"] = None):
        self.packing = packing
        self.warehouse29 = warehouse29 if warehouse29 is not None else set()
        
        pass
    @property
    def packing(self):
        return self.__packing
    @packing.setter
    def packing(self, packing: str):
        self.__packing = packing

    @property
    def warehouse29(self):
        return self.__warehouse29
    @warehouse29.setter
    def warehouse29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shipment__warehouse29", None)
        self.__warehouse29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shipment28"):
                    opp_val = getattr(item, "shipment28", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shipment28"):
                    opp_val = getattr(item, "shipment28", None)
                    
                    if opp_val is None:
                        setattr(item, "shipment28", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Transaction:

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

    def __init__(self, database: str, location: str, shipment28: set["Shipment"] = None, product31: set["Product"] = None):
        self.database = database
        self.location = location
        self.shipment28 = shipment28 if shipment28 is not None else set()
        self.product31 = product31 if product31 is not None else set()
        
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
    def shipment28(self):
        return self.__shipment28
    @shipment28.setter
    def shipment28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Warehouse__shipment28", None)
        self.__shipment28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "warehouse29"):
                    opp_val = getattr(item, "warehouse29", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "warehouse29"):
                    opp_val = getattr(item, "warehouse29", None)
                    
                    if opp_val is None:
                        setattr(item, "warehouse29", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def product31(self):
        return self.__product31
    @product31.setter
    def product31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Warehouse__product31", None)
        self.__product31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "warehouse30"):
                    opp_val = getattr(item, "warehouse30", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "warehouse30"):
                    opp_val = getattr(item, "warehouse30", None)
                    
                    if opp_val is None:
                        setattr(item, "warehouse30", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Product:

    def __init__(self, name: str, id: int, type: str, oRDER25: set["Order"] = None, warehouse30: set["Warehouse"] = None):
        self.name = name
        self.id = id
        self.type = type
        self.oRDER25 = oRDER25 if oRDER25 is not None else set()
        self.warehouse30 = warehouse30 if warehouse30 is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oRDER25(self):
        return self.__oRDER25
    @oRDER25.setter
    def oRDER25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__oRDER25", None)
        self.__oRDER25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pRODUCT24"):
                    opp_val = getattr(item, "pRODUCT24", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pRODUCT24"):
                    opp_val = getattr(item, "pRODUCT24", None)
                    
                    if opp_val is None:
                        setattr(item, "pRODUCT24", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def warehouse30(self):
        return self.__warehouse30
    @warehouse30.setter
    def warehouse30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__warehouse30", None)
        self.__warehouse30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product31"):
                    opp_val = getattr(item, "product31", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product31"):
                    opp_val = getattr(item, "product31", None)
                    
                    if opp_val is None:
                        setattr(item, "product31", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Order:

    def __init__(self, item: str, quantity: int, list: str, pRODUCT24: set["Product"] = None):
        self.item = item
        self.quantity = quantity
        self.list = list
        self.pRODUCT24 = pRODUCT24 if pRODUCT24 is not None else set()
        
        pass
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
    def item(self):
        return self.__item
    @item.setter
    def item(self, item: str):
        self.__item = item

    @property
    def pRODUCT24(self):
        return self.__pRODUCT24
    @pRODUCT24.setter
    def pRODUCT24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__pRODUCT24", None)
        self.__pRODUCT24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oRDER25"):
                    opp_val = getattr(item, "oRDER25", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oRDER25"):
                    opp_val = getattr(item, "oRDER25", None)
                    
                    if opp_val is None:
                        setattr(item, "oRDER25", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Customer:

    def __init__(self, mailid: str, address: str, phoneno: int, name: str, id: int, customercare26: set["Customercare"] = None):
        self.mailid = mailid
        self.address = address
        self.phoneno = phoneno
        self.name = name
        self.id = id
        self.customercare26 = customercare26 if customercare26 is not None else set()
        
        pass
    @property
    def mailid(self):
        return self.__mailid
    @mailid.setter
    def mailid(self, mailid: str):
        self.__mailid = mailid

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def phoneno(self):
        return self.__phoneno
    @phoneno.setter
    def phoneno(self, phoneno: int):
        self.__phoneno = phoneno

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def customercare26(self):
        return self.__customercare26
    @customercare26.setter
    def customercare26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__customercare26", None)
        self.__customercare26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer27"):
                    opp_val = getattr(item, "customer27", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer27"):
                    opp_val = getattr(item, "customer27", None)
                    
                    if opp_val is None:
                        setattr(item, "customer27", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

