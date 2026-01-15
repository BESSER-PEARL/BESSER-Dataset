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
class model1_OrderDetail:

    def __init__(self, price: float, orderDetails: "model1_Order" = None, orderDetails16: "model1_Product1" = None, OrderDetail: "model1_Order" = None, OrderDetail31: "model1_Product1" = None):
        self.price = price
        self.orderDetails = orderDetails
        self.orderDetails16 = orderDetails16
        self.OrderDetail = OrderDetail
        self.OrderDetail31 = OrderDetail31
        
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

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
    def OrderDetail31(self):
        return self.__OrderDetail31

    @OrderDetail31.setter
    def OrderDetail31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_OrderDetail__OrderDetail31", None)
        self.__OrderDetail31 = value
        
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

class model1_Order(ABC):

    pass
class model1_ProductToOrder:

    pass
class model1_SalesOrder(Order):

    def __init__(self, id: int, model1_SalesOrder: "model1_Company" = None, SalesOrder: "model1_Customer" = None, SalesOrder20: "model1_PurchaseOrder" = None, salesOrders: "model1_Customer" = None, salesOrders23: set["model1_PurchaseOrder"] = None, model1_SalesOrder37: "model1_ProductToOrder" = None):
        self.id = id
        self.model1_SalesOrder = model1_SalesOrder
        self.SalesOrder = SalesOrder
        self.SalesOrder20 = SalesOrder20
        self.salesOrders = salesOrders
        self.salesOrders23 = salesOrders23 if salesOrders23 is not None else set()
        self.model1_SalesOrder37 = model1_SalesOrder37
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def model1_SalesOrder37(self):
        return self.__model1_SalesOrder37

    @model1_SalesOrder37.setter
    def model1_SalesOrder37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_SalesOrder__model1_SalesOrder37", None)
        self.__model1_SalesOrder37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model1_ProductToOrder36"):
                opp_val = getattr(old_value, "model1_ProductToOrder36", None)
                if opp_val == self:
                    setattr(old_value, "model1_ProductToOrder36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model1_ProductToOrder36"):
                opp_val = getattr(value, "model1_ProductToOrder36", None)
                setattr(value, "model1_ProductToOrder36", self)

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
    def salesOrders23(self):
        return self.__salesOrders23

    @salesOrders23.setter
    def salesOrders23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_SalesOrder__salesOrders23", None)
        self.__salesOrders23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PurchaseOrder24"):
                    opp_val = getattr(item, "PurchaseOrder24", None)
                    
                    if opp_val == self:
                        setattr(item, "PurchaseOrder24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PurchaseOrder24"):
                    opp_val = getattr(item, "PurchaseOrder24", None)
                    
                    setattr(item, "PurchaseOrder24", self)
                    

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
    def SalesOrder20(self):
        return self.__SalesOrder20

    @SalesOrder20.setter
    def SalesOrder20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_SalesOrder__SalesOrder20", None)
        self.__SalesOrder20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "purchaseOrders19"):
                opp_val = getattr(old_value, "purchaseOrders19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "purchaseOrders19"):
                opp_val = getattr(value, "purchaseOrders19", None)
                if opp_val is None:
                    setattr(value, "purchaseOrders19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class model1_PurchaseOrder(Order):

    def __init__(self, date: date, model1_PurchaseOrder: "model1_Company" = None, PurchaseOrder: "model1_Supplier" = None, purchaseOrders: "model1_Supplier" = None, purchaseOrders19: set["model1_SalesOrder"] = None, PurchaseOrder24: "model1_SalesOrder" = None):
        self.date = date
        self.model1_PurchaseOrder = model1_PurchaseOrder
        self.PurchaseOrder = PurchaseOrder
        self.purchaseOrders = purchaseOrders
        self.purchaseOrders19 = purchaseOrders19 if purchaseOrders19 is not None else set()
        self.PurchaseOrder24 = PurchaseOrder24
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def PurchaseOrder24(self):
        return self.__PurchaseOrder24

    @PurchaseOrder24.setter
    def PurchaseOrder24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_PurchaseOrder__PurchaseOrder24", None)
        self.__PurchaseOrder24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "salesOrders23"):
                opp_val = getattr(old_value, "salesOrders23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "salesOrders23"):
                opp_val = getattr(value, "salesOrders23", None)
                if opp_val is None:
                    setattr(value, "salesOrders23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def purchaseOrders19(self):
        return self.__purchaseOrders19

    @purchaseOrders19.setter
    def purchaseOrders19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_PurchaseOrder__purchaseOrders19", None)
        self.__purchaseOrders19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SalesOrder20"):
                    opp_val = getattr(item, "SalesOrder20", None)
                    
                    if opp_val == self:
                        setattr(item, "SalesOrder20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SalesOrder20"):
                    opp_val = getattr(item, "SalesOrder20", None)
                    
                    setattr(item, "SalesOrder20", self)
                    

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

class model1_Category:

    def __init__(self, name: str, model1_Category: "model1_Company" = None, model1_Category27: "model1_Category" = None, model1_Category25: set["model1_Category"] = None, model1_Category29: set["model1_Product1"] = None):
        self.name = name
        self.model1_Category = model1_Category
        self.model1_Category27 = model1_Category27
        self.model1_Category25 = model1_Category25 if model1_Category25 is not None else set()
        self.model1_Category29 = model1_Category29 if model1_Category29 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model1_Category27(self):
        return self.__model1_Category27

    @model1_Category27.setter
    def model1_Category27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_Category__model1_Category27", None)
        self.__model1_Category27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model1_Category25"):
                opp_val = getattr(old_value, "model1_Category25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model1_Category25"):
                opp_val = getattr(value, "model1_Category25", None)
                if opp_val is None:
                    setattr(value, "model1_Category25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model1_Category29(self):
        return self.__model1_Category29

    @model1_Category29.setter
    def model1_Category29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_Category__model1_Category29", None)
        self.__model1_Category29 = value if value is not None else set()
        
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
    def model1_Category25(self):
        return self.__model1_Category25

    @model1_Category25.setter
    def model1_Category25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_Category__model1_Category25", None)
        self.__model1_Category25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model1_Category27"):
                    opp_val = getattr(item, "model1_Category27", None)
                    
                    if opp_val == self:
                        setattr(item, "model1_Category27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model1_Category27"):
                    opp_val = getattr(item, "model1_Category27", None)
                    
                    setattr(item, "model1_Category27", self)
                    

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
                    

class model1_OrderAddress(Order, Address, OrderDetail):

    def __init__(self, testAttribute: bool):
        self.testAttribute = testAttribute
        
    @property
    def testAttribute(self) -> bool:
        return self.__testAttribute

    @testAttribute.setter
    def testAttribute(self, testAttribute: bool):
        self.__testAttribute = testAttribute

class model1_Customer(Address):

    pass
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

class model1_Product1:

    def __init__(self, name: str, vat: str, otherVATs: str, description: str, Product1: "model1_OrderDetail" = None, model1_Product134: "model1_ProductToOrder" = None, model1_Product1: "model1_Category" = None, product: set["model1_OrderDetail"] = None):
        self.name = name
        self.vat = vat
        self.otherVATs = otherVATs
        self.description = description
        self.Product1 = Product1
        self.model1_Product134 = model1_Product134
        self.model1_Product1 = model1_Product1
        self.product = product if product is not None else set()
        
    @property
    def vat(self) -> str:
        return self.__vat

    @vat.setter
    def vat(self, vat: str):
        self.__vat = vat

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def otherVATs(self) -> str:
        return self.__otherVATs

    @otherVATs.setter
    def otherVATs(self, otherVATs: str):
        self.__otherVATs = otherVATs

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "model1_Category29"):
                opp_val = getattr(old_value, "model1_Category29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model1_Category29"):
                opp_val = getattr(value, "model1_Category29", None)
                if opp_val is None:
                    setattr(value, "model1_Category29", set([self]))
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
                if hasattr(item, "OrderDetail31"):
                    opp_val = getattr(item, "OrderDetail31", None)
                    
                    if opp_val == self:
                        setattr(item, "OrderDetail31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OrderDetail31"):
                    opp_val = getattr(item, "OrderDetail31", None)
                    
                    setattr(item, "OrderDetail31", self)
                    

    @property
    def model1_Product134(self):
        return self.__model1_Product134

    @model1_Product134.setter
    def model1_Product134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model1_Product1__model1_Product134", None)
        self.__model1_Product134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model1_ProductToOrder33"):
                opp_val = getattr(old_value, "model1_ProductToOrder33", None)
                if opp_val == self:
                    setattr(old_value, "model1_ProductToOrder33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model1_ProductToOrder33"):
                opp_val = getattr(value, "model1_ProductToOrder33", None)
                setattr(value, "model1_ProductToOrder33", self)
