from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class persons_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Facility:

    pass
class persons_OrdinaryFacility(Facility):

    pass
class persons_SpecialFacility(Facility):

    pass
class persons_Person(ABC):

    def __init__(self, fullName: str, persons_Person7: "persons_TownHall" = None, persons_Person: "persons_Community" = None, persons_Person19: "persons_Facility" = None):
        self.fullName = fullName
        self.persons_Person7 = persons_Person7
        self.persons_Person = persons_Person
        self.persons_Person19 = persons_Person19
        
    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def persons_Person19(self):
        return self.__persons_Person19

    @persons_Person19.setter
    def persons_Person19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persons_Person__persons_Person19", None)
        self.__persons_Person19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persons_Facility18"):
                opp_val = getattr(old_value, "persons_Facility18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persons_Facility18"):
                opp_val = getattr(value, "persons_Facility18", None)
                if opp_val is None:
                    setattr(value, "persons_Facility18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persons_Person(self):
        return self.__persons_Person

    @persons_Person.setter
    def persons_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persons_Person__persons_Person", None)
        self.__persons_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persons_Community"):
                opp_val = getattr(old_value, "persons_Community", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persons_Community"):
                opp_val = getattr(value, "persons_Community", None)
                if opp_val is None:
                    setattr(value, "persons_Community", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persons_Person7(self):
        return self.__persons_Person7

    @persons_Person7.setter
    def persons_Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persons_Person__persons_Person7", None)
        self.__persons_Person7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persons_TownHall6"):
                opp_val = getattr(old_value, "persons_TownHall6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persons_TownHall6"):
                opp_val = getattr(value, "persons_TownHall6", None)
                if opp_val is None:
                    setattr(value, "persons_TownHall6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class persons_Community:

    pass
class NamedElement:

    pass
class persons_TownHall(NamedElement):

    pass
class persons_Committee(NamedElement):

    pass
class persons_Facility(NamedElement):

    pass
class persons_District(NamedElement):

    pass
class Person:

    pass
class persons_Woman(Person):

    pass
class persons_Man(Person):

    pass
class persons_Association(NamedElement):

    pass