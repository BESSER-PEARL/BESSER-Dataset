from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class PayAt_Delivery_UseCase:

    pass


class Add_new_address_UseCase:

    pass


class Pre_order_UseCase:

    pass


class Admin_Actor:

    pass


class Manage_accounts_UseCase:

    pass


class Edit_menu_UseCase:

    pass


class Deliver_pizza_UseCase:

    pass


class Cook_Pizza_UseCase:

    pass


class Receive_order_UseCase:

    pass


class Delivery_person_Actor:

    pass


class Pizza_Chef_Actor:

    pass


class Order_tracking_UseCase:

    pass


class Make_Payment_UseCase:

    pass


class Save_favourite_order_UseCase:

    pass


class Pay_online_UseCase:

    pass


class Checkout_UseCase:

    pass


class Search_store_locations_UseCase:

    pass


class Change_toppings_UseCase:

    pass


class Create_Account_UseCase:

    pass


class View_side_orders_UseCase:

    pass


class Add_item_UseCase:

    pass


class Create_your_own_pizza_UseCase:

    pass


class View_Pizza_types_UseCase:

    pass


class View_Meal_Deal_UseCase:

    pass


class Sign_In_UseCase:

    pass


class Registered_User_Actor:

    pass





class Menu:

    def __init__(self, Quantity: str, toppings: str, assoc_137: "Online_pizza_ordering" = None):
        self.Quantity = Quantity
        self.toppings = toppings
        self.assoc_137 = assoc_137
        
        pass
    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: str):
        self.__Quantity = Quantity

    @property
    def toppings(self):
        return self.__toppings
    @toppings.setter
    def toppings(self, toppings: str):
        self.__toppings = toppings

    @property
    def assoc_137(self):
        return self.__assoc_137
    @assoc_137.setter
    def assoc_137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu__assoc_137", None)
        self.__assoc_137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assoc_036"):
                opp_val = getattr(old_value, "assoc_036", None)
                if opp_val == self:
                    setattr(old_value, "assoc_036", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assoc_036"):
                opp_val = getattr(value, "assoc_036", None)
                setattr(value, "assoc_036", self)



class Online_pizza_ordering:

    def __init__(self, Price: float, pizza_type: str, Ingredients: str, Customer_Online_pizza_ordering_131: set["Customer"] = None, assoc_032: "Admin" = None, assoc_036: "Menu" = None):
        self.Price = Price
        self.pizza_type = pizza_type
        self.Ingredients = Ingredients
        self.Customer_Online_pizza_ordering_131 = Customer_Online_pizza_ordering_131 if Customer_Online_pizza_ordering_131 is not None else set()
        self.assoc_032 = assoc_032
        self.assoc_036 = assoc_036
        
        pass
    @property
    def Ingredients(self):
        return self.__Ingredients
    @Ingredients.setter
    def Ingredients(self, Ingredients: str):
        self.__Ingredients = Ingredients

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
    def assoc_036(self):
        return self.__assoc_036
    @assoc_036.setter
    def assoc_036(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_pizza_ordering__assoc_036", None)
        self.__assoc_036 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assoc_137"):
                opp_val = getattr(old_value, "assoc_137", None)
                if opp_val == self:
                    setattr(old_value, "assoc_137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assoc_137"):
                opp_val = getattr(value, "assoc_137", None)
                setattr(value, "assoc_137", self)

    @property
    def assoc_032(self):
        return self.__assoc_032
    @assoc_032.setter
    def assoc_032(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_pizza_ordering__assoc_032", None)
        self.__assoc_032 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assoc_133"):
                opp_val = getattr(old_value, "assoc_133", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assoc_133"):
                opp_val = getattr(value, "assoc_133", None)
                if opp_val is None:
                    setattr(value, "assoc_133", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Customer_Online_pizza_ordering_131(self):
        return self.__Customer_Online_pizza_ordering_131
    @Customer_Online_pizza_ordering_131.setter
    def Customer_Online_pizza_ordering_131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_pizza_ordering__Customer_Online_pizza_ordering_131", None)
        self.__Customer_Online_pizza_ordering_131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Customer_Online_pizza_ordering_030"):
                    opp_val = getattr(item, "Customer_Online_pizza_ordering_030", None)
                    
                    if opp_val == self:
                        setattr(item, "Customer_Online_pizza_ordering_030", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Customer_Online_pizza_ordering_030"):
                    opp_val = getattr(item, "Customer_Online_pizza_ordering_030", None)
                    
                    setattr(item, "Customer_Online_pizza_ordering_030", self)
                    



class Online_payment_methods:

    pass


class Pay_cash_on_deliver:

    pass


class Payment:

    pass


class Admin:

    pass


class Customer:

    def __init__(self, Password: str, Name: str, Customer_Online_pizza_ordering_030: "Online_pizza_ordering" = None, assoc_034: set["Payment"] = None):
        self.Password = Password
        self.Name = Name
        self.Customer_Online_pizza_ordering_030 = Customer_Online_pizza_ordering_030
        self.assoc_034 = assoc_034 if assoc_034 is not None else set()
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def assoc_034(self):
        return self.__assoc_034
    @assoc_034.setter
    def assoc_034(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__assoc_034", None)
        self.__assoc_034 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "assoc_135"):
                    opp_val = getattr(item, "assoc_135", None)
                    
                    if opp_val == self:
                        setattr(item, "assoc_135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "assoc_135"):
                    opp_val = getattr(item, "assoc_135", None)
                    
                    setattr(item, "assoc_135", self)
                    

    @property
    def Customer_Online_pizza_ordering_030(self):
        return self.__Customer_Online_pizza_ordering_030
    @Customer_Online_pizza_ordering_030.setter
    def Customer_Online_pizza_ordering_030(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Customer_Online_pizza_ordering_030", None)
        self.__Customer_Online_pizza_ordering_030 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_Online_pizza_ordering_131"):
                opp_val = getattr(old_value, "Customer_Online_pizza_ordering_131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_Online_pizza_ordering_131"):
                opp_val = getattr(value, "Customer_Online_pizza_ordering_131", None)
                if opp_val is None:
                    setattr(value, "Customer_Online_pizza_ordering_131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

