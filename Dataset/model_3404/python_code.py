from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Gender(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    UNSPECIFIED = "UNSPECIFIED"


############################################
# Definition of Classes
############################################

class menus_PersonDirectory:

    pass
class menus_Person:

    def __init__(self, firstname: str, lastname: str, sex: str, pregnant: bool, dateOfBirth: date, menus_Person: "menus_Person" = None, menus_Person0: "menus_Person" = None, menus_Person3: "menus_PersonDirectory" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.sex = sex
        self.pregnant = pregnant
        self.dateOfBirth = dateOfBirth
        self.menus_Person = menus_Person
        self.menus_Person0 = menus_Person0
        self.menus_Person3 = menus_Person3
        
    @property
    def sex(self) -> str:
        return self.__sex

    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex

    @property
    def pregnant(self) -> bool:
        return self.__pregnant

    @pregnant.setter
    def pregnant(self, pregnant: bool):
        self.__pregnant = pregnant

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def dateOfBirth(self) -> date:
        return self.__dateOfBirth

    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def menus_Person3(self):
        return self.__menus_Person3

    @menus_Person3.setter
    def menus_Person3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_menus_Person__menus_Person3", None)
        self.__menus_Person3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menus_PersonDirectory"):
                opp_val = getattr(old_value, "menus_PersonDirectory", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menus_PersonDirectory"):
                opp_val = getattr(value, "menus_PersonDirectory", None)
                if opp_val is None:
                    setattr(value, "menus_PersonDirectory", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def menus_Person(self):
        return self.__menus_Person

    @menus_Person.setter
    def menus_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_menus_Person__menus_Person", None)
        self.__menus_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menus_Person0"):
                opp_val = getattr(old_value, "menus_Person0", None)
                if opp_val == self:
                    setattr(old_value, "menus_Person0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menus_Person0"):
                opp_val = getattr(value, "menus_Person0", None)
                setattr(value, "menus_Person0", self)

    @property
    def menus_Person0(self):
        return self.__menus_Person0

    @menus_Person0.setter
    def menus_Person0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_menus_Person__menus_Person0", None)
        self.__menus_Person0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menus_Person"):
                opp_val = getattr(old_value, "menus_Person", None)
                if opp_val == self:
                    setattr(old_value, "menus_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menus_Person"):
                opp_val = getattr(value, "menus_Person", None)
                setattr(value, "menus_Person", self)
