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

class extendedPO2_Supplier:

    def __init__(self, name: str, extendedPO2_Supplier: set["extendedPO2_PurchaseOrder"] = None, extendedPO2_Supplier15: set["extendedPO2_Customer"] = None, extendedPO2_Supplier17: set["extendedPO2_PurchaseOrder"] = None, extendedPO2_Supplier20: set["extendedPO2_PurchaseOrder"] = None):
        self.name = name
        self.extendedPO2_Supplier = extendedPO2_Supplier if extendedPO2_Supplier is not None else set()
        self.extendedPO2_Supplier15 = extendedPO2_Supplier15 if extendedPO2_Supplier15 is not None else set()
        self.extendedPO2_Supplier17 = extendedPO2_Supplier17 if extendedPO2_Supplier17 is not None else set()
        self.extendedPO2_Supplier20 = extendedPO2_Supplier20 if extendedPO2_Supplier20 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def extendedPO2_Supplier15(self):
        return self.__extendedPO2_Supplier15

    @extendedPO2_Supplier15.setter
    def extendedPO2_Supplier15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_Supplier__extendedPO2_Supplier15", None)
        self.__extendedPO2_Supplier15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extendedPO2_Customer"):
                    opp_val = getattr(item, "extendedPO2_Customer", None)
                    
                    if opp_val == self:
                        setattr(item, "extendedPO2_Customer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extendedPO2_Customer"):
                    opp_val = getattr(item, "extendedPO2_Customer", None)
                    
                    setattr(item, "extendedPO2_Customer", self)
                    

    @property
    def extendedPO2_Supplier(self):
        return self.__extendedPO2_Supplier

    @extendedPO2_Supplier.setter
    def extendedPO2_Supplier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_Supplier__extendedPO2_Supplier", None)
        self.__extendedPO2_Supplier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extendedPO2_PurchaseOrder13"):
                    opp_val = getattr(item, "extendedPO2_PurchaseOrder13", None)
                    
                    if opp_val == self:
                        setattr(item, "extendedPO2_PurchaseOrder13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extendedPO2_PurchaseOrder13"):
                    opp_val = getattr(item, "extendedPO2_PurchaseOrder13", None)
                    
                    setattr(item, "extendedPO2_PurchaseOrder13", self)
                    

    @property
    def extendedPO2_Supplier20(self):
        return self.__extendedPO2_Supplier20

    @extendedPO2_Supplier20.setter
    def extendedPO2_Supplier20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_Supplier__extendedPO2_Supplier20", None)
        self.__extendedPO2_Supplier20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extendedPO2_PurchaseOrder21"):
                    opp_val = getattr(item, "extendedPO2_PurchaseOrder21", None)
                    
                    if opp_val == self:
                        setattr(item, "extendedPO2_PurchaseOrder21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extendedPO2_PurchaseOrder21"):
                    opp_val = getattr(item, "extendedPO2_PurchaseOrder21", None)
                    
                    setattr(item, "extendedPO2_PurchaseOrder21", self)
                    

    @property
    def extendedPO2_Supplier17(self):
        return self.__extendedPO2_Supplier17

    @extendedPO2_Supplier17.setter
    def extendedPO2_Supplier17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_Supplier__extendedPO2_Supplier17", None)
        self.__extendedPO2_Supplier17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extendedPO2_PurchaseOrder18"):
                    opp_val = getattr(item, "extendedPO2_PurchaseOrder18", None)
                    
                    if opp_val == self:
                        setattr(item, "extendedPO2_PurchaseOrder18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extendedPO2_PurchaseOrder18"):
                    opp_val = getattr(item, "extendedPO2_PurchaseOrder18", None)
                    
                    setattr(item, "extendedPO2_PurchaseOrder18", self)
                    

class extendedPO2_PurchaseOrder:

    def __init__(self, totalAmount: int, comment: str, orderDate: str, status: str, order: set["extendedPO2_Item"] = None, extendedPO2_PurchaseOrder: "extendedPO2_Address" = None, extendedPO2_PurchaseOrder3: "extendedPO2_Address" = None, extendedPO2_PurchaseOrder7: "extendedPO2_PurchaseOrder" = None, extendedPO2_PurchaseOrder5: "extendedPO2_PurchaseOrder" = None, orders: "extendedPO2_Customer" = None, PurchaseOrder: "extendedPO2_Item" = None, extendedPO2_PurchaseOrder13: "extendedPO2_Supplier" = None, extendedPO2_PurchaseOrder18: "extendedPO2_Supplier" = None, extendedPO2_PurchaseOrder21: "extendedPO2_Supplier" = None, PurchaseOrder11: "extendedPO2_Customer" = None):
        self.totalAmount = totalAmount
        self.comment = comment
        self.orderDate = orderDate
        self.status = status
        self.order = order if order is not None else set()
        self.extendedPO2_PurchaseOrder = extendedPO2_PurchaseOrder
        self.extendedPO2_PurchaseOrder3 = extendedPO2_PurchaseOrder3
        self.extendedPO2_PurchaseOrder7 = extendedPO2_PurchaseOrder7
        self.extendedPO2_PurchaseOrder5 = extendedPO2_PurchaseOrder5
        self.orders = orders
        self.PurchaseOrder = PurchaseOrder
        self.extendedPO2_PurchaseOrder13 = extendedPO2_PurchaseOrder13
        self.extendedPO2_PurchaseOrder18 = extendedPO2_PurchaseOrder18
        self.extendedPO2_PurchaseOrder21 = extendedPO2_PurchaseOrder21
        self.PurchaseOrder11 = PurchaseOrder11
        
    @property
    def orderDate(self) -> str:
        return self.__orderDate

    @orderDate.setter
    def orderDate(self, orderDate: str):
        self.__orderDate = orderDate

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
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_PurchaseOrder__order", None)
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
    def extendedPO2_PurchaseOrder(self):
        return self.__extendedPO2_PurchaseOrder

    @extendedPO2_PurchaseOrder.setter
    def extendedPO2_PurchaseOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_PurchaseOrder__extendedPO2_PurchaseOrder", None)
        self.__extendedPO2_PurchaseOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPO2_Address"):
                opp_val = getattr(old_value, "extendedPO2_Address", None)
                if opp_val == self:
                    setattr(old_value, "extendedPO2_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPO2_Address"):
                opp_val = getattr(value, "extendedPO2_Address", None)
                setattr(value, "extendedPO2_Address", self)

    @property
    def extendedPO2_PurchaseOrder18(self):
        return self.__extendedPO2_PurchaseOrder18

    @extendedPO2_PurchaseOrder18.setter
    def extendedPO2_PurchaseOrder18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_PurchaseOrder__extendedPO2_PurchaseOrder18", None)
        self.__extendedPO2_PurchaseOrder18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPO2_Supplier17"):
                opp_val = getattr(old_value, "extendedPO2_Supplier17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPO2_Supplier17"):
                opp_val = getattr(value, "extendedPO2_Supplier17", None)
                if opp_val is None:
                    setattr(value, "extendedPO2_Supplier17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def extendedPO2_PurchaseOrder3(self):
        return self.__extendedPO2_PurchaseOrder3

    @extendedPO2_PurchaseOrder3.setter
    def extendedPO2_PurchaseOrder3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_PurchaseOrder__extendedPO2_PurchaseOrder3", None)
        self.__extendedPO2_PurchaseOrder3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPO2_Address4"):
                opp_val = getattr(old_value, "extendedPO2_Address4", None)
                if opp_val == self:
                    setattr(old_value, "extendedPO2_Address4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPO2_Address4"):
                opp_val = getattr(value, "extendedPO2_Address4", None)
                setattr(value, "extendedPO2_Address4", self)

    @property
    def PurchaseOrder11(self):
        return self.__PurchaseOrder11

    @PurchaseOrder11.setter
    def PurchaseOrder11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_PurchaseOrder__PurchaseOrder11", None)
        self.__PurchaseOrder11 = value
        
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
    def PurchaseOrder(self):
        return self.__PurchaseOrder

    @PurchaseOrder.setter
    def PurchaseOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_PurchaseOrder__PurchaseOrder", None)
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
    def orders(self):
        return self.__orders

    @orders.setter
    def orders(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_PurchaseOrder__orders", None)
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
    def extendedPO2_PurchaseOrder7(self):
        return self.__extendedPO2_PurchaseOrder7

    @extendedPO2_PurchaseOrder7.setter
    def extendedPO2_PurchaseOrder7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_PurchaseOrder__extendedPO2_PurchaseOrder7", None)
        self.__extendedPO2_PurchaseOrder7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPO2_PurchaseOrder5"):
                opp_val = getattr(old_value, "extendedPO2_PurchaseOrder5", None)
                if opp_val == self:
                    setattr(old_value, "extendedPO2_PurchaseOrder5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPO2_PurchaseOrder5"):
                opp_val = getattr(value, "extendedPO2_PurchaseOrder5", None)
                setattr(value, "extendedPO2_PurchaseOrder5", self)

    @property
    def extendedPO2_PurchaseOrder21(self):
        return self.__extendedPO2_PurchaseOrder21

    @extendedPO2_PurchaseOrder21.setter
    def extendedPO2_PurchaseOrder21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_PurchaseOrder__extendedPO2_PurchaseOrder21", None)
        self.__extendedPO2_PurchaseOrder21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPO2_Supplier20"):
                opp_val = getattr(old_value, "extendedPO2_Supplier20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPO2_Supplier20"):
                opp_val = getattr(value, "extendedPO2_Supplier20", None)
                if opp_val is None:
                    setattr(value, "extendedPO2_Supplier20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def extendedPO2_PurchaseOrder13(self):
        return self.__extendedPO2_PurchaseOrder13

    @extendedPO2_PurchaseOrder13.setter
    def extendedPO2_PurchaseOrder13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_PurchaseOrder__extendedPO2_PurchaseOrder13", None)
        self.__extendedPO2_PurchaseOrder13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPO2_Supplier"):
                opp_val = getattr(old_value, "extendedPO2_Supplier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPO2_Supplier"):
                opp_val = getattr(value, "extendedPO2_Supplier", None)
                if opp_val is None:
                    setattr(value, "extendedPO2_Supplier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def extendedPO2_PurchaseOrder5(self):
        return self.__extendedPO2_PurchaseOrder5

    @extendedPO2_PurchaseOrder5.setter
    def extendedPO2_PurchaseOrder5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_PurchaseOrder__extendedPO2_PurchaseOrder5", None)
        self.__extendedPO2_PurchaseOrder5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPO2_PurchaseOrder7"):
                opp_val = getattr(old_value, "extendedPO2_PurchaseOrder7", None)
                if opp_val == self:
                    setattr(old_value, "extendedPO2_PurchaseOrder7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPO2_PurchaseOrder7"):
                opp_val = getattr(value, "extendedPO2_PurchaseOrder7", None)
                setattr(value, "extendedPO2_PurchaseOrder7", self)

class Address:

    pass
class extendedPO2_GlobalAddress(Address):

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class extendedPO2_USAddress(Address):

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

class extendedPO2_Customer:

    def __init__(self, customerID: int, Customer: "extendedPO2_PurchaseOrder" = None, extendedPO2_Customer: "extendedPO2_Supplier" = None, customer: set["extendedPO2_PurchaseOrder"] = None):
        self.customerID = customerID
        self.Customer = Customer
        self.extendedPO2_Customer = extendedPO2_Customer
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
        old_value = getattr(self, f"_extendedPO2_Customer__Customer", None)
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
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_Customer__customer", None)
        self.__customer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PurchaseOrder11"):
                    opp_val = getattr(item, "PurchaseOrder11", None)
                    
                    if opp_val == self:
                        setattr(item, "PurchaseOrder11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PurchaseOrder11"):
                    opp_val = getattr(item, "PurchaseOrder11", None)
                    
                    setattr(item, "PurchaseOrder11", self)
                    

    @property
    def extendedPO2_Customer(self):
        return self.__extendedPO2_Customer

    @extendedPO2_Customer.setter
    def extendedPO2_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_Customer__extendedPO2_Customer", None)
        self.__extendedPO2_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPO2_Supplier15"):
                opp_val = getattr(old_value, "extendedPO2_Supplier15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPO2_Supplier15"):
                opp_val = getattr(value, "extendedPO2_Supplier15", None)
                if opp_val is None:
                    setattr(value, "extendedPO2_Supplier15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class extendedPO2_Address(ABC):

    def __init__(self, name: str, country: str, extendedPO2_Address: "extendedPO2_PurchaseOrder" = None, extendedPO2_Address4: "extendedPO2_PurchaseOrder" = None):
        self.name = name
        self.country = country
        self.extendedPO2_Address = extendedPO2_Address
        self.extendedPO2_Address4 = extendedPO2_Address4
        
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
    def extendedPO2_Address4(self):
        return self.__extendedPO2_Address4

    @extendedPO2_Address4.setter
    def extendedPO2_Address4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_Address__extendedPO2_Address4", None)
        self.__extendedPO2_Address4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPO2_PurchaseOrder3"):
                opp_val = getattr(old_value, "extendedPO2_PurchaseOrder3", None)
                if opp_val == self:
                    setattr(old_value, "extendedPO2_PurchaseOrder3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPO2_PurchaseOrder3"):
                opp_val = getattr(value, "extendedPO2_PurchaseOrder3", None)
                setattr(value, "extendedPO2_PurchaseOrder3", self)

    @property
    def extendedPO2_Address(self):
        return self.__extendedPO2_Address

    @extendedPO2_Address.setter
    def extendedPO2_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_Address__extendedPO2_Address", None)
        self.__extendedPO2_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPO2_PurchaseOrder"):
                opp_val = getattr(old_value, "extendedPO2_PurchaseOrder", None)
                if opp_val == self:
                    setattr(old_value, "extendedPO2_PurchaseOrder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPO2_PurchaseOrder"):
                opp_val = getattr(value, "extendedPO2_PurchaseOrder", None)
                setattr(value, "extendedPO2_PurchaseOrder", self)

class extendedPO2_Item:

    def __init__(self, productName: str, quantity: int, USPrice: int, comment: str, shipDate: str, partNum: str, Item: "extendedPO2_PurchaseOrder" = None, items: "extendedPO2_PurchaseOrder" = None):
        self.productName = productName
        self.quantity = quantity
        self.USPrice = USPrice
        self.comment = comment
        self.shipDate = shipDate
        self.partNum = partNum
        self.Item = Item
        self.items = items
        
    @property
    def partNum(self) -> str:
        return self.__partNum

    @partNum.setter
    def partNum(self, partNum: str):
        self.__partNum = partNum

    @property
    def USPrice(self) -> int:
        return self.__USPrice

    @USPrice.setter
    def USPrice(self, USPrice: int):
        self.__USPrice = USPrice

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def shipDate(self) -> str:
        return self.__shipDate

    @shipDate.setter
    def shipDate(self, shipDate: str):
        self.__shipDate = shipDate

    @property
    def productName(self) -> str:
        return self.__productName

    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPO2_Item__items", None)
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
        old_value = getattr(self, f"_extendedPO2_Item__Item", None)
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
