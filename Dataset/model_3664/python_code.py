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

    def __init__(self, id: int, name: str, address: str, employee_EmailAddress: "employee_Employee" = None):
        self.id = id
        self.name = name
        self.address = address
        self.employee_EmailAddress = employee_EmailAddress
        
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
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

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
            if hasattr(old_value, "employee_Employee21"):
                opp_val = getattr(old_value, "employee_Employee21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee21"):
                opp_val = getattr(value, "employee_Employee21", None)
                if opp_val is None:
                    setattr(value, "employee_Employee21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class employee_Degree:

    def __init__(self, name: str, employee_Degree: "employee_Employee" = None):
        self.name = name
        self.employee_Degree = employee_Degree
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "employee_Employee16"):
                opp_val = getattr(old_value, "employee_Employee16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee16"):
                opp_val = getattr(value, "employee_Employee16", None)
                if opp_val is None:
                    setattr(value, "employee_Employee16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class employee_Address:

    def __init__(self, id: int, city: str, country: str, province: str, postalCode: str, street: str, employee_Address: "employee_Employee" = None):
        self.id = id
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
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def postalCode(self) -> str:
        return self.__postalCode

    @postalCode.setter
    def postalCode(self, postalCode: str):
        self.__postalCode = postalCode

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

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
    def employee_Address(self):
        return self.__employee_Address

    @employee_Address.setter
    def employee_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Address__employee_Address", None)
        self.__employee_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee5"):
                opp_val = getattr(old_value, "employee_Employee5", None)
                if opp_val == self:
                    setattr(old_value, "employee_Employee5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee5"):
                opp_val = getattr(value, "employee_Employee5", None)
                setattr(value, "employee_Employee5", self)

class employee_EmploymentPeriod:

    def __init__(self, id: int, startDate: date, endDate: date, employee_EmploymentPeriod: "employee_Employee" = None):
        self.id = id
        self.startDate = startDate
        self.endDate = endDate
        self.employee_EmploymentPeriod = employee_EmploymentPeriod
        
    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def endDate(self) -> date:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

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
            if hasattr(old_value, "employee_Employee3"):
                opp_val = getattr(old_value, "employee_Employee3", None)
                if opp_val == self:
                    setattr(old_value, "employee_Employee3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee3"):
                opp_val = getattr(value, "employee_Employee3", None)
                setattr(value, "employee_Employee3", self)

class employee_JobTitle:

    def __init__(self, title: str, employee_JobTitle: "employee_Employee" = None):
        self.title = title
        self.employee_JobTitle = employee_JobTitle
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

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
            if hasattr(old_value, "employee_Employee7"):
                opp_val = getattr(old_value, "employee_Employee7", None)
                if opp_val == self:
                    setattr(old_value, "employee_Employee7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee7"):
                opp_val = getattr(value, "employee_Employee7", None)
                setattr(value, "employee_Employee7", self)

class Project:

    pass
class employee_LargeProject(Project):

    def __init__(self, budget: float, milestone: date):
        self.budget = budget
        self.milestone = milestone
        
    @property
    def budget(self) -> float:
        return self.__budget

    @budget.setter
    def budget(self, budget: float):
        self.__budget = budget

    @property
    def milestone(self) -> date:
        return self.__milestone

    @milestone.setter
    def milestone(self, milestone: date):
        self.__milestone = milestone

class employee_SmallProject(Project):

    pass
class employee_Employee:

    def __init__(self, gender: str, firstName: str, lastName: str, salary: float, version: str, responsibilities: str, employee_Employee: "employee_Project" = None, Employee: "employee_PhoneNumber" = None, Employee10: "employee_Employee" = None, managedEmployees: "employee_Employee" = None, Employee13: "employee_Employee" = None, manager: set["employee_Employee"] = None, employee_Employee3: "employee_EmploymentPeriod" = None, owner: set["employee_PhoneNumber"] = None, employee_Employee5: "employee_Address" = None, employee_Employee7: "employee_JobTitle" = None, employee_Employee21: set["employee_EmailAddress"] = None, employee_Employee16: set["employee_Degree"] = None, employee_Employee18: set["employee_Project"] = None):
        self.gender = gender
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.version = version
        self.responsibilities = responsibilities
        self.employee_Employee = employee_Employee
        self.Employee = Employee
        self.Employee10 = Employee10
        self.managedEmployees = managedEmployees
        self.Employee13 = Employee13
        self.manager = manager if manager is not None else set()
        self.employee_Employee3 = employee_Employee3
        self.owner = owner if owner is not None else set()
        self.employee_Employee5 = employee_Employee5
        self.employee_Employee7 = employee_Employee7
        self.employee_Employee21 = employee_Employee21 if employee_Employee21 is not None else set()
        self.employee_Employee16 = employee_Employee16 if employee_Employee16 is not None else set()
        self.employee_Employee18 = employee_Employee18 if employee_Employee18 is not None else set()
        
    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def responsibilities(self) -> str:
        return self.__responsibilities

    @responsibilities.setter
    def responsibilities(self, responsibilities: str):
        self.__responsibilities = responsibilities

    @property
    def employee_Employee3(self):
        return self.__employee_Employee3

    @employee_Employee3.setter
    def employee_Employee3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee3", None)
        self.__employee_Employee3 = value
        
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
                if hasattr(item, "Employee13"):
                    opp_val = getattr(item, "Employee13", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee13"):
                    opp_val = getattr(item, "Employee13", None)
                    
                    setattr(item, "Employee13", self)
                    

    @property
    def Employee13(self):
        return self.__Employee13

    @Employee13.setter
    def Employee13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__Employee13", None)
        self.__Employee13 = value
        
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
    def employee_Employee5(self):
        return self.__employee_Employee5

    @employee_Employee5.setter
    def employee_Employee5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee5", None)
        self.__employee_Employee5 = value
        
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
    def employee_Employee16(self):
        return self.__employee_Employee16

    @employee_Employee16.setter
    def employee_Employee16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee16", None)
        self.__employee_Employee16 = value if value is not None else set()
        
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
    def employee_Employee18(self):
        return self.__employee_Employee18

    @employee_Employee18.setter
    def employee_Employee18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee18", None)
        self.__employee_Employee18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee_Project19"):
                    opp_val = getattr(item, "employee_Project19", None)
                    
                    if opp_val == self:
                        setattr(item, "employee_Project19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee_Project19"):
                    opp_val = getattr(item, "employee_Project19", None)
                    
                    setattr(item, "employee_Project19", self)
                    

    @property
    def employee_Employee21(self):
        return self.__employee_Employee21

    @employee_Employee21.setter
    def employee_Employee21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee21", None)
        self.__employee_Employee21 = value if value is not None else set()
        
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
            if hasattr(old_value, "Employee10"):
                opp_val = getattr(old_value, "Employee10", None)
                if opp_val == self:
                    setattr(old_value, "Employee10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee10"):
                opp_val = getattr(value, "Employee10", None)
                setattr(value, "Employee10", self)

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
            if hasattr(old_value, "employee_Project"):
                opp_val = getattr(old_value, "employee_Project", None)
                if opp_val == self:
                    setattr(old_value, "employee_Project", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Project"):
                opp_val = getattr(value, "employee_Project", None)
                setattr(value, "employee_Project", self)

    @property
    def employee_Employee7(self):
        return self.__employee_Employee7

    @employee_Employee7.setter
    def employee_Employee7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee7", None)
        self.__employee_Employee7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_JobTitle"):
                opp_val = getattr(old_value, "employee_JobTitle", None)
                if opp_val == self:
                    setattr(old_value, "employee_JobTitle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_JobTitle"):
                opp_val = getattr(value, "employee_JobTitle", None)
                setattr(value, "employee_JobTitle", self)

    @property
    def Employee10(self):
        return self.__Employee10

    @Employee10.setter
    def Employee10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__Employee10", None)
        self.__Employee10 = value
        
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

class employee_PhoneNumber:

    def __init__(self, number: str, type: str, areaCode: str, phoneNumbers: "employee_Employee" = None, PhoneNumber: "employee_Employee" = None):
        self.number = number
        self.type = type
        self.areaCode = areaCode
        self.phoneNumbers = phoneNumbers
        self.PhoneNumber = PhoneNumber
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def areaCode(self) -> str:
        return self.__areaCode

    @areaCode.setter
    def areaCode(self, areaCode: str):
        self.__areaCode = areaCode

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

class employee_Project(ABC):

    def __init__(self, name: str, description: str, employee_Project: "employee_Employee" = None, employee_Project19: "employee_Employee" = None):
        self.name = name
        self.description = description
        self.employee_Project = employee_Project
        self.employee_Project19 = employee_Project19
        
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
            if hasattr(old_value, "employee_Employee"):
                opp_val = getattr(old_value, "employee_Employee", None)
                if opp_val == self:
                    setattr(old_value, "employee_Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee"):
                opp_val = getattr(value, "employee_Employee", None)
                setattr(value, "employee_Employee", self)

    @property
    def employee_Project19(self):
        return self.__employee_Project19

    @employee_Project19.setter
    def employee_Project19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Project__employee_Project19", None)
        self.__employee_Project19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee18"):
                opp_val = getattr(old_value, "employee_Employee18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee18"):
                opp_val = getattr(value, "employee_Employee18", None)
                if opp_val is None:
                    setattr(value, "employee_Employee18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
