from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DirectionKind(Enum):
    out = "out"
    in_ = "in_"
    inout = "inout"
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
class ImportKind(Enum):
    extension = "extension"
    access = "access"
class EnforcementMode(Enum):
    Creation = "Creation"
    Deletion = "Deletion"


############################################
# Definition of Classes
############################################

class ResolveExp:

    pass
class QVTOperational_ResolveInExp(ResolveExp):

    pass
class VarParameter:

    pass
class QVTOperational_ModelParameter(VarParameter):

    pass
class QVTOperational_MappingParameter(VarParameter):

    pass
class InstantiationExp:

    pass
class QVTOperational_ObjectExp(InstantiationExp):

    pass
class Property:

    pass
class QVTOperational_ContextualProperty(Property):

    pass
class OperationBody:

    pass
class QVTOperational_ConstructorBody(OperationBody):

    pass
class ImperativeOperation:

    pass
class QVTOperational_Constructor(ImperativeOperation):

    pass
class QVTOperational_MappingOperation(ImperativeOperation):

    pass
class ImperativeCallExp:

    pass
class QVTOperational_MappingCallExp(ImperativeCallExp):

    pass
class QVTOperational_MappingBody(OperationBody):

    pass
class Module:

    pass
class QVTOperational_OperationalTransformation(Module):

    pass
class QVTOperational_Library(Module):

    pass
class QVTOperational_Helper(ImperativeOperation):

    pass
class QVTOperational_EntryOperation(ImperativeOperation):

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
class ImperativeOCL_LogExp(OperationCallExp, ImperativeExpression):

    pass
class ImperativeOCL_WhileExp(ImperativeExpression):

    pass
class ImperativeOCL_TryExp(ImperativeExpression):

    pass
class ImperativeOCL_RaiseExp(ImperativeExpression):

    pass
class ImperativeOCL_BreakExp(ImperativeExpression):

    pass
class ImperativeOCL_AssignExp(ImperativeExpression):

    pass
class QVTOperational_ImperativeCallExp(OperationCallExp, ImperativeExpression):

    pass
class ImperativeOCL_SwitchExp(ImperativeExpression):

    pass
class ImperativeOCL_BlockExp(ImperativeExpression):

    pass
class ImperativeOCL_UnlinkExp(ImperativeExpression):

    pass
class ImperativeOCL_InstantiationExp(ImperativeExpression):

    pass
class ImperativeOCL_VariableInitExp(ImperativeExpression):

    pass
class ImperativeOCL_AssertExp(ImperativeExpression):

    pass
class ImperativeOCL_ReturnExp(ImperativeExpression):

    pass
class ImperativeOCL_AltExp(ImperativeExpression):

    pass
class Transformation:

    pass
class QVTRelation_RelationalTransformation(Transformation):

    pass
class ImperativeOCL_ContinueExp(ImperativeExpression):

    pass
class ImperativeOCL_ComputeExp(ImperativeExpression):

    pass
class PropertyCallExp:

    pass
class QVTRelation_OppositePropertyCallExp(PropertyCallExp):

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
class TemplateExp:

    pass
class QVTTemplate_ObjectTemplateExp(TemplateExp):

    pass
class QVTTemplate_CollectionTemplateExp(TemplateExp):

    pass
class Package:

    pass
class Parameter:

    pass
class Area:

    pass
class QVTCore_Mapping(Rule, Area):

    pass
class Domain:

    pass
class QVTRelation_RelationDomain(Domain):

    pass
class QVTCore_CoreDomain(Domain, Area):

    pass
class CorePattern:

    pass
class QVTCore_GuardPattern(CorePattern):

    pass
class QVTCore_BottomPattern(CorePattern):

    pass
class QVTCore_Area(ABC):

    pass
class Variable:

    pass
class QVTCore_RealizedVariable(Variable):

    pass
class QVTOperational_VarParameter(Variable, Parameter):

    pass
class QVTBase_FunctionParameter(Variable, Parameter):

    pass
class Operation:

    pass
class QVTOperational_ImperativeOperation(Operation):

    pass
class QVTBase_Function(Operation):

    pass
class FeatureCallExp:

    pass
class EssentialOCL_OperationCallExp(FeatureCallExp):

    pass
class EssentialOCL_NavigationCallExp(FeatureCallExp):

    pass
class Class:

    pass
class ImperativeOCL_Typedef(Class):

    pass
class QVTOperational_Module(Package, Class):

    pass
class QVTBase_Transformation(Package, Class):

    pass
class QVTOperational_ModelType(Class):

    pass
class NavigationCallExp:

    pass
class EssentialOCL_PropertyCallExp(NavigationCallExp):

    pass
class LiteralExp:

    pass
class ImperativeOCL_ListLiteralExp(LiteralExp):

    pass
class EssentialOCL_PrimitiveLiteralExp(LiteralExp):

    pass
class QVTTemplate_TemplateExp(LiteralExp):

    pass
class EssentialOCL_NullLiteralExp(LiteralExp):

    pass
class EssentialOCL_EnumLiteralExp(LiteralExp):

    pass
class ImperativeOCL_DictLiteralExp(LiteralExp):

    pass
class EssentialOCL_TupleLiteralExp(LiteralExp):

    pass
class EssentialOCL_CollectionLiteralExp(LiteralExp):

    pass
class LoopExp:

    pass
class ImperativeOCL_ImperativeLoopExp(LoopExp, ImperativeExpression):

    pass
class EssentialOCL_IteratorExp(LoopExp):

    pass
class EssentialOCL_IterateExp(LoopExp):

    pass
class EssentialOCL_InvalidLiteralExp(LiteralExp):

    pass
class NumericLiteralExp:

    pass
class EssentialOCL_UnlimitedNaturalExp(NumericLiteralExp):

    pass
class EssentialOCL_RealLiteralExp(NumericLiteralExp):

    pass
class EssentialOCL_IntegerLiteralExp(NumericLiteralExp):

    pass
class CallExp:

    pass
class QVTOperational_ResolveExp(CallExp, ImperativeExpression):

    pass
class EssentialOCL_FeatureCallExp(CallExp):

    pass
class ReflectiveCollection:

    pass
class EMOF_ReflectiveSequence(ReflectiveCollection):

    def __init__(self):
        
        pass
    def get(self, EMOF_index) :
        # TODO: Implement get method
        pass

    def remove(self, EMOF_index) :
        # TODO: Implement remove method
        pass

    def set(self, EMOF_object, EMOF_index) :
        # TODO: Implement set method
        pass

    def add(self, EMOF_index, EMOF_object):
        # TODO: Implement add method
        pass

class CollectionLiteralPart:

    pass
class EssentialOCL_CollectionRange(CollectionLiteralPart):

    pass
class EssentialOCL_CollectionItem(CollectionLiteralPart):

    pass
class OclExpression:

    pass
class EssentialOCL_LiteralExp(OclExpression):

    pass
class QVTRelation_RelationCallExp(OclExpression):

    pass
class ImperativeOCL_ImperativeExpression(OclExpression):

    pass
class EssentialOCL_VariableExp(OclExpression):

    pass
class EssentialOCL_IfExp(OclExpression):

    pass
class EssentialOCL_LetExp(OclExpression):

    pass
class EssentialOCL_TypeExp(OclExpression):

    pass
class EssentialOCL_LoopExp(OclExpression, CallExp):

    pass
class EssentialOCL_CallExp(OclExpression):

    pass
class PrimitiveLiteralExp:

    pass
class EssentialOCL_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class EssentialOCL_StringLiteralExp(PrimitiveLiteralExp):

    pass
class EssentialOCL_BooleanLiteralExp(PrimitiveLiteralExp):

    pass
class CollectionType:

    pass
class ImperativeOCL_ListType(CollectionType):

    pass
class ImperativeOCL_DictionaryType(CollectionType):

    pass
class EssentialOCL_SetType(CollectionType):

    pass
class EssentialOCL_OrderedSetType(CollectionType):

    pass
class EssentialOCL_SequenceType(CollectionType):

    pass
class EssentialOCL_BagType(CollectionType):

    pass
class Extent:

    pass
class EMOF_URIExtent(Extent):

    def __init__(self):
        
        pass
    def contextURI(self) :
        # TODO: Implement contextURI method
        pass

    def uri(self, EMOF_element) :
        # TODO: Implement uri method
        pass

    def element(self, EMOF_uri) :
        # TODO: Implement element method
        pass

class EMOF_MultiplicityElement(ABC):

    pass
class NamedElement:

    pass
class QVTBase_Rule(NamedElement):

    pass
class EMOF_TypedElement(NamedElement):

    pass
class QVTBase_Domain(NamedElement):

    pass
class QVTBase_TypedModel(NamedElement):

    pass
class EMOF_Type(NamedElement):

    def __init__(self):
        
        pass
    def isInstance(self, EMOF_object) :
        # TODO: Implement isInstance method
        pass

class EMOF_EnumerationLiteral(NamedElement):

    pass
class DataType:

    pass
class EssentialOCL_TupleType(DataType, Class):

    pass
class EssentialOCL_CollectionType(DataType):

    pass
class EMOF_Enumeration(DataType):

    pass
class Object:

    pass
class EMOF_Extent(Object):

    def __init__(self):
        
        pass
    def elements(self) :
        # TODO: Implement elements method
        pass

    def useContainment(self) :
        # TODO: Implement useContainment method
        pass

class EMOF_ReflectiveCollection(Object):

    def __init__(self):
        
        pass
    def remove(self, EMOF_object) :
        # TODO: Implement remove method
        pass

    def addAll(self, EMOF_objects) :
        # TODO: Implement addAll method
        pass

    def clear(self):
        # TODO: Implement clear method
        pass

    def size(self) :
        # TODO: Implement size method
        pass

    def add(self, EMOF_object) :
        # TODO: Implement add method
        pass

class EMOF_Element(Object):

    def __init__(self):
        
        pass
    def equals(self, EMOF_object) :
        # TODO: Implement equals method
        pass

    def container(self) :
        # TODO: Implement container method
        pass

    def unset(self, EMOF_property):
        # TODO: Implement unset method
        pass

    def isSet(self, EMOF_property) :
        # TODO: Implement isSet method
        pass

    def set(self, EMOF_property, EMOF_object):
        # TODO: Implement set method
        pass

    def getMetaClass(self) :
        # TODO: Implement getMetaClass method
        pass

    def get(self, EMOF_property) :
        # TODO: Implement get method
        pass

class EMOF_PrimitiveType(DataType):

    pass
class Element:

    pass
class ImperativeOCL_DictLiteralPart(Element):

    pass
class QVTTemplate_PropertyTemplateItem(Element):

    pass
class QVTBase_Predicate(Element):

    pass
class EMOF_Factory(Element):

    def __init__(self):
        
        pass
    def create(self, EMOF_metaClass) :
        # TODO: Implement create method
        pass

    def convertToString(self, EMOF_object, EMOF_dataType) :
        # TODO: Implement convertToString method
        pass

    def createFromString(self, EMOF_string, EMOF_dataType) :
        # TODO: Implement createFromString method
        pass

class QVTCore_EnforcementOperation(Element):

    pass
class QVTCore_Assignment(Element):

    pass
class QVTOperational_ModuleImport(Element):

    pass
class QVTRelation_Key(Element):

    pass
class EMOF_NamedElement(Element):

    pass
class EMOF_Tag(Element):

    pass
class QVTRelation_RelationImplementation(Element):

    pass
class QVTRelation_RelationDomainAssignment(Element):

    pass
class QVTOperational_OperationBody(Element):

    pass
class QVTBase_Pattern(Element):

    pass
class EMOF_Comment(Element):

    pass
class EMOF_Package(NamedElement):

    pass
class Type:

    pass
class EssentialOCL_VoidType(Type):

    pass
class EssentialOCL_InvalidType(Type):

    pass
class EMOF_DataType(Type):

    pass
class EssentialOCL_TemplateParameterType(Type):

    pass
class EssentialOCL_AnyType(Type):

    pass
class MultiplicityElement:

    pass
class EMOF_Class(Type):

    pass
class TypedElement:

    pass
class EssentialOCL_TupleLiteralPart(TypedElement):

    pass
class EMOF_Property(TypedElement, MultiplicityElement):

    pass
class EMOF_Parameter(TypedElement, MultiplicityElement):

    pass
class EssentialOCL_Variable(TypedElement):

    pass
class EssentialOCL_ExpressionInOcl(TypedElement):

    pass
class EssentialOCL_CollectionLiteralPart(TypedElement):

    pass
class EssentialOCL_OclExpression(TypedElement):

    pass
class EMOF_Operation(TypedElement, MultiplicityElement):

    pass
class EMOF_Object:

    pass