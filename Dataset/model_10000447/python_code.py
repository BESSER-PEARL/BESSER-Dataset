from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Food:

    def __init__(self, food_id: str, name: str, price: float, prepared: bool, served: bool, items10: "Items" = None, app13: "app" = None):
        self.food_id = food_id
        self.name = name
        self.price = price
        self.prepared = prepared
        self.served = served
        self.items10 = items10
        self.app13 = app13
        
        pass
    @property
    def prepared(self):
        return self.__prepared
    @prepared.setter
    def prepared(self, prepared: bool):
        self.__prepared = prepared

    @property
    def food_id(self):
        return self.__food_id
    @food_id.setter
    def food_id(self, food_id: str):
        self.__food_id = food_id

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def served(self):
        return self.__served
    @served.setter
    def served(self, served: bool):
        self.__served = served

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def items10(self):
        return self.__items10
    @items10.setter
    def items10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Food__items10", None)
        self.__items10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "food11"):
                opp_val = getattr(old_value, "food11", None)
                if opp_val == self:
                    setattr(old_value, "food11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "food11"):
                opp_val = getattr(value, "food11", None)
                setattr(value, "food11", self)

    @property
    def app13(self):
        return self.__app13
    @app13.setter
    def app13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Food__app13", None)
        self.__app13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "food12"):
                opp_val = getattr(old_value, "food12", None)
                if opp_val == self:
                    setattr(old_value, "food12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "food12"):
                opp_val = getattr(value, "food12", None)
                setattr(value, "food12", self)



class app:

    pass


class cost:

    pass


class Chef:

    pass


class Items:

    pass


class Table:

    def __init__(self, tableNumber: int, seats: int, customer2: "Customer" = None, app6: "app" = None):
        self.tableNumber = tableNumber
        self.seats = seats
        self.customer2 = customer2
        self.app6 = app6
        
        pass
    @property
    def tableNumber(self):
        return self.__tableNumber
    @tableNumber.setter
    def tableNumber(self, tableNumber: int):
        self.__tableNumber = tableNumber

    @property
    def seats(self):
        return self.__seats
    @seats.setter
    def seats(self, seats: int):
        self.__seats = seats

    @property
    def app6(self):
        return self.__app6
    @app6.setter
    def app6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__app6", None)
        self.__app6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table7"):
                opp_val = getattr(old_value, "table7", None)
                if opp_val == self:
                    setattr(old_value, "table7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table7"):
                opp_val = getattr(value, "table7", None)
                setattr(value, "table7", self)

    @property
    def customer2(self):
        return self.__customer2
    @customer2.setter
    def customer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__customer2", None)
        self.__customer2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table3"):
                opp_val = getattr(old_value, "table3", None)
                if opp_val == self:
                    setattr(old_value, "table3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table3"):
                opp_val = getattr(value, "table3", None)
                setattr(value, "table3", self)



class Host:

    def __init__(self, ID: str, shift: str, customer0: "Customer" = None):
        self.ID = ID
        self.shift = shift
        self.customer0 = customer0
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def shift(self):
        return self.__shift
    @shift.setter
    def shift(self, shift: str):
        self.__shift = shift

    @property
    def customer0(self):
        return self.__customer0
    @customer0.setter
    def customer0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Host__customer0", None)
        self.__customer0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "host1"):
                opp_val = getattr(old_value, "host1", None)
                if opp_val == self:
                    setattr(old_value, "host1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "host1"):
                opp_val = getattr(value, "host1", None)
                setattr(value, "host1", self)



class robotWaiter:

    pass


class Customer:

    def __init__(self, name: str, numberPeople: int, host1: "Host" = None, table3: "Table" = None, robotWaiter5: "robotWaiter" = None):
        self.name = name
        self.numberPeople = numberPeople
        self.host1 = host1
        self.table3 = table3
        self.robotWaiter5 = robotWaiter5
        
        pass
    @property
    def numberPeople(self):
        return self.__numberPeople
    @numberPeople.setter
    def numberPeople(self, numberPeople: int):
        self.__numberPeople = numberPeople

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def host1(self):
        return self.__host1
    @host1.setter
    def host1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__host1", None)
        self.__host1 = value
        
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

    @property
    def table3(self):
        return self.__table3
    @table3.setter
    def table3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__table3", None)
        self.__table3 = value
        
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

    @property
    def robotWaiter5(self):
        return self.__robotWaiter5
    @robotWaiter5.setter
    def robotWaiter5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__robotWaiter5", None)
        self.__robotWaiter5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer4"):
                opp_val = getattr(old_value, "customer4", None)
                if opp_val == self:
                    setattr(old_value, "customer4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer4"):
                opp_val = getattr(value, "customer4", None)
                setattr(value, "customer4", self)

