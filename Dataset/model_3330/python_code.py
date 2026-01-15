from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveTypes(Enum):
    int = "int"
    bool = "bool"
    string = "string"
    double = "double"
class Visibility(Enum):
    private = "private"
    protected = "protected"
    public = "public"


############################################
# Definition of Classes
############################################

class Object:

    pass
class psample_Type(Object):

    pass
class Type:

    pass
class psample_PrimitiveTypeVariable(Type):

    def __init__(self, isParameter: bool, psample_PrimitiveTypeVariable5: "psample_Function" = None, psample_PrimitiveTypeVariable: "psample_Class" = None):
        self.isParameter = isParameter
        self.psample_PrimitiveTypeVariable5 = psample_PrimitiveTypeVariable5
        self.psample_PrimitiveTypeVariable = psample_PrimitiveTypeVariable
        
    @property
    def isParameter(self) -> bool:
        return self.__isParameter

    @isParameter.setter
    def isParameter(self, isParameter: bool):
        self.__isParameter = isParameter

    @property
    def psample_PrimitiveTypeVariable(self):
        return self.__psample_PrimitiveTypeVariable

    @psample_PrimitiveTypeVariable.setter
    def psample_PrimitiveTypeVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_psample_PrimitiveTypeVariable__psample_PrimitiveTypeVariable", None)
        self.__psample_PrimitiveTypeVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "psample_Class3"):
                opp_val = getattr(old_value, "psample_Class3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "psample_Class3"):
                opp_val = getattr(value, "psample_Class3", None)
                if opp_val is None:
                    setattr(value, "psample_Class3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def psample_PrimitiveTypeVariable5(self):
        return self.__psample_PrimitiveTypeVariable5

    @psample_PrimitiveTypeVariable5.setter
    def psample_PrimitiveTypeVariable5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_psample_PrimitiveTypeVariable__psample_PrimitiveTypeVariable5", None)
        self.__psample_PrimitiveTypeVariable5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "psample_Function"):
                opp_val = getattr(old_value, "psample_Function", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "psample_Function"):
                opp_val = getattr(value, "psample_Function", None)
                if opp_val is None:
                    setattr(value, "psample_Function", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class psample_Member(Type):

    pass
class TypedElement:

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
class Member:

    pass
class psample_Variable(Member):

    def __init__(self, isParameter: bool, psample_Variable: "psample_Function" = None):
        self.isParameter = isParameter
        self.psample_Variable = psample_Variable
        
    @property
    def isParameter(self) -> bool:
        return self.__isParameter

    @isParameter.setter
    def isParameter(self, isParameter: bool):
        self.__isParameter = isParameter

    @property
    def psample_Variable(self):
        return self.__psample_Variable

    @psample_Variable.setter
    def psample_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_psample_Variable__psample_Variable", None)
        self.__psample_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "psample_Function7"):
                opp_val = getattr(old_value, "psample_Function7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "psample_Function7"):
                opp_val = getattr(value, "psample_Function7", None)
                if opp_val is None:
                    setattr(value, "psample_Function7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class psample_Function(Member):

    pass
class psample_Interface(TypedElement):

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
                    
