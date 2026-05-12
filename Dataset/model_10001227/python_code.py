from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Customer_Actor:

    pass


class Add_pizza_UseCase:

    pass


class View_feedback_UseCase:

    pass


class View_pizza_sales_UseCase:

    pass


class Update_order_UseCase:

    pass


class Change_password_UseCase:

    pass


class Write_feedback_UseCase:

    pass


class Pay_At_delivery_UseCase:

    pass


class Pay_online_UseCase:

    pass


class Make_payment_UseCase:

    pass


class Add_to_cart_and_buy_UseCase:

    pass


class Registration_UseCase:

    pass


class Visit_home_page_UseCase:

    pass


class Admin_Actor:

    pass


class Manage_accounts_UseCase:

    pass


class Edit____delete___view_menu_UseCase:

    pass


class Order_tracking_UseCase:

    pass


class Change_toppings_UseCase:

    pass


class View_side_orders_UseCase:

    pass


class Add_item_UseCase:

    pass


class Create_your_own_pizza_UseCase:

    pass


class View_Pizza_types_UseCase:

    pass


class Log_In_UseCase:

    pass





class Menu:

    def __init__(self, Quantity: str, toppings: str, assoc_119: "Online_pizza_ordering" = None):
        self.Quantity = Quantity
        self.toppings = toppings
        self.assoc_119 = assoc_119
        
        pass
    @property
    def toppings(self):
        return self.__toppings
    @toppings.setter
    def toppings(self, toppings: str):
        self.__toppings = toppings

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: str):
        self.__Quantity = Quantity

    @property
    def assoc_119(self):
        return self.__assoc_119
    @assoc_119.setter
    def assoc_119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu__assoc_119", None)
        self.__assoc_119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assoc_018"):
                opp_val = getattr(old_value, "assoc_018", None)
                if opp_val == self:
                    setattr(old_value, "assoc_018", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assoc_018"):
                opp_val = getattr(value, "assoc_018", None)
                setattr(value, "assoc_018", self)



class Online_pizza_ordering:

    def __init__(self, Price: float, pizza_type: str, Ingredients: str, Customer_Online_pizza_ordering_113: set["Customer"] = None, assoc_014: "Admin" = None, assoc_018: "Menu" = None):
        self.Price = Price
        self.pizza_type = pizza_type
        self.Ingredients = Ingredients
        self.Customer_Online_pizza_ordering_113 = Customer_Online_pizza_ordering_113 if Customer_Online_pizza_ordering_113 is not None else set()
        self.assoc_014 = assoc_014
        self.assoc_018 = assoc_018
        
        pass
    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: float):
        self.__Price = Price

    @property
    def pizza_type(self):
        return self.__pizza_type
    @pizza_type.setter
    def pizza_type(self, pizza_type: str):
        self.__pizza_type = pizza_type

    @property
    def Ingredients(self):
        return self.__Ingredients
    @Ingredients.setter
    def Ingredients(self, Ingredients: str):
        self.__Ingredients = Ingredients

    @property
    def assoc_014(self):
        return self.__assoc_014
    @assoc_014.setter
    def assoc_014(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_pizza_ordering__assoc_014", None)
        self.__assoc_014 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assoc_115"):
                opp_val = getattr(old_value, "assoc_115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assoc_115"):
                opp_val = getattr(value, "assoc_115", None)
                if opp_val is None:
                    setattr(value, "assoc_115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Customer_Online_pizza_ordering_113(self):
        return self.__Customer_Online_pizza_ordering_113
    @Customer_Online_pizza_ordering_113.setter
    def Customer_Online_pizza_ordering_113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_pizza_ordering__Customer_Online_pizza_ordering_113", None)
        self.__Customer_Online_pizza_ordering_113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Customer_Online_pizza_ordering_012"):
                    opp_val = getattr(item, "Customer_Online_pizza_ordering_012", None)
                    
                    if opp_val == self:
                        setattr(item, "Customer_Online_pizza_ordering_012", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Customer_Online_pizza_ordering_012"):
                    opp_val = getattr(item, "Customer_Online_pizza_ordering_012", None)
                    
                    setattr(item, "Customer_Online_pizza_ordering_012", self)
                    

    @property
    def assoc_018(self):
        return self.__assoc_018
    @assoc_018.setter
    def assoc_018(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_pizza_ordering__assoc_018", None)
        self.__assoc_018 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assoc_119"):
                opp_val = getattr(old_value, "assoc_119", None)
                if opp_val == self:
                    setattr(old_value, "assoc_119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assoc_119"):
                opp_val = getattr(value, "assoc_119", None)
                setattr(value, "assoc_119", self)



class Online_payment_methods:

    pass


class Pay_cash_on_deliver:

    pass


class Payment:

    pass


class Admin:

    pass


class Customer:

    def __init__(self, Password: str, Name: str, Customer_Online_pizza_ordering_012: "Online_pizza_ordering" = None, assoc_016: set["Payment"] = None):
        self.Password = Password
        self.Name = Name
        self.Customer_Online_pizza_ordering_012 = Customer_Online_pizza_ordering_012
        self.assoc_016 = assoc_016 if assoc_016 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Customer_Online_pizza_ordering_012(self):
        return self.__Customer_Online_pizza_ordering_012
    @Customer_Online_pizza_ordering_012.setter
    def Customer_Online_pizza_ordering_012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Customer_Online_pizza_ordering_012", None)
        self.__Customer_Online_pizza_ordering_012 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_Online_pizza_ordering_113"):
                opp_val = getattr(old_value, "Customer_Online_pizza_ordering_113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_Online_pizza_ordering_113"):
                opp_val = getattr(value, "Customer_Online_pizza_ordering_113", None)
                if opp_val is None:
                    setattr(value, "Customer_Online_pizza_ordering_113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def assoc_016(self):
        return self.__assoc_016
    @assoc_016.setter
    def assoc_016(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__assoc_016", None)
        self.__assoc_016 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "assoc_117"):
                    opp_val = getattr(item, "assoc_117", None)
                    
                    if opp_val == self:
                        setattr(item, "assoc_117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "assoc_117"):
                    opp_val = getattr(item, "assoc_117", None)
                    
                    setattr(item, "assoc_117", self)
                    

