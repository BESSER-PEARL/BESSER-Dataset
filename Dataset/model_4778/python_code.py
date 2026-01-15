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

class types_AnnotatableElement:

    def __init__(self, types_AnnotatableElement: set["types_Annotation"] = None, types_AnnotatableElement35: "types_AnnotatableElement" = None, types_AnnotatableElement33: "types_AnnotatableElement" = None):
        self.types_AnnotatableElement = types_AnnotatableElement if types_AnnotatableElement is not None else set()
        self.types_AnnotatableElement35 = types_AnnotatableElement35
        self.types_AnnotatableElement33 = types_AnnotatableElement33
        
    @property
    def types_AnnotatableElement33(self):
        return self.__types_AnnotatableElement33

    @types_AnnotatableElement33.setter
    def types_AnnotatableElement33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_AnnotatableElement__types_AnnotatableElement33", None)
        self.__types_AnnotatableElement33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_AnnotatableElement35"):
                opp_val = getattr(old_value, "types_AnnotatableElement35", None)
                if opp_val == self:
                    setattr(old_value, "types_AnnotatableElement35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_AnnotatableElement35"):
                opp_val = getattr(value, "types_AnnotatableElement35", None)
                setattr(value, "types_AnnotatableElement35", self)

    @property
    def types_AnnotatableElement(self):
        return self.__types_AnnotatableElement

    @types_AnnotatableElement.setter
    def types_AnnotatableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_AnnotatableElement__types_AnnotatableElement", None)
        self.__types_AnnotatableElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_Annotation32"):
                    opp_val = getattr(item, "types_Annotation32", None)
                    
                    if opp_val == self:
                        setattr(item, "types_Annotation32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_Annotation32"):
                    opp_val = getattr(item, "types_Annotation32", None)
                    
                    setattr(item, "types_Annotation32", self)
                    

    @property
    def types_AnnotatableElement35(self):
        return self.__types_AnnotatableElement35

    @types_AnnotatableElement35.setter
    def types_AnnotatableElement35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_AnnotatableElement__types_AnnotatableElement35", None)
        self.__types_AnnotatableElement35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_AnnotatableElement33"):
                opp_val = getattr(old_value, "types_AnnotatableElement33", None)
                if opp_val == self:
                    setattr(old_value, "types_AnnotatableElement33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_AnnotatableElement33"):
                opp_val = getattr(value, "types_AnnotatableElement33", None)
                setattr(value, "types_AnnotatableElement33", self)

    def getAnnotationOfType(self, typeName: str) -> str:
        # TODO: Implement getAnnotationOfType method
        pass

class types_Annotation:

    pass
class types_MetaComposite:

    pass
class types_EObject:

    pass
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

class types_TypedElement(ABC):

    pass
class types_Domain:

    def __init__(self, domainID: str):
        self.domainID = domainID
        
    @property
    def domainID(self) -> str:
        return self.__domainID

    @domainID.setter
    def domainID(self, domainID: str):
        self.__domainID = domainID

class Type:

    pass
class types_TypeParameter(Type):

    pass
class types_AnnotationType(Type):

    pass
class types_PrimitiveType(Type):

    pass
class ComplexType:

    pass
class types_EnumerationType(ComplexType):

    pass
class DomainElement:

    pass
class Declaration:

    pass
class types_Package(Declaration, DomainElement):

    pass
class TypedElement:

    pass
class types_TypedDeclaration(Declaration, TypedElement):

    pass
class types_Expression(ABC):

    pass
class GenericElement:

    pass
class types_ComplexType(Type, GenericElement):

    def __init__(self, types_ComplexType: set["types_Declaration"] = None):
        self.types_ComplexType = types_ComplexType if types_ComplexType is not None else set()
        
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
                if hasattr(item, "types_Declaration21"):
                    opp_val = getattr(item, "types_Declaration21", None)
                    
                    if opp_val == self:
                        setattr(item, "types_Declaration21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_Declaration21"):
                    opp_val = getattr(item, "types_Declaration21", None)
                    
                    setattr(item, "types_Declaration21", self)
                    

    def getAllFeatures(self) -> Declaration:
        # TODO: Implement getAllFeatures method
        pass

class TypedDeclaration:

    pass
class types_Enumerator(TypedDeclaration):

    def __init__(self, literalValue: int, Enumerator: "types_EnumerationType" = None, enumerator: "types_EnumerationType" = None):
        self.literalValue = literalValue
        self.Enumerator = Enumerator
        self.enumerator = enumerator
        
    @property
    def literalValue(self) -> int:
        return self.__literalValue

    @literalValue.setter
    def literalValue(self, literalValue: int):
        self.__literalValue = literalValue

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

class types_Property(TypedDeclaration):

    def __init__(self, const: bool, readonly: bool, types_Property: "types_Expression" = None, types_Property38: "types_AnnotationType" = None):
        self.const = const
        self.readonly = readonly
        self.types_Property = types_Property
        self.types_Property38 = types_Property38
        
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
    def types_Property(self):
        return self.__types_Property

    @types_Property.setter
    def types_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Property__types_Property", None)
        self.__types_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Expression"):
                opp_val = getattr(old_value, "types_Expression", None)
                if opp_val == self:
                    setattr(old_value, "types_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Expression"):
                opp_val = getattr(value, "types_Expression", None)
                setattr(value, "types_Expression", self)

    @property
    def types_Property38(self):
        return self.__types_Property38

    @types_Property38.setter
    def types_Property38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Property__types_Property38", None)
        self.__types_Property38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_AnnotationType37"):
                opp_val = getattr(old_value, "types_AnnotationType37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_AnnotationType37"):
                opp_val = getattr(value, "types_AnnotationType37", None)
                if opp_val is None:
                    setattr(value, "types_AnnotationType37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class types_Event(TypedDeclaration):

    def __init__(self, direction: str):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class types_TypeAlias(TypedDeclaration, Type):

    pass
class types_Operation(TypedDeclaration, GenericElement):

    def __init__(self, variadic: bool, owningOperation: set["types_Parameter"] = None, Operation: "types_Parameter" = None):
        self.variadic = variadic
        self.owningOperation = owningOperation if owningOperation is not None else set()
        self.Operation = Operation
        
    @property
    def variadic(self) -> bool:
        return self.__variadic

    @variadic.setter
    def variadic(self, variadic: bool):
        self.__variadic = variadic

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameters"):
                opp_val = getattr(old_value, "parameters", None)
                if opp_val == self:
                    setattr(old_value, "parameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameters"):
                opp_val = getattr(value, "parameters", None)
                setattr(value, "parameters", self)

    @property
    def owningOperation(self):
        return self.__owningOperation

    @owningOperation.setter
    def owningOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Operation__owningOperation", None)
        self.__owningOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

    def getVarArgIndex(self) -> int:
        # TODO: Implement getVarArgIndex method
        pass

class MetaComposite:

    pass
class AnnotatableElement:

    pass
class NamedElement:

    pass
class types_Parameter(NamedElement, TypedElement, AnnotatableElement):

    def __init__(self, varArgs: bool, optional: bool, Parameter: "types_Operation" = None, parameters: "types_Operation" = None):
        self.varArgs = varArgs
        self.optional = optional
        self.Parameter = Parameter
        self.parameters = parameters
        
    @property
    def varArgs(self) -> bool:
        return self.__varArgs

    @varArgs.setter
    def varArgs(self, varArgs: bool):
        self.__varArgs = varArgs

    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Parameter__Parameter", None)
        self.__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningOperation"):
                opp_val = getattr(old_value, "owningOperation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningOperation"):
                opp_val = getattr(value, "owningOperation", None)
                if opp_val is None:
                    setattr(value, "owningOperation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Parameter__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation"):
                opp_val = getattr(old_value, "Operation", None)
                if opp_val == self:
                    setattr(old_value, "Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation"):
                opp_val = getattr(value, "Operation", None)
                setattr(value, "Operation", self)

class types_GenericElement(NamedElement):

    pass
class types_TypeSpecifier:

    pass
class types_Type(Declaration):

    def __init__(self, abstract: bool, visible: bool, types_Type: set["types_TypeSpecifier"] = None, types_Type24: "types_TypeParameter" = None, types_Type9: "types_TypedElement" = None, types_Type15: "types_TypeSpecifier" = None):
        self.abstract = abstract
        self.visible = visible
        self.types_Type = types_Type if types_Type is not None else set()
        self.types_Type24 = types_Type24
        self.types_Type9 = types_Type9
        self.types_Type15 = types_Type15
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

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
                if hasattr(item, "types_TypeSpecifier"):
                    opp_val = getattr(item, "types_TypeSpecifier", None)
                    
                    if opp_val == self:
                        setattr(item, "types_TypeSpecifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_TypeSpecifier"):
                    opp_val = getattr(item, "types_TypeSpecifier", None)
                    
                    setattr(item, "types_TypeSpecifier", self)
                    

    @property
    def types_Type24(self):
        return self.__types_Type24

    @types_Type24.setter
    def types_Type24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type24", None)
        self.__types_Type24 = value
        
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
    def types_Type9(self):
        return self.__types_Type9

    @types_Type9.setter
    def types_Type9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type9", None)
        self.__types_Type9 = value
        
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

class types_Declaration(NamedElement, MetaComposite, AnnotatableElement):

    def __init__(self, static: bool, id: str, types_Declaration: "types_Package" = None, types_Declaration21: "types_ComplexType" = None, types_Declaration42: "types_MetaComposite" = None):
        self.static = static
        self.id = id
        self.types_Declaration = types_Declaration
        self.types_Declaration21 = types_Declaration21
        self.types_Declaration42 = types_Declaration42
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def types_Declaration21(self):
        return self.__types_Declaration21

    @types_Declaration21.setter
    def types_Declaration21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Declaration__types_Declaration21", None)
        self.__types_Declaration21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_ComplexType"):
                opp_val = getattr(old_value, "types_ComplexType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_ComplexType"):
                opp_val = getattr(value, "types_ComplexType", None)
                if opp_val is None:
                    setattr(value, "types_ComplexType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_Declaration(self):
        return self.__types_Declaration

    @types_Declaration.setter
    def types_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Declaration__types_Declaration", None)
        self.__types_Declaration = value
        
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

    @property
    def types_Declaration42(self):
        return self.__types_Declaration42

    @types_Declaration42.setter
    def types_Declaration42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Declaration__types_Declaration42", None)
        self.__types_Declaration42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_MetaComposite"):
                opp_val = getattr(old_value, "types_MetaComposite", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_MetaComposite"):
                opp_val = getattr(value, "types_MetaComposite", None)
                if opp_val is None:
                    setattr(value, "types_MetaComposite", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
