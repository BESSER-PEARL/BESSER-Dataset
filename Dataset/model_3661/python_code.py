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

    def __init__(self, id: str, name: str, address: str, employee_EmailAddress: "employee_Employee" = None):
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
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
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
            if hasattr(old_value, "employee_Employee30"):
                opp_val = getattr(old_value, "employee_Employee30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee30"):
                opp_val = getattr(value, "employee_Employee30", None)
                if opp_val is None:
                    setattr(value, "employee_Employee30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class employee_Address:

    def __init__(self, city: str, country: str, province: str, id: str, postalCode: str, street: str, employee_Address: "employee_Employee" = None):
        self.city = city
        self.country = country
        self.province = province
        self.id = id
        self.postalCode = postalCode
        self.street = street
        self.employee_Address = employee_Address
        
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
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

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
            if hasattr(old_value, "employee_Employee13"):
                opp_val = getattr(old_value, "employee_Employee13", None)
                if opp_val == self:
                    setattr(old_value, "employee_Employee13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee13"):
                opp_val = getattr(value, "employee_Employee13", None)
                setattr(value, "employee_Employee13", self)

class employee_EmploymentPeriod:

    def __init__(self, id: str, endDate: date, startDate: date, employee_EmploymentPeriod: "employee_Employee" = None):
        self.id = id
        self.endDate = endDate
        self.startDate = startDate
        self.employee_EmploymentPeriod = employee_EmploymentPeriod
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
            if hasattr(old_value, "employee_Employee11"):
                opp_val = getattr(old_value, "employee_Employee11", None)
                if opp_val == self:
                    setattr(old_value, "employee_Employee11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee11"):
                opp_val = getattr(value, "employee_Employee11", None)
                setattr(value, "employee_Employee11", self)

class employee_PhoneNumber:

    def __init__(self, number: str, areaCode: str, type: str, employee_PhoneNumber: "employee_Employee" = None, employee_PhoneNumber25: "employee_Employee" = None):
        self.number = number
        self.areaCode = areaCode
        self.type = type
        self.employee_PhoneNumber = employee_PhoneNumber
        self.employee_PhoneNumber25 = employee_PhoneNumber25
        
    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

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
    def employee_PhoneNumber25(self):
        return self.__employee_PhoneNumber25

    @employee_PhoneNumber25.setter
    def employee_PhoneNumber25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_PhoneNumber__employee_PhoneNumber25", None)
        self.__employee_PhoneNumber25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee24"):
                opp_val = getattr(old_value, "employee_Employee24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee24"):
                opp_val = getattr(value, "employee_Employee24", None)
                if opp_val is None:
                    setattr(value, "employee_Employee24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def employee_PhoneNumber(self):
        return self.__employee_PhoneNumber

    @employee_PhoneNumber.setter
    def employee_PhoneNumber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_PhoneNumber__employee_PhoneNumber", None)
        self.__employee_PhoneNumber = value
        
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
class employee_JobTitle:

    def __init__(self, title: str, employee_JobTitle: "employee_Organization" = None, employee_JobTitle16: "employee_Employee" = None):
        self.title = title
        self.employee_JobTitle = employee_JobTitle
        self.employee_JobTitle16 = employee_JobTitle16
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def employee_JobTitle16(self):
        return self.__employee_JobTitle16

    @employee_JobTitle16.setter
    def employee_JobTitle16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_JobTitle__employee_JobTitle16", None)
        self.__employee_JobTitle16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee15"):
                opp_val = getattr(old_value, "employee_Employee15", None)
                if opp_val == self:
                    setattr(old_value, "employee_Employee15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee15"):
                opp_val = getattr(value, "employee_Employee15", None)
                setattr(value, "employee_Employee15", self)

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
            if hasattr(old_value, "employee_Organization4"):
                opp_val = getattr(old_value, "employee_Organization4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Organization4"):
                opp_val = getattr(value, "employee_Organization4", None)
                if opp_val is None:
                    setattr(value, "employee_Organization4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class employee_Project(ABC):

    def __init__(self, description: str, name: str, employee_Project: "employee_Organization" = None, employee_Project6: "employee_Employee" = None, employee_Project28: "employee_Employee" = None):
        self.description = description
        self.name = name
        self.employee_Project = employee_Project
        self.employee_Project6 = employee_Project6
        self.employee_Project28 = employee_Project28
        
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
    def employee_Project6(self):
        return self.__employee_Project6

    @employee_Project6.setter
    def employee_Project6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Project__employee_Project6", None)
        self.__employee_Project6 = value
        
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

    @property
    def employee_Project28(self):
        return self.__employee_Project28

    @employee_Project28.setter
    def employee_Project28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Project__employee_Project28", None)
        self.__employee_Project28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee27"):
                opp_val = getattr(old_value, "employee_Employee27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee27"):
                opp_val = getattr(value, "employee_Employee27", None)
                if opp_val is None:
                    setattr(value, "employee_Employee27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "employee_Organization2"):
                opp_val = getattr(old_value, "employee_Organization2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Organization2"):
                opp_val = getattr(value, "employee_Organization2", None)
                if opp_val is None:
                    setattr(value, "employee_Organization2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class employee_Employee:

    def __init__(self, id: str, firstName: str, lastName: str, gender: str, salary: float, responsibilities: str, employee_Employee: "employee_Organization" = None, employee_Employee7: "employee_Project" = None, employee_Employee9: "employee_PhoneNumber" = None, employee_Employee13: "employee_Address" = None, employee_Employee15: "employee_JobTitle" = None, employee_Employee19: "employee_Employee" = None, employee_Employee17: "employee_Employee" = None, employee_Employee22: "employee_Employee" = None, employee_Employee20: set["employee_Employee"] = None, employee_Employee24: set["employee_PhoneNumber"] = None, employee_Employee11: "employee_EmploymentPeriod" = None, employee_Employee30: set["employee_EmailAddress"] = None, employee_Employee27: set["employee_Project"] = None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.salary = salary
        self.responsibilities = responsibilities
        self.employee_Employee = employee_Employee
        self.employee_Employee7 = employee_Employee7
        self.employee_Employee9 = employee_Employee9
        self.employee_Employee13 = employee_Employee13
        self.employee_Employee15 = employee_Employee15
        self.employee_Employee19 = employee_Employee19
        self.employee_Employee17 = employee_Employee17
        self.employee_Employee22 = employee_Employee22
        self.employee_Employee20 = employee_Employee20 if employee_Employee20 is not None else set()
        self.employee_Employee24 = employee_Employee24 if employee_Employee24 is not None else set()
        self.employee_Employee11 = employee_Employee11
        self.employee_Employee30 = employee_Employee30 if employee_Employee30 is not None else set()
        self.employee_Employee27 = employee_Employee27 if employee_Employee27 is not None else set()
        
    @property
    def responsibilities(self) -> str:
        return self.__responsibilities

    @responsibilities.setter
    def responsibilities(self, responsibilities: str):
        self.__responsibilities = responsibilities

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
    def employee_Employee13(self):
        return self.__employee_Employee13

    @employee_Employee13.setter
    def employee_Employee13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee13", None)
        self.__employee_Employee13 = value
        
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
    def employee_Employee11(self):
        return self.__employee_Employee11

    @employee_Employee11.setter
    def employee_Employee11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee11", None)
        self.__employee_Employee11 = value
        
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
    def employee_Employee19(self):
        return self.__employee_Employee19

    @employee_Employee19.setter
    def employee_Employee19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee19", None)
        self.__employee_Employee19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee17"):
                opp_val = getattr(old_value, "employee_Employee17", None)
                if opp_val == self:
                    setattr(old_value, "employee_Employee17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee17"):
                opp_val = getattr(value, "employee_Employee17", None)
                setattr(value, "employee_Employee17", self)

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
            if hasattr(old_value, "employee_PhoneNumber"):
                opp_val = getattr(old_value, "employee_PhoneNumber", None)
                if opp_val == self:
                    setattr(old_value, "employee_PhoneNumber", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_PhoneNumber"):
                opp_val = getattr(value, "employee_PhoneNumber", None)
                setattr(value, "employee_PhoneNumber", self)

    @property
    def employee_Employee15(self):
        return self.__employee_Employee15

    @employee_Employee15.setter
    def employee_Employee15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee15", None)
        self.__employee_Employee15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_JobTitle16"):
                opp_val = getattr(old_value, "employee_JobTitle16", None)
                if opp_val == self:
                    setattr(old_value, "employee_JobTitle16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_JobTitle16"):
                opp_val = getattr(value, "employee_JobTitle16", None)
                setattr(value, "employee_JobTitle16", self)

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
            if hasattr(old_value, "employee_Project6"):
                opp_val = getattr(old_value, "employee_Project6", None)
                if opp_val == self:
                    setattr(old_value, "employee_Project6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Project6"):
                opp_val = getattr(value, "employee_Project6", None)
                setattr(value, "employee_Project6", self)

    @property
    def employee_Employee27(self):
        return self.__employee_Employee27

    @employee_Employee27.setter
    def employee_Employee27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee27", None)
        self.__employee_Employee27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee_Project28"):
                    opp_val = getattr(item, "employee_Project28", None)
                    
                    if opp_val == self:
                        setattr(item, "employee_Project28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee_Project28"):
                    opp_val = getattr(item, "employee_Project28", None)
                    
                    setattr(item, "employee_Project28", self)
                    

    @property
    def employee_Employee17(self):
        return self.__employee_Employee17

    @employee_Employee17.setter
    def employee_Employee17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee17", None)
        self.__employee_Employee17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee19"):
                opp_val = getattr(old_value, "employee_Employee19", None)
                if opp_val == self:
                    setattr(old_value, "employee_Employee19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee19"):
                opp_val = getattr(value, "employee_Employee19", None)
                setattr(value, "employee_Employee19", self)

    @property
    def employee_Employee30(self):
        return self.__employee_Employee30

    @employee_Employee30.setter
    def employee_Employee30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee30", None)
        self.__employee_Employee30 = value if value is not None else set()
        
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
    def employee_Employee24(self):
        return self.__employee_Employee24

    @employee_Employee24.setter
    def employee_Employee24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee24", None)
        self.__employee_Employee24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee_PhoneNumber25"):
                    opp_val = getattr(item, "employee_PhoneNumber25", None)
                    
                    if opp_val == self:
                        setattr(item, "employee_PhoneNumber25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee_PhoneNumber25"):
                    opp_val = getattr(item, "employee_PhoneNumber25", None)
                    
                    setattr(item, "employee_PhoneNumber25", self)
                    

    @property
    def employee_Employee20(self):
        return self.__employee_Employee20

    @employee_Employee20.setter
    def employee_Employee20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee20", None)
        self.__employee_Employee20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee_Employee22"):
                    opp_val = getattr(item, "employee_Employee22", None)
                    
                    if opp_val == self:
                        setattr(item, "employee_Employee22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee_Employee22"):
                    opp_val = getattr(item, "employee_Employee22", None)
                    
                    setattr(item, "employee_Employee22", self)
                    

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
            if hasattr(old_value, "employee_Organization"):
                opp_val = getattr(old_value, "employee_Organization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Organization"):
                opp_val = getattr(value, "employee_Organization", None)
                if opp_val is None:
                    setattr(value, "employee_Organization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def employee_Employee22(self):
        return self.__employee_Employee22

    @employee_Employee22.setter
    def employee_Employee22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee22", None)
        self.__employee_Employee22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee20"):
                opp_val = getattr(old_value, "employee_Employee20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee20"):
                opp_val = getattr(value, "employee_Employee20", None)
                if opp_val is None:
                    setattr(value, "employee_Employee20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class employee_Organization:

    def __init__(self, name: str, employee_Organization: set["employee_Employee"] = None, employee_Organization2: set["employee_Project"] = None, employee_Organization4: set["employee_JobTitle"] = None):
        self.name = name
        self.employee_Organization = employee_Organization if employee_Organization is not None else set()
        self.employee_Organization2 = employee_Organization2 if employee_Organization2 is not None else set()
        self.employee_Organization4 = employee_Organization4 if employee_Organization4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def employee_Organization4(self):
        return self.__employee_Organization4

    @employee_Organization4.setter
    def employee_Organization4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Organization__employee_Organization4", None)
        self.__employee_Organization4 = value if value is not None else set()
        
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
                    

    @property
    def employee_Organization2(self):
        return self.__employee_Organization2

    @employee_Organization2.setter
    def employee_Organization2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Organization__employee_Organization2", None)
        self.__employee_Organization2 = value if value is not None else set()
        
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
    def employee_Organization(self):
        return self.__employee_Organization

    @employee_Organization.setter
    def employee_Organization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Organization__employee_Organization", None)
        self.__employee_Organization = value if value is not None else set()
        
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
                    
