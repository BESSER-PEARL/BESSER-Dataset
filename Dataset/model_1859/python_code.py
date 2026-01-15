from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class NativeTypeKind(Enum):
    Simple = "Simple"
    Length = "Length"
    LengthAndPrecision = "LengthAndPrecision"
    Enum = "Enum"
class TypesLibraryKind(Enum):
    logicalTypes = "logicalTypes"
    physicalTypes = "physicalTypes"


############################################
# Definition of Classes
############################################

class typeslibrary_TypesLibrary(ABC):

    def __init__(self, kind: str, typeslibrary_TypesLibrary: "typeslibrary_TypesLibraryUser" = None):
        self.kind = kind
        self.typeslibrary_TypesLibrary = typeslibrary_TypesLibrary
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def typeslibrary_TypesLibrary(self):
        return self.__typeslibrary_TypesLibrary

    @typeslibrary_TypesLibrary.setter
    def typeslibrary_TypesLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeslibrary_TypesLibrary__typeslibrary_TypesLibrary", None)
        self.__typeslibrary_TypesLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeslibrary_TypesLibraryUser"):
                opp_val = getattr(old_value, "typeslibrary_TypesLibraryUser", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeslibrary_TypesLibraryUser"):
                opp_val = getattr(value, "typeslibrary_TypesLibraryUser", None)
                if opp_val is None:
                    setattr(value, "typeslibrary_TypesLibraryUser", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class typeslibrary_TypesLibraryUser(ABC):

    pass
class Type:

    pass
class typeslibrary_UserDefinedTypeRef(Type):

    pass
class typeslibrary_TypeInstance(Type):

    def __init__(self, literals: str, length: int, precision: int, typeslibrary_TypeInstance8: "typeslibrary_SimpleNamedType" = None, typeslibrary_TypeInstance: "typeslibrary_NativeType" = None):
        self.literals = literals
        self.length = length
        self.precision = precision
        self.typeslibrary_TypeInstance8 = typeslibrary_TypeInstance8
        self.typeslibrary_TypeInstance = typeslibrary_TypeInstance
        
    @property
    def literals(self) -> str:
        return self.__literals

    @literals.setter
    def literals(self, literals: str):
        self.__literals = literals

    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def typeslibrary_TypeInstance(self):
        return self.__typeslibrary_TypeInstance

    @typeslibrary_TypeInstance.setter
    def typeslibrary_TypeInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeslibrary_TypeInstance__typeslibrary_TypeInstance", None)
        self.__typeslibrary_TypeInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeslibrary_NativeType2"):
                opp_val = getattr(old_value, "typeslibrary_NativeType2", None)
                if opp_val == self:
                    setattr(old_value, "typeslibrary_NativeType2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeslibrary_NativeType2"):
                opp_val = getattr(value, "typeslibrary_NativeType2", None)
                setattr(value, "typeslibrary_NativeType2", self)

    @property
    def typeslibrary_TypeInstance8(self):
        return self.__typeslibrary_TypeInstance8

    @typeslibrary_TypeInstance8.setter
    def typeslibrary_TypeInstance8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeslibrary_TypeInstance__typeslibrary_TypeInstance8", None)
        self.__typeslibrary_TypeInstance8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeslibrary_SimpleNamedType"):
                opp_val = getattr(old_value, "typeslibrary_SimpleNamedType", None)
                if opp_val == self:
                    setattr(old_value, "typeslibrary_SimpleNamedType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeslibrary_SimpleNamedType"):
                opp_val = getattr(value, "typeslibrary_SimpleNamedType", None)
                setattr(value, "typeslibrary_SimpleNamedType", self)

class typeslibrary_Type(ABC):

    pass
class typeslibrary_UserDefinedType(ABC):

    def __init__(self, name: str, typeslibrary_UserDefinedType: "typeslibrary_ComplexNamedType" = None, typeslibrary_UserDefinedType12: "typeslibrary_UserDefinedTypesLibrary" = None, typeslibrary_UserDefinedType10: "typeslibrary_UserDefinedTypeRef" = None):
        self.name = name
        self.typeslibrary_UserDefinedType = typeslibrary_UserDefinedType
        self.typeslibrary_UserDefinedType12 = typeslibrary_UserDefinedType12
        self.typeslibrary_UserDefinedType10 = typeslibrary_UserDefinedType10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typeslibrary_UserDefinedType10(self):
        return self.__typeslibrary_UserDefinedType10

    @typeslibrary_UserDefinedType10.setter
    def typeslibrary_UserDefinedType10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeslibrary_UserDefinedType__typeslibrary_UserDefinedType10", None)
        self.__typeslibrary_UserDefinedType10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeslibrary_UserDefinedTypeRef"):
                opp_val = getattr(old_value, "typeslibrary_UserDefinedTypeRef", None)
                if opp_val == self:
                    setattr(old_value, "typeslibrary_UserDefinedTypeRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeslibrary_UserDefinedTypeRef"):
                opp_val = getattr(value, "typeslibrary_UserDefinedTypeRef", None)
                setattr(value, "typeslibrary_UserDefinedTypeRef", self)

    @property
    def typeslibrary_UserDefinedType12(self):
        return self.__typeslibrary_UserDefinedType12

    @typeslibrary_UserDefinedType12.setter
    def typeslibrary_UserDefinedType12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeslibrary_UserDefinedType__typeslibrary_UserDefinedType12", None)
        self.__typeslibrary_UserDefinedType12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeslibrary_UserDefinedTypesLibrary"):
                opp_val = getattr(old_value, "typeslibrary_UserDefinedTypesLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeslibrary_UserDefinedTypesLibrary"):
                opp_val = getattr(value, "typeslibrary_UserDefinedTypesLibrary", None)
                if opp_val is None:
                    setattr(value, "typeslibrary_UserDefinedTypesLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def typeslibrary_UserDefinedType(self):
        return self.__typeslibrary_UserDefinedType

    @typeslibrary_UserDefinedType.setter
    def typeslibrary_UserDefinedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeslibrary_UserDefinedType__typeslibrary_UserDefinedType", None)
        self.__typeslibrary_UserDefinedType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeslibrary_ComplexNamedType"):
                opp_val = getattr(old_value, "typeslibrary_ComplexNamedType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeslibrary_ComplexNamedType"):
                opp_val = getattr(value, "typeslibrary_ComplexNamedType", None)
                if opp_val is None:
                    setattr(value, "typeslibrary_ComplexNamedType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UserDefinedType:

    pass
class typeslibrary_SimpleNamedType(UserDefinedType):

    pass
class typeslibrary_ComplexNamedType(UserDefinedType):

    pass
class typeslibrary_NativeType:

    def __init__(self, name: str, spec: str, typeslibrary_NativeType: "typeslibrary_NativeTypesLibrary" = None, typeslibrary_NativeType5: "typeslibrary_NativeType" = None, typeslibrary_NativeType3: "typeslibrary_NativeType" = None, typeslibrary_NativeType2: "typeslibrary_TypeInstance" = None):
        self.name = name
        self.spec = spec
        self.typeslibrary_NativeType = typeslibrary_NativeType
        self.typeslibrary_NativeType5 = typeslibrary_NativeType5
        self.typeslibrary_NativeType3 = typeslibrary_NativeType3
        self.typeslibrary_NativeType2 = typeslibrary_NativeType2
        
    @property
    def spec(self) -> str:
        return self.__spec

    @spec.setter
    def spec(self, spec: str):
        self.__spec = spec

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typeslibrary_NativeType2(self):
        return self.__typeslibrary_NativeType2

    @typeslibrary_NativeType2.setter
    def typeslibrary_NativeType2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeslibrary_NativeType__typeslibrary_NativeType2", None)
        self.__typeslibrary_NativeType2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeslibrary_TypeInstance"):
                opp_val = getattr(old_value, "typeslibrary_TypeInstance", None)
                if opp_val == self:
                    setattr(old_value, "typeslibrary_TypeInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeslibrary_TypeInstance"):
                opp_val = getattr(value, "typeslibrary_TypeInstance", None)
                setattr(value, "typeslibrary_TypeInstance", self)

    @property
    def typeslibrary_NativeType3(self):
        return self.__typeslibrary_NativeType3

    @typeslibrary_NativeType3.setter
    def typeslibrary_NativeType3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeslibrary_NativeType__typeslibrary_NativeType3", None)
        self.__typeslibrary_NativeType3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeslibrary_NativeType5"):
                opp_val = getattr(old_value, "typeslibrary_NativeType5", None)
                if opp_val == self:
                    setattr(old_value, "typeslibrary_NativeType5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeslibrary_NativeType5"):
                opp_val = getattr(value, "typeslibrary_NativeType5", None)
                setattr(value, "typeslibrary_NativeType5", self)

    @property
    def typeslibrary_NativeType5(self):
        return self.__typeslibrary_NativeType5

    @typeslibrary_NativeType5.setter
    def typeslibrary_NativeType5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeslibrary_NativeType__typeslibrary_NativeType5", None)
        self.__typeslibrary_NativeType5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeslibrary_NativeType3"):
                opp_val = getattr(old_value, "typeslibrary_NativeType3", None)
                if opp_val == self:
                    setattr(old_value, "typeslibrary_NativeType3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeslibrary_NativeType3"):
                opp_val = getattr(value, "typeslibrary_NativeType3", None)
                setattr(value, "typeslibrary_NativeType3", self)

    @property
    def typeslibrary_NativeType(self):
        return self.__typeslibrary_NativeType

    @typeslibrary_NativeType.setter
    def typeslibrary_NativeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeslibrary_NativeType__typeslibrary_NativeType", None)
        self.__typeslibrary_NativeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeslibrary_NativeTypesLibrary"):
                opp_val = getattr(old_value, "typeslibrary_NativeTypesLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeslibrary_NativeTypesLibrary"):
                opp_val = getattr(value, "typeslibrary_NativeTypesLibrary", None)
                if opp_val is None:
                    setattr(value, "typeslibrary_NativeTypesLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TypesLibrary:

    pass
class typeslibrary_UserDefinedTypesLibrary(TypesLibrary):

    def __init__(self, name: str, typeslibrary_UserDefinedTypesLibrary: set["typeslibrary_UserDefinedType"] = None):
        self.name = name
        self.typeslibrary_UserDefinedTypesLibrary = typeslibrary_UserDefinedTypesLibrary if typeslibrary_UserDefinedTypesLibrary is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typeslibrary_UserDefinedTypesLibrary(self):
        return self.__typeslibrary_UserDefinedTypesLibrary

    @typeslibrary_UserDefinedTypesLibrary.setter
    def typeslibrary_UserDefinedTypesLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeslibrary_UserDefinedTypesLibrary__typeslibrary_UserDefinedTypesLibrary", None)
        self.__typeslibrary_UserDefinedTypesLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "typeslibrary_UserDefinedType12"):
                    opp_val = getattr(item, "typeslibrary_UserDefinedType12", None)
                    
                    if opp_val == self:
                        setattr(item, "typeslibrary_UserDefinedType12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "typeslibrary_UserDefinedType12"):
                    opp_val = getattr(item, "typeslibrary_UserDefinedType12", None)
                    
                    setattr(item, "typeslibrary_UserDefinedType12", self)
                    

class typeslibrary_NativeTypesLibrary(TypesLibrary):

    def __init__(self, name: str, typeslibrary_NativeTypesLibrary: set["typeslibrary_NativeType"] = None):
        self.name = name
        self.typeslibrary_NativeTypesLibrary = typeslibrary_NativeTypesLibrary if typeslibrary_NativeTypesLibrary is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typeslibrary_NativeTypesLibrary(self):
        return self.__typeslibrary_NativeTypesLibrary

    @typeslibrary_NativeTypesLibrary.setter
    def typeslibrary_NativeTypesLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeslibrary_NativeTypesLibrary__typeslibrary_NativeTypesLibrary", None)
        self.__typeslibrary_NativeTypesLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "typeslibrary_NativeType"):
                    opp_val = getattr(item, "typeslibrary_NativeType", None)
                    
                    if opp_val == self:
                        setattr(item, "typeslibrary_NativeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "typeslibrary_NativeType"):
                    opp_val = getattr(item, "typeslibrary_NativeType", None)
                    
                    setattr(item, "typeslibrary_NativeType", self)
                    

    def findTypeByName(self, name: str) -> str:
        # TODO: Implement findTypeByName method
        pass
