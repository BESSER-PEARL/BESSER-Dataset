from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class families_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class families_Member(ABC):

    def __init__(self, firstName: str, families_Member: "families_Family" = None, families_Member36: "families_City" = None):
        self.firstName = firstName
        self.families_Member = families_Member
        self.families_Member36 = families_Member36
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def families_Member36(self):
        return self.__families_Member36

    @families_Member36.setter
    def families_Member36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__families_Member36", None)
        self.__families_Member36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "families_City37"):
                opp_val = getattr(old_value, "families_City37", None)
                if opp_val == self:
                    setattr(old_value, "families_City37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "families_City37"):
                opp_val = getattr(value, "families_City37", None)
                setattr(value, "families_City37", self)

    @property
    def families_Member(self):
        return self.__families_Member

    @families_Member.setter
    def families_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Member__families_Member", None)
        self.__families_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "families_Family34"):
                opp_val = getattr(old_value, "families_Family34", None)
                if opp_val == self:
                    setattr(old_value, "families_Family34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "families_Family34"):
                opp_val = getattr(value, "families_Family34", None)
                setattr(value, "families_Family34", self)

class Member:

    pass
class families_Service:

    pass
class families_Family:

    def __init__(self, lastName: str, families_Family6: set["families_Parent"] = None, families_Family8: set["families_Parent"] = None, families_Family11: set["families_Child"] = None, families_Family: "families_Country" = None, families_Family13: set["families_Child"] = None, contains: "families_Neighborhood" = None, Family: "families_Neighborhood" = None, families_Family34: "families_Member" = None):
        self.lastName = lastName
        self.families_Family6 = families_Family6 if families_Family6 is not None else set()
        self.families_Family8 = families_Family8 if families_Family8 is not None else set()
        self.families_Family11 = families_Family11 if families_Family11 is not None else set()
        self.families_Family = families_Family
        self.families_Family13 = families_Family13 if families_Family13 is not None else set()
        self.contains = contains
        self.Family = Family
        self.families_Family34 = families_Family34
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def families_Family11(self):
        return self.__families_Family11

    @families_Family11.setter
    def families_Family11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__families_Family11", None)
        self.__families_Family11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "families_Child"):
                    opp_val = getattr(item, "families_Child", None)
                    
                    if opp_val == self:
                        setattr(item, "families_Child", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "families_Child"):
                    opp_val = getattr(item, "families_Child", None)
                    
                    setattr(item, "families_Child", self)
                    

    @property
    def Family(self):
        return self.__Family

    @Family.setter
    def Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__Family", None)
        self.__Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registeredIn"):
                opp_val = getattr(old_value, "registeredIn", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registeredIn"):
                opp_val = getattr(value, "registeredIn", None)
                if opp_val is None:
                    setattr(value, "registeredIn", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def families_Family(self):
        return self.__families_Family

    @families_Family.setter
    def families_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__families_Family", None)
        self.__families_Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "families_Country"):
                opp_val = getattr(old_value, "families_Country", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "families_Country"):
                opp_val = getattr(value, "families_Country", None)
                if opp_val is None:
                    setattr(value, "families_Country", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def families_Family34(self):
        return self.__families_Family34

    @families_Family34.setter
    def families_Family34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__families_Family34", None)
        self.__families_Family34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "families_Member"):
                opp_val = getattr(old_value, "families_Member", None)
                if opp_val == self:
                    setattr(old_value, "families_Member", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "families_Member"):
                opp_val = getattr(value, "families_Member", None)
                setattr(value, "families_Member", self)

    @property
    def contains(self):
        return self.__contains

    @contains.setter
    def contains(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__contains", None)
        self.__contains = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Neighborhood"):
                opp_val = getattr(old_value, "Neighborhood", None)
                if opp_val == self:
                    setattr(old_value, "Neighborhood", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Neighborhood"):
                opp_val = getattr(value, "Neighborhood", None)
                setattr(value, "Neighborhood", self)

    @property
    def families_Family6(self):
        return self.__families_Family6

    @families_Family6.setter
    def families_Family6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__families_Family6", None)
        self.__families_Family6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "families_Parent"):
                    opp_val = getattr(item, "families_Parent", None)
                    
                    if opp_val == self:
                        setattr(item, "families_Parent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "families_Parent"):
                    opp_val = getattr(item, "families_Parent", None)
                    
                    setattr(item, "families_Parent", self)
                    

    @property
    def families_Family8(self):
        return self.__families_Family8

    @families_Family8.setter
    def families_Family8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__families_Family8", None)
        self.__families_Family8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "families_Parent9"):
                    opp_val = getattr(item, "families_Parent9", None)
                    
                    if opp_val == self:
                        setattr(item, "families_Parent9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "families_Parent9"):
                    opp_val = getattr(item, "families_Parent9", None)
                    
                    setattr(item, "families_Parent9", self)
                    

    @property
    def families_Family13(self):
        return self.__families_Family13

    @families_Family13.setter
    def families_Family13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__families_Family13", None)
        self.__families_Family13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "families_Child14"):
                    opp_val = getattr(item, "families_Child14", None)
                    
                    if opp_val == self:
                        setattr(item, "families_Child14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "families_Child14"):
                    opp_val = getattr(item, "families_Child14", None)
                    
                    setattr(item, "families_Child14", self)
                    

class NamedElement:

    pass
class families_School(NamedElement):

    pass
class families_Neighborhood(NamedElement):

    pass
class families_Country(NamedElement):

    pass
class families_Child(Member):

    pass
class families_Parent(Member):

    pass
class families_Company(NamedElement):

    pass
class families_City(NamedElement):

    pass