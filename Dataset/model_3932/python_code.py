from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class office_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class OfficeElement:

    pass
class office_Office(OfficeElement):

    pass
class office_Employee(OfficeElement):

    def __init__(self, title: str, employees: "office_Office" = None, office_Employee: "office_Employee" = None, office_Employee2: set["office_Employee"] = None, Employee: "office_Office" = None):
        self.title = title
        self.employees = employees
        self.office_Employee = office_Employee
        self.office_Employee2 = office_Employee2 if office_Employee2 is not None else set()
        self.Employee = Employee
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_office_Employee__employees", None)
        self.__employees = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Office"):
                opp_val = getattr(old_value, "Office", None)
                if opp_val == self:
                    setattr(old_value, "Office", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Office"):
                opp_val = getattr(value, "Office", None)
                setattr(value, "Office", self)

    @property
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_office_Employee__Employee", None)
        self.__Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "worksIn"):
                opp_val = getattr(old_value, "worksIn", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "worksIn"):
                opp_val = getattr(value, "worksIn", None)
                if opp_val is None:
                    setattr(value, "worksIn", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def office_Employee2(self):
        return self.__office_Employee2

    @office_Employee2.setter
    def office_Employee2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_office_Employee__office_Employee2", None)
        self.__office_Employee2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "office_Employee"):
                    opp_val = getattr(item, "office_Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "office_Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "office_Employee"):
                    opp_val = getattr(item, "office_Employee", None)
                    
                    setattr(item, "office_Employee", self)
                    

    @property
    def office_Employee(self):
        return self.__office_Employee

    @office_Employee.setter
    def office_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_office_Employee__office_Employee", None)
        self.__office_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "office_Employee2"):
                opp_val = getattr(old_value, "office_Employee2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "office_Employee2"):
                opp_val = getattr(value, "office_Employee2", None)
                if opp_val is None:
                    setattr(value, "office_Employee2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class office_OfficeElement(NamedElement):

    pass
class office_OfficeModel(NamedElement):

    pass