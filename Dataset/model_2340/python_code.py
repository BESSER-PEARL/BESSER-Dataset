from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Facility:

    pass
class Persons_SpecialFacility(Facility):

    pass
class Persons_OrdinaryFacility(Facility):

    pass
class Persons_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class Persons_Committee(NamedElement):

    pass
class Persons_Facility(NamedElement):

    pass
class Persons_District(NamedElement):

    pass
class Persons_Association(NamedElement):

    pass
class Persons_TownHall(NamedElement):

    pass
class Person:

    pass
class Persons_Woman(Person):

    pass
class Persons_Man(Person):

    pass
class Persons_Community:

    pass
class Persons_Person(ABC):

    def __init__(self, fullName: str, Persons_Person: "Persons_Community" = None, Persons_Person7: "Persons_TownHall" = None, Persons_Person19: "Persons_Facility" = None):
        self.fullName = fullName
        self.Persons_Person = Persons_Person
        self.Persons_Person7 = Persons_Person7
        self.Persons_Person19 = Persons_Person19
        
    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def Persons_Person7(self):
        return self.__Persons_Person7

    @Persons_Person7.setter
    def Persons_Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Persons_Person__Persons_Person7", None)
        self.__Persons_Person7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Persons_TownHall6"):
                opp_val = getattr(old_value, "Persons_TownHall6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Persons_TownHall6"):
                opp_val = getattr(value, "Persons_TownHall6", None)
                if opp_val is None:
                    setattr(value, "Persons_TownHall6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Persons_Person19(self):
        return self.__Persons_Person19

    @Persons_Person19.setter
    def Persons_Person19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Persons_Person__Persons_Person19", None)
        self.__Persons_Person19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Persons_Facility18"):
                opp_val = getattr(old_value, "Persons_Facility18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Persons_Facility18"):
                opp_val = getattr(value, "Persons_Facility18", None)
                if opp_val is None:
                    setattr(value, "Persons_Facility18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "Persons_Community"):
                opp_val = getattr(old_value, "Persons_Community", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Persons_Community"):
                opp_val = getattr(value, "Persons_Community", None)
                if opp_val is None:
                    setattr(value, "Persons_Community", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
