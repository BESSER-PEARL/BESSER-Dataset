from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VAT(Enum):
    vat0 = "vat0"
    vat7 = "vat7"
    vat15 = "vat15"


############################################
# Definition of Classes
############################################

class OrderDetail:

    pass
class Order:

    pass
class model1_SalesOrder(Order):

    def __init__(self, id: int, SalesOrder: "model1_Customer" = None, salesOrders: "model1_Customer" = None, model1_SalesOrder: "model1_Company" = None, model1_SalesOrder31: "model1_ProductToOrder" = None):
        self.id = id
        self.SalesOrder = SalesOrder
        self.salesOrders = salesOrders
        self.model1_SalesOrder = model1_SalesOrder
        self.model1_SalesOrder31 = model1_SalesOrder31
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def SalesOrder(self):
        return self.__SalesOrder

    @SalesOrder.setter
    def SalesOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_SalesOrder__SalesOrder", None)
        self.__SalesOrder = value
        
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
    def model1_SalesOrder31(self):
        return self.__model1_SalesOrder31

    @model1_SalesOrder31.setter
    def model1_SalesOrder31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_SalesOrder__model1_SalesOrder31", None)
        self.__model1_SalesOrder31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model1_ProductToOrder30"):
                opp_val = getattr(old_value, "model1_ProductToOrder30", None)
                if opp_val == self:
                    setattr(old_value, "model1_ProductToOrder30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model1_ProductToOrder30"):
                opp_val = getattr(value, "model1_ProductToOrder30", None)
                setattr(value, "model1_ProductToOrder30", self)

    @property
    def salesOrders(self):
        return self.__salesOrders

    @salesOrders.setter
    def salesOrders(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_SalesOrder__salesOrders", None)
        self.__salesOrders = value
        
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
    def model1_SalesOrder(self):
        return self.__model1_SalesOrder

    @model1_SalesOrder.setter
    def model1_SalesOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_SalesOrder__model1_SalesOrder", None)
        self.__model1_SalesOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model1_Company8"):
                opp_val = getattr(old_value, "model1_Company8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model1_Company8"):
                opp_val = getattr(value, "model1_Company8", None)
                if opp_val is None:
                    setattr(value, "model1_Company8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model1_Product1:

    def __init__(self, name: str, description: str, vat: str, Product1: "model1_OrderDetail" = None, model1_Product1: "model1_Category" = None, model1_Product128: "model1_ProductToOrder" = None, product: set["model1_OrderDetail"] = None):
        self.name = name
        self.description = description
        self.vat = vat
        self.Product1 = Product1
        self.model1_Product1 = model1_Product1
        self.model1_Product128 = model1_Product128
        self.product = product if product is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def vat(self) -> str:
        return self.__vat

    @vat.setter
    def vat(self, vat: str):
        self.__vat = vat

    @property
    def Product1(self):
        return self.__Product1

    @Product1.setter
    def Product1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_Product1__Product1", None)
        self.__Product1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderDetails16"):
                opp_val = getattr(old_value, "orderDetails16", None)
                if opp_val == self:
                    setattr(old_value, "orderDetails16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderDetails16"):
                opp_val = getattr(value, "orderDetails16", None)
                setattr(value, "orderDetails16", self)

    @property
    def model1_Product1(self):
        return self.__model1_Product1

    @model1_Product1.setter
    def model1_Product1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_Product1__model1_Product1", None)
        self.__model1_Product1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model1_Category23"):
                opp_val = getattr(old_value, "model1_Category23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model1_Category23"):
                opp_val = getattr(value, "model1_Category23", None)
                if opp_val is None:
                    setattr(value, "model1_Category23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_Product1__product", None)
        self.__product = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OrderDetail25"):
                    opp_val = getattr(item, "OrderDetail25", None)
                    
                    if opp_val == self:
                        setattr(item, "OrderDetail25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OrderDetail25"):
                    opp_val = getattr(item, "OrderDetail25", None)
                    
                    setattr(item, "OrderDetail25", self)
                    

    @property
    def model1_Product128(self):
        return self.__model1_Product128

    @model1_Product128.setter
    def model1_Product128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_Product1__model1_Product128", None)
        self.__model1_Product128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model1_ProductToOrder27"):
                opp_val = getattr(old_value, "model1_ProductToOrder27", None)
                if opp_val == self:
                    setattr(old_value, "model1_ProductToOrder27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model1_ProductToOrder27"):
                opp_val = getattr(value, "model1_ProductToOrder27", None)
                setattr(value, "model1_ProductToOrder27", self)

class model1_OrderDetail:

    def __init__(self, price: float, OrderDetail: "model1_Order" = None, orderDetails: "model1_Order" = None, orderDetails16: "model1_Product1" = None, OrderDetail25: "model1_Product1" = None):
        self.price = price
        self.OrderDetail = OrderDetail
        self.orderDetails = orderDetails
        self.orderDetails16 = orderDetails16
        self.OrderDetail25 = OrderDetail25
        
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def OrderDetail(self):
        return self.__OrderDetail

    @OrderDetail.setter
    def OrderDetail(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_OrderDetail__OrderDetail", None)
        self.__OrderDetail = value
        
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

    @property
    def OrderDetail25(self):
        return self.__OrderDetail25

    @OrderDetail25.setter
    def OrderDetail25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_OrderDetail__OrderDetail25", None)
        self.__OrderDetail25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product"):
                opp_val = getattr(old_value, "product", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product"):
                opp_val = getattr(value, "product", None)
                if opp_val is None:
                    setattr(value, "product", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def orderDetails(self):
        return self.__orderDetails

    @orderDetails.setter
    def orderDetails(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_OrderDetail__orderDetails", None)
        self.__orderDetails = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order"):
                opp_val = getattr(old_value, "Order", None)
                if opp_val == self:
                    setattr(old_value, "Order", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order"):
                opp_val = getattr(value, "Order", None)
                setattr(value, "Order", self)

    @property
    def orderDetails16(self):
        return self.__orderDetails16

    @orderDetails16.setter
    def orderDetails16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_OrderDetail__orderDetails16", None)
        self.__orderDetails16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Product1"):
                opp_val = getattr(old_value, "Product1", None)
                if opp_val == self:
                    setattr(old_value, "Product1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Product1"):
                opp_val = getattr(value, "Product1", None)
                setattr(value, "Product1", self)

class model1_Order(ABC):

    pass
class model1_ProductToOrder:

    pass
class model1_PurchaseOrder(Order):

    def __init__(self, date: date, model1_PurchaseOrder: "model1_Company" = None, PurchaseOrder: "model1_Supplier" = None, purchaseOrders: "model1_Supplier" = None):
        self.date = date
        self.model1_PurchaseOrder = model1_PurchaseOrder
        self.PurchaseOrder = PurchaseOrder
        self.purchaseOrders = purchaseOrders
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def PurchaseOrder(self):
        return self.__PurchaseOrder

    @PurchaseOrder.setter
    def PurchaseOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_PurchaseOrder__PurchaseOrder", None)
        self.__PurchaseOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "supplier"):
                opp_val = getattr(old_value, "supplier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "supplier"):
                opp_val = getattr(value, "supplier", None)
                if opp_val is None:
                    setattr(value, "supplier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def purchaseOrders(self):
        return self.__purchaseOrders

    @purchaseOrders.setter
    def purchaseOrders(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_PurchaseOrder__purchaseOrders", None)
        self.__purchaseOrders = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Supplier"):
                opp_val = getattr(old_value, "Supplier", None)
                if opp_val == self:
                    setattr(old_value, "Supplier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Supplier"):
                opp_val = getattr(value, "Supplier", None)
                setattr(value, "Supplier", self)

    @property
    def model1_PurchaseOrder(self):
        return self.__model1_PurchaseOrder

    @model1_PurchaseOrder.setter
    def model1_PurchaseOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_PurchaseOrder__model1_PurchaseOrder", None)
        self.__model1_PurchaseOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model1_Company6"):
                opp_val = getattr(old_value, "model1_Company6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model1_Company6"):
                opp_val = getattr(value, "model1_Company6", None)
                if opp_val is None:
                    setattr(value, "model1_Company6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model1_Category:

    def __init__(self, name: str, model1_Category: "model1_Company" = None, model1_Category21: "model1_Category" = None, model1_Category19: set["model1_Category"] = None, model1_Category23: set["model1_Product1"] = None):
        self.name = name
        self.model1_Category = model1_Category
        self.model1_Category21 = model1_Category21
        self.model1_Category19 = model1_Category19 if model1_Category19 is not None else set()
        self.model1_Category23 = model1_Category23 if model1_Category23 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model1_Category21(self):
        return self.__model1_Category21

    @model1_Category21.setter
    def model1_Category21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_Category__model1_Category21", None)
        self.__model1_Category21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model1_Category19"):
                opp_val = getattr(old_value, "model1_Category19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model1_Category19"):
                opp_val = getattr(value, "model1_Category19", None)
                if opp_val is None:
                    setattr(value, "model1_Category19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model1_Category(self):
        return self.__model1_Category

    @model1_Category.setter
    def model1_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_Category__model1_Category", None)
        self.__model1_Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model1_Company"):
                opp_val = getattr(old_value, "model1_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model1_Company"):
                opp_val = getattr(value, "model1_Company", None)
                if opp_val is None:
                    setattr(value, "model1_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model1_Category19(self):
        return self.__model1_Category19

    @model1_Category19.setter
    def model1_Category19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_Category__model1_Category19", None)
        self.__model1_Category19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model1_Category21"):
                    opp_val = getattr(item, "model1_Category21", None)
                    
                    if opp_val == self:
                        setattr(item, "model1_Category21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model1_Category21"):
                    opp_val = getattr(item, "model1_Category21", None)
                    
                    setattr(item, "model1_Category21", self)
                    

    @property
    def model1_Category23(self):
        return self.__model1_Category23

    @model1_Category23.setter
    def model1_Category23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_Category__model1_Category23", None)
        self.__model1_Category23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model1_Product1"):
                    opp_val = getattr(item, "model1_Product1", None)
                    
                    if opp_val == self:
                        setattr(item, "model1_Product1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model1_Product1"):
                    opp_val = getattr(item, "model1_Product1", None)
                    
                    setattr(item, "model1_Product1", self)
                    

class Address:

    pass
class model1_Supplier(Address):

    def __init__(self, preferred: bool, model1_Supplier: "model1_Company" = None, supplier: set["model1_PurchaseOrder"] = None, Supplier: "model1_PurchaseOrder" = None):
        self.preferred = preferred
        self.model1_Supplier = model1_Supplier
        self.supplier = supplier if supplier is not None else set()
        self.Supplier = Supplier
        
    @property
    def preferred(self) -> bool:
        return self.__preferred

    @preferred.setter
    def preferred(self, preferred: bool):
        self.__preferred = preferred

    @property
    def model1_Supplier(self):
        return self.__model1_Supplier

    @model1_Supplier.setter
    def model1_Supplier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_Supplier__model1_Supplier", None)
        self.__model1_Supplier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model1_Company2"):
                opp_val = getattr(old_value, "model1_Company2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model1_Company2"):
                opp_val = getattr(value, "model1_Company2", None)
                if opp_val is None:
                    setattr(value, "model1_Company2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Supplier(self):
        return self.__Supplier

    @Supplier.setter
    def Supplier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_Supplier__Supplier", None)
        self.__Supplier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "purchaseOrders"):
                opp_val = getattr(old_value, "purchaseOrders", None)
                if opp_val == self:
                    setattr(old_value, "purchaseOrders", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "purchaseOrders"):
                opp_val = getattr(value, "purchaseOrders", None)
                setattr(value, "purchaseOrders", self)

    @property
    def supplier(self):
        return self.__supplier

    @supplier.setter
    def supplier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_Supplier__supplier", None)
        self.__supplier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PurchaseOrder"):
                    opp_val = getattr(item, "PurchaseOrder", None)
                    
                    if opp_val == self:
                        setattr(item, "PurchaseOrder", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PurchaseOrder"):
                    opp_val = getattr(item, "PurchaseOrder", None)
                    
                    setattr(item, "PurchaseOrder", self)
                    

class model1_Customer(Address):

    pass
class model1_OrderAddress(Order, OrderDetail, Address):

    def __init__(self, testAttribute: bool):
        self.testAttribute = testAttribute
        
    @property
    def testAttribute(self) -> bool:
        return self.__testAttribute

    @testAttribute.setter
    def testAttribute(self, testAttribute: bool):
        self.__testAttribute = testAttribute

class model1_Company(Address):

    pass
class model1_Address:

    def __init__(self, name: str, street: str, city: str):
        self.name = name
        self.street = street
        self.city = city
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
