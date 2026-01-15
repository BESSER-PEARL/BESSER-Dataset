from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Company_Project:

    def __init__(self, name: str, budget: int, 4: "Company_Employee" = None, 10: "Company_Department" = None, 12: set["Company_Employee"] = None, 15: "Company_Department" = None):
        self.name = name
        self.budget = budget
        self.4 = 4
        self.10 = 10
        self.12 = 12 if 12 is not None else set()
        self.15 = 15
        
    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, budget: int):
        self.__budget = budget

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 12(self):
        return self.__12

    @12.setter
    def 12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Project__12", None)
        self.__12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "13"):
                    opp_val = getattr(item, "13", None)
                    
                    if opp_val == self:
                        setattr(item, "13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "13"):
                    opp_val = getattr(item, "13", None)
                    
                    setattr(item, "13", self)
                    

    @property
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Project__10", None)
        self.__10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "9"):
                opp_val = getattr(old_value, "9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "9"):
                opp_val = getattr(value, "9", None)
                if opp_val is None:
                    setattr(value, "9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 15(self):
        return self.__15

    @15.setter
    def 15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Project__15", None)
        self.__15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "16"):
                opp_val = getattr(old_value, "16", None)
                if opp_val == self:
                    setattr(old_value, "16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "16"):
                opp_val = getattr(value, "16", None)
                setattr(value, "16", self)

    @property
    def 4(self):
        return self.__4

    @4.setter
    def 4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Project__4", None)
        self.__4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "3"):
                opp_val = getattr(old_value, "3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "3"):
                opp_val = getattr(value, "3", None)
                if opp_val is None:
                    setattr(value, "3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Company_Department:

    def __init__(self, name: str, location: str, budget: int, 1: "Company_Employee" = None, 6: set["Company_Employee"] = None, 9: set["Company_Project"] = None, 16: "Company_Project" = None):
        self.name = name
        self.location = location
        self.budget = budget
        self.1 = 1
        self.6 = 6 if 6 is not None else set()
        self.9 = 9 if 9 is not None else set()
        self.16 = 16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, budget: int):
        self.__budget = budget

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def 16(self):
        return self.__16

    @16.setter
    def 16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Department__16", None)
        self.__16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "15"):
                opp_val = getattr(old_value, "15", None)
                if opp_val == self:
                    setattr(old_value, "15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "15"):
                opp_val = getattr(value, "15", None)
                setattr(value, "15", self)

    @property
    def 9(self):
        return self.__9

    @9.setter
    def 9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Department__9", None)
        self.__9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "10"):
                    opp_val = getattr(item, "10", None)
                    
                    if opp_val == self:
                        setattr(item, "10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "10"):
                    opp_val = getattr(item, "10", None)
                    
                    setattr(item, "10", self)
                    

    @property
    def 6(self):
        return self.__6

    @6.setter
    def 6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Department__6", None)
        self.__6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "7"):
                    opp_val = getattr(item, "7", None)
                    
                    if opp_val == self:
                        setattr(item, "7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "7"):
                    opp_val = getattr(item, "7", None)
                    
                    setattr(item, "7", self)
                    

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Department__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Company_Employee:

    def __init__(self, name: str, salary: int, : set["Company_Department"] = None, 3: set["Company_Project"] = None, 7: "Company_Department" = None, 13: "Company_Project" = None):
        self.name = name
        self.salary = salary
        self. =  if  is not None else set()
        self.3 = 3 if 3 is not None else set()
        self.7 = 7
        self.13 = 13
        
    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self, salary: int):
        self.__salary = salary

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Employee__13", None)
        self.__13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "12"):
                opp_val = getattr(old_value, "12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "12"):
                opp_val = getattr(value, "12", None)
                if opp_val is None:
                    setattr(value, "12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Employee__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    if opp_val == self:
                        setattr(item, "1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    setattr(item, "1", self)
                    

    @property
    def 7(self):
        return self.__7

    @7.setter
    def 7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Employee__7", None)
        self.__7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "6"):
                opp_val = getattr(old_value, "6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "6"):
                opp_val = getattr(value, "6", None)
                if opp_val is None:
                    setattr(value, "6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 3(self):
        return self.__3

    @3.setter
    def 3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Employee__3", None)
        self.__3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "4"):
                    opp_val = getattr(item, "4", None)
                    
                    if opp_val == self:
                        setattr(item, "4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "4"):
                    opp_val = getattr(item, "4", None)
                    
                    setattr(item, "4", self)
                    
