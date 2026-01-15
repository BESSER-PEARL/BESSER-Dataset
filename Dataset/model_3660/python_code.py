from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Gender(Enum):
    Male = "Male"
    Female = "Female"


############################################
# Definition of Classes
############################################

class employee_EmailAddress:

    def __init__(self, address: str, employee_EmailAddress: "employee_Employee" = None):
        self.address = address
        self.employee_EmailAddress = employee_EmailAddress
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def employee_EmailAddress(self):
        return self.__employee_EmailAddress

    @employee_EmailAddress.setter
    def employee_EmailAddress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_EmailAddress__employee_EmailAddress", None)
        self.__employee_EmailAddress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee32"):
                opp_val = getattr(old_value, "employee_Employee32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee32"):
                opp_val = getattr(value, "employee_Employee32", None)
                if opp_val is None:
                    setattr(value, "employee_Employee32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class employee_Address:

    def __init__(self, city: str, country: str, province: str, postalCode: str, street: str, employee_Address: "employee_Employee" = None):
        self.city = city
        self.country = country
        self.province = province
        self.postalCode = postalCode
        self.street = street
        self.employee_Address = employee_Address
        
    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def postalCode(self) -> str:
        return self.__postalCode

    @postalCode.setter
    def postalCode(self, postalCode: str):
        self.__postalCode = postalCode

    @property
    def province(self) -> str:
        return self.__province

    @province.setter
    def province(self, province: str):
        self.__province = province

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def employee_Address(self):
        return self.__employee_Address

    @employee_Address.setter
    def employee_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Address__employee_Address", None)
        self.__employee_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee14"):
                opp_val = getattr(old_value, "employee_Employee14", None)
                if opp_val == self:
                    setattr(old_value, "employee_Employee14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee14"):
                opp_val = getattr(value, "employee_Employee14", None)
                setattr(value, "employee_Employee14", self)

class employee_PhoneNumber:

    def __init__(self, type: str, areaCode: str, number: str, phoneNumbers: "employee_Employee" = None, PhoneNumber: "employee_Employee" = None):
        self.type = type
        self.areaCode = areaCode
        self.number = number
        self.phoneNumbers = phoneNumbers
        self.PhoneNumber = PhoneNumber
        
    @property
    def areaCode(self) -> str:
        return self.__areaCode

    @areaCode.setter
    def areaCode(self, areaCode: str):
        self.__areaCode = areaCode

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def phoneNumbers(self):
        return self.__phoneNumbers

    @phoneNumbers.setter
    def phoneNumbers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_PhoneNumber__phoneNumbers", None)
        self.__phoneNumbers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee"):
                opp_val = getattr(old_value, "Employee", None)
                if opp_val == self:
                    setattr(old_value, "Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee"):
                opp_val = getattr(value, "Employee", None)
                setattr(value, "Employee", self)

    @property
    def PhoneNumber(self):
        return self.__PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_PhoneNumber__PhoneNumber", None)
        self.__PhoneNumber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Project:

    pass
class employee_LargeProject(Project):

    def __init__(self, budget: float, milestone: date):
        self.budget = budget
        self.milestone = milestone
        
    @property
    def milestone(self) -> date:
        return self.__milestone

    @milestone.setter
    def milestone(self, milestone: date):
        self.__milestone = milestone

    @property
    def budget(self) -> float:
        return self.__budget

    @budget.setter
    def budget(self, budget: float):
        self.__budget = budget

class employee_SmallProject(Project):

    pass
class employee_EmploymentPeriod:

    def __init__(self, startDate: date, endDate: date, employee_EmploymentPeriod: "employee_Employee" = None):
        self.startDate = startDate
        self.endDate = endDate
        self.employee_EmploymentPeriod = employee_EmploymentPeriod
        
    @property
    def endDate(self) -> date:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate

    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def employee_EmploymentPeriod(self):
        return self.__employee_EmploymentPeriod

    @employee_EmploymentPeriod.setter
    def employee_EmploymentPeriod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_EmploymentPeriod__employee_EmploymentPeriod", None)
        self.__employee_EmploymentPeriod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee12"):
                opp_val = getattr(old_value, "employee_Employee12", None)
                if opp_val == self:
                    setattr(old_value, "employee_Employee12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee12"):
                opp_val = getattr(value, "employee_Employee12", None)
                setattr(value, "employee_Employee12", self)

class employee_Employee:

    def __init__(self, firstName: str, lastName: str, gender: str, salary: float, responsibilities: str, employee_Employee9: "employee_Project" = None, employee_Employee: "employee_Directory" = None, Employee: "employee_PhoneNumber" = None, employee_Employee14: "employee_Address" = None, employee_Employee16: "employee_JobTitle" = None, Employee20: "employee_Employee" = None, managedEmployees: "employee_Employee" = None, Employee23: "employee_Employee" = None, manager: set["employee_Employee"] = None, owner: set["employee_PhoneNumber"] = None, employee_Employee26: set["employee_Degree"] = None, employee_Employee29: set["employee_Project"] = None, employee_Employee32: set["employee_EmailAddress"] = None, employee_Employee12: "employee_EmploymentPeriod" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.salary = salary
        self.responsibilities = responsibilities
        self.employee_Employee9 = employee_Employee9
        self.employee_Employee = employee_Employee
        self.Employee = Employee
        self.employee_Employee14 = employee_Employee14
        self.employee_Employee16 = employee_Employee16
        self.Employee20 = Employee20
        self.managedEmployees = managedEmployees
        self.Employee23 = Employee23
        self.manager = manager if manager is not None else set()
        self.owner = owner if owner is not None else set()
        self.employee_Employee26 = employee_Employee26 if employee_Employee26 is not None else set()
        self.employee_Employee29 = employee_Employee29 if employee_Employee29 is not None else set()
        self.employee_Employee32 = employee_Employee32 if employee_Employee32 is not None else set()
        self.employee_Employee12 = employee_Employee12
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def responsibilities(self) -> str:
        return self.__responsibilities

    @responsibilities.setter
    def responsibilities(self, responsibilities: str):
        self.__responsibilities = responsibilities

    @property
    def employee_Employee(self):
        return self.__employee_Employee

    @employee_Employee.setter
    def employee_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee", None)
        self.__employee_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Directory2"):
                opp_val = getattr(old_value, "employee_Directory2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Directory2"):
                opp_val = getattr(value, "employee_Directory2", None)
                if opp_val is None:
                    setattr(value, "employee_Directory2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def employee_Employee26(self):
        return self.__employee_Employee26

    @employee_Employee26.setter
    def employee_Employee26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee26", None)
        self.__employee_Employee26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee_Degree27"):
                    opp_val = getattr(item, "employee_Degree27", None)
                    
                    if opp_val == self:
                        setattr(item, "employee_Degree27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee_Degree27"):
                    opp_val = getattr(item, "employee_Degree27", None)
                    
                    setattr(item, "employee_Degree27", self)
                    

    @property
    def employee_Employee14(self):
        return self.__employee_Employee14

    @employee_Employee14.setter
    def employee_Employee14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee14", None)
        self.__employee_Employee14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Address"):
                opp_val = getattr(old_value, "employee_Address", None)
                if opp_val == self:
                    setattr(old_value, "employee_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Address"):
                opp_val = getattr(value, "employee_Address", None)
                setattr(value, "employee_Address", self)

    @property
    def Employee20(self):
        return self.__Employee20

    @Employee20.setter
    def Employee20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__Employee20", None)
        self.__Employee20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "managedEmployees"):
                opp_val = getattr(old_value, "managedEmployees", None)
                if opp_val == self:
                    setattr(old_value, "managedEmployees", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "managedEmployees"):
                opp_val = getattr(value, "managedEmployees", None)
                setattr(value, "managedEmployees", self)

    @property
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__Employee", None)
        self.__Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "phoneNumbers"):
                opp_val = getattr(old_value, "phoneNumbers", None)
                if opp_val == self:
                    setattr(old_value, "phoneNumbers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "phoneNumbers"):
                opp_val = getattr(value, "phoneNumbers", None)
                setattr(value, "phoneNumbers", self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhoneNumber"):
                    opp_val = getattr(item, "PhoneNumber", None)
                    
                    if opp_val == self:
                        setattr(item, "PhoneNumber", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhoneNumber"):
                    opp_val = getattr(item, "PhoneNumber", None)
                    
                    setattr(item, "PhoneNumber", self)
                    

    @property
    def Employee23(self):
        return self.__Employee23

    @Employee23.setter
    def Employee23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__Employee23", None)
        self.__Employee23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager"):
                opp_val = getattr(old_value, "manager", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager"):
                opp_val = getattr(value, "manager", None)
                if opp_val is None:
                    setattr(value, "manager", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def employee_Employee9(self):
        return self.__employee_Employee9

    @employee_Employee9.setter
    def employee_Employee9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee9", None)
        self.__employee_Employee9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Project8"):
                opp_val = getattr(old_value, "employee_Project8", None)
                if opp_val == self:
                    setattr(old_value, "employee_Project8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Project8"):
                opp_val = getattr(value, "employee_Project8", None)
                setattr(value, "employee_Project8", self)

    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__manager", None)
        self.__manager = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee23"):
                    opp_val = getattr(item, "Employee23", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee23"):
                    opp_val = getattr(item, "Employee23", None)
                    
                    setattr(item, "Employee23", self)
                    

    @property
    def employee_Employee32(self):
        return self.__employee_Employee32

    @employee_Employee32.setter
    def employee_Employee32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee32", None)
        self.__employee_Employee32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee_EmailAddress"):
                    opp_val = getattr(item, "employee_EmailAddress", None)
                    
                    if opp_val == self:
                        setattr(item, "employee_EmailAddress", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee_EmailAddress"):
                    opp_val = getattr(item, "employee_EmailAddress", None)
                    
                    setattr(item, "employee_EmailAddress", self)
                    

    @property
    def managedEmployees(self):
        return self.__managedEmployees

    @managedEmployees.setter
    def managedEmployees(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__managedEmployees", None)
        self.__managedEmployees = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee20"):
                opp_val = getattr(old_value, "Employee20", None)
                if opp_val == self:
                    setattr(old_value, "Employee20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee20"):
                opp_val = getattr(value, "Employee20", None)
                setattr(value, "Employee20", self)

    @property
    def employee_Employee29(self):
        return self.__employee_Employee29

    @employee_Employee29.setter
    def employee_Employee29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee29", None)
        self.__employee_Employee29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee_Project30"):
                    opp_val = getattr(item, "employee_Project30", None)
                    
                    if opp_val == self:
                        setattr(item, "employee_Project30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee_Project30"):
                    opp_val = getattr(item, "employee_Project30", None)
                    
                    setattr(item, "employee_Project30", self)
                    

    @property
    def employee_Employee12(self):
        return self.__employee_Employee12

    @employee_Employee12.setter
    def employee_Employee12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee12", None)
        self.__employee_Employee12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_EmploymentPeriod"):
                opp_val = getattr(old_value, "employee_EmploymentPeriod", None)
                if opp_val == self:
                    setattr(old_value, "employee_EmploymentPeriod", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_EmploymentPeriod"):
                opp_val = getattr(value, "employee_EmploymentPeriod", None)
                setattr(value, "employee_EmploymentPeriod", self)

    @property
    def employee_Employee16(self):
        return self.__employee_Employee16

    @employee_Employee16.setter
    def employee_Employee16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee16", None)
        self.__employee_Employee16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_JobTitle17"):
                opp_val = getattr(old_value, "employee_JobTitle17", None)
                if opp_val == self:
                    setattr(old_value, "employee_JobTitle17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_JobTitle17"):
                opp_val = getattr(value, "employee_JobTitle17", None)
                setattr(value, "employee_JobTitle17", self)

class employee_Project(ABC):

    def __init__(self, name: str, description: str, employee_Project8: "employee_Employee" = None, employee_Project: "employee_Directory" = None, employee_Project30: "employee_Employee" = None):
        self.name = name
        self.description = description
        self.employee_Project8 = employee_Project8
        self.employee_Project = employee_Project
        self.employee_Project30 = employee_Project30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def employee_Project(self):
        return self.__employee_Project

    @employee_Project.setter
    def employee_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Project__employee_Project", None)
        self.__employee_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Directory"):
                opp_val = getattr(old_value, "employee_Directory", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Directory"):
                opp_val = getattr(value, "employee_Directory", None)
                if opp_val is None:
                    setattr(value, "employee_Directory", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def employee_Project8(self):
        return self.__employee_Project8

    @employee_Project8.setter
    def employee_Project8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Project__employee_Project8", None)
        self.__employee_Project8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee9"):
                opp_val = getattr(old_value, "employee_Employee9", None)
                if opp_val == self:
                    setattr(old_value, "employee_Employee9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee9"):
                opp_val = getattr(value, "employee_Employee9", None)
                setattr(value, "employee_Employee9", self)

    @property
    def employee_Project30(self):
        return self.__employee_Project30

    @employee_Project30.setter
    def employee_Project30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Project__employee_Project30", None)
        self.__employee_Project30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee29"):
                opp_val = getattr(old_value, "employee_Employee29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee29"):
                opp_val = getattr(value, "employee_Employee29", None)
                if opp_val is None:
                    setattr(value, "employee_Employee29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class employee_Directory:

    def __init__(self, name: str, employee_Directory4: set["employee_JobTitle"] = None, employee_Directory6: set["employee_Degree"] = None, employee_Directory: set["employee_Project"] = None, employee_Directory2: set["employee_Employee"] = None):
        self.name = name
        self.employee_Directory4 = employee_Directory4 if employee_Directory4 is not None else set()
        self.employee_Directory6 = employee_Directory6 if employee_Directory6 is not None else set()
        self.employee_Directory = employee_Directory if employee_Directory is not None else set()
        self.employee_Directory2 = employee_Directory2 if employee_Directory2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def employee_Directory6(self):
        return self.__employee_Directory6

    @employee_Directory6.setter
    def employee_Directory6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Directory__employee_Directory6", None)
        self.__employee_Directory6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee_Degree"):
                    opp_val = getattr(item, "employee_Degree", None)
                    
                    if opp_val == self:
                        setattr(item, "employee_Degree", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee_Degree"):
                    opp_val = getattr(item, "employee_Degree", None)
                    
                    setattr(item, "employee_Degree", self)
                    

    @property
    def employee_Directory2(self):
        return self.__employee_Directory2

    @employee_Directory2.setter
    def employee_Directory2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Directory__employee_Directory2", None)
        self.__employee_Directory2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee_Employee"):
                    opp_val = getattr(item, "employee_Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "employee_Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee_Employee"):
                    opp_val = getattr(item, "employee_Employee", None)
                    
                    setattr(item, "employee_Employee", self)
                    

    @property
    def employee_Directory(self):
        return self.__employee_Directory

    @employee_Directory.setter
    def employee_Directory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Directory__employee_Directory", None)
        self.__employee_Directory = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee_Project"):
                    opp_val = getattr(item, "employee_Project", None)
                    
                    if opp_val == self:
                        setattr(item, "employee_Project", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee_Project"):
                    opp_val = getattr(item, "employee_Project", None)
                    
                    setattr(item, "employee_Project", self)
                    

    @property
    def employee_Directory4(self):
        return self.__employee_Directory4

    @employee_Directory4.setter
    def employee_Directory4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Directory__employee_Directory4", None)
        self.__employee_Directory4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee_JobTitle"):
                    opp_val = getattr(item, "employee_JobTitle", None)
                    
                    if opp_val == self:
                        setattr(item, "employee_JobTitle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee_JobTitle"):
                    opp_val = getattr(item, "employee_JobTitle", None)
                    
                    setattr(item, "employee_JobTitle", self)
                    

class employee_Degree:

    def __init__(self, name: str, employee_Degree: "employee_Directory" = None, employee_Degree27: "employee_Employee" = None):
        self.name = name
        self.employee_Degree = employee_Degree
        self.employee_Degree27 = employee_Degree27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def employee_Degree27(self):
        return self.__employee_Degree27

    @employee_Degree27.setter
    def employee_Degree27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Degree__employee_Degree27", None)
        self.__employee_Degree27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee26"):
                opp_val = getattr(old_value, "employee_Employee26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee26"):
                opp_val = getattr(value, "employee_Employee26", None)
                if opp_val is None:
                    setattr(value, "employee_Employee26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def employee_Degree(self):
        return self.__employee_Degree

    @employee_Degree.setter
    def employee_Degree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Degree__employee_Degree", None)
        self.__employee_Degree = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Directory6"):
                opp_val = getattr(old_value, "employee_Directory6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Directory6"):
                opp_val = getattr(value, "employee_Directory6", None)
                if opp_val is None:
                    setattr(value, "employee_Directory6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class employee_JobTitle:

    def __init__(self, title: str, employee_JobTitle: "employee_Directory" = None, employee_JobTitle17: "employee_Employee" = None):
        self.title = title
        self.employee_JobTitle = employee_JobTitle
        self.employee_JobTitle17 = employee_JobTitle17
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def employee_JobTitle17(self):
        return self.__employee_JobTitle17

    @employee_JobTitle17.setter
    def employee_JobTitle17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_JobTitle__employee_JobTitle17", None)
        self.__employee_JobTitle17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee16"):
                opp_val = getattr(old_value, "employee_Employee16", None)
                if opp_val == self:
                    setattr(old_value, "employee_Employee16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee16"):
                opp_val = getattr(value, "employee_Employee16", None)
                setattr(value, "employee_Employee16", self)

    @property
    def employee_JobTitle(self):
        return self.__employee_JobTitle

    @employee_JobTitle.setter
    def employee_JobTitle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_JobTitle__employee_JobTitle", None)
        self.__employee_JobTitle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Directory4"):
                opp_val = getattr(old_value, "employee_Directory4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Directory4"):
                opp_val = getattr(value, "employee_Directory4", None)
                if opp_val is None:
                    setattr(value, "employee_Directory4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
