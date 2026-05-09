from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SexType(Enum):
    female = "female"
    male = "male"


############################################
# Definition of Classes
############################################

class Person:

    pass
class family_Child(Person):

    pass
class family_Mother(Person):

    pass
class family_Father(Person):

    pass
class FNamedElement:

    pass
class family_Family(FNamedElement):

    pass
class family_Person(FNamedElement):

    def __init__(self, age: int, sex: str, family_Person: "family_Family" = None):
        self.age = age
        self.sex = sex
        self.family_Person = family_Person
        
        pass
    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age


    @property
    def family_Person(self):
        return self.__family_Person

    @family_Person.setter
    def family_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__family_Person", None)
        self.__family_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Family"):
                opp_val = getattr(old_value, "family_Family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Family"):
                opp_val = getattr(value, "family_Family", None)
                if opp_val is None:
                    setattr(value, "family_Family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class family_FNamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

