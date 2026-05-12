from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class MAINTAINS_THE_PRODUCTS_SERVICES_UseCase:

    pass


class ADMINISTRATOR_Actor:

    pass


class REACT_NATIVE_DEVELOPER_Actor:

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


class CREATES_THE_APPLICATION_UseCase:

    pass


class VISITS_THE_APPLICATION_UseCase:

    pass


class CUSTOMER_Actor:

    pass





class Showroom:

    def __init__(self, Car_Make: str, Model: str, Year: int, Horsepower: int, Price_Range: str, customer34: "Customer" = None):
        self.Car_Make = Car_Make
        self.Model = Model
        self.Year = Year
        self.Horsepower = Horsepower
        self.Price_Range = Price_Range
        self.customer34 = customer34
        
        pass
    @property
    def Year(self):
        return self.__Year
    @Year.setter
    def Year(self, Year: int):
        self.__Year = Year

    @property
    def Horsepower(self):
        return self.__Horsepower
    @Horsepower.setter
    def Horsepower(self, Horsepower: int):
        self.__Horsepower = Horsepower

    @property
    def Price_Range(self):
        return self.__Price_Range
    @Price_Range.setter
    def Price_Range(self, Price_Range: str):
        self.__Price_Range = Price_Range

    @property
    def Car_Make(self):
        return self.__Car_Make
    @Car_Make.setter
    def Car_Make(self, Car_Make: str):
        self.__Car_Make = Car_Make

    @property
    def Model(self):
        return self.__Model
    @Model.setter
    def Model(self, Model: str):
        self.__Model = Model

    @property
    def customer34(self):
        return self.__customer34
    @customer34.setter
    def customer34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Showroom__customer34", None)
        self.__customer34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "showroom35"):
                opp_val = getattr(old_value, "showroom35", None)
                if opp_val == self:
                    setattr(old_value, "showroom35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "showroom35"):
                opp_val = getattr(value, "showroom35", None)
                setattr(value, "showroom35", self)



class _unnamed:

    pass


class Appointment:

    def __init__(self, Time: float, Ap_ID: str, Confirmation: bool, E_ID: str, customercare33: "Customercare" = None):
        self.Time = Time
        self.Ap_ID = Ap_ID
        self.Confirmation = Confirmation
        self.E_ID = E_ID
        self.customercare33 = customercare33
        
        pass
    @property
    def Confirmation(self):
        return self.__Confirmation
    @Confirmation.setter
    def Confirmation(self, Confirmation: bool):
        self.__Confirmation = Confirmation

    @property
    def E_ID(self):
        return self.__E_ID
    @E_ID.setter
    def E_ID(self, E_ID: str):
        self.__E_ID = E_ID

    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: float):
        self.__Time = Time

    @property
    def Ap_ID(self):
        return self.__Ap_ID
    @Ap_ID.setter
    def Ap_ID(self, Ap_ID: str):
        self.__Ap_ID = Ap_ID

    @property
    def customercare33(self):
        return self.__customercare33
    @customercare33.setter
    def customercare33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appointment__customercare33", None)
        self.__customercare33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appointment32"):
                opp_val = getattr(old_value, "appointment32", None)
                if opp_val == self:
                    setattr(old_value, "appointment32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appointment32"):
                opp_val = getattr(value, "appointment32", None)
                setattr(value, "appointment32", self)



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
    def phoneno(self):
        return self.__phoneno
    @phoneno.setter
    def phoneno(self, phoneno: int):
        self.__phoneno = phoneno

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



class Customercare:

    def __init__(self, no: int, address: str, customer27: set["Customer"] = None, appointment32: "Appointment" = None):
        self.no = no
        self.address = address
        self.customer27 = customer27 if customer27 is not None else set()
        self.appointment32 = appointment32
        
        pass
    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self, no: int):
        self.__no = no

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def appointment32(self):
        return self.__appointment32
    @appointment32.setter
    def appointment32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customercare__appointment32", None)
        self.__appointment32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customercare33"):
                opp_val = getattr(old_value, "customercare33", None)
                if opp_val == self:
                    setattr(old_value, "customercare33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customercare33"):
                opp_val = getattr(value, "customercare33", None)
                setattr(value, "customercare33", self)

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
    def cashondelivery(self):
        return self.__cashondelivery
    @cashondelivery.setter
    def cashondelivery(self, cashondelivery: int):
        self.__cashondelivery = cashondelivery

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
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

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
                    



class Order:

    def __init__(self, list: str, item: str, quantity: int, pRODUCT24: set["Product"] = None):
        self.list = list
        self.item = item
        self.quantity = quantity
        self.pRODUCT24 = pRODUCT24 if pRODUCT24 is not None else set()
        
        pass
    @property
    def item(self):
        return self.__item
    @item.setter
    def item(self, item: str):
        self.__item = item

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def list(self):
        return self.__list
    @list.setter
    def list(self, list: str):
        self.__list = list

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

    def __init__(self, name: str, id: int, mailid: str, address: str, phoneno: int, customercare26: set["Customercare"] = None, showroom35: "Showroom" = None):
        self.name = name
        self.id = id
        self.mailid = mailid
        self.address = address
        self.phoneno = phoneno
        self.customercare26 = customercare26 if customercare26 is not None else set()
        self.showroom35 = showroom35
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

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

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def phoneno(self):
        return self.__phoneno
    @phoneno.setter
    def phoneno(self, phoneno: int):
        self.__phoneno = phoneno

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
                    

    @property
    def showroom35(self):
        return self.__showroom35
    @showroom35.setter
    def showroom35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__showroom35", None)
        self.__showroom35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer34"):
                opp_val = getattr(old_value, "customer34", None)
                if opp_val == self:
                    setattr(old_value, "customer34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer34"):
                opp_val = getattr(value, "customer34", None)
                setattr(value, "customer34", self)

