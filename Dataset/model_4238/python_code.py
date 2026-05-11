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

class company_Person:

    def __init__(self, lastname: str, gender: str, age: int, isUnemployed: bool, salary: int, name: str, manager: "company_Company" = None, Person: "company_Company" = None):
        self.lastname = lastname
        self.gender = gender
        self.age = age
        self.isUnemployed = isUnemployed
        self.salary = salary
        self.name = name
        self.manager = manager
        self.Person = Person
        
        pass
    @property
    def isUnemployed(self):
        return self.__isUnemployed

    @isUnemployed.setter
    def isUnemployed(self, isUnemployed: bool):
        self.__isUnemployed = isUnemployed


    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary: int):
        self.__salary = salary


    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age


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

class company_Company:

    def __init__(self, name: str, numberOfManager: int, Company: "company_Person" = None, managerCompanies: set["company_Person"] = None):
        self.name = name
        self.numberOfManager = numberOfManager
        self.Company = Company
        self.managerCompanies = managerCompanies if managerCompanies is not None else set()
        
        pass
    @property
    def numberOfManager(self):
        return self.__numberOfManager

    @numberOfManager.setter
    def numberOfManager(self, numberOfManager: int):
        self.__numberOfManager = numberOfManager


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
                    
