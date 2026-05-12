from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Actor_Actor:

    pass


class UseCase2_UseCase:

    pass


class UseCase_UseCase:

    pass


class Credit_card_UseCase:

    pass


class Cash_UseCase:

    pass


class express_UseCase:

    pass


class Normal_UseCase:

    pass


class set_deducted_percent_UseCase:

    pass


class Set_period_of_ship_UseCase:

    pass


class Se_price_UseCase:

    pass


class Get_dedcuted_percent_UseCase:

    pass


class Cancel_UseCase:

    pass


class Pay_UseCase:

    pass


class Point_system_UseCase:

    pass


class Shipping_UseCase:

    pass


class Company_Actor:

    pass


class customer_Actor:

    pass


class Internet_____________________network_UseCase:

    pass


class Client_3_UseCase:

    pass


class Client_4_UseCase:

    pass


class Client_2_UseCase:

    pass


class Client_1_UseCase:

    pass


class Shipmment_UseCase:

    pass





class mysubject_Component:

    pass


class Order_server_Component:

    pass


class Shipment_server_Component:

    pass


class Payment:

    def __init__(self, Amuant: int, Order_Payment_17: "Order" = None):
        self.Amuant = Amuant
        self.Order_Payment_17 = Order_Payment_17
        
        pass
    @property
    def Amuant(self):
        return self.__Amuant
    @Amuant.setter
    def Amuant(self, Amuant: int):
        self.__Amuant = Amuant

    @property
    def Order_Payment_17(self):
        return self.__Order_Payment_17
    @Order_Payment_17.setter
    def Order_Payment_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__Order_Payment_17", None)
        self.__Order_Payment_17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order_Payment_06"):
                opp_val = getattr(old_value, "Order_Payment_06", None)
                if opp_val == self:
                    setattr(old_value, "Order_Payment_06", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order_Payment_06"):
                opp_val = getattr(value, "Order_Payment_06", None)
                setattr(value, "Order_Payment_06", self)



class CreditCard:

    def __init__(self, CCNumber: int):
        self.CCNumber = CCNumber
        
        pass
    @property
    def CCNumber(self):
        return self.__CCNumber
    @CCNumber.setter
    def CCNumber(self, CCNumber: int):
        self.__CCNumber = CCNumber



class Cahs:

    pass


class Item:

    def __init__(self, Quantity: int, price: int, ItemID: int, Item_Order_04: "Order" = None):
        self.Quantity = Quantity
        self.price = price
        self.ItemID = ItemID
        self.Item_Order_04 = Item_Order_04
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def ItemID(self):
        return self.__ItemID
    @ItemID.setter
    def ItemID(self, ItemID: int):
        self.__ItemID = ItemID

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def Item_Order_04(self):
        return self.__Item_Order_04
    @Item_Order_04.setter
    def Item_Order_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__Item_Order_04", None)
        self.__Item_Order_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Item_Order_15"):
                opp_val = getattr(old_value, "Item_Order_15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Item_Order_15"):
                opp_val = getattr(value, "Item_Order_15", None)
                if opp_val is None:
                    setattr(value, "Item_Order_15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order:

    def __init__(self, orderSirealNumber: int, Order_Costomer_00: "Costomer" = None, Item_Order_15: set["Item"] = None, Order_Payment_06: "Payment" = None):
        self.orderSirealNumber = orderSirealNumber
        self.Order_Costomer_00 = Order_Costomer_00
        self.Item_Order_15 = Item_Order_15 if Item_Order_15 is not None else set()
        self.Order_Payment_06 = Order_Payment_06
        
        pass
    @property
    def orderSirealNumber(self):
        return self.__orderSirealNumber
    @orderSirealNumber.setter
    def orderSirealNumber(self, orderSirealNumber: int):
        self.__orderSirealNumber = orderSirealNumber

    @property
    def Item_Order_15(self):
        return self.__Item_Order_15
    @Item_Order_15.setter
    def Item_Order_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__Item_Order_15", None)
        self.__Item_Order_15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Item_Order_04"):
                    opp_val = getattr(item, "Item_Order_04", None)
                    
                    if opp_val == self:
                        setattr(item, "Item_Order_04", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Item_Order_04"):
                    opp_val = getattr(item, "Item_Order_04", None)
                    
                    setattr(item, "Item_Order_04", self)
                    

    @property
    def Order_Costomer_00(self):
        return self.__Order_Costomer_00
    @Order_Costomer_00.setter
    def Order_Costomer_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__Order_Costomer_00", None)
        self.__Order_Costomer_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ship_to1"):
                opp_val = getattr(old_value, "ship_to1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ship_to1"):
                opp_val = getattr(value, "ship_to1", None)
                if opp_val is None:
                    setattr(value, "ship_to1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Order_Payment_06(self):
        return self.__Order_Payment_06
    @Order_Payment_06.setter
    def Order_Payment_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__Order_Payment_06", None)
        self.__Order_Payment_06 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order_Payment_17"):
                opp_val = getattr(old_value, "Order_Payment_17", None)
                if opp_val == self:
                    setattr(old_value, "Order_Payment_17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order_Payment_17"):
                opp_val = getattr(value, "Order_Payment_17", None)
                setattr(value, "Order_Payment_17", self)



class Normal:

    pass


class Express:

    pass


class MyClass:

    pass


class Shipment:

    def __init__(self, pireodofShip: int, Date: date, Forbidden_to_ship: str, SippingType: str, has_shippment3: set["Costomer"] = None):
        self.pireodofShip = pireodofShip
        self.Date = Date
        self.Forbidden_to_ship = Forbidden_to_ship
        self.SippingType = SippingType
        self.has_shippment3 = has_shippment3 if has_shippment3 is not None else set()
        
        pass
    @property
    def Forbidden_to_ship(self):
        return self.__Forbidden_to_ship
    @Forbidden_to_ship.setter
    def Forbidden_to_ship(self, Forbidden_to_ship: str):
        self.__Forbidden_to_ship = Forbidden_to_ship

    @property
    def SippingType(self):
        return self.__SippingType
    @SippingType.setter
    def SippingType(self, SippingType: str):
        self.__SippingType = SippingType

    @property
    def pireodofShip(self):
        return self.__pireodofShip
    @pireodofShip.setter
    def pireodofShip(self, pireodofShip: int):
        self.__pireodofShip = pireodofShip

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: date):
        self.__Date = Date

    @property
    def has_shippment3(self):
        return self.__has_shippment3
    @has_shippment3.setter
    def has_shippment3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shipment__has_shippment3", None)
        self.__has_shippment3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Costomer_Shipment_02"):
                    opp_val = getattr(item, "Costomer_Shipment_02", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Costomer_Shipment_02"):
                    opp_val = getattr(item, "Costomer_Shipment_02", None)
                    
                    if opp_val is None:
                        setattr(item, "Costomer_Shipment_02", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Costomer:

    def __init__(self, Name: str, ID: int, Address: str, Email: str, mobileNumber: int, ship_to1: set["Order"] = None, Costomer_Shipment_02: set["Shipment"] = None):
        self.Name = Name
        self.ID = ID
        self.Address = Address
        self.Email = Email
        self.mobileNumber = mobileNumber
        self.ship_to1 = ship_to1 if ship_to1 is not None else set()
        self.Costomer_Shipment_02 = Costomer_Shipment_02 if Costomer_Shipment_02 is not None else set()
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def mobileNumber(self):
        return self.__mobileNumber
    @mobileNumber.setter
    def mobileNumber(self, mobileNumber: int):
        self.__mobileNumber = mobileNumber

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Costomer_Shipment_02(self):
        return self.__Costomer_Shipment_02
    @Costomer_Shipment_02.setter
    def Costomer_Shipment_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Costomer__Costomer_Shipment_02", None)
        self.__Costomer_Shipment_02 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has_shippment3"):
                    opp_val = getattr(item, "has_shippment3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has_shippment3"):
                    opp_val = getattr(item, "has_shippment3", None)
                    
                    if opp_val is None:
                        setattr(item, "has_shippment3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def ship_to1(self):
        return self.__ship_to1
    @ship_to1.setter
    def ship_to1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Costomer__ship_to1", None)
        self.__ship_to1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Order_Costomer_00"):
                    opp_val = getattr(item, "Order_Costomer_00", None)
                    
                    if opp_val == self:
                        setattr(item, "Order_Costomer_00", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Order_Costomer_00"):
                    opp_val = getattr(item, "Order_Costomer_00", None)
                    
                    setattr(item, "Order_Costomer_00", self)
                    

