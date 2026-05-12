from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class gives_feedback_UseCase:

    pass


class requests_to_rate_the_website_UseCase:

    pass


class asks_feedback_UseCase:

    pass


class checks_availability_of_item_UseCase:

    pass


class selectsitem_UseCase:

    pass


class cancelorder_UseCase:

    pass


class placeorder_UseCase:

    pass


class purchase_UseCase:

    pass


class shoppingcart_Actor:

    pass


class customer_Actor:

    pass





class preferredcustomer:

    def __init__(self, discount: int):
        self.discount = discount
        
        pass
    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self, discount: int):
        self.__discount = discount



class itemtopurchase:

    def __init__(self, quantity: int, itemtopurchase: int, shoppingcart1: "shoppingcart" = None):
        self.quantity = quantity
        self.itemtopurchase = itemtopurchase
        self.shoppingcart1 = shoppingcart1
        
        pass
    @property
    def itemtopurchase(self):
        return self.__itemtopurchase
    @itemtopurchase.setter
    def itemtopurchase(self, itemtopurchase: int):
        self.__itemtopurchase = itemtopurchase

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def shoppingcart1(self):
        return self.__shoppingcart1
    @shoppingcart1.setter
    def shoppingcart1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itemtopurchase__shoppingcart1", None)
        self.__shoppingcart1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itemtopurchase0"):
                opp_val = getattr(old_value, "itemtopurchase0", None)
                if opp_val == self:
                    setattr(old_value, "itemtopurchase0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itemtopurchase0"):
                opp_val = getattr(value, "itemtopurchase0", None)
                setattr(value, "itemtopurchase0", self)



class shoppingcart:

    def __init__(self, subtotal: int, salestax: int, total: int, itemtopurchase0: "itemtopurchase" = None):
        self.subtotal = subtotal
        self.salestax = salestax
        self.total = total
        self.itemtopurchase0 = itemtopurchase0
        
        pass
    @property
    def salestax(self):
        return self.__salestax
    @salestax.setter
    def salestax(self, salestax: int):
        self.__salestax = salestax

    @property
    def subtotal(self):
        return self.__subtotal
    @subtotal.setter
    def subtotal(self, subtotal: int):
        self.__subtotal = subtotal

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: int):
        self.__total = total

    @property
    def itemtopurchase0(self):
        return self.__itemtopurchase0
    @itemtopurchase0.setter
    def itemtopurchase0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shoppingcart__itemtopurchase0", None)
        self.__itemtopurchase0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingcart1"):
                opp_val = getattr(old_value, "shoppingcart1", None)
                if opp_val == self:
                    setattr(old_value, "shoppingcart1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingcart1"):
                opp_val = getattr(value, "shoppingcart1", None)
                setattr(value, "shoppingcart1", self)



class customer:

    def __init__(self, name: str, addresstobill: int, addresstoship: int, creditcard3: "creditcard" = None):
        self.name = name
        self.addresstobill = addresstobill
        self.addresstoship = addresstoship
        self.creditcard3 = creditcard3
        
        pass
    @property
    def addresstoship(self):
        return self.__addresstoship
    @addresstoship.setter
    def addresstoship(self, addresstoship: int):
        self.__addresstoship = addresstoship

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def addresstobill(self):
        return self.__addresstobill
    @addresstobill.setter
    def addresstobill(self, addresstobill: int):
        self.__addresstobill = addresstobill

    @property
    def creditcard3(self):
        return self.__creditcard3
    @creditcard3.setter
    def creditcard3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customer__creditcard3", None)
        self.__creditcard3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer2"):
                opp_val = getattr(old_value, "customer2", None)
                if opp_val == self:
                    setattr(old_value, "customer2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer2"):
                opp_val = getattr(value, "customer2", None)
                setattr(value, "customer2", self)



class creditcard:

    def __init__(self, issuer: str, number: int, expirationdate: date, customer2: "customer" = None):
        self.issuer = issuer
        self.number = number
        self.expirationdate = expirationdate
        self.customer2 = customer2
        
        pass
    @property
    def issuer(self):
        return self.__issuer
    @issuer.setter
    def issuer(self, issuer: str):
        self.__issuer = issuer

    @property
    def expirationdate(self):
        return self.__expirationdate
    @expirationdate.setter
    def expirationdate(self, expirationdate: date):
        self.__expirationdate = expirationdate

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def customer2(self):
        return self.__customer2
    @customer2.setter
    def customer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_creditcard__customer2", None)
        self.__customer2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "creditcard3"):
                opp_val = getattr(old_value, "creditcard3", None)
                if opp_val == self:
                    setattr(old_value, "creditcard3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "creditcard3"):
                opp_val = getattr(value, "creditcard3", None)
                setattr(value, "creditcard3", self)

