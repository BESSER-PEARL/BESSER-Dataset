from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Visibility(Enum):
    private = "private"
    protected = "protected"
    public = "public"
class PrimitiveTypes(Enum):
    int = "int"
    bool = "bool"
    string = "string"
    double = "double"


############################################
# Definition of Classes
############################################

class Object:

    pass
class psample_Type(Object):

    pass
class Member:

    pass
class psample_Variable(Member):

    pass
class psample_Function(Member):

    pass
class Type:

    pass
class psample_PrimitiveTypeVariable(Type):

    pass
class psample_Member(Type):

    pass
class TypedElement:

    pass
class psample_Interface(TypedElement):

    pass
class psample_Class(TypedElement):

    pass
class psample_Object(ABC):

    def __init__(self, Name: str):
        self.Name = Name
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

class psample_TypedElement(Object):

    pass
class psample_Package:

    def __init__(self, Name: str, psample_Package: set["psample_TypedElement"] = None):
        self.Name = Name
        self.psample_Package = psample_Package if psample_Package is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def psample_Package(self):
        return self.__psample_Package

    @psample_Package.setter
    def psample_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_psample_Package__psample_Package", None)
        self.__psample_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "psample_TypedElement"):
                    opp_val = getattr(item, "psample_TypedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "psample_TypedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "psample_TypedElement"):
                    opp_val = getattr(item, "psample_TypedElement", None)
                    
                    setattr(item, "psample_TypedElement", self)
                    
