from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Menu:

    def __init__(self, foodItem: FoodItem, drinksItem: DrinksItem, category: str, menuItem4: "MenuItem" = None):
        self.foodItem = foodItem
        self.drinksItem = drinksItem
        self.category = category
        self.menuItem4 = menuItem4
        
        pass
    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def drinksItem(self):
        return self.__drinksItem
    @drinksItem.setter
    def drinksItem(self, drinksItem: DrinksItem):
        self.__drinksItem = drinksItem

    @property
    def foodItem(self):
        return self.__foodItem
    @foodItem.setter
    def foodItem(self, foodItem: FoodItem):
        self.__foodItem = foodItem

    @property
    def menuItem4(self):
        return self.__menuItem4
    @menuItem4.setter
    def menuItem4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu__menuItem4", None)
        self.__menuItem4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu5"):
                opp_val = getattr(old_value, "menu5", None)
                if opp_val == self:
                    setattr(old_value, "menu5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu5"):
                opp_val = getattr(value, "menu5", None)
                setattr(value, "menu5", self)



class MenuItem:

    def __init__(self, item_Id: int, item_price: int, available: bool, quantity: int, item_description: str, menu5: "Menu" = None):
        self.item_Id = item_Id
        self.item_price = item_price
        self.available = available
        self.quantity = quantity
        self.item_description = item_description
        self.menu5 = menu5
        
        pass
    @property
    def item_description(self):
        return self.__item_description
    @item_description.setter
    def item_description(self, item_description: str):
        self.__item_description = item_description

    @property
    def item_price(self):
        return self.__item_price
    @item_price.setter
    def item_price(self, item_price: int):
        self.__item_price = item_price

    @property
    def available(self):
        return self.__available
    @available.setter
    def available(self, available: bool):
        self.__available = available

    @property
    def item_Id(self):
        return self.__item_Id
    @item_Id.setter
    def item_Id(self, item_Id: int):
        self.__item_Id = item_Id

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def menu5(self):
        return self.__menu5
    @menu5.setter
    def menu5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MenuItem__menu5", None)
        self.__menu5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menuItem4"):
                opp_val = getattr(old_value, "menuItem4", None)
                if opp_val == self:
                    setattr(old_value, "menuItem4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menuItem4"):
                opp_val = getattr(value, "menuItem4", None)
                setattr(value, "menuItem4", self)



class FoodItem:

    def __init__(self, drinkType: str, order2: "Order" = None):
        self.drinkType = drinkType
        self.order2 = order2
        
        pass
    @property
    def drinkType(self):
        return self.__drinkType
    @drinkType.setter
    def drinkType(self, drinkType: str):
        self.__drinkType = drinkType

    @property
    def order2(self):
        return self.__order2
    @order2.setter
    def order2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FoodItem__order2", None)
        self.__order2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foodItem23"):
                opp_val = getattr(old_value, "foodItem23", None)
                if opp_val == self:
                    setattr(old_value, "foodItem23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foodItem23"):
                opp_val = getattr(value, "foodItem23", None)
                setattr(value, "foodItem23", self)



class DrinksItem:

    def __init__(self, drinkType: str, order0: "Order" = None):
        self.drinkType = drinkType
        self.order0 = order0
        
        pass
    @property
    def drinkType(self):
        return self.__drinkType
    @drinkType.setter
    def drinkType(self, drinkType: str):
        self.__drinkType = drinkType

    @property
    def order0(self):
        return self.__order0
    @order0.setter
    def order0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DrinksItem__order0", None)
        self.__order0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drinksItem21"):
                opp_val = getattr(old_value, "drinksItem21", None)
                if opp_val == self:
                    setattr(old_value, "drinksItem21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drinksItem21"):
                opp_val = getattr(value, "drinksItem21", None)
                setattr(value, "drinksItem21", self)



class Customer:

    def __init__(self, cust_name: str, cust_Id: str):
        self.cust_name = cust_name
        self.cust_Id = cust_Id
        
        pass
    @property
    def cust_name(self):
        return self.__cust_name
    @cust_name.setter
    def cust_name(self, cust_name: str):
        self.__cust_name = cust_name

    @property
    def cust_Id(self):
        return self.__cust_Id
    @cust_Id.setter
    def cust_Id(self, cust_Id: str):
        self.__cust_Id = cust_Id



class Order:

    def __init__(self, order_Id: str, cust_id: str, cust_name: str, numTable: int, foodItem: FoodItem, drinksItem: DrinksItem, drinksItem21: "DrinksItem" = None, foodItem23: "FoodItem" = None):
        self.order_Id = order_Id
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.numTable = numTable
        self.foodItem = foodItem
        self.drinksItem = drinksItem
        self.drinksItem21 = drinksItem21
        self.foodItem23 = foodItem23
        
        pass
    @property
    def order_Id(self):
        return self.__order_Id
    @order_Id.setter
    def order_Id(self, order_Id: str):
        self.__order_Id = order_Id

    @property
    def drinksItem(self):
        return self.__drinksItem
    @drinksItem.setter
    def drinksItem(self, drinksItem: DrinksItem):
        self.__drinksItem = drinksItem

    @property
    def cust_id(self):
        return self.__cust_id
    @cust_id.setter
    def cust_id(self, cust_id: str):
        self.__cust_id = cust_id

    @property
    def numTable(self):
        return self.__numTable
    @numTable.setter
    def numTable(self, numTable: int):
        self.__numTable = numTable

    @property
    def foodItem(self):
        return self.__foodItem
    @foodItem.setter
    def foodItem(self, foodItem: FoodItem):
        self.__foodItem = foodItem

    @property
    def cust_name(self):
        return self.__cust_name
    @cust_name.setter
    def cust_name(self, cust_name: str):
        self.__cust_name = cust_name

    @property
    def foodItem23(self):
        return self.__foodItem23
    @foodItem23.setter
    def foodItem23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__foodItem23", None)
        self.__foodItem23 = value
        
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
    def drinksItem21(self):
        return self.__drinksItem21
    @drinksItem21.setter
    def drinksItem21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__drinksItem21", None)
        self.__drinksItem21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order0"):
                opp_val = getattr(old_value, "order0", None)
                if opp_val == self:
                    setattr(old_value, "order0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order0"):
                opp_val = getattr(value, "order0", None)
                setattr(value, "order0", self)



class Report:

    def __init__(self, profit: str, orders: str, totalSales: str):
        self.profit = profit
        self.orders = orders
        self.totalSales = totalSales
        
        pass
    @property
    def totalSales(self):
        return self.__totalSales
    @totalSales.setter
    def totalSales(self, totalSales: str):
        self.__totalSales = totalSales

    @property
    def profit(self):
        return self.__profit
    @profit.setter
    def profit(self, profit: str):
        self.__profit = profit

    @property
    def orders(self):
        return self.__orders
    @orders.setter
    def orders(self, orders: str):
        self.__orders = orders



class Kasir:

    def __init__(self, order_id: str, cust_id: str):
        self.order_id = order_id
        self.cust_id = cust_id
        
        pass
    @property
    def cust_id(self):
        return self.__cust_id
    @cust_id.setter
    def cust_id(self, cust_id: str):
        self.__cust_id = cust_id

    @property
    def order_id(self):
        return self.__order_id
    @order_id.setter
    def order_id(self, order_id: str):
        self.__order_id = order_id



class Karyawan:

    def __init__(self, staff_Id: str, name: str, contact: str):
        self.staff_Id = staff_Id
        self.name = name
        self.contact = contact
        
        pass
    @property
    def staff_Id(self):
        return self.__staff_Id
    @staff_Id.setter
    def staff_Id(self, staff_Id: str):
        self.__staff_Id = staff_Id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def contact(self):
        return self.__contact
    @contact.setter
    def contact(self, contact: str):
        self.__contact = contact



class Bartender:

    def __init__(self, staff_Id: str, name: str):
        self.staff_Id = staff_Id
        self.name = name
        
        pass
    @property
    def staff_Id(self):
        return self.__staff_Id
    @staff_Id.setter
    def staff_Id(self, staff_Id: str):
        self.__staff_Id = staff_Id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class Chef:

    def __init__(self, staff_Id: str, name: str):
        self.staff_Id = staff_Id
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def staff_Id(self):
        return self.__staff_Id
    @staff_Id.setter
    def staff_Id(self, staff_Id: str):
        self.__staff_Id = staff_Id



class Manager_Owner:

    pass
