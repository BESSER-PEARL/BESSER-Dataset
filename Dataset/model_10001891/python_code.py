from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class delivery:

    def __init__(self, name: char, password: char, product12: "product" = None, payment14: "Payment" = None):
        self.name = name
        self.password = password
        self.product12 = product12
        self.payment14 = payment14
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: char):
        self.__password = password

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: char):
        self.__name = name

    @property
    def product12(self):
        return self.__product12
    @product12.setter
    def product12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delivery__product12", None)
        self.__product12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delivery13"):
                opp_val = getattr(old_value, "delivery13", None)
                if opp_val == self:
                    setattr(old_value, "delivery13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delivery13"):
                opp_val = getattr(value, "delivery13", None)
                setattr(value, "delivery13", self)

    @property
    def payment14(self):
        return self.__payment14
    @payment14.setter
    def payment14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delivery__payment14", None)
        self.__payment14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delivery15"):
                opp_val = getattr(old_value, "delivery15", None)
                if opp_val == self:
                    setattr(old_value, "delivery15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delivery15"):
                opp_val = getattr(value, "delivery15", None)
                setattr(value, "delivery15", self)



class supplier:

    def __init__(self, name: char, password: int, product10: "product" = None):
        self.name = name
        self.password = password
        self.product10 = product10
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: char):
        self.__name = name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: int):
        self.__password = password

    @property
    def product10(self):
        return self.__product10
    @product10.setter
    def product10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_supplier__product10", None)
        self.__product10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "supplier11"):
                opp_val = getattr(old_value, "supplier11", None)
                if opp_val == self:
                    setattr(old_value, "supplier11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "supplier11"):
                opp_val = getattr(value, "supplier11", None)
                setattr(value, "supplier11", self)



class gest:

    pass


class cart:

    def __init__(self, NumberOfProduct: int, product1: char, product2: char, productn: char, price: str, total: str, id: int, customer3: "customer" = None):
        self.NumberOfProduct = NumberOfProduct
        self.product1 = product1
        self.product2 = product2
        self.productn = productn
        self.price = price
        self.total = total
        self.id = id
        self.customer3 = customer3
        
        pass
    @property
    def NumberOfProduct(self):
        return self.__NumberOfProduct
    @NumberOfProduct.setter
    def NumberOfProduct(self, NumberOfProduct: int):
        self.__NumberOfProduct = NumberOfProduct

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: str):
        self.__total = total

    @property
    def product2(self):
        return self.__product2
    @product2.setter
    def product2(self, product2: char):
        self.__product2 = product2

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def product1(self):
        return self.__product1
    @product1.setter
    def product1(self, product1: char):
        self.__product1 = product1

    @property
    def productn(self):
        return self.__productn
    @productn.setter
    def productn(self, productn: char):
        self.__productn = productn

    @property
    def customer3(self):
        return self.__customer3
    @customer3.setter
    def customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cart__customer3", None)
        self.__customer3 = value
        
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



class product:

    def __init__(self, name: char, group: char, subgroub: char, id: int, customer5: "customer" = None, gest6: "gest" = None, admin9: "admin" = None, supplier11: "supplier" = None, delivery13: "delivery" = None):
        self.name = name
        self.group = group
        self.subgroub = subgroub
        self.id = id
        self.customer5 = customer5
        self.gest6 = gest6
        self.admin9 = admin9
        self.supplier11 = supplier11
        self.delivery13 = delivery13
        
        pass
    @property
    def group(self):
        return self.__group
    @group.setter
    def group(self, group: char):
        self.__group = group

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: char):
        self.__name = name

    @property
    def subgroub(self):
        return self.__subgroub
    @subgroub.setter
    def subgroub(self, subgroub: char):
        self.__subgroub = subgroub

    @property
    def delivery13(self):
        return self.__delivery13
    @delivery13.setter
    def delivery13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product__delivery13", None)
        self.__delivery13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product12"):
                opp_val = getattr(old_value, "product12", None)
                if opp_val == self:
                    setattr(old_value, "product12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product12"):
                opp_val = getattr(value, "product12", None)
                setattr(value, "product12", self)

    @property
    def admin9(self):
        return self.__admin9
    @admin9.setter
    def admin9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product__admin9", None)
        self.__admin9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product8"):
                opp_val = getattr(old_value, "product8", None)
                if opp_val == self:
                    setattr(old_value, "product8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product8"):
                opp_val = getattr(value, "product8", None)
                setattr(value, "product8", self)

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product__customer5", None)
        self.__customer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product4"):
                opp_val = getattr(old_value, "product4", None)
                if opp_val == self:
                    setattr(old_value, "product4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product4"):
                opp_val = getattr(value, "product4", None)
                setattr(value, "product4", self)

    @property
    def supplier11(self):
        return self.__supplier11
    @supplier11.setter
    def supplier11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product__supplier11", None)
        self.__supplier11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product10"):
                opp_val = getattr(old_value, "product10", None)
                if opp_val == self:
                    setattr(old_value, "product10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product10"):
                opp_val = getattr(value, "product10", None)
                setattr(value, "product10", self)

    @property
    def gest6(self):
        return self.__gest6
    @gest6.setter
    def gest6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product__gest6", None)
        self.__gest6 = value
        
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



class Payment:

    def __init__(self, customerName: char, cardType: char, cardNo: int, customerName1: char, customer0: "customer" = None, delivery15: "delivery" = None):
        self.customerName = customerName
        self.cardType = cardType
        self.cardNo = cardNo
        self.customerName1 = customerName1
        self.customer0 = customer0
        self.delivery15 = delivery15
        
        pass
    @property
    def cardNo(self):
        return self.__cardNo
    @cardNo.setter
    def cardNo(self, cardNo: int):
        self.__cardNo = cardNo

    @property
    def customerName(self):
        return self.__customerName
    @customerName.setter
    def customerName(self, customerName: char):
        self.__customerName = customerName

    @property
    def cardType(self):
        return self.__cardType
    @cardType.setter
    def cardType(self, cardType: char):
        self.__cardType = cardType

    @property
    def customerName1(self):
        return self.__customerName1
    @customerName1.setter
    def customerName1(self, customerName1: char):
        self.__customerName1 = customerName1

    @property
    def customer0(self):
        return self.__customer0
    @customer0.setter
    def customer0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__customer0", None)
        self.__customer0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment1"):
                opp_val = getattr(old_value, "payment1", None)
                if opp_val == self:
                    setattr(old_value, "payment1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment1"):
                opp_val = getattr(value, "payment1", None)
                setattr(value, "payment1", self)

    @property
    def delivery15(self):
        return self.__delivery15
    @delivery15.setter
    def delivery15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__delivery15", None)
        self.__delivery15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment14"):
                opp_val = getattr(old_value, "payment14", None)
                if opp_val == self:
                    setattr(old_value, "payment14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment14"):
                opp_val = getattr(value, "payment14", None)
                setattr(value, "payment14", self)



class char:

    pass


class customer:

    def __init__(self, name: char, address: char, phone: int, email: char, password: int, payment1: "Payment" = None, cart2: "cart" = None, product4: "product" = None):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.password = password
        self.payment1 = payment1
        self.cart2 = cart2
        self.product4 = product4
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: int):
        self.__password = password

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: char):
        self.__name = name

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
    def email(self, email: char):
        self.__email = email

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: char):
        self.__address = address

    @property
    def cart2(self):
        return self.__cart2
    @cart2.setter
    def cart2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customer__cart2", None)
        self.__cart2 = value
        
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

    @property
    def product4(self):
        return self.__product4
    @product4.setter
    def product4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customer__product4", None)
        self.__product4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer5"):
                opp_val = getattr(old_value, "customer5", None)
                if opp_val == self:
                    setattr(old_value, "customer5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer5"):
                opp_val = getattr(value, "customer5", None)
                setattr(value, "customer5", self)

    @property
    def payment1(self):
        return self.__payment1
    @payment1.setter
    def payment1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customer__payment1", None)
        self.__payment1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer0"):
                opp_val = getattr(old_value, "customer0", None)
                if opp_val == self:
                    setattr(old_value, "customer0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer0"):
                opp_val = getattr(value, "customer0", None)
                setattr(value, "customer0", self)



class admin:

    def __init__(self, user_type: int, user_name: str, user_mobile: int, product8: "product" = None):
        self.user_type = user_type
        self.user_name = user_name
        self.user_mobile = user_mobile
        self.product8 = product8
        
        pass
    @property
    def user_type(self):
        return self.__user_type
    @user_type.setter
    def user_type(self, user_type: int):
        self.__user_type = user_type

    @property
    def user_mobile(self):
        return self.__user_mobile
    @user_mobile.setter
    def user_mobile(self, user_mobile: int):
        self.__user_mobile = user_mobile

    @property
    def user_name(self):
        return self.__user_name
    @user_name.setter
    def user_name(self, user_name: str):
        self.__user_name = user_name

    @property
    def product8(self):
        return self.__product8
    @product8.setter
    def product8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_admin__product8", None)
        self.__product8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin9"):
                opp_val = getattr(old_value, "admin9", None)
                if opp_val == self:
                    setattr(old_value, "admin9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin9"):
                opp_val = getattr(value, "admin9", None)
                setattr(value, "admin9", self)

