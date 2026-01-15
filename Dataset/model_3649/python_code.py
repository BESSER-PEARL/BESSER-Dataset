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

class company_Employee:

    def __init__(self, name: str, hasNameAsAttribute: bool, company_Employee: "company_Employee" = None, company_Employee1: "company_Employee" = None, Employee: "company_Company" = None, company_Employee12: "company_Employee" = None, company_Employee10: set["company_Employee"] = None, employees: "company_Company" = None, company_Employee6: "company_Employee" = None, company_Employee4: set["company_Employee"] = None, company_Employee9: "company_Employee" = None, company_Employee7: set["company_Employee"] = None):
        self.name = name
        self.hasNameAsAttribute = hasNameAsAttribute
        self.company_Employee = company_Employee
        self.company_Employee1 = company_Employee1
        self.Employee = Employee
        self.company_Employee12 = company_Employee12
        self.company_Employee10 = company_Employee10 if company_Employee10 is not None else set()
        self.employees = employees
        self.company_Employee6 = company_Employee6
        self.company_Employee4 = company_Employee4 if company_Employee4 is not None else set()
        self.company_Employee9 = company_Employee9
        self.company_Employee7 = company_Employee7 if company_Employee7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hasNameAsAttribute(self) -> bool:
        return self.__hasNameAsAttribute

    @hasNameAsAttribute.setter
    def hasNameAsAttribute(self, hasNameAsAttribute: bool):
        self.__hasNameAsAttribute = hasNameAsAttribute

    @property
    def company_Employee1(self):
        return self.__company_Employee1

    @company_Employee1.setter
    def company_Employee1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee1", None)
        self.__company_Employee1 = value
        
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
    def company_Employee10(self):
        return self.__company_Employee10

    @company_Employee10.setter
    def company_Employee10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee10", None)
        self.__company_Employee10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company_Employee12"):
                    opp_val = getattr(item, "company_Employee12", None)
                    
                    if opp_val == self:
                        setattr(item, "company_Employee12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company_Employee12"):
                    opp_val = getattr(item, "company_Employee12", None)
                    
                    setattr(item, "company_Employee12", self)
                    

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
            if hasattr(old_value, "company_Employee1"):
                opp_val = getattr(old_value, "company_Employee1", None)
                if opp_val == self:
                    setattr(old_value, "company_Employee1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Employee1"):
                opp_val = getattr(value, "company_Employee1", None)
                setattr(value, "company_Employee1", self)

    @property
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__Employee", None)
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
    def company_Employee6(self):
        return self.__company_Employee6

    @company_Employee6.setter
    def company_Employee6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee6", None)
        self.__company_Employee6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Employee4"):
                opp_val = getattr(old_value, "company_Employee4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Employee4"):
                opp_val = getattr(value, "company_Employee4", None)
                if opp_val is None:
                    setattr(value, "company_Employee4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def company_Employee7(self):
        return self.__company_Employee7

    @company_Employee7.setter
    def company_Employee7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee7", None)
        self.__company_Employee7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company_Employee9"):
                    opp_val = getattr(item, "company_Employee9", None)
                    
                    if opp_val == self:
                        setattr(item, "company_Employee9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company_Employee9"):
                    opp_val = getattr(item, "company_Employee9", None)
                    
                    setattr(item, "company_Employee9", self)
                    

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__employees", None)
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
    def company_Employee12(self):
        return self.__company_Employee12

    @company_Employee12.setter
    def company_Employee12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee12", None)
        self.__company_Employee12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Employee10"):
                opp_val = getattr(old_value, "company_Employee10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Employee10"):
                opp_val = getattr(value, "company_Employee10", None)
                if opp_val is None:
                    setattr(value, "company_Employee10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def company_Employee4(self):
        return self.__company_Employee4

    @company_Employee4.setter
    def company_Employee4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee4", None)
        self.__company_Employee4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company_Employee6"):
                    opp_val = getattr(item, "company_Employee6", None)
                    
                    if opp_val == self:
                        setattr(item, "company_Employee6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company_Employee6"):
                    opp_val = getattr(item, "company_Employee6", None)
                    
                    setattr(item, "company_Employee6", self)
                    

    @property
    def company_Employee9(self):
        return self.__company_Employee9

    @company_Employee9.setter
    def company_Employee9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee9", None)
        self.__company_Employee9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Employee7"):
                opp_val = getattr(old_value, "company_Employee7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Employee7"):
                opp_val = getattr(value, "company_Employee7", None)
                if opp_val is None:
                    setattr(value, "company_Employee7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def hasNameAsOperation(self) -> bool:
        # TODO: Implement hasNameAsOperation method
        pass

    def reportsTo(self, manager: str) -> bool:
        # TODO: Implement reportsTo method
        pass

    def noManagerImpliesDirectReports(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement noManagerImpliesDirectReports method
        pass

class company_Company:

    def __init__(self, name: str, size: str, Company: "company_Employee" = None, company: set["company_Employee"] = None):
        self.name = name
        self.size = size
        self.Company = Company
        self.company = company if company is not None else set()
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Company__company", None)
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
        old_value = getattr(self, f"_company_Company__Company", None)
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

    def dummyInvariant(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement dummyInvariant method
        pass
