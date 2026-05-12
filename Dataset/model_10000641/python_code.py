from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class OrderController:

    def __init__(self, Order: Order, OrderController_Order_018: "Order" = None):
        self.Order = Order
        self.OrderController_Order_018 = OrderController_Order_018
        
        pass
    @property
    def Order(self):
        return self.__Order
    @Order.setter
    def Order(self, Order: Order):
        self.__Order = Order

    @property
    def OrderController_Order_018(self):
        return self.__OrderController_Order_018
    @OrderController_Order_018.setter
    def OrderController_Order_018(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderController__OrderController_Order_018", None)
        self.__OrderController_Order_018 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OrderController_Order_119"):
                opp_val = getattr(old_value, "OrderController_Order_119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OrderController_Order_119"):
                opp_val = getattr(value, "OrderController_Order_119", None)
                if opp_val is None:
                    setattr(value, "OrderController_Order_119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class RestaurantController:

    def __init__(self, Restaurant: Restaurant, RestaurantManager_Restaurant_016: set["Restaurant"] = None):
        self.Restaurant = Restaurant
        self.RestaurantManager_Restaurant_016 = RestaurantManager_Restaurant_016 if RestaurantManager_Restaurant_016 is not None else set()
        
        pass
    @property
    def Restaurant(self):
        return self.__Restaurant
    @Restaurant.setter
    def Restaurant(self, Restaurant: Restaurant):
        self.__Restaurant = Restaurant

    @property
    def RestaurantManager_Restaurant_016(self):
        return self.__RestaurantManager_Restaurant_016
    @RestaurantManager_Restaurant_016.setter
    def RestaurantManager_Restaurant_016(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RestaurantController__RestaurantManager_Restaurant_016", None)
        self.__RestaurantManager_Restaurant_016 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RestaurantManager_Restaurant_117"):
                    opp_val = getattr(item, "RestaurantManager_Restaurant_117", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RestaurantManager_Restaurant_117"):
                    opp_val = getattr(item, "RestaurantManager_Restaurant_117", None)
                    
                    if opp_val is None:
                        setattr(item, "RestaurantManager_Restaurant_117", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Customer:

    def __init__(self, FullName: str, CreditCard: str, Cellphone: str, Address: str, PostCode: int, Order_Customer_115: set["Order"] = None):
        self.FullName = FullName
        self.CreditCard = CreditCard
        self.Cellphone = Cellphone
        self.Address = Address
        self.PostCode = PostCode
        self.Order_Customer_115 = Order_Customer_115 if Order_Customer_115 is not None else set()
        
        pass
    @property
    def PostCode(self):
        return self.__PostCode
    @PostCode.setter
    def PostCode(self, PostCode: int):
        self.__PostCode = PostCode

    @property
    def FullName(self):
        return self.__FullName
    @FullName.setter
    def FullName(self, FullName: str):
        self.__FullName = FullName

    @property
    def Cellphone(self):
        return self.__Cellphone
    @Cellphone.setter
    def Cellphone(self, Cellphone: str):
        self.__Cellphone = Cellphone

    @property
    def CreditCard(self):
        return self.__CreditCard
    @CreditCard.setter
    def CreditCard(self, CreditCard: str):
        self.__CreditCard = CreditCard

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Order_Customer_115(self):
        return self.__Order_Customer_115
    @Order_Customer_115.setter
    def Order_Customer_115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Order_Customer_115", None)
        self.__Order_Customer_115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Order_Customer_014"):
                    opp_val = getattr(item, "Order_Customer_014", None)
                    
                    if opp_val == self:
                        setattr(item, "Order_Customer_014", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Order_Customer_014"):
                    opp_val = getattr(item, "Order_Customer_014", None)
                    
                    setattr(item, "Order_Customer_014", self)
                    



class Order:

    def __init__(self, Restaurant: Restaurant, ItemList: MenuItem, Customer: Customer, Order_MenuItem_010: set["MenuItem"] = None, Order_Restaurant_012: "Restaurant" = None, OrderController_Order_119: set["OrderController"] = None, Order_Customer_014: "Customer" = None):
        self.Restaurant = Restaurant
        self.ItemList = ItemList
        self.Customer = Customer
        self.Order_MenuItem_010 = Order_MenuItem_010 if Order_MenuItem_010 is not None else set()
        self.Order_Restaurant_012 = Order_Restaurant_012
        self.OrderController_Order_119 = OrderController_Order_119 if OrderController_Order_119 is not None else set()
        self.Order_Customer_014 = Order_Customer_014
        
        pass
    @property
    def ItemList(self):
        return self.__ItemList
    @ItemList.setter
    def ItemList(self, ItemList: MenuItem):
        self.__ItemList = ItemList

    @property
    def Customer(self):
        return self.__Customer
    @Customer.setter
    def Customer(self, Customer: Customer):
        self.__Customer = Customer

    @property
    def Restaurant(self):
        return self.__Restaurant
    @Restaurant.setter
    def Restaurant(self, Restaurant: Restaurant):
        self.__Restaurant = Restaurant

    @property
    def Order_Customer_014(self):
        return self.__Order_Customer_014
    @Order_Customer_014.setter
    def Order_Customer_014(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__Order_Customer_014", None)
        self.__Order_Customer_014 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order_Customer_115"):
                opp_val = getattr(old_value, "Order_Customer_115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order_Customer_115"):
                opp_val = getattr(value, "Order_Customer_115", None)
                if opp_val is None:
                    setattr(value, "Order_Customer_115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Order_MenuItem_010(self):
        return self.__Order_MenuItem_010
    @Order_MenuItem_010.setter
    def Order_MenuItem_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__Order_MenuItem_010", None)
        self.__Order_MenuItem_010 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Order_MenuItem_111"):
                    opp_val = getattr(item, "Order_MenuItem_111", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Order_MenuItem_111"):
                    opp_val = getattr(item, "Order_MenuItem_111", None)
                    
                    if opp_val is None:
                        setattr(item, "Order_MenuItem_111", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Order_Restaurant_012(self):
        return self.__Order_Restaurant_012
    @Order_Restaurant_012.setter
    def Order_Restaurant_012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__Order_Restaurant_012", None)
        self.__Order_Restaurant_012 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order_Restaurant_113"):
                opp_val = getattr(old_value, "Order_Restaurant_113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order_Restaurant_113"):
                opp_val = getattr(value, "Order_Restaurant_113", None)
                if opp_val is None:
                    setattr(value, "Order_Restaurant_113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OrderController_Order_119(self):
        return self.__OrderController_Order_119
    @OrderController_Order_119.setter
    def OrderController_Order_119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__OrderController_Order_119", None)
        self.__OrderController_Order_119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OrderController_Order_018"):
                    opp_val = getattr(item, "OrderController_Order_018", None)
                    
                    if opp_val == self:
                        setattr(item, "OrderController_Order_018", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OrderController_Order_018"):
                    opp_val = getattr(item, "OrderController_Order_018", None)
                    
                    setattr(item, "OrderController_Order_018", self)
                    



class Food:

    def __init__(self, Price: int, Calories: int, Vegetarian: bool, FoodItem_Food_15: set["FoodItem"] = None, FoodPackage_Food_17: set["FoodPackage"] = None):
        self.Price = Price
        self.Calories = Calories
        self.Vegetarian = Vegetarian
        self.FoodItem_Food_15 = FoodItem_Food_15 if FoodItem_Food_15 is not None else set()
        self.FoodPackage_Food_17 = FoodPackage_Food_17 if FoodPackage_Food_17 is not None else set()
        
        pass
    @property
    def Vegetarian(self):
        return self.__Vegetarian
    @Vegetarian.setter
    def Vegetarian(self, Vegetarian: bool):
        self.__Vegetarian = Vegetarian

    @property
    def Calories(self):
        return self.__Calories
    @Calories.setter
    def Calories(self, Calories: int):
        self.__Calories = Calories

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: int):
        self.__Price = Price

    @property
    def FoodItem_Food_15(self):
        return self.__FoodItem_Food_15
    @FoodItem_Food_15.setter
    def FoodItem_Food_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Food__FoodItem_Food_15", None)
        self.__FoodItem_Food_15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FoodItem_Food_04"):
                    opp_val = getattr(item, "FoodItem_Food_04", None)
                    
                    if opp_val == self:
                        setattr(item, "FoodItem_Food_04", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FoodItem_Food_04"):
                    opp_val = getattr(item, "FoodItem_Food_04", None)
                    
                    setattr(item, "FoodItem_Food_04", self)
                    

    @property
    def FoodPackage_Food_17(self):
        return self.__FoodPackage_Food_17
    @FoodPackage_Food_17.setter
    def FoodPackage_Food_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Food__FoodPackage_Food_17", None)
        self.__FoodPackage_Food_17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FoodPackage_Food_06"):
                    opp_val = getattr(item, "FoodPackage_Food_06", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FoodPackage_Food_06"):
                    opp_val = getattr(item, "FoodPackage_Food_06", None)
                    
                    if opp_val is None:
                        setattr(item, "FoodPackage_Food_06", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class FoodItem:

    def __init__(self, Food: Food, FoodItem_Food_04: "Food" = None, MenuItem_FoodItem_11: set["MenuItem"] = None):
        self.Food = Food
        self.FoodItem_Food_04 = FoodItem_Food_04
        self.MenuItem_FoodItem_11 = MenuItem_FoodItem_11 if MenuItem_FoodItem_11 is not None else set()
        
        pass
    @property
    def Food(self):
        return self.__Food
    @Food.setter
    def Food(self, Food: Food):
        self.__Food = Food

    @property
    def FoodItem_Food_04(self):
        return self.__FoodItem_Food_04
    @FoodItem_Food_04.setter
    def FoodItem_Food_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FoodItem__FoodItem_Food_04", None)
        self.__FoodItem_Food_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FoodItem_Food_15"):
                opp_val = getattr(old_value, "FoodItem_Food_15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FoodItem_Food_15"):
                opp_val = getattr(value, "FoodItem_Food_15", None)
                if opp_val is None:
                    setattr(value, "FoodItem_Food_15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MenuItem_FoodItem_11(self):
        return self.__MenuItem_FoodItem_11
    @MenuItem_FoodItem_11.setter
    def MenuItem_FoodItem_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FoodItem__MenuItem_FoodItem_11", None)
        self.__MenuItem_FoodItem_11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MenuItem_FoodItem_00"):
                    opp_val = getattr(item, "MenuItem_FoodItem_00", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MenuItem_FoodItem_00"):
                    opp_val = getattr(item, "MenuItem_FoodItem_00", None)
                    
                    if opp_val is None:
                        setattr(item, "MenuItem_FoodItem_00", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class FoodPackage:

    def __init__(self, FoodList: Food, MenuItem_FoodPackage_13: set["MenuItem"] = None, FoodPackage_Food_06: set["Food"] = None):
        self.FoodList = FoodList
        self.MenuItem_FoodPackage_13 = MenuItem_FoodPackage_13 if MenuItem_FoodPackage_13 is not None else set()
        self.FoodPackage_Food_06 = FoodPackage_Food_06 if FoodPackage_Food_06 is not None else set()
        
        pass
    @property
    def FoodList(self):
        return self.__FoodList
    @FoodList.setter
    def FoodList(self, FoodList: Food):
        self.__FoodList = FoodList

    @property
    def MenuItem_FoodPackage_13(self):
        return self.__MenuItem_FoodPackage_13
    @MenuItem_FoodPackage_13.setter
    def MenuItem_FoodPackage_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FoodPackage__MenuItem_FoodPackage_13", None)
        self.__MenuItem_FoodPackage_13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MenuItem_FoodPackage_02"):
                    opp_val = getattr(item, "MenuItem_FoodPackage_02", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MenuItem_FoodPackage_02"):
                    opp_val = getattr(item, "MenuItem_FoodPackage_02", None)
                    
                    if opp_val is None:
                        setattr(item, "MenuItem_FoodPackage_02", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def FoodPackage_Food_06(self):
        return self.__FoodPackage_Food_06
    @FoodPackage_Food_06.setter
    def FoodPackage_Food_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FoodPackage__FoodPackage_Food_06", None)
        self.__FoodPackage_Food_06 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FoodPackage_Food_17"):
                    opp_val = getattr(item, "FoodPackage_Food_17", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FoodPackage_Food_17"):
                    opp_val = getattr(item, "FoodPackage_Food_17", None)
                    
                    if opp_val is None:
                        setattr(item, "FoodPackage_Food_17", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class MenuItem:

    def __init__(self, Description: str, MenuItem_FoodPackage_02: set["FoodPackage"] = None, Restaurant_MenuItem_19: set["Restaurant"] = None, Order_MenuItem_111: set["Order"] = None, MenuItem_FoodItem_00: set["FoodItem"] = None):
        self.Description = Description
        self.MenuItem_FoodPackage_02 = MenuItem_FoodPackage_02 if MenuItem_FoodPackage_02 is not None else set()
        self.Restaurant_MenuItem_19 = Restaurant_MenuItem_19 if Restaurant_MenuItem_19 is not None else set()
        self.Order_MenuItem_111 = Order_MenuItem_111 if Order_MenuItem_111 is not None else set()
        self.MenuItem_FoodItem_00 = MenuItem_FoodItem_00 if MenuItem_FoodItem_00 is not None else set()
        
        pass
    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def MenuItem_FoodItem_00(self):
        return self.__MenuItem_FoodItem_00
    @MenuItem_FoodItem_00.setter
    def MenuItem_FoodItem_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MenuItem__MenuItem_FoodItem_00", None)
        self.__MenuItem_FoodItem_00 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MenuItem_FoodItem_11"):
                    opp_val = getattr(item, "MenuItem_FoodItem_11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MenuItem_FoodItem_11"):
                    opp_val = getattr(item, "MenuItem_FoodItem_11", None)
                    
                    if opp_val is None:
                        setattr(item, "MenuItem_FoodItem_11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def MenuItem_FoodPackage_02(self):
        return self.__MenuItem_FoodPackage_02
    @MenuItem_FoodPackage_02.setter
    def MenuItem_FoodPackage_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MenuItem__MenuItem_FoodPackage_02", None)
        self.__MenuItem_FoodPackage_02 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MenuItem_FoodPackage_13"):
                    opp_val = getattr(item, "MenuItem_FoodPackage_13", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MenuItem_FoodPackage_13"):
                    opp_val = getattr(item, "MenuItem_FoodPackage_13", None)
                    
                    if opp_val is None:
                        setattr(item, "MenuItem_FoodPackage_13", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Restaurant_MenuItem_19(self):
        return self.__Restaurant_MenuItem_19
    @Restaurant_MenuItem_19.setter
    def Restaurant_MenuItem_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MenuItem__Restaurant_MenuItem_19", None)
        self.__Restaurant_MenuItem_19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Restaurant_MenuItem_08"):
                    opp_val = getattr(item, "Restaurant_MenuItem_08", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Restaurant_MenuItem_08"):
                    opp_val = getattr(item, "Restaurant_MenuItem_08", None)
                    
                    if opp_val is None:
                        setattr(item, "Restaurant_MenuItem_08", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Order_MenuItem_111(self):
        return self.__Order_MenuItem_111
    @Order_MenuItem_111.setter
    def Order_MenuItem_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MenuItem__Order_MenuItem_111", None)
        self.__Order_MenuItem_111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Order_MenuItem_010"):
                    opp_val = getattr(item, "Order_MenuItem_010", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Order_MenuItem_010"):
                    opp_val = getattr(item, "Order_MenuItem_010", None)
                    
                    if opp_val is None:
                        setattr(item, "Order_MenuItem_010", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Restaurant:

    def __init__(self, Name: str, Address: str, PostCode: int, Menu: MenuItem, Restaurant_MenuItem_08: set["MenuItem"] = None, Order_Restaurant_113: set["Order"] = None, RestaurantManager_Restaurant_117: set["RestaurantController"] = None):
        self.Name = Name
        self.Address = Address
        self.PostCode = PostCode
        self.Menu = Menu
        self.Restaurant_MenuItem_08 = Restaurant_MenuItem_08 if Restaurant_MenuItem_08 is not None else set()
        self.Order_Restaurant_113 = Order_Restaurant_113 if Order_Restaurant_113 is not None else set()
        self.RestaurantManager_Restaurant_117 = RestaurantManager_Restaurant_117 if RestaurantManager_Restaurant_117 is not None else set()
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Menu(self):
        return self.__Menu
    @Menu.setter
    def Menu(self, Menu: MenuItem):
        self.__Menu = Menu

    @property
    def PostCode(self):
        return self.__PostCode
    @PostCode.setter
    def PostCode(self, PostCode: int):
        self.__PostCode = PostCode

    @property
    def RestaurantManager_Restaurant_117(self):
        return self.__RestaurantManager_Restaurant_117
    @RestaurantManager_Restaurant_117.setter
    def RestaurantManager_Restaurant_117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Restaurant__RestaurantManager_Restaurant_117", None)
        self.__RestaurantManager_Restaurant_117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RestaurantManager_Restaurant_016"):
                    opp_val = getattr(item, "RestaurantManager_Restaurant_016", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RestaurantManager_Restaurant_016"):
                    opp_val = getattr(item, "RestaurantManager_Restaurant_016", None)
                    
                    if opp_val is None:
                        setattr(item, "RestaurantManager_Restaurant_016", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Restaurant_MenuItem_08(self):
        return self.__Restaurant_MenuItem_08
    @Restaurant_MenuItem_08.setter
    def Restaurant_MenuItem_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Restaurant__Restaurant_MenuItem_08", None)
        self.__Restaurant_MenuItem_08 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Restaurant_MenuItem_19"):
                    opp_val = getattr(item, "Restaurant_MenuItem_19", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Restaurant_MenuItem_19"):
                    opp_val = getattr(item, "Restaurant_MenuItem_19", None)
                    
                    if opp_val is None:
                        setattr(item, "Restaurant_MenuItem_19", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Order_Restaurant_113(self):
        return self.__Order_Restaurant_113
    @Order_Restaurant_113.setter
    def Order_Restaurant_113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Restaurant__Order_Restaurant_113", None)
        self.__Order_Restaurant_113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Order_Restaurant_012"):
                    opp_val = getattr(item, "Order_Restaurant_012", None)
                    
                    if opp_val == self:
                        setattr(item, "Order_Restaurant_012", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Order_Restaurant_012"):
                    opp_val = getattr(item, "Order_Restaurant_012", None)
                    
                    setattr(item, "Order_Restaurant_012", self)
                    

