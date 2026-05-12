from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Management_Actor:

    pass


class Bar_Staff_Actor:

    pass


class Kitchen_Staff_Actor:

    pass


class Waiter_Actor:

    pass


class Diner_Actor:

    pass


class View_statistics_UseCase:

    pass


class Change_Order_UseCase:

    pass


class Input_payment_details_UseCase:

    pass


class Grant_discount_UseCase:

    pass


class Pay_for_food_UseCase:

    pass


class Alerted_to_Prepare_drinks_UseCase:

    pass


class Print_bill_UseCase:

    pass


class Alerted_to_Serve_Food_UseCase:

    pass


class Alerted_to_Serve_drinks_UseCase:

    pass


class Alerted_to_Prepare_food_UseCase:

    pass


class Order_food_UseCase:

    pass


class Input_Order_UseCase:

    pass





class Drinks:

    def __init__(self, softDrink: str, beer: str, wine: str, spirits: str, cocktail: str, Order_Drinks_19: "Order" = None):
        self.softDrink = softDrink
        self.beer = beer
        self.wine = wine
        self.spirits = spirits
        self.cocktail = cocktail
        self.Order_Drinks_19 = Order_Drinks_19
        
        pass
    @property
    def wine(self):
        return self.__wine
    @wine.setter
    def wine(self, wine: str):
        self.__wine = wine

    @property
    def spirits(self):
        return self.__spirits
    @spirits.setter
    def spirits(self, spirits: str):
        self.__spirits = spirits

    @property
    def cocktail(self):
        return self.__cocktail
    @cocktail.setter
    def cocktail(self, cocktail: str):
        self.__cocktail = cocktail

    @property
    def softDrink(self):
        return self.__softDrink
    @softDrink.setter
    def softDrink(self, softDrink: str):
        self.__softDrink = softDrink

    @property
    def beer(self):
        return self.__beer
    @beer.setter
    def beer(self, beer: str):
        self.__beer = beer

    @property
    def Order_Drinks_19(self):
        return self.__Order_Drinks_19
    @Order_Drinks_19.setter
    def Order_Drinks_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Drinks__Order_Drinks_19", None)
        self.__Order_Drinks_19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order_Drinks_08"):
                opp_val = getattr(old_value, "Order_Drinks_08", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order_Drinks_08"):
                opp_val = getattr(value, "Order_Drinks_08", None)
                if opp_val is None:
                    setattr(value, "Order_Drinks_08", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Menu:

    def __init__(self, starter: str, mainCourse: str, desert: str, specialCourse: str, Order_Menu_17: "Order" = None):
        self.starter = starter
        self.mainCourse = mainCourse
        self.desert = desert
        self.specialCourse = specialCourse
        self.Order_Menu_17 = Order_Menu_17
        
        pass
    @property
    def starter(self):
        return self.__starter
    @starter.setter
    def starter(self, starter: str):
        self.__starter = starter

    @property
    def desert(self):
        return self.__desert
    @desert.setter
    def desert(self, desert: str):
        self.__desert = desert

    @property
    def specialCourse(self):
        return self.__specialCourse
    @specialCourse.setter
    def specialCourse(self, specialCourse: str):
        self.__specialCourse = specialCourse

    @property
    def mainCourse(self):
        return self.__mainCourse
    @mainCourse.setter
    def mainCourse(self, mainCourse: str):
        self.__mainCourse = mainCourse

    @property
    def Order_Menu_17(self):
        return self.__Order_Menu_17
    @Order_Menu_17.setter
    def Order_Menu_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu__Order_Menu_17", None)
        self.__Order_Menu_17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order_Menu_06"):
                opp_val = getattr(old_value, "Order_Menu_06", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order_Menu_06"):
                opp_val = getattr(value, "Order_Menu_06", None)
                if opp_val is None:
                    setattr(value, "Order_Menu_06", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order:

    pass


class Table:

    def __init__(self, tableID: int, Bill_Table_13: "Bill" = None):
        self.tableID = tableID
        self.Bill_Table_13 = Bill_Table_13
        
        pass
    @property
    def tableID(self):
        return self.__tableID
    @tableID.setter
    def tableID(self, tableID: int):
        self.__tableID = tableID

    @property
    def Bill_Table_13(self):
        return self.__Bill_Table_13
    @Bill_Table_13.setter
    def Bill_Table_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__Bill_Table_13", None)
        self.__Bill_Table_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bill_Table_02"):
                opp_val = getattr(old_value, "Bill_Table_02", None)
                if opp_val == self:
                    setattr(old_value, "Bill_Table_02", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bill_Table_02"):
                opp_val = getattr(value, "Bill_Table_02", None)
                setattr(value, "Bill_Table_02", self)



class Payment:

    def __init__(self, paymentType: str, bill1: set["Bill"] = None):
        self.paymentType = paymentType
        self.bill1 = bill1 if bill1 is not None else set()
        
        pass
    @property
    def paymentType(self):
        return self.__paymentType
    @paymentType.setter
    def paymentType(self, paymentType: str):
        self.__paymentType = paymentType

    @property
    def bill1(self):
        return self.__bill1
    @bill1.setter
    def bill1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__bill1", None)
        self.__bill1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "payment0"):
                    opp_val = getattr(item, "payment0", None)
                    
                    if opp_val == self:
                        setattr(item, "payment0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "payment0"):
                    opp_val = getattr(item, "payment0", None)
                    
                    setattr(item, "payment0", self)
                    



class Bill:

    pass


class Print_bill_external:

    pass


class Alerted_to_Serve_Food_external:

    pass


class Alerted_to_Serve_drinks_external:

    pass


class Input_Order_external:

    pass


class View_statistics_external:

    pass


class Grant_discount_external:

    pass


class Alerted_to_Prepare_drinks_external:

    pass


class Alerted_to_Prepare_food_external:

    pass


class Input_payment_details_external:

    pass


class Pay_for_food_UseCase1:

    pass


class Order_food_UseCase1:

    pass


class _Component:

    pass


class Discount:

    def __init__(self, discountAmount: int, bill11: "Bill" = None):
        self.discountAmount = discountAmount
        self.bill11 = bill11
        
        pass
    @property
    def discountAmount(self):
        return self.__discountAmount
    @discountAmount.setter
    def discountAmount(self, discountAmount: int):
        self.__discountAmount = discountAmount

    @property
    def bill11(self):
        return self.__bill11
    @bill11.setter
    def bill11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Discount__bill11", None)
        self.__bill11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "discount10"):
                opp_val = getattr(old_value, "discount10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "discount10"):
                opp_val = getattr(value, "discount10", None)
                if opp_val is None:
                    setattr(value, "discount10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

