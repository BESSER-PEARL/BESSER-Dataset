from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass
class CustomerType(Enum):
    pass

############################################
# Definition of Classes
############################################










class Customer:

    def __init__(self, DiscountSlab_list_: PurchaseAmountSlab, type: CustomerType, shoppingCart: ShoppingCart, p0: set["Payment"] = None, customer3: "PremiumCustomer" = None, order4: set["Order"] = None, customerHandler16: "CustomerHandler" = None, shoppingCart219: "ShoppingCart" = None, shoppingCart221: "ShoppingCart" = None, customer22: "Customer" = None, customer23: "Customer" = None, purchaseAmountSlab25: "PurchaseAmountSlab" = None):
        self.DiscountSlab_list_ = DiscountSlab_list_
        self.type = type
        self.shoppingCart = shoppingCart
        self.p0 = p0 if p0 is not None else set()
        self.customer3 = customer3
        self.order4 = order4 if order4 is not None else set()
        self.customerHandler16 = customerHandler16
        self.shoppingCart219 = shoppingCart219
        self.shoppingCart221 = shoppingCart221
        self.customer22 = customer22
        self.customer23 = customer23
        self.purchaseAmountSlab25 = purchaseAmountSlab25
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: CustomerType):
        self.__type = type

    @property
    def DiscountSlab_list_(self):
        return self.__DiscountSlab_list_
    @DiscountSlab_list_.setter
    def DiscountSlab_list_(self, DiscountSlab_list_: PurchaseAmountSlab):
        self.__DiscountSlab_list_ = DiscountSlab_list_

    @property
    def shoppingCart(self):
        return self.__shoppingCart
    @shoppingCart.setter
    def shoppingCart(self, shoppingCart: ShoppingCart):
        self.__shoppingCart = shoppingCart

    @property
    def customer23(self):
        return self.__customer23
    @customer23.setter
    def customer23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__customer23", None)
        self.__customer23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer22"):
                opp_val = getattr(old_value, "customer22", None)
                if opp_val == self:
                    setattr(old_value, "customer22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer22"):
                opp_val = getattr(value, "customer22", None)
                setattr(value, "customer22", self)

    @property
    def shoppingCart219(self):
        return self.__shoppingCart219
    @shoppingCart219.setter
    def shoppingCart219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__shoppingCart219", None)
        self.__shoppingCart219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer18"):
                opp_val = getattr(old_value, "customer18", None)
                if opp_val == self:
                    setattr(old_value, "customer18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer18"):
                opp_val = getattr(value, "customer18", None)
                setattr(value, "customer18", self)

    @property
    def customer22(self):
        return self.__customer22
    @customer22.setter
    def customer22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__customer22", None)
        self.__customer22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer23"):
                opp_val = getattr(old_value, "customer23", None)
                if opp_val == self:
                    setattr(old_value, "customer23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer23"):
                opp_val = getattr(value, "customer23", None)
                setattr(value, "customer23", self)

    @property
    def p0(self):
        return self.__p0
    @p0.setter
    def p0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__p0", None)
        self.__p0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "acc1"):
                    opp_val = getattr(item, "acc1", None)
                    
                    if opp_val == self:
                        setattr(item, "acc1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "acc1"):
                    opp_val = getattr(item, "acc1", None)
                    
                    setattr(item, "acc1", self)
                    

    @property
    def customer3(self):
        return self.__customer3
    @customer3.setter
    def customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__customer3", None)
        self.__customer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account2"):
                opp_val = getattr(old_value, "account2", None)
                if opp_val == self:
                    setattr(old_value, "account2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account2"):
                opp_val = getattr(value, "account2", None)
                setattr(value, "account2", self)

    @property
    def customerHandler16(self):
        return self.__customerHandler16
    @customerHandler16.setter
    def customerHandler16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__customerHandler16", None)
        self.__customerHandler16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer17"):
                opp_val = getattr(old_value, "customer17", None)
                if opp_val == self:
                    setattr(old_value, "customer17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer17"):
                opp_val = getattr(value, "customer17", None)
                setattr(value, "customer17", self)

    @property
    def order4(self):
        return self.__order4
    @order4.setter
    def order4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__order4", None)
        self.__order4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account5"):
                    opp_val = getattr(item, "account5", None)
                    
                    if opp_val == self:
                        setattr(item, "account5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account5"):
                    opp_val = getattr(item, "account5", None)
                    
                    setattr(item, "account5", self)
                    

    @property
    def shoppingCart221(self):
        return self.__shoppingCart221
    @shoppingCart221.setter
    def shoppingCart221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__shoppingCart221", None)
        self.__shoppingCart221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer20"):
                opp_val = getattr(old_value, "customer20", None)
                if opp_val == self:
                    setattr(old_value, "customer20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer20"):
                opp_val = getattr(value, "customer20", None)
                setattr(value, "customer20", self)

    @property
    def purchaseAmountSlab25(self):
        return self.__purchaseAmountSlab25
    @purchaseAmountSlab25.setter
    def purchaseAmountSlab25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__purchaseAmountSlab25", None)
        self.__purchaseAmountSlab25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer24"):
                opp_val = getattr(old_value, "customer24", None)
                if opp_val == self:
                    setattr(old_value, "customer24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer24"):
                opp_val = getattr(value, "customer24", None)
                setattr(value, "customer24", self)



class PremiumDiscountSlab:

    def __init__(self, RadixClient: str, log: str, email: str, PremiumSlab_list_: PurchaseAmountSlab, purchaseAmountSlab13: "PurchaseAmountSlab" = None):
        self.RadixClient = RadixClient
        self.log = log
        self.email = email
        self.PremiumSlab_list_ = PremiumSlab_list_
        self.purchaseAmountSlab13 = purchaseAmountSlab13
        
        pass
    @property
    def PremiumSlab_list_(self):
        return self.__PremiumSlab_list_
    @PremiumSlab_list_.setter
    def PremiumSlab_list_(self, PremiumSlab_list_: PurchaseAmountSlab):
        self.__PremiumSlab_list_ = PremiumSlab_list_

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def RadixClient(self):
        return self.__RadixClient
    @RadixClient.setter
    def RadixClient(self, RadixClient: str):
        self.__RadixClient = RadixClient

    @property
    def log(self):
        return self.__log
    @log.setter
    def log(self, log: str):
        self.__log = log

    @property
    def purchaseAmountSlab13(self):
        return self.__purchaseAmountSlab13
    @purchaseAmountSlab13.setter
    def purchaseAmountSlab13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PremiumDiscountSlab__purchaseAmountSlab13", None)
        self.__purchaseAmountSlab13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "premiumDiscountSlab12"):
                opp_val = getattr(old_value, "premiumDiscountSlab12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "premiumDiscountSlab12"):
                opp_val = getattr(value, "premiumDiscountSlab12", None)
                if opp_val is None:
                    setattr(value, "premiumDiscountSlab12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class RegularDiscountSlab:

    def __init__(self, RadixClient: str, log: str, email: str, attribute: str, RegularSlab_list__: PurchaseAmountSlab, _attr: str, attribute2: str, RegularSlab_list_: PurchaseAmountSlab, purchaseAmountSlab15: "PurchaseAmountSlab" = None):
        self.RadixClient = RadixClient
        self.log = log
        self.email = email
        self.attribute = attribute
        self.RegularSlab_list__ = RegularSlab_list__
        self._attr = _attr
        self.attribute2 = attribute2
        self.RegularSlab_list_ = RegularSlab_list_
        self.purchaseAmountSlab15 = purchaseAmountSlab15
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def RegularSlab_list_(self):
        return self.__RegularSlab_list_
    @RegularSlab_list_.setter
    def RegularSlab_list_(self, RegularSlab_list_: PurchaseAmountSlab):
        self.__RegularSlab_list_ = RegularSlab_list_

    @property
    def RegularSlab_list__(self):
        return self.__RegularSlab_list__
    @RegularSlab_list__.setter
    def RegularSlab_list__(self, RegularSlab_list__: PurchaseAmountSlab):
        self.__RegularSlab_list__ = RegularSlab_list__

    @property
    def RadixClient(self):
        return self.__RadixClient
    @RadixClient.setter
    def RadixClient(self, RadixClient: str):
        self.__RadixClient = RadixClient

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def log(self):
        return self.__log
    @log.setter
    def log(self, log: str):
        self.__log = log

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def purchaseAmountSlab15(self):
        return self.__purchaseAmountSlab15
    @purchaseAmountSlab15.setter
    def purchaseAmountSlab15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RegularDiscountSlab__purchaseAmountSlab15", None)
        self.__purchaseAmountSlab15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "regularDiscountSlab14"):
                opp_val = getattr(old_value, "regularDiscountSlab14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "regularDiscountSlab14"):
                opp_val = getattr(value, "regularDiscountSlab14", None)
                if opp_val is None:
                    setattr(value, "regularDiscountSlab14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class PurchaseAmountSlab:

    def __init__(self, from1: float, discount: float, to: float, premiumDiscountSlab12: set["PremiumDiscountSlab"] = None, regularDiscountSlab14: set["RegularDiscountSlab"] = None, customer24: "Customer" = None):
        self.from1 = from1
        self.discount = discount
        self.to = to
        self.premiumDiscountSlab12 = premiumDiscountSlab12 if premiumDiscountSlab12 is not None else set()
        self.regularDiscountSlab14 = regularDiscountSlab14 if regularDiscountSlab14 is not None else set()
        self.customer24 = customer24
        
        pass
    @property
    def from1(self):
        return self.__from1
    @from1.setter
    def from1(self, from1: float):
        self.__from1 = from1

    @property
    def to(self):
        return self.__to
    @to.setter
    def to(self, to: float):
        self.__to = to

    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self, discount: float):
        self.__discount = discount

    @property
    def regularDiscountSlab14(self):
        return self.__regularDiscountSlab14
    @regularDiscountSlab14.setter
    def regularDiscountSlab14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PurchaseAmountSlab__regularDiscountSlab14", None)
        self.__regularDiscountSlab14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "purchaseAmountSlab15"):
                    opp_val = getattr(item, "purchaseAmountSlab15", None)
                    
                    if opp_val == self:
                        setattr(item, "purchaseAmountSlab15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "purchaseAmountSlab15"):
                    opp_val = getattr(item, "purchaseAmountSlab15", None)
                    
                    setattr(item, "purchaseAmountSlab15", self)
                    

    @property
    def customer24(self):
        return self.__customer24
    @customer24.setter
    def customer24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PurchaseAmountSlab__customer24", None)
        self.__customer24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "purchaseAmountSlab25"):
                opp_val = getattr(old_value, "purchaseAmountSlab25", None)
                if opp_val == self:
                    setattr(old_value, "purchaseAmountSlab25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "purchaseAmountSlab25"):
                opp_val = getattr(value, "purchaseAmountSlab25", None)
                setattr(value, "purchaseAmountSlab25", self)

    @property
    def premiumDiscountSlab12(self):
        return self.__premiumDiscountSlab12
    @premiumDiscountSlab12.setter
    def premiumDiscountSlab12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PurchaseAmountSlab__premiumDiscountSlab12", None)
        self.__premiumDiscountSlab12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "purchaseAmountSlab13"):
                    opp_val = getattr(item, "purchaseAmountSlab13", None)
                    
                    if opp_val == self:
                        setattr(item, "purchaseAmountSlab13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "purchaseAmountSlab13"):
                    opp_val = getattr(item, "purchaseAmountSlab13", None)
                    
                    setattr(item, "purchaseAmountSlab13", self)
                    



class CustomerHandler:

    def __init__(self, populate: str, password: str, state: CustomerType, customer17: "Customer" = None):
        self.populate = populate
        self.password = password
        self.state = state
        self.customer17 = customer17
        
        pass
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: CustomerType):
        self.__state = state

    @property
    def populate(self):
        return self.__populate
    @populate.setter
    def populate(self, populate: str):
        self.__populate = populate

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def customer17(self):
        return self.__customer17
    @customer17.setter
    def customer17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CustomerHandler__customer17", None)
        self.__customer17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customerHandler16"):
                opp_val = getattr(old_value, "customerHandler16", None)
                if opp_val == self:
                    setattr(old_value, "customerHandler16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customerHandler16"):
                opp_val = getattr(value, "customerHandler16", None)
                setattr(value, "customerHandler16", self)



class RegularCustomer:

    def __init__(self, RadixClient: str, log: str, email: str):
        self.RadixClient = RadixClient
        self.log = log
        self.email = email
        
        pass
    @property
    def RadixClient(self):
        return self.__RadixClient
    @RadixClient.setter
    def RadixClient(self, RadixClient: str):
        self.__RadixClient = RadixClient

    @property
    def log(self):
        return self.__log
    @log.setter
    def log(self, log: str):
        self.__log = log

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email



class Item:

    def __init__(self, quantity: int, price: float, name: str, item8: "Item" = None, item9: "Item" = None, shoppingCart10: set["ShoppingCart"] = None):
        self.quantity = quantity
        self.price = price
        self.name = name
        self.item8 = item8
        self.item9 = item9
        self.shoppingCart10 = shoppingCart10 if shoppingCart10 is not None else set()
        
        pass
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
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def item9(self):
        return self.__item9
    @item9.setter
    def item9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__item9", None)
        self.__item9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item8"):
                opp_val = getattr(old_value, "item8", None)
                if opp_val == self:
                    setattr(old_value, "item8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item8"):
                opp_val = getattr(value, "item8", None)
                setattr(value, "item8", self)

    @property
    def item8(self):
        return self.__item8
    @item8.setter
    def item8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__item8", None)
        self.__item8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item9"):
                opp_val = getattr(old_value, "item9", None)
                if opp_val == self:
                    setattr(old_value, "item9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item9"):
                opp_val = getattr(value, "item9", None)
                setattr(value, "item9", self)

    @property
    def shoppingCart10(self):
        return self.__shoppingCart10
    @shoppingCart10.setter
    def shoppingCart10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__shoppingCart10", None)
        self.__shoppingCart10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "item11"):
                    opp_val = getattr(item, "item11", None)
                    
                    if opp_val == self:
                        setattr(item, "item11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "item11"):
                    opp_val = getattr(item, "item11", None)
                    
                    setattr(item, "item11", self)
                    



class ShoppingCart:

    def __init__(self, _attr: date, Items_list_: Item, item11: "Item" = None, customer18: "Customer" = None, customer20: "Customer" = None):
        self._attr = _attr
        self.Items_list_ = Items_list_
        self.item11 = item11
        self.customer18 = customer18
        self.customer20 = customer20
        
        pass
    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: date):
        self.___attr = _attr

    @property
    def Items_list_(self):
        return self.__Items_list_
    @Items_list_.setter
    def Items_list_(self, Items_list_: Item):
        self.__Items_list_ = Items_list_

    @property
    def item11(self):
        return self.__item11
    @item11.setter
    def item11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__item11", None)
        self.__item11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart10"):
                opp_val = getattr(old_value, "shoppingCart10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart10"):
                opp_val = getattr(value, "shoppingCart10", None)
                if opp_val is None:
                    setattr(value, "shoppingCart10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer18(self):
        return self.__customer18
    @customer18.setter
    def customer18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__customer18", None)
        self.__customer18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart219"):
                opp_val = getattr(old_value, "shoppingCart219", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart219"):
                opp_val = getattr(value, "shoppingCart219", None)
                setattr(value, "shoppingCart219", self)

    @property
    def customer20(self):
        return self.__customer20
    @customer20.setter
    def customer20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__customer20", None)
        self.__customer20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart221"):
                opp_val = getattr(old_value, "shoppingCart221", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart221"):
                opp_val = getattr(value, "shoppingCart221", None)
                setattr(value, "shoppingCart221", self)



class LZUser2:

    def __init__(self, populate: str, password: str, state: CustomerType):
        self.populate = populate
        self.password = password
        self.state = state
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: CustomerType):
        self.__state = state

    @property
    def populate(self):
        return self.__populate
    @populate.setter
    def populate(self, populate: str):
        self.__populate = populate



class Order:

    def __init__(self, number: int, ordered: date, shipped: bool, shipTo: str, total: float, status: str, account5: "Customer" = None, payment7: "Payment" = None):
        self.number = number
        self.ordered = ordered
        self.shipped = shipped
        self.shipTo = shipTo
        self.total = total
        self.status = status
        self.account5 = account5
        self.payment7 = payment7
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def shipTo(self):
        return self.__shipTo
    @shipTo.setter
    def shipTo(self, shipTo: str):
        self.__shipTo = shipTo

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def ordered(self):
        return self.__ordered
    @ordered.setter
    def ordered(self, ordered: date):
        self.__ordered = ordered

    @property
    def shipped(self):
        return self.__shipped
    @shipped.setter
    def shipped(self, shipped: bool):
        self.__shipped = shipped

    @property
    def payment7(self):
        return self.__payment7
    @payment7.setter
    def payment7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment7", None)
        self.__payment7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order6"):
                opp_val = getattr(old_value, "order6", None)
                if opp_val == self:
                    setattr(old_value, "order6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order6"):
                opp_val = getattr(value, "order6", None)
                setattr(value, "order6", self)

    @property
    def account5(self):
        return self.__account5
    @account5.setter
    def account5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__account5", None)
        self.__account5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order4"):
                opp_val = getattr(old_value, "order4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order4"):
                opp_val = getattr(value, "order4", None)
                if opp_val is None:
                    setattr(value, "order4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class SalesPerson:

    def __init__(self, populate: str, password: str, state: CustomerType):
        self.populate = populate
        self.password = password
        self.state = state
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: CustomerType):
        self.__state = state

    @property
    def populate(self):
        return self.__populate
    @populate.setter
    def populate(self, populate: str):
        self.__populate = populate



class Payment:

    def __init__(self, paidDate: date, total: float, details: str, acc1: "Customer" = None, order6: "Order" = None):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        self.acc1 = acc1
        self.order6 = order6
        
        pass
    @property
    def details(self):
        return self.__details
    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def paidDate(self):
        return self.__paidDate
    @paidDate.setter
    def paidDate(self, paidDate: date):
        self.__paidDate = paidDate

    @property
    def order6(self):
        return self.__order6
    @order6.setter
    def order6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order6", None)
        self.__order6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment7"):
                opp_val = getattr(old_value, "payment7", None)
                if opp_val == self:
                    setattr(old_value, "payment7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment7"):
                opp_val = getattr(value, "payment7", None)
                setattr(value, "payment7", self)

    @property
    def acc1(self):
        return self.__acc1
    @acc1.setter
    def acc1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__acc1", None)
        self.__acc1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p0"):
                opp_val = getattr(old_value, "p0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p0"):
                opp_val = getattr(value, "p0", None)
                if opp_val is None:
                    setattr(value, "p0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class PremiumCustomer:

    def __init__(self, RadixClient: str, log: str, email: str, account2: "Customer" = None):
        self.RadixClient = RadixClient
        self.log = log
        self.email = email
        self.account2 = account2
        
        pass
    @property
    def RadixClient(self):
        return self.__RadixClient
    @RadixClient.setter
    def RadixClient(self, RadixClient: str):
        self.__RadixClient = RadixClient

    @property
    def log(self):
        return self.__log
    @log.setter
    def log(self, log: str):
        self.__log = log

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def account2(self):
        return self.__account2
    @account2.setter
    def account2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PremiumCustomer__account2", None)
        self.__account2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer3"):
                opp_val = getattr(old_value, "customer3", None)
                if opp_val == self:
                    setattr(old_value, "customer3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer3"):
                opp_val = getattr(value, "customer3", None)
                setattr(value, "customer3", self)

