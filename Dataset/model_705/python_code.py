from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SeverityKind(Enum):
    error = "error"
    warning = "warning"
    fatal = "fatal"
class EnforcementMode(Enum):
    Creation = "Creation"
    Deletion = "Deletion"
class DirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
class CollectionKind(Enum):
    Set = "Set"
    OrderedSet = "OrderedSet"
    Bag = "Bag"
    Sequence = "Sequence"
    Collection = "Collection"
class ImportKind(Enum):
    extension = "extension"
    access = "access"


############################################
# Definition of Classes
############################################

class Extent:

    pass
class FlatQVT_URIExtent(Extent):

    def __init__(self):
        
    def contextURI(self) -> str:
        # TODO: Implement contextURI method
        pass

    def uri(self, element: Element) -> str:
        # TODO: Implement uri method
        pass

    def element(self, uri: str) -> Element:
        # TODO: Implement element method
        pass

class ResolveExp:

    pass
class FlatQVT_ResolveInExp(ResolveExp):

    pass
class Transformation:

    pass
class FlatQVT_RelationalTransformation(Transformation):

    pass
class ReflectiveCollection:

    pass
class FlatQVT_ReflectiveSequence(ReflectiveCollection):

    def __init__(self):
        
    def remove(self, index: str) -> Object:
        # TODO: Implement remove method
        pass

    def get(self, index: str) -> Object:
        # TODO: Implement get method
        pass

    def add(self, object: Object, index: str):
        # TODO: Implement add method
        pass

    def set(self, index: str, object: Object) -> Object:
        # TODO: Implement set method
        pass

class NavigationCallExp:

    pass
class FlatQVT_PropertyCallExp(NavigationCallExp):

    pass
class Assignment:

    pass
class FlatQVT_VariableAssignment(Assignment):

    pass
class FlatQVT_PropertyAssignment(Assignment):

    pass
class PropertyCallExp:

    pass
class FlatQVT_OppositePropertyCallExp(PropertyCallExp):

    pass
class MultiplicityElement:

    pass
class FlatQVT_MultiplicityElement(ABC):

    pass
class InstantiationExp:

    pass
class FlatQVT_ObjectExp(InstantiationExp):

    pass
class FlatQVT_Object:

    pass
class FeatureCallExp:

    pass
class FlatQVT_OperationCallExp(FeatureCallExp):

    pass
class FlatQVT_NavigationCallExp(FeatureCallExp):

    pass
class Package:

    pass
class Class:

    pass
class FlatQVT_Typedef(Class):

    pass
class FlatQVT_Transformation(Class, Package):

    pass
class FlatQVT_Module(Class, Package):

    pass
class FlatQVT_ModelType(Class):

    pass
class ImperativeCallExp:

    pass
class FlatQVT_MappingCallExp(ImperativeCallExp):

    pass
class VarParameter:

    pass
class FlatQVT_ModelParameter(VarParameter):

    pass
class FlatQVT_MappingParameter(VarParameter):

    pass
class Module:

    pass
class FlatQVT_OperationalTransformation(Module):

    pass
class FlatQVT_Library(Module):

    pass
class Rule:

    pass
class FlatQVT_Relation(Rule):

    pass
class NumericLiteralExp:

    pass
class FlatQVT_UnlimitedNaturalExp(NumericLiteralExp):

    pass
class FlatQVT_RealLiteralExp(NumericLiteralExp):

    pass
class FlatQVT_IntegerLiteralExp(NumericLiteralExp):

    pass
class LoopExp:

    pass
class FlatQVT_IteratorExp(LoopExp):

    pass
class FlatQVT_IterateExp(LoopExp):

    pass
class OperationCallExp:

    pass
class Operation:

    pass
class FlatQVT_ImperativeOperation(Operation):

    pass
class FlatQVT_Function(Operation):

    pass
class ImperativeLoopExp:

    pass
class FlatQVT_ImperativeIterateExp(ImperativeLoopExp):

    pass
class FlatQVT_ForExp(ImperativeLoopExp):

    pass
class CallExp:

    pass
class FlatQVT_FeatureCallExp(CallExp):

    pass
class Parameter:

    pass
class Variable:

    pass
class FlatQVT_RealizedVariable(Variable):

    pass
class FlatQVT_VarParameter(Variable, Parameter):

    pass
class FlatQVT_FunctionParameter(Variable, Parameter):

    pass
class Object:

    pass
class FlatQVT_ReflectiveCollection(Object):

    def __init__(self):
        
    def add(self, object: Object) -> str:
        # TODO: Implement add method
        pass

    def size(self) -> str:
        # TODO: Implement size method
        pass

    def clear(self):
        # TODO: Implement clear method
        pass

    def addAll(self, objects: str) -> str:
        # TODO: Implement addAll method
        pass

    def remove(self, object: Object) -> str:
        # TODO: Implement remove method
        pass

class FlatQVT_Extent(Object):

    def __init__(self):
        
    def elements(self) -> str:
        # TODO: Implement elements method
        pass

    def useContainment(self) -> str:
        # TODO: Implement useContainment method
        pass

class FlatQVT_Element(Object):

    def __init__(self):
        
    def get(self, property: Property) -> Object:
        # TODO: Implement get method
        pass

    def getMetaClass(self) -> str:
        # TODO: Implement getMetaClass method
        pass

    def equals(self, object: Object) -> str:
        # TODO: Implement equals method
        pass

    def unset(self, property: Property):
        # TODO: Implement unset method
        pass

    def isSet(self, property: Property) -> str:
        # TODO: Implement isSet method
        pass

    def set(self, property: Property, object: Object):
        # TODO: Implement set method
        pass

    def container(self) -> Element:
        # TODO: Implement container method
        pass

class NamedElement:

    pass
class FlatQVT_Package(NamedElement):

    pass
class FlatQVT_TypedModel(NamedElement):

    pass
class FlatQVT_Rule(NamedElement):

    pass
class FlatQVT_TypedElement(NamedElement):

    pass
class FlatQVT_Type(NamedElement):

    def __init__(self):
        
    def isInstance(self, object: Object) -> str:
        # TODO: Implement isInstance method
        pass

class FlatQVT_EnumerationLiteral(NamedElement):

    pass
class FlatQVT_Domain(NamedElement):

    pass
class Property:

    pass
class FlatQVT_ContextualProperty(Property):

    pass
class OperationBody:

    pass
class FlatQVT_MappingBody(OperationBody):

    pass
class FlatQVT_ConstructorBody(OperationBody):

    pass
class ImperativeOperation:

    pass
class FlatQVT_Helper(ImperativeOperation):

    pass
class FlatQVT_MappingOperation(ImperativeOperation):

    pass
class FlatQVT_EntryOperation(ImperativeOperation):

    pass
class FlatQVT_Constructor(ImperativeOperation):

    pass
class Pattern:

    pass
class FlatQVT_DomainPattern(Pattern):

    pass
class FlatQVT_CorePattern(Pattern):

    pass
class Area:

    pass
class FlatQVT_Mapping(Rule, Area):

    pass
class Domain:

    pass
class FlatQVT_RelationDomain(Domain):

    pass
class FlatQVT_CoreDomain(Domain, Area):

    pass
class TemplateExp:

    pass
class FlatQVT_ObjectTemplateExp(TemplateExp):

    pass
class FlatQVT_CollectionTemplateExp(TemplateExp):

    pass
class TypedElement:

    pass
class FlatQVT_TupleLiteralPart(TypedElement):

    pass
class FlatQVT_ExpressionInOcl(TypedElement):

    pass
class FlatQVT_OclExpression(TypedElement):

    pass
class FlatQVT_Parameter(MultiplicityElement, TypedElement):

    pass
class FlatQVT_Operation(MultiplicityElement, TypedElement):

    pass
class FlatQVT_Property(MultiplicityElement, TypedElement):

    pass
class FlatQVT_Variable(TypedElement):

    pass
class FlatQVT_CollectionLiteralPart(TypedElement):

    pass
class LiteralExp:

    pass
class FlatQVT_PrimitiveLiteralExp(LiteralExp):

    pass
class FlatQVT_NullLiteralExp(LiteralExp):

    pass
class FlatQVT_TemplateExp(LiteralExp):

    pass
class FlatQVT_InvalidLiteralExp(LiteralExp):

    pass
class FlatQVT_DictLiteralExp(LiteralExp):

    pass
class FlatQVT_TupleLiteralExp(LiteralExp):

    pass
class FlatQVT_EnumLiteralExp(LiteralExp):

    pass
class FlatQVT_ListLiteralExp(LiteralExp):

    pass
class DataType:

    pass
class FlatQVT_TupleType(Class, DataType):

    pass
class FlatQVT_PrimitiveType(DataType):

    pass
class FlatQVT_Enumeration(DataType):

    pass
class FlatQVT_CollectionType(DataType):

    pass
class FlatQVT_CollectionLiteralExp(LiteralExp):

    pass
class CollectionLiteralPart:

    pass
class FlatQVT_CollectionRange(CollectionLiteralPart):

    pass
class FlatQVT_CollectionItem(CollectionLiteralPart):

    pass
class CorePattern:

    pass
class FlatQVT_GuardPattern(CorePattern):

    pass
class FlatQVT_BottomPattern(CorePattern):

    pass
class PrimitiveLiteralExp:

    pass
class FlatQVT_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class FlatQVT_StringLiteralExp(PrimitiveLiteralExp):

    pass
class FlatQVT_BooleanLiteralExp(PrimitiveLiteralExp):

    pass
class CollectionType:

    pass
class FlatQVT_OrderedSetType(CollectionType):

    pass
class FlatQVT_ListType(CollectionType):

    pass
class FlatQVT_SequenceType(CollectionType):

    pass
class FlatQVT_DictionaryType(CollectionType):

    pass
class FlatQVT_SetType(CollectionType):

    pass
class FlatQVT_BagType(CollectionType):

    pass
class OclExpression:

    pass
class FlatQVT_LiteralExp(OclExpression):

    pass
class FlatQVT_LoopExp(CallExp, OclExpression):

    pass
class FlatQVT_IfExp(OclExpression):

    pass
class FlatQVT_TypeExp(OclExpression):

    pass
class FlatQVT_LetExp(OclExpression):

    pass
class FlatQVT_RelationCallExp(OclExpression):

    pass
class FlatQVT_ImperativeExpression(OclExpression):

    pass
class FlatQVT_VariableExp(OclExpression):

    pass
class FlatQVT_CallExp(OclExpression):

    pass
class FlatQVT_Area(ABC):

    pass
class Type:

    pass
class FlatQVT_Class(Type):

    pass
class FlatQVT_VoidType(Type):

    pass
class FlatQVT_InvalidType(Type):

    pass
class FlatQVT_TemplateParameterType(Type):

    pass
class FlatQVT_DataType(Type):

    pass
class FlatQVT_AnyType(Type):

    pass
class Element:

    pass
class FlatQVT_DictLiteralPart(Element):

    pass
class FlatQVT_NamedElement(Element):

    pass
class FlatQVT_RelationImplementation(Element):

    pass
class FlatQVT_RelationDomainAssignment(Element):

    pass
class FlatQVT_ModuleImport(Element):

    pass
class FlatQVT_EnforcementOperation(Element):

    pass
class FlatQVT_Key(Element):

    pass
class FlatQVT_Comment(Element):

    pass
class FlatQVT_Tag(Element):

    pass
class FlatQVT_PropertyTemplateItem(Element):

    pass
class FlatQVT_Predicate(Element):

    pass
class FlatQVT_Factory(Element):

    def __init__(self):
        
    def convertToString(self, object: Object, dataType: DataType) -> str:
        # TODO: Implement convertToString method
        pass

    def create(self, metaClass: str) -> Element:
        # TODO: Implement create method
        pass

    def createFromString(self, string: str, dataType: DataType) -> Object:
        # TODO: Implement createFromString method
        pass

class FlatQVT_OperationBody(Element):

    pass
class FlatQVT_Pattern(Element):

    pass
class FlatQVT_Assignment(Element):

    pass
class ImperativeExpression:

    pass
class FlatQVT_ReturnExp(ImperativeExpression):

    pass
class FlatQVT_AssertExp(ImperativeExpression):

    pass
class FlatQVT_UnlinkExp(ImperativeExpression):

    pass
class FlatQVT_WhileExp(ImperativeExpression):

    pass
class FlatQVT_VariableInitExp(ImperativeExpression):

    pass
class FlatQVT_InstantiationExp(ImperativeExpression):

    pass
class FlatQVT_ContinueExp(ImperativeExpression):

    pass
class FlatQVT_ImperativeLoopExp(ImperativeExpression, LoopExp):

    pass
class FlatQVT_CatchExp(ImperativeExpression):

    pass
class FlatQVT_AssignExp(ImperativeExpression):

    pass
class FlatQVT_RaiseExp(ImperativeExpression):

    pass
class FlatQVT_ImperativeCallExp(ImperativeExpression, OperationCallExp):

    pass
class FlatQVT_LogExp(ImperativeExpression, OperationCallExp):

    pass
class FlatQVT_BreakExp(ImperativeExpression):

    pass
class FlatQVT_BlockExp(ImperativeExpression):

    pass
class FlatQVT_TryExp(ImperativeExpression):

    pass
class FlatQVT_SwitchExp(ImperativeExpression):

    pass
class FlatQVT_ComputeExp(ImperativeExpression):

    pass
class FlatQVT_ResolveExp(ImperativeExpression, CallExp):

    pass
class FlatQVT_AltExp(ImperativeExpression):

    pass