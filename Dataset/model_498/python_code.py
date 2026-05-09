from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Families_LastNameElement(ABC):

    def __init__(self, lastName: str):
        self.lastName = lastName
        
        pass
    @property
    def lastName(self):
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

    def __init__(self, firstName: str, father: "Family" = None, mother: "Family" = None, sons: "Family" = None, daughters: "Family" = None):
        self.firstName = firstName
        self.father = father
        self.mother = mother
        self.sons = sons
        self.daughters = daughters
        
        pass
    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


    @property
    def sons(self):
        return self.__sons

    @sons.setter
    def sons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__sons", None)
        self.__sons = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family11"):
                opp_val = getattr(old_value, "Family11", None)
                if opp_val == self:
                    setattr(old_value, "Family11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family11"):
                opp_val = getattr(value, "Family11", None)
                setattr(value, "Family11", self)

    @property
    def mother(self):
        return self.__mother

    @mother.setter
    def mother(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__mother", None)
        self.__mother = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family9"):
                opp_val = getattr(old_value, "Family9", None)
                if opp_val == self:
                    setattr(old_value, "Family9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family9"):
                opp_val = getattr(value, "Family9", None)
                setattr(value, "Family9", self)

    @property
    def father(self):
        return self.__father

    @father.setter
    def father(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__father", None)
        self.__father = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family"):
                opp_val = getattr(old_value, "Family", None)
                if opp_val == self:
                    setattr(old_value, "Family", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family"):
                opp_val = getattr(value, "Family", None)
                setattr(value, "Family", self)

    @property
    def daughters(self):
        return self.__daughters

    @daughters.setter
    def daughters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__daughters", None)
        self.__daughters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family13"):
                opp_val = getattr(old_value, "Family13", None)
                if opp_val == self:
                    setattr(old_value, "Family13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family13"):
                opp_val = getattr(value, "Family13", None)
                setattr(value, "Family13", self)

class Families_Family(LastNameElement):

    pass