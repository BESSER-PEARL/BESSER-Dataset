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

class company_Category:

    def __init__(self, name: str, company_Category19: "company_Category" = None, company_Category17: set["company_Category"] = None, company_Category21: set["company_Product"] = None, company_Category: "company_Company" = None):
        self.name = name
        self.company_Category19 = company_Category19
        self.company_Category17 = company_Category17 if company_Category17 is not None else set()
        self.company_Category21 = company_Category21 if company_Category21 is not None else set()
        self.company_Category = company_Category
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def company_Category(self):
        return self.__company_Category

    @company_Category.setter
    def company_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Category__company_Category", None)
        self.__company_Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Company"):
                opp_val = getattr(old_value, "company_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Company"):
                opp_val = getattr(value, "company_Company", None)
                if opp_val is None:
                    setattr(value, "company_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def company_Category17(self):
        return self.__company_Category17

    @company_Category17.setter
    def company_Category17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Category__company_Category17", None)
        self.__company_Category17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company_Category19"):
                    opp_val = getattr(item, "company_Category19", None)
                    
                    if opp_val == self:
                        setattr(item, "company_Category19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company_Category19"):
                    opp_val = getattr(item, "company_Category19", None)
                    
                    setattr(item, "company_Category19", self)
                    

    @property
    def company_Category19(self):
        return self.__company_Category19

    @company_Category19.setter
    def company_Category19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Category__company_Category19", None)
        self.__company_Category19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Category17"):
                opp_val = getattr(old_value, "company_Category17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Category17"):
                opp_val = getattr(value, "company_Category17", None)
                if opp_val is None:
                    setattr(value, "company_Category17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def company_Category21(self):
        return self.__company_Category21

    @company_Category21.setter
    def company_Category21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Category__company_Category21", None)
        self.__company_Category21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company_Product"):
                    opp_val = getattr(item, "company_Product", None)
                    
                    if opp_val == self:
                        setattr(item, "company_Product", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company_Product"):
                    opp_val = getattr(item, "company_Product", None)
                    
                    setattr(item, "company_Product", self)
                    

class Addressable:

    pass
class company_Supplier(Addressable):

    def __init__(self, preferred: bool, supplier: set["company_PurchaseOrder"] = None, Supplier: "company_PurchaseOrder" = None, company_Supplier: "company_Company" = None):
        self.preferred = preferred
        self.supplier = supplier if supplier is not None else set()
        self.Supplier = Supplier
        self.company_Supplier = company_Supplier
        
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
        old_value = getattr(self, f"_company_Supplier__Supplier", None)
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
        old_value = getattr(self, f"_company_Supplier__supplier", None)
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
                    

    @property
    def company_Supplier(self):
        return self.__company_Supplier

    @company_Supplier.setter
    def company_Supplier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Supplier__company_Supplier", None)
        self.__company_Supplier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Company2"):
                opp_val = getattr(old_value, "company_Company2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Company2"):
                opp_val = getattr(value, "company_Company2", None)
                if opp_val is None:
                    setattr(value, "company_Company2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class company_Customer(Addressable):

    pass
class company_Company(Addressable):

    pass
class Order:

    pass
class company_SalesOrder(Order):

    def __init__(self, id: int, SalesOrder: "company_Customer" = None, salesOrders: "company_Customer" = None, company_SalesOrder: "company_Company" = None):
        self.id = id
        self.SalesOrder = SalesOrder
        self.salesOrders = salesOrders
        self.company_SalesOrder = company_SalesOrder
        
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
        old_value = getattr(self, f"_company_SalesOrder__SalesOrder", None)
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
    def salesOrders(self):
        return self.__salesOrders

    @salesOrders.setter
    def salesOrders(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_SalesOrder__salesOrders", None)
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
    def company_SalesOrder(self):
        return self.__company_SalesOrder

    @company_SalesOrder.setter
    def company_SalesOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_SalesOrder__company_SalesOrder", None)
        self.__company_SalesOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Company8"):
                opp_val = getattr(old_value, "company_Company8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Company8"):
                opp_val = getattr(value, "company_Company8", None)
                if opp_val is None:
                    setattr(value, "company_Company8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class company_PurchaseOrder(Order):

    def __init__(self, date: date, PurchaseOrder: "company_Supplier" = None, purchaseOrders: "company_Supplier" = None, company_PurchaseOrder: "company_Company" = None):
        self.date = date
        self.PurchaseOrder = PurchaseOrder
        self.purchaseOrders = purchaseOrders
        self.company_PurchaseOrder = company_PurchaseOrder
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def purchaseOrders(self):
        return self.__purchaseOrders

    @purchaseOrders.setter
    def purchaseOrders(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_PurchaseOrder__purchaseOrders", None)
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
    def company_PurchaseOrder(self):
        return self.__company_PurchaseOrder

    @company_PurchaseOrder.setter
    def company_PurchaseOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_PurchaseOrder__company_PurchaseOrder", None)
        self.__company_PurchaseOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Company6"):
                opp_val = getattr(old_value, "company_Company6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Company6"):
                opp_val = getattr(value, "company_Company6", None)
                if opp_val is None:
                    setattr(value, "company_Company6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PurchaseOrder(self):
        return self.__PurchaseOrder

    @PurchaseOrder.setter
    def PurchaseOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_PurchaseOrder__PurchaseOrder", None)
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

class company_Product:

    def __init__(self, name: str, vat: str, description: str, price: float, Product: "company_OrderDetail" = None, company_Product: "company_Category" = None, product: set["company_OrderDetail"] = None):
        self.name = name
        self.vat = vat
        self.description = description
        self.price = price
        self.Product = Product
        self.company_Product = company_Product
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Product__product", None)
        self.__product = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OrderDetail23"):
                    opp_val = getattr(item, "OrderDetail23", None)
                    
                    if opp_val == self:
                        setattr(item, "OrderDetail23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OrderDetail23"):
                    opp_val = getattr(item, "OrderDetail23", None)
                    
                    setattr(item, "OrderDetail23", self)
                    

    @property
    def Product(self):
        return self.__Product

    @Product.setter
    def Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Product__Product", None)
        self.__Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderDetails14"):
                opp_val = getattr(old_value, "orderDetails14", None)
                if opp_val == self:
                    setattr(old_value, "orderDetails14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderDetails14"):
                opp_val = getattr(value, "orderDetails14", None)
                setattr(value, "orderDetails14", self)

    @property
    def company_Product(self):
        return self.__company_Product

    @company_Product.setter
    def company_Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Product__company_Product", None)
        self.__company_Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Category21"):
                opp_val = getattr(old_value, "company_Category21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Category21"):
                opp_val = getattr(value, "company_Category21", None)
                if opp_val is None:
                    setattr(value, "company_Category21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class company_OrderDetail:

    def __init__(self, price: float, OrderDetail: "company_Order" = None, orderDetails: "company_Order" = None, orderDetails14: "company_Product" = None, OrderDetail23: "company_Product" = None):
        self.price = price
        self.OrderDetail = OrderDetail
        self.orderDetails = orderDetails
        self.orderDetails14 = orderDetails14
        self.OrderDetail23 = OrderDetail23
        
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
        old_value = getattr(self, f"_company_OrderDetail__OrderDetail", None)
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
    def OrderDetail23(self):
        return self.__OrderDetail23

    @OrderDetail23.setter
    def OrderDetail23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_OrderDetail__OrderDetail23", None)
        self.__OrderDetail23 = value
        
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
        old_value = getattr(self, f"_company_OrderDetail__orderDetails", None)
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
    def orderDetails14(self):
        return self.__orderDetails14

    @orderDetails14.setter
    def orderDetails14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_OrderDetail__orderDetails14", None)
        self.__orderDetails14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Product"):
                opp_val = getattr(old_value, "Product", None)
                if opp_val == self:
                    setattr(old_value, "Product", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Product"):
                opp_val = getattr(value, "Product", None)
                setattr(value, "Product", self)

class company_Order:

    pass
class company_Addressable(ABC):

    def __init__(self, name: str, street: str, city: str):
        self.name = name
        self.street = street
        self.city = city
        
    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

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
