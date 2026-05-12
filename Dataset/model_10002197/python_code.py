from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Admin_:

    def __init__(self, Password: str, ArrayList_member_: str, ArrayList_worker_: str, member6: "member" = None, workers8: "Workers" = None):
        self.Password = Password
        self.ArrayList_member_ = ArrayList_member_
        self.ArrayList_worker_ = ArrayList_worker_
        self.member6 = member6
        self.workers8 = workers8
        
        pass
    @property
    def ArrayList_member_(self):
        return self.__ArrayList_member_
    @ArrayList_member_.setter
    def ArrayList_member_(self, ArrayList_member_: str):
        self.__ArrayList_member_ = ArrayList_member_

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def ArrayList_worker_(self):
        return self.__ArrayList_worker_
    @ArrayList_worker_.setter
    def ArrayList_worker_(self, ArrayList_worker_: str):
        self.__ArrayList_worker_ = ArrayList_worker_

    @property
    def member6(self):
        return self.__member6
    @member6.setter
    def member6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin___member6", None)
        self.__member6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin_7"):
                opp_val = getattr(old_value, "admin_7", None)
                if opp_val == self:
                    setattr(old_value, "admin_7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin_7"):
                opp_val = getattr(value, "admin_7", None)
                setattr(value, "admin_7", self)

    @property
    def workers8(self):
        return self.__workers8
    @workers8.setter
    def workers8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin___workers8", None)
        self.__workers8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin_9"):
                opp_val = getattr(old_value, "admin_9", None)
                if opp_val == self:
                    setattr(old_value, "admin_9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin_9"):
                opp_val = getattr(value, "admin_9", None)
                setattr(value, "admin_9", self)



class member:

    def __init__(self, name: str, password: str, memberType: str, admin_7: "Admin_" = None):
        self.name = name
        self.password = password
        self.memberType = memberType
        self.admin_7 = admin_7
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def memberType(self):
        return self.__memberType
    @memberType.setter
    def memberType(self, memberType: str):
        self.__memberType = memberType

    @property
    def admin_7(self):
        return self.__admin_7
    @admin_7.setter
    def admin_7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_member__admin_7", None)
        self.__admin_7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "member6"):
                opp_val = getattr(old_value, "member6", None)
                if opp_val == self:
                    setattr(old_value, "member6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "member6"):
                opp_val = getattr(value, "member6", None)
                setattr(value, "member6", self)



class Workers:

    def __init__(self, name: str, Designation: str, Password: str, salary: int, admin_9: "Admin_" = None):
        self.name = name
        self.Designation = Designation
        self.Password = Password
        self.salary = salary
        self.admin_9 = admin_9
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

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
    def Designation(self):
        return self.__Designation
    @Designation.setter
    def Designation(self, Designation: str):
        self.__Designation = Designation

    @property
    def admin_9(self):
        return self.__admin_9
    @admin_9.setter
    def admin_9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Workers__admin_9", None)
        self.__admin_9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workers8"):
                opp_val = getattr(old_value, "workers8", None)
                if opp_val == self:
                    setattr(old_value, "workers8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workers8"):
                opp_val = getattr(value, "workers8", None)
                setattr(value, "workers8", self)



class customers:

    def __init__(self, name: str, shoppingCost: int):
        self.name = name
        self.shoppingCost = shoppingCost
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def shoppingCost(self):
        return self.__shoppingCost
    @shoppingCost.setter
    def shoppingCost(self, shoppingCost: int):
        self.__shoppingCost = shoppingCost



class Accessories:

    def __init__(self, name: str, price: int, items5: "Items" = None):
        self.name = name
        self.price = price
        self.items5 = items5
        
        pass
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
    def items5(self):
        return self.__items5
    @items5.setter
    def items5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Accessories__items5", None)
        self.__items5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "food4"):
                opp_val = getattr(old_value, "food4", None)
                if opp_val == self:
                    setattr(old_value, "food4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "food4"):
                opp_val = getattr(value, "food4", None)
                setattr(value, "food4", self)



class Devices:

    def __init__(self, name: str, price: int, items1: "Items" = None):
        self.name = name
        self.price = price
        self.items1 = items1
        
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
    def price(self, price: int):
        self.__price = price

    @property
    def items1(self):
        return self.__items1
    @items1.setter
    def items1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Devices__items1", None)
        self.__items1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appliacne0"):
                opp_val = getattr(old_value, "appliacne0", None)
                if opp_val == self:
                    setattr(old_value, "appliacne0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appliacne0"):
                opp_val = getattr(value, "appliacne0", None)
                setattr(value, "appliacne0", self)



class ComputerParts:

    def __init__(self, name: str, price: int, items3: "Items" = None):
        self.name = name
        self.price = price
        self.items3 = items3
        
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
    def price(self, price: int):
        self.__price = price

    @property
    def items3(self):
        return self.__items3
    @items3.setter
    def items3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ComputerParts__items3", None)
        self.__items3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "furniture2"):
                opp_val = getattr(old_value, "furniture2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "furniture2"):
                opp_val = getattr(value, "furniture2", None)
                if opp_val is None:
                    setattr(value, "furniture2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Items:

    def __init__(self, ArrayList_ComputerParts_: str, ArrayList_devices_: str, typeOfItems: int, ArrayList_accessories_: str, appliacne0: "Devices" = None, furniture2: set["ComputerParts"] = None, food4: "Accessories" = None):
        self.ArrayList_ComputerParts_ = ArrayList_ComputerParts_
        self.ArrayList_devices_ = ArrayList_devices_
        self.typeOfItems = typeOfItems
        self.ArrayList_accessories_ = ArrayList_accessories_
        self.appliacne0 = appliacne0
        self.furniture2 = furniture2 if furniture2 is not None else set()
        self.food4 = food4
        
        pass
    @property
    def ArrayList_accessories_(self):
        return self.__ArrayList_accessories_
    @ArrayList_accessories_.setter
    def ArrayList_accessories_(self, ArrayList_accessories_: str):
        self.__ArrayList_accessories_ = ArrayList_accessories_

    @property
    def ArrayList_devices_(self):
        return self.__ArrayList_devices_
    @ArrayList_devices_.setter
    def ArrayList_devices_(self, ArrayList_devices_: str):
        self.__ArrayList_devices_ = ArrayList_devices_

    @property
    def typeOfItems(self):
        return self.__typeOfItems
    @typeOfItems.setter
    def typeOfItems(self, typeOfItems: int):
        self.__typeOfItems = typeOfItems

    @property
    def ArrayList_ComputerParts_(self):
        return self.__ArrayList_ComputerParts_
    @ArrayList_ComputerParts_.setter
    def ArrayList_ComputerParts_(self, ArrayList_ComputerParts_: str):
        self.__ArrayList_ComputerParts_ = ArrayList_ComputerParts_

    @property
    def appliacne0(self):
        return self.__appliacne0
    @appliacne0.setter
    def appliacne0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Items__appliacne0", None)
        self.__appliacne0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items1"):
                opp_val = getattr(old_value, "items1", None)
                if opp_val == self:
                    setattr(old_value, "items1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items1"):
                opp_val = getattr(value, "items1", None)
                setattr(value, "items1", self)

    @property
    def food4(self):
        return self.__food4
    @food4.setter
    def food4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Items__food4", None)
        self.__food4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items5"):
                opp_val = getattr(old_value, "items5", None)
                if opp_val == self:
                    setattr(old_value, "items5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items5"):
                opp_val = getattr(value, "items5", None)
                setattr(value, "items5", self)

    @property
    def furniture2(self):
        return self.__furniture2
    @furniture2.setter
    def furniture2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Items__furniture2", None)
        self.__furniture2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "items3"):
                    opp_val = getattr(item, "items3", None)
                    
                    if opp_val == self:
                        setattr(item, "items3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "items3"):
                    opp_val = getattr(item, "items3", None)
                    
                    setattr(item, "items3", self)
                    

