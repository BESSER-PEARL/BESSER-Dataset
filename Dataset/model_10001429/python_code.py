from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass

############################################
# Definition of Classes
############################################







class Bank_System_Actor:

    pass


class Manager_Actor:

    pass


class Employee_Actor:

    pass


class Shopping_System_Manage_Settings_UseCase:

    pass


class Shopping_System_Manage_Bills_UseCase:

    pass


class Shopping_System_Manage_Catalog_UseCase:

    pass


class Shopping_System_Payment_UseCase:

    pass


class Shopping_System_Manage_Order_UseCase:

    pass


class Shopping_System_Manage_ShopCart_UseCase:

    pass


class Shopping_System_Search_Product_UseCase:

    pass


class Shopping_System_Registration_UseCase:

    pass


class Shopping_System_Login_UseCase:

    pass


class Customer_Actor:

    pass


class Checkout_UseCase:

    pass





class Class2:

    pass


class Class1:

    pass


class User:

    def __init__(self, u_id: int, name: str, password: str, e_mail: str, phone: str):
        self.u_id = u_id
        self.name = name
        self.password = password
        self.e_mail = e_mail
        self.phone = phone
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def u_id(self):
        return self.__u_id
    @u_id.setter
    def u_id(self, u_id: int):
        self.__u_id = u_id

    @property
    def e_mail(self):
        return self.__e_mail
    @e_mail.setter
    def e_mail(self, e_mail: str):
        self.__e_mail = e_mail

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password



class Administrator:

    def __init__(self, u_id: int, username: str, e_mail: str, phone: str):
        self.u_id = u_id
        self.username = username
        self.e_mail = e_mail
        self.phone = phone
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def u_id(self):
        return self.__u_id
    @u_id.setter
    def u_id(self, u_id: int):
        self.__u_id = u_id

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def e_mail(self):
        return self.__e_mail
    @e_mail.setter
    def e_mail(self, e_mail: str):
        self.__e_mail = e_mail



class Class:

    pass


class Customer:

    def __init__(self, u_id: int, name: str, surname: str, address: str, e_mail: str, orders8: set["Orders"] = None, shoppingCart13: "ShoppingCart" = None, shoppingCart14: "ShoppingCart" = None, statistics20: "Statistics" = None):
        self.u_id = u_id
        self.name = name
        self.surname = surname
        self.address = address
        self.e_mail = e_mail
        self.orders8 = orders8 if orders8 is not None else set()
        self.shoppingCart13 = shoppingCart13
        self.shoppingCart14 = shoppingCart14
        self.statistics20 = statistics20
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def e_mail(self):
        return self.__e_mail
    @e_mail.setter
    def e_mail(self, e_mail: str):
        self.__e_mail = e_mail

    @property
    def u_id(self):
        return self.__u_id
    @u_id.setter
    def u_id(self, u_id: int):
        self.__u_id = u_id

    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def shoppingCart13(self):
        return self.__shoppingCart13
    @shoppingCart13.setter
    def shoppingCart13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__shoppingCart13", None)
        self.__shoppingCart13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer12"):
                opp_val = getattr(old_value, "customer12", None)
                if opp_val == self:
                    setattr(old_value, "customer12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer12"):
                opp_val = getattr(value, "customer12", None)
                setattr(value, "customer12", self)

    @property
    def shoppingCart14(self):
        return self.__shoppingCart14
    @shoppingCart14.setter
    def shoppingCart14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__shoppingCart14", None)
        self.__shoppingCart14 = value
        
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

    @property
    def statistics20(self):
        return self.__statistics20
    @statistics20.setter
    def statistics20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__statistics20", None)
        self.__statistics20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer21"):
                opp_val = getattr(old_value, "customer21", None)
                if opp_val == self:
                    setattr(old_value, "customer21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer21"):
                opp_val = getattr(value, "customer21", None)
                setattr(value, "customer21", self)

    @property
    def orders8(self):
        return self.__orders8
    @orders8.setter
    def orders8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__orders8", None)
        self.__orders8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer9"):
                    opp_val = getattr(item, "customer9", None)
                    
                    if opp_val == self:
                        setattr(item, "customer9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer9"):
                    opp_val = getattr(item, "customer9", None)
                    
                    setattr(item, "customer9", self)
                    



class SubCategory:

    def __init__(self, id: int, name: str, cat_id: int, subCategory4: "SubCategory" = None, subCategory5: "SubCategory" = None, category6: "Category" = None, category2: set["Category"] = None):
        self.id = id
        self.name = name
        self.cat_id = cat_id
        self.subCategory4 = subCategory4
        self.subCategory5 = subCategory5
        self.category6 = category6
        self.category2 = category2 if category2 is not None else set()
        
        pass
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
    def name(self, name: str):
        self.__name = name

    @property
    def cat_id(self):
        return self.__cat_id
    @cat_id.setter
    def cat_id(self, cat_id: int):
        self.__cat_id = cat_id

    @property
    def subCategory4(self):
        return self.__subCategory4
    @subCategory4.setter
    def subCategory4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SubCategory__subCategory4", None)
        self.__subCategory4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subCategory5"):
                opp_val = getattr(old_value, "subCategory5", None)
                if opp_val == self:
                    setattr(old_value, "subCategory5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subCategory5"):
                opp_val = getattr(value, "subCategory5", None)
                setattr(value, "subCategory5", self)

    @property
    def subCategory5(self):
        return self.__subCategory5
    @subCategory5.setter
    def subCategory5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SubCategory__subCategory5", None)
        self.__subCategory5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subCategory4"):
                opp_val = getattr(old_value, "subCategory4", None)
                if opp_val == self:
                    setattr(old_value, "subCategory4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subCategory4"):
                opp_val = getattr(value, "subCategory4", None)
                setattr(value, "subCategory4", self)

    @property
    def category6(self):
        return self.__category6
    @category6.setter
    def category6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SubCategory__category6", None)
        self.__category6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subCategory7"):
                opp_val = getattr(old_value, "subCategory7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subCategory7"):
                opp_val = getattr(value, "subCategory7", None)
                if opp_val is None:
                    setattr(value, "subCategory7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def category2(self):
        return self.__category2
    @category2.setter
    def category2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SubCategory__category2", None)
        self.__category2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "subCategory3"):
                    opp_val = getattr(item, "subCategory3", None)
                    
                    if opp_val == self:
                        setattr(item, "subCategory3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "subCategory3"):
                    opp_val = getattr(item, "subCategory3", None)
                    
                    setattr(item, "subCategory3", self)
                    



class Producer:

    def __init__(self, u_id: int, name: str, country: str, product18: set["Product"] = None):
        self.u_id = u_id
        self.name = name
        self.country = country
        self.product18 = product18 if product18 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def u_id(self):
        return self.__u_id
    @u_id.setter
    def u_id(self, u_id: int):
        self.__u_id = u_id

    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def product18(self):
        return self.__product18
    @product18.setter
    def product18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Producer__product18", None)
        self.__product18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "producer19"):
                    opp_val = getattr(item, "producer19", None)
                    
                    if opp_val == self:
                        setattr(item, "producer19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "producer19"):
                    opp_val = getattr(item, "producer19", None)
                    
                    setattr(item, "producer19", self)
                    



class _Interface:

    pass


class Category:

    def __init__(self, u_id: int, name: str, sequence_id: int, subCategory7: set["SubCategory"] = None, category0: "Category" = None, category1: "Category" = None, subCategory3: "SubCategory" = None, category22: set["Category"] = None, category23: "Category" = None):
        self.u_id = u_id
        self.name = name
        self.sequence_id = sequence_id
        self.subCategory7 = subCategory7 if subCategory7 is not None else set()
        self.category0 = category0
        self.category1 = category1
        self.subCategory3 = subCategory3
        self.category22 = category22 if category22 is not None else set()
        self.category23 = category23
        
        pass
    @property
    def sequence_id(self):
        return self.__sequence_id
    @sequence_id.setter
    def sequence_id(self, sequence_id: int):
        self.__sequence_id = sequence_id

    @property
    def u_id(self):
        return self.__u_id
    @u_id.setter
    def u_id(self, u_id: int):
        self.__u_id = u_id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def category22(self):
        return self.__category22
    @category22.setter
    def category22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__category22", None)
        self.__category22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "category23"):
                    opp_val = getattr(item, "category23", None)
                    
                    if opp_val == self:
                        setattr(item, "category23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "category23"):
                    opp_val = getattr(item, "category23", None)
                    
                    setattr(item, "category23", self)
                    

    @property
    def category23(self):
        return self.__category23
    @category23.setter
    def category23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__category23", None)
        self.__category23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category22"):
                opp_val = getattr(old_value, "category22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category22"):
                opp_val = getattr(value, "category22", None)
                if opp_val is None:
                    setattr(value, "category22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def category1(self):
        return self.__category1
    @category1.setter
    def category1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__category1", None)
        self.__category1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category0"):
                opp_val = getattr(old_value, "category0", None)
                if opp_val == self:
                    setattr(old_value, "category0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category0"):
                opp_val = getattr(value, "category0", None)
                setattr(value, "category0", self)

    @property
    def subCategory7(self):
        return self.__subCategory7
    @subCategory7.setter
    def subCategory7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__subCategory7", None)
        self.__subCategory7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "category6"):
                    opp_val = getattr(item, "category6", None)
                    
                    if opp_val == self:
                        setattr(item, "category6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "category6"):
                    opp_val = getattr(item, "category6", None)
                    
                    setattr(item, "category6", self)
                    

    @property
    def subCategory3(self):
        return self.__subCategory3
    @subCategory3.setter
    def subCategory3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__subCategory3", None)
        self.__subCategory3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category2"):
                opp_val = getattr(old_value, "category2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category2"):
                opp_val = getattr(value, "category2", None)
                if opp_val is None:
                    setattr(value, "category2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def category0(self):
        return self.__category0
    @category0.setter
    def category0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__category0", None)
        self.__category0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category1"):
                opp_val = getattr(old_value, "category1", None)
                if opp_val == self:
                    setattr(old_value, "category1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category1"):
                opp_val = getattr(value, "category1", None)
                setattr(value, "category1", self)



class Component_Component:

    pass


class Statistics:

    def __init__(self, customer_id: int, click_homepage: int, click_homeCat: int, click_subCat: int, item_id: int, clicks: int, customer21: "Customer" = None):
        self.customer_id = customer_id
        self.click_homepage = click_homepage
        self.click_homeCat = click_homeCat
        self.click_subCat = click_subCat
        self.item_id = item_id
        self.clicks = clicks
        self.customer21 = customer21
        
        pass
    @property
    def click_homepage(self):
        return self.__click_homepage
    @click_homepage.setter
    def click_homepage(self, click_homepage: int):
        self.__click_homepage = click_homepage

    @property
    def item_id(self):
        return self.__item_id
    @item_id.setter
    def item_id(self, item_id: int):
        self.__item_id = item_id

    @property
    def click_homeCat(self):
        return self.__click_homeCat
    @click_homeCat.setter
    def click_homeCat(self, click_homeCat: int):
        self.__click_homeCat = click_homeCat

    @property
    def clicks(self):
        return self.__clicks
    @clicks.setter
    def clicks(self, clicks: int):
        self.__clicks = clicks

    @property
    def click_subCat(self):
        return self.__click_subCat
    @click_subCat.setter
    def click_subCat(self, click_subCat: int):
        self.__click_subCat = click_subCat

    @property
    def customer_id(self):
        return self.__customer_id
    @customer_id.setter
    def customer_id(self, customer_id: int):
        self.__customer_id = customer_id

    @property
    def customer21(self):
        return self.__customer21
    @customer21.setter
    def customer21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Statistics__customer21", None)
        self.__customer21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statistics20"):
                opp_val = getattr(old_value, "statistics20", None)
                if opp_val == self:
                    setattr(old_value, "statistics20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statistics20"):
                opp_val = getattr(value, "statistics20", None)
                setattr(value, "statistics20", self)



class Product:

    def __init__(self, u_id: int, stock: int, price: str, orderDetails16: "OrderDetails" = None, producer19: "Producer" = None):
        self.u_id = u_id
        self.stock = stock
        self.price = price
        self.orderDetails16 = orderDetails16
        self.producer19 = producer19
        
        pass
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, stock: int):
        self.__stock = stock

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def u_id(self):
        return self.__u_id
    @u_id.setter
    def u_id(self, u_id: int):
        self.__u_id = u_id

    @property
    def orderDetails16(self):
        return self.__orderDetails16
    @orderDetails16.setter
    def orderDetails16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__orderDetails16", None)
        self.__orderDetails16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product17"):
                opp_val = getattr(old_value, "product17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product17"):
                opp_val = getattr(value, "product17", None)
                if opp_val is None:
                    setattr(value, "product17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def producer19(self):
        return self.__producer19
    @producer19.setter
    def producer19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__producer19", None)
        self.__producer19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product18"):
                opp_val = getattr(old_value, "product18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product18"):
                opp_val = getattr(value, "product18", None)
                if opp_val is None:
                    setattr(value, "product18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class inter:

    pass


class ShoppingCart:

    def __init__(self, cart_id: int, product_id: int, quantity: int, customer12: "Customer" = None, customer15: "Customer" = None):
        self.cart_id = cart_id
        self.product_id = product_id
        self.quantity = quantity
        self.customer12 = customer12
        self.customer15 = customer15
        
        pass
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def cart_id(self):
        return self.__cart_id
    @cart_id.setter
    def cart_id(self, cart_id: int):
        self.__cart_id = cart_id

    @property
    def product_id(self):
        return self.__product_id
    @product_id.setter
    def product_id(self, product_id: int):
        self.__product_id = product_id

    @property
    def customer12(self):
        return self.__customer12
    @customer12.setter
    def customer12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__customer12", None)
        self.__customer12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart13"):
                opp_val = getattr(old_value, "shoppingCart13", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart13"):
                opp_val = getattr(value, "shoppingCart13", None)
                setattr(value, "shoppingCart13", self)

    @property
    def customer15(self):
        return self.__customer15
    @customer15.setter
    def customer15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__customer15", None)
        self.__customer15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart14"):
                opp_val = getattr(old_value, "shoppingCart14", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart14"):
                opp_val = getattr(value, "shoppingCart14", None)
                setattr(value, "shoppingCart14", self)



class OrderDetails:

    def __init__(self, order_id: int, product_id: int, product_name: str, quantity: int, orders11: "Orders" = None, product17: set["Product"] = None):
        self.order_id = order_id
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.orders11 = orders11
        self.product17 = product17 if product17 is not None else set()
        
        pass
    @property
    def order_id(self):
        return self.__order_id
    @order_id.setter
    def order_id(self, order_id: int):
        self.__order_id = order_id

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def product_id(self):
        return self.__product_id
    @product_id.setter
    def product_id(self, product_id: int):
        self.__product_id = product_id

    @property
    def product_name(self):
        return self.__product_name
    @product_name.setter
    def product_name(self, product_name: str):
        self.__product_name = product_name

    @property
    def product17(self):
        return self.__product17
    @product17.setter
    def product17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderDetails__product17", None)
        self.__product17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "orderDetails16"):
                    opp_val = getattr(item, "orderDetails16", None)
                    
                    if opp_val == self:
                        setattr(item, "orderDetails16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "orderDetails16"):
                    opp_val = getattr(item, "orderDetails16", None)
                    
                    setattr(item, "orderDetails16", self)
                    

    @property
    def orders11(self):
        return self.__orders11
    @orders11.setter
    def orders11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderDetails__orders11", None)
        self.__orders11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderDetails10"):
                opp_val = getattr(old_value, "orderDetails10", None)
                if opp_val == self:
                    setattr(old_value, "orderDetails10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderDetails10"):
                opp_val = getattr(value, "orderDetails10", None)
                setattr(value, "orderDetails10", self)



class Orders:

    def __init__(self, u_id: int, dateCreated: str, dateShipped: str, customer_id: int, status: int, customer9: "Customer" = None, orderDetails10: "OrderDetails" = None):
        self.u_id = u_id
        self.dateCreated = dateCreated
        self.dateShipped = dateShipped
        self.customer_id = customer_id
        self.status = status
        self.customer9 = customer9
        self.orderDetails10 = orderDetails10
        
        pass
    @property
    def dateCreated(self):
        return self.__dateCreated
    @dateCreated.setter
    def dateCreated(self, dateCreated: str):
        self.__dateCreated = dateCreated

    @property
    def customer_id(self):
        return self.__customer_id
    @customer_id.setter
    def customer_id(self, customer_id: int):
        self.__customer_id = customer_id

    @property
    def u_id(self):
        return self.__u_id
    @u_id.setter
    def u_id(self, u_id: int):
        self.__u_id = u_id

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
    def status(self, status: int):
        self.__status = status

    @property
    def orderDetails10(self):
        return self.__orderDetails10
    @orderDetails10.setter
    def orderDetails10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__orderDetails10", None)
        self.__orderDetails10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders11"):
                opp_val = getattr(old_value, "orders11", None)
                if opp_val == self:
                    setattr(old_value, "orders11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders11"):
                opp_val = getattr(value, "orders11", None)
                setattr(value, "orders11", self)

    @property
    def customer9(self):
        return self.__customer9
    @customer9.setter
    def customer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__customer9", None)
        self.__customer9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders8"):
                opp_val = getattr(old_value, "orders8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders8"):
                opp_val = getattr(value, "orders8", None)
                if opp_val is None:
                    setattr(value, "orders8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Class21:

    pass
