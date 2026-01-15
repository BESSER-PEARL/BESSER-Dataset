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
class DirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
class EnforcementMode(Enum):
    Creation = "Creation"
    Deletion = "Deletion"
class ImportKind(Enum):
    extension = "extension"
    access = "access"
class SeverityKind(Enum):
    error = "error"
    warning = "warning"
    fatal = "fatal"


############################################
# Definition of Classes
############################################

class ResolveExp:

    pass
class QVTOperational_ResolveInExp(ResolveExp):

    pass
class InstantiationExp:

    pass
class QVTOperational_ObjectExp(InstantiationExp):

    pass
class ImperativeCallExp:

    pass
class QVTOperational_MappingCallExp(ImperativeCallExp):

    pass
class VarParameter:

    pass
class QVTOperational_ModelParameter(VarParameter):

    pass
class QVTOperational_MappingParameter(VarParameter):

    pass
class Module:

    pass
class QVTOperational_OperationalTransformation(Module):

    pass
class QVTOperational_Library(Module):

    pass
class Property:

    pass
class QVTOperational_ContextualProperty(Property):

    pass
class OperationBody:

    pass
class QVTOperational_MappingBody(OperationBody):

    pass
class QVTOperational_ConstructorBody(OperationBody):

    pass
class ImperativeOperation:

    pass
class QVTOperational_Helper(ImperativeOperation):

    pass
class QVTOperational_EntryOperation(ImperativeOperation):

    pass
class QVTOperational_MappingOperation(ImperativeOperation):

    pass
class QVTOperational_Constructor(ImperativeOperation):

    pass
class OperationCallExp:

    pass
class ImperativeLoopExp:

    pass
class ImperativeOCL_ImperativeIterateExp(ImperativeLoopExp):

    pass
class ImperativeOCL_ForExp(ImperativeLoopExp):

    pass
class ImperativeExpression:

    pass
class ImperativeOCL_CatchExp(ImperativeExpression):

    pass
class ImperativeOCL_WhileExp(ImperativeExpression):

    pass
class ImperativeOCL_InstantiationExp(ImperativeExpression):

    pass
class ImperativeOCL_VariableInitExp(ImperativeExpression):

    pass
class ImperativeOCL_UnlinkExp(ImperativeExpression):

    pass
class ImperativeOCL_AssignExp(ImperativeExpression):

    pass
class ImperativeOCL_RaiseExp(ImperativeExpression):

    pass
class ImperativeOCL_AssertExp(ImperativeExpression):

    pass
class QVTOperational_ImperativeCallExp(OperationCallExp, ImperativeExpression):

    pass
class ImperativeOCL_BlockExp(ImperativeExpression):

    pass
class ImperativeOCL_TryExp(ImperativeExpression):

    pass
class ImperativeOCL_ContinueExp(ImperativeExpression):

    pass
class ImperativeOCL_LogExp(OperationCallExp, ImperativeExpression):

    pass
class ImperativeOCL_ReturnExp(ImperativeExpression):

    pass
class ImperativeOCL_ComputeExp(ImperativeExpression):

    pass
class ImperativeOCL_SwitchExp(ImperativeExpression):

    pass
class ImperativeOCL_BreakExp(ImperativeExpression):

    pass
class ImperativeOCL_AltExp(ImperativeExpression):

    pass
class Transformation:

    pass
class QVTRelation_RelationalTransformation(Transformation):

    pass
class PropertyCallExp:

    pass
class QVTRelation_OppositePropertyCallExp(PropertyCallExp):

    pass
class TemplateExp:

    pass
class QVTTemplate_ObjectTemplateExp(TemplateExp):

    pass
class QVTTemplate_CollectionTemplateExp(TemplateExp):

    pass
class Assignment:

    pass
class QVTCore_VariableAssignment(Assignment):

    pass
class QVTCore_PropertyAssignment(Assignment):

    pass
class Rule:

    pass
class QVTRelation_Relation(Rule):

    pass
class Pattern:

    pass
class QVTRelation_DomainPattern(Pattern):

    pass
class QVTCore_CorePattern(Pattern):

    pass
class Area:

    pass
class QVTCore_Mapping(Area, Rule):

    pass
class Domain:

    pass
class QVTRelation_RelationDomain(Domain):

    pass
class QVTCore_CoreDomain(Area, Domain):

    pass
class CorePattern:

    pass
class QVTCore_GuardPattern(CorePattern):

    pass
class QVTCore_BottomPattern(CorePattern):

    pass
class QVTCore_Area(ABC):

    pass
class Operation:

    pass
class QVTOperational_ImperativeOperation(Operation):

    pass
class QVTBase_Function(Operation):

    pass
class Package:

    pass
class Parameter:

    pass
class Variable:

    pass
class QVTCore_RealizedVariable(Variable):

    pass
class QVTOperational_VarParameter(Variable, Parameter):

    pass
class QVTBase_FunctionParameter(Variable, Parameter):

    pass
class Class:

    pass
class QVTOperational_Module(Package, Class):

    pass
class QVTOperational_ModelType(Class):

    pass
class QVTBase_Transformation(Package, Class):

    pass
class ImperativeOCL_Typedef(Class):

    pass
class NavigationCallExp:

    pass
class EssentialOCL_PropertyCallExp(NavigationCallExp):

    pass
class LoopExp:

    pass
class ImperativeOCL_ImperativeLoopExp(LoopExp, ImperativeExpression):

    pass
class EssentialOCL_IterateExp(LoopExp):

    pass
class FeatureCallExp:

    pass
class EssentialOCL_OperationCallExp(FeatureCallExp):

    pass
class EssentialOCL_NavigationCallExp(FeatureCallExp):

    pass
class EssentialOCL_IteratorExp(LoopExp):

    pass
class NumericLiteralExp:

    pass
class EssentialOCL_RealLiteralExp(NumericLiteralExp):

    pass
class EssentialOCL_UnlimitedNaturalExp(NumericLiteralExp):

    pass
class EssentialOCL_IntegerLiteralExp(NumericLiteralExp):

    pass
class CallExp:

    pass
class QVTOperational_ResolveExp(CallExp, ImperativeExpression):

    pass
class EssentialOCL_FeatureCallExp(CallExp):

    pass
class CollectionLiteralPart:

    pass
class EssentialOCL_CollectionItem(CollectionLiteralPart):

    pass
class EssentialOCL_CollectionRange(CollectionLiteralPart):

    pass
class LiteralExp:

    pass
class ImperativeOCL_ListLiteralExp(LiteralExp):

    pass
class EssentialOCL_EnumLiteralExp(LiteralExp):

    pass
class EssentialOCL_NullLiteralExp(LiteralExp):

    pass
class EssentialOCL_TupleLiteralExp(LiteralExp):

    pass
class EssentialOCL_PrimitiveLiteralExp(LiteralExp):

    pass
class EssentialOCL_InvalidLiteralExp(LiteralExp):

    pass
class QVTTemplate_TemplateExp(LiteralExp):

    pass
class ImperativeOCL_DictLiteralExp(LiteralExp):

    pass
class EssentialOCL_CollectionLiteralExp(LiteralExp):

    pass
class OclExpression:

    pass
class ImperativeOCL_ImperativeExpression(OclExpression):

    pass
class QVTRelation_RelationCallExp(OclExpression):

    pass
class EssentialOCL_LiteralExp(OclExpression):

    pass
class EssentialOCL_IfExp(OclExpression):

    pass
class EssentialOCL_VariableExp(OclExpression):

    pass
class EssentialOCL_LoopExp(OclExpression, CallExp):

    pass
class EssentialOCL_TypeExp(OclExpression):

    pass
class EssentialOCL_LetExp(OclExpression):

    pass
class EssentialOCL_CallExp(OclExpression):

    pass
class PrimitiveLiteralExp:

    pass
class EssentialOCL_StringLiteralExp(PrimitiveLiteralExp):

    pass
class EssentialOCL_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class EssentialOCL_BooleanLiteralExp(PrimitiveLiteralExp):

    pass
class CollectionType:

    pass
class EssentialOCL_OrderedSetType(CollectionType):

    pass
class EssentialOCL_SequenceType(CollectionType):

    pass
class ImperativeOCL_ListType(CollectionType):

    pass
class ImperativeOCL_DictionaryType(CollectionType):

    pass
class EssentialOCL_SetType(CollectionType):

    pass
class EssentialOCL_BagType(CollectionType):

    pass
class Extent:

    pass
class EMOF_URIExtent(Extent):

    def __init__(self):
        
    def uri(self, element: str) -> str:
        # TODO: Implement uri method
        pass

    def contextURI(self) -> str:
        # TODO: Implement contextURI method
        pass

    def element(self, uri: str) -> str:
        # TODO: Implement element method
        pass

class ReflectiveCollection:

    pass
class EMOF_ReflectiveSequence(ReflectiveCollection):

    def __init__(self):
        
    def remove(self, index: str) -> str:
        # TODO: Implement remove method
        pass

    def add(self, index: str, object: str):
        # TODO: Implement add method
        pass

    def get(self, index: str) -> str:
        # TODO: Implement get method
        pass

    def set(self, object: str, index: str) -> str:
        # TODO: Implement set method
        pass

class MultiplicityElement:

    pass
class TypedElement:

    pass
class EssentialOCL_TupleLiteralPart(TypedElement):

    pass
class EssentialOCL_OclExpression(TypedElement):

    pass
class EssentialOCL_Variable(TypedElement):

    pass
class EMOF_Parameter(MultiplicityElement, TypedElement):

    pass
class EssentialOCL_CollectionLiteralPart(TypedElement):

    pass
class EMOF_Property(MultiplicityElement, TypedElement):

    pass
class EssentialOCL_ExpressionInOcl(TypedElement):

    pass
class EMOF_Operation(MultiplicityElement, TypedElement):

    pass
class EMOF_Object:

    pass
class EMOF_MultiplicityElement(ABC):

    pass
class NamedElement:

    pass
class EMOF_Type(NamedElement):

    def __init__(self):
        
    def isInstance(self, object: str) -> str:
        # TODO: Implement isInstance method
        pass

class QVTBase_Domain(NamedElement):

    pass
class QVTBase_Rule(NamedElement):

    pass
class QVTBase_TypedModel(NamedElement):

    pass
class EMOF_TypedElement(NamedElement):

    pass
class EMOF_Package(NamedElement):

    pass
class EMOF_EnumerationLiteral(NamedElement):

    pass
class DataType:

    pass
class EMOF_PrimitiveType(DataType):

    pass
class EssentialOCL_TupleType(Class, DataType):

    pass
class EssentialOCL_CollectionType(DataType):

    pass
class EMOF_Enumeration(DataType):

    pass
class Type:

    pass
class EssentialOCL_TemplateParameterType(Type):

    pass
class EssentialOCL_AnyType(Type):

    pass
class EssentialOCL_InvalidType(Type):

    pass
class EssentialOCL_VoidType(Type):

    pass
class EMOF_Class(Type):

    pass
class Object:

    pass
class EMOF_ReflectiveCollection(Object):

    def __init__(self):
        
    def add(self, object: str) -> str:
        # TODO: Implement add method
        pass

    def addAll(self, objects: str) -> str:
        # TODO: Implement addAll method
        pass

    def size(self) -> str:
        # TODO: Implement size method
        pass

    def clear(self):
        # TODO: Implement clear method
        pass

    def remove(self, object: str) -> str:
        # TODO: Implement remove method
        pass

class EMOF_Extent(Object):

    def __init__(self):
        
    def elements(self) -> str:
        # TODO: Implement elements method
        pass

    def useContainment(self) -> str:
        # TODO: Implement useContainment method
        pass

class EMOF_Element(Object):

    def __init__(self):
        
    def getMetaClass(self) -> str:
        # TODO: Implement getMetaClass method
        pass

    def set(self, property: str, object: str):
        # TODO: Implement set method
        pass

    def isSet(self, property: str) -> str:
        # TODO: Implement isSet method
        pass

    def container(self) -> str:
        # TODO: Implement container method
        pass

    def get(self, property: str) -> str:
        # TODO: Implement get method
        pass

    def unset(self, property: str):
        # TODO: Implement unset method
        pass

    def equals(self, object: str) -> str:
        # TODO: Implement equals method
        pass

class EMOF_DataType(Type):

    pass
class Element:

    pass
class QVTRelation_RelationImplementation(Element):

    pass
class QVTCore_Assignment(Element):

    pass
class QVTRelation_Key(Element):

    pass
class EMOF_Factory(Element):

    def __init__(self):
        
    def createFromString(self, dataType: str, string: str) -> str:
        # TODO: Implement createFromString method
        pass

    def create(self, metaClass: str) -> str:
        # TODO: Implement create method
        pass

    def convertToString(self, object: str, dataType: str) -> str:
        # TODO: Implement convertToString method
        pass

class QVTBase_Pattern(Element):

    pass
class EMOF_Tag(Element):

    pass
class QVTBase_Predicate(Element):

    pass
class QVTOperational_OperationBody(Element):

    pass
class ImperativeOCL_DictLiteralPart(Element):

    pass
class QVTRelation_RelationDomainAssignment(Element):

    pass
class EMOF_NamedElement(Element):

    pass
class QVTTemplate_PropertyTemplateItem(Element):

    pass
class QVTCore_EnforcementOperation(Element):

    pass
class QVTOperational_ModuleImport(Element):

    pass
class EMOF_Comment(Element):

    pass