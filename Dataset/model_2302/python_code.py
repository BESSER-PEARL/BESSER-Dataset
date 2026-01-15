from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Families2Persons_Member:

    pass
class Families2Persons_MemberToPerson(ABC):

    def __init__(self, firstName: str, familyName: str, Families2Persons_MemberToPerson: "Families2Persons_Member" = None, Families2Persons_MemberToPerson2: "Families2Persons_Person" = None):
        self.firstName = firstName
        self.familyName = familyName
        self.Families2Persons_MemberToPerson = Families2Persons_MemberToPerson
        self.Families2Persons_MemberToPerson2 = Families2Persons_MemberToPerson2
        
    @property
    def familyName(self) -> str:
        return self.__familyName

    @familyName.setter
    def familyName(self, familyName: str):
        self.__familyName = familyName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def Families2Persons_MemberToPerson2(self):
        return self.__Families2Persons_MemberToPerson2

    @Families2Persons_MemberToPerson2.setter
    def Families2Persons_MemberToPerson2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families2Persons_MemberToPerson__Families2Persons_MemberToPerson2", None)
        self.__Families2Persons_MemberToPerson2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families2Persons_Person"):
                opp_val = getattr(old_value, "Families2Persons_Person", None)
                if opp_val == self:
                    setattr(old_value, "Families2Persons_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families2Persons_Person"):
                opp_val = getattr(value, "Families2Persons_Person", None)
                setattr(value, "Families2Persons_Person", self)

    @property
    def Families2Persons_MemberToPerson(self):
        return self.__Families2Persons_MemberToPerson

    @Families2Persons_MemberToPerson.setter
    def Families2Persons_MemberToPerson(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families2Persons_MemberToPerson__Families2Persons_MemberToPerson", None)
        self.__Families2Persons_MemberToPerson = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families2Persons_Member"):
                opp_val = getattr(old_value, "Families2Persons_Member", None)
                if opp_val == self:
                    setattr(old_value, "Families2Persons_Member", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families2Persons_Member"):
                opp_val = getattr(value, "Families2Persons_Member", None)
                setattr(value, "Families2Persons_Member", self)

class MemberToPerson:

    pass
class Families2Persons_Member2Female(MemberToPerson):

    pass
class Families2Persons_Member2Male(MemberToPerson):

    pass
class Families2Persons_Person:

    pass