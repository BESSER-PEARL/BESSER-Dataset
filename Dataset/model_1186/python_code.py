from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CollectionKind(Enum):
    OrderedSet = "OrderedSet"
    Sequence = "Sequence"
    Bag = "Bag"
    Set = "Set"


############################################
# Definition of Classes
############################################

class Iterator:

    pass
class NumericLiteralExp:

    pass
class OCL_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class OCL_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class OperationCallExp:

    pass
class OCL_OperatorCallExp(OperationCallExp):

    pass
class OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class FeaturePropertyCall:

    pass
class OCL_PropertyCallExp(FeaturePropertyCall):

    pass
class OCL_OperationCallExp(FeaturePropertyCall):

    pass
class LoopExp:

    pass
class OCL_IteratorExp(LoopExp):

    pass
class OCL_IterateExp(LoopExp):

    pass
class PrimitiveLiteralExp:

    pass
class OCL_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class OCL_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class OCL_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class CollectionLiteralPart:

    pass
class OCL_CollectionItem(CollectionLiteralPart):

    pass
class OCL_CollectionRange(CollectionLiteralPart):

    pass
class TupleLiteralPart:

    pass
class CallExp:

    pass
class OCL_LoopExp(CallExp):

    pass
class OCL_FeaturePropertyCall(CallExp):

    pass
class LiteralExp:

    pass
class OCL_CollectionLiteralExp(LiteralExp):

    def __init__(self, kind: str, OCL_CollectionLiteralExp: set["CollectionLiteralPart"] = None):
        self.kind = kind
        self.OCL_CollectionLiteralExp = OCL_CollectionLiteralExp if OCL_CollectionLiteralExp is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def OCL_CollectionLiteralExp(self):
        return self.__OCL_CollectionLiteralExp

    @OCL_CollectionLiteralExp.setter
    def OCL_CollectionLiteralExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_CollectionLiteralExp__OCL_CollectionLiteralExp", None)
        self.__OCL_CollectionLiteralExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CollectionLiteralPart"):
                    opp_val = getattr(item, "CollectionLiteralPart", None)
                    
                    if opp_val == self:
                        setattr(item, "CollectionLiteralPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CollectionLiteralPart"):
                    opp_val = getattr(item, "CollectionLiteralPart", None)
                    
                    setattr(item, "CollectionLiteralPart", self)
                    

class OCL_InvalidLiteralExp(LiteralExp):

    pass
class OCL_TupleLiteralExp(LiteralExp):

    pass
class OCL_PrimitiveLiteralExp(LiteralExp):

    pass
class OCL_NullLiteralExp(LiteralExp):

    pass
class OCL_EnumLiteralExp(LiteralExp):

    pass
class CollectionType:

    pass
class OCL_OrderedSetType(CollectionType):

    pass
class OCL_SequenceType(CollectionType):

    pass
class OCL_BagType(CollectionType):

    pass
class OCL_SetType(CollectionType):

    pass
class EnumerationLiteral:

    pass
class Object:

    pass
class OCL_Element(Object):

    pass
class OCL_Extent(Object):

    pass
class OCL_Object(ABC):

    pass
class MultiplicityElement:

    pass
class TypedElement:

    pass
class OCL_Variable(TypedElement):

    pass
class OCL_OclExpression(TypedElement):

    pass
class OCL_Property(MultiplicityElement, TypedElement):

    def __init__(self, isReadOnly: str, isDerived: str, isComposite: str, isId: str, default: str, OCL_Property: "Property" = None):
        self.isReadOnly = isReadOnly
        self.isDerived = isDerived
        self.isComposite = isComposite
        self.isId = isId
        self.default = default
        self.OCL_Property = OCL_Property
        
    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def isId(self) -> str:
        return self.__isId

    @isId.setter
    def isId(self, isId: str):
        self.__isId = isId

    @property
    def OCL_Property(self):
        return self.__OCL_Property

    @OCL_Property.setter
    def OCL_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Property__OCL_Property", None)
        self.__OCL_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property"):
                opp_val = getattr(old_value, "Property", None)
                if opp_val == self:
                    setattr(old_value, "Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property"):
                opp_val = getattr(value, "Property", None)
                setattr(value, "Property", self)

class OCL_CollectionLiteralPart(TypedElement):

    pass
class OCL_TupleLiteralPart(TypedElement):

    pass
class OCL_Operation(MultiplicityElement, TypedElement):

    pass
class OCL_Parameter(MultiplicityElement, TypedElement):

    pass
class Type:

    pass
class OCL_VoidType(Type):

    pass
class OCL_InvalidType(Type):

    pass
class OCL_DataType(Type):

    pass
class OCL_Class(Type):

    def __init__(self, isAbstract: str, OCL_Class: set["Property"] = None, OCL_Class41: set["Operation"] = None, Type36: "OCL_Operation", Type: "OCL_TypedElement", Type27: "OCL_Package", Type45: "OCL_CollectionType"):
        self.isAbstract = isAbstract
        self.OCL_Class = OCL_Class if OCL_Class is not None else set()
        self.OCL_Class41 = OCL_Class41 if OCL_Class41 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def OCL_Class(self):
        return self.__OCL_Class

    @OCL_Class.setter
    def OCL_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Class__OCL_Class", None)
        self.__OCL_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property39"):
                    opp_val = getattr(item, "Property39", None)
                    
                    if opp_val == self:
                        setattr(item, "Property39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property39"):
                    opp_val = getattr(item, "Property39", None)
                    
                    setattr(item, "Property39", self)
                    

    @property
    def OCL_Class41(self):
        return self.__OCL_Class41

    @OCL_Class41.setter
    def OCL_Class41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Class__OCL_Class41", None)
        self.__OCL_Class41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

class PrimitiveType:

    pass
class OCL_StringType(PrimitiveType):

    pass
class OCL_RealType(PrimitiveType):

    pass
class OCL_BooleanType(PrimitiveType):

    pass
class OCL_IntegerType(PrimitiveType):

    pass
class DataType:

    pass
class OCL_Enumeration(DataType):

    pass
class OCL_CollectionType(DataType):

    pass
class OCL_TupleType(DataType):

    pass
class OCL_PrimitiveType(DataType):

    pass
class Extent:

    pass
class OCL_URIExtent(Extent):

    pass
class NamedElement:

    pass
class OCL_EnumerationLiteral(NamedElement):

    pass
class OCL_TypedElement(NamedElement):

    pass
class OCL_Package(NamedElement):

    def __init__(self, uri: str, OCL_Package: set["Type"] = None, OCL_Package29: set["Package"] = None, NamedElement: "OCL_Comment"):
        self.uri = uri
        self.OCL_Package = OCL_Package if OCL_Package is not None else set()
        self.OCL_Package29 = OCL_Package29 if OCL_Package29 is not None else set()
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def OCL_Package(self):
        return self.__OCL_Package

    @OCL_Package.setter
    def OCL_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Package__OCL_Package", None)
        self.__OCL_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type27"):
                    opp_val = getattr(item, "Type27", None)
                    
                    if opp_val == self:
                        setattr(item, "Type27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type27"):
                    opp_val = getattr(item, "Type27", None)
                    
                    setattr(item, "Type27", self)
                    

    @property
    def OCL_Package29(self):
        return self.__OCL_Package29

    @OCL_Package29.setter
    def OCL_Package29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Package__OCL_Package29", None)
        self.__OCL_Package29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    if opp_val == self:
                        setattr(item, "Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    setattr(item, "Package", self)
                    

class OCL_Type(NamedElement):

    pass
class Package:

    pass
class OCL_OclModule(Package):

    pass
class OCL_MultiplicityElement(ABC):

    def __init__(self, isOrdered: str, isUnique: str, lower: str, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

class Element:

    pass
class OCL_Comment(Element):

    pass
class OCL_NamedElement(Element):

    def __init__(self, name: str, Element: "OCL_Tag"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class OCL_Tag(Element):

    def __init__(self, value: str, name: str, OCL_Tag: set["Element"] = None, Element: "OCL_Tag"):
        self.value = value
        self.name = name
        self.OCL_Tag = OCL_Tag if OCL_Tag is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OCL_Tag(self):
        return self.__OCL_Tag

    @OCL_Tag.setter
    def OCL_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Tag__OCL_Tag", None)
        self.__OCL_Tag = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    setattr(item, "Element", self)
                    

class OCL_OclContextDefinition(Element):

    pass
class Parameter:

    pass
class OclModuleElement:

    pass
class OCL_DeriveOclModuleElement(OclModuleElement):

    pass
class OCL_Invariant(OclModuleElement):

    def __init__(self, name: str, OCL_Invariant: "OclExpression" = None, OCL_Invariant22: "Variable" = None, OclModuleElement: "OCL_OclModule"):
        self.name = name
        self.OCL_Invariant = OCL_Invariant
        self.OCL_Invariant22 = OCL_Invariant22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OCL_Invariant22(self):
        return self.__OCL_Invariant22

    @OCL_Invariant22.setter
    def OCL_Invariant22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Invariant__OCL_Invariant22", None)
        self.__OCL_Invariant22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable23"):
                opp_val = getattr(old_value, "Variable23", None)
                if opp_val == self:
                    setattr(old_value, "Variable23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable23"):
                opp_val = getattr(value, "Variable23", None)
                setattr(value, "Variable23", self)

    @property
    def OCL_Invariant(self):
        return self.__OCL_Invariant

    @OCL_Invariant.setter
    def OCL_Invariant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Invariant__OCL_Invariant", None)
        self.__OCL_Invariant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression20"):
                opp_val = getattr(old_value, "OclExpression20", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression20"):
                opp_val = getattr(value, "OclExpression20", None)
                setattr(value, "OclExpression20", self)

class OCL_DefOclModuleElement(OclModuleElement):

    pass
class OclContextDefinition:

    pass
class OCL_OclModuleElement(ABC):

    pass
class OCL_OclFeature(ABC):

    pass
class Property:

    pass
class OclExpression:

    pass
class OCL_IfExp(OclExpression):

    pass
class OCL_CallExp(OclExpression):

    pass
class OCL_LiteralExp(OclExpression):

    pass
class OCL_LetExp(OclExpression):

    pass
class OCL_VariableExp(OclExpression):

    pass
class Variable:

    pass
class OCL_Iterator(Variable):

    pass
class OclFeature:

    pass
class OCL_OclProperty(OclFeature, Property):

    pass
class Operation:

    pass
class OCL_OclOperation(OclFeature, Operation):

    pass
class Class:

    pass
class OCL_AnyType(Class):

    pass