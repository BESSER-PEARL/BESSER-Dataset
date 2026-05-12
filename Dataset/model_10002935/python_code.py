from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Store:

    def __init__(self, Sid: int, SName: str, member11: "member" = None, employee12: "Employee" = None, product14: "Product" = None):
        self.Sid = Sid
        self.SName = SName
        self.member11 = member11
        self.employee12 = employee12
        self.product14 = product14
        
        pass
    @property
    def Sid(self):
        return self.__Sid
    @Sid.setter
    def Sid(self, Sid: int):
        self.__Sid = Sid

    @property
    def SName(self):
        return self.__SName
    @SName.setter
    def SName(self, SName: str):
        self.__SName = SName

    @property
    def product14(self):
        return self.__product14
    @product14.setter
    def product14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Store__product14", None)
        self.__product14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "store15"):
                opp_val = getattr(old_value, "store15", None)
                if opp_val == self:
                    setattr(old_value, "store15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "store15"):
                opp_val = getattr(value, "store15", None)
                setattr(value, "store15", self)

    @property
    def member11(self):
        return self.__member11
    @member11.setter
    def member11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Store__member11", None)
        self.__member11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "store10"):
                opp_val = getattr(old_value, "store10", None)
                if opp_val == self:
                    setattr(old_value, "store10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "store10"):
                opp_val = getattr(value, "store10", None)
                setattr(value, "store10", self)

    @property
    def employee12(self):
        return self.__employee12
    @employee12.setter
    def employee12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Store__employee12", None)
        self.__employee12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "store13"):
                opp_val = getattr(old_value, "store13", None)
                if opp_val == self:
                    setattr(old_value, "store13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "store13"):
                opp_val = getattr(value, "store13", None)
                setattr(value, "store13", self)



class Admin_:

    def __init__(self, Password: str, ArrayList_member_: str, ArryList_Employee: str, member6: "member" = None, workers8: "Employee" = None):
        self.Password = Password
        self.ArrayList_member_ = ArrayList_member_
        self.ArryList_Employee = ArryList_Employee
        self.member6 = member6
        self.workers8 = workers8
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def ArrayList_member_(self):
        return self.__ArrayList_member_
    @ArrayList_member_.setter
    def ArrayList_member_(self, ArrayList_member_: str):
        self.__ArrayList_member_ = ArrayList_member_

    @property
    def ArryList_Employee(self):
        return self.__ArryList_Employee
    @ArryList_Employee.setter
    def ArryList_Employee(self, ArryList_Employee: str):
        self.__ArryList_Employee = ArryList_Employee

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



class member:

    def __init__(self, name: str, password: str, memberType: str, admin_7: "Admin_" = None, store10: "Store" = None):
        self.name = name
        self.password = password
        self.memberType = memberType
        self.admin_7 = admin_7
        self.store10 = store10
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def memberType(self):
        return self.__memberType
    @memberType.setter
    def memberType(self, memberType: str):
        self.__memberType = memberType

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def store10(self):
        return self.__store10
    @store10.setter
    def store10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_member__store10", None)
        self.__store10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "member11"):
                opp_val = getattr(old_value, "member11", None)
                if opp_val == self:
                    setattr(old_value, "member11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "member11"):
                opp_val = getattr(value, "member11", None)
                setattr(value, "member11", self)

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



class Employee:

    def __init__(self, Password: str, salary: int, name: str, Designation: str, admin_9: "Admin_" = None, store13: "Store" = None):
        self.Password = Password
        self.salary = salary
        self.name = name
        self.Designation = Designation
        self.admin_9 = admin_9
        self.store13 = store13
        
        pass
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
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary: int):
        self.__salary = salary

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def admin_9(self):
        return self.__admin_9
    @admin_9.setter
    def admin_9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__admin_9", None)
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

    @property
    def store13(self):
        return self.__store13
    @store13.setter
    def store13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__store13", None)
        self.__store13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee12"):
                opp_val = getattr(old_value, "employee12", None)
                if opp_val == self:
                    setattr(old_value, "employee12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee12"):
                opp_val = getattr(value, "employee12", None)
                setattr(value, "employee12", self)



class customers:

    def __init__(self, name: str, shoppingCost: int):
        self.name = name
        self.shoppingCost = shoppingCost
        
        pass
    @property
    def shoppingCost(self):
        return self.__shoppingCost
    @shoppingCost.setter
    def shoppingCost(self, shoppingCost: int):
        self.__shoppingCost = shoppingCost

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class food:

    def __init__(self, name: str, price: int, items5: "Product" = None):
        self.name = name
        self.price = price
        self.items5 = items5
        
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
    def items5(self):
        return self.__items5
    @items5.setter
    def items5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_food__items5", None)
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



class Appliacne:

    def __init__(self, name: str, price: int, items1: "Product" = None):
        self.name = name
        self.price = price
        self.items1 = items1
        
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
    def items1(self):
        return self.__items1
    @items1.setter
    def items1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appliacne__items1", None)
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



class Furniture:

    def __init__(self, name: str, price: int, items3: "Product" = None):
        self.name = name
        self.price = price
        self.items3 = items3
        
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
    def items3(self):
        return self.__items3
    @items3.setter
    def items3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Furniture__items3", None)
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



class Product:

    def __init__(self, ArrayList_food_: str, typeOfItems: int, ArrayList_furniture_: str, ArrayList_appliance_: str, appliacne0: "Appliacne" = None, furniture2: set["Furniture"] = None, food4: "food" = None, store15: "Store" = None):
        self.ArrayList_food_ = ArrayList_food_
        self.typeOfItems = typeOfItems
        self.ArrayList_furniture_ = ArrayList_furniture_
        self.ArrayList_appliance_ = ArrayList_appliance_
        self.appliacne0 = appliacne0
        self.furniture2 = furniture2 if furniture2 is not None else set()
        self.food4 = food4
        self.store15 = store15
        
        pass
    @property
    def ArrayList_appliance_(self):
        return self.__ArrayList_appliance_
    @ArrayList_appliance_.setter
    def ArrayList_appliance_(self, ArrayList_appliance_: str):
        self.__ArrayList_appliance_ = ArrayList_appliance_

    @property
    def ArrayList_furniture_(self):
        return self.__ArrayList_furniture_
    @ArrayList_furniture_.setter
    def ArrayList_furniture_(self, ArrayList_furniture_: str):
        self.__ArrayList_furniture_ = ArrayList_furniture_

    @property
    def ArrayList_food_(self):
        return self.__ArrayList_food_
    @ArrayList_food_.setter
    def ArrayList_food_(self, ArrayList_food_: str):
        self.__ArrayList_food_ = ArrayList_food_

    @property
    def typeOfItems(self):
        return self.__typeOfItems
    @typeOfItems.setter
    def typeOfItems(self, typeOfItems: int):
        self.__typeOfItems = typeOfItems

    @property
    def appliacne0(self):
        return self.__appliacne0
    @appliacne0.setter
    def appliacne0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__appliacne0", None)
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
    def furniture2(self):
        return self.__furniture2
    @furniture2.setter
    def furniture2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__furniture2", None)
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
                    

    @property
    def food4(self):
        return self.__food4
    @food4.setter
    def food4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__food4", None)
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
    def store15(self):
        return self.__store15
    @store15.setter
    def store15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__store15", None)
        self.__store15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product14"):
                opp_val = getattr(old_value, "product14", None)
                if opp_val == self:
                    setattr(old_value, "product14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product14"):
                opp_val = getattr(value, "product14", None)
                setattr(value, "product14", self)

