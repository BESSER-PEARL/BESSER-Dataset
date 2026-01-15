from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Person:

    pass
class SimplePersons_Female(Person):

    pass
class SimplePersons_Male(Person):

    pass
class SimplePersons_PersonRegister:

    pass
class SimplePersons_Person(ABC):

    def __init__(self, name: str, SimplePersons_Person: "SimplePersons_PersonRegister" = None):
        self.name = name
        self.SimplePersons_Person = SimplePersons_Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SimplePersons_Person(self):
        return self.__SimplePersons_Person

    @SimplePersons_Person.setter
    def SimplePersons_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePersons_Person__SimplePersons_Person", None)
        self.__SimplePersons_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplePersons_PersonRegister"):
                opp_val = getattr(old_value, "SimplePersons_PersonRegister", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplePersons_PersonRegister"):
                opp_val = getattr(value, "SimplePersons_PersonRegister", None)
                if opp_val is None:
                    setattr(value, "SimplePersons_PersonRegister", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
