from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class OrderStatus(Enum):
    Pending = "Pending"
    BackOrder = "BackOrder"
    Complete = "Complete"


############################################
# Definition of Classes
############################################

class epo2_Supplier:

    def __init__(self, name: str, epo2_Supplier: set["epo2_Customer"] = None, epo2_Supplier12: set["epo2_PurchaseOrder"] = None, epo2_Supplier15: set["epo2_PurchaseOrder"] = None, epo2_Supplier18: set["epo2_PurchaseOrder"] = None):
        self.name = name
        self.epo2_Supplier = epo2_Supplier if epo2_Supplier is not None else set()
        self.epo2_Supplier12 = epo2_Supplier12 if epo2_Supplier12 is not None else set()
        self.epo2_Supplier15 = epo2_Supplier15 if epo2_Supplier15 is not None else set()
        self.epo2_Supplier18 = epo2_Supplier18 if epo2_Supplier18 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def epo2_Supplier15(self):
        return self.__epo2_Supplier15

    @epo2_Supplier15.setter
    def epo2_Supplier15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_Supplier__epo2_Supplier15", None)
        self.__epo2_Supplier15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "epo2_PurchaseOrder16"):
                    opp_val = getattr(item, "epo2_PurchaseOrder16", None)
                    
                    if opp_val == self:
                        setattr(item, "epo2_PurchaseOrder16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "epo2_PurchaseOrder16"):
                    opp_val = getattr(item, "epo2_PurchaseOrder16", None)
                    
                    setattr(item, "epo2_PurchaseOrder16", self)
                    

    @property
    def epo2_Supplier12(self):
        return self.__epo2_Supplier12

    @epo2_Supplier12.setter
    def epo2_Supplier12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_Supplier__epo2_Supplier12", None)
        self.__epo2_Supplier12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "epo2_PurchaseOrder13"):
                    opp_val = getattr(item, "epo2_PurchaseOrder13", None)
                    
                    if opp_val == self:
                        setattr(item, "epo2_PurchaseOrder13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "epo2_PurchaseOrder13"):
                    opp_val = getattr(item, "epo2_PurchaseOrder13", None)
                    
                    setattr(item, "epo2_PurchaseOrder13", self)
                    

    @property
    def epo2_Supplier(self):
        return self.__epo2_Supplier

    @epo2_Supplier.setter
    def epo2_Supplier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_Supplier__epo2_Supplier", None)
        self.__epo2_Supplier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "epo2_Customer"):
                    opp_val = getattr(item, "epo2_Customer", None)
                    
                    if opp_val == self:
                        setattr(item, "epo2_Customer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "epo2_Customer"):
                    opp_val = getattr(item, "epo2_Customer", None)
                    
                    setattr(item, "epo2_Customer", self)
                    

    @property
    def epo2_Supplier18(self):
        return self.__epo2_Supplier18

    @epo2_Supplier18.setter
    def epo2_Supplier18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_Supplier__epo2_Supplier18", None)
        self.__epo2_Supplier18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "epo2_PurchaseOrder19"):
                    opp_val = getattr(item, "epo2_PurchaseOrder19", None)
                    
                    if opp_val == self:
                        setattr(item, "epo2_PurchaseOrder19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "epo2_PurchaseOrder19"):
                    opp_val = getattr(item, "epo2_PurchaseOrder19", None)
                    
                    setattr(item, "epo2_PurchaseOrder19", self)
                    

class epo2_Customer:

    def __init__(self, customerID: int, epo2_Customer: "epo2_Supplier" = None, customer: set["epo2_PurchaseOrder"] = None, Customer: "epo2_PurchaseOrder" = None):
        self.customerID = customerID
        self.epo2_Customer = epo2_Customer
        self.customer = customer if customer is not None else set()
        self.Customer = Customer
        
    @property
    def customerID(self) -> int:
        return self.__customerID

    @customerID.setter
    def customerID(self, customerID: int):
        self.__customerID = customerID

    @property
    def Customer(self):
        return self.__Customer

    @Customer.setter
    def Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_Customer__Customer", None)
        self.__Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders"):
                opp_val = getattr(old_value, "orders", None)
                if opp_val == self:
                    setattr(old_value, "orders", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders"):
                opp_val = getattr(value, "orders", None)
                setattr(value, "orders", self)

    @property
    def epo2_Customer(self):
        return self.__epo2_Customer

    @epo2_Customer.setter
    def epo2_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_Customer__epo2_Customer", None)
        self.__epo2_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo2_Supplier"):
                opp_val = getattr(old_value, "epo2_Supplier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo2_Supplier"):
                opp_val = getattr(value, "epo2_Supplier", None)
                if opp_val is None:
                    setattr(value, "epo2_Supplier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_Customer__customer", None)
        self.__customer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PurchaseOrder21"):
                    opp_val = getattr(item, "PurchaseOrder21", None)
                    
                    if opp_val == self:
                        setattr(item, "PurchaseOrder21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PurchaseOrder21"):
                    opp_val = getattr(item, "PurchaseOrder21", None)
                    
                    setattr(item, "PurchaseOrder21", self)
                    

class epo2_GlobalLocation:

    def __init__(self, countryCode: int):
        self.countryCode = countryCode
        
    @property
    def countryCode(self) -> int:
        return self.__countryCode

    @countryCode.setter
    def countryCode(self, countryCode: int):
        self.__countryCode = countryCode

class GlobalLocation:

    pass
class epo2_Address(ABC):

    def __init__(self, name: str, country: str, epo2_Address: "epo2_PurchaseOrder" = None, epo2_Address5: "epo2_PurchaseOrder" = None):
        self.name = name
        self.country = country
        self.epo2_Address = epo2_Address
        self.epo2_Address5 = epo2_Address5
        
    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def epo2_Address(self):
        return self.__epo2_Address

    @epo2_Address.setter
    def epo2_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_Address__epo2_Address", None)
        self.__epo2_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo2_PurchaseOrder"):
                opp_val = getattr(old_value, "epo2_PurchaseOrder", None)
                if opp_val == self:
                    setattr(old_value, "epo2_PurchaseOrder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo2_PurchaseOrder"):
                opp_val = getattr(value, "epo2_PurchaseOrder", None)
                setattr(value, "epo2_PurchaseOrder", self)

    @property
    def epo2_Address5(self):
        return self.__epo2_Address5

    @epo2_Address5.setter
    def epo2_Address5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_Address__epo2_Address5", None)
        self.__epo2_Address5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo2_PurchaseOrder4"):
                opp_val = getattr(old_value, "epo2_PurchaseOrder4", None)
                if opp_val == self:
                    setattr(old_value, "epo2_PurchaseOrder4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo2_PurchaseOrder4"):
                opp_val = getattr(value, "epo2_PurchaseOrder4", None)
                setattr(value, "epo2_PurchaseOrder4", self)

class Address:

    pass
class epo2_GlobalAddress(GlobalLocation, Address):

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class epo2_USAddress(Address):

    def __init__(self, street: str, city: str, state: str, zip: int):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        
    @property
    def zip(self) -> int:
        return self.__zip

    @zip.setter
    def zip(self, zip: int):
        self.__zip = zip

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

class epo2_PurchaseOrder:

    def __init__(self, comment: str, orderDate: str, status: str, totalAmount: int, PurchaseOrder: "epo2_Item" = None, order: set["epo2_Item"] = None, epo2_PurchaseOrder: "epo2_Address" = None, epo2_PurchaseOrder13: "epo2_Supplier" = None, epo2_PurchaseOrder16: "epo2_Supplier" = None, epo2_PurchaseOrder19: "epo2_Supplier" = None, PurchaseOrder21: "epo2_Customer" = None, epo2_PurchaseOrder4: "epo2_Address" = None, orders: "epo2_Customer" = None, epo2_PurchaseOrder9: "epo2_PurchaseOrder" = None, epo2_PurchaseOrder7: "epo2_PurchaseOrder" = None):
        self.comment = comment
        self.orderDate = orderDate
        self.status = status
        self.totalAmount = totalAmount
        self.PurchaseOrder = PurchaseOrder
        self.order = order if order is not None else set()
        self.epo2_PurchaseOrder = epo2_PurchaseOrder
        self.epo2_PurchaseOrder13 = epo2_PurchaseOrder13
        self.epo2_PurchaseOrder16 = epo2_PurchaseOrder16
        self.epo2_PurchaseOrder19 = epo2_PurchaseOrder19
        self.PurchaseOrder21 = PurchaseOrder21
        self.epo2_PurchaseOrder4 = epo2_PurchaseOrder4
        self.orders = orders
        self.epo2_PurchaseOrder9 = epo2_PurchaseOrder9
        self.epo2_PurchaseOrder7 = epo2_PurchaseOrder7
        
    @property
    def totalAmount(self) -> int:
        return self.__totalAmount

    @totalAmount.setter
    def totalAmount(self, totalAmount: int):
        self.__totalAmount = totalAmount

    @property
    def orderDate(self) -> str:
        return self.__orderDate

    @orderDate.setter
    def orderDate(self, orderDate: str):
        self.__orderDate = orderDate

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def epo2_PurchaseOrder4(self):
        return self.__epo2_PurchaseOrder4

    @epo2_PurchaseOrder4.setter
    def epo2_PurchaseOrder4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_PurchaseOrder__epo2_PurchaseOrder4", None)
        self.__epo2_PurchaseOrder4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo2_Address5"):
                opp_val = getattr(old_value, "epo2_Address5", None)
                if opp_val == self:
                    setattr(old_value, "epo2_Address5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo2_Address5"):
                opp_val = getattr(value, "epo2_Address5", None)
                setattr(value, "epo2_Address5", self)

    @property
    def epo2_PurchaseOrder(self):
        return self.__epo2_PurchaseOrder

    @epo2_PurchaseOrder.setter
    def epo2_PurchaseOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_PurchaseOrder__epo2_PurchaseOrder", None)
        self.__epo2_PurchaseOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo2_Address"):
                opp_val = getattr(old_value, "epo2_Address", None)
                if opp_val == self:
                    setattr(old_value, "epo2_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo2_Address"):
                opp_val = getattr(value, "epo2_Address", None)
                setattr(value, "epo2_Address", self)

    @property
    def orders(self):
        return self.__orders

    @orders.setter
    def orders(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_PurchaseOrder__orders", None)
        self.__orders = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer"):
                opp_val = getattr(old_value, "Customer", None)
                if opp_val == self:
                    setattr(old_value, "Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer"):
                opp_val = getattr(value, "Customer", None)
                setattr(value, "Customer", self)

    @property
    def epo2_PurchaseOrder9(self):
        return self.__epo2_PurchaseOrder9

    @epo2_PurchaseOrder9.setter
    def epo2_PurchaseOrder9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_PurchaseOrder__epo2_PurchaseOrder9", None)
        self.__epo2_PurchaseOrder9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo2_PurchaseOrder7"):
                opp_val = getattr(old_value, "epo2_PurchaseOrder7", None)
                if opp_val == self:
                    setattr(old_value, "epo2_PurchaseOrder7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo2_PurchaseOrder7"):
                opp_val = getattr(value, "epo2_PurchaseOrder7", None)
                setattr(value, "epo2_PurchaseOrder7", self)

    @property
    def epo2_PurchaseOrder13(self):
        return self.__epo2_PurchaseOrder13

    @epo2_PurchaseOrder13.setter
    def epo2_PurchaseOrder13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_PurchaseOrder__epo2_PurchaseOrder13", None)
        self.__epo2_PurchaseOrder13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo2_Supplier12"):
                opp_val = getattr(old_value, "epo2_Supplier12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo2_Supplier12"):
                opp_val = getattr(value, "epo2_Supplier12", None)
                if opp_val is None:
                    setattr(value, "epo2_Supplier12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def epo2_PurchaseOrder7(self):
        return self.__epo2_PurchaseOrder7

    @epo2_PurchaseOrder7.setter
    def epo2_PurchaseOrder7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_PurchaseOrder__epo2_PurchaseOrder7", None)
        self.__epo2_PurchaseOrder7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo2_PurchaseOrder9"):
                opp_val = getattr(old_value, "epo2_PurchaseOrder9", None)
                if opp_val == self:
                    setattr(old_value, "epo2_PurchaseOrder9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo2_PurchaseOrder9"):
                opp_val = getattr(value, "epo2_PurchaseOrder9", None)
                setattr(value, "epo2_PurchaseOrder9", self)

    @property
    def epo2_PurchaseOrder16(self):
        return self.__epo2_PurchaseOrder16

    @epo2_PurchaseOrder16.setter
    def epo2_PurchaseOrder16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_PurchaseOrder__epo2_PurchaseOrder16", None)
        self.__epo2_PurchaseOrder16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo2_Supplier15"):
                opp_val = getattr(old_value, "epo2_Supplier15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo2_Supplier15"):
                opp_val = getattr(value, "epo2_Supplier15", None)
                if opp_val is None:
                    setattr(value, "epo2_Supplier15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PurchaseOrder(self):
        return self.__PurchaseOrder

    @PurchaseOrder.setter
    def PurchaseOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_PurchaseOrder__PurchaseOrder", None)
        self.__PurchaseOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items"):
                opp_val = getattr(old_value, "items", None)
                if opp_val == self:
                    setattr(old_value, "items", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items"):
                opp_val = getattr(value, "items", None)
                setattr(value, "items", self)

    @property
    def PurchaseOrder21(self):
        return self.__PurchaseOrder21

    @PurchaseOrder21.setter
    def PurchaseOrder21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_PurchaseOrder__PurchaseOrder21", None)
        self.__PurchaseOrder21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer"):
                opp_val = getattr(old_value, "customer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer"):
                opp_val = getattr(value, "customer", None)
                if opp_val is None:
                    setattr(value, "customer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def epo2_PurchaseOrder19(self):
        return self.__epo2_PurchaseOrder19

    @epo2_PurchaseOrder19.setter
    def epo2_PurchaseOrder19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_PurchaseOrder__epo2_PurchaseOrder19", None)
        self.__epo2_PurchaseOrder19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo2_Supplier18"):
                opp_val = getattr(old_value, "epo2_Supplier18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo2_Supplier18"):
                opp_val = getattr(value, "epo2_Supplier18", None)
                if opp_val is None:
                    setattr(value, "epo2_Supplier18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_PurchaseOrder__order", None)
        self.__order = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Item"):
                    opp_val = getattr(item, "Item", None)
                    
                    if opp_val == self:
                        setattr(item, "Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Item"):
                    opp_val = getattr(item, "Item", None)
                    
                    setattr(item, "Item", self)
                    

class epo2_Item:

    def __init__(self, productName: str, quantity: int, USPrice: int, comment: str, shipDate: str, partNum: str, items: "epo2_PurchaseOrder" = None, Item: "epo2_PurchaseOrder" = None):
        self.productName = productName
        self.quantity = quantity
        self.USPrice = USPrice
        self.comment = comment
        self.shipDate = shipDate
        self.partNum = partNum
        self.items = items
        self.Item = Item
        
    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def USPrice(self) -> int:
        return self.__USPrice

    @USPrice.setter
    def USPrice(self, USPrice: int):
        self.__USPrice = USPrice

    @property
    def productName(self) -> str:
        return self.__productName

    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def partNum(self) -> str:
        return self.__partNum

    @partNum.setter
    def partNum(self, partNum: str):
        self.__partNum = partNum

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def shipDate(self) -> str:
        return self.__shipDate

    @shipDate.setter
    def shipDate(self, shipDate: str):
        self.__shipDate = shipDate

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_Item__items", None)
        self.__items = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PurchaseOrder"):
                opp_val = getattr(old_value, "PurchaseOrder", None)
                if opp_val == self:
                    setattr(old_value, "PurchaseOrder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PurchaseOrder"):
                opp_val = getattr(value, "PurchaseOrder", None)
                setattr(value, "PurchaseOrder", self)

    @property
    def Item(self):
        return self.__Item

    @Item.setter
    def Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo2_Item__Item", None)
        self.__Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order"):
                opp_val = getattr(old_value, "order", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order"):
                opp_val = getattr(value, "order", None)
                if opp_val is None:
                    setattr(value, "order", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
