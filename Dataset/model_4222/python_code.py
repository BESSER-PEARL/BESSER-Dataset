from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class organization_core_Cass:

    pass
class organization_ABase(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class ABase:

    pass
class organization_Department(ABase):

    def __init__(self, number: int, organization_Department: "organization_Company" = None, organization_Department2: set["organization_Employee"] = None):
        self.number = number
        self.organization_Department = organization_Department
        self.organization_Department2 = organization_Department2 if organization_Department2 is not None else set()
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def organization_Department(self):
        return self.__organization_Department

    @organization_Department.setter
    def organization_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organization_Department__organization_Department", None)
        self.__organization_Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "organization_Company"):
                opp_val = getattr(old_value, "organization_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "organization_Company"):
                opp_val = getattr(value, "organization_Company", None)
                if opp_val is None:
                    setattr(value, "organization_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def organization_Department2(self):
        return self.__organization_Department2

    @organization_Department2.setter
    def organization_Department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organization_Department__organization_Department2", None)
        self.__organization_Department2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "organization_Employee"):
                    opp_val = getattr(item, "organization_Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "organization_Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "organization_Employee"):
                    opp_val = getattr(item, "organization_Employee", None)
                    
                    setattr(item, "organization_Employee", self)
                    

class organization_Company(ABase):

    def __init__(self, name: str, organization_Company: set["organization_Department"] = None):
        self.name = name
        self.organization_Company = organization_Company if organization_Company is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def organization_Company(self):
        return self.__organization_Company

    @organization_Company.setter
    def organization_Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organization_Company__organization_Company", None)
        self.__organization_Company = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "organization_Department"):
                    opp_val = getattr(item, "organization_Department", None)
                    
                    if opp_val == self:
                        setattr(item, "organization_Department", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "organization_Department"):
                    opp_val = getattr(item, "organization_Department", None)
                    
                    setattr(item, "organization_Department", self)
                    

class organization_Employee(ABase):

    def __init__(self, name: str, organization_Employee: "organization_Department" = None):
        self.name = name
        self.organization_Employee = organization_Employee
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def organization_Employee(self):
        return self.__organization_Employee

    @organization_Employee.setter
    def organization_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organization_Employee__organization_Employee", None)
        self.__organization_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "organization_Department2"):
                opp_val = getattr(old_value, "organization_Department2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "organization_Department2"):
                opp_val = getattr(value, "organization_Department2", None)
                if opp_val is None:
                    setattr(value, "organization_Department2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
