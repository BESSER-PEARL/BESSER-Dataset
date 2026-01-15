from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Member:

    pass
class Families_Female(Member):

    pass
class Families_Male(Member):

    pass
class Families_Member(ABC):

    def __init__(self, firstname: str, Member: "Families_Family" = None, members: "Families_Family" = None):
        self.firstname = firstname
        self.Member = Member
        self.members = members
        
    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def members(self):
        return self.__members

    @members.setter
    def members(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__members", None)
        self.__members = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family4"):
                opp_val = getattr(old_value, "Family4", None)
                if opp_val == self:
                    setattr(old_value, "Family4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family4"):
                opp_val = getattr(value, "Family4", None)
                setattr(value, "Family4", self)

    @property
    def Member(self):
        return self.__Member

    @Member.setter
    def Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__Member", None)
        self.__Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family"):
                opp_val = getattr(old_value, "family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family"):
                opp_val = getattr(value, "family", None)
                if opp_val is None:
                    setattr(value, "family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Families_Family:

    def __init__(self, lastname: str, family: set["Families_Member"] = None, Family: "Families_Families" = None, families: "Families_Families" = None, Family4: "Families_Member" = None):
        self.lastname = lastname
        self.family = family if family is not None else set()
        self.Family = Family
        self.families = families
        self.Family4 = Family4
        
    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__family", None)
        self.__family = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Member"):
                    opp_val = getattr(item, "Member", None)
                    
                    if opp_val == self:
                        setattr(item, "Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Member"):
                    opp_val = getattr(item, "Member", None)
                    
                    setattr(item, "Member", self)
                    

    @property
    def families(self):
        return self.__families

    @families.setter
    def families(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__families", None)
        self.__families = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families"):
                opp_val = getattr(old_value, "Families", None)
                if opp_val == self:
                    setattr(old_value, "Families", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families"):
                opp_val = getattr(value, "Families", None)
                setattr(value, "Families", self)

    @property
    def Family(self):
        return self.__Family

    @Family.setter
    def Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Family", None)
        self.__Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container"):
                opp_val = getattr(old_value, "container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container"):
                opp_val = getattr(value, "container", None)
                if opp_val is None:
                    setattr(value, "container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Family4(self):
        return self.__Family4

    @Family4.setter
    def Family4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Family4", None)
        self.__Family4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "members"):
                opp_val = getattr(old_value, "members", None)
                if opp_val == self:
                    setattr(old_value, "members", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "members"):
                opp_val = getattr(value, "members", None)
                setattr(value, "members", self)

class Families_Families:

    pass