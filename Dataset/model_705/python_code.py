from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CollectionKind(Enum):
    Set = "Set"
    OrderedSet = "OrderedSet"
    Bag = "Bag"
    Sequence = "Sequence"
    Collection = "Collection"
class SeverityKind(Enum):
    error = "error"
    warning = "warning"
    fatal = "fatal"
class DirectionKind(Enum):
    in_ = "in_"
    inout = "inout"
    out = "out"
class ImportKind(Enum):
    extension = "extension"
    access = "access"
class EnforcementMode(Enum):
    Creation = "Creation"
    Deletion = "Deletion"


############################################
# Definition of Classes
############################################

class DataType:

    pass
class FlatQVT_CollectionType(DataType):

    pass
class TemplateExp:

    pass
class FlatQVT_CollectionTemplateExp(TemplateExp):

    pass
class TypedElement:

    pass
class FlatQVT_CollectionLiteralPart(TypedElement):

    pass
class LiteralExp:

    pass
class FlatQVT_CollectionLiteralExp(LiteralExp):

    pass
class CollectionLiteralPart:

    pass
class FlatQVT_CollectionRange(CollectionLiteralPart):

    pass
class FlatQVT_CollectionItem(CollectionLiteralPart):

    pass
class OclExpression:

    pass
class FlatQVT_CallExp(OclExpression):

    pass
class CorePattern:

    pass
class FlatQVT_BottomPattern(CorePattern):

    pass
class PrimitiveLiteralExp:

    pass
class FlatQVT_BooleanLiteralExp(PrimitiveLiteralExp):

    pass
class CollectionType:

    pass
class FlatQVT_BagType(CollectionType):

    pass
class Element:

    pass
class FlatQVT_Comment(Element):

    pass
class FlatQVT_Assignment(Element):

    pass
class FlatQVT_VariableExp(OclExpression):

    pass
class FlatQVT_Variable(TypedElement):

    pass
class Extent:

    pass
class FlatQVT_URIExtent(Extent):

    def __init__(self):
        
        pass
    def contextURI(self) :
        # TODO: Implement contextURI method
        pass

    def uri(self, FlatQVT_element) :
        # TODO: Implement uri method
        pass

    def element(self, FlatQVT_uri) :
        # TODO: Implement element method
        pass

class FlatQVT_TypeExp(OclExpression):

    pass
class FlatQVT_TupleLiteralPart(TypedElement):

    pass
class FlatQVT_TupleLiteralExp(LiteralExp):

    pass
class Transformation:

    pass
class FlatQVT_RelationalTransformation(Transformation):

    pass
class FlatQVT_TemplateExp(LiteralExp):

    pass
class FlatQVT_Tag(Element):

    pass
class FlatQVT_StringLiteralExp(PrimitiveLiteralExp):

    pass
class FlatQVT_SetType(CollectionType):

    pass
class FlatQVT_SequenceType(CollectionType):

    pass
class ResolveExp:

    pass
class FlatQVT_ResolveInExp(ResolveExp):

    pass
class FlatQVT_RelationImplementation(Element):

    pass
class FlatQVT_RelationDomainAssignment(Element):

    pass
class FlatQVT_RelationCallExp(OclExpression):

    pass
class ReflectiveCollection:

    pass
class FlatQVT_ReflectiveSequence(ReflectiveCollection):

    def __init__(self):
        
        pass
    def add(self, FlatQVT_index, FlatQVT_object):
        # TODO: Implement add method
        pass

    def set(self, FlatQVT_object, FlatQVT_index) :
        # TODO: Implement set method
        pass

    def remove(self, FlatQVT_index) :
        # TODO: Implement remove method
        pass

    def get(self, FlatQVT_index) :
        # TODO: Implement get method
        pass

class FlatQVT_OrderedSetType(CollectionType):

    pass
class FlatQVT_PropertyTemplateItem(Element):

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
class FlatQVT_PrimitiveType(DataType):

    pass
class FlatQVT_PrimitiveLiteralExp(LiteralExp):

    pass
class FlatQVT_Predicate(Element):

    pass
class FlatQVT_Pattern(Element):

    pass
class PropertyCallExp:

    pass
class FlatQVT_OppositePropertyCallExp(PropertyCallExp):

    pass
class FlatQVT_OperationBody(Element):

    pass
class MultiplicityElement:

    pass
class FlatQVT_Property(MultiplicityElement, TypedElement):

    pass
class FlatQVT_Parameter(MultiplicityElement, TypedElement):

    pass
class FlatQVT_Operation(MultiplicityElement, TypedElement):

    pass
class FlatQVT_OclExpression(TypedElement):

    pass
class FlatQVT_ObjectTemplateExp(TemplateExp):

    pass
class InstantiationExp:

    pass
class FlatQVT_ObjectExp(InstantiationExp):

    pass
class FlatQVT_Object:

    pass
class FlatQVT_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class FlatQVT_NullLiteralExp(LiteralExp):

    pass
class FeatureCallExp:

    pass
class FlatQVT_OperationCallExp(FeatureCallExp):

    pass
class FlatQVT_NavigationCallExp(FeatureCallExp):

    pass
class FlatQVT_NamedElement(Element):

    pass
class FlatQVT_MultiplicityElement(ABC):

    pass
class FlatQVT_ModuleImport(Element):

    pass
class Package:

    pass
class Class:

    pass
class FlatQVT_TupleType(DataType, Class):

    pass
class FlatQVT_Typedef(Class):

    pass
class FlatQVT_Module(Package, Class):

    pass
class FlatQVT_Transformation(Package, Class):

    pass
class FlatQVT_ModelType(Class):

    pass
class VarParameter:

    pass
class FlatQVT_ModelParameter(VarParameter):

    pass
class FlatQVT_MappingParameter(VarParameter):

    pass
class FlatQVT_InvalidLiteralExp(LiteralExp):

    pass
class ImperativeCallExp:

    pass
class FlatQVT_MappingCallExp(ImperativeCallExp):

    pass
class Rule:

    pass
class FlatQVT_Relation(Rule):

    pass
class FlatQVT_LiteralExp(OclExpression):

    pass
class FlatQVT_ListType(CollectionType):

    pass
class FlatQVT_ListLiteralExp(LiteralExp):

    pass
class Module:

    pass
class FlatQVT_OperationalTransformation(Module):

    pass
class FlatQVT_Library(Module):

    pass
class FlatQVT_LetExp(OclExpression):

    pass
class FlatQVT_Key(Element):

    pass
class NumericLiteralExp:

    pass
class FlatQVT_RealLiteralExp(NumericLiteralExp):

    pass
class FlatQVT_UnlimitedNaturalExp(NumericLiteralExp):

    pass
class FlatQVT_IntegerLiteralExp(NumericLiteralExp):

    pass
class LoopExp:

    pass
class FlatQVT_IterateExp(LoopExp):

    pass
class FlatQVT_IteratorExp(LoopExp):

    pass
class FlatQVT_ImperativeExpression(OclExpression):

    pass
class OperationCallExp:

    pass
class FlatQVT_IfExp(OclExpression):

    pass
class FlatQVT_GuardPattern(CorePattern):

    pass
class Parameter:

    pass
class Variable:

    pass
class FlatQVT_VarParameter(Parameter, Variable):

    pass
class FlatQVT_RealizedVariable(Variable):

    pass
class FlatQVT_FunctionParameter(Parameter, Variable):

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
class FlatQVT_LoopExp(OclExpression, CallExp):

    pass
class FlatQVT_FeatureCallExp(CallExp):

    pass
class FlatQVT_Factory(Element):

    def __init__(self):
        
        pass
    def convertToString(self, FlatQVT_dataType, FlatQVT_object) :
        # TODO: Implement convertToString method
        pass

    def createFromString(self, FlatQVT_string, FlatQVT_dataType) :
        # TODO: Implement createFromString method
        pass

    def create(self, FlatQVT_metaClass) :
        # TODO: Implement create method
        pass

class FlatQVT_ExpressionInOcl(TypedElement):

    pass
class FlatQVT_Enumeration(DataType):

    pass
class FlatQVT_EnumLiteralExp(LiteralExp):

    pass
class FlatQVT_EnforcementOperation(Element):

    pass
class Object:

    pass
class FlatQVT_Extent(Object):

    def __init__(self):
        
        pass
    def elements(self) :
        # TODO: Implement elements method
        pass

    def useContainment(self) :
        # TODO: Implement useContainment method
        pass

class FlatQVT_ReflectiveCollection(Object):

    def __init__(self):
        
        pass
    def add(self, FlatQVT_object) :
        # TODO: Implement add method
        pass

    def addAll(self, FlatQVT_objects) :
        # TODO: Implement addAll method
        pass

    def clear(self):
        # TODO: Implement clear method
        pass

    def remove(self, FlatQVT_object) :
        # TODO: Implement remove method
        pass

    def size(self) :
        # TODO: Implement size method
        pass

class FlatQVT_Element(Object):

    def __init__(self):
        
        pass
    def get(self, FlatQVT_property) :
        # TODO: Implement get method
        pass

    def isSet(self, FlatQVT_property) :
        # TODO: Implement isSet method
        pass

    def getMetaClass(self) :
        # TODO: Implement getMetaClass method
        pass

    def set(self, FlatQVT_property, FlatQVT_object):
        # TODO: Implement set method
        pass

    def unset(self, FlatQVT_property):
        # TODO: Implement unset method
        pass

    def container(self) :
        # TODO: Implement container method
        pass

    def equals(self, FlatQVT_object) :
        # TODO: Implement equals method
        pass

class NamedElement:

    pass
class FlatQVT_TypedElement(NamedElement):

    pass
class FlatQVT_TypedModel(NamedElement):

    pass
class FlatQVT_Type(NamedElement):

    def __init__(self):
        
        pass
    def isInstance(self, FlatQVT_object) :
        # TODO: Implement isInstance method
        pass

class FlatQVT_Rule(NamedElement):

    pass
class FlatQVT_Package(NamedElement):

    pass
class FlatQVT_EnumerationLiteral(NamedElement):

    pass
class FlatQVT_Domain(NamedElement):

    pass
class FlatQVT_DictionaryType(CollectionType):

    pass
class FlatQVT_DictLiteralPart(Element):

    pass
class FlatQVT_DictLiteralExp(LiteralExp):

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
class FlatQVT_CoreDomain(Area, Domain):

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
class FlatQVT_EntryOperation(ImperativeOperation):

    pass
class FlatQVT_MappingOperation(ImperativeOperation):

    pass
class FlatQVT_Constructor(ImperativeOperation):

    pass
class FlatQVT_Helper(ImperativeOperation):

    pass
class FlatQVT_Area(ABC):

    pass
class Type:

    pass
class FlatQVT_DataType(Type):

    pass
class FlatQVT_Class(Type):

    pass
class FlatQVT_InvalidType(Type):

    pass
class FlatQVT_VoidType(Type):

    pass
class FlatQVT_TemplateParameterType(Type):

    pass
class FlatQVT_AnyType(Type):

    pass
class ImperativeExpression:

    pass
class FlatQVT_BreakExp(ImperativeExpression):

    pass
class FlatQVT_AssignExp(ImperativeExpression):

    pass
class FlatQVT_BlockExp(ImperativeExpression):

    pass
class FlatQVT_ImperativeCallExp(OperationCallExp, ImperativeExpression):

    pass
class FlatQVT_SwitchExp(ImperativeExpression):

    pass
class FlatQVT_WhileExp(ImperativeExpression):

    pass
class FlatQVT_InstantiationExp(ImperativeExpression):

    pass
class FlatQVT_ComputeExp(ImperativeExpression):

    pass
class FlatQVT_CatchExp(ImperativeExpression):

    pass
class FlatQVT_AssertExp(ImperativeExpression):

    pass
class FlatQVT_VariableInitExp(ImperativeExpression):

    pass
class FlatQVT_TryExp(ImperativeExpression):

    pass
class FlatQVT_ReturnExp(ImperativeExpression):

    pass
class FlatQVT_LogExp(OperationCallExp, ImperativeExpression):

    pass
class FlatQVT_RaiseExp(ImperativeExpression):

    pass
class FlatQVT_ResolveExp(ImperativeExpression, CallExp):

    pass
class FlatQVT_UnlinkExp(ImperativeExpression):

    pass
class FlatQVT_ImperativeLoopExp(LoopExp, ImperativeExpression):

    pass
class FlatQVT_ContinueExp(ImperativeExpression):

    pass
class FlatQVT_AltExp(ImperativeExpression):

    pass