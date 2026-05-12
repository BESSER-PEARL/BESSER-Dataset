from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class shippinginfo:

    def __init__(self, shippingId: int, shippingcost: int, order_shippinginfo_113: "order" = None):
        self.shippingId = shippingId
        self.shippingcost = shippingcost
        self.order_shippinginfo_113 = order_shippinginfo_113
        
        pass
    @property
    def shippingcost(self):
        return self.__shippingcost
    @shippingcost.setter
    def shippingcost(self, shippingcost: int):
        self.__shippingcost = shippingcost

    @property
    def shippingId(self):
        return self.__shippingId
    @shippingId.setter
    def shippingId(self, shippingId: int):
        self.__shippingId = shippingId

    @property
    def order_shippinginfo_113(self):
        return self.__order_shippinginfo_113
    @order_shippinginfo_113.setter
    def order_shippinginfo_113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shippinginfo__order_shippinginfo_113", None)
        self.__order_shippinginfo_113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_shippinginfo_012"):
                opp_val = getattr(old_value, "order_shippinginfo_012", None)
                if opp_val == self:
                    setattr(old_value, "order_shippinginfo_012", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_shippinginfo_012"):
                opp_val = getattr(value, "order_shippinginfo_012", None)
                setattr(value, "order_shippinginfo_012", self)



class order:

    def __init__(self, orderId: int, datecreated: str, name: str, customerid: int, shippingid: str, coustomer_order_19: "coustomer" = None, order_orderDetail_010: "orderDetail" = None, order_shippinginfo_012: "shippinginfo" = None):
        self.orderId = orderId
        self.datecreated = datecreated
        self.name = name
        self.customerid = customerid
        self.shippingid = shippingid
        self.coustomer_order_19 = coustomer_order_19
        self.order_orderDetail_010 = order_orderDetail_010
        self.order_shippinginfo_012 = order_shippinginfo_012
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def orderId(self):
        return self.__orderId
    @orderId.setter
    def orderId(self, orderId: int):
        self.__orderId = orderId

    @property
    def shippingid(self):
        return self.__shippingid
    @shippingid.setter
    def shippingid(self, shippingid: str):
        self.__shippingid = shippingid

    @property
    def datecreated(self):
        return self.__datecreated
    @datecreated.setter
    def datecreated(self, datecreated: str):
        self.__datecreated = datecreated

    @property
    def customerid(self):
        return self.__customerid
    @customerid.setter
    def customerid(self, customerid: int):
        self.__customerid = customerid

    @property
    def order_orderDetail_010(self):
        return self.__order_orderDetail_010
    @order_orderDetail_010.setter
    def order_orderDetail_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__order_orderDetail_010", None)
        self.__order_orderDetail_010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_orderDetail_111"):
                opp_val = getattr(old_value, "order_orderDetail_111", None)
                if opp_val == self:
                    setattr(old_value, "order_orderDetail_111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_orderDetail_111"):
                opp_val = getattr(value, "order_orderDetail_111", None)
                setattr(value, "order_orderDetail_111", self)

    @property
    def coustomer_order_19(self):
        return self.__coustomer_order_19
    @coustomer_order_19.setter
    def coustomer_order_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__coustomer_order_19", None)
        self.__coustomer_order_19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coustomer_order_08"):
                opp_val = getattr(old_value, "coustomer_order_08", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coustomer_order_08"):
                opp_val = getattr(value, "coustomer_order_08", None)
                if opp_val is None:
                    setattr(value, "coustomer_order_08", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order_shippinginfo_012(self):
        return self.__order_shippinginfo_012
    @order_shippinginfo_012.setter
    def order_shippinginfo_012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__order_shippinginfo_012", None)
        self.__order_shippinginfo_012 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_shippinginfo_113"):
                opp_val = getattr(old_value, "order_shippinginfo_113", None)
                if opp_val == self:
                    setattr(old_value, "order_shippinginfo_113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_shippinginfo_113"):
                opp_val = getattr(value, "order_shippinginfo_113", None)
                setattr(value, "order_shippinginfo_113", self)



class orderDetail:

    def __init__(self, orderId: int, productid: int, productname: str, quantity: int, unitcost: float, subtotall: float, orderDetail_ProLocal_06: "product" = None, order_orderDetail_111: "order" = None):
        self.orderId = orderId
        self.productid = productid
        self.productname = productname
        self.quantity = quantity
        self.unitcost = unitcost
        self.subtotall = subtotall
        self.orderDetail_ProLocal_06 = orderDetail_ProLocal_06
        self.order_orderDetail_111 = order_orderDetail_111
        
        pass
    @property
    def orderId(self):
        return self.__orderId
    @orderId.setter
    def orderId(self, orderId: int):
        self.__orderId = orderId

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def subtotall(self):
        return self.__subtotall
    @subtotall.setter
    def subtotall(self, subtotall: float):
        self.__subtotall = subtotall

    @property
    def productname(self):
        return self.__productname
    @productname.setter
    def productname(self, productname: str):
        self.__productname = productname

    @property
    def unitcost(self):
        return self.__unitcost
    @unitcost.setter
    def unitcost(self, unitcost: float):
        self.__unitcost = unitcost

    @property
    def productid(self):
        return self.__productid
    @productid.setter
    def productid(self, productid: int):
        self.__productid = productid

    @property
    def orderDetail_ProLocal_06(self):
        return self.__orderDetail_ProLocal_06
    @orderDetail_ProLocal_06.setter
    def orderDetail_ProLocal_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_orderDetail__orderDetail_ProLocal_06", None)
        self.__orderDetail_ProLocal_06 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderDetail_ProLocal_17"):
                opp_val = getattr(old_value, "orderDetail_ProLocal_17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderDetail_ProLocal_17"):
                opp_val = getattr(value, "orderDetail_ProLocal_17", None)
                if opp_val is None:
                    setattr(value, "orderDetail_ProLocal_17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order_orderDetail_111(self):
        return self.__order_orderDetail_111
    @order_orderDetail_111.setter
    def order_orderDetail_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_orderDetail__order_orderDetail_111", None)
        self.__order_orderDetail_111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_orderDetail_010"):
                opp_val = getattr(old_value, "order_orderDetail_010", None)
                if opp_val == self:
                    setattr(old_value, "order_orderDetail_010", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_orderDetail_010"):
                opp_val = getattr(value, "order_orderDetail_010", None)
                setattr(value, "order_orderDetail_010", self)



class product:

    def __init__(self, productId: int, name: str, description: str, price: int, image: str, cartitem_ProLocal_15: "cartitem" = None, orderDetail_ProLocal_17: set["orderDetail"] = None):
        self.productId = productId
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.cartitem_ProLocal_15 = cartitem_ProLocal_15
        self.orderDetail_ProLocal_17 = orderDetail_ProLocal_17 if orderDetail_ProLocal_17 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: int):
        self.__productId = productId

    @property
    def cartitem_ProLocal_15(self):
        return self.__cartitem_ProLocal_15
    @cartitem_ProLocal_15.setter
    def cartitem_ProLocal_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product__cartitem_ProLocal_15", None)
        self.__cartitem_ProLocal_15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cartitem_ProLocal_04"):
                opp_val = getattr(old_value, "cartitem_ProLocal_04", None)
                if opp_val == self:
                    setattr(old_value, "cartitem_ProLocal_04", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cartitem_ProLocal_04"):
                opp_val = getattr(value, "cartitem_ProLocal_04", None)
                setattr(value, "cartitem_ProLocal_04", self)

    @property
    def orderDetail_ProLocal_17(self):
        return self.__orderDetail_ProLocal_17
    @orderDetail_ProLocal_17.setter
    def orderDetail_ProLocal_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product__orderDetail_ProLocal_17", None)
        self.__orderDetail_ProLocal_17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "orderDetail_ProLocal_06"):
                    opp_val = getattr(item, "orderDetail_ProLocal_06", None)
                    
                    if opp_val == self:
                        setattr(item, "orderDetail_ProLocal_06", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "orderDetail_ProLocal_06"):
                    opp_val = getattr(item, "orderDetail_ProLocal_06", None)
                    
                    setattr(item, "orderDetail_ProLocal_06", self)
                    



class cartitem:

    def __init__(self, productId: int, quantity: int, unitcost: float, subtotal: float, ShoppingCart_cartitem_13: "ShoppingCart" = None, cartitem_ProLocal_04: "product" = None):
        self.productId = productId
        self.quantity = quantity
        self.unitcost = unitcost
        self.subtotal = subtotal
        self.ShoppingCart_cartitem_13 = ShoppingCart_cartitem_13
        self.cartitem_ProLocal_04 = cartitem_ProLocal_04
        
        pass
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
    def unitcost(self):
        return self.__unitcost
    @unitcost.setter
    def unitcost(self, unitcost: float):
        self.__unitcost = unitcost

    @property
    def subtotal(self):
        return self.__subtotal
    @subtotal.setter
    def subtotal(self, subtotal: float):
        self.__subtotal = subtotal

    @property
    def cartitem_ProLocal_04(self):
        return self.__cartitem_ProLocal_04
    @cartitem_ProLocal_04.setter
    def cartitem_ProLocal_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cartitem__cartitem_ProLocal_04", None)
        self.__cartitem_ProLocal_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cartitem_ProLocal_15"):
                opp_val = getattr(old_value, "cartitem_ProLocal_15", None)
                if opp_val == self:
                    setattr(old_value, "cartitem_ProLocal_15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cartitem_ProLocal_15"):
                opp_val = getattr(value, "cartitem_ProLocal_15", None)
                setattr(value, "cartitem_ProLocal_15", self)

    @property
    def ShoppingCart_cartitem_13(self):
        return self.__ShoppingCart_cartitem_13
    @ShoppingCart_cartitem_13.setter
    def ShoppingCart_cartitem_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cartitem__ShoppingCart_cartitem_13", None)
        self.__ShoppingCart_cartitem_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ShoppingCart_cartitem_02"):
                opp_val = getattr(old_value, "ShoppingCart_cartitem_02", None)
                if opp_val == self:
                    setattr(old_value, "ShoppingCart_cartitem_02", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ShoppingCart_cartitem_02"):
                opp_val = getattr(value, "ShoppingCart_cartitem_02", None)
                setattr(value, "ShoppingCart_cartitem_02", self)



class ShoppingCart:

    def __init__(self, cartId: int, productId: int, quantity: int, dateAdded: int, ShoppingCart_coustomer_00: "coustomer" = None, ShoppingCart_cartitem_02: "cartitem" = None):
        self.cartId = cartId
        self.productId = productId
        self.quantity = quantity
        self.dateAdded = dateAdded
        self.ShoppingCart_coustomer_00 = ShoppingCart_coustomer_00
        self.ShoppingCart_cartitem_02 = ShoppingCart_cartitem_02
        
        pass
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def cartId(self):
        return self.__cartId
    @cartId.setter
    def cartId(self, cartId: int):
        self.__cartId = cartId

    @property
    def dateAdded(self):
        return self.__dateAdded
    @dateAdded.setter
    def dateAdded(self, dateAdded: int):
        self.__dateAdded = dateAdded

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: int):
        self.__productId = productId

    @property
    def ShoppingCart_cartitem_02(self):
        return self.__ShoppingCart_cartitem_02
    @ShoppingCart_cartitem_02.setter
    def ShoppingCart_cartitem_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__ShoppingCart_cartitem_02", None)
        self.__ShoppingCart_cartitem_02 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ShoppingCart_cartitem_13"):
                opp_val = getattr(old_value, "ShoppingCart_cartitem_13", None)
                if opp_val == self:
                    setattr(old_value, "ShoppingCart_cartitem_13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ShoppingCart_cartitem_13"):
                opp_val = getattr(value, "ShoppingCart_cartitem_13", None)
                setattr(value, "ShoppingCart_cartitem_13", self)

    @property
    def ShoppingCart_coustomer_00(self):
        return self.__ShoppingCart_coustomer_00
    @ShoppingCart_coustomer_00.setter
    def ShoppingCart_coustomer_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__ShoppingCart_coustomer_00", None)
        self.__ShoppingCart_coustomer_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ShoppingCart_coustomer_11"):
                opp_val = getattr(old_value, "ShoppingCart_coustomer_11", None)
                if opp_val == self:
                    setattr(old_value, "ShoppingCart_coustomer_11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ShoppingCart_coustomer_11"):
                opp_val = getattr(value, "ShoppingCart_coustomer_11", None)
                setattr(value, "ShoppingCart_coustomer_11", self)



class coustomer:

    def __init__(self, customerId: int, name: str, address: str, email: str, phoneno: int, shippinginfo: str, ShoppingCart_coustomer_11: "ShoppingCart" = None, coustomer_order_08: set["order"] = None):
        self.customerId = customerId
        self.name = name
        self.address = address
        self.email = email
        self.phoneno = phoneno
        self.shippinginfo = shippinginfo
        self.ShoppingCart_coustomer_11 = ShoppingCart_coustomer_11
        self.coustomer_order_08 = coustomer_order_08 if coustomer_order_08 is not None else set()
        
        pass
    @property
    def shippinginfo(self):
        return self.__shippinginfo
    @shippinginfo.setter
    def shippinginfo(self, shippinginfo: str):
        self.__shippinginfo = shippinginfo

    @property
    def customerId(self):
        return self.__customerId
    @customerId.setter
    def customerId(self, customerId: int):
        self.__customerId = customerId

    @property
    def phoneno(self):
        return self.__phoneno
    @phoneno.setter
    def phoneno(self, phoneno: int):
        self.__phoneno = phoneno

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def ShoppingCart_coustomer_11(self):
        return self.__ShoppingCart_coustomer_11
    @ShoppingCart_coustomer_11.setter
    def ShoppingCart_coustomer_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coustomer__ShoppingCart_coustomer_11", None)
        self.__ShoppingCart_coustomer_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ShoppingCart_coustomer_00"):
                opp_val = getattr(old_value, "ShoppingCart_coustomer_00", None)
                if opp_val == self:
                    setattr(old_value, "ShoppingCart_coustomer_00", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ShoppingCart_coustomer_00"):
                opp_val = getattr(value, "ShoppingCart_coustomer_00", None)
                setattr(value, "ShoppingCart_coustomer_00", self)

    @property
    def coustomer_order_08(self):
        return self.__coustomer_order_08
    @coustomer_order_08.setter
    def coustomer_order_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coustomer__coustomer_order_08", None)
        self.__coustomer_order_08 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coustomer_order_19"):
                    opp_val = getattr(item, "coustomer_order_19", None)
                    
                    if opp_val == self:
                        setattr(item, "coustomer_order_19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coustomer_order_19"):
                    opp_val = getattr(item, "coustomer_order_19", None)
                    
                    setattr(item, "coustomer_order_19", self)
                    



class user:

    def __init__(self, UserId: int, email: str, password: str, loginstatus: str):
        self.UserId = UserId
        self.email = email
        self.password = password
        self.loginstatus = loginstatus
        
        pass
    @property
    def UserId(self):
        return self.__UserId
    @UserId.setter
    def UserId(self, UserId: int):
        self.__UserId = UserId

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def loginstatus(self):
        return self.__loginstatus
    @loginstatus.setter
    def loginstatus(self, loginstatus: str):
        self.__loginstatus = loginstatus

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

