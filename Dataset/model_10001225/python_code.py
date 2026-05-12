from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class customer:

    pass


class manger:

    pass


class Chef:

    pass


class system:

    def __init__(self, user_id: str, name: str, app8: "app" = None, chef11: "Chef" = None, manger13: "manger" = None):
        self.user_id = user_id
        self.name = name
        self.app8 = app8
        self.chef11 = chef11
        self.manger13 = manger13
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: str):
        self.__user_id = user_id

    @property
    def chef11(self):
        return self.__chef11
    @chef11.setter
    def chef11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_system__chef11", None)
        self.__chef11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system10"):
                opp_val = getattr(old_value, "system10", None)
                if opp_val == self:
                    setattr(old_value, "system10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system10"):
                opp_val = getattr(value, "system10", None)
                setattr(value, "system10", self)

    @property
    def manger13(self):
        return self.__manger13
    @manger13.setter
    def manger13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_system__manger13", None)
        self.__manger13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system12"):
                opp_val = getattr(old_value, "system12", None)
                if opp_val == self:
                    setattr(old_value, "system12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system12"):
                opp_val = getattr(value, "system12", None)
                setattr(value, "system12", self)

    @property
    def app8(self):
        return self.__app8
    @app8.setter
    def app8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_system__app8", None)
        self.__app8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system9"):
                opp_val = getattr(old_value, "system9", None)
                if opp_val == self:
                    setattr(old_value, "system9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system9"):
                opp_val = getattr(value, "system9", None)
                setattr(value, "system9", self)



class app:

    def __init__(self, user_id: str, name: str, table5: "Table" = None, order6: "Order" = None, system9: "system" = None, waiter17: "Waiter" = None):
        self.user_id = user_id
        self.name = name
        self.table5 = table5
        self.order6 = order6
        self.system9 = system9
        self.waiter17 = waiter17
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: str):
        self.__user_id = user_id

    @property
    def system9(self):
        return self.__system9
    @system9.setter
    def system9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_app__system9", None)
        self.__system9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "app8"):
                opp_val = getattr(old_value, "app8", None)
                if opp_val == self:
                    setattr(old_value, "app8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "app8"):
                opp_val = getattr(value, "app8", None)
                setattr(value, "app8", self)

    @property
    def order6(self):
        return self.__order6
    @order6.setter
    def order6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_app__order6", None)
        self.__order6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "app7"):
                opp_val = getattr(old_value, "app7", None)
                if opp_val == self:
                    setattr(old_value, "app7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "app7"):
                opp_val = getattr(value, "app7", None)
                setattr(value, "app7", self)

    @property
    def table5(self):
        return self.__table5
    @table5.setter
    def table5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_app__table5", None)
        self.__table5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "app4"):
                opp_val = getattr(old_value, "app4", None)
                if opp_val == self:
                    setattr(old_value, "app4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "app4"):
                opp_val = getattr(value, "app4", None)
                setattr(value, "app4", self)

    @property
    def waiter17(self):
        return self.__waiter17
    @waiter17.setter
    def waiter17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_app__waiter17", None)
        self.__waiter17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "app16"):
                opp_val = getattr(old_value, "app16", None)
                if opp_val == self:
                    setattr(old_value, "app16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "app16"):
                opp_val = getattr(value, "app16", None)
                setattr(value, "app16", self)



class Waiter:

    pass


class meal:

    def __init__(self, meal_id: str, name: str, price: float, prepared: bool, served: bool, has1: "Order" = None):
        self.meal_id = meal_id
        self.name = name
        self.price = price
        self.prepared = prepared
        self.served = served
        self.has1 = has1
        
        pass
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
    def prepared(self):
        return self.__prepared
    @prepared.setter
    def prepared(self, prepared: bool):
        self.__prepared = prepared

    @property
    def served(self):
        return self.__served
    @served.setter
    def served(self, served: bool):
        self.__served = served

    @property
    def meal_id(self):
        return self.__meal_id
    @meal_id.setter
    def meal_id(self, meal_id: str):
        self.__meal_id = meal_id

    @property
    def has1(self):
        return self.__has1
    @has1.setter
    def has1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_meal__has1", None)
        self.__has1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orde0"):
                opp_val = getattr(old_value, "orde0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orde0"):
                opp_val = getattr(value, "orde0", None)
                if opp_val is None:
                    setattr(value, "orde0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order:

    def __init__(self, order_id: str, foodList: str, app7: "app" = None, customer15: "customer" = None, orde0: set["meal"] = None):
        self.order_id = order_id
        self.foodList = foodList
        self.app7 = app7
        self.customer15 = customer15
        self.orde0 = orde0 if orde0 is not None else set()
        
        pass
    @property
    def foodList(self):
        return self.__foodList
    @foodList.setter
    def foodList(self, foodList: str):
        self.__foodList = foodList

    @property
    def order_id(self):
        return self.__order_id
    @order_id.setter
    def order_id(self, order_id: str):
        self.__order_id = order_id

    @property
    def orde0(self):
        return self.__orde0
    @orde0.setter
    def orde0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orde0", None)
        self.__orde0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has1"):
                    opp_val = getattr(item, "has1", None)
                    
                    if opp_val == self:
                        setattr(item, "has1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has1"):
                    opp_val = getattr(item, "has1", None)
                    
                    setattr(item, "has1", self)
                    

    @property
    def customer15(self):
        return self.__customer15
    @customer15.setter
    def customer15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer15", None)
        self.__customer15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order14"):
                opp_val = getattr(old_value, "order14", None)
                if opp_val == self:
                    setattr(old_value, "order14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order14"):
                opp_val = getattr(value, "order14", None)
                setattr(value, "order14", self)

    @property
    def app7(self):
        return self.__app7
    @app7.setter
    def app7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__app7", None)
        self.__app7 = value
        
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



class Table:

    def __init__(self, numSeats: int, table_id: str, avaliable: bool, app4: "app" = None, waiter3: "Waiter" = None):
        self.numSeats = numSeats
        self.table_id = table_id
        self.avaliable = avaliable
        self.app4 = app4
        self.waiter3 = waiter3
        
        pass
    @property
    def numSeats(self):
        return self.__numSeats
    @numSeats.setter
    def numSeats(self, numSeats: int):
        self.__numSeats = numSeats

    @property
    def avaliable(self):
        return self.__avaliable
    @avaliable.setter
    def avaliable(self, avaliable: bool):
        self.__avaliable = avaliable

    @property
    def table_id(self):
        return self.__table_id
    @table_id.setter
    def table_id(self, table_id: str):
        self.__table_id = table_id

    @property
    def app4(self):
        return self.__app4
    @app4.setter
    def app4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__app4", None)
        self.__app4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table5"):
                opp_val = getattr(old_value, "table5", None)
                if opp_val == self:
                    setattr(old_value, "table5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table5"):
                opp_val = getattr(value, "table5", None)
                setattr(value, "table5", self)

    @property
    def waiter3(self):
        return self.__waiter3
    @waiter3.setter
    def waiter3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__waiter3", None)
        self.__waiter3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table2"):
                opp_val = getattr(old_value, "table2", None)
                if opp_val == self:
                    setattr(old_value, "table2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table2"):
                opp_val = getattr(value, "table2", None)
                setattr(value, "table2", self)

