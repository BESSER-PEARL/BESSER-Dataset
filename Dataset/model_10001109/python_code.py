from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Models_ShippingType(Enum):
    pass
class Models_ShoppingCartStatus(Enum):
    pass
class Models_OrderStatus(Enum):
    pass

############################################
# Definition of Classes
############################################










class Controllers_ProductController:

    pass


class Controllers_OrderController:

    pass


class Controllers_ShoppingCartController:

    pass


class Models_ShippingInfo:

    def __init__(self, shippingid: int, shippingtype: str, shippingcost: int, shippingregionid: int, shippingInfo1: "dao_ShippingInfoDao_Interface" = None, order_shippinginfo_125: "Models_Order" = None):
        self.shippingid = shippingid
        self.shippingtype = shippingtype
        self.shippingcost = shippingcost
        self.shippingregionid = shippingregionid
        self.shippingInfo1 = shippingInfo1
        self.order_shippinginfo_125 = order_shippinginfo_125
        
        pass
    @property
    def shippingtype(self):
        return self.__shippingtype
    @shippingtype.setter
    def shippingtype(self, shippingtype: str):
        self.__shippingtype = shippingtype

    @property
    def shippingregionid(self):
        return self.__shippingregionid
    @shippingregionid.setter
    def shippingregionid(self, shippingregionid: int):
        self.__shippingregionid = shippingregionid

    @property
    def shippingid(self):
        return self.__shippingid
    @shippingid.setter
    def shippingid(self, shippingid: int):
        self.__shippingid = shippingid

    @property
    def shippingcost(self):
        return self.__shippingcost
    @shippingcost.setter
    def shippingcost(self, shippingcost: int):
        self.__shippingcost = shippingcost

    @property
    def shippingInfo1(self):
        return self.__shippingInfo1
    @shippingInfo1.setter
    def shippingInfo1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_ShippingInfo__shippingInfo1", None)
        self.__shippingInfo1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shippingInfo0"):
                opp_val = getattr(old_value, "shippingInfo0", None)
                if opp_val == self:
                    setattr(old_value, "shippingInfo0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shippingInfo0"):
                opp_val = getattr(value, "shippingInfo0", None)
                setattr(value, "shippingInfo0", self)

    @property
    def order_shippinginfo_125(self):
        return self.__order_shippinginfo_125
    @order_shippinginfo_125.setter
    def order_shippinginfo_125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_ShippingInfo__order_shippinginfo_125", None)
        self.__order_shippinginfo_125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_shippinginfo_024"):
                opp_val = getattr(old_value, "order_shippinginfo_024", None)
                if opp_val == self:
                    setattr(old_value, "order_shippinginfo_024", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_shippinginfo_024"):
                opp_val = getattr(value, "order_shippinginfo_024", None)
                setattr(value, "order_shippinginfo_024", self)



class Models_cartItem:

    def __init__(self, name: str, cartId: int, quantity: int, unitcost: float, subtotal: float, deleted: bool, cartItemDao5: "dao_CartItemDao_Interface" = None, ShoppingCart_cartitem_121: "Models_ShoppingCart" = None, cartitem_ProLocal_022: "Models_Product" = None):
        self.name = name
        self.cartId = cartId
        self.quantity = quantity
        self.unitcost = unitcost
        self.subtotal = subtotal
        self.deleted = deleted
        self.cartItemDao5 = cartItemDao5
        self.ShoppingCart_cartitem_121 = ShoppingCart_cartitem_121
        self.cartitem_ProLocal_022 = cartitem_ProLocal_022
        
        pass
    @property
    def deleted(self):
        return self.__deleted
    @deleted.setter
    def deleted(self, deleted: bool):
        self.__deleted = deleted

    @property
    def cartId(self):
        return self.__cartId
    @cartId.setter
    def cartId(self, cartId: int):
        self.__cartId = cartId

    @property
    def subtotal(self):
        return self.__subtotal
    @subtotal.setter
    def subtotal(self, subtotal: float):
        self.__subtotal = subtotal

    @property
    def unitcost(self):
        return self.__unitcost
    @unitcost.setter
    def unitcost(self, unitcost: float):
        self.__unitcost = unitcost

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ShoppingCart_cartitem_121(self):
        return self.__ShoppingCart_cartitem_121
    @ShoppingCart_cartitem_121.setter
    def ShoppingCart_cartitem_121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_cartItem__ShoppingCart_cartitem_121", None)
        self.__ShoppingCart_cartitem_121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ShoppingCart_cartitem_020"):
                opp_val = getattr(old_value, "ShoppingCart_cartitem_020", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ShoppingCart_cartitem_020"):
                opp_val = getattr(value, "ShoppingCart_cartitem_020", None)
                if opp_val is None:
                    setattr(value, "ShoppingCart_cartitem_020", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cartitem_ProLocal_022(self):
        return self.__cartitem_ProLocal_022
    @cartitem_ProLocal_022.setter
    def cartitem_ProLocal_022(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_cartItem__cartitem_ProLocal_022", None)
        self.__cartitem_ProLocal_022 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cartitem_ProLocal_123"):
                opp_val = getattr(old_value, "cartitem_ProLocal_123", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cartitem_ProLocal_123"):
                opp_val = getattr(value, "cartitem_ProLocal_123", None)
                if opp_val is None:
                    setattr(value, "cartitem_ProLocal_123", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cartItemDao5(self):
        return self.__cartItemDao5
    @cartItemDao5.setter
    def cartItemDao5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_cartItem__cartItemDao5", None)
        self.__cartItemDao5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cartItem4"):
                opp_val = getattr(old_value, "cartItem4", None)
                if opp_val == self:
                    setattr(old_value, "cartItem4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cartItem4"):
                opp_val = getattr(value, "cartItem4", None)
                setattr(value, "cartItem4", self)



class Models_Product:

    def __init__(self, productid: int, productname: str, price: float, imagefilename: str, quantity: int, orderDetail_ProLocal_119: "Models_LineItem" = None, cartitem_ProLocal_123: set["Models_cartItem"] = None, productDao26: "dao_ProductDao_Interface" = None):
        self.productid = productid
        self.productname = productname
        self.price = price
        self.imagefilename = imagefilename
        self.quantity = quantity
        self.orderDetail_ProLocal_119 = orderDetail_ProLocal_119
        self.cartitem_ProLocal_123 = cartitem_ProLocal_123 if cartitem_ProLocal_123 is not None else set()
        self.productDao26 = productDao26
        
        pass
    @property
    def imagefilename(self):
        return self.__imagefilename
    @imagefilename.setter
    def imagefilename(self, imagefilename: str):
        self.__imagefilename = imagefilename

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def productname(self):
        return self.__productname
    @productname.setter
    def productname(self, productname: str):
        self.__productname = productname

    @property
    def productid(self):
        return self.__productid
    @productid.setter
    def productid(self, productid: int):
        self.__productid = productid

    @property
    def orderDetail_ProLocal_119(self):
        return self.__orderDetail_ProLocal_119
    @orderDetail_ProLocal_119.setter
    def orderDetail_ProLocal_119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_Product__orderDetail_ProLocal_119", None)
        self.__orderDetail_ProLocal_119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderDetail_ProLocal_018"):
                opp_val = getattr(old_value, "orderDetail_ProLocal_018", None)
                if opp_val == self:
                    setattr(old_value, "orderDetail_ProLocal_018", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderDetail_ProLocal_018"):
                opp_val = getattr(value, "orderDetail_ProLocal_018", None)
                setattr(value, "orderDetail_ProLocal_018", self)

    @property
    def cartitem_ProLocal_123(self):
        return self.__cartitem_ProLocal_123
    @cartitem_ProLocal_123.setter
    def cartitem_ProLocal_123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_Product__cartitem_ProLocal_123", None)
        self.__cartitem_ProLocal_123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cartitem_ProLocal_022"):
                    opp_val = getattr(item, "cartitem_ProLocal_022", None)
                    
                    if opp_val == self:
                        setattr(item, "cartitem_ProLocal_022", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cartitem_ProLocal_022"):
                    opp_val = getattr(item, "cartitem_ProLocal_022", None)
                    
                    setattr(item, "cartitem_ProLocal_022", self)
                    

    @property
    def productDao26(self):
        return self.__productDao26
    @productDao26.setter
    def productDao26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_Product__productDao26", None)
        self.__productDao26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product27"):
                opp_val = getattr(old_value, "product27", None)
                if opp_val == self:
                    setattr(old_value, "product27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product27"):
                opp_val = getattr(value, "product27", None)
                setattr(value, "product27", self)



class Models_LoginLog:

    def __init__(self, id: int, user_id: int, isLogin: bool, lastLoginDate: date, user16: "Models_User" = None):
        self.id = id
        self.user_id = user_id
        self.isLogin = isLogin
        self.lastLoginDate = lastLoginDate
        self.user16 = user16
        
        pass
    @property
    def isLogin(self):
        return self.__isLogin
    @isLogin.setter
    def isLogin(self, isLogin: bool):
        self.__isLogin = isLogin

    @property
    def lastLoginDate(self):
        return self.__lastLoginDate
    @lastLoginDate.setter
    def lastLoginDate(self, lastLoginDate: date):
        self.__lastLoginDate = lastLoginDate

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def user16(self):
        return self.__user16
    @user16.setter
    def user16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_LoginLog__user16", None)
        self.__user16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "loginLog17"):
                opp_val = getattr(old_value, "loginLog17", None)
                if opp_val == self:
                    setattr(old_value, "loginLog17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "loginLog17"):
                opp_val = getattr(value, "loginLog17", None)
                setattr(value, "loginLog17", self)



class Models_User:

    def __init__(self, UserId: str, password: str, email: str, loginLog17: "Models_LoginLog" = None):
        self.UserId = UserId
        self.password = password
        self.email = email
        self.loginLog17 = loginLog17
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def UserId(self):
        return self.__UserId
    @UserId.setter
    def UserId(self, UserId: str):
        self.__UserId = UserId

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def loginLog17(self):
        return self.__loginLog17
    @loginLog17.setter
    def loginLog17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_User__loginLog17", None)
        self.__loginLog17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user16"):
                opp_val = getattr(old_value, "user16", None)
                if opp_val == self:
                    setattr(old_value, "user16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user16"):
                opp_val = getattr(value, "user16", None)
                setattr(value, "user16", self)



class Models_Order:

    def __init__(self, orderID: int, dateCreated: date, dateShipped: str, customerid: int, status: str, shippingInfoId: int, coustomer_order_113: "Models_Customer" = None, order_orderDetail_014: set["Models_LineItem"] = None, orderDao3: "dao_OrderDao_Interface" = None, order_shippinginfo_024: "Models_ShippingInfo" = None):
        self.orderID = orderID
        self.dateCreated = dateCreated
        self.dateShipped = dateShipped
        self.customerid = customerid
        self.status = status
        self.shippingInfoId = shippingInfoId
        self.coustomer_order_113 = coustomer_order_113
        self.order_orderDetail_014 = order_orderDetail_014 if order_orderDetail_014 is not None else set()
        self.orderDao3 = orderDao3
        self.order_shippinginfo_024 = order_shippinginfo_024
        
        pass
    @property
    def orderID(self):
        return self.__orderID
    @orderID.setter
    def orderID(self, orderID: int):
        self.__orderID = orderID

    @property
    def shippingInfoId(self):
        return self.__shippingInfoId
    @shippingInfoId.setter
    def shippingInfoId(self, shippingInfoId: int):
        self.__shippingInfoId = shippingInfoId

    @property
    def customerid(self):
        return self.__customerid
    @customerid.setter
    def customerid(self, customerid: int):
        self.__customerid = customerid

    @property
    def dateCreated(self):
        return self.__dateCreated
    @dateCreated.setter
    def dateCreated(self, dateCreated: date):
        self.__dateCreated = dateCreated

    @property
    def dateShipped(self):
        return self.__dateShipped
    @dateShipped.setter
    def dateShipped(self, dateShipped: str):
        self.__dateShipped = dateShipped

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def orderDao3(self):
        return self.__orderDao3
    @orderDao3.setter
    def orderDao3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_Order__orderDao3", None)
        self.__orderDao3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order2"):
                opp_val = getattr(old_value, "order2", None)
                if opp_val == self:
                    setattr(old_value, "order2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order2"):
                opp_val = getattr(value, "order2", None)
                setattr(value, "order2", self)

    @property
    def order_shippinginfo_024(self):
        return self.__order_shippinginfo_024
    @order_shippinginfo_024.setter
    def order_shippinginfo_024(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_Order__order_shippinginfo_024", None)
        self.__order_shippinginfo_024 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_shippinginfo_125"):
                opp_val = getattr(old_value, "order_shippinginfo_125", None)
                if opp_val == self:
                    setattr(old_value, "order_shippinginfo_125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_shippinginfo_125"):
                opp_val = getattr(value, "order_shippinginfo_125", None)
                setattr(value, "order_shippinginfo_125", self)

    @property
    def coustomer_order_113(self):
        return self.__coustomer_order_113
    @coustomer_order_113.setter
    def coustomer_order_113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_Order__coustomer_order_113", None)
        self.__coustomer_order_113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coustomer_order_012"):
                opp_val = getattr(old_value, "coustomer_order_012", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coustomer_order_012"):
                opp_val = getattr(value, "coustomer_order_012", None)
                if opp_val is None:
                    setattr(value, "coustomer_order_012", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order_orderDetail_014(self):
        return self.__order_orderDetail_014
    @order_orderDetail_014.setter
    def order_orderDetail_014(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_Order__order_orderDetail_014", None)
        self.__order_orderDetail_014 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order_orderDetail_115"):
                    opp_val = getattr(item, "order_orderDetail_115", None)
                    
                    if opp_val == self:
                        setattr(item, "order_orderDetail_115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order_orderDetail_115"):
                    opp_val = getattr(item, "order_orderDetail_115", None)
                    
                    setattr(item, "order_orderDetail_115", self)
                    



class Models_LineItem:

    def __init__(self, orderId: int, productid: int, productname: str, quantity: int, unitcost: float, subtotal: float, order_orderDetail_115: "Models_Order" = None, orderDetail_ProLocal_018: "Models_Product" = None, lineItemDao6: "dao_LineItemDao_Interface" = None):
        self.orderId = orderId
        self.productid = productid
        self.productname = productname
        self.quantity = quantity
        self.unitcost = unitcost
        self.subtotal = subtotal
        self.order_orderDetail_115 = order_orderDetail_115
        self.orderDetail_ProLocal_018 = orderDetail_ProLocal_018
        self.lineItemDao6 = lineItemDao6
        
        pass
    @property
    def productid(self):
        return self.__productid
    @productid.setter
    def productid(self, productid: int):
        self.__productid = productid

    @property
    def orderId(self):
        return self.__orderId
    @orderId.setter
    def orderId(self, orderId: int):
        self.__orderId = orderId

    @property
    def unitcost(self):
        return self.__unitcost
    @unitcost.setter
    def unitcost(self, unitcost: float):
        self.__unitcost = unitcost

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def subtotal(self):
        return self.__subtotal
    @subtotal.setter
    def subtotal(self, subtotal: float):
        self.__subtotal = subtotal

    @property
    def productname(self):
        return self.__productname
    @productname.setter
    def productname(self, productname: str):
        self.__productname = productname

    @property
    def order_orderDetail_115(self):
        return self.__order_orderDetail_115
    @order_orderDetail_115.setter
    def order_orderDetail_115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_LineItem__order_orderDetail_115", None)
        self.__order_orderDetail_115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_orderDetail_014"):
                opp_val = getattr(old_value, "order_orderDetail_014", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_orderDetail_014"):
                opp_val = getattr(value, "order_orderDetail_014", None)
                if opp_val is None:
                    setattr(value, "order_orderDetail_014", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lineItemDao6(self):
        return self.__lineItemDao6
    @lineItemDao6.setter
    def lineItemDao6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_LineItem__lineItemDao6", None)
        self.__lineItemDao6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LineItem7"):
                opp_val = getattr(old_value, "LineItem7", None)
                if opp_val == self:
                    setattr(old_value, "LineItem7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LineItem7"):
                opp_val = getattr(value, "LineItem7", None)
                setattr(value, "LineItem7", self)

    @property
    def orderDetail_ProLocal_018(self):
        return self.__orderDetail_ProLocal_018
    @orderDetail_ProLocal_018.setter
    def orderDetail_ProLocal_018(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_LineItem__orderDetail_ProLocal_018", None)
        self.__orderDetail_ProLocal_018 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderDetail_ProLocal_119"):
                opp_val = getattr(old_value, "orderDetail_ProLocal_119", None)
                if opp_val == self:
                    setattr(old_value, "orderDetail_ProLocal_119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderDetail_ProLocal_119"):
                opp_val = getattr(value, "orderDetail_ProLocal_119", None)
                setattr(value, "orderDetail_ProLocal_119", self)



class Models_Customer:

    def __init__(self, coustomername: str, address: str, phoneno: int, creditcardinfo: str, shippinginfo: str, deleted: bool, coustomer_order_012: set["Models_Order"] = None, ShoppingCart_coustomer_111: "Models_ShoppingCart" = None, customerDao28: "dao_CustomerDao_Interface" = None):
        self.coustomername = coustomername
        self.address = address
        self.phoneno = phoneno
        self.creditcardinfo = creditcardinfo
        self.shippinginfo = shippinginfo
        self.deleted = deleted
        self.coustomer_order_012 = coustomer_order_012 if coustomer_order_012 is not None else set()
        self.ShoppingCart_coustomer_111 = ShoppingCart_coustomer_111
        self.customerDao28 = customerDao28
        
        pass
    @property
    def coustomername(self):
        return self.__coustomername
    @coustomername.setter
    def coustomername(self, coustomername: str):
        self.__coustomername = coustomername

    @property
    def deleted(self):
        return self.__deleted
    @deleted.setter
    def deleted(self, deleted: bool):
        self.__deleted = deleted

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def phoneno(self):
        return self.__phoneno
    @phoneno.setter
    def phoneno(self, phoneno: int):
        self.__phoneno = phoneno

    @property
    def shippinginfo(self):
        return self.__shippinginfo
    @shippinginfo.setter
    def shippinginfo(self, shippinginfo: str):
        self.__shippinginfo = shippinginfo

    @property
    def creditcardinfo(self):
        return self.__creditcardinfo
    @creditcardinfo.setter
    def creditcardinfo(self, creditcardinfo: str):
        self.__creditcardinfo = creditcardinfo

    @property
    def customerDao28(self):
        return self.__customerDao28
    @customerDao28.setter
    def customerDao28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_Customer__customerDao28", None)
        self.__customerDao28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer29"):
                opp_val = getattr(old_value, "customer29", None)
                if opp_val == self:
                    setattr(old_value, "customer29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer29"):
                opp_val = getattr(value, "customer29", None)
                setattr(value, "customer29", self)

    @property
    def coustomer_order_012(self):
        return self.__coustomer_order_012
    @coustomer_order_012.setter
    def coustomer_order_012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_Customer__coustomer_order_012", None)
        self.__coustomer_order_012 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coustomer_order_113"):
                    opp_val = getattr(item, "coustomer_order_113", None)
                    
                    if opp_val == self:
                        setattr(item, "coustomer_order_113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coustomer_order_113"):
                    opp_val = getattr(item, "coustomer_order_113", None)
                    
                    setattr(item, "coustomer_order_113", self)
                    

    @property
    def ShoppingCart_coustomer_111(self):
        return self.__ShoppingCart_coustomer_111
    @ShoppingCart_coustomer_111.setter
    def ShoppingCart_coustomer_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_Customer__ShoppingCart_coustomer_111", None)
        self.__ShoppingCart_coustomer_111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ShoppingCart_coustomer_010"):
                opp_val = getattr(old_value, "ShoppingCart_coustomer_010", None)
                if opp_val == self:
                    setattr(old_value, "ShoppingCart_coustomer_010", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ShoppingCart_coustomer_010"):
                opp_val = getattr(value, "ShoppingCart_coustomer_010", None)
                setattr(value, "ShoppingCart_coustomer_010", self)



class Models_ShoppingCart:

    def __init__(self, cartId: int, customerId: int, dateAdded: int, status: int, deleted: bool, shoppingCartDao8: "dao_ShoppingCartDao_Interface" = None, ShoppingCart_coustomer_010: "Models_Customer" = None, ShoppingCart_cartitem_020: set["Models_cartItem"] = None):
        self.cartId = cartId
        self.customerId = customerId
        self.dateAdded = dateAdded
        self.status = status
        self.deleted = deleted
        self.shoppingCartDao8 = shoppingCartDao8
        self.ShoppingCart_coustomer_010 = ShoppingCart_coustomer_010
        self.ShoppingCart_cartitem_020 = ShoppingCart_cartitem_020 if ShoppingCart_cartitem_020 is not None else set()
        
        pass
    @property
    def customerId(self):
        return self.__customerId
    @customerId.setter
    def customerId(self, customerId: int):
        self.__customerId = customerId

    @property
    def deleted(self):
        return self.__deleted
    @deleted.setter
    def deleted(self, deleted: bool):
        self.__deleted = deleted

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: int):
        self.__status = status

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
    def ShoppingCart_cartitem_020(self):
        return self.__ShoppingCart_cartitem_020
    @ShoppingCart_cartitem_020.setter
    def ShoppingCart_cartitem_020(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_ShoppingCart__ShoppingCart_cartitem_020", None)
        self.__ShoppingCart_cartitem_020 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ShoppingCart_cartitem_121"):
                    opp_val = getattr(item, "ShoppingCart_cartitem_121", None)
                    
                    if opp_val == self:
                        setattr(item, "ShoppingCart_cartitem_121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ShoppingCart_cartitem_121"):
                    opp_val = getattr(item, "ShoppingCart_cartitem_121", None)
                    
                    setattr(item, "ShoppingCart_cartitem_121", self)
                    

    @property
    def shoppingCartDao8(self):
        return self.__shoppingCartDao8
    @shoppingCartDao8.setter
    def shoppingCartDao8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_ShoppingCart__shoppingCartDao8", None)
        self.__shoppingCartDao8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart9"):
                opp_val = getattr(old_value, "shoppingCart9", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart9"):
                opp_val = getattr(value, "shoppingCart9", None)
                setattr(value, "shoppingCart9", self)

    @property
    def ShoppingCart_coustomer_010(self):
        return self.__ShoppingCart_coustomer_010
    @ShoppingCart_coustomer_010.setter
    def ShoppingCart_coustomer_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Models_ShoppingCart__ShoppingCart_coustomer_010", None)
        self.__ShoppingCart_coustomer_010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ShoppingCart_coustomer_111"):
                opp_val = getattr(old_value, "ShoppingCart_coustomer_111", None)
                if opp_val == self:
                    setattr(old_value, "ShoppingCart_coustomer_111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ShoppingCart_coustomer_111"):
                opp_val = getattr(value, "ShoppingCart_coustomer_111", None)
                setattr(value, "ShoppingCart_coustomer_111", self)



class dao_ShoppingCartDao_Interface:

    pass


class dao_OrderDao_Interface:

    pass


class dao_CartItemDao_Interface:

    pass


class dao_ShippingInfoDao_Interface:

    pass


class dao_LineItemDao_Interface:

    pass


class dao_CustomerDao_Interface:

    pass


class dao_ProductDao_Interface:

    pass
