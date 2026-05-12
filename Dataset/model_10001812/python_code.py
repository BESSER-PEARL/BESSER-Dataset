from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class email_Interface:

    pass


class notify_Interface:

    pass


class cartItem:

    def __init__(self, name: str, productId: int, quantity: int, unitCost: str, subtotal: str, cart2: "cartItem" = None, cart3: "cartItem" = None, product21: "Product" = None):
        self.name = name
        self.productId = productId
        self.quantity = quantity
        self.unitCost = unitCost
        self.subtotal = subtotal
        self.cart2 = cart2
        self.cart3 = cart3
        self.product21 = product21
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: int):
        self.__productId = productId

    @property
    def unitCost(self):
        return self.__unitCost
    @unitCost.setter
    def unitCost(self, unitCost: str):
        self.__unitCost = unitCost

    @property
    def subtotal(self):
        return self.__subtotal
    @subtotal.setter
    def subtotal(self, subtotal: str):
        self.__subtotal = subtotal

    @property
    def cart2(self):
        return self.__cart2
    @cart2.setter
    def cart2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cartItem__cart2", None)
        self.__cart2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart3"):
                opp_val = getattr(old_value, "cart3", None)
                if opp_val == self:
                    setattr(old_value, "cart3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart3"):
                opp_val = getattr(value, "cart3", None)
                setattr(value, "cart3", self)

    @property
    def cart3(self):
        return self.__cart3
    @cart3.setter
    def cart3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cartItem__cart3", None)
        self.__cart3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart2"):
                opp_val = getattr(old_value, "cart2", None)
                if opp_val == self:
                    setattr(old_value, "cart2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart2"):
                opp_val = getattr(value, "cart2", None)
                setattr(value, "cart2", self)

    @property
    def product21(self):
        return self.__product21
    @product21.setter
    def product21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cartItem__product21", None)
        self.__product21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cartItem20"):
                opp_val = getattr(old_value, "cartItem20", None)
                if opp_val == self:
                    setattr(old_value, "cartItem20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cartItem20"):
                opp_val = getattr(value, "cartItem20", None)
                setattr(value, "cartItem20", self)



class keywordSet:

    def __init__(self, keyword: str, searchFacade23: "searchFacade" = None, product24: "Product" = None):
        self.keyword = keyword
        self.searchFacade23 = searchFacade23
        self.product24 = product24
        
        pass
    @property
    def keyword(self):
        return self.__keyword
    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    def searchFacade23(self):
        return self.__searchFacade23
    @searchFacade23.setter
    def searchFacade23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_keywordSet__searchFacade23", None)
        self.__searchFacade23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "keywordSet22"):
                opp_val = getattr(old_value, "keywordSet22", None)
                if opp_val == self:
                    setattr(old_value, "keywordSet22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "keywordSet22"):
                opp_val = getattr(value, "keywordSet22", None)
                setattr(value, "keywordSet22", self)

    @property
    def product24(self):
        return self.__product24
    @product24.setter
    def product24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_keywordSet__product24", None)
        self.__product24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "keywordSet25"):
                opp_val = getattr(old_value, "keywordSet25", None)
                if opp_val == self:
                    setattr(old_value, "keywordSet25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "keywordSet25"):
                opp_val = getattr(value, "keywordSet25", None)
                setattr(value, "keywordSet25", self)



class Product:

    def __init__(self, productId: int, Name: str, SKU: str, description: str, attribute5: str, attribute6: str, attribute7: str, Price: str, reviews: str, genre5: "Department" = None, genre7: "Category" = None, orderDetail18: "OrderDetail" = None, cartItem20: "cartItem" = None, keywordSet25: "keywordSet" = None, offer58: "Offer_Interface" = None, price60: "Price" = None, item63: "Item" = None):
        self.productId = productId
        self.Name = Name
        self.SKU = SKU
        self.description = description
        self.attribute5 = attribute5
        self.attribute6 = attribute6
        self.attribute7 = attribute7
        self.Price = Price
        self.reviews = reviews
        self.genre5 = genre5
        self.genre7 = genre7
        self.orderDetail18 = orderDetail18
        self.cartItem20 = cartItem20
        self.keywordSet25 = keywordSet25
        self.offer58 = offer58
        self.price60 = price60
        self.item63 = item63
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def SKU(self):
        return self.__SKU
    @SKU.setter
    def SKU(self, SKU: str):
        self.__SKU = SKU

    @property
    def reviews(self):
        return self.__reviews
    @reviews.setter
    def reviews(self, reviews: str):
        self.__reviews = reviews

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def attribute5(self):
        return self.__attribute5
    @attribute5.setter
    def attribute5(self, attribute5: str):
        self.__attribute5 = attribute5

    @property
    def attribute7(self):
        return self.__attribute7
    @attribute7.setter
    def attribute7(self, attribute7: str):
        self.__attribute7 = attribute7

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: int):
        self.__productId = productId

    @property
    def attribute6(self):
        return self.__attribute6
    @attribute6.setter
    def attribute6(self, attribute6: str):
        self.__attribute6 = attribute6

    @property
    def price60(self):
        return self.__price60
    @price60.setter
    def price60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__price60", None)
        self.__price60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product61"):
                opp_val = getattr(old_value, "product61", None)
                if opp_val == self:
                    setattr(old_value, "product61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product61"):
                opp_val = getattr(value, "product61", None)
                setattr(value, "product61", self)

    @property
    def genre7(self):
        return self.__genre7
    @genre7.setter
    def genre7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__genre7", None)
        self.__genre7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product6"):
                opp_val = getattr(old_value, "product6", None)
                if opp_val == self:
                    setattr(old_value, "product6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product6"):
                opp_val = getattr(value, "product6", None)
                setattr(value, "product6", self)

    @property
    def item63(self):
        return self.__item63
    @item63.setter
    def item63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__item63", None)
        self.__item63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product62"):
                opp_val = getattr(old_value, "product62", None)
                if opp_val == self:
                    setattr(old_value, "product62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product62"):
                opp_val = getattr(value, "product62", None)
                setattr(value, "product62", self)

    @property
    def genre5(self):
        return self.__genre5
    @genre5.setter
    def genre5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__genre5", None)
        self.__genre5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genre4"):
                opp_val = getattr(old_value, "genre4", None)
                if opp_val == self:
                    setattr(old_value, "genre4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genre4"):
                opp_val = getattr(value, "genre4", None)
                setattr(value, "genre4", self)

    @property
    def orderDetail18(self):
        return self.__orderDetail18
    @orderDetail18.setter
    def orderDetail18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__orderDetail18", None)
        self.__orderDetail18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product19"):
                opp_val = getattr(old_value, "product19", None)
                if opp_val == self:
                    setattr(old_value, "product19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product19"):
                opp_val = getattr(value, "product19", None)
                setattr(value, "product19", self)

    @property
    def offer58(self):
        return self.__offer58
    @offer58.setter
    def offer58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__offer58", None)
        self.__offer58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product59"):
                opp_val = getattr(old_value, "product59", None)
                if opp_val == self:
                    setattr(old_value, "product59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product59"):
                opp_val = getattr(value, "product59", None)
                setattr(value, "product59", self)

    @property
    def keywordSet25(self):
        return self.__keywordSet25
    @keywordSet25.setter
    def keywordSet25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__keywordSet25", None)
        self.__keywordSet25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product24"):
                opp_val = getattr(old_value, "product24", None)
                if opp_val == self:
                    setattr(old_value, "product24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product24"):
                opp_val = getattr(value, "product24", None)
                setattr(value, "product24", self)

    @property
    def cartItem20(self):
        return self.__cartItem20
    @cartItem20.setter
    def cartItem20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__cartItem20", None)
        self.__cartItem20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product21"):
                opp_val = getattr(old_value, "product21", None)
                if opp_val == self:
                    setattr(old_value, "product21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product21"):
                opp_val = getattr(value, "product21", None)
                setattr(value, "product21", self)



class OrderDetail:

    def __init__(self, orderId: int, productId: int, productName: str, quantity: int, unitCost: str, subTotal: str, order13: "Order" = None, product19: "Product" = None):
        self.orderId = orderId
        self.productId = productId
        self.productName = productName
        self.quantity = quantity
        self.unitCost = unitCost
        self.subTotal = subTotal
        self.order13 = order13
        self.product19 = product19
        
        pass
    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: int):
        self.__productId = productId

    @property
    def subTotal(self):
        return self.__subTotal
    @subTotal.setter
    def subTotal(self, subTotal: str):
        self.__subTotal = subTotal

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
    def orderId(self):
        return self.__orderId
    @orderId.setter
    def orderId(self, orderId: int):
        self.__orderId = orderId

    @property
    def unitCost(self):
        return self.__unitCost
    @unitCost.setter
    def unitCost(self, unitCost: str):
        self.__unitCost = unitCost

    @property
    def order13(self):
        return self.__order13
    @order13.setter
    def order13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderDetail__order13", None)
        self.__order13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderDetail12"):
                opp_val = getattr(old_value, "orderDetail12", None)
                if opp_val == self:
                    setattr(old_value, "orderDetail12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderDetail12"):
                opp_val = getattr(value, "orderDetail12", None)
                setattr(value, "orderDetail12", self)

    @property
    def product19(self):
        return self.__product19
    @product19.setter
    def product19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderDetail__product19", None)
        self.__product19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderDetail18"):
                opp_val = getattr(old_value, "orderDetail18", None)
                if opp_val == self:
                    setattr(old_value, "orderDetail18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderDetail18"):
                opp_val = getattr(value, "orderDetail18", None)
                setattr(value, "orderDetail18", self)



class Shipping:

    def __init__(self, shippingId: int, shippingType: str, shippingAddress: str, _attr: int, ShippingType: str, Order_Shippinginfo_111: "Order" = None, shippingType272: "ShippingType_Interface" = None, order75: "Order" = None):
        self.shippingId = shippingId
        self.shippingType = shippingType
        self.shippingAddress = shippingAddress
        self._attr = _attr
        self.ShippingType = ShippingType
        self.Order_Shippinginfo_111 = Order_Shippinginfo_111
        self.shippingType272 = shippingType272
        self.order75 = order75
        
        pass
    @property
    def shippingAddress(self):
        return self.__shippingAddress
    @shippingAddress.setter
    def shippingAddress(self, shippingAddress: str):
        self.__shippingAddress = shippingAddress

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: int):
        self.___attr = _attr

    @property
    def ShippingType(self):
        return self.__ShippingType
    @ShippingType.setter
    def ShippingType(self, ShippingType: str):
        self.__ShippingType = ShippingType

    @property
    def shippingId(self):
        return self.__shippingId
    @shippingId.setter
    def shippingId(self, shippingId: int):
        self.__shippingId = shippingId

    @property
    def shippingType(self):
        return self.__shippingType
    @shippingType.setter
    def shippingType(self, shippingType: str):
        self.__shippingType = shippingType

    @property
    def Order_Shippinginfo_111(self):
        return self.__Order_Shippinginfo_111
    @Order_Shippinginfo_111.setter
    def Order_Shippinginfo_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shipping__Order_Shippinginfo_111", None)
        self.__Order_Shippinginfo_111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order_Shippinginfo_010"):
                opp_val = getattr(old_value, "Order_Shippinginfo_010", None)
                if opp_val == self:
                    setattr(old_value, "Order_Shippinginfo_010", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order_Shippinginfo_010"):
                opp_val = getattr(value, "Order_Shippinginfo_010", None)
                setattr(value, "Order_Shippinginfo_010", self)

    @property
    def shippingType272(self):
        return self.__shippingType272
    @shippingType272.setter
    def shippingType272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shipping__shippingType272", None)
        self.__shippingType272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shipping73"):
                opp_val = getattr(old_value, "shipping73", None)
                if opp_val == self:
                    setattr(old_value, "shipping73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shipping73"):
                opp_val = getattr(value, "shipping73", None)
                setattr(value, "shipping73", self)

    @property
    def order75(self):
        return self.__order75
    @order75.setter
    def order75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shipping__order75", None)
        self.__order75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shipping74"):
                opp_val = getattr(old_value, "shipping74", None)
                if opp_val == self:
                    setattr(old_value, "shipping74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shipping74"):
                opp_val = getattr(value, "shipping74", None)
                setattr(value, "shipping74", self)



class Order:

    def __init__(self, OrderId: int, Item: str, dateCreated: str, dateShipped: str, customerName: str, status: str, customerId: str, ShippingAddress: str, BillingAddress: str, OrderStatus: str, Payment: str, Order_Shippinginfo_010: "Shipping" = None, orderDetail12: "OrderDetail" = None, customer15: "Customer" = None, administrator17: "Administrator" = None, orderService65: "OrderService" = None, payment66: "Payment" = None, payment68: "Payment_Interface" = None, shipping74: "Shipping" = None, item77: "Item" = None, address80: "Address" = None):
        self.OrderId = OrderId
        self.Item = Item
        self.dateCreated = dateCreated
        self.dateShipped = dateShipped
        self.customerName = customerName
        self.status = status
        self.customerId = customerId
        self.ShippingAddress = ShippingAddress
        self.BillingAddress = BillingAddress
        self.OrderStatus = OrderStatus
        self.Payment = Payment
        self.Order_Shippinginfo_010 = Order_Shippinginfo_010
        self.orderDetail12 = orderDetail12
        self.customer15 = customer15
        self.administrator17 = administrator17
        self.orderService65 = orderService65
        self.payment66 = payment66
        self.payment68 = payment68
        self.shipping74 = shipping74
        self.item77 = item77
        self.address80 = address80
        
        pass
    @property
    def Payment(self):
        return self.__Payment
    @Payment.setter
    def Payment(self, Payment: str):
        self.__Payment = Payment

    @property
    def OrderId(self):
        return self.__OrderId
    @OrderId.setter
    def OrderId(self, OrderId: int):
        self.__OrderId = OrderId

    @property
    def customerId(self):
        return self.__customerId
    @customerId.setter
    def customerId(self, customerId: str):
        self.__customerId = customerId

    @property
    def ShippingAddress(self):
        return self.__ShippingAddress
    @ShippingAddress.setter
    def ShippingAddress(self, ShippingAddress: str):
        self.__ShippingAddress = ShippingAddress

    @property
    def BillingAddress(self):
        return self.__BillingAddress
    @BillingAddress.setter
    def BillingAddress(self, BillingAddress: str):
        self.__BillingAddress = BillingAddress

    @property
    def OrderStatus(self):
        return self.__OrderStatus
    @OrderStatus.setter
    def OrderStatus(self, OrderStatus: str):
        self.__OrderStatus = OrderStatus

    @property
    def customerName(self):
        return self.__customerName
    @customerName.setter
    def customerName(self, customerName: str):
        self.__customerName = customerName

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def dateShipped(self):
        return self.__dateShipped
    @dateShipped.setter
    def dateShipped(self, dateShipped: str):
        self.__dateShipped = dateShipped

    @property
    def dateCreated(self):
        return self.__dateCreated
    @dateCreated.setter
    def dateCreated(self, dateCreated: str):
        self.__dateCreated = dateCreated

    @property
    def Item(self):
        return self.__Item
    @Item.setter
    def Item(self, Item: str):
        self.__Item = Item

    @property
    def orderService65(self):
        return self.__orderService65
    @orderService65.setter
    def orderService65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orderService65", None)
        self.__orderService65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order64"):
                opp_val = getattr(old_value, "order64", None)
                if opp_val == self:
                    setattr(old_value, "order64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order64"):
                opp_val = getattr(value, "order64", None)
                setattr(value, "order64", self)

    @property
    def item77(self):
        return self.__item77
    @item77.setter
    def item77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__item77", None)
        self.__item77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order76"):
                opp_val = getattr(old_value, "order76", None)
                if opp_val == self:
                    setattr(old_value, "order76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order76"):
                opp_val = getattr(value, "order76", None)
                setattr(value, "order76", self)

    @property
    def administrator17(self):
        return self.__administrator17
    @administrator17.setter
    def administrator17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__administrator17", None)
        self.__administrator17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order16"):
                opp_val = getattr(old_value, "order16", None)
                if opp_val == self:
                    setattr(old_value, "order16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order16"):
                opp_val = getattr(value, "order16", None)
                setattr(value, "order16", self)

    @property
    def orderDetail12(self):
        return self.__orderDetail12
    @orderDetail12.setter
    def orderDetail12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orderDetail12", None)
        self.__orderDetail12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order13"):
                opp_val = getattr(old_value, "order13", None)
                if opp_val == self:
                    setattr(old_value, "order13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order13"):
                opp_val = getattr(value, "order13", None)
                setattr(value, "order13", self)

    @property
    def payment66(self):
        return self.__payment66
    @payment66.setter
    def payment66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment66", None)
        self.__payment66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order67"):
                opp_val = getattr(old_value, "order67", None)
                if opp_val == self:
                    setattr(old_value, "order67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order67"):
                opp_val = getattr(value, "order67", None)
                setattr(value, "order67", self)

    @property
    def Order_Shippinginfo_010(self):
        return self.__Order_Shippinginfo_010
    @Order_Shippinginfo_010.setter
    def Order_Shippinginfo_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__Order_Shippinginfo_010", None)
        self.__Order_Shippinginfo_010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order_Shippinginfo_111"):
                opp_val = getattr(old_value, "Order_Shippinginfo_111", None)
                if opp_val == self:
                    setattr(old_value, "Order_Shippinginfo_111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order_Shippinginfo_111"):
                opp_val = getattr(value, "Order_Shippinginfo_111", None)
                setattr(value, "Order_Shippinginfo_111", self)

    @property
    def shipping74(self):
        return self.__shipping74
    @shipping74.setter
    def shipping74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__shipping74", None)
        self.__shipping74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order75"):
                opp_val = getattr(old_value, "order75", None)
                if opp_val == self:
                    setattr(old_value, "order75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order75"):
                opp_val = getattr(value, "order75", None)
                setattr(value, "order75", self)

    @property
    def customer15(self):
        return self.__customer15
    @customer15.setter
    def customer15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer15", None)
        self.__customer15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order14"):
                opp_val = getattr(old_value, "order14", None)
                if opp_val == self:
                    setattr(old_value, "order14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order14"):
                opp_val = getattr(value, "order14", None)
                setattr(value, "order14", self)

    @property
    def address80(self):
        return self.__address80
    @address80.setter
    def address80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__address80", None)
        self.__address80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order81"):
                opp_val = getattr(old_value, "order81", None)
                if opp_val == self:
                    setattr(old_value, "order81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order81"):
                opp_val = getattr(value, "order81", None)
                setattr(value, "order81", self)

    @property
    def payment68(self):
        return self.__payment68
    @payment68.setter
    def payment68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment68", None)
        self.__payment68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order69"):
                opp_val = getattr(old_value, "order69", None)
                if opp_val == self:
                    setattr(old_value, "order69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order69"):
                opp_val = getattr(value, "order69", None)
                setattr(value, "order69", self)



class searchFacade:

    pass


class Department:

    def __init__(self, departmentID: int, departmentName: str, description: str, genre4: "Product" = None, sessionManager9: "SessionManager" = None, department52: "Department" = None, department53: "Department" = None, category54: "Category" = None):
        self.departmentID = departmentID
        self.departmentName = departmentName
        self.description = description
        self.genre4 = genre4
        self.sessionManager9 = sessionManager9
        self.department52 = department52
        self.department53 = department53
        self.category54 = category54
        
        pass
    @property
    def departmentName(self):
        return self.__departmentName
    @departmentName.setter
    def departmentName(self, departmentName: str):
        self.__departmentName = departmentName

    @property
    def departmentID(self):
        return self.__departmentID
    @departmentID.setter
    def departmentID(self, departmentID: int):
        self.__departmentID = departmentID

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def category54(self):
        return self.__category54
    @category54.setter
    def category54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__category54", None)
        self.__category54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department55"):
                opp_val = getattr(old_value, "department55", None)
                if opp_val == self:
                    setattr(old_value, "department55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department55"):
                opp_val = getattr(value, "department55", None)
                setattr(value, "department55", self)

    @property
    def sessionManager9(self):
        return self.__sessionManager9
    @sessionManager9.setter
    def sessionManager9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__sessionManager9", None)
        self.__sessionManager9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genre8"):
                opp_val = getattr(old_value, "genre8", None)
                if opp_val == self:
                    setattr(old_value, "genre8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genre8"):
                opp_val = getattr(value, "genre8", None)
                setattr(value, "genre8", self)

    @property
    def department53(self):
        return self.__department53
    @department53.setter
    def department53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__department53", None)
        self.__department53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department52"):
                opp_val = getattr(old_value, "department52", None)
                if opp_val == self:
                    setattr(old_value, "department52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department52"):
                opp_val = getattr(value, "department52", None)
                setattr(value, "department52", self)

    @property
    def department52(self):
        return self.__department52
    @department52.setter
    def department52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__department52", None)
        self.__department52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department53"):
                opp_val = getattr(old_value, "department53", None)
                if opp_val == self:
                    setattr(old_value, "department53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department53"):
                opp_val = getattr(value, "department53", None)
                setattr(value, "department53", self)

    @property
    def genre4(self):
        return self.__genre4
    @genre4.setter
    def genre4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__genre4", None)
        self.__genre4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genre5"):
                opp_val = getattr(old_value, "genre5", None)
                if opp_val == self:
                    setattr(old_value, "genre5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genre5"):
                opp_val = getattr(value, "genre5", None)
                setattr(value, "genre5", self)



class Administrator:

    def __init__(self, adminName: str, email: str, order16: "Order" = None):
        self.adminName = adminName
        self.email = email
        self.order16 = order16
        
        pass
    @property
    def adminName(self):
        return self.__adminName
    @adminName.setter
    def adminName(self, adminName: str):
        self.__adminName = adminName

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def order16(self):
        return self.__order16
    @order16.setter
    def order16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__order16", None)
        self.__order16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator17"):
                opp_val = getattr(old_value, "administrator17", None)
                if opp_val == self:
                    setattr(old_value, "administrator17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator17"):
                opp_val = getattr(value, "administrator17", None)
                setattr(value, "administrator17", self)



class Customer:

    def __init__(self, customerName: str, address: str, email: str, phoneno: int, creditcardinfo: str, shippinginfo: str, newsLettersub: bool, surveys: bool, order14: "Order" = None, promotions34: "promotions" = None):
        self.customerName = customerName
        self.address = address
        self.email = email
        self.phoneno = phoneno
        self.creditcardinfo = creditcardinfo
        self.shippinginfo = shippinginfo
        self.newsLettersub = newsLettersub
        self.surveys = surveys
        self.order14 = order14
        self.promotions34 = promotions34
        
        pass
    @property
    def shippinginfo(self):
        return self.__shippinginfo
    @shippinginfo.setter
    def shippinginfo(self, shippinginfo: str):
        self.__shippinginfo = shippinginfo

    @property
    def phoneno(self):
        return self.__phoneno
    @phoneno.setter
    def phoneno(self, phoneno: int):
        self.__phoneno = phoneno

    @property
    def surveys(self):
        return self.__surveys
    @surveys.setter
    def surveys(self, surveys: bool):
        self.__surveys = surveys

    @property
    def creditcardinfo(self):
        return self.__creditcardinfo
    @creditcardinfo.setter
    def creditcardinfo(self, creditcardinfo: str):
        self.__creditcardinfo = creditcardinfo

    @property
    def newsLettersub(self):
        return self.__newsLettersub
    @newsLettersub.setter
    def newsLettersub(self, newsLettersub: bool):
        self.__newsLettersub = newsLettersub

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def customerName(self):
        return self.__customerName
    @customerName.setter
    def customerName(self, customerName: str):
        self.__customerName = customerName

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def promotions34(self):
        return self.__promotions34
    @promotions34.setter
    def promotions34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__promotions34", None)
        self.__promotions34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer35"):
                opp_val = getattr(old_value, "customer35", None)
                if opp_val == self:
                    setattr(old_value, "customer35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer35"):
                opp_val = getattr(value, "customer35", None)
                setattr(value, "customer35", self)

    @property
    def order14(self):
        return self.__order14
    @order14.setter
    def order14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__order14", None)
        self.__order14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer15"):
                opp_val = getattr(old_value, "customer15", None)
                if opp_val == self:
                    setattr(old_value, "customer15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer15"):
                opp_val = getattr(value, "customer15", None)
                setattr(value, "customer15", self)



class SessionManager:

    def __init__(self, userid: str, departmentName: str, user0: "User" = None, genre8: "Department" = None):
        self.userid = userid
        self.departmentName = departmentName
        self.user0 = user0
        self.genre8 = genre8
        
        pass
    @property
    def departmentName(self):
        return self.__departmentName
    @departmentName.setter
    def departmentName(self, departmentName: str):
        self.__departmentName = departmentName

    @property
    def userid(self):
        return self.__userid
    @userid.setter
    def userid(self, userid: str):
        self.__userid = userid

    @property
    def genre8(self):
        return self.__genre8
    @genre8.setter
    def genre8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SessionManager__genre8", None)
        self.__genre8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sessionManager9"):
                opp_val = getattr(old_value, "sessionManager9", None)
                if opp_val == self:
                    setattr(old_value, "sessionManager9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sessionManager9"):
                opp_val = getattr(value, "sessionManager9", None)
                setattr(value, "sessionManager9", self)

    @property
    def user0(self):
        return self.__user0
    @user0.setter
    def user0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SessionManager__user0", None)
        self.__user0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sessionManager1"):
                opp_val = getattr(old_value, "sessionManager1", None)
                if opp_val == self:
                    setattr(old_value, "sessionManager1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sessionManager1"):
                opp_val = getattr(value, "sessionManager1", None)
                setattr(value, "sessionManager1", self)



class User:

    def __init__(self, userId: str, password: str, loginStatus: str, sessionManager1: "SessionManager" = None):
        self.userId = userId
        self.password = password
        self.loginStatus = loginStatus
        self.sessionManager1 = sessionManager1
        
        pass
    @property
    def loginStatus(self):
        return self.__loginStatus
    @loginStatus.setter
    def loginStatus(self, loginStatus: str):
        self.__loginStatus = loginStatus

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def sessionManager1(self):
        return self.__sessionManager1
    @sessionManager1.setter
    def sessionManager1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__sessionManager1", None)
        self.__sessionManager1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user0"):
                opp_val = getattr(old_value, "user0", None)
                if opp_val == self:
                    setattr(old_value, "user0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user0"):
                opp_val = getattr(value, "user0", None)
                setattr(value, "user0", self)



class email:

    def __init__(self, EmailAddress: str):
        self.EmailAddress = EmailAddress
        
        pass
    @property
    def EmailAddress(self):
        return self.__EmailAddress
    @EmailAddress.setter
    def EmailAddress(self, EmailAddress: str):
        self.__EmailAddress = EmailAddress



class SMS:

    def __init__(self, MobileNo: int):
        self.MobileNo = MobileNo
        
        pass
    @property
    def MobileNo(self):
        return self.__MobileNo
    @MobileNo.setter
    def MobileNo(self, MobileNo: int):
        self.__MobileNo = MobileNo



class Notify_Interface:

    pass


class Address:

    def __init__(self, Street: str, City: str, State: str, ZipCode: str, Country: str, Type: str, order81: "Order" = None):
        self.Street = Street
        self.City = City
        self.State = State
        self.ZipCode = ZipCode
        self.Country = Country
        self.Type = Type
        self.order81 = order81
        
        pass
    @property
    def Street(self):
        return self.__Street
    @Street.setter
    def Street(self, Street: str):
        self.__Street = Street

    @property
    def State(self):
        return self.__State
    @State.setter
    def State(self, State: str):
        self.__State = State

    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Country(self):
        return self.__Country
    @Country.setter
    def Country(self, Country: str):
        self.__Country = Country

    @property
    def ZipCode(self):
        return self.__ZipCode
    @ZipCode.setter
    def ZipCode(self, ZipCode: str):
        self.__ZipCode = ZipCode

    @property
    def City(self):
        return self.__City
    @City.setter
    def City(self, City: str):
        self.__City = City

    @property
    def order81(self):
        return self.__order81
    @order81.setter
    def order81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Address__order81", None)
        self.__order81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "address80"):
                opp_val = getattr(old_value, "address80", None)
                if opp_val == self:
                    setattr(old_value, "address80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "address80"):
                opp_val = getattr(value, "address80", None)
                setattr(value, "address80", self)



class ShoppingCart:

    def __init__(self, Item: str, GetTotalPrice: str, quantity: int, dateAdded: int, item78: "Item" = None):
        self.Item = Item
        self.GetTotalPrice = GetTotalPrice
        self.quantity = quantity
        self.dateAdded = dateAdded
        self.item78 = item78
        
        pass
    @property
    def GetTotalPrice(self):
        return self.__GetTotalPrice
    @GetTotalPrice.setter
    def GetTotalPrice(self, GetTotalPrice: str):
        self.__GetTotalPrice = GetTotalPrice

    @property
    def Item(self):
        return self.__Item
    @Item.setter
    def Item(self, Item: str):
        self.__Item = Item

    @property
    def dateAdded(self):
        return self.__dateAdded
    @dateAdded.setter
    def dateAdded(self, dateAdded: int):
        self.__dateAdded = dateAdded

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def item78(self):
        return self.__item78
    @item78.setter
    def item78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__item78", None)
        self.__item78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart79"):
                opp_val = getattr(old_value, "shoppingCart79", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart79"):
                opp_val = getattr(value, "shoppingCart79", None)
                setattr(value, "shoppingCart79", self)



class Vendor:

    def __init__(self, attribute: str, attribute2: str):
        self.attribute = attribute
        self.attribute2 = attribute2
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class ShippingType_Interface:

    pass


class PayLater1:

    def __init__(self, UserID: str):
        self.UserID = UserID
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: str):
        self.__UserID = UserID



class CreditCardPayment:

    def __init__(self, CardType: str, CardNumber: int):
        self.CardType = CardType
        self.CardNumber = CardNumber
        
        pass
    @property
    def CardNumber(self):
        return self.__CardNumber
    @CardNumber.setter
    def CardNumber(self, CardNumber: int):
        self.__CardNumber = CardNumber

    @property
    def CardType(self):
        return self.__CardType
    @CardType.setter
    def CardType(self, CardType: str):
        self.__CardType = CardType



class Payment_Interface:

    pass


class Payment:

    pass


class OrderService:

    def __init__(self, attribute: str, order64: "Order" = None, notify82: "Notify_Interface" = None):
        self.attribute = attribute
        self.order64 = order64
        self.notify82 = notify82
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def notify82(self):
        return self.__notify82
    @notify82.setter
    def notify82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderService__notify82", None)
        self.__notify82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderService83"):
                opp_val = getattr(old_value, "orderService83", None)
                if opp_val == self:
                    setattr(old_value, "orderService83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderService83"):
                opp_val = getattr(value, "orderService83", None)
                setattr(value, "orderService83", self)

    @property
    def order64(self):
        return self.__order64
    @order64.setter
    def order64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderService__order64", None)
        self.__order64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderService65"):
                opp_val = getattr(old_value, "orderService65", None)
                if opp_val == self:
                    setattr(old_value, "orderService65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderService65"):
                opp_val = getattr(value, "orderService65", None)
                setattr(value, "orderService65", self)



class Item:

    def __init__(self, Name: str, Quantity: int, attribute: str, product62: "Product" = None, order76: "Order" = None, shoppingCart79: "ShoppingCart" = None):
        self.Name = Name
        self.Quantity = Quantity
        self.attribute = attribute
        self.product62 = product62
        self.order76 = order76
        self.shoppingCart79 = shoppingCart79
        
        pass
    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def shoppingCart79(self):
        return self.__shoppingCart79
    @shoppingCart79.setter
    def shoppingCart79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__shoppingCart79", None)
        self.__shoppingCart79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item78"):
                opp_val = getattr(old_value, "item78", None)
                if opp_val == self:
                    setattr(old_value, "item78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item78"):
                opp_val = getattr(value, "item78", None)
                setattr(value, "item78", self)

    @property
    def product62(self):
        return self.__product62
    @product62.setter
    def product62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__product62", None)
        self.__product62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item63"):
                opp_val = getattr(old_value, "item63", None)
                if opp_val == self:
                    setattr(old_value, "item63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item63"):
                opp_val = getattr(value, "item63", None)
                setattr(value, "item63", self)

    @property
    def order76(self):
        return self.__order76
    @order76.setter
    def order76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__order76", None)
        self.__order76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item77"):
                opp_val = getattr(old_value, "item77", None)
                if opp_val == self:
                    setattr(old_value, "item77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item77"):
                opp_val = getattr(value, "item77", None)
                setattr(value, "item77", self)



class Price:

    def __init__(self, ActualPrice: str, price56: "Price" = None, price57: "Price" = None, product61: "Product" = None):
        self.ActualPrice = ActualPrice
        self.price56 = price56
        self.price57 = price57
        self.product61 = product61
        
        pass
    @property
    def ActualPrice(self):
        return self.__ActualPrice
    @ActualPrice.setter
    def ActualPrice(self, ActualPrice: str):
        self.__ActualPrice = ActualPrice

    @property
    def price57(self):
        return self.__price57
    @price57.setter
    def price57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Price__price57", None)
        self.__price57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "price56"):
                opp_val = getattr(old_value, "price56", None)
                if opp_val == self:
                    setattr(old_value, "price56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "price56"):
                opp_val = getattr(value, "price56", None)
                setattr(value, "price56", self)

    @property
    def price56(self):
        return self.__price56
    @price56.setter
    def price56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Price__price56", None)
        self.__price56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "price57"):
                opp_val = getattr(old_value, "price57", None)
                if opp_val == self:
                    setattr(old_value, "price57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "price57"):
                opp_val = getattr(value, "price57", None)
                setattr(value, "price57", self)

    @property
    def product61(self):
        return self.__product61
    @product61.setter
    def product61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Price__product61", None)
        self.__product61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "price60"):
                opp_val = getattr(old_value, "price60", None)
                if opp_val == self:
                    setattr(old_value, "price60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "price60"):
                opp_val = getattr(value, "price60", None)
                setattr(value, "price60", self)



class TimeBasedDiscount:

    pass


class ProductDiscount:

    pass


class Offer_Interface:

    pass


class Class2:

    pass


class Class1:

    pass


class Category:

    def __init__(self, description: str, categoryID: int, categoryName: str, departmentId: int, product6: "Product" = None, department55: "Department" = None):
        self.description = description
        self.categoryID = categoryID
        self.categoryName = categoryName
        self.departmentId = departmentId
        self.product6 = product6
        self.department55 = department55
        
        pass
    @property
    def categoryID(self):
        return self.__categoryID
    @categoryID.setter
    def categoryID(self, categoryID: int):
        self.__categoryID = categoryID

    @property
    def departmentId(self):
        return self.__departmentId
    @departmentId.setter
    def departmentId(self, departmentId: int):
        self.__departmentId = departmentId

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def categoryName(self):
        return self.__categoryName
    @categoryName.setter
    def categoryName(self, categoryName: str):
        self.__categoryName = categoryName

    @property
    def department55(self):
        return self.__department55
    @department55.setter
    def department55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__department55", None)
        self.__department55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category54"):
                opp_val = getattr(old_value, "category54", None)
                if opp_val == self:
                    setattr(old_value, "category54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category54"):
                opp_val = getattr(value, "category54", None)
                setattr(value, "category54", self)

    @property
    def product6(self):
        return self.__product6
    @product6.setter
    def product6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__product6", None)
        self.__product6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genre7"):
                opp_val = getattr(old_value, "genre7", None)
                if opp_val == self:
                    setattr(old_value, "genre7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genre7"):
                opp_val = getattr(value, "genre7", None)
                setattr(value, "genre7", self)



class PayLater:

    pass


class Gpay:

    pass


class Credit_DebitCard1:

    pass


class PushNotification:

    pass


class EmailNotification:

    pass


class paylater_Interface:

    pass


class Class:

    pass


class gpay_Interface:

    pass


class Credit_DebitCard:

    pass


class billdesk_Interface:

    pass


class payment_Interface:

    pass


class promotions:

    def __init__(self, promotionCode: str, startDate: int, endDate: int, customer35: "Customer" = None):
        self.promotionCode = promotionCode
        self.startDate = startDate
        self.endDate = endDate
        self.customer35 = customer35
        
        pass
    @property
    def endDate(self):
        return self.__endDate
    @endDate.setter
    def endDate(self, endDate: int):
        self.__endDate = endDate

    @property
    def promotionCode(self):
        return self.__promotionCode
    @promotionCode.setter
    def promotionCode(self, promotionCode: str):
        self.__promotionCode = promotionCode

    @property
    def startDate(self):
        return self.__startDate
    @startDate.setter
    def startDate(self, startDate: int):
        self.__startDate = startDate

    @property
    def customer35(self):
        return self.__customer35
    @customer35.setter
    def customer35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_promotions__customer35", None)
        self.__customer35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "promotions34"):
                opp_val = getattr(old_value, "promotions34", None)
                if opp_val == self:
                    setattr(old_value, "promotions34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "promotions34"):
                opp_val = getattr(value, "promotions34", None)
                setattr(value, "promotions34", self)



class customeraddress_Interface:

    pass


class pickuppoint_Interface:

    pass


class shiporder_Interface:

    pass


class mobile_Interface:

    pass
