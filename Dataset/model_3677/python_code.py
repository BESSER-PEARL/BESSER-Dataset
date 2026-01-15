from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class companies_Visitable:

    pass
class companies_CSTrace(ABC):

    pass
class CSTrace:

    pass
class companies_department_manager(CSTrace):

    pass
class companies_department_employees(CSTrace):

    pass
class companies_department(CSTrace):

    def __init__(self, name: str, companies_department4: "companies_department_employees" = None, companies_department7: "companies_department" = None, companies_department5: set["companies_department"] = None, companies_department: "companies_company" = None, companies_department2: "companies_department_manager" = None):
        self.name = name
        self.companies_department4 = companies_department4
        self.companies_department7 = companies_department7
        self.companies_department5 = companies_department5 if companies_department5 is not None else set()
        self.companies_department = companies_department
        self.companies_department2 = companies_department2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def companies_department4(self):
        return self.__companies_department4

    @companies_department4.setter
    def companies_department4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_companies_department__companies_department4", None)
        self.__companies_department4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "companies_department_employees"):
                opp_val = getattr(old_value, "companies_department_employees", None)
                if opp_val == self:
                    setattr(old_value, "companies_department_employees", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "companies_department_employees"):
                opp_val = getattr(value, "companies_department_employees", None)
                setattr(value, "companies_department_employees", self)

    @property
    def companies_department7(self):
        return self.__companies_department7

    @companies_department7.setter
    def companies_department7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_companies_department__companies_department7", None)
        self.__companies_department7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "companies_department5"):
                opp_val = getattr(old_value, "companies_department5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "companies_department5"):
                opp_val = getattr(value, "companies_department5", None)
                if opp_val is None:
                    setattr(value, "companies_department5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def companies_department2(self):
        return self.__companies_department2

    @companies_department2.setter
    def companies_department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_companies_department__companies_department2", None)
        self.__companies_department2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "companies_department_manager"):
                opp_val = getattr(old_value, "companies_department_manager", None)
                if opp_val == self:
                    setattr(old_value, "companies_department_manager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "companies_department_manager"):
                opp_val = getattr(value, "companies_department_manager", None)
                setattr(value, "companies_department_manager", self)

    @property
    def companies_department(self):
        return self.__companies_department

    @companies_department.setter
    def companies_department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_companies_department__companies_department", None)
        self.__companies_department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "companies_company"):
                opp_val = getattr(old_value, "companies_company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "companies_company"):
                opp_val = getattr(value, "companies_company", None)
                if opp_val is None:
                    setattr(value, "companies_company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def companies_department5(self):
        return self.__companies_department5

    @companies_department5.setter
    def companies_department5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_companies_department__companies_department5", None)
        self.__companies_department5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "companies_department7"):
                    opp_val = getattr(item, "companies_department7", None)
                    
                    if opp_val == self:
                        setattr(item, "companies_department7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "companies_department7"):
                    opp_val = getattr(item, "companies_department7", None)
                    
                    setattr(item, "companies_department7", self)
                    

class companies_company(CSTrace):

    def __init__(self, name: str, companies_company: set["companies_department"] = None):
        self.name = name
        self.companies_company = companies_company if companies_company is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def companies_company(self):
        return self.__companies_company

    @companies_company.setter
    def companies_company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_companies_company__companies_company", None)
        self.__companies_company = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "companies_department"):
                    opp_val = getattr(item, "companies_department", None)
                    
                    if opp_val == self:
                        setattr(item, "companies_department", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "companies_department"):
                    opp_val = getattr(item, "companies_department", None)
                    
                    setattr(item, "companies_department", self)
                    

class companies_employee(CSTrace):

    def __init__(self, name: str, address: str, salary: float, mentor: str, companies_employee: "companies_department_manager" = None, companies_employee12: "companies_department_employees" = None):
        self.name = name
        self.address = address
        self.salary = salary
        self.mentor = mentor
        self.companies_employee = companies_employee
        self.companies_employee12 = companies_employee12
        
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
    def mentor(self) -> str:
        return self.__mentor

    @mentor.setter
    def mentor(self, mentor: str):
        self.__mentor = mentor

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary

    @property
    def companies_employee(self):
        return self.__companies_employee

    @companies_employee.setter
    def companies_employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_companies_employee__companies_employee", None)
        self.__companies_employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "companies_department_manager9"):
                opp_val = getattr(old_value, "companies_department_manager9", None)
                if opp_val == self:
                    setattr(old_value, "companies_department_manager9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "companies_department_manager9"):
                opp_val = getattr(value, "companies_department_manager9", None)
                setattr(value, "companies_department_manager9", self)

    @property
    def companies_employee12(self):
        return self.__companies_employee12

    @companies_employee12.setter
    def companies_employee12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_companies_employee__companies_employee12", None)
        self.__companies_employee12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "companies_department_employees11"):
                opp_val = getattr(old_value, "companies_department_employees11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "companies_department_employees11"):
                opp_val = getattr(value, "companies_department_employees11", None)
                if opp_val is None:
                    setattr(value, "companies_department_employees11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
