from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Gender(Enum):
    male = "male"
    female = "female"


############################################
# Definition of Classes
############################################

class company_Company:

    def __init__(self, name: str, numberOfManager: int, Company: "company_Person" = None, managerCompanies: set["company_Person"] = None):
        self.name = name
        self.numberOfManager = numberOfManager
        self.Company = Company
        self.managerCompanies = managerCompanies if managerCompanies is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def numberOfManager(self) -> int:
        return self.__numberOfManager

    @numberOfManager.setter
    def numberOfManager(self, numberOfManager: int):
        self.__numberOfManager = numberOfManager

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
            if hasattr(old_value, "manager"):
                opp_val = getattr(old_value, "manager", None)
                if opp_val == self:
                    setattr(old_value, "manager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager"):
                opp_val = getattr(value, "manager", None)
                setattr(value, "manager", self)

    @property
    def managerCompanies(self):
        return self.__managerCompanies

    @managerCompanies.setter
    def managerCompanies(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Company__managerCompanies", None)
        self.__managerCompanies = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

class company_Person:

    def __init__(self, name: str, lastname: str, gender: str, age: int, isUnemployed: bool, salary: int, manager: "company_Company" = None, Person: "company_Company" = None):
        self.name = name
        self.lastname = lastname
        self.gender = gender
        self.age = age
        self.isUnemployed = isUnemployed
        self.salary = salary
        self.manager = manager
        self.Person = Person
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isUnemployed(self) -> bool:
        return self.__isUnemployed

    @isUnemployed.setter
    def isUnemployed(self, isUnemployed: bool):
        self.__isUnemployed = isUnemployed

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self, salary: int):
        self.__salary = salary

    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Person__manager", None)
        self.__manager = value
        
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
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "managerCompanies"):
                opp_val = getattr(old_value, "managerCompanies", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "managerCompanies"):
                opp_val = getattr(value, "managerCompanies", None)
                if opp_val is None:
                    setattr(value, "managerCompanies", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
