from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Families_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Families_Member(ABC):

    def __init__(self, firstName: str, Families_Member: "Families_Family" = None, Families_Member36: "Families_City" = None):
        self.firstName = firstName
        self.Families_Member = Families_Member
        self.Families_Member36 = Families_Member36
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def Families_Member36(self):
        return self.__Families_Member36

    @Families_Member36.setter
    def Families_Member36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__Families_Member36", None)
        self.__Families_Member36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families_City37"):
                opp_val = getattr(old_value, "Families_City37", None)
                if opp_val == self:
                    setattr(old_value, "Families_City37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families_City37"):
                opp_val = getattr(value, "Families_City37", None)
                setattr(value, "Families_City37", self)

    @property
    def Families_Member(self):
        return self.__Families_Member

    @Families_Member.setter
    def Families_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__Families_Member", None)
        self.__Families_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families_Family34"):
                opp_val = getattr(old_value, "Families_Family34", None)
                if opp_val == self:
                    setattr(old_value, "Families_Family34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families_Family34"):
                opp_val = getattr(value, "Families_Family34", None)
                setattr(value, "Families_Family34", self)

class Families_Service:

    pass
class Member:

    pass
class Families_Child(Member):

    pass
class Families_Parent(Member):

    pass
class Families_Family:

    def __init__(self, lastName: str, Families_Family: "Families_Country" = None, Families_Family6: set["Families_Parent"] = None, Families_Family8: set["Families_Parent"] = None, Families_Family11: set["Families_Child"] = None, Families_Family13: set["Families_Child"] = None, contains: "Families_Neighborhood" = None, Family: "Families_Neighborhood" = None, Families_Family34: "Families_Member" = None):
        self.lastName = lastName
        self.Families_Family = Families_Family
        self.Families_Family6 = Families_Family6 if Families_Family6 is not None else set()
        self.Families_Family8 = Families_Family8 if Families_Family8 is not None else set()
        self.Families_Family11 = Families_Family11 if Families_Family11 is not None else set()
        self.Families_Family13 = Families_Family13 if Families_Family13 is not None else set()
        self.contains = contains
        self.Family = Family
        self.Families_Family34 = Families_Family34
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

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
    def contains(self):
        return self.__contains

    @contains.setter
    def contains(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__contains", None)
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
    def Families_Family6(self):
        return self.__Families_Family6

    @Families_Family6.setter
    def Families_Family6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family6", None)
        self.__Families_Family6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Families_Parent"):
                    opp_val = getattr(item, "Families_Parent", None)
                    
                    if opp_val == self:
                        setattr(item, "Families_Parent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Families_Parent"):
                    opp_val = getattr(item, "Families_Parent", None)
                    
                    setattr(item, "Families_Parent", self)
                    

    @property
    def Families_Family11(self):
        return self.__Families_Family11

    @Families_Family11.setter
    def Families_Family11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family11", None)
        self.__Families_Family11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Families_Child"):
                    opp_val = getattr(item, "Families_Child", None)
                    
                    if opp_val == self:
                        setattr(item, "Families_Child", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Families_Child"):
                    opp_val = getattr(item, "Families_Child", None)
                    
                    setattr(item, "Families_Child", self)
                    

    @property
    def Families_Family13(self):
        return self.__Families_Family13

    @Families_Family13.setter
    def Families_Family13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family13", None)
        self.__Families_Family13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Families_Child14"):
                    opp_val = getattr(item, "Families_Child14", None)
                    
                    if opp_val == self:
                        setattr(item, "Families_Child14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Families_Child14"):
                    opp_val = getattr(item, "Families_Child14", None)
                    
                    setattr(item, "Families_Child14", self)
                    

    @property
    def Families_Family8(self):
        return self.__Families_Family8

    @Families_Family8.setter
    def Families_Family8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family8", None)
        self.__Families_Family8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Families_Parent9"):
                    opp_val = getattr(item, "Families_Parent9", None)
                    
                    if opp_val == self:
                        setattr(item, "Families_Parent9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Families_Parent9"):
                    opp_val = getattr(item, "Families_Parent9", None)
                    
                    setattr(item, "Families_Parent9", self)
                    

    @property
    def Families_Family(self):
        return self.__Families_Family

    @Families_Family.setter
    def Families_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family", None)
        self.__Families_Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families_Country"):
                opp_val = getattr(old_value, "Families_Country", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families_Country"):
                opp_val = getattr(value, "Families_Country", None)
                if opp_val is None:
                    setattr(value, "Families_Country", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Families_Family34(self):
        return self.__Families_Family34

    @Families_Family34.setter
    def Families_Family34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family34", None)
        self.__Families_Family34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families_Member"):
                opp_val = getattr(old_value, "Families_Member", None)
                if opp_val == self:
                    setattr(old_value, "Families_Member", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families_Member"):
                opp_val = getattr(value, "Families_Member", None)
                setattr(value, "Families_Member", self)

class NamedElement:

    pass
class Families_City(NamedElement):

    pass
class Families_Neighborhood(NamedElement):

    pass
class Families_Company(NamedElement):

    pass
class Families_School(NamedElement):

    pass
class Families_Country(NamedElement):

    pass