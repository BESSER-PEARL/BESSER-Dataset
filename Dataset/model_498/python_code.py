from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Families_LastNameElement(ABC):

    def __init__(self, lastName: str):
        self.lastName = lastName
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

class Family:

    pass
class Member:

    pass
class LastNameElement:

    pass
class Families_Member(LastNameElement):

    def __init__(self, firstName: str, 011: "Family" = None, 014: "Family" = None, 017: "Family" = None, 020: "Family" = None):
        self.firstName = firstName
        self.011 = 011
        self.014 = 014
        self.017 = 017
        self.020 = 020
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def 017(self):
        return self.__017

    @017.setter
    def 017(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__017", None)
        self.__017 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#18"):
                opp_val = getattr(old_value, "#18", None)
                if opp_val == self:
                    setattr(old_value, "#18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#18"):
                opp_val = getattr(value, "#18", None)
                setattr(value, "#18", self)

    @property
    def 011(self):
        return self.__011

    @011.setter
    def 011(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__011", None)
        self.__011 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#12"):
                opp_val = getattr(old_value, "#12", None)
                if opp_val == self:
                    setattr(old_value, "#12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#12"):
                opp_val = getattr(value, "#12", None)
                setattr(value, "#12", self)

    @property
    def 014(self):
        return self.__014

    @014.setter
    def 014(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__014", None)
        self.__014 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#15"):
                opp_val = getattr(old_value, "#15", None)
                if opp_val == self:
                    setattr(old_value, "#15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#15"):
                opp_val = getattr(value, "#15", None)
                setattr(value, "#15", self)

    @property
    def 020(self):
        return self.__020

    @020.setter
    def 020(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__020", None)
        self.__020 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#21"):
                opp_val = getattr(old_value, "#21", None)
                if opp_val == self:
                    setattr(old_value, "#21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#21"):
                opp_val = getattr(value, "#21", None)
                setattr(value, "#21", self)

class Families_Family(LastNameElement):

    pass