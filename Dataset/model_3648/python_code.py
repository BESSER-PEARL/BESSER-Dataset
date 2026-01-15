from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CompanySizeKind(Enum):
    small = "small"
    medium = "medium"
    large = "large"


############################################
# Definition of Classes
############################################

class ecoreJavascriptDelegatesTest_Employee:

    def __init__(self, name: str, Employee: "ecoreJavascriptDelegatesTest_Company" = None, ecoreJavascriptDelegatesTest_Employee: "ecoreJavascriptDelegatesTest_Employee" = None, ecoreJavascriptDelegatesTest_Employee1: "ecoreJavascriptDelegatesTest_Employee" = None, employees: "ecoreJavascriptDelegatesTest_Company" = None, ecoreJavascriptDelegatesTest_Employee6: "ecoreJavascriptDelegatesTest_Employee" = None, ecoreJavascriptDelegatesTest_Employee4: set["ecoreJavascriptDelegatesTest_Employee"] = None, ecoreJavascriptDelegatesTest_Employee9: "ecoreJavascriptDelegatesTest_Employee" = None, ecoreJavascriptDelegatesTest_Employee7: set["ecoreJavascriptDelegatesTest_Employee"] = None, ecoreJavascriptDelegatesTest_Employee12: "ecoreJavascriptDelegatesTest_Employee" = None, ecoreJavascriptDelegatesTest_Employee10: set["ecoreJavascriptDelegatesTest_Employee"] = None):
        self.name = name
        self.Employee = Employee
        self.ecoreJavascriptDelegatesTest_Employee = ecoreJavascriptDelegatesTest_Employee
        self.ecoreJavascriptDelegatesTest_Employee1 = ecoreJavascriptDelegatesTest_Employee1
        self.employees = employees
        self.ecoreJavascriptDelegatesTest_Employee6 = ecoreJavascriptDelegatesTest_Employee6
        self.ecoreJavascriptDelegatesTest_Employee4 = ecoreJavascriptDelegatesTest_Employee4 if ecoreJavascriptDelegatesTest_Employee4 is not None else set()
        self.ecoreJavascriptDelegatesTest_Employee9 = ecoreJavascriptDelegatesTest_Employee9
        self.ecoreJavascriptDelegatesTest_Employee7 = ecoreJavascriptDelegatesTest_Employee7 if ecoreJavascriptDelegatesTest_Employee7 is not None else set()
        self.ecoreJavascriptDelegatesTest_Employee12 = ecoreJavascriptDelegatesTest_Employee12
        self.ecoreJavascriptDelegatesTest_Employee10 = ecoreJavascriptDelegatesTest_Employee10 if ecoreJavascriptDelegatesTest_Employee10 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ecoreJavascriptDelegatesTest_Employee(self):
        return self.__ecoreJavascriptDelegatesTest_Employee

    @ecoreJavascriptDelegatesTest_Employee.setter
    def ecoreJavascriptDelegatesTest_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptDelegatesTest_Employee__ecoreJavascriptDelegatesTest_Employee", None)
        self.__ecoreJavascriptDelegatesTest_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreJavascriptDelegatesTest_Employee1"):
                opp_val = getattr(old_value, "ecoreJavascriptDelegatesTest_Employee1", None)
                if opp_val == self:
                    setattr(old_value, "ecoreJavascriptDelegatesTest_Employee1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreJavascriptDelegatesTest_Employee1"):
                opp_val = getattr(value, "ecoreJavascriptDelegatesTest_Employee1", None)
                setattr(value, "ecoreJavascriptDelegatesTest_Employee1", self)

    @property
    def ecoreJavascriptDelegatesTest_Employee9(self):
        return self.__ecoreJavascriptDelegatesTest_Employee9

    @ecoreJavascriptDelegatesTest_Employee9.setter
    def ecoreJavascriptDelegatesTest_Employee9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptDelegatesTest_Employee__ecoreJavascriptDelegatesTest_Employee9", None)
        self.__ecoreJavascriptDelegatesTest_Employee9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreJavascriptDelegatesTest_Employee7"):
                opp_val = getattr(old_value, "ecoreJavascriptDelegatesTest_Employee7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreJavascriptDelegatesTest_Employee7"):
                opp_val = getattr(value, "ecoreJavascriptDelegatesTest_Employee7", None)
                if opp_val is None:
                    setattr(value, "ecoreJavascriptDelegatesTest_Employee7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreJavascriptDelegatesTest_Employee4(self):
        return self.__ecoreJavascriptDelegatesTest_Employee4

    @ecoreJavascriptDelegatesTest_Employee4.setter
    def ecoreJavascriptDelegatesTest_Employee4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptDelegatesTest_Employee__ecoreJavascriptDelegatesTest_Employee4", None)
        self.__ecoreJavascriptDelegatesTest_Employee4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreJavascriptDelegatesTest_Employee6"):
                    opp_val = getattr(item, "ecoreJavascriptDelegatesTest_Employee6", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreJavascriptDelegatesTest_Employee6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreJavascriptDelegatesTest_Employee6"):
                    opp_val = getattr(item, "ecoreJavascriptDelegatesTest_Employee6", None)
                    
                    setattr(item, "ecoreJavascriptDelegatesTest_Employee6", self)
                    

    @property
    def ecoreJavascriptDelegatesTest_Employee1(self):
        return self.__ecoreJavascriptDelegatesTest_Employee1

    @ecoreJavascriptDelegatesTest_Employee1.setter
    def ecoreJavascriptDelegatesTest_Employee1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptDelegatesTest_Employee__ecoreJavascriptDelegatesTest_Employee1", None)
        self.__ecoreJavascriptDelegatesTest_Employee1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreJavascriptDelegatesTest_Employee"):
                opp_val = getattr(old_value, "ecoreJavascriptDelegatesTest_Employee", None)
                if opp_val == self:
                    setattr(old_value, "ecoreJavascriptDelegatesTest_Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreJavascriptDelegatesTest_Employee"):
                opp_val = getattr(value, "ecoreJavascriptDelegatesTest_Employee", None)
                setattr(value, "ecoreJavascriptDelegatesTest_Employee", self)

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptDelegatesTest_Employee__employees", None)
        self.__employees = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company"):
                opp_val = getattr(old_value, "Company", None)
                if opp_val == self:
                    setattr(old_value, "Company", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company"):
                opp_val = getattr(value, "Company", None)
                setattr(value, "Company", self)

    @property
    def ecoreJavascriptDelegatesTest_Employee12(self):
        return self.__ecoreJavascriptDelegatesTest_Employee12

    @ecoreJavascriptDelegatesTest_Employee12.setter
    def ecoreJavascriptDelegatesTest_Employee12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptDelegatesTest_Employee__ecoreJavascriptDelegatesTest_Employee12", None)
        self.__ecoreJavascriptDelegatesTest_Employee12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreJavascriptDelegatesTest_Employee10"):
                opp_val = getattr(old_value, "ecoreJavascriptDelegatesTest_Employee10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreJavascriptDelegatesTest_Employee10"):
                opp_val = getattr(value, "ecoreJavascriptDelegatesTest_Employee10", None)
                if opp_val is None:
                    setattr(value, "ecoreJavascriptDelegatesTest_Employee10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreJavascriptDelegatesTest_Employee7(self):
        return self.__ecoreJavascriptDelegatesTest_Employee7

    @ecoreJavascriptDelegatesTest_Employee7.setter
    def ecoreJavascriptDelegatesTest_Employee7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptDelegatesTest_Employee__ecoreJavascriptDelegatesTest_Employee7", None)
        self.__ecoreJavascriptDelegatesTest_Employee7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreJavascriptDelegatesTest_Employee9"):
                    opp_val = getattr(item, "ecoreJavascriptDelegatesTest_Employee9", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreJavascriptDelegatesTest_Employee9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreJavascriptDelegatesTest_Employee9"):
                    opp_val = getattr(item, "ecoreJavascriptDelegatesTest_Employee9", None)
                    
                    setattr(item, "ecoreJavascriptDelegatesTest_Employee9", self)
                    

    @property
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptDelegatesTest_Employee__Employee", None)
        self.__Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company"):
                opp_val = getattr(old_value, "company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company"):
                opp_val = getattr(value, "company", None)
                if opp_val is None:
                    setattr(value, "company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreJavascriptDelegatesTest_Employee6(self):
        return self.__ecoreJavascriptDelegatesTest_Employee6

    @ecoreJavascriptDelegatesTest_Employee6.setter
    def ecoreJavascriptDelegatesTest_Employee6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptDelegatesTest_Employee__ecoreJavascriptDelegatesTest_Employee6", None)
        self.__ecoreJavascriptDelegatesTest_Employee6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreJavascriptDelegatesTest_Employee4"):
                opp_val = getattr(old_value, "ecoreJavascriptDelegatesTest_Employee4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreJavascriptDelegatesTest_Employee4"):
                opp_val = getattr(value, "ecoreJavascriptDelegatesTest_Employee4", None)
                if opp_val is None:
                    setattr(value, "ecoreJavascriptDelegatesTest_Employee4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreJavascriptDelegatesTest_Employee10(self):
        return self.__ecoreJavascriptDelegatesTest_Employee10

    @ecoreJavascriptDelegatesTest_Employee10.setter
    def ecoreJavascriptDelegatesTest_Employee10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptDelegatesTest_Employee__ecoreJavascriptDelegatesTest_Employee10", None)
        self.__ecoreJavascriptDelegatesTest_Employee10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreJavascriptDelegatesTest_Employee12"):
                    opp_val = getattr(item, "ecoreJavascriptDelegatesTest_Employee12", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreJavascriptDelegatesTest_Employee12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreJavascriptDelegatesTest_Employee12"):
                    opp_val = getattr(item, "ecoreJavascriptDelegatesTest_Employee12", None)
                    
                    setattr(item, "ecoreJavascriptDelegatesTest_Employee12", self)
                    

    def checkNameLength(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement checkNameLength method
        pass

    def reportsTo(self, manager: str) -> bool:
        # TODO: Implement reportsTo method
        pass

class ecoreJavascriptDelegatesTest_Company:

    def __init__(self, name: str, size: str, company: set["ecoreJavascriptDelegatesTest_Employee"] = None, Company: "ecoreJavascriptDelegatesTest_Employee" = None):
        self.name = name
        self.size = size
        self.company = company if company is not None else set()
        self.Company = Company
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptDelegatesTest_Company__company", None)
        self.__company = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee"):
                    opp_val = getattr(item, "Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee"):
                    opp_val = getattr(item, "Employee", None)
                    
                    setattr(item, "Employee", self)
                    

    @property
    def Company(self):
        return self.__Company

    @Company.setter
    def Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptDelegatesTest_Company__Company", None)
        self.__Company = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employees"):
                opp_val = getattr(old_value, "employees", None)
                if opp_val == self:
                    setattr(old_value, "employees", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employees"):
                opp_val = getattr(value, "employees", None)
                setattr(value, "employees", self)
