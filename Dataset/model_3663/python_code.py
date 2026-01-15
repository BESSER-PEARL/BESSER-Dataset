from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Employee:

    pass
class iOI_Manager(Employee):

    pass
class iOI_Department:

    def __init__(self, name: str, iOI_Department14: "iOI_Department" = None, iOI_Department12: "iOI_Department" = None, iOI_Department: "iOI_Company" = None, iOI_Department8: "iOI_Manager" = None, iOI_Department10: set["iOI_Employee"] = None):
        self.name = name
        self.iOI_Department14 = iOI_Department14
        self.iOI_Department12 = iOI_Department12
        self.iOI_Department = iOI_Department
        self.iOI_Department8 = iOI_Department8
        self.iOI_Department10 = iOI_Department10 if iOI_Department10 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iOI_Department8(self):
        return self.__iOI_Department8

    @iOI_Department8.setter
    def iOI_Department8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOI_Department__iOI_Department8", None)
        self.__iOI_Department8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOI_Manager"):
                opp_val = getattr(old_value, "iOI_Manager", None)
                if opp_val == self:
                    setattr(old_value, "iOI_Manager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOI_Manager"):
                opp_val = getattr(value, "iOI_Manager", None)
                setattr(value, "iOI_Manager", self)

    @property
    def iOI_Department12(self):
        return self.__iOI_Department12

    @iOI_Department12.setter
    def iOI_Department12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOI_Department__iOI_Department12", None)
        self.__iOI_Department12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOI_Department14"):
                opp_val = getattr(old_value, "iOI_Department14", None)
                if opp_val == self:
                    setattr(old_value, "iOI_Department14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOI_Department14"):
                opp_val = getattr(value, "iOI_Department14", None)
                setattr(value, "iOI_Department14", self)

    @property
    def iOI_Department(self):
        return self.__iOI_Department

    @iOI_Department.setter
    def iOI_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOI_Department__iOI_Department", None)
        self.__iOI_Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOI_Company6"):
                opp_val = getattr(old_value, "iOI_Company6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOI_Company6"):
                opp_val = getattr(value, "iOI_Company6", None)
                if opp_val is None:
                    setattr(value, "iOI_Company6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iOI_Department14(self):
        return self.__iOI_Department14

    @iOI_Department14.setter
    def iOI_Department14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOI_Department__iOI_Department14", None)
        self.__iOI_Department14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOI_Department12"):
                opp_val = getattr(old_value, "iOI_Department12", None)
                if opp_val == self:
                    setattr(old_value, "iOI_Department12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOI_Department12"):
                opp_val = getattr(value, "iOI_Department12", None)
                setattr(value, "iOI_Department12", self)

    @property
    def iOI_Department10(self):
        return self.__iOI_Department10

    @iOI_Department10.setter
    def iOI_Department10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOI_Department__iOI_Department10", None)
        self.__iOI_Department10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iOI_Employee11"):
                    opp_val = getattr(item, "iOI_Employee11", None)
                    
                    if opp_val == self:
                        setattr(item, "iOI_Employee11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iOI_Employee11"):
                    opp_val = getattr(item, "iOI_Employee11", None)
                    
                    setattr(item, "iOI_Employee11", self)
                    

class iOI_Company:

    def __init__(self, name: str, iOI_Company: "iOI_Model" = None, iOI_Company3: set["iOI_Position"] = None, iOI_Company6: set["iOI_Department"] = None):
        self.name = name
        self.iOI_Company = iOI_Company
        self.iOI_Company3 = iOI_Company3 if iOI_Company3 is not None else set()
        self.iOI_Company6 = iOI_Company6 if iOI_Company6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iOI_Company(self):
        return self.__iOI_Company

    @iOI_Company.setter
    def iOI_Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOI_Company__iOI_Company", None)
        self.__iOI_Company = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOI_Model"):
                opp_val = getattr(old_value, "iOI_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOI_Model"):
                opp_val = getattr(value, "iOI_Model", None)
                if opp_val is None:
                    setattr(value, "iOI_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iOI_Company6(self):
        return self.__iOI_Company6

    @iOI_Company6.setter
    def iOI_Company6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOI_Company__iOI_Company6", None)
        self.__iOI_Company6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iOI_Department"):
                    opp_val = getattr(item, "iOI_Department", None)
                    
                    if opp_val == self:
                        setattr(item, "iOI_Department", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iOI_Department"):
                    opp_val = getattr(item, "iOI_Department", None)
                    
                    setattr(item, "iOI_Department", self)
                    

    @property
    def iOI_Company3(self):
        return self.__iOI_Company3

    @iOI_Company3.setter
    def iOI_Company3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOI_Company__iOI_Company3", None)
        self.__iOI_Company3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iOI_Position4"):
                    opp_val = getattr(item, "iOI_Position4", None)
                    
                    if opp_val == self:
                        setattr(item, "iOI_Position4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iOI_Position4"):
                    opp_val = getattr(item, "iOI_Position4", None)
                    
                    setattr(item, "iOI_Position4", self)
                    

class iOI_Model:

    def __init__(self, name: str, iOI_Model: set["iOI_Company"] = None):
        self.name = name
        self.iOI_Model = iOI_Model if iOI_Model is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iOI_Model(self):
        return self.__iOI_Model

    @iOI_Model.setter
    def iOI_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOI_Model__iOI_Model", None)
        self.__iOI_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iOI_Company"):
                    opp_val = getattr(item, "iOI_Company", None)
                    
                    if opp_val == self:
                        setattr(item, "iOI_Company", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iOI_Company"):
                    opp_val = getattr(item, "iOI_Company", None)
                    
                    setattr(item, "iOI_Company", self)
                    

class iOI_Position:

    def __init__(self, name: str, iOI_Position: "iOI_Employee" = None, iOI_Position4: "iOI_Company" = None):
        self.name = name
        self.iOI_Position = iOI_Position
        self.iOI_Position4 = iOI_Position4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iOI_Position4(self):
        return self.__iOI_Position4

    @iOI_Position4.setter
    def iOI_Position4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOI_Position__iOI_Position4", None)
        self.__iOI_Position4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOI_Company3"):
                opp_val = getattr(old_value, "iOI_Company3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOI_Company3"):
                opp_val = getattr(value, "iOI_Company3", None)
                if opp_val is None:
                    setattr(value, "iOI_Company3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iOI_Position(self):
        return self.__iOI_Position

    @iOI_Position.setter
    def iOI_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOI_Position__iOI_Position", None)
        self.__iOI_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOI_Employee"):
                opp_val = getattr(old_value, "iOI_Employee", None)
                if opp_val == self:
                    setattr(old_value, "iOI_Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOI_Employee"):
                opp_val = getattr(value, "iOI_Employee", None)
                setattr(value, "iOI_Employee", self)

class iOI_Employee:

    def __init__(self, name: str, salary: int, iOI_Employee: "iOI_Position" = None, iOI_Employee11: "iOI_Department" = None):
        self.name = name
        self.salary = salary
        self.iOI_Employee = iOI_Employee
        self.iOI_Employee11 = iOI_Employee11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self, salary: int):
        self.__salary = salary

    @property
    def iOI_Employee(self):
        return self.__iOI_Employee

    @iOI_Employee.setter
    def iOI_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOI_Employee__iOI_Employee", None)
        self.__iOI_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOI_Position"):
                opp_val = getattr(old_value, "iOI_Position", None)
                if opp_val == self:
                    setattr(old_value, "iOI_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOI_Position"):
                opp_val = getattr(value, "iOI_Position", None)
                setattr(value, "iOI_Position", self)

    @property
    def iOI_Employee11(self):
        return self.__iOI_Employee11

    @iOI_Employee11.setter
    def iOI_Employee11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOI_Employee__iOI_Employee11", None)
        self.__iOI_Employee11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOI_Department10"):
                opp_val = getattr(old_value, "iOI_Department10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOI_Department10"):
                opp_val = getattr(value, "iOI_Department10", None)
                if opp_val is None:
                    setattr(value, "iOI_Department10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
