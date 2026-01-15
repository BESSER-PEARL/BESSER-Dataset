from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Subunit:

    pass
class company_Employee(Subunit):

    def __init__(self, salary: float, company_Employee6: "company_Person" = None, company_Employee: "company_Dept" = None):
        self.salary = salary
        self.company_Employee6 = company_Employee6
        self.company_Employee = company_Employee
        
    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary

    @property
    def company_Employee(self):
        return self.__company_Employee

    @company_Employee.setter
    def company_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee", None)
        self.__company_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Dept2"):
                opp_val = getattr(old_value, "company_Dept2", None)
                if opp_val == self:
                    setattr(old_value, "company_Dept2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Dept2"):
                opp_val = getattr(value, "company_Dept2", None)
                setattr(value, "company_Dept2", self)

    @property
    def company_Employee6(self):
        return self.__company_Employee6

    @company_Employee6.setter
    def company_Employee6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee6", None)
        self.__company_Employee6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Person"):
                opp_val = getattr(old_value, "company_Person", None)
                if opp_val == self:
                    setattr(old_value, "company_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Person"):
                opp_val = getattr(value, "company_Person", None)
                setattr(value, "company_Person", self)

class company_Person:

    def __init__(self, name: str, address: str, company_Person: "company_Employee" = None):
        self.name = name
        self.address = address
        self.company_Person = company_Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def company_Person(self):
        return self.__company_Person

    @company_Person.setter
    def company_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Person__company_Person", None)
        self.__company_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Employee6"):
                opp_val = getattr(old_value, "company_Employee6", None)
                if opp_val == self:
                    setattr(old_value, "company_Employee6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Employee6"):
                opp_val = getattr(value, "company_Employee6", None)
                setattr(value, "company_Employee6", self)

class company_Subunit(ABC):

    pass
class company_Dept(Subunit):

    def __init__(self, name: str, company_Dept: "company_Company" = None, company_Dept4: set["company_Subunit"] = None, company_Dept2: "company_Employee" = None):
        self.name = name
        self.company_Dept = company_Dept
        self.company_Dept4 = company_Dept4 if company_Dept4 is not None else set()
        self.company_Dept2 = company_Dept2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def company_Dept4(self):
        return self.__company_Dept4

    @company_Dept4.setter
    def company_Dept4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Dept__company_Dept4", None)
        self.__company_Dept4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company_Subunit"):
                    opp_val = getattr(item, "company_Subunit", None)
                    
                    if opp_val == self:
                        setattr(item, "company_Subunit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company_Subunit"):
                    opp_val = getattr(item, "company_Subunit", None)
                    
                    setattr(item, "company_Subunit", self)
                    

    @property
    def company_Dept2(self):
        return self.__company_Dept2

    @company_Dept2.setter
    def company_Dept2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Dept__company_Dept2", None)
        self.__company_Dept2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Employee"):
                opp_val = getattr(old_value, "company_Employee", None)
                if opp_val == self:
                    setattr(old_value, "company_Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Employee"):
                opp_val = getattr(value, "company_Employee", None)
                setattr(value, "company_Employee", self)

    @property
    def company_Dept(self):
        return self.__company_Dept

    @company_Dept.setter
    def company_Dept(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Dept__company_Dept", None)
        self.__company_Dept = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Company"):
                opp_val = getattr(old_value, "company_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Company"):
                opp_val = getattr(value, "company_Company", None)
                if opp_val is None:
                    setattr(value, "company_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class company_Company:

    pass