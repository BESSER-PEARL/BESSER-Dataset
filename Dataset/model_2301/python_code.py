from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Gender(Enum):
    Male = "Male"
    Female = "Female"


############################################
# Definition of Classes
############################################

class Person:

    pass
class PersonList_Female(Person):

    pass
class PersonList_Male(Person):

    pass
class PersonList_WorkingPosition:

    def __init__(self, description: str, WorkingPosition7: "PersonList_WorkPlace" = None, WorkingPosition: "PersonList_Person" = None, position: "PersonList_WorkPlace" = None, works12: "PersonList_Person" = None):
        self.description = description
        self.WorkingPosition7 = WorkingPosition7
        self.WorkingPosition = WorkingPosition
        self.position = position
        self.works12 = works12
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_WorkingPosition__position", None)
        self.__position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkPlace"):
                opp_val = getattr(old_value, "WorkPlace", None)
                if opp_val == self:
                    setattr(old_value, "WorkPlace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkPlace"):
                opp_val = getattr(value, "WorkPlace", None)
                setattr(value, "WorkPlace", self)

    @property
    def WorkingPosition(self):
        return self.__WorkingPosition

    @WorkingPosition.setter
    def WorkingPosition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_WorkingPosition__WorkingPosition", None)
        self.__WorkingPosition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persons"):
                opp_val = getattr(old_value, "persons", None)
                if opp_val == self:
                    setattr(old_value, "persons", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persons"):
                opp_val = getattr(value, "persons", None)
                setattr(value, "persons", self)

    @property
    def WorkingPosition7(self):
        return self.__WorkingPosition7

    @WorkingPosition7.setter
    def WorkingPosition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_WorkingPosition__WorkingPosition7", None)
        self.__WorkingPosition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "works"):
                opp_val = getattr(old_value, "works", None)
                if opp_val == self:
                    setattr(old_value, "works", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "works"):
                opp_val = getattr(value, "works", None)
                setattr(value, "works", self)

    @property
    def works12(self):
        return self.__works12

    @works12.setter
    def works12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_WorkingPosition__works12", None)
        self.__works12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person13"):
                opp_val = getattr(old_value, "Person13", None)
                if opp_val == self:
                    setattr(old_value, "Person13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person13"):
                opp_val = getattr(value, "Person13", None)
                setattr(value, "Person13", self)

class Place:

    pass
class PersonList_WorkPlace(Place):

    pass
class PersonList_LivingPlace(Place):

    pass
class PersonList_Place(ABC):

    def __init__(self, address: str, PersonList_Place: "PersonList_List" = None):
        self.address = address
        self.PersonList_Place = PersonList_Place
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def PersonList_Place(self):
        return self.__PersonList_Place

    @PersonList_Place.setter
    def PersonList_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_Place__PersonList_Place", None)
        self.__PersonList_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PersonList_List"):
                opp_val = getattr(old_value, "PersonList_List", None)
                if opp_val == self:
                    setattr(old_value, "PersonList_List", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PersonList_List"):
                opp_val = getattr(value, "PersonList_List", None)
                setattr(value, "PersonList_List", self)

class PersonList_Person(ABC):

    def __init__(self, name: str, Person: "PersonList_List" = None, members: "PersonList_List" = None, persons5: "PersonList_LivingPlace" = None, Person9: "PersonList_LivingPlace" = None, persons: "PersonList_WorkingPosition" = None, Person13: "PersonList_WorkingPosition" = None):
        self.name = name
        self.Person = Person
        self.members = members
        self.persons5 = persons5
        self.Person9 = Person9
        self.persons = persons
        self.Person13 = Person13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Person13(self):
        return self.__Person13

    @Person13.setter
    def Person13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_Person__Person13", None)
        self.__Person13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "works12"):
                opp_val = getattr(old_value, "works12", None)
                if opp_val == self:
                    setattr(old_value, "works12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "works12"):
                opp_val = getattr(value, "works12", None)
                setattr(value, "works12", self)

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_Person__Person", None)
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
    def Person9(self):
        return self.__Person9

    @Person9.setter
    def Person9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_Person__Person9", None)
        self.__Person9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home"):
                opp_val = getattr(old_value, "home", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home"):
                opp_val = getattr(value, "home", None)
                if opp_val is None:
                    setattr(value, "home", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persons(self):
        return self.__persons

    @persons.setter
    def persons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_Person__persons", None)
        self.__persons = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkingPosition"):
                opp_val = getattr(old_value, "WorkingPosition", None)
                if opp_val == self:
                    setattr(old_value, "WorkingPosition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkingPosition"):
                opp_val = getattr(value, "WorkingPosition", None)
                setattr(value, "WorkingPosition", self)

    @property
    def persons5(self):
        return self.__persons5

    @persons5.setter
    def persons5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_Person__persons5", None)
        self.__persons5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LivingPlace"):
                opp_val = getattr(old_value, "LivingPlace", None)
                if opp_val == self:
                    setattr(old_value, "LivingPlace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LivingPlace"):
                opp_val = getattr(value, "LivingPlace", None)
                setattr(value, "LivingPlace", self)

    @property
    def members(self):
        return self.__members

    @members.setter
    def members(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_Person__members", None)
        self.__members = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "List"):
                opp_val = getattr(old_value, "List", None)
                if opp_val == self:
                    setattr(old_value, "List", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "List"):
                opp_val = getattr(value, "List", None)
                setattr(value, "List", self)

class PersonList_List:

    pass