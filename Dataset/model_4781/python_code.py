from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Direction(Enum):
    LOCAL = "LOCAL"
    IN = "IN"
    OUT = "OUT"


############################################
# Definition of Classes
############################################

class TypeConstraint:

    pass
class types_RangeConstraint(TypeConstraint):

    def __init__(self, lowerBound: str, upperBound: str):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        
    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> str:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: str):
        self.__lowerBound = lowerBound

class ParameterizedType:

    pass
class types_ComplexType(ParameterizedType):

    def __init__(self, types_ComplexType: set["types_Declaration"] = None, types_ComplexType17: "types_ComplexType" = None, types_ComplexType15: set["types_ComplexType"] = None):
        self.types_ComplexType = types_ComplexType if types_ComplexType is not None else set()
        self.types_ComplexType17 = types_ComplexType17
        self.types_ComplexType15 = types_ComplexType15 if types_ComplexType15 is not None else set()
        
    @property
    def types_ComplexType(self):
        return self.__types_ComplexType

    @types_ComplexType.setter
    def types_ComplexType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_ComplexType__types_ComplexType", None)
        self.__types_ComplexType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_Declaration"):
                    opp_val = getattr(item, "types_Declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "types_Declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_Declaration"):
                    opp_val = getattr(item, "types_Declaration", None)
                    
                    setattr(item, "types_Declaration", self)
                    

    @property
    def types_ComplexType17(self):
        return self.__types_ComplexType17

    @types_ComplexType17.setter
    def types_ComplexType17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_ComplexType__types_ComplexType17", None)
        self.__types_ComplexType17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_ComplexType15"):
                opp_val = getattr(old_value, "types_ComplexType15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_ComplexType15"):
                opp_val = getattr(value, "types_ComplexType15", None)
                if opp_val is None:
                    setattr(value, "types_ComplexType15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_ComplexType15(self):
        return self.__types_ComplexType15

    @types_ComplexType15.setter
    def types_ComplexType15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_ComplexType__types_ComplexType15", None)
        self.__types_ComplexType15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_ComplexType17"):
                    opp_val = getattr(item, "types_ComplexType17", None)
                    
                    if opp_val == self:
                        setattr(item, "types_ComplexType17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_ComplexType17"):
                    opp_val = getattr(item, "types_ComplexType17", None)
                    
                    setattr(item, "types_ComplexType17", self)
                    

    def getAllFeatures(self) -> Declaration:
        # TODO: Implement getAllFeatures method
        pass

class Type:

    pass
class types_ParameterizedType(Type):

    pass
class types_TypeParameter(Type):

    pass
class types_PrimitiveType(Type):

    pass
class PrimitiveType:

    pass
class types_EnumerationType(PrimitiveType):

    pass
class types_TypedElement(ABC):

    pass
class Declaration:

    pass
class types_Property(Declaration):

    def __init__(self, external: bool, const: bool, readonly: bool):
        self.external = external
        self.const = const
        self.readonly = readonly
        
    @property
    def readonly(self) -> bool:
        return self.__readonly

    @readonly.setter
    def readonly(self, readonly: bool):
        self.__readonly = readonly

    @property
    def external(self) -> bool:
        return self.__external

    @external.setter
    def external(self, external: bool):
        self.__external = external

    @property
    def const(self) -> bool:
        return self.__const

    @const.setter
    def const(self, const: bool):
        self.__const = const

class types_Event(Declaration):

    def __init__(self, direction: str):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class TypedElement:

    pass
class types_TypeAlias(Type, TypedElement):

    pass
class types_TypeConstraint:

    def __init__(self, value: str, types_TypeConstraint: "types_Type" = None):
        self.value = value
        self.types_TypeConstraint = types_TypeConstraint
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def types_TypeConstraint(self):
        return self.__types_TypeConstraint

    @types_TypeConstraint.setter
    def types_TypeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_TypeConstraint__types_TypeConstraint", None)
        self.__types_TypeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Type"):
                opp_val = getattr(old_value, "types_Type", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Type"):
                opp_val = getattr(value, "types_Type", None)
                if opp_val is None:
                    setattr(value, "types_Type", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PackageMember:

    pass
class types_Operation(PackageMember, Declaration):

    pass
class types_Type(PackageMember):

    def __init__(self, abstract: bool, types_Type: set["types_TypeConstraint"] = None, types_Type7: "types_TypedElement" = None, types_Type10: "types_TypedElement" = None, types_Type20: "types_TypeParameter" = None):
        self.abstract = abstract
        self.types_Type = types_Type if types_Type is not None else set()
        self.types_Type7 = types_Type7
        self.types_Type10 = types_Type10
        self.types_Type20 = types_Type20
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def types_Type10(self):
        return self.__types_Type10

    @types_Type10.setter
    def types_Type10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type10", None)
        self.__types_Type10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_TypedElement9"):
                opp_val = getattr(old_value, "types_TypedElement9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_TypedElement9"):
                opp_val = getattr(value, "types_TypedElement9", None)
                if opp_val is None:
                    setattr(value, "types_TypedElement9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_Type7(self):
        return self.__types_Type7

    @types_Type7.setter
    def types_Type7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type7", None)
        self.__types_Type7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_TypedElement"):
                opp_val = getattr(old_value, "types_TypedElement", None)
                if opp_val == self:
                    setattr(old_value, "types_TypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_TypedElement"):
                opp_val = getattr(value, "types_TypedElement", None)
                setattr(value, "types_TypedElement", self)

    @property
    def types_Type(self):
        return self.__types_Type

    @types_Type.setter
    def types_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type", None)
        self.__types_Type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_TypeConstraint"):
                    opp_val = getattr(item, "types_TypeConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "types_TypeConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_TypeConstraint"):
                    opp_val = getattr(item, "types_TypeConstraint", None)
                    
                    setattr(item, "types_TypeConstraint", self)
                    

    @property
    def types_Type20(self):
        return self.__types_Type20

    @types_Type20.setter
    def types_Type20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type20", None)
        self.__types_Type20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_TypeParameter"):
                opp_val = getattr(old_value, "types_TypeParameter", None)
                if opp_val == self:
                    setattr(old_value, "types_TypeParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_TypeParameter"):
                opp_val = getattr(value, "types_TypeParameter", None)
                setattr(value, "types_TypeParameter", self)

    def getOriginType(self) -> str:
        # TODO: Implement getOriginType method
        pass

class types_Domain:

    def __init__(self, domainID: str, types_Domain: "types_Package" = None):
        self.domainID = domainID
        self.types_Domain = types_Domain
        
    @property
    def domainID(self) -> str:
        return self.__domainID

    @domainID.setter
    def domainID(self, domainID: str):
        self.__domainID = domainID

    @property
    def types_Domain(self):
        return self.__types_Domain

    @types_Domain.setter
    def types_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Domain__types_Domain", None)
        self.__types_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Package2"):
                opp_val = getattr(old_value, "types_Package2", None)
                if opp_val == self:
                    setattr(old_value, "types_Package2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Package2"):
                opp_val = getattr(value, "types_Package2", None)
                setattr(value, "types_Package2", self)

class NamedElement:

    pass
class types_PackageMember(NamedElement):

    pass
class types_Parameter(TypedElement, NamedElement):

    pass
class types_Declaration(TypedElement, NamedElement):

    pass
class types_Enumerator(NamedElement):

    def __init__(self, literalValue: str, Enumerator: "types_EnumerationType" = None, enumerator: "types_EnumerationType" = None):
        self.literalValue = literalValue
        self.Enumerator = Enumerator
        self.enumerator = enumerator
        
    @property
    def literalValue(self) -> str:
        return self.__literalValue

    @literalValue.setter
    def literalValue(self, literalValue: str):
        self.__literalValue = literalValue

    @property
    def Enumerator(self):
        return self.__Enumerator

    @Enumerator.setter
    def Enumerator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Enumerator__Enumerator", None)
        self.__Enumerator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningEnumeration"):
                opp_val = getattr(old_value, "owningEnumeration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningEnumeration"):
                opp_val = getattr(value, "owningEnumeration", None)
                if opp_val is None:
                    setattr(value, "owningEnumeration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def enumerator(self):
        return self.__enumerator

    @enumerator.setter
    def enumerator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Enumerator__enumerator", None)
        self.__enumerator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EnumerationType"):
                opp_val = getattr(old_value, "EnumerationType", None)
                if opp_val == self:
                    setattr(old_value, "EnumerationType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EnumerationType"):
                opp_val = getattr(value, "EnumerationType", None)
                setattr(value, "EnumerationType", self)

class types_Package(NamedElement):

    pass