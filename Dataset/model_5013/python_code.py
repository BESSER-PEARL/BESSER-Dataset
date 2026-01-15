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

class epo_GlobalLocation:

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
class epo_Supplier:

    def __init__(self, name: str, epo_Supplier12: set["epo_PurchaseOrder"] = None, epo_Supplier15: set["epo_PurchaseOrder"] = None, epo_Supplier18: set["epo_PurchaseOrder"] = None, epo_Supplier: set["epo_Customer"] = None):
        self.name = name
        self.epo_Supplier12 = epo_Supplier12 if epo_Supplier12 is not None else set()
        self.epo_Supplier15 = epo_Supplier15 if epo_Supplier15 is not None else set()
        self.epo_Supplier18 = epo_Supplier18 if epo_Supplier18 is not None else set()
        self.epo_Supplier = epo_Supplier if epo_Supplier is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def epo_Supplier12(self):
        return self.__epo_Supplier12

    @epo_Supplier12.setter
    def epo_Supplier12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_Supplier__epo_Supplier12", None)
        self.__epo_Supplier12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "epo_PurchaseOrder13"):
                    opp_val = getattr(item, "epo_PurchaseOrder13", None)
                    
                    if opp_val == self:
                        setattr(item, "epo_PurchaseOrder13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "epo_PurchaseOrder13"):
                    opp_val = getattr(item, "epo_PurchaseOrder13", None)
                    
                    setattr(item, "epo_PurchaseOrder13", self)
                    

    @property
    def epo_Supplier18(self):
        return self.__epo_Supplier18

    @epo_Supplier18.setter
    def epo_Supplier18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_Supplier__epo_Supplier18", None)
        self.__epo_Supplier18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "epo_PurchaseOrder19"):
                    opp_val = getattr(item, "epo_PurchaseOrder19", None)
                    
                    if opp_val == self:
                        setattr(item, "epo_PurchaseOrder19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "epo_PurchaseOrder19"):
                    opp_val = getattr(item, "epo_PurchaseOrder19", None)
                    
                    setattr(item, "epo_PurchaseOrder19", self)
                    

    @property
    def epo_Supplier15(self):
        return self.__epo_Supplier15

    @epo_Supplier15.setter
    def epo_Supplier15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_Supplier__epo_Supplier15", None)
        self.__epo_Supplier15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "epo_PurchaseOrder16"):
                    opp_val = getattr(item, "epo_PurchaseOrder16", None)
                    
                    if opp_val == self:
                        setattr(item, "epo_PurchaseOrder16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "epo_PurchaseOrder16"):
                    opp_val = getattr(item, "epo_PurchaseOrder16", None)
                    
                    setattr(item, "epo_PurchaseOrder16", self)
                    

    @property
    def epo_Supplier(self):
        return self.__epo_Supplier

    @epo_Supplier.setter
    def epo_Supplier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_Supplier__epo_Supplier", None)
        self.__epo_Supplier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "epo_Customer"):
                    opp_val = getattr(item, "epo_Customer", None)
                    
                    if opp_val == self:
                        setattr(item, "epo_Customer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "epo_Customer"):
                    opp_val = getattr(item, "epo_Customer", None)
                    
                    setattr(item, "epo_Customer", self)
                    

class epo_Customer:

    def __init__(self, customerID: int, Customer: "epo_PurchaseOrder" = None, epo_Customer: "epo_Supplier" = None, customer: set["epo_PurchaseOrder"] = None):
        self.customerID = customerID
        self.Customer = Customer
        self.epo_Customer = epo_Customer
        self.customer = customer if customer is not None else set()
        
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
        old_value = getattr(self, f"_epo_Customer__Customer", None)
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
    def epo_Customer(self):
        return self.__epo_Customer

    @epo_Customer.setter
    def epo_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_Customer__epo_Customer", None)
        self.__epo_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo_Supplier"):
                opp_val = getattr(old_value, "epo_Supplier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo_Supplier"):
                opp_val = getattr(value, "epo_Supplier", None)
                if opp_val is None:
                    setattr(value, "epo_Supplier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_Customer__customer", None)
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
                    

class epo_Address(ABC):

    def __init__(self, name: str, country: str, epo_Address: "epo_PurchaseOrder" = None, epo_Address5: "epo_PurchaseOrder" = None):
        self.name = name
        self.country = country
        self.epo_Address = epo_Address
        self.epo_Address5 = epo_Address5
        
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
    def epo_Address5(self):
        return self.__epo_Address5

    @epo_Address5.setter
    def epo_Address5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_Address__epo_Address5", None)
        self.__epo_Address5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo_PurchaseOrder4"):
                opp_val = getattr(old_value, "epo_PurchaseOrder4", None)
                if opp_val == self:
                    setattr(old_value, "epo_PurchaseOrder4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo_PurchaseOrder4"):
                opp_val = getattr(value, "epo_PurchaseOrder4", None)
                setattr(value, "epo_PurchaseOrder4", self)

    @property
    def epo_Address(self):
        return self.__epo_Address

    @epo_Address.setter
    def epo_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_Address__epo_Address", None)
        self.__epo_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo_PurchaseOrder"):
                opp_val = getattr(old_value, "epo_PurchaseOrder", None)
                if opp_val == self:
                    setattr(old_value, "epo_PurchaseOrder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo_PurchaseOrder"):
                opp_val = getattr(value, "epo_PurchaseOrder", None)
                setattr(value, "epo_PurchaseOrder", self)

class Address:

    pass
class epo_CanadianAddress(Address):

    def __init__(self, street: str, city: str, province: str, postalCode: str):
        self.street = street
        self.city = city
        self.province = province
        self.postalCode = postalCode
        
    @property
    def province(self) -> str:
        return self.__province

    @province.setter
    def province(self, province: str):
        self.__province = province

    @property
    def postalCode(self) -> str:
        return self.__postalCode

    @postalCode.setter
    def postalCode(self, postalCode: str):
        self.__postalCode = postalCode

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

class epo_GlobalAddress(Address, GlobalLocation):

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class epo_USAddress(Address):

    def __init__(self, street: str, city: str, state: str, zip: int):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        
    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def zip(self) -> int:
        return self.__zip

    @zip.setter
    def zip(self, zip: int):
        self.__zip = zip

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

class epo_PurchaseOrder:

    def __init__(self, comment: str, orderDate: str, status: str, totalAmount: int, PurchaseOrder: "epo_Item" = None, epo_PurchaseOrder13: "epo_Supplier" = None, epo_PurchaseOrder16: "epo_Supplier" = None, epo_PurchaseOrder19: "epo_Supplier" = None, order: set["epo_Item"] = None, epo_PurchaseOrder: "epo_Address" = None, epo_PurchaseOrder4: "epo_Address" = None, orders: "epo_Customer" = None, epo_PurchaseOrder9: "epo_PurchaseOrder" = None, epo_PurchaseOrder7: "epo_PurchaseOrder" = None, PurchaseOrder21: "epo_Customer" = None):
        self.comment = comment
        self.orderDate = orderDate
        self.status = status
        self.totalAmount = totalAmount
        self.PurchaseOrder = PurchaseOrder
        self.epo_PurchaseOrder13 = epo_PurchaseOrder13
        self.epo_PurchaseOrder16 = epo_PurchaseOrder16
        self.epo_PurchaseOrder19 = epo_PurchaseOrder19
        self.order = order if order is not None else set()
        self.epo_PurchaseOrder = epo_PurchaseOrder
        self.epo_PurchaseOrder4 = epo_PurchaseOrder4
        self.orders = orders
        self.epo_PurchaseOrder9 = epo_PurchaseOrder9
        self.epo_PurchaseOrder7 = epo_PurchaseOrder7
        self.PurchaseOrder21 = PurchaseOrder21
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def totalAmount(self) -> int:
        return self.__totalAmount

    @totalAmount.setter
    def totalAmount(self, totalAmount: int):
        self.__totalAmount = totalAmount

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def orderDate(self) -> str:
        return self.__orderDate

    @orderDate.setter
    def orderDate(self, orderDate: str):
        self.__orderDate = orderDate

    @property
    def epo_PurchaseOrder13(self):
        return self.__epo_PurchaseOrder13

    @epo_PurchaseOrder13.setter
    def epo_PurchaseOrder13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_PurchaseOrder__epo_PurchaseOrder13", None)
        self.__epo_PurchaseOrder13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo_Supplier12"):
                opp_val = getattr(old_value, "epo_Supplier12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo_Supplier12"):
                opp_val = getattr(value, "epo_Supplier12", None)
                if opp_val is None:
                    setattr(value, "epo_Supplier12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_PurchaseOrder__order", None)
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
                    

    @property
    def orders(self):
        return self.__orders

    @orders.setter
    def orders(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_PurchaseOrder__orders", None)
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
    def epo_PurchaseOrder19(self):
        return self.__epo_PurchaseOrder19

    @epo_PurchaseOrder19.setter
    def epo_PurchaseOrder19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_PurchaseOrder__epo_PurchaseOrder19", None)
        self.__epo_PurchaseOrder19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo_Supplier18"):
                opp_val = getattr(old_value, "epo_Supplier18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo_Supplier18"):
                opp_val = getattr(value, "epo_Supplier18", None)
                if opp_val is None:
                    setattr(value, "epo_Supplier18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def epo_PurchaseOrder9(self):
        return self.__epo_PurchaseOrder9

    @epo_PurchaseOrder9.setter
    def epo_PurchaseOrder9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_PurchaseOrder__epo_PurchaseOrder9", None)
        self.__epo_PurchaseOrder9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo_PurchaseOrder7"):
                opp_val = getattr(old_value, "epo_PurchaseOrder7", None)
                if opp_val == self:
                    setattr(old_value, "epo_PurchaseOrder7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo_PurchaseOrder7"):
                opp_val = getattr(value, "epo_PurchaseOrder7", None)
                setattr(value, "epo_PurchaseOrder7", self)

    @property
    def PurchaseOrder(self):
        return self.__PurchaseOrder

    @PurchaseOrder.setter
    def PurchaseOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_PurchaseOrder__PurchaseOrder", None)
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
    def epo_PurchaseOrder(self):
        return self.__epo_PurchaseOrder

    @epo_PurchaseOrder.setter
    def epo_PurchaseOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_PurchaseOrder__epo_PurchaseOrder", None)
        self.__epo_PurchaseOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo_Address"):
                opp_val = getattr(old_value, "epo_Address", None)
                if opp_val == self:
                    setattr(old_value, "epo_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo_Address"):
                opp_val = getattr(value, "epo_Address", None)
                setattr(value, "epo_Address", self)

    @property
    def epo_PurchaseOrder16(self):
        return self.__epo_PurchaseOrder16

    @epo_PurchaseOrder16.setter
    def epo_PurchaseOrder16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_PurchaseOrder__epo_PurchaseOrder16", None)
        self.__epo_PurchaseOrder16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo_Supplier15"):
                opp_val = getattr(old_value, "epo_Supplier15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo_Supplier15"):
                opp_val = getattr(value, "epo_Supplier15", None)
                if opp_val is None:
                    setattr(value, "epo_Supplier15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def epo_PurchaseOrder7(self):
        return self.__epo_PurchaseOrder7

    @epo_PurchaseOrder7.setter
    def epo_PurchaseOrder7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_PurchaseOrder__epo_PurchaseOrder7", None)
        self.__epo_PurchaseOrder7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo_PurchaseOrder9"):
                opp_val = getattr(old_value, "epo_PurchaseOrder9", None)
                if opp_val == self:
                    setattr(old_value, "epo_PurchaseOrder9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo_PurchaseOrder9"):
                opp_val = getattr(value, "epo_PurchaseOrder9", None)
                setattr(value, "epo_PurchaseOrder9", self)

    @property
    def epo_PurchaseOrder4(self):
        return self.__epo_PurchaseOrder4

    @epo_PurchaseOrder4.setter
    def epo_PurchaseOrder4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_PurchaseOrder__epo_PurchaseOrder4", None)
        self.__epo_PurchaseOrder4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "epo_Address5"):
                opp_val = getattr(old_value, "epo_Address5", None)
                if opp_val == self:
                    setattr(old_value, "epo_Address5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "epo_Address5"):
                opp_val = getattr(value, "epo_Address5", None)
                setattr(value, "epo_Address5", self)

    @property
    def PurchaseOrder21(self):
        return self.__PurchaseOrder21

    @PurchaseOrder21.setter
    def PurchaseOrder21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_PurchaseOrder__PurchaseOrder21", None)
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

class epo_Item:

    def __init__(self, productName: str, quantity: int, USPrice: int, comment: str, shipDate: str, partNum: str, items: "epo_PurchaseOrder" = None, Item: "epo_PurchaseOrder" = None):
        self.productName = productName
        self.quantity = quantity
        self.USPrice = USPrice
        self.comment = comment
        self.shipDate = shipDate
        self.partNum = partNum
        self.items = items
        self.Item = Item
        
    @property
    def partNum(self) -> str:
        return self.__partNum

    @partNum.setter
    def partNum(self, partNum: str):
        self.__partNum = partNum

    @property
    def productName(self) -> str:
        return self.__productName

    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

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
    def USPrice(self) -> int:
        return self.__USPrice

    @USPrice.setter
    def USPrice(self, USPrice: int):
        self.__USPrice = USPrice

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_epo_Item__items", None)
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
        old_value = getattr(self, f"_epo_Item__Item", None)
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
