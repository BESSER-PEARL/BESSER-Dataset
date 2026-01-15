from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Persons_LocaledElement(ABC):

    pass
class PersonsModel:

    pass
class Persons_Person:

    def __init__(self, fullName: str, Persons_Person: "PersonsModel" = None):
        self.fullName = fullName
        self.Persons_Person = Persons_Person
        
    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def Persons_Person(self):
        return self.__Persons_Person

    @Persons_Person.setter
    def Persons_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Persons_Person__Persons_Person", None)
        self.__Persons_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PersonsModel"):
                opp_val = getattr(old_value, "PersonsModel", None)
                if opp_val == self:
                    setattr(old_value, "PersonsModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PersonsModel"):
                opp_val = getattr(value, "PersonsModel", None)
                setattr(value, "PersonsModel", self)

class Persons_PersonsModel:

    pass
class Person:

    pass
class Persons_Female(Person):

    def __init__(self, age: int, Person: "Persons_PersonsModel"):
        self.age = age
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

class Persons_Employee(Person):

    pass
class Persons_Male(Person):

    def __init__(self, age: int, Person: "Persons_PersonsModel"):
        self.age = age
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age
