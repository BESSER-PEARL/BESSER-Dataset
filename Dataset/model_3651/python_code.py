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

class noreflectioncompany_Employee:

    def __init__(self, name: str, hasNameAsAttribute: bool, Employee: "noreflectioncompany_Company" = None, noreflectioncompany_Employee: "noreflectioncompany_Employee" = None, noreflectioncompany_Employee1: "noreflectioncompany_Employee" = None, employees: "noreflectioncompany_Company" = None, noreflectioncompany_Employee6: "noreflectioncompany_Employee" = None, noreflectioncompany_Employee4: set["noreflectioncompany_Employee"] = None, noreflectioncompany_Employee9: "noreflectioncompany_Employee" = None, noreflectioncompany_Employee7: set["noreflectioncompany_Employee"] = None, noreflectioncompany_Employee12: "noreflectioncompany_Employee" = None, noreflectioncompany_Employee10: set["noreflectioncompany_Employee"] = None):
        self.name = name
        self.hasNameAsAttribute = hasNameAsAttribute
        self.Employee = Employee
        self.noreflectioncompany_Employee = noreflectioncompany_Employee
        self.noreflectioncompany_Employee1 = noreflectioncompany_Employee1
        self.employees = employees
        self.noreflectioncompany_Employee6 = noreflectioncompany_Employee6
        self.noreflectioncompany_Employee4 = noreflectioncompany_Employee4 if noreflectioncompany_Employee4 is not None else set()
        self.noreflectioncompany_Employee9 = noreflectioncompany_Employee9
        self.noreflectioncompany_Employee7 = noreflectioncompany_Employee7 if noreflectioncompany_Employee7 is not None else set()
        self.noreflectioncompany_Employee12 = noreflectioncompany_Employee12
        self.noreflectioncompany_Employee10 = noreflectioncompany_Employee10 if noreflectioncompany_Employee10 is not None else set()
        
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
    def noreflectioncompany_Employee1(self):
        return self.__noreflectioncompany_Employee1

    @noreflectioncompany_Employee1.setter
    def noreflectioncompany_Employee1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noreflectioncompany_Employee__noreflectioncompany_Employee1", None)
        self.__noreflectioncompany_Employee1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noreflectioncompany_Employee"):
                opp_val = getattr(old_value, "noreflectioncompany_Employee", None)
                if opp_val == self:
                    setattr(old_value, "noreflectioncompany_Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noreflectioncompany_Employee"):
                opp_val = getattr(value, "noreflectioncompany_Employee", None)
                setattr(value, "noreflectioncompany_Employee", self)

    @property
    def noreflectioncompany_Employee(self):
        return self.__noreflectioncompany_Employee

    @noreflectioncompany_Employee.setter
    def noreflectioncompany_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noreflectioncompany_Employee__noreflectioncompany_Employee", None)
        self.__noreflectioncompany_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noreflectioncompany_Employee1"):
                opp_val = getattr(old_value, "noreflectioncompany_Employee1", None)
                if opp_val == self:
                    setattr(old_value, "noreflectioncompany_Employee1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noreflectioncompany_Employee1"):
                opp_val = getattr(value, "noreflectioncompany_Employee1", None)
                setattr(value, "noreflectioncompany_Employee1", self)

    @property
    def noreflectioncompany_Employee9(self):
        return self.__noreflectioncompany_Employee9

    @noreflectioncompany_Employee9.setter
    def noreflectioncompany_Employee9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noreflectioncompany_Employee__noreflectioncompany_Employee9", None)
        self.__noreflectioncompany_Employee9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noreflectioncompany_Employee7"):
                opp_val = getattr(old_value, "noreflectioncompany_Employee7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noreflectioncompany_Employee7"):
                opp_val = getattr(value, "noreflectioncompany_Employee7", None)
                if opp_val is None:
                    setattr(value, "noreflectioncompany_Employee7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noreflectioncompany_Employee__Employee", None)
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
    def noreflectioncompany_Employee4(self):
        return self.__noreflectioncompany_Employee4

    @noreflectioncompany_Employee4.setter
    def noreflectioncompany_Employee4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noreflectioncompany_Employee__noreflectioncompany_Employee4", None)
        self.__noreflectioncompany_Employee4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "noreflectioncompany_Employee6"):
                    opp_val = getattr(item, "noreflectioncompany_Employee6", None)
                    
                    if opp_val == self:
                        setattr(item, "noreflectioncompany_Employee6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "noreflectioncompany_Employee6"):
                    opp_val = getattr(item, "noreflectioncompany_Employee6", None)
                    
                    setattr(item, "noreflectioncompany_Employee6", self)
                    

    @property
    def noreflectioncompany_Employee6(self):
        return self.__noreflectioncompany_Employee6

    @noreflectioncompany_Employee6.setter
    def noreflectioncompany_Employee6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noreflectioncompany_Employee__noreflectioncompany_Employee6", None)
        self.__noreflectioncompany_Employee6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noreflectioncompany_Employee4"):
                opp_val = getattr(old_value, "noreflectioncompany_Employee4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noreflectioncompany_Employee4"):
                opp_val = getattr(value, "noreflectioncompany_Employee4", None)
                if opp_val is None:
                    setattr(value, "noreflectioncompany_Employee4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def noreflectioncompany_Employee10(self):
        return self.__noreflectioncompany_Employee10

    @noreflectioncompany_Employee10.setter
    def noreflectioncompany_Employee10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noreflectioncompany_Employee__noreflectioncompany_Employee10", None)
        self.__noreflectioncompany_Employee10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "noreflectioncompany_Employee12"):
                    opp_val = getattr(item, "noreflectioncompany_Employee12", None)
                    
                    if opp_val == self:
                        setattr(item, "noreflectioncompany_Employee12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "noreflectioncompany_Employee12"):
                    opp_val = getattr(item, "noreflectioncompany_Employee12", None)
                    
                    setattr(item, "noreflectioncompany_Employee12", self)
                    

    @property
    def noreflectioncompany_Employee12(self):
        return self.__noreflectioncompany_Employee12

    @noreflectioncompany_Employee12.setter
    def noreflectioncompany_Employee12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noreflectioncompany_Employee__noreflectioncompany_Employee12", None)
        self.__noreflectioncompany_Employee12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noreflectioncompany_Employee10"):
                opp_val = getattr(old_value, "noreflectioncompany_Employee10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noreflectioncompany_Employee10"):
                opp_val = getattr(value, "noreflectioncompany_Employee10", None)
                if opp_val is None:
                    setattr(value, "noreflectioncompany_Employee10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def noreflectioncompany_Employee7(self):
        return self.__noreflectioncompany_Employee7

    @noreflectioncompany_Employee7.setter
    def noreflectioncompany_Employee7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noreflectioncompany_Employee__noreflectioncompany_Employee7", None)
        self.__noreflectioncompany_Employee7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "noreflectioncompany_Employee9"):
                    opp_val = getattr(item, "noreflectioncompany_Employee9", None)
                    
                    if opp_val == self:
                        setattr(item, "noreflectioncompany_Employee9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "noreflectioncompany_Employee9"):
                    opp_val = getattr(item, "noreflectioncompany_Employee9", None)
                    
                    setattr(item, "noreflectioncompany_Employee9", self)
                    

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noreflectioncompany_Employee__employees", None)
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

    def hasNameAsOperation(self) -> bool:
        # TODO: Implement hasNameAsOperation method
        pass

    def noManagerImpliesDirectReports(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement noManagerImpliesDirectReports method
        pass

    def reportsTo(self, manager: str) -> bool:
        # TODO: Implement reportsTo method
        pass

class noreflectioncompany_Company:

    def __init__(self, name: str, size: str, company: set["noreflectioncompany_Employee"] = None, Company: "noreflectioncompany_Employee" = None):
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
        old_value = getattr(self, f"_noreflectioncompany_Company__company", None)
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
        old_value = getattr(self, f"_noreflectioncompany_Company__Company", None)
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
