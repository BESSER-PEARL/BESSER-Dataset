from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class User:

    def __init__(self, userId: int, product4: set["Product"] = None):
        self.userId = userId
        self.product4 = product4 if product4 is not None else set()
        
        pass
    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: int):
        self.__userId = userId

    @property
    def product4(self):
        return self.__product4
    @product4.setter
    def product4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__product4", None)
        self.__product4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user5"):
                    opp_val = getattr(item, "user5", None)
                    
                    if opp_val == self:
                        setattr(item, "user5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user5"):
                    opp_val = getattr(item, "user5", None)
                    
                    setattr(item, "user5", self)
                    



class Cart:

    pass


class Appliances:

    pass


class Electronics:

    pass


class Ornaments:

    def __init__(self, Name: str):
        self.Name = Name
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name



class Payment_Interface:

    pass


class CreditCardPayment:

    pass


class DebitCardPayment:

    pass


class PaymentFactory:

    pass


class Seller:

    def __init__(self, name: str, sellerId: str, rating: str, product7: "Product" = None):
        self.name = name
        self.sellerId = sellerId
        self.rating = rating
        self.product7 = product7
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sellerId(self):
        return self.__sellerId
    @sellerId.setter
    def sellerId(self, sellerId: str):
        self.__sellerId = sellerId

    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def rating(self, rating: str):
        self.__rating = rating

    @property
    def product7(self):
        return self.__product7
    @product7.setter
    def product7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Seller__product7", None)
        self.__product7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seller6"):
                opp_val = getattr(old_value, "seller6", None)
                if opp_val == self:
                    setattr(old_value, "seller6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seller6"):
                opp_val = getattr(value, "seller6", None)
                setattr(value, "seller6", self)



class ShippingInfo:

    def __init__(self, estimatedDeliveryDate: str, shippingCharges: int, deliveryAddress: str, deliveryType: str, order3: "Order" = None):
        self.estimatedDeliveryDate = estimatedDeliveryDate
        self.shippingCharges = shippingCharges
        self.deliveryAddress = deliveryAddress
        self.deliveryType = deliveryType
        self.order3 = order3
        
        pass
    @property
    def deliveryType(self):
        return self.__deliveryType
    @deliveryType.setter
    def deliveryType(self, deliveryType: str):
        self.__deliveryType = deliveryType

    @property
    def deliveryAddress(self):
        return self.__deliveryAddress
    @deliveryAddress.setter
    def deliveryAddress(self, deliveryAddress: str):
        self.__deliveryAddress = deliveryAddress

    @property
    def shippingCharges(self):
        return self.__shippingCharges
    @shippingCharges.setter
    def shippingCharges(self, shippingCharges: int):
        self.__shippingCharges = shippingCharges

    @property
    def estimatedDeliveryDate(self):
        return self.__estimatedDeliveryDate
    @estimatedDeliveryDate.setter
    def estimatedDeliveryDate(self, estimatedDeliveryDate: str):
        self.__estimatedDeliveryDate = estimatedDeliveryDate

    @property
    def order3(self):
        return self.__order3
    @order3.setter
    def order3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShippingInfo__order3", None)
        self.__order3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shippingInfo2"):
                opp_val = getattr(old_value, "shippingInfo2", None)
                if opp_val == self:
                    setattr(old_value, "shippingInfo2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shippingInfo2"):
                opp_val = getattr(value, "shippingInfo2", None)
                setattr(value, "shippingInfo2", self)



class ProductListHelper:

    pass


class WishList:

    pass


class Order:

    def __init__(self, orderId: int, orderedOn: str, status: str, shippingId: int, noOfItem: int, orderTotalAmount: int, deliveryDate: int, items: List_Product_, customer1: "Customer" = None, shippingInfo2: "ShippingInfo" = None, product9: set["Product"] = None):
        self.orderId = orderId
        self.orderedOn = orderedOn
        self.status = status
        self.shippingId = shippingId
        self.noOfItem = noOfItem
        self.orderTotalAmount = orderTotalAmount
        self.deliveryDate = deliveryDate
        self.items = items
        self.customer1 = customer1
        self.shippingInfo2 = shippingInfo2
        self.product9 = product9 if product9 is not None else set()
        
        pass
    @property
    def orderId(self):
        return self.__orderId
    @orderId.setter
    def orderId(self, orderId: int):
        self.__orderId = orderId

    @property
    def orderedOn(self):
        return self.__orderedOn
    @orderedOn.setter
    def orderedOn(self, orderedOn: str):
        self.__orderedOn = orderedOn

    @property
    def orderTotalAmount(self):
        return self.__orderTotalAmount
    @orderTotalAmount.setter
    def orderTotalAmount(self, orderTotalAmount: int):
        self.__orderTotalAmount = orderTotalAmount

    @property
    def items(self):
        return self.__items
    @items.setter
    def items(self, items: List_Product_):
        self.__items = items

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def noOfItem(self):
        return self.__noOfItem
    @noOfItem.setter
    def noOfItem(self, noOfItem: int):
        self.__noOfItem = noOfItem

    @property
    def shippingId(self):
        return self.__shippingId
    @shippingId.setter
    def shippingId(self, shippingId: int):
        self.__shippingId = shippingId

    @property
    def deliveryDate(self):
        return self.__deliveryDate
    @deliveryDate.setter
    def deliveryDate(self, deliveryDate: int):
        self.__deliveryDate = deliveryDate

    @property
    def product9(self):
        return self.__product9
    @product9.setter
    def product9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__product9", None)
        self.__product9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order8"):
                    opp_val = getattr(item, "order8", None)
                    
                    if opp_val == self:
                        setattr(item, "order8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order8"):
                    opp_val = getattr(item, "order8", None)
                    
                    setattr(item, "order8", self)
                    

    @property
    def shippingInfo2(self):
        return self.__shippingInfo2
    @shippingInfo2.setter
    def shippingInfo2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__shippingInfo2", None)
        self.__shippingInfo2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order3"):
                opp_val = getattr(old_value, "order3", None)
                if opp_val == self:
                    setattr(old_value, "order3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order3"):
                opp_val = getattr(value, "order3", None)
                setattr(value, "order3", self)

    @property
    def customer1(self):
        return self.__customer1
    @customer1.setter
    def customer1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer1", None)
        self.__customer1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order0"):
                opp_val = getattr(old_value, "order0", None)
                if opp_val == self:
                    setattr(old_value, "order0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order0"):
                opp_val = getattr(value, "order0", None)
                setattr(value, "order0", self)



class List_Product_:

    pass


class Product:

    def __init__(self, productId: int, productName: str, price: int, image: str, sellerInfo: Seller, description: str, rating: int, user5: "User" = None, seller6: "Seller" = None, order8: "Order" = None, wishList18: "WishList" = None, cart20: "Cart" = None):
        self.productId = productId
        self.productName = productName
        self.price = price
        self.image = image
        self.sellerInfo = sellerInfo
        self.description = description
        self.rating = rating
        self.user5 = user5
        self.seller6 = seller6
        self.order8 = order8
        self.wishList18 = wishList18
        self.cart20 = cart20
        
        pass
    @property
    def sellerInfo(self):
        return self.__sellerInfo
    @sellerInfo.setter
    def sellerInfo(self, sellerInfo: Seller):
        self.__sellerInfo = sellerInfo

    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def rating(self, rating: int):
        self.__rating = rating

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
    def price(self, price: int):
        self.__price = price

    @property
    def productName(self):
        return self.__productName
    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: int):
        self.__productId = productId

    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def order8(self):
        return self.__order8
    @order8.setter
    def order8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__order8", None)
        self.__order8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product9"):
                opp_val = getattr(old_value, "product9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product9"):
                opp_val = getattr(value, "product9", None)
                if opp_val is None:
                    setattr(value, "product9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def seller6(self):
        return self.__seller6
    @seller6.setter
    def seller6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__seller6", None)
        self.__seller6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product7"):
                opp_val = getattr(old_value, "product7", None)
                if opp_val == self:
                    setattr(old_value, "product7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product7"):
                opp_val = getattr(value, "product7", None)
                setattr(value, "product7", self)

    @property
    def wishList18(self):
        return self.__wishList18
    @wishList18.setter
    def wishList18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__wishList18", None)
        self.__wishList18 = value
        
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
    def user5(self):
        return self.__user5
    @user5.setter
    def user5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__user5", None)
        self.__user5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product4"):
                opp_val = getattr(old_value, "product4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product4"):
                opp_val = getattr(value, "product4", None)
                if opp_val is None:
                    setattr(value, "product4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cart20(self):
        return self.__cart20
    @cart20.setter
    def cart20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__cart20", None)
        self.__cart20 = value
        
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



class Customer:

    def __init__(self, user_name: str, firstName: str, lastName: str, phoneNo: int, address: str, order0: "Order" = None, cart10: "Cart" = None, wishList12: "WishList" = None):
        self.user_name = user_name
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNo = phoneNo
        self.address = address
        self.order0 = order0
        self.cart10 = cart10
        self.wishList12 = wishList12
        
        pass
    @property
    def firstName(self):
        return self.__firstName
    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def lastName(self):
        return self.__lastName
    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def phoneNo(self):
        return self.__phoneNo
    @phoneNo.setter
    def phoneNo(self, phoneNo: int):
        self.__phoneNo = phoneNo

    @property
    def user_name(self):
        return self.__user_name
    @user_name.setter
    def user_name(self, user_name: str):
        self.__user_name = user_name

    @property
    def wishList12(self):
        return self.__wishList12
    @wishList12.setter
    def wishList12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__wishList12", None)
        self.__wishList12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer13"):
                opp_val = getattr(old_value, "customer13", None)
                if opp_val == self:
                    setattr(old_value, "customer13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer13"):
                opp_val = getattr(value, "customer13", None)
                setattr(value, "customer13", self)

    @property
    def order0(self):
        return self.__order0
    @order0.setter
    def order0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__order0", None)
        self.__order0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer1"):
                opp_val = getattr(old_value, "customer1", None)
                if opp_val == self:
                    setattr(old_value, "customer1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer1"):
                opp_val = getattr(value, "customer1", None)
                setattr(value, "customer1", self)

    @property
    def cart10(self):
        return self.__cart10
    @cart10.setter
    def cart10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__cart10", None)
        self.__cart10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer11"):
                opp_val = getattr(old_value, "customer11", None)
                if opp_val == self:
                    setattr(old_value, "customer11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer11"):
                opp_val = getattr(value, "customer11", None)
                setattr(value, "customer11", self)



class Guest:

    pass
