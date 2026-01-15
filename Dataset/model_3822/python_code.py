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

class TypeSpecifier:

    pass
class types_ArrayTypeSpecifier(TypeSpecifier):

    def __init__(self, size: int):
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    def getElementType(self) -> Type:
        # TODO: Implement getElementType method
        pass

class types_AnnotatableElement:

    pass
class types_EObject:

    pass
class ParameterizedType:

    pass
class types_ComplexType(ParameterizedType):

    def __init__(self, types_ComplexType25: "types_ComplexType" = None, types_ComplexType23: set["types_ComplexType"] = None, types_ComplexType: set["types_Declaration"] = None):
        self.types_ComplexType25 = types_ComplexType25
        self.types_ComplexType23 = types_ComplexType23 if types_ComplexType23 is not None else set()
        self.types_ComplexType = types_ComplexType if types_ComplexType is not None else set()
        
    @property
    def types_ComplexType25(self):
        return self.__types_ComplexType25

    @types_ComplexType25.setter
    def types_ComplexType25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_ComplexType__types_ComplexType25", None)
        self.__types_ComplexType25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_ComplexType23"):
                opp_val = getattr(old_value, "types_ComplexType23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_ComplexType23"):
                opp_val = getattr(value, "types_ComplexType23", None)
                if opp_val is None:
                    setattr(value, "types_ComplexType23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def types_ComplexType23(self):
        return self.__types_ComplexType23

    @types_ComplexType23.setter
    def types_ComplexType23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_ComplexType__types_ComplexType23", None)
        self.__types_ComplexType23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_ComplexType25"):
                    opp_val = getattr(item, "types_ComplexType25", None)
                    
                    if opp_val == self:
                        setattr(item, "types_ComplexType25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_ComplexType25"):
                    opp_val = getattr(item, "types_ComplexType25", None)
                    
                    setattr(item, "types_ComplexType25", self)
                    

    def getAllFeatures(self) -> Declaration:
        # TODO: Implement getAllFeatures method
        pass

class Type:

    pass
class types_PrimitiveType(Type):

    pass
class PrimitiveType:

    pass
class types_EnumerationType(PrimitiveType):

    pass
class TypeConstraint:

    pass
class types_RangeConstraint(TypeConstraint):

    def __init__(self, lowerBound: str, upperBound: str):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        
    @property
    def lowerBound(self) -> str:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: str):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

class types_ParameterizedType(Type):

    pass
class types_TypeParameter(Type):

    pass
class AnnotatableElement:

    pass
class types_TypeSpecifier:

    pass
class types_TypedElement(ABC):

    pass
class PackageMember:

    pass
class types_Annotation(PackageMember):

    pass
class types_Type(PackageMember):

    def __init__(self, abstract: bool, visible: bool, types_Type: set["types_TypeConstraint"] = None, types_Type10: "types_TypedElement" = None, types_Type15: "types_TypeSpecifier" = None, types_Type28: "types_TypeParameter" = None):
        self.abstract = abstract
        self.visible = visible
        self.types_Type = types_Type if types_Type is not None else set()
        self.types_Type10 = types_Type10
        self.types_Type15 = types_Type15
        self.types_Type28 = types_Type28
        
    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

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
    def types_Type28(self):
        return self.__types_Type28

    @types_Type28.setter
    def types_Type28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type28", None)
        self.__types_Type28 = value
        
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

    @property
    def types_Type15(self):
        return self.__types_Type15

    @types_Type15.setter
    def types_Type15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type15", None)
        self.__types_Type15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_TypeSpecifier14"):
                opp_val = getattr(old_value, "types_TypeSpecifier14", None)
                if opp_val == self:
                    setattr(old_value, "types_TypeSpecifier14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_TypeSpecifier14"):
                opp_val = getattr(value, "types_TypeSpecifier14", None)
                setattr(value, "types_TypeSpecifier14", self)

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
            if hasattr(old_value, "types_TypedElement"):
                opp_val = getattr(old_value, "types_TypedElement", None)
                if opp_val == self:
                    setattr(old_value, "types_TypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_TypedElement"):
                opp_val = getattr(value, "types_TypedElement", None)
                setattr(value, "types_TypedElement", self)

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

class Declaration:

    pass
class types_Enumerator(Declaration):

    def __init__(self, literalValue: int, enumerator: "types_EnumerationType" = None, Enumerator: "types_EnumerationType" = None):
        self.literalValue = literalValue
        self.enumerator = enumerator
        self.Enumerator = Enumerator
        
    @property
    def literalValue(self) -> int:
        return self.__literalValue

    @literalValue.setter
    def literalValue(self, literalValue: int):
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

class types_Event(Declaration):

    def __init__(self, direction: str):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class types_Property(Declaration):

    def __init__(self, const: bool, readonly: bool, external: bool, types_Property: "types_Annotation" = None):
        self.const = const
        self.readonly = readonly
        self.external = external
        self.types_Property = types_Property
        
    @property
    def readonly(self) -> bool:
        return self.__readonly

    @readonly.setter
    def readonly(self, readonly: bool):
        self.__readonly = readonly

    @property
    def const(self) -> bool:
        return self.__const

    @const.setter
    def const(self, const: bool):
        self.__const = const

    @property
    def external(self) -> bool:
        return self.__external

    @external.setter
    def external(self, external: bool):
        self.__external = external

    @property
    def types_Property(self):
        return self.__types_Property

    @types_Property.setter
    def types_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Property__types_Property", None)
        self.__types_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Annotation"):
                opp_val = getattr(old_value, "types_Annotation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Annotation"):
                opp_val = getattr(value, "types_Annotation", None)
                if opp_val is None:
                    setattr(value, "types_Annotation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class types_Operation(Declaration):

    pass
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

class NamedElement:

    pass
class types_PackageMember(NamedElement, AnnotatableElement):

    def __init__(self, id: str, types_PackageMember: "types_Package" = None):
        self.id = id
        self.types_PackageMember = types_PackageMember
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def types_PackageMember(self):
        return self.__types_PackageMember

    @types_PackageMember.setter
    def types_PackageMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_PackageMember__types_PackageMember", None)
        self.__types_PackageMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Package"):
                opp_val = getattr(old_value, "types_Package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Package"):
                opp_val = getattr(value, "types_Package", None)
                if opp_val is None:
                    setattr(value, "types_Package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class types_Parameter(NamedElement, AnnotatableElement, TypedElement):

    pass
class types_Declaration(NamedElement, PackageMember, TypedElement):

    pass
class types_Package(NamedElement):

    pass