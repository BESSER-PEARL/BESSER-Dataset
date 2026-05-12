from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class real(Enum):
    pass
class OrderStatus(Enum):
    pass

############################################
# Definition of Classes
############################################










class PremiumCustomer:

    def __init__(self, subscriptionExpires: str):
        self.subscriptionExpires = subscriptionExpires
        
        pass
    @property
    def subscriptionExpires(self):
        return self.__subscriptionExpires
    @subscriptionExpires.setter
    def subscriptionExpires(self, subscriptionExpires: str):
        self.__subscriptionExpires = subscriptionExpires



class Product:

    def __init__(self, productId: int, description: str, productName: str, price: float, imageFileName: str, stock: int, orderDetails2: set["OrderDetail"] = None):
        self.productId = productId
        self.description = description
        self.productName = productName
        self.price = price
        self.imageFileName = imageFileName
        self.stock = stock
        self.orderDetails2 = orderDetails2 if orderDetails2 is not None else set()
        
        pass
    @property
    def imageFileName(self):
        return self.__imageFileName
    @imageFileName.setter
    def imageFileName(self, imageFileName: str):
        self.__imageFileName = imageFileName

    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, stock: int):
        self.__stock = stock

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: int):
        self.__productId = productId

    @property
    def productName(self):
        return self.__productName
    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def orderDetails2(self):
        return self.__orderDetails2
    @orderDetails2.setter
    def orderDetails2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__orderDetails2", None)
        self.__orderDetails2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product3"):
                    opp_val = getattr(item, "product3", None)
                    
                    if opp_val == self:
                        setattr(item, "product3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product3"):
                    opp_val = getattr(item, "product3", None)
                    
                    setattr(item, "product3", self)
                    



class OrderDetail:

    def __init__(self, ordrId: int, productId: int, productName: str, quantity: int, unitCost: float, subtotal: float, order1: "Order" = None, product3: "Product" = None):
        self.ordrId = ordrId
        self.productId = productId
        self.productName = productName
        self.quantity = quantity
        self.unitCost = unitCost
        self.subtotal = subtotal
        self.order1 = order1
        self.product3 = product3
        
        pass
    @property
    def subtotal(self):
        return self.__subtotal
    @subtotal.setter
    def subtotal(self, subtotal: float):
        self.__subtotal = subtotal

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: int):
        self.__productId = productId

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def productName(self):
        return self.__productName
    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def ordrId(self):
        return self.__ordrId
    @ordrId.setter
    def ordrId(self, ordrId: int):
        self.__ordrId = ordrId

    @property
    def unitCost(self):
        return self.__unitCost
    @unitCost.setter
    def unitCost(self, unitCost: float):
        self.__unitCost = unitCost

    @property
    def order1(self):
        return self.__order1
    @order1.setter
    def order1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderDetail__order1", None)
        self.__order1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderDetails0"):
                opp_val = getattr(old_value, "orderDetails0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderDetails0"):
                opp_val = getattr(value, "orderDetails0", None)
                if opp_val is None:
                    setattr(value, "orderDetails0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product3(self):
        return self.__product3
    @product3.setter
    def product3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderDetail__product3", None)
        self.__product3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderDetails2"):
                opp_val = getattr(old_value, "orderDetails2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderDetails2"):
                opp_val = getattr(value, "orderDetails2", None)
                if opp_val is None:
                    setattr(value, "orderDetails2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order:

    def __init__(self, orderId: int, creationDate: str, dateShipped: str, customerId: int, status: OrderStatus, shippingId: int, totalPrice: float, orderDetails0: set["OrderDetail"] = None, customer5: "Customer" = None):
        self.orderId = orderId
        self.creationDate = creationDate
        self.dateShipped = dateShipped
        self.customerId = customerId
        self.status = status
        self.shippingId = shippingId
        self.totalPrice = totalPrice
        self.orderDetails0 = orderDetails0 if orderDetails0 is not None else set()
        self.customer5 = customer5
        
        pass
    @property
    def orderId(self):
        return self.__orderId
    @orderId.setter
    def orderId(self, orderId: int):
        self.__orderId = orderId

    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: str):
        self.__creationDate = creationDate

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: OrderStatus):
        self.__status = status

    @property
    def shippingId(self):
        return self.__shippingId
    @shippingId.setter
    def shippingId(self, shippingId: int):
        self.__shippingId = shippingId

    @property
    def customerId(self):
        return self.__customerId
    @customerId.setter
    def customerId(self, customerId: int):
        self.__customerId = customerId

    @property
    def dateShipped(self):
        return self.__dateShipped
    @dateShipped.setter
    def dateShipped(self, dateShipped: str):
        self.__dateShipped = dateShipped

    @property
    def totalPrice(self):
        return self.__totalPrice
    @totalPrice.setter
    def totalPrice(self, totalPrice: float):
        self.__totalPrice = totalPrice

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer5", None)
        self.__customer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders4"):
                opp_val = getattr(old_value, "orders4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders4"):
                opp_val = getattr(value, "orders4", None)
                if opp_val is None:
                    setattr(value, "orders4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def orderDetails0(self):
        return self.__orderDetails0
    @orderDetails0.setter
    def orderDetails0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orderDetails0", None)
        self.__orderDetails0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order1"):
                    opp_val = getattr(item, "order1", None)
                    
                    if opp_val == self:
                        setattr(item, "order1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order1"):
                    opp_val = getattr(item, "order1", None)
                    
                    setattr(item, "order1", self)
                    



class Customer:

    def __init__(self, name: str, address: str, email: str, phone: int, creditCardInfo: str, shippingInfo: str, orders4: set["Order"] = None, portal6: "Portal" = None):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.creditCardInfo = creditCardInfo
        self.shippingInfo = shippingInfo
        self.orders4 = orders4 if orders4 is not None else set()
        self.portal6 = portal6
        
        pass
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: int):
        self.__phone = phone

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def creditCardInfo(self):
        return self.__creditCardInfo
    @creditCardInfo.setter
    def creditCardInfo(self, creditCardInfo: str):
        self.__creditCardInfo = creditCardInfo

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def shippingInfo(self):
        return self.__shippingInfo
    @shippingInfo.setter
    def shippingInfo(self, shippingInfo: str):
        self.__shippingInfo = shippingInfo

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def portal6(self):
        return self.__portal6
    @portal6.setter
    def portal6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__portal6", None)
        self.__portal6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "users7"):
                opp_val = getattr(old_value, "users7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "users7"):
                opp_val = getattr(value, "users7", None)
                if opp_val is None:
                    setattr(value, "users7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def orders4(self):
        return self.__orders4
    @orders4.setter
    def orders4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__orders4", None)
        self.__orders4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer5"):
                    opp_val = getattr(item, "customer5", None)
                    
                    if opp_val == self:
                        setattr(item, "customer5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer5"):
                    opp_val = getattr(item, "customer5", None)
                    
                    setattr(item, "customer5", self)
                    



class Portal:

    def __init__(self, portalId: str, name: str, url: str, users7: set["Customer"] = None):
        self.portalId = portalId
        self.name = name
        self.url = url
        self.users7 = users7 if users7 is not None else set()
        
        pass
    @property
    def portalId(self):
        return self.__portalId
    @portalId.setter
    def portalId(self, portalId: str):
        self.__portalId = portalId

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def url(self):
        return self.__url
    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def users7(self):
        return self.__users7
    @users7.setter
    def users7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Portal__users7", None)
        self.__users7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "portal6"):
                    opp_val = getattr(item, "portal6", None)
                    
                    if opp_val == self:
                        setattr(item, "portal6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "portal6"):
                    opp_val = getattr(item, "portal6", None)
                    
                    setattr(item, "portal6", self)
                    

