from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class add_customer_UseCase:

    pass


class add_seller__UseCase:

    pass


class delete_seller_UseCase:

    pass


class seller_registration_UseCase:

    pass


class add_products_to_sections__UseCase:

    pass


class update_section_UseCase:

    pass


class delete_customer__UseCase:

    pass


class manager_Actor:

    pass


class Entering_prices_UseCase:

    pass


class Make_comprehensive_reports_UseCase:

    pass


class Calculating_the_check_UseCase:

    pass


class Add_sold_products_UseCase:

    pass


class cashier_Actor:

    pass


class Card_id_registration_UseCase:

    pass


class customer_address__UseCase:

    pass


class customer_name_UseCase:

    pass


class Online_customer_request_UseCase:

    pass


class later_payment_sale__UseCase:

    pass


class direct_sale_UseCase:

    pass


class seller__Actor:

    pass





class customer:

    def __init__(self, name: str, id_card: int, address: str, the_product31: "the_product" = None):
        self.name = name
        self.id_card = id_card
        self.address = address
        self.the_product31 = the_product31
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id_card(self):
        return self.__id_card
    @id_card.setter
    def id_card(self, id_card: int):
        self.__id_card = id_card

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def the_product31(self):
        return self.__the_product31
    @the_product31.setter
    def the_product31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customer__the_product31", None)
        self.__the_product31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer30"):
                opp_val = getattr(old_value, "customer30", None)
                if opp_val == self:
                    setattr(old_value, "customer30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer30"):
                opp_val = getattr(value, "customer30", None)
                setattr(value, "customer30", self)



class sale_by_instalment:

    def __init__(self, customer_name: str, id_card: int, saled_product: str, the_product35: "the_product" = None):
        self.customer_name = customer_name
        self.id_card = id_card
        self.saled_product = saled_product
        self.the_product35 = the_product35
        
        pass
    @property
    def customer_name(self):
        return self.__customer_name
    @customer_name.setter
    def customer_name(self, customer_name: str):
        self.__customer_name = customer_name

    @property
    def id_card(self):
        return self.__id_card
    @id_card.setter
    def id_card(self, id_card: int):
        self.__id_card = id_card

    @property
    def saled_product(self):
        return self.__saled_product
    @saled_product.setter
    def saled_product(self, saled_product: str):
        self.__saled_product = saled_product

    @property
    def the_product35(self):
        return self.__the_product35
    @the_product35.setter
    def the_product35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sale_by_instalment__the_product35", None)
        self.__the_product35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sale_by_instalment34"):
                opp_val = getattr(old_value, "sale_by_instalment34", None)
                if opp_val == self:
                    setattr(old_value, "sale_by_instalment34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sale_by_instalment34"):
                opp_val = getattr(value, "sale_by_instalment34", None)
                setattr(value, "sale_by_instalment34", self)



class direct_sale:

    def __init__(self, username: str, saled_products: str, attribute: str, the_product33: "the_product" = None):
        self.username = username
        self.saled_products = saled_products
        self.attribute = attribute
        self.the_product33 = the_product33
        
        pass
    @property
    def saled_products(self):
        return self.__saled_products
    @saled_products.setter
    def saled_products(self, saled_products: str):
        self.__saled_products = saled_products

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def the_product33(self):
        return self.__the_product33
    @the_product33.setter
    def the_product33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_direct_sale__the_product33", None)
        self.__the_product33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "direct_sale32"):
                opp_val = getattr(old_value, "direct_sale32", None)
                if opp_val == self:
                    setattr(old_value, "direct_sale32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "direct_sale32"):
                opp_val = getattr(value, "direct_sale32", None)
                setattr(value, "direct_sale32", self)



class seller:

    def __init__(self, name: str, section_name: str, salary: int, number: int, section36: "section" = None):
        self.name = name
        self.section_name = section_name
        self.salary = salary
        self.number = number
        self.section36 = section36
        
        pass
    @property
    def section_name(self):
        return self.__section_name
    @section_name.setter
    def section_name(self, section_name: str):
        self.__section_name = section_name

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary: int):
        self.__salary = salary

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def section36(self):
        return self.__section36
    @section36.setter
    def section36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_seller__section36", None)
        self.__section36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seller37"):
                opp_val = getattr(old_value, "seller37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seller37"):
                opp_val = getattr(value, "seller37", None)
                if opp_val is None:
                    setattr(value, "seller37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class section:

    def __init__(self, name: str, number: int, seller37: set["seller"] = None):
        self.name = name
        self.number = number
        self.seller37 = seller37 if seller37 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def seller37(self):
        return self.__seller37
    @seller37.setter
    def seller37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_section__seller37", None)
        self.__seller37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "section36"):
                    opp_val = getattr(item, "section36", None)
                    
                    if opp_val == self:
                        setattr(item, "section36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "section36"):
                    opp_val = getattr(item, "section36", None)
                    
                    setattr(item, "section36", self)
                    



class online_market:

    def __init__(self, register_id_card: int, customer_address: str, customer_name: str, product_type: str, product_price: str, the_product29: "the_product" = None):
        self.register_id_card = register_id_card
        self.customer_address = customer_address
        self.customer_name = customer_name
        self.product_type = product_type
        self.product_price = product_price
        self.the_product29 = the_product29
        
        pass
    @property
    def customer_name(self):
        return self.__customer_name
    @customer_name.setter
    def customer_name(self, customer_name: str):
        self.__customer_name = customer_name

    @property
    def customer_address(self):
        return self.__customer_address
    @customer_address.setter
    def customer_address(self, customer_address: str):
        self.__customer_address = customer_address

    @property
    def register_id_card(self):
        return self.__register_id_card
    @register_id_card.setter
    def register_id_card(self, register_id_card: int):
        self.__register_id_card = register_id_card

    @property
    def product_price(self):
        return self.__product_price
    @product_price.setter
    def product_price(self, product_price: str):
        self.__product_price = product_price

    @property
    def product_type(self):
        return self.__product_type
    @product_type.setter
    def product_type(self, product_type: str):
        self.__product_type = product_type

    @property
    def the_product29(self):
        return self.__the_product29
    @the_product29.setter
    def the_product29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_market__the_product29", None)
        self.__the_product29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "online_market28"):
                opp_val = getattr(old_value, "online_market28", None)
                if opp_val == self:
                    setattr(old_value, "online_market28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "online_market28"):
                opp_val = getattr(value, "online_market28", None)
                setattr(value, "online_market28", self)



class the_product:

    def __init__(self, name: str, type: str, price: int, direct_sale32: "direct_sale" = None, sale_by_instalment34: "sale_by_instalment" = None, online_market28: "online_market" = None, customer30: "customer" = None):
        self.name = name
        self.type = type
        self.price = price
        self.direct_sale32 = direct_sale32
        self.sale_by_instalment34 = sale_by_instalment34
        self.online_market28 = online_market28
        self.customer30 = customer30
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def customer30(self):
        return self.__customer30
    @customer30.setter
    def customer30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_the_product__customer30", None)
        self.__customer30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "the_product31"):
                opp_val = getattr(old_value, "the_product31", None)
                if opp_val == self:
                    setattr(old_value, "the_product31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "the_product31"):
                opp_val = getattr(value, "the_product31", None)
                setattr(value, "the_product31", self)

    @property
    def sale_by_instalment34(self):
        return self.__sale_by_instalment34
    @sale_by_instalment34.setter
    def sale_by_instalment34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_the_product__sale_by_instalment34", None)
        self.__sale_by_instalment34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "the_product35"):
                opp_val = getattr(old_value, "the_product35", None)
                if opp_val == self:
                    setattr(old_value, "the_product35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "the_product35"):
                opp_val = getattr(value, "the_product35", None)
                setattr(value, "the_product35", self)

    @property
    def direct_sale32(self):
        return self.__direct_sale32
    @direct_sale32.setter
    def direct_sale32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_the_product__direct_sale32", None)
        self.__direct_sale32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "the_product33"):
                opp_val = getattr(old_value, "the_product33", None)
                if opp_val == self:
                    setattr(old_value, "the_product33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "the_product33"):
                opp_val = getattr(value, "the_product33", None)
                setattr(value, "the_product33", self)

    @property
    def online_market28(self):
        return self.__online_market28
    @online_market28.setter
    def online_market28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_the_product__online_market28", None)
        self.__online_market28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "the_product29"):
                opp_val = getattr(old_value, "the_product29", None)
                if opp_val == self:
                    setattr(old_value, "the_product29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "the_product29"):
                opp_val = getattr(value, "the_product29", None)
                setattr(value, "the_product29", self)

