from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PersonsModel:

    pass
class Persons_Person(ABC):

    def __init__(self, fullName: str, 0: "PersonsModel" = None):
        self.fullName = fullName
        self.0 = 0
        
    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def 0(self):
        return self.__0

    @0.setter
    def 0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Persons_Person__0", None)
        self.__0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#"):
                opp_val = getattr(old_value, "#", None)
                if opp_val == self:
                    setattr(old_value, "#", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#"):
                opp_val = getattr(value, "#", None)
                setattr(value, "#", self)

class Persons_PersonsModel:

    pass
class Person:

    pass
class Persons_Female(Person):

    pass
class Persons_Employee(Person):

    pass
class Persons_Male(Person):

    pass