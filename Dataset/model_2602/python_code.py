from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class GenderType(Enum):
    male = "male"
    female = "female"


############################################
# Definition of Classes
############################################

class Persons_Person:

    def __init__(self, lastname: str, gender: str, firstname: str, persons: "Persons_Persons" = None, Person: "Persons_Persons" = None):
        self.lastname = lastname
        self.gender = gender
        self.firstname = firstname
        self.persons = persons
        self.Person = Person
        
    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Persons_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "list"):
                opp_val = getattr(old_value, "list", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "list"):
                opp_val = getattr(value, "list", None)
                if opp_val is None:
                    setattr(value, "list", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persons(self):
        return self.__persons

    @persons.setter
    def persons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Persons_Person__persons", None)
        self.__persons = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Persons"):
                opp_val = getattr(old_value, "Persons", None)
                if opp_val == self:
                    setattr(old_value, "Persons", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Persons"):
                opp_val = getattr(value, "Persons", None)
                setattr(value, "Persons", self)

class Persons_Persons:

    pass