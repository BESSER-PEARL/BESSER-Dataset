from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Persons_Person(ABC):

    def __init__(self, name: str, birthday: date, persons: "Persons_PersonRegister" = None, Person: "Persons_PersonRegister" = None):
        self.name = name
        self.birthday = birthday
        self.persons = persons
        self.Person = Person
        
    @property
    def birthday(self) -> date:
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday: date):
        self.__birthday = birthday

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "personsInverse"):
                opp_val = getattr(old_value, "personsInverse", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personsInverse"):
                opp_val = getattr(value, "personsInverse", None)
                if opp_val is None:
                    setattr(value, "personsInverse", set([self]))
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
            if hasattr(old_value, "PersonRegister"):
                opp_val = getattr(old_value, "PersonRegister", None)
                if opp_val == self:
                    setattr(old_value, "PersonRegister", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PersonRegister"):
                opp_val = getattr(value, "PersonRegister", None)
                setattr(value, "PersonRegister", self)

class Persons_PersonRegister:

    pass
class Person:

    pass
class Persons_Female(Person):

    pass
class Persons_Male(Person):

    pass