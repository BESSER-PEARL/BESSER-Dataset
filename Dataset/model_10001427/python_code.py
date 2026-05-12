from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class login_status(Enum):
    pass

############################################
# Definition of Classes
############################################










class Payment:

    def __init__(self, Payment_id: str, Payment_type: str, Payment_method: int, order11: "order" = None):
        self.Payment_id = Payment_id
        self.Payment_type = Payment_type
        self.Payment_method = Payment_method
        self.order11 = order11
        
        pass
    @property
    def Payment_method(self):
        return self.__Payment_method
    @Payment_method.setter
    def Payment_method(self, Payment_method: int):
        self.__Payment_method = Payment_method

    @property
    def Payment_id(self):
        return self.__Payment_id
    @Payment_id.setter
    def Payment_id(self, Payment_id: str):
        self.__Payment_id = Payment_id

    @property
    def Payment_type(self):
        return self.__Payment_type
    @Payment_type.setter
    def Payment_type(self, Payment_type: str):
        self.__Payment_type = Payment_type

    @property
    def order11(self):
        return self.__order11
    @order11.setter
    def order11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order11", None)
        self.__order11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment10"):
                opp_val = getattr(old_value, "payment10", None)
                if opp_val == self:
                    setattr(old_value, "payment10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment10"):
                opp_val = getattr(value, "payment10", None)
                setattr(value, "payment10", self)



class shippinginfo:

    def __init__(self, shipping_id: str, shipping_type: str, shipping_cost: int, shipping_Address: str, shipping_date: date, order_shippinginfo_19: "order" = None):
        self.shipping_id = shipping_id
        self.shipping_type = shipping_type
        self.shipping_cost = shipping_cost
        self.shipping_Address = shipping_Address
        self.shipping_date = shipping_date
        self.order_shippinginfo_19 = order_shippinginfo_19
        
        pass
    @property
    def shipping_type(self):
        return self.__shipping_type
    @shipping_type.setter
    def shipping_type(self, shipping_type: str):
        self.__shipping_type = shipping_type

    @property
    def shipping_cost(self):
        return self.__shipping_cost
    @shipping_cost.setter
    def shipping_cost(self, shipping_cost: int):
        self.__shipping_cost = shipping_cost

    @property
    def shipping_Address(self):
        return self.__shipping_Address
    @shipping_Address.setter
    def shipping_Address(self, shipping_Address: str):
        self.__shipping_Address = shipping_Address

    @property
    def shipping_id(self):
        return self.__shipping_id
    @shipping_id.setter
    def shipping_id(self, shipping_id: str):
        self.__shipping_id = shipping_id

    @property
    def shipping_date(self):
        return self.__shipping_date
    @shipping_date.setter
    def shipping_date(self, shipping_date: date):
        self.__shipping_date = shipping_date

    @property
    def order_shippinginfo_19(self):
        return self.__order_shippinginfo_19
    @order_shippinginfo_19.setter
    def order_shippinginfo_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shippinginfo__order_shippinginfo_19", None)
        self.__order_shippinginfo_19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_shippinginfo_08"):
                opp_val = getattr(old_value, "order_shippinginfo_08", None)
                if opp_val == self:
                    setattr(old_value, "order_shippinginfo_08", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_shippinginfo_08"):
                opp_val = getattr(value, "order_shippinginfo_08", None)
                setattr(value, "order_shippinginfo_08", self)



class order:

    def __init__(self, shipping_date: date, c_name: str, status: str, shippingid: str, order_ID: int, date_created: date, coustomer_order_15: "User" = None, order_orderDetail_06: "orderDetail" = None, order_shippinginfo_08: "shippinginfo" = None, payment10: "Payment" = None):
        self.shipping_date = shipping_date
        self.c_name = c_name
        self.status = status
        self.shippingid = shippingid
        self.order_ID = order_ID
        self.date_created = date_created
        self.coustomer_order_15 = coustomer_order_15
        self.order_orderDetail_06 = order_orderDetail_06
        self.order_shippinginfo_08 = order_shippinginfo_08
        self.payment10 = payment10
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def date_created(self):
        return self.__date_created
    @date_created.setter
    def date_created(self, date_created: date):
        self.__date_created = date_created

    @property
    def shippingid(self):
        return self.__shippingid
    @shippingid.setter
    def shippingid(self, shippingid: str):
        self.__shippingid = shippingid

    @property
    def shipping_date(self):
        return self.__shipping_date
    @shipping_date.setter
    def shipping_date(self, shipping_date: date):
        self.__shipping_date = shipping_date

    @property
    def c_name(self):
        return self.__c_name
    @c_name.setter
    def c_name(self, c_name: str):
        self.__c_name = c_name

    @property
    def order_ID(self):
        return self.__order_ID
    @order_ID.setter
    def order_ID(self, order_ID: int):
        self.__order_ID = order_ID

    @property
    def order_orderDetail_06(self):
        return self.__order_orderDetail_06
    @order_orderDetail_06.setter
    def order_orderDetail_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__order_orderDetail_06", None)
        self.__order_orderDetail_06 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_orderDetail_17"):
                opp_val = getattr(old_value, "order_orderDetail_17", None)
                if opp_val == self:
                    setattr(old_value, "order_orderDetail_17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_orderDetail_17"):
                opp_val = getattr(value, "order_orderDetail_17", None)
                setattr(value, "order_orderDetail_17", self)

    @property
    def coustomer_order_15(self):
        return self.__coustomer_order_15
    @coustomer_order_15.setter
    def coustomer_order_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__coustomer_order_15", None)
        self.__coustomer_order_15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coustomer_order_04"):
                opp_val = getattr(old_value, "coustomer_order_04", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coustomer_order_04"):
                opp_val = getattr(value, "coustomer_order_04", None)
                if opp_val is None:
                    setattr(value, "coustomer_order_04", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def payment10(self):
        return self.__payment10
    @payment10.setter
    def payment10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__payment10", None)
        self.__payment10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order11"):
                opp_val = getattr(old_value, "order11", None)
                if opp_val == self:
                    setattr(old_value, "order11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order11"):
                opp_val = getattr(value, "order11", None)
                setattr(value, "order11", self)

    @property
    def order_shippinginfo_08(self):
        return self.__order_shippinginfo_08
    @order_shippinginfo_08.setter
    def order_shippinginfo_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__order_shippinginfo_08", None)
        self.__order_shippinginfo_08 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_shippinginfo_19"):
                opp_val = getattr(old_value, "order_shippinginfo_19", None)
                if opp_val == self:
                    setattr(old_value, "order_shippinginfo_19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_shippinginfo_19"):
                opp_val = getattr(value, "order_shippinginfo_19", None)
                setattr(value, "order_shippinginfo_19", self)



class orderDetail:

    def __init__(self, orderId: int, productid: int, productname: str, quantity: int, unitcost: float, subtotall: float, order_orderDetail_17: "order" = None):
        self.orderId = orderId
        self.productid = productid
        self.productname = productname
        self.quantity = quantity
        self.unitcost = unitcost
        self.subtotall = subtotall
        self.order_orderDetail_17 = order_orderDetail_17
        
        pass
    @property
    def subtotall(self):
        return self.__subtotall
    @subtotall.setter
    def subtotall(self, subtotall: float):
        self.__subtotall = subtotall

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

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
    def orderId(self):
        return self.__orderId
    @orderId.setter
    def orderId(self, orderId: int):
        self.__orderId = orderId

    @property
    def productname(self):
        return self.__productname
    @productname.setter
    def productname(self, productname: str):
        self.__productname = productname

    @property
    def order_orderDetail_17(self):
        return self.__order_orderDetail_17
    @order_orderDetail_17.setter
    def order_orderDetail_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_orderDetail__order_orderDetail_17", None)
        self.__order_orderDetail_17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_orderDetail_06"):
                opp_val = getattr(old_value, "order_orderDetail_06", None)
                if opp_val == self:
                    setattr(old_value, "order_orderDetail_06", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_orderDetail_06"):
                opp_val = getattr(value, "order_orderDetail_06", None)
                setattr(value, "order_orderDetail_06", self)



class product:

    def __init__(self, productid: int, productname: str, price: int, imagefilename: str, cartitem13: "cartitem" = None):
        self.productid = productid
        self.productname = productname
        self.price = price
        self.imagefilename = imagefilename
        self.cartitem13 = cartitem13
        
        pass
    @property
    def productname(self):
        return self.__productname
    @productname.setter
    def productname(self, productname: str):
        self.__productname = productname

    @property
    def imagefilename(self):
        return self.__imagefilename
    @imagefilename.setter
    def imagefilename(self, imagefilename: str):
        self.__imagefilename = imagefilename

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def productid(self):
        return self.__productid
    @productid.setter
    def productid(self, productid: int):
        self.__productid = productid

    @property
    def cartitem13(self):
        return self.__cartitem13
    @cartitem13.setter
    def cartitem13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product__cartitem13", None)
        self.__cartitem13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product212"):
                opp_val = getattr(old_value, "product212", None)
                if opp_val == self:
                    setattr(old_value, "product212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product212"):
                opp_val = getattr(value, "product212", None)
                setattr(value, "product212", self)



class cartitem:

    def __init__(self, name: str, product: int, quantity: int, unitcost: float, subtotal: float, ShoppingCart_cartitem_13: "ShoppingCart" = None, product212: "product" = None):
        self.name = name
        self.product = product
        self.quantity = quantity
        self.unitcost = unitcost
        self.subtotal = subtotal
        self.ShoppingCart_cartitem_13 = ShoppingCart_cartitem_13
        self.product212 = product212
        
        pass
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
    def unitcost(self):
        return self.__unitcost
    @unitcost.setter
    def unitcost(self, unitcost: float):
        self.__unitcost = unitcost

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def product(self):
        return self.__product
    @product.setter
    def product(self, product: int):
        self.__product = product

    @property
    def product212(self):
        return self.__product212
    @product212.setter
    def product212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cartitem__product212", None)
        self.__product212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cartitem13"):
                opp_val = getattr(old_value, "cartitem13", None)
                if opp_val == self:
                    setattr(old_value, "cartitem13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cartitem13"):
                opp_val = getattr(value, "cartitem13", None)
                setattr(value, "cartitem13", self)

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

    def __init__(self, cartId: int, productId: int, quantity: int, dateAdded: int, ShoppingCart_coustomer_00: "User" = None, ShoppingCart_cartitem_02: "cartitem" = None):
        self.cartId = cartId
        self.productId = productId
        self.quantity = quantity
        self.dateAdded = dateAdded
        self.ShoppingCart_coustomer_00 = ShoppingCart_coustomer_00
        self.ShoppingCart_cartitem_02 = ShoppingCart_cartitem_02
        
        pass
    @property
    def cartId(self):
        return self.__cartId
    @cartId.setter
    def cartId(self, cartId: int):
        self.__cartId = cartId

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: int):
        self.__productId = productId

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



class User:

    def __init__(self, User_name: str, address: str, email: str, phone_no: int, Card_info: str, shipping_info: str, ShoppingCart_coustomer_11: "ShoppingCart" = None, coustomer_order_04: set["order"] = None):
        self.User_name = User_name
        self.address = address
        self.email = email
        self.phone_no = phone_no
        self.Card_info = Card_info
        self.shipping_info = shipping_info
        self.ShoppingCart_coustomer_11 = ShoppingCart_coustomer_11
        self.coustomer_order_04 = coustomer_order_04 if coustomer_order_04 is not None else set()
        
        pass
    @property
    def phone_no(self):
        return self.__phone_no
    @phone_no.setter
    def phone_no(self, phone_no: int):
        self.__phone_no = phone_no

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def Card_info(self):
        return self.__Card_info
    @Card_info.setter
    def Card_info(self, Card_info: str):
        self.__Card_info = Card_info

    @property
    def User_name(self):
        return self.__User_name
    @User_name.setter
    def User_name(self, User_name: str):
        self.__User_name = User_name

    @property
    def shipping_info(self):
        return self.__shipping_info
    @shipping_info.setter
    def shipping_info(self, shipping_info: str):
        self.__shipping_info = shipping_info

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def coustomer_order_04(self):
        return self.__coustomer_order_04
    @coustomer_order_04.setter
    def coustomer_order_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__coustomer_order_04", None)
        self.__coustomer_order_04 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coustomer_order_15"):
                    opp_val = getattr(item, "coustomer_order_15", None)
                    
                    if opp_val == self:
                        setattr(item, "coustomer_order_15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coustomer_order_15"):
                    opp_val = getattr(item, "coustomer_order_15", None)
                    
                    setattr(item, "coustomer_order_15", self)
                    

    @property
    def ShoppingCart_coustomer_11(self):
        return self.__ShoppingCart_coustomer_11
    @ShoppingCart_coustomer_11.setter
    def ShoppingCart_coustomer_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__ShoppingCart_coustomer_11", None)
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



class Login:

    def __init__(self, UserId: str, password: str, login_status: str):
        self.UserId = UserId
        self.password = password
        self.login_status = login_status
        
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
    def login_status(self):
        return self.__login_status
    @login_status.setter
    def login_status(self, login_status: str):
        self.__login_status = login_status

