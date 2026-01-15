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

class Families_uncertainty_aFamilyMember(ABC):

    pass
class uFamilyMember:

    pass
class uFamilyRegister:

    pass
class uncertainty_Families_FamilyRegister:

    pass
class uncertainty_UData:

    pass
class uncertainty_Families_FamilyMember:

    pass
class Families_uncertainty_aFamily(ABC):

    pass
class uFamily:

    pass
class uncertainty_Families_Family:

    pass
class Families_uncertainty_aFamilyRegister(ABC):

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
class uncertainty_aFamilyMember:

    pass
class Families_uncertainty_uFamilyMember(uncertainty_aFamilyMember, uncertainty_UData):

    pass
class aFamilyRegister:

    pass
class aFamilyMember:

    pass
class uncertainty_aFamily:

    pass
class Families_uncertainty_uFamily(uncertainty_aFamily, uncertainty_UData):

    pass
class aFamily:

    pass
class uncertainty_aFamilyRegister:

    pass
class Families_uncertainty_uFamilyRegister(uncertainty_UData, uncertainty_aFamilyRegister):

    pass
class uncertainty_ModelElement:

    pass
class Families_Family(uncertainty_aFamily, uncertainty_ModelElement):

    def __init__(self, name: str, Families_Family: "aFamilyMember" = None, Families_Family9: set["aFamilyMember"] = None, Families_Family12: "aFamilyRegister" = None, Families_Family3: "aFamilyMember" = None, Families_Family6: set["aFamilyMember"] = None):
        self.name = name
        self.Families_Family = Families_Family
        self.Families_Family9 = Families_Family9 if Families_Family9 is not None else set()
        self.Families_Family12 = Families_Family12
        self.Families_Family3 = Families_Family3
        self.Families_Family6 = Families_Family6 if Families_Family6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Families_Family12(self):
        return self.__Families_Family12

    @Families_Family12.setter
    def Families_Family12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family12", None)
        self.__Families_Family12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aFamilyRegister"):
                opp_val = getattr(old_value, "aFamilyRegister", None)
                if opp_val == self:
                    setattr(old_value, "aFamilyRegister", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aFamilyRegister"):
                opp_val = getattr(value, "aFamilyRegister", None)
                setattr(value, "aFamilyRegister", self)

    @property
    def Families_Family9(self):
        return self.__Families_Family9

    @Families_Family9.setter
    def Families_Family9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family9", None)
        self.__Families_Family9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aFamilyMember10"):
                    opp_val = getattr(item, "aFamilyMember10", None)
                    
                    if opp_val == self:
                        setattr(item, "aFamilyMember10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aFamilyMember10"):
                    opp_val = getattr(item, "aFamilyMember10", None)
                    
                    setattr(item, "aFamilyMember10", self)
                    

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
                if hasattr(item, "aFamilyMember7"):
                    opp_val = getattr(item, "aFamilyMember7", None)
                    
                    if opp_val == self:
                        setattr(item, "aFamilyMember7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aFamilyMember7"):
                    opp_val = getattr(item, "aFamilyMember7", None)
                    
                    setattr(item, "aFamilyMember7", self)
                    

    @property
    def Families_Family3(self):
        return self.__Families_Family3

    @Families_Family3.setter
    def Families_Family3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family3", None)
        self.__Families_Family3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aFamilyMember4"):
                opp_val = getattr(old_value, "aFamilyMember4", None)
                if opp_val == self:
                    setattr(old_value, "aFamilyMember4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aFamilyMember4"):
                opp_val = getattr(value, "aFamilyMember4", None)
                setattr(value, "aFamilyMember4", self)

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
            if hasattr(old_value, "aFamilyMember"):
                opp_val = getattr(old_value, "aFamilyMember", None)
                if opp_val == self:
                    setattr(old_value, "aFamilyMember", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aFamilyMember"):
                opp_val = getattr(value, "aFamilyMember", None)
                setattr(value, "aFamilyMember", self)

class Families_FamilyMember(uncertainty_aFamilyMember, uncertainty_ModelElement):

    def __init__(self, name: str, Families_FamilyMember: "aFamily" = None, Families_FamilyMember16: "aFamily" = None, Families_FamilyMember19: "aFamily" = None, Families_FamilyMember22: "aFamily" = None):
        self.name = name
        self.Families_FamilyMember = Families_FamilyMember
        self.Families_FamilyMember16 = Families_FamilyMember16
        self.Families_FamilyMember19 = Families_FamilyMember19
        self.Families_FamilyMember22 = Families_FamilyMember22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Families_FamilyMember19(self):
        return self.__Families_FamilyMember19

    @Families_FamilyMember19.setter
    def Families_FamilyMember19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_FamilyMember__Families_FamilyMember19", None)
        self.__Families_FamilyMember19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aFamily20"):
                opp_val = getattr(old_value, "aFamily20", None)
                if opp_val == self:
                    setattr(old_value, "aFamily20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aFamily20"):
                opp_val = getattr(value, "aFamily20", None)
                setattr(value, "aFamily20", self)

    @property
    def Families_FamilyMember16(self):
        return self.__Families_FamilyMember16

    @Families_FamilyMember16.setter
    def Families_FamilyMember16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_FamilyMember__Families_FamilyMember16", None)
        self.__Families_FamilyMember16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aFamily17"):
                opp_val = getattr(old_value, "aFamily17", None)
                if opp_val == self:
                    setattr(old_value, "aFamily17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aFamily17"):
                opp_val = getattr(value, "aFamily17", None)
                setattr(value, "aFamily17", self)

    @property
    def Families_FamilyMember(self):
        return self.__Families_FamilyMember

    @Families_FamilyMember.setter
    def Families_FamilyMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_FamilyMember__Families_FamilyMember", None)
        self.__Families_FamilyMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aFamily14"):
                opp_val = getattr(old_value, "aFamily14", None)
                if opp_val == self:
                    setattr(old_value, "aFamily14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aFamily14"):
                opp_val = getattr(value, "aFamily14", None)
                setattr(value, "aFamily14", self)

    @property
    def Families_FamilyMember22(self):
        return self.__Families_FamilyMember22

    @Families_FamilyMember22.setter
    def Families_FamilyMember22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_FamilyMember__Families_FamilyMember22", None)
        self.__Families_FamilyMember22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aFamily23"):
                opp_val = getattr(old_value, "aFamily23", None)
                if opp_val == self:
                    setattr(old_value, "aFamily23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aFamily23"):
                opp_val = getattr(value, "aFamily23", None)
                setattr(value, "aFamily23", self)

class Families_FamilyRegister(uncertainty_aFamilyRegister, uncertainty_ModelElement):

    pass