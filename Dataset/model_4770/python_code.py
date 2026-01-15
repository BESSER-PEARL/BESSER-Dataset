from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class CollectionType:

    pass
class eol_types_OrderedCollectionType(CollectionType):

    pass
class eol_types_UniqueCollectionType(CollectionType):

    pass
class eol_types_BagType(CollectionType):

    pass
class RealType:

    pass
class eol_types_IntegerType(RealType):

    pass
class PrimitiveType:

    pass
class eol_types_StringType(PrimitiveType):

    pass
class eol_types_RealType(PrimitiveType):

    pass
class eol_types_BooleanType(PrimitiveType):

    pass
class OrderedCollectionType:

    pass
class eol_types_SequenceType(OrderedCollectionType):

    pass
class UniqueCollectionType:

    pass
class eol_types_OrderedSetType(OrderedCollectionType, UniqueCollectionType):

    pass
class eol_types_SetType(UniqueCollectionType):

    pass
class PseudoType:

    pass
class eol_types_SelfContentType(PseudoType):

    pass
class eol_types_SelfType(PseudoType):

    pass
class AnyType:

    pass
class eol_types_VoidType(AnyType):

    pass
class eol_types_CollectionType(AnyType):

    pass
class eol_types_MapType(AnyType):

    pass
class eol_types_PrimitiveType(AnyType):

    pass
class eol_types_PseudoType(AnyType):

    pass
class eol_types_NativeType(AnyType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class eol_types_InvalidType(AnyType):

    pass
class eol_types_ModelElementType(AnyType):

    def __init__(self, modelName: str, elementName: str):
        self.modelName = modelName
        self.elementName = elementName
        
    @property
    def modelName(self) -> str:
        return self.__modelName

    @modelName.setter
    def modelName(self, modelName: str):
        self.__modelName = modelName

    @property
    def elementName(self) -> str:
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName

class eol_types_ModelType(AnyType):

    def __init__(self, modelName: str):
        self.modelName = modelName
        
    @property
    def modelName(self) -> str:
        return self.__modelName

    @modelName.setter
    def modelName(self, modelName: str):
        self.__modelName = modelName

class Type:

    pass
class eol_types_AnyType(Type):

    def __init__(self, declared: bool, eol_types_AnyType: set["eol_types_Type"] = None, eol_types_AnyType2: "eol_types_MapType" = None, eol_types_AnyType5: "eol_types_MapType" = None):
        self.declared = declared
        self.eol_types_AnyType = eol_types_AnyType if eol_types_AnyType is not None else set()
        self.eol_types_AnyType2 = eol_types_AnyType2
        self.eol_types_AnyType5 = eol_types_AnyType5
        
    @property
    def declared(self) -> bool:
        return self.__declared

    @declared.setter
    def declared(self, declared: bool):
        self.__declared = declared

    @property
    def eol_types_AnyType5(self):
        return self.__eol_types_AnyType5

    @eol_types_AnyType5.setter
    def eol_types_AnyType5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_types_AnyType__eol_types_AnyType5", None)
        self.__eol_types_AnyType5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_types_MapType4"):
                opp_val = getattr(old_value, "eol_types_MapType4", None)
                if opp_val == self:
                    setattr(old_value, "eol_types_MapType4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_types_MapType4"):
                opp_val = getattr(value, "eol_types_MapType4", None)
                setattr(value, "eol_types_MapType4", self)

    @property
    def eol_types_AnyType2(self):
        return self.__eol_types_AnyType2

    @eol_types_AnyType2.setter
    def eol_types_AnyType2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_types_AnyType__eol_types_AnyType2", None)
        self.__eol_types_AnyType2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_types_MapType"):
                opp_val = getattr(old_value, "eol_types_MapType", None)
                if opp_val == self:
                    setattr(old_value, "eol_types_MapType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_types_MapType"):
                opp_val = getattr(value, "eol_types_MapType", None)
                setattr(value, "eol_types_MapType", self)

    @property
    def eol_types_AnyType(self):
        return self.__eol_types_AnyType

    @eol_types_AnyType.setter
    def eol_types_AnyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_types_AnyType__eol_types_AnyType", None)
        self.__eol_types_AnyType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_types_Type"):
                    opp_val = getattr(item, "eol_types_Type", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_types_Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_types_Type"):
                    opp_val = getattr(item, "eol_types_Type", None)
                    
                    setattr(item, "eol_types_Type", self)
                    

class eol_types_Type:

    pass