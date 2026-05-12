from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Shopping_Interface:

    pass


class Address:

    def __init__(self, street: str, city: str, state: str, country: str, postalcode: str, customerInfo11: "CustomerInfo" = None):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.postalcode = postalcode
        self.customerInfo11 = customerInfo11
        
        pass
    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def postalcode(self):
        return self.__postalcode
    @postalcode.setter
    def postalcode(self, postalcode: str):
        self.__postalcode = postalcode

    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def customerInfo11(self):
        return self.__customerInfo11
    @customerInfo11.setter
    def customerInfo11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Address__customerInfo11", None)
        self.__customerInfo11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "address10"):
                opp_val = getattr(old_value, "address10", None)
                if opp_val == self:
                    setattr(old_value, "address10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "address10"):
                opp_val = getattr(value, "address10", None)
                setattr(value, "address10", self)



class Electronic:

    def __init__(self, brand: str):
        self.brand = brand
        
        pass
    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand: str):
        self.__brand = brand



class Clothes:

    def __init__(self, typeofclothe: str, color: str):
        self.typeofclothe = typeofclothe
        self.color = color
        
        pass
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def typeofclothe(self):
        return self.__typeofclothe
    @typeofclothe.setter
    def typeofclothe(self, typeofclothe: str):
        self.__typeofclothe = typeofclothe



class payment:

    def __init__(self, cardID: int, amount: int, order9: "Order" = None):
        self.cardID = cardID
        self.amount = amount
        self.order9 = order9
        
        pass
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

    @property
    def cardID(self):
        return self.__cardID
    @cardID.setter
    def cardID(self, cardID: int):
        self.__cardID = cardID

    @property
    def order9(self):
        return self.__order9
    @order9.setter
    def order9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_payment__order9", None)
        self.__order9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment8"):
                opp_val = getattr(old_value, "payment8", None)
                if opp_val == self:
                    setattr(old_value, "payment8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment8"):
                opp_val = getattr(value, "payment8", None)
                setattr(value, "payment8", self)



class ShippingCart:

    def __init__(self, productID: int, cartID: int, quantity: int, dateAdded: int, customerInfo7: "CustomerInfo" = None):
        self.productID = productID
        self.cartID = cartID
        self.quantity = quantity
        self.dateAdded = dateAdded
        self.customerInfo7 = customerInfo7
        
        pass
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
    def productID(self):
        return self.__productID
    @productID.setter
    def productID(self, productID: int):
        self.__productID = productID

    @property
    def cartID(self):
        return self.__cartID
    @cartID.setter
    def cartID(self, cartID: int):
        self.__cartID = cartID

    @property
    def customerInfo7(self):
        return self.__customerInfo7
    @customerInfo7.setter
    def customerInfo7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShippingCart__customerInfo7", None)
        self.__customerInfo7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shippingCart6"):
                opp_val = getattr(old_value, "shippingCart6", None)
                if opp_val == self:
                    setattr(old_value, "shippingCart6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shippingCart6"):
                opp_val = getattr(value, "shippingCart6", None)
                setattr(value, "shippingCart6", self)



class Items:

    def __init__(self, itemid: int, onlineShopping1: "OnlineShopping" = None):
        self.itemid = itemid
        self.onlineShopping1 = onlineShopping1
        
        pass
    @property
    def itemid(self):
        return self.__itemid
    @itemid.setter
    def itemid(self, itemid: int):
        self.__itemid = itemid

    @property
    def onlineShopping1(self):
        return self.__onlineShopping1
    @onlineShopping1.setter
    def onlineShopping1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Items__onlineShopping1", None)
        self.__onlineShopping1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items0"):
                opp_val = getattr(old_value, "items0", None)
                if opp_val == self:
                    setattr(old_value, "items0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items0"):
                opp_val = getattr(value, "items0", None)
                setattr(value, "items0", self)



class Order:

    def __init__(self, Orderid: int, datecreated: int, shippinddate: int, customername: str, customerid: int, statues: str, shippingid: int, onlineShopping3: "OnlineShopping" = None, payment8: "payment" = None):
        self.Orderid = Orderid
        self.datecreated = datecreated
        self.shippinddate = shippinddate
        self.customername = customername
        self.customerid = customerid
        self.statues = statues
        self.shippingid = shippingid
        self.onlineShopping3 = onlineShopping3
        self.payment8 = payment8
        
        pass
    @property
    def datecreated(self):
        return self.__datecreated
    @datecreated.setter
    def datecreated(self, datecreated: int):
        self.__datecreated = datecreated

    @property
    def shippinddate(self):
        return self.__shippinddate
    @shippinddate.setter
    def shippinddate(self, shippinddate: int):
        self.__shippinddate = shippinddate

    @property
    def customername(self):
        return self.__customername
    @customername.setter
    def customername(self, customername: str):
        self.__customername = customername

    @property
    def statues(self):
        return self.__statues
    @statues.setter
    def statues(self, statues: str):
        self.__statues = statues

    @property
    def Orderid(self):
        return self.__Orderid
    @Orderid.setter
    def Orderid(self, Orderid: int):
        self.__Orderid = Orderid

    @property
    def shippingid(self):
        return self.__shippingid
    @shippingid.setter
    def shippingid(self, shippingid: int):
        self.__shippingid = shippingid

    @property
    def customerid(self):
        return self.__customerid
    @customerid.setter
    def customerid(self, customerid: int):
        self.__customerid = customerid

    @property
    def onlineShopping3(self):
        return self.__onlineShopping3
    @onlineShopping3.setter
    def onlineShopping3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__onlineShopping3", None)
        self.__onlineShopping3 = value
        
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
    def payment8(self):
        return self.__payment8
    @payment8.setter
    def payment8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment8", None)
        self.__payment8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order9"):
                opp_val = getattr(old_value, "order9", None)
                if opp_val == self:
                    setattr(old_value, "order9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order9"):
                opp_val = getattr(value, "order9", None)
                setattr(value, "order9", self)



class CustomerInfo:

    def __init__(self, Cname: str, Cid: int, password: str, shippingaddress: str, billingaddress: str, onlineShopping5: "OnlineShopping" = None, shippingCart6: "ShippingCart" = None, address10: "Address" = None):
        self.Cname = Cname
        self.Cid = Cid
        self.password = password
        self.shippingaddress = shippingaddress
        self.billingaddress = billingaddress
        self.onlineShopping5 = onlineShopping5
        self.shippingCart6 = shippingCart6
        self.address10 = address10
        
        pass
    @property
    def shippingaddress(self):
        return self.__shippingaddress
    @shippingaddress.setter
    def shippingaddress(self, shippingaddress: str):
        self.__shippingaddress = shippingaddress

    @property
    def Cname(self):
        return self.__Cname
    @Cname.setter
    def Cname(self, Cname: str):
        self.__Cname = Cname

    @property
    def billingaddress(self):
        return self.__billingaddress
    @billingaddress.setter
    def billingaddress(self, billingaddress: str):
        self.__billingaddress = billingaddress

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def Cid(self):
        return self.__Cid
    @Cid.setter
    def Cid(self, Cid: int):
        self.__Cid = Cid

    @property
    def shippingCart6(self):
        return self.__shippingCart6
    @shippingCart6.setter
    def shippingCart6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CustomerInfo__shippingCart6", None)
        self.__shippingCart6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customerInfo7"):
                opp_val = getattr(old_value, "customerInfo7", None)
                if opp_val == self:
                    setattr(old_value, "customerInfo7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customerInfo7"):
                opp_val = getattr(value, "customerInfo7", None)
                setattr(value, "customerInfo7", self)

    @property
    def onlineShopping5(self):
        return self.__onlineShopping5
    @onlineShopping5.setter
    def onlineShopping5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CustomerInfo__onlineShopping5", None)
        self.__onlineShopping5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customerInfo4"):
                opp_val = getattr(old_value, "customerInfo4", None)
                if opp_val == self:
                    setattr(old_value, "customerInfo4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customerInfo4"):
                opp_val = getattr(value, "customerInfo4", None)
                setattr(value, "customerInfo4", self)

    @property
    def address10(self):
        return self.__address10
    @address10.setter
    def address10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CustomerInfo__address10", None)
        self.__address10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customerInfo11"):
                opp_val = getattr(old_value, "customerInfo11", None)
                if opp_val == self:
                    setattr(old_value, "customerInfo11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customerInfo11"):
                opp_val = getattr(value, "customerInfo11", None)
                setattr(value, "customerInfo11", self)



class RetailStore:

    pass


class OnlineShopping:

    pass
