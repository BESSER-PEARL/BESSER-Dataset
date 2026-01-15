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
class uFamily:

    pass
class uncertainty_Families_FamilyRegistry:

    pass
class Families_uncertainty_aMember(ABC):

    pass
class uMember:

    pass
class uncertainty_Families_Member:

    pass
class Families_uncertainty_aFamily(ABC):

    pass
class uncertainty_Families_Family:

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
class uncertainty_aMember:

    pass
class Families_uncertainty_uMember(uncertainty_UData, uncertainty_aMember):

    pass
class uncertainty_aFamilyRegistry:

    pass
class Families_uncertainty_uFamilyRegistry(uncertainty_aFamilyRegistry, uncertainty_UData):

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
class Families_FamilyRegistry(uncertainty_aFamilyRegistry, uncertainty_ModelElement):

    pass
class Families_Member(uncertainty_aMember, uncertainty_ModelElement):

    def __init__(self, firstName: str, age: int, Families_Member: "aFamily" = None):
        self.firstName = firstName
        self.age = age
        self.Families_Member = Families_Member
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

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
            if hasattr(old_value, "aFamily"):
                opp_val = getattr(old_value, "aFamily", None)
                if opp_val == self:
                    setattr(old_value, "aFamily", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aFamily"):
                opp_val = getattr(value, "aFamily", None)
                setattr(value, "aFamily", self)

class Families_Family(uncertainty_aFamily, uncertainty_ModelElement):

    def __init__(self, lastName: str, address: str, Families_Family2: "aMember" = None, Families_Family5: "aMember" = None, Families_Family: set["aMember"] = None):
        self.lastName = lastName
        self.address = address
        self.Families_Family2 = Families_Family2
        self.Families_Family5 = Families_Family5
        self.Families_Family = Families_Family if Families_Family is not None else set()
        
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
    def Families_Family2(self):
        return self.__Families_Family2

    @Families_Family2.setter
    def Families_Family2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family2", None)
        self.__Families_Family2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aMember3"):
                opp_val = getattr(old_value, "aMember3", None)
                if opp_val == self:
                    setattr(old_value, "aMember3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aMember3"):
                opp_val = getattr(value, "aMember3", None)
                setattr(value, "aMember3", self)

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
                    
