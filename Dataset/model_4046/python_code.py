from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class SuperType:

    pass
class smalluml_Type(SuperType):

    pass
class smalluml_Enumeration(SuperType):

    def __init__(self, enumeration: str):
        self.enumeration = enumeration
        
    @property
    def enumeration(self) -> str:
        return self.__enumeration

    @enumeration.setter
    def enumeration(self, enumeration: str):
        self.__enumeration = enumeration

class smalluml_Class(SuperType):

    def __init__(self, isAbstract: bool, smalluml_Class: "smalluml_Role" = None, smalluml_Class12: set["smalluml_Attribute"] = None, smalluml_Class15: set["smalluml_Operation"] = None, smalluml_Class19: "smalluml_Class" = None, smalluml_Class17: "smalluml_Class" = None):
        self.isAbstract = isAbstract
        self.smalluml_Class = smalluml_Class
        self.smalluml_Class12 = smalluml_Class12 if smalluml_Class12 is not None else set()
        self.smalluml_Class15 = smalluml_Class15 if smalluml_Class15 is not None else set()
        self.smalluml_Class19 = smalluml_Class19
        self.smalluml_Class17 = smalluml_Class17
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def smalluml_Class15(self):
        return self.__smalluml_Class15

    @smalluml_Class15.setter
    def smalluml_Class15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class15", None)
        self.__smalluml_Class15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Operation16"):
                    opp_val = getattr(item, "smalluml_Operation16", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Operation16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Operation16"):
                    opp_val = getattr(item, "smalluml_Operation16", None)
                    
                    setattr(item, "smalluml_Operation16", self)
                    

    @property
    def smalluml_Class12(self):
        return self.__smalluml_Class12

    @smalluml_Class12.setter
    def smalluml_Class12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class12", None)
        self.__smalluml_Class12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Attribute13"):
                    opp_val = getattr(item, "smalluml_Attribute13", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Attribute13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Attribute13"):
                    opp_val = getattr(item, "smalluml_Attribute13", None)
                    
                    setattr(item, "smalluml_Attribute13", self)
                    

    @property
    def smalluml_Class17(self):
        return self.__smalluml_Class17

    @smalluml_Class17.setter
    def smalluml_Class17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class17", None)
        self.__smalluml_Class17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Class19"):
                opp_val = getattr(old_value, "smalluml_Class19", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Class19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Class19"):
                opp_val = getattr(value, "smalluml_Class19", None)
                setattr(value, "smalluml_Class19", self)

    @property
    def smalluml_Class(self):
        return self.__smalluml_Class

    @smalluml_Class.setter
    def smalluml_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class", None)
        self.__smalluml_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Role"):
                opp_val = getattr(old_value, "smalluml_Role", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Role", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Role"):
                opp_val = getattr(value, "smalluml_Role", None)
                setattr(value, "smalluml_Role", self)

    @property
    def smalluml_Class19(self):
        return self.__smalluml_Class19

    @smalluml_Class19.setter
    def smalluml_Class19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class19", None)
        self.__smalluml_Class19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Class17"):
                opp_val = getattr(old_value, "smalluml_Class17", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Class17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Class17"):
                opp_val = getattr(value, "smalluml_Class17", None)
                setattr(value, "smalluml_Class17", self)

class NamedElement:

    pass
class smalluml_Parameter(NamedElement):

    pass
class smalluml_Association(NamedElement):

    pass
class smalluml_Role(NamedElement):

    def __init__(self, lowerBound: int, upperBound: int, smalluml_Role: "smalluml_Class" = None, smalluml_Role3: "smalluml_Association" = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.smalluml_Role = smalluml_Role
        self.smalluml_Role3 = smalluml_Role3
        
    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def smalluml_Role(self):
        return self.__smalluml_Role

    @smalluml_Role.setter
    def smalluml_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Role__smalluml_Role", None)
        self.__smalluml_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Class"):
                opp_val = getattr(old_value, "smalluml_Class", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Class"):
                opp_val = getattr(value, "smalluml_Class", None)
                setattr(value, "smalluml_Class", self)

    @property
    def smalluml_Role3(self):
        return self.__smalluml_Role3

    @smalluml_Role3.setter
    def smalluml_Role3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Role__smalluml_Role3", None)
        self.__smalluml_Role3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Association"):
                opp_val = getattr(old_value, "smalluml_Association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Association"):
                opp_val = getattr(value, "smalluml_Association", None)
                if opp_val is None:
                    setattr(value, "smalluml_Association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smalluml_Operation(NamedElement):

    def __init__(self, isAbstract: bool, smalluml_Operation: set["smalluml_Parameter"] = None, smalluml_Operation6: "smalluml_SuperType" = None, smalluml_Operation16: "smalluml_Class" = None):
        self.isAbstract = isAbstract
        self.smalluml_Operation = smalluml_Operation if smalluml_Operation is not None else set()
        self.smalluml_Operation6 = smalluml_Operation6
        self.smalluml_Operation16 = smalluml_Operation16
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def smalluml_Operation(self):
        return self.__smalluml_Operation

    @smalluml_Operation.setter
    def smalluml_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Operation__smalluml_Operation", None)
        self.__smalluml_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Parameter"):
                    opp_val = getattr(item, "smalluml_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Parameter"):
                    opp_val = getattr(item, "smalluml_Parameter", None)
                    
                    setattr(item, "smalluml_Parameter", self)
                    

    @property
    def smalluml_Operation16(self):
        return self.__smalluml_Operation16

    @smalluml_Operation16.setter
    def smalluml_Operation16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Operation__smalluml_Operation16", None)
        self.__smalluml_Operation16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Class15"):
                opp_val = getattr(old_value, "smalluml_Class15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Class15"):
                opp_val = getattr(value, "smalluml_Class15", None)
                if opp_val is None:
                    setattr(value, "smalluml_Class15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smalluml_Operation6(self):
        return self.__smalluml_Operation6

    @smalluml_Operation6.setter
    def smalluml_Operation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Operation__smalluml_Operation6", None)
        self.__smalluml_Operation6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_SuperType7"):
                opp_val = getattr(old_value, "smalluml_SuperType7", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_SuperType7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_SuperType7"):
                opp_val = getattr(value, "smalluml_SuperType7", None)
                setattr(value, "smalluml_SuperType7", self)

class smalluml_Attribute(NamedElement):

    pass
class smalluml_Package(NamedElement):

    pass
class smalluml_SuperType(NamedElement):

    pass
class smalluml_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
