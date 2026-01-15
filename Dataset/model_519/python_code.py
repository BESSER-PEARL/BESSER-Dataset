from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class OperatorType(Enum):
    XOR = "XOR"
    AND = "AND"
    OR = "OR"


############################################
# Definition of Classes
############################################

class Families_uncertainty_aFamilyRegistry(ABC):

    pass
class uFamilyRegistry:

    pass
class aFamilyRegistry:

    pass
class Families_uncertainty_aMember(ABC):

    pass
class uMember:

    pass
class Families_uncertainty_aFamily(ABC):

    pass
class uFamily:

    pass
class uncertainty_UData:

    pass
class Families_uncertainty_UData(ABC):

    def __init__(self, name: str, utype: str):
        self.name = name
        self.utype = utype
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def utype(self) -> str:
        return self.__utype

    @utype.setter
    def utype(self, utype: str):
        self.__utype = utype

class ModelElement:

    pass
class Families_uncertainty_ModelElement(ABC):

    pass
class uncertainty_aFamilyRegistry:

    pass
class Families_uncertainty_uFamilyRegistry(uncertainty_UData, uncertainty_aFamilyRegistry):

    pass
class uncertainty_aMember:

    pass
class Families_uncertainty_uMember(uncertainty_UData, uncertainty_aMember):

    pass
class aFamily:

    pass
class aMember:

    pass
class uncertainty_aFamily:

    pass
class Families_uncertainty_uFamily(uncertainty_UData, uncertainty_aFamily):

    pass
class uncertainty_ModelElement:

    pass
class Families_Member(uncertainty_ModelElement, uncertainty_aMember):

    def __init__(self, firstName: str, age: int, Families_Member: "aMember" = None):
        self.firstName = firstName
        self.age = age
        self.Families_Member = Families_Member
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

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
            if hasattr(old_value, "aMember13"):
                opp_val = getattr(old_value, "aMember13", None)
                if opp_val == self:
                    setattr(old_value, "aMember13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aMember13"):
                opp_val = getattr(value, "aMember13", None)
                setattr(value, "aMember13", self)

class Families_FamilyRegistry(uncertainty_ModelElement, uncertainty_aFamilyRegistry):

    pass
class Families_Family(uncertainty_ModelElement, uncertainty_aFamily):

    def __init__(self, lastName: str, address: str, Families_Family: set["aMember"] = None, Families_Family2: set["aMember"] = None, Families_Family5: "aMember" = None, Families_Family8: "aMember" = None, Families_Family11: set["aFamily"] = None):
        self.lastName = lastName
        self.address = address
        self.Families_Family = Families_Family if Families_Family is not None else set()
        self.Families_Family2 = Families_Family2 if Families_Family2 is not None else set()
        self.Families_Family5 = Families_Family5
        self.Families_Family8 = Families_Family8
        self.Families_Family11 = Families_Family11 if Families_Family11 is not None else set()
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

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
                if hasattr(item, "aFamily"):
                    opp_val = getattr(item, "aFamily", None)
                    
                    if opp_val == self:
                        setattr(item, "aFamily", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aFamily"):
                    opp_val = getattr(item, "aFamily", None)
                    
                    setattr(item, "aFamily", self)
                    

    @property
    def Families_Family5(self):
        return self.__Families_Family5

    @Families_Family5.setter
    def Families_Family5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family5", None)
        self.__Families_Family5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aMember6"):
                opp_val = getattr(old_value, "aMember6", None)
                if opp_val == self:
                    setattr(old_value, "aMember6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aMember6"):
                opp_val = getattr(value, "aMember6", None)
                setattr(value, "aMember6", self)

    @property
    def Families_Family(self):
        return self.__Families_Family

    @Families_Family.setter
    def Families_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family", None)
        self.__Families_Family = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aMember"):
                    opp_val = getattr(item, "aMember", None)
                    
                    if opp_val == self:
                        setattr(item, "aMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aMember"):
                    opp_val = getattr(item, "aMember", None)
                    
                    setattr(item, "aMember", self)
                    

    @property
    def Families_Family2(self):
        return self.__Families_Family2

    @Families_Family2.setter
    def Families_Family2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family2", None)
        self.__Families_Family2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aMember3"):
                    opp_val = getattr(item, "aMember3", None)
                    
                    if opp_val == self:
                        setattr(item, "aMember3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aMember3"):
                    opp_val = getattr(item, "aMember3", None)
                    
                    setattr(item, "aMember3", self)
                    

    @property
    def Families_Family8(self):
        return self.__Families_Family8

    @Families_Family8.setter
    def Families_Family8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family8", None)
        self.__Families_Family8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aMember9"):
                opp_val = getattr(old_value, "aMember9", None)
                if opp_val == self:
                    setattr(old_value, "aMember9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aMember9"):
                opp_val = getattr(value, "aMember9", None)
                setattr(value, "aMember9", self)
