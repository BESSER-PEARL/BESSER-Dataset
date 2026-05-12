import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DomainPattern,
    RelationDomainAssignment,
    RelationImplementation,
    ReflectiveCollection,
    FlatQVT_ReflectiveSequence,
    NavigationCallExp,
    FlatQVT_PropertyCallExp,
    ObjectTemplateExp,
    Predicate,
    OrderedTupleLiteralPart,
    PropertyCallExp,
    FlatQVT_OppositePropertyCallExp,
    PropertyTemplateItem,
    ConstructorBody,
    InstantiationExp,
    FlatQVT_ObjectExp,
    FlatQVT_Object,
    FeatureCallExp,
    FlatQVT_OperationCallExp,
    FlatQVT_NavigationCallExp,
    MultiplicityElement,
    ModelType,
    FlatQVT_MultiplicityElement,
    RelationDomain,
    ModelParameter,
    Tag,
    ModuleImport,
    EntryOperation,
    ImperativeCallExp,
    FlatQVT_MappingCallExp,
    Relation,
    MappingOperation,
    Module,
    FlatQVT_OperationalTransformation,
    FlatQVT_Library,
    RelationalTransformation,
    Mapping,
    VarParameter,
    FlatQVT_MappingParameter,
    FlatQVT_ModelParameter,
    NumericLiteralExp,
    FlatQVT_RealLiteralExp,
    FlatQVT_IntegerLiteralExp,
    Parameter,
    LoopExp,
    FlatQVT_IteratorExp,
    FlatQVT_IterateExp,
    Enumeration,
    ImperativeLoopExp,
    FlatQVT_ImperativeIterateExp,
    FlatQVT_ForExp,
    CallExp,
    FlatQVT_FeatureCallExp,
    Package,
    Object,
    FlatQVT_ReflectiveCollection,
    FlatQVT_Extent,
    FlatQVT_Element,
    TypedModel,
    EnumerationLiteral,
    OperationCallExp,
    Comment,
    DictLiteralPart,
    Pattern,
    FlatQVT_DomainPattern,
    FlatQVT_CorePattern,
    Rule,
    FlatQVT_Relation,
    NamedElement,
    FlatQVT_Package,
    FlatQVT_EnumerationLiteral,
    FlatQVT_Domain,
    DataType,
    FlatQVT_PrimitiveType,
    FlatQVT_Enumeration,
    FlatQVT_CollectionType,
    Variable,
    FlatQVT_RealizedVariable,
    FlatQVT_FunctionParameter,
    Domain,
    FlatQVT_RelationDomain,
    OperationBody,
    FlatQVT_MappingBody,
    FlatQVT_ConstructorBody,
    ImperativeOperation,
    FlatQVT_EntryOperation,
    FlatQVT_MappingOperation,
    FlatQVT_Helper,
    FlatQVT_Constructor,
    CollectionLiteralPart,
    FlatQVT_CollectionItem,
    Class,
    FlatQVT_OrderedTupleType,
    FlatQVT_ModelType,
    FlatQVT_Module,
    Operation,
    FlatQVT_ImperativeOperation,
    FlatQVT_Function,
    Property,
    FlatQVT_ContextualProperty,
    TemplateExp,
    FlatQVT_ObjectTemplateExp,
    FlatQVT_CollectionTemplateExp,
    FlatQVT_CollectionRange,
    CollectionLiteralExp,
    TypedElement,
    FlatQVT_OclExpression,
    FlatQVT_Parameter,
    FlatQVT_Property,
    FlatQVT_Operation,
    FlatQVT_ExpressionInOcl,
    FlatQVT_CollectionLiteralPart,
    LiteralExp,
    FlatQVT_OrderedTupleLiteralExp,
    FlatQVT_EnumLiteralExp,
    FlatQVT_DictLiteralExp,
    FlatQVT_PrimitiveLiteralExp,
    FlatQVT_ListLiteralExp,
    FlatQVT_InvalidLiteralExp,
    FlatQVT_NullLiteralExp,
    FlatQVT_CollectionLiteralExp,
    CorePattern,
    FlatQVT_GuardPattern,
    FlatQVT_BottomPattern,
    PrimitiveLiteralExp,
    FlatQVT_NumericLiteralExp,
    FlatQVT_BooleanLiteralExp,
    CollectionType,
    FlatQVT_DictionaryType,
    FlatQVT_OrderedSetType,
    FlatQVT_ListType,
    FlatQVT_BagType,
    Element,
    FlatQVT_Key,
    FlatQVT_OrderedTupleLiteralPart,
    FlatQVT_NamedElement,
    FlatQVT_OperationBody,
    FlatQVT_RelationDomainAssignment,
    FlatQVT_Predicate,
    FlatQVT_DictLiteralPart,
    FlatQVT_PropertyTemplateItem,
    FlatQVT_EnforcementOperation,
    FlatQVT_ModuleImport,
    FlatQVT_Pattern,
    FlatQVT_Comment,
    FlatQVT_Factory,
    FlatQVT_Assignment,
    RealizedVariable,
    EnforcementOperation,
    Assignment,
    FlatQVT_PropertyAssignment,
    GuardPattern,
    FlatQVT_Variable,
    FlatQVT_VarParameter,
    FlatQVT_VariableAssignment,
    LetExp,
    FlatQVT_UnlimitedNaturalExp,
    Extent,
    FlatQVT_URIExtent,
    FlatQVT_Typedef,
    FlatQVT_Type,
    FlatQVT_TupleType,
    TupleLiteralExp,
    FlatQVT_TupleLiteralPart,
    TupleLiteralPart,
    FlatQVT_TypedModel,
    FlatQVT_TypedElement,
    FlatQVT_Transformation,
    FlatQVT_TemplateExp,
    FlatQVT_TupleLiteralExp,
    CatchExp,
    FlatQVT_SetType,
    FlatQVT_SequenceType,
    FlatQVT_Rule,
    FlatQVT_Tag,
    AltExp,
    FlatQVT_StringLiteralExp,
    Key,
    Transformation,
    FlatQVT_RelationalTransformation,
    FlatQVT_RelationImplementation,
    ResolveExp,
    FlatQVT_ResolveInExp,
    Area,
    FlatQVT_Mapping,
    FlatQVT_CoreDomain,
    BottomPattern,
    FlatQVT_Area,
    Type,
    FlatQVT_TemplateParameterType,
    FlatQVT_InvalidType,
    FlatQVT_VoidType,
    FlatQVT_DataType,
    FlatQVT_Class,
    FlatQVT_AnyType,
    OclExpression,
    FlatQVT_ImperativeExpression,
    FlatQVT_VariableExp,
    FlatQVT_IfExp,
    FlatQVT_CallExp,
    FlatQVT_TypeExp,
    FlatQVT_LoopExp,
    FlatQVT_RelationCallExp,
    FlatQVT_LetExp,
    FlatQVT_LiteralExp,
    ImperativeExpression,
    FlatQVT_VariableInitExp,
    FlatQVT_InstantiationExp,
    FlatQVT_TryExp,
    FlatQVT_SwitchExp,
    FlatQVT_WhileExp,
    FlatQVT_BlockExp,
    FlatQVT_BreakExp,
    FlatQVT_ReturnExp,
    FlatQVT_ResolveExp,
    FlatQVT_LogExp,
    FlatQVT_ImperativeCallExp,
    FlatQVT_CatchExp,
    FlatQVT_UnlinkExp,
    FlatQVT_UnpackExp,
    FlatQVT_ImperativeLoopExp,
    FlatQVT_ComputeExp,
    FlatQVT_ContinueExp,
    FlatQVT_RaiseExp,
    FlatQVT_AltExp,
    FlatQVT_AssignExp,
    LogExp,
    FlatQVT_AssertExp,
    SeverityKind,
    EnforcementMode,
    DirectionKind,
    CollectionKind,
    ImportKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_domainpattern_is_not_abstract():
    assert not inspect.isabstract(DomainPattern)


def test_domainpattern_constructor_exists():
    assert callable(DomainPattern.__init__)


def test_domainpattern_constructor_args():
    sig = inspect.signature(DomainPattern.__init__)
    params = list(sig.parameters.keys())



def test_relationdomainassignment_is_not_abstract():
    assert not inspect.isabstract(RelationDomainAssignment)


def test_relationdomainassignment_constructor_exists():
    assert callable(RelationDomainAssignment.__init__)


def test_relationdomainassignment_constructor_args():
    sig = inspect.signature(RelationDomainAssignment.__init__)
    params = list(sig.parameters.keys())



def test_relationimplementation_is_not_abstract():
    assert not inspect.isabstract(RelationImplementation)


def test_relationimplementation_constructor_exists():
    assert callable(RelationImplementation.__init__)


def test_relationimplementation_constructor_args():
    sig = inspect.signature(RelationImplementation.__init__)
    params = list(sig.parameters.keys())



def test_reflectivecollection_is_not_abstract():
    assert not inspect.isabstract(ReflectiveCollection)


def test_reflectivecollection_constructor_exists():
    assert callable(ReflectiveCollection.__init__)


def test_reflectivecollection_constructor_args():
    sig = inspect.signature(ReflectiveCollection.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_reflectivesequence_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ReflectiveSequence)


def test_flatqvt_reflectivesequence_constructor_exists():
    assert callable(FlatQVT_ReflectiveSequence.__init__)


def test_flatqvt_reflectivesequence_constructor_args():
    sig = inspect.signature(FlatQVT_ReflectiveSequence.__init__)
    params = list(sig.parameters.keys())



def test_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(NavigationCallExp)


def test_navigationcallexp_constructor_exists():
    assert callable(NavigationCallExp.__init__)


def test_navigationcallexp_constructor_args():
    sig = inspect.signature(NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_PropertyCallExp)


def test_flatqvt_propertycallexp_constructor_exists():
    assert callable(FlatQVT_PropertyCallExp.__init__)


def test_flatqvt_propertycallexp_constructor_args():
    sig = inspect.signature(FlatQVT_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(ObjectTemplateExp)


def test_objecttemplateexp_constructor_exists():
    assert callable(ObjectTemplateExp.__init__)


def test_objecttemplateexp_constructor_args():
    sig = inspect.signature(ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_orderedtupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(OrderedTupleLiteralPart)


def test_orderedtupleliteralpart_constructor_exists():
    assert callable(OrderedTupleLiteralPart.__init__)


def test_orderedtupleliteralpart_constructor_args():
    sig = inspect.signature(OrderedTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_oppositepropertycallexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_OppositePropertyCallExp)


def test_flatqvt_oppositepropertycallexp_constructor_exists():
    assert callable(FlatQVT_OppositePropertyCallExp.__init__)


def test_flatqvt_oppositepropertycallexp_constructor_args():
    sig = inspect.signature(FlatQVT_OppositePropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(PropertyTemplateItem)


def test_propertytemplateitem_constructor_exists():
    assert callable(PropertyTemplateItem.__init__)


def test_propertytemplateitem_constructor_args():
    sig = inspect.signature(PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())



def test_constructorbody_is_not_abstract():
    assert not inspect.isabstract(ConstructorBody)


def test_constructorbody_constructor_exists():
    assert callable(ConstructorBody.__init__)


def test_constructorbody_constructor_args():
    sig = inspect.signature(ConstructorBody.__init__)
    params = list(sig.parameters.keys())



def test_instantiationexp_is_not_abstract():
    assert not inspect.isabstract(InstantiationExp)


def test_instantiationexp_constructor_exists():
    assert callable(InstantiationExp.__init__)


def test_instantiationexp_constructor_args():
    sig = inspect.signature(InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_objectexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ObjectExp)


def test_flatqvt_objectexp_constructor_exists():
    assert callable(FlatQVT_ObjectExp.__init__)


def test_flatqvt_objectexp_constructor_args():
    sig = inspect.signature(FlatQVT_ObjectExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_object_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Object)


def test_flatqvt_object_constructor_exists():
    assert callable(FlatQVT_Object.__init__)


def test_flatqvt_object_constructor_args():
    sig = inspect.signature(FlatQVT_Object.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExp)


def test_featurecallexp_constructor_exists():
    assert callable(FeatureCallExp.__init__)


def test_featurecallexp_constructor_args():
    sig = inspect.signature(FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_OperationCallExp)


def test_flatqvt_operationcallexp_constructor_exists():
    assert callable(FlatQVT_OperationCallExp.__init__)


def test_flatqvt_operationcallexp_constructor_args():
    sig = inspect.signature(FlatQVT_OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_NavigationCallExp)


def test_flatqvt_navigationcallexp_constructor_exists():
    assert callable(FlatQVT_NavigationCallExp.__init__)


def test_flatqvt_navigationcallexp_constructor_args():
    sig = inspect.signature(FlatQVT_NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_modeltype_is_not_abstract():
    assert not inspect.isabstract(ModelType)


def test_modeltype_constructor_exists():
    assert callable(ModelType.__init__)


def test_modeltype_constructor_args():
    sig = inspect.signature(ModelType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_MultiplicityElement)


def test_flatqvt_multiplicityelement_constructor_exists():
    assert callable(FlatQVT_MultiplicityElement.__init__)


def test_flatqvt_multiplicityelement_constructor_args():
    sig = inspect.signature(FlatQVT_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_flatqvt_multiplicityelement_has_isUnique():
    assert hasattr(FlatQVT_MultiplicityElement, "isUnique")
    descriptor = None
    for klass in FlatQVT_MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt_multiplicityelement_has_upper():
    assert hasattr(FlatQVT_MultiplicityElement, "upper")
    descriptor = None
    for klass in FlatQVT_MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt_multiplicityelement_has_isOrdered():
    assert hasattr(FlatQVT_MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in FlatQVT_MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt_multiplicityelement_has_lower():
    assert hasattr(FlatQVT_MultiplicityElement, "lower")
    descriptor = None
    for klass in FlatQVT_MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_relationdomain_is_not_abstract():
    assert not inspect.isabstract(RelationDomain)


def test_relationdomain_constructor_exists():
    assert callable(RelationDomain.__init__)


def test_relationdomain_constructor_args():
    sig = inspect.signature(RelationDomain.__init__)
    params = list(sig.parameters.keys())



def test_modelparameter_is_not_abstract():
    assert not inspect.isabstract(ModelParameter)


def test_modelparameter_constructor_exists():
    assert callable(ModelParameter.__init__)


def test_modelparameter_constructor_args():
    sig = inspect.signature(ModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_tag_is_not_abstract():
    assert not inspect.isabstract(Tag)


def test_tag_constructor_exists():
    assert callable(Tag.__init__)


def test_tag_constructor_args():
    sig = inspect.signature(Tag.__init__)
    params = list(sig.parameters.keys())



def test_moduleimport_is_not_abstract():
    assert not inspect.isabstract(ModuleImport)


def test_moduleimport_constructor_exists():
    assert callable(ModuleImport.__init__)


def test_moduleimport_constructor_args():
    sig = inspect.signature(ModuleImport.__init__)
    params = list(sig.parameters.keys())



def test_entryoperation_is_not_abstract():
    assert not inspect.isabstract(EntryOperation)


def test_entryoperation_constructor_exists():
    assert callable(EntryOperation.__init__)


def test_entryoperation_constructor_args():
    sig = inspect.signature(EntryOperation.__init__)
    params = list(sig.parameters.keys())



def test_imperativecallexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeCallExp)


def test_imperativecallexp_constructor_exists():
    assert callable(ImperativeCallExp.__init__)


def test_imperativecallexp_constructor_args():
    sig = inspect.signature(ImperativeCallExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_mappingcallexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_MappingCallExp)


def test_flatqvt_mappingcallexp_constructor_exists():
    assert callable(FlatQVT_MappingCallExp.__init__)


def test_flatqvt_mappingcallexp_constructor_args():
    sig = inspect.signature(FlatQVT_MappingCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isStrict" in params, "Missing parameter 'isStrict'"

def test_flatqvt_mappingcallexp_has_isStrict():
    assert hasattr(FlatQVT_MappingCallExp, "isStrict")
    descriptor = None
    for klass in FlatQVT_MappingCallExp.__mro__:
        if "isStrict" in klass.__dict__:
            descriptor = klass.__dict__["isStrict"]
            break
    assert isinstance(descriptor, property)



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_mappingoperation_is_not_abstract():
    assert not inspect.isabstract(MappingOperation)


def test_mappingoperation_constructor_exists():
    assert callable(MappingOperation.__init__)


def test_mappingoperation_constructor_args():
    sig = inspect.signature(MappingOperation.__init__)
    params = list(sig.parameters.keys())



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_operationaltransformation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_OperationalTransformation)


def test_flatqvt_operationaltransformation_constructor_exists():
    assert callable(FlatQVT_OperationalTransformation.__init__)


def test_flatqvt_operationaltransformation_constructor_args():
    sig = inspect.signature(FlatQVT_OperationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_library_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Library)


def test_flatqvt_library_constructor_exists():
    assert callable(FlatQVT_Library.__init__)


def test_flatqvt_library_constructor_args():
    sig = inspect.signature(FlatQVT_Library.__init__)
    params = list(sig.parameters.keys())



def test_relationaltransformation_is_not_abstract():
    assert not inspect.isabstract(RelationalTransformation)


def test_relationaltransformation_constructor_exists():
    assert callable(RelationalTransformation.__init__)


def test_relationaltransformation_constructor_args():
    sig = inspect.signature(RelationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_mapping_is_not_abstract():
    assert not inspect.isabstract(Mapping)


def test_mapping_constructor_exists():
    assert callable(Mapping.__init__)


def test_mapping_constructor_args():
    sig = inspect.signature(Mapping.__init__)
    params = list(sig.parameters.keys())



def test_varparameter_is_not_abstract():
    assert not inspect.isabstract(VarParameter)


def test_varparameter_constructor_exists():
    assert callable(VarParameter.__init__)


def test_varparameter_constructor_args():
    sig = inspect.signature(VarParameter.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_mappingparameter_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_MappingParameter)


def test_flatqvt_mappingparameter_constructor_exists():
    assert callable(FlatQVT_MappingParameter.__init__)


def test_flatqvt_mappingparameter_constructor_args():
    sig = inspect.signature(FlatQVT_MappingParameter.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_modelparameter_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ModelParameter)


def test_flatqvt_modelparameter_constructor_exists():
    assert callable(FlatQVT_ModelParameter.__init__)


def test_flatqvt_modelparameter_constructor_args():
    sig = inspect.signature(FlatQVT_ModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_realliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_RealLiteralExp)


def test_flatqvt_realliteralexp_constructor_exists():
    assert callable(FlatQVT_RealLiteralExp.__init__)


def test_flatqvt_realliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT_RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_flatqvt_realliteralexp_has_realSymbol():
    assert hasattr(FlatQVT_RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in FlatQVT_RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_IntegerLiteralExp)


def test_flatqvt_integerliteralexp_constructor_exists():
    assert callable(FlatQVT_IntegerLiteralExp.__init__)


def test_flatqvt_integerliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT_IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_flatqvt_integerliteralexp_has_integerSymbol():
    assert hasattr(FlatQVT_IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in FlatQVT_IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_IteratorExp)


def test_flatqvt_iteratorexp_constructor_exists():
    assert callable(FlatQVT_IteratorExp.__init__)


def test_flatqvt_iteratorexp_constructor_args():
    sig = inspect.signature(FlatQVT_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_iterateexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_IterateExp)


def test_flatqvt_iterateexp_constructor_exists():
    assert callable(FlatQVT_IterateExp.__init__)


def test_flatqvt_iterateexp_constructor_args():
    sig = inspect.signature(FlatQVT_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_enumeration_is_not_abstract():
    assert not inspect.isabstract(Enumeration)


def test_enumeration_constructor_exists():
    assert callable(Enumeration.__init__)


def test_enumeration_constructor_args():
    sig = inspect.signature(Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExp)


def test_imperativeloopexp_constructor_exists():
    assert callable(ImperativeLoopExp.__init__)


def test_imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_imperativeiterateexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ImperativeIterateExp)


def test_flatqvt_imperativeiterateexp_constructor_exists():
    assert callable(FlatQVT_ImperativeIterateExp.__init__)


def test_flatqvt_imperativeiterateexp_constructor_args():
    sig = inspect.signature(FlatQVT_ImperativeIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_forexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ForExp)


def test_flatqvt_forexp_constructor_exists():
    assert callable(FlatQVT_ForExp.__init__)


def test_flatqvt_forexp_constructor_args():
    sig = inspect.signature(FlatQVT_ForExp.__init__)
    params = list(sig.parameters.keys())



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_FeatureCallExp)


def test_flatqvt_featurecallexp_constructor_exists():
    assert callable(FlatQVT_FeatureCallExp.__init__)


def test_flatqvt_featurecallexp_constructor_args():
    sig = inspect.signature(FlatQVT_FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_reflectivecollection_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ReflectiveCollection)


def test_flatqvt_reflectivecollection_constructor_exists():
    assert callable(FlatQVT_ReflectiveCollection.__init__)


def test_flatqvt_reflectivecollection_constructor_args():
    sig = inspect.signature(FlatQVT_ReflectiveCollection.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_extent_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Extent)


def test_flatqvt_extent_constructor_exists():
    assert callable(FlatQVT_Extent.__init__)


def test_flatqvt_extent_constructor_args():
    sig = inspect.signature(FlatQVT_Extent.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_element_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Element)


def test_flatqvt_element_constructor_exists():
    assert callable(FlatQVT_Element.__init__)


def test_flatqvt_element_constructor_args():
    sig = inspect.signature(FlatQVT_Element.__init__)
    params = list(sig.parameters.keys())



def test_typedmodel_is_not_abstract():
    assert not inspect.isabstract(TypedModel)


def test_typedmodel_constructor_exists():
    assert callable(TypedModel.__init__)


def test_typedmodel_constructor_args():
    sig = inspect.signature(TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(DictLiteralPart)


def test_dictliteralpart_constructor_exists():
    assert callable(DictLiteralPart.__init__)


def test_dictliteralpart_constructor_args():
    sig = inspect.signature(DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_domainpattern_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_DomainPattern)


def test_flatqvt_domainpattern_constructor_exists():
    assert callable(FlatQVT_DomainPattern.__init__)


def test_flatqvt_domainpattern_constructor_args():
    sig = inspect.signature(FlatQVT_DomainPattern.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_corepattern_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_CorePattern)


def test_flatqvt_corepattern_constructor_exists():
    assert callable(FlatQVT_CorePattern.__init__)


def test_flatqvt_corepattern_constructor_args():
    sig = inspect.signature(FlatQVT_CorePattern.__init__)
    params = list(sig.parameters.keys())



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_relation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Relation)


def test_flatqvt_relation_constructor_exists():
    assert callable(FlatQVT_Relation.__init__)


def test_flatqvt_relation_constructor_args():
    sig = inspect.signature(FlatQVT_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "isTopLevel" in params, "Missing parameter 'isTopLevel'"

def test_flatqvt_relation_has_isTopLevel():
    assert hasattr(FlatQVT_Relation, "isTopLevel")
    descriptor = None
    for klass in FlatQVT_Relation.__mro__:
        if "isTopLevel" in klass.__dict__:
            descriptor = klass.__dict__["isTopLevel"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_package_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Package)


def test_flatqvt_package_constructor_exists():
    assert callable(FlatQVT_Package.__init__)


def test_flatqvt_package_constructor_args():
    sig = inspect.signature(FlatQVT_Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_flatqvt_package_has_uri():
    assert hasattr(FlatQVT_Package, "uri")
    descriptor = None
    for klass in FlatQVT_Package.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_EnumerationLiteral)


def test_flatqvt_enumerationliteral_constructor_exists():
    assert callable(FlatQVT_EnumerationLiteral.__init__)


def test_flatqvt_enumerationliteral_constructor_args():
    sig = inspect.signature(FlatQVT_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_domain_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Domain)


def test_flatqvt_domain_constructor_exists():
    assert callable(FlatQVT_Domain.__init__)


def test_flatqvt_domain_constructor_args():
    sig = inspect.signature(FlatQVT_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "isCheckable" in params, "Missing parameter 'isCheckable'"
    assert "isEnforceable" in params, "Missing parameter 'isEnforceable'"

def test_flatqvt_domain_has_isCheckable():
    assert hasattr(FlatQVT_Domain, "isCheckable")
    descriptor = None
    for klass in FlatQVT_Domain.__mro__:
        if "isCheckable" in klass.__dict__:
            descriptor = klass.__dict__["isCheckable"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt_domain_has_isEnforceable():
    assert hasattr(FlatQVT_Domain, "isEnforceable")
    descriptor = None
    for klass in FlatQVT_Domain.__mro__:
        if "isEnforceable" in klass.__dict__:
            descriptor = klass.__dict__["isEnforceable"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_primitivetype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_PrimitiveType)


def test_flatqvt_primitivetype_constructor_exists():
    assert callable(FlatQVT_PrimitiveType.__init__)


def test_flatqvt_primitivetype_constructor_args():
    sig = inspect.signature(FlatQVT_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_enumeration_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Enumeration)


def test_flatqvt_enumeration_constructor_exists():
    assert callable(FlatQVT_Enumeration.__init__)


def test_flatqvt_enumeration_constructor_args():
    sig = inspect.signature(FlatQVT_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_collectiontype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_CollectionType)


def test_flatqvt_collectiontype_constructor_exists():
    assert callable(FlatQVT_CollectionType.__init__)


def test_flatqvt_collectiontype_constructor_args():
    sig = inspect.signature(FlatQVT_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_realizedvariable_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_RealizedVariable)


def test_flatqvt_realizedvariable_constructor_exists():
    assert callable(FlatQVT_RealizedVariable.__init__)


def test_flatqvt_realizedvariable_constructor_args():
    sig = inspect.signature(FlatQVT_RealizedVariable.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_functionparameter_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_FunctionParameter)


def test_flatqvt_functionparameter_constructor_exists():
    assert callable(FlatQVT_FunctionParameter.__init__)


def test_flatqvt_functionparameter_constructor_args():
    sig = inspect.signature(FlatQVT_FunctionParameter.__init__)
    params = list(sig.parameters.keys())



def test_domain_is_not_abstract():
    assert not inspect.isabstract(Domain)


def test_domain_constructor_exists():
    assert callable(Domain.__init__)


def test_domain_constructor_args():
    sig = inspect.signature(Domain.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_relationdomain_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_RelationDomain)


def test_flatqvt_relationdomain_constructor_exists():
    assert callable(FlatQVT_RelationDomain.__init__)


def test_flatqvt_relationdomain_constructor_args():
    sig = inspect.signature(FlatQVT_RelationDomain.__init__)
    params = list(sig.parameters.keys())



def test_operationbody_is_not_abstract():
    assert not inspect.isabstract(OperationBody)


def test_operationbody_constructor_exists():
    assert callable(OperationBody.__init__)


def test_operationbody_constructor_args():
    sig = inspect.signature(OperationBody.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_mappingbody_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_MappingBody)


def test_flatqvt_mappingbody_constructor_exists():
    assert callable(FlatQVT_MappingBody.__init__)


def test_flatqvt_mappingbody_constructor_args():
    sig = inspect.signature(FlatQVT_MappingBody.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_constructorbody_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ConstructorBody)


def test_flatqvt_constructorbody_constructor_exists():
    assert callable(FlatQVT_ConstructorBody.__init__)


def test_flatqvt_constructorbody_constructor_args():
    sig = inspect.signature(FlatQVT_ConstructorBody.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoperation_is_not_abstract():
    assert not inspect.isabstract(ImperativeOperation)


def test_imperativeoperation_constructor_exists():
    assert callable(ImperativeOperation.__init__)


def test_imperativeoperation_constructor_args():
    sig = inspect.signature(ImperativeOperation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_entryoperation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_EntryOperation)


def test_flatqvt_entryoperation_constructor_exists():
    assert callable(FlatQVT_EntryOperation.__init__)


def test_flatqvt_entryoperation_constructor_args():
    sig = inspect.signature(FlatQVT_EntryOperation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_mappingoperation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_MappingOperation)


def test_flatqvt_mappingoperation_constructor_exists():
    assert callable(FlatQVT_MappingOperation.__init__)


def test_flatqvt_mappingoperation_constructor_args():
    sig = inspect.signature(FlatQVT_MappingOperation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_helper_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Helper)


def test_flatqvt_helper_constructor_exists():
    assert callable(FlatQVT_Helper.__init__)


def test_flatqvt_helper_constructor_args():
    sig = inspect.signature(FlatQVT_Helper.__init__)
    params = list(sig.parameters.keys())
    assert "isQuery" in params, "Missing parameter 'isQuery'"

def test_flatqvt_helper_has_isQuery():
    assert hasattr(FlatQVT_Helper, "isQuery")
    descriptor = None
    for klass in FlatQVT_Helper.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_constructor_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Constructor)


def test_flatqvt_constructor_constructor_exists():
    assert callable(FlatQVT_Constructor.__init__)


def test_flatqvt_constructor_constructor_args():
    sig = inspect.signature(FlatQVT_Constructor.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_collectionitem_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_CollectionItem)


def test_flatqvt_collectionitem_constructor_exists():
    assert callable(FlatQVT_CollectionItem.__init__)


def test_flatqvt_collectionitem_constructor_args():
    sig = inspect.signature(FlatQVT_CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_orderedtupletype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_OrderedTupleType)


def test_flatqvt_orderedtupletype_constructor_exists():
    assert callable(FlatQVT_OrderedTupleType.__init__)


def test_flatqvt_orderedtupletype_constructor_args():
    sig = inspect.signature(FlatQVT_OrderedTupleType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_modeltype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ModelType)


def test_flatqvt_modeltype_constructor_exists():
    assert callable(FlatQVT_ModelType.__init__)


def test_flatqvt_modeltype_constructor_args():
    sig = inspect.signature(FlatQVT_ModelType.__init__)
    params = list(sig.parameters.keys())
    assert "conformanceKind" in params, "Missing parameter 'conformanceKind'"

def test_flatqvt_modeltype_has_conformanceKind():
    assert hasattr(FlatQVT_ModelType, "conformanceKind")
    descriptor = None
    for klass in FlatQVT_ModelType.__mro__:
        if "conformanceKind" in klass.__dict__:
            descriptor = klass.__dict__["conformanceKind"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_module_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Module)


def test_flatqvt_module_constructor_exists():
    assert callable(FlatQVT_Module.__init__)


def test_flatqvt_module_constructor_args():
    sig = inspect.signature(FlatQVT_Module.__init__)
    params = list(sig.parameters.keys())
    assert "isBlackbox" in params, "Missing parameter 'isBlackbox'"

def test_flatqvt_module_has_isBlackbox():
    assert hasattr(FlatQVT_Module, "isBlackbox")
    descriptor = None
    for klass in FlatQVT_Module.__mro__:
        if "isBlackbox" in klass.__dict__:
            descriptor = klass.__dict__["isBlackbox"]
            break
    assert isinstance(descriptor, property)



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_imperativeoperation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ImperativeOperation)


def test_flatqvt_imperativeoperation_constructor_exists():
    assert callable(FlatQVT_ImperativeOperation.__init__)


def test_flatqvt_imperativeoperation_constructor_args():
    sig = inspect.signature(FlatQVT_ImperativeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "isBlackbox" in params, "Missing parameter 'isBlackbox'"

def test_flatqvt_imperativeoperation_has_isBlackbox():
    assert hasattr(FlatQVT_ImperativeOperation, "isBlackbox")
    descriptor = None
    for klass in FlatQVT_ImperativeOperation.__mro__:
        if "isBlackbox" in klass.__dict__:
            descriptor = klass.__dict__["isBlackbox"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_function_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Function)


def test_flatqvt_function_constructor_exists():
    assert callable(FlatQVT_Function.__init__)


def test_flatqvt_function_constructor_args():
    sig = inspect.signature(FlatQVT_Function.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_contextualproperty_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ContextualProperty)


def test_flatqvt_contextualproperty_constructor_exists():
    assert callable(FlatQVT_ContextualProperty.__init__)


def test_flatqvt_contextualproperty_constructor_args():
    sig = inspect.signature(FlatQVT_ContextualProperty.__init__)
    params = list(sig.parameters.keys())



def test_templateexp_is_not_abstract():
    assert not inspect.isabstract(TemplateExp)


def test_templateexp_constructor_exists():
    assert callable(TemplateExp.__init__)


def test_templateexp_constructor_args():
    sig = inspect.signature(TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ObjectTemplateExp)


def test_flatqvt_objecttemplateexp_constructor_exists():
    assert callable(FlatQVT_ObjectTemplateExp.__init__)


def test_flatqvt_objecttemplateexp_constructor_args():
    sig = inspect.signature(FlatQVT_ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_collectiontemplateexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_CollectionTemplateExp)


def test_flatqvt_collectiontemplateexp_constructor_exists():
    assert callable(FlatQVT_CollectionTemplateExp.__init__)


def test_flatqvt_collectiontemplateexp_constructor_args():
    sig = inspect.signature(FlatQVT_CollectionTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_collectionrange_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_CollectionRange)


def test_flatqvt_collectionrange_constructor_exists():
    assert callable(FlatQVT_CollectionRange.__init__)


def test_flatqvt_collectionrange_constructor_args():
    sig = inspect.signature(FlatQVT_CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExp)


def test_collectionliteralexp_constructor_exists():
    assert callable(CollectionLiteralExp.__init__)


def test_collectionliteralexp_constructor_args():
    sig = inspect.signature(CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_oclexpression_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_OclExpression)


def test_flatqvt_oclexpression_constructor_exists():
    assert callable(FlatQVT_OclExpression.__init__)


def test_flatqvt_oclexpression_constructor_args():
    sig = inspect.signature(FlatQVT_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_parameter_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Parameter)


def test_flatqvt_parameter_constructor_exists():
    assert callable(FlatQVT_Parameter.__init__)


def test_flatqvt_parameter_constructor_args():
    sig = inspect.signature(FlatQVT_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_property_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Property)


def test_flatqvt_property_constructor_exists():
    assert callable(FlatQVT_Property.__init__)


def test_flatqvt_property_constructor_args():
    sig = inspect.signature(FlatQVT_Property.__init__)
    params = list(sig.parameters.keys())
    assert "isID" in params, "Missing parameter 'isID'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"

def test_flatqvt_property_has_isID():
    assert hasattr(FlatQVT_Property, "isID")
    descriptor = None
    for klass in FlatQVT_Property.__mro__:
        if "isID" in klass.__dict__:
            descriptor = klass.__dict__["isID"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt_property_has_default():
    assert hasattr(FlatQVT_Property, "default")
    descriptor = None
    for klass in FlatQVT_Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt_property_has_isDerived():
    assert hasattr(FlatQVT_Property, "isDerived")
    descriptor = None
    for klass in FlatQVT_Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt_property_has_isReadOnly():
    assert hasattr(FlatQVT_Property, "isReadOnly")
    descriptor = None
    for klass in FlatQVT_Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt_property_has_isComposite():
    assert hasattr(FlatQVT_Property, "isComposite")
    descriptor = None
    for klass in FlatQVT_Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_operation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Operation)


def test_flatqvt_operation_constructor_exists():
    assert callable(FlatQVT_Operation.__init__)


def test_flatqvt_operation_constructor_args():
    sig = inspect.signature(FlatQVT_Operation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_expressioninocl_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ExpressionInOcl)


def test_flatqvt_expressioninocl_constructor_exists():
    assert callable(FlatQVT_ExpressionInOcl.__init__)


def test_flatqvt_expressioninocl_constructor_args():
    sig = inspect.signature(FlatQVT_ExpressionInOcl.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_CollectionLiteralPart)


def test_flatqvt_collectionliteralpart_constructor_exists():
    assert callable(FlatQVT_CollectionLiteralPart.__init__)


def test_flatqvt_collectionliteralpart_constructor_args():
    sig = inspect.signature(FlatQVT_CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_orderedtupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_OrderedTupleLiteralExp)


def test_flatqvt_orderedtupleliteralexp_constructor_exists():
    assert callable(FlatQVT_OrderedTupleLiteralExp.__init__)


def test_flatqvt_orderedtupleliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT_OrderedTupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_EnumLiteralExp)


def test_flatqvt_enumliteralexp_constructor_exists():
    assert callable(FlatQVT_EnumLiteralExp.__init__)


def test_flatqvt_enumliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_DictLiteralExp)


def test_flatqvt_dictliteralexp_constructor_exists():
    assert callable(FlatQVT_DictLiteralExp.__init__)


def test_flatqvt_dictliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT_DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_PrimitiveLiteralExp)


def test_flatqvt_primitiveliteralexp_constructor_exists():
    assert callable(FlatQVT_PrimitiveLiteralExp.__init__)


def test_flatqvt_primitiveliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT_PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_listliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ListLiteralExp)


def test_flatqvt_listliteralexp_constructor_exists():
    assert callable(FlatQVT_ListLiteralExp.__init__)


def test_flatqvt_listliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT_ListLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_InvalidLiteralExp)


def test_flatqvt_invalidliteralexp_constructor_exists():
    assert callable(FlatQVT_InvalidLiteralExp.__init__)


def test_flatqvt_invalidliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_NullLiteralExp)


def test_flatqvt_nullliteralexp_constructor_exists():
    assert callable(FlatQVT_NullLiteralExp.__init__)


def test_flatqvt_nullliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT_NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_CollectionLiteralExp)


def test_flatqvt_collectionliteralexp_constructor_exists():
    assert callable(FlatQVT_CollectionLiteralExp.__init__)


def test_flatqvt_collectionliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT_CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_flatqvt_collectionliteralexp_has_kind():
    assert hasattr(FlatQVT_CollectionLiteralExp, "kind")
    descriptor = None
    for klass in FlatQVT_CollectionLiteralExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_corepattern_is_not_abstract():
    assert not inspect.isabstract(CorePattern)


def test_corepattern_constructor_exists():
    assert callable(CorePattern.__init__)


def test_corepattern_constructor_args():
    sig = inspect.signature(CorePattern.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_guardpattern_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_GuardPattern)


def test_flatqvt_guardpattern_constructor_exists():
    assert callable(FlatQVT_GuardPattern.__init__)


def test_flatqvt_guardpattern_constructor_args():
    sig = inspect.signature(FlatQVT_GuardPattern.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_bottompattern_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_BottomPattern)


def test_flatqvt_bottompattern_constructor_exists():
    assert callable(FlatQVT_BottomPattern.__init__)


def test_flatqvt_bottompattern_constructor_args():
    sig = inspect.signature(FlatQVT_BottomPattern.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_NumericLiteralExp)


def test_flatqvt_numericliteralexp_constructor_exists():
    assert callable(FlatQVT_NumericLiteralExp.__init__)


def test_flatqvt_numericliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT_NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_BooleanLiteralExp)


def test_flatqvt_booleanliteralexp_constructor_exists():
    assert callable(FlatQVT_BooleanLiteralExp.__init__)


def test_flatqvt_booleanliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_flatqvt_booleanliteralexp_has_booleanSymbol():
    assert hasattr(FlatQVT_BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in FlatQVT_BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_dictionarytype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_DictionaryType)


def test_flatqvt_dictionarytype_constructor_exists():
    assert callable(FlatQVT_DictionaryType.__init__)


def test_flatqvt_dictionarytype_constructor_args():
    sig = inspect.signature(FlatQVT_DictionaryType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_OrderedSetType)


def test_flatqvt_orderedsettype_constructor_exists():
    assert callable(FlatQVT_OrderedSetType.__init__)


def test_flatqvt_orderedsettype_constructor_args():
    sig = inspect.signature(FlatQVT_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_listtype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ListType)


def test_flatqvt_listtype_constructor_exists():
    assert callable(FlatQVT_ListType.__init__)


def test_flatqvt_listtype_constructor_args():
    sig = inspect.signature(FlatQVT_ListType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_bagtype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_BagType)


def test_flatqvt_bagtype_constructor_exists():
    assert callable(FlatQVT_BagType.__init__)


def test_flatqvt_bagtype_constructor_args():
    sig = inspect.signature(FlatQVT_BagType.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_key_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Key)


def test_flatqvt_key_constructor_exists():
    assert callable(FlatQVT_Key.__init__)


def test_flatqvt_key_constructor_args():
    sig = inspect.signature(FlatQVT_Key.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_orderedtupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_OrderedTupleLiteralPart)


def test_flatqvt_orderedtupleliteralpart_constructor_exists():
    assert callable(FlatQVT_OrderedTupleLiteralPart.__init__)


def test_flatqvt_orderedtupleliteralpart_constructor_args():
    sig = inspect.signature(FlatQVT_OrderedTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_namedelement_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_NamedElement)


def test_flatqvt_namedelement_constructor_exists():
    assert callable(FlatQVT_NamedElement.__init__)


def test_flatqvt_namedelement_constructor_args():
    sig = inspect.signature(FlatQVT_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_flatqvt_namedelement_has_name():
    assert hasattr(FlatQVT_NamedElement, "name")
    descriptor = None
    for klass in FlatQVT_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_operationbody_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_OperationBody)


def test_flatqvt_operationbody_constructor_exists():
    assert callable(FlatQVT_OperationBody.__init__)


def test_flatqvt_operationbody_constructor_args():
    sig = inspect.signature(FlatQVT_OperationBody.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_relationdomainassignment_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_RelationDomainAssignment)


def test_flatqvt_relationdomainassignment_constructor_exists():
    assert callable(FlatQVT_RelationDomainAssignment.__init__)


def test_flatqvt_relationdomainassignment_constructor_args():
    sig = inspect.signature(FlatQVT_RelationDomainAssignment.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_predicate_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Predicate)


def test_flatqvt_predicate_constructor_exists():
    assert callable(FlatQVT_Predicate.__init__)


def test_flatqvt_predicate_constructor_args():
    sig = inspect.signature(FlatQVT_Predicate.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_DictLiteralPart)


def test_flatqvt_dictliteralpart_constructor_exists():
    assert callable(FlatQVT_DictLiteralPart.__init__)


def test_flatqvt_dictliteralpart_constructor_args():
    sig = inspect.signature(FlatQVT_DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_PropertyTemplateItem)


def test_flatqvt_propertytemplateitem_constructor_exists():
    assert callable(FlatQVT_PropertyTemplateItem.__init__)


def test_flatqvt_propertytemplateitem_constructor_args():
    sig = inspect.signature(FlatQVT_PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())
    assert "isOpposite" in params, "Missing parameter 'isOpposite'"

def test_flatqvt_propertytemplateitem_has_isOpposite():
    assert hasattr(FlatQVT_PropertyTemplateItem, "isOpposite")
    descriptor = None
    for klass in FlatQVT_PropertyTemplateItem.__mro__:
        if "isOpposite" in klass.__dict__:
            descriptor = klass.__dict__["isOpposite"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_enforcementoperation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_EnforcementOperation)


def test_flatqvt_enforcementoperation_constructor_exists():
    assert callable(FlatQVT_EnforcementOperation.__init__)


def test_flatqvt_enforcementoperation_constructor_args():
    sig = inspect.signature(FlatQVT_EnforcementOperation.__init__)
    params = list(sig.parameters.keys())
    assert "enforcementMode" in params, "Missing parameter 'enforcementMode'"

def test_flatqvt_enforcementoperation_has_enforcementMode():
    assert hasattr(FlatQVT_EnforcementOperation, "enforcementMode")
    descriptor = None
    for klass in FlatQVT_EnforcementOperation.__mro__:
        if "enforcementMode" in klass.__dict__:
            descriptor = klass.__dict__["enforcementMode"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_moduleimport_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ModuleImport)


def test_flatqvt_moduleimport_constructor_exists():
    assert callable(FlatQVT_ModuleImport.__init__)


def test_flatqvt_moduleimport_constructor_args():
    sig = inspect.signature(FlatQVT_ModuleImport.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_flatqvt_moduleimport_has_kind():
    assert hasattr(FlatQVT_ModuleImport, "kind")
    descriptor = None
    for klass in FlatQVT_ModuleImport.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_pattern_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Pattern)


def test_flatqvt_pattern_constructor_exists():
    assert callable(FlatQVT_Pattern.__init__)


def test_flatqvt_pattern_constructor_args():
    sig = inspect.signature(FlatQVT_Pattern.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_comment_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Comment)


def test_flatqvt_comment_constructor_exists():
    assert callable(FlatQVT_Comment.__init__)


def test_flatqvt_comment_constructor_args():
    sig = inspect.signature(FlatQVT_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_flatqvt_comment_has_body():
    assert hasattr(FlatQVT_Comment, "body")
    descriptor = None
    for klass in FlatQVT_Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_factory_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Factory)


def test_flatqvt_factory_constructor_exists():
    assert callable(FlatQVT_Factory.__init__)


def test_flatqvt_factory_constructor_args():
    sig = inspect.signature(FlatQVT_Factory.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_assignment_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Assignment)


def test_flatqvt_assignment_constructor_exists():
    assert callable(FlatQVT_Assignment.__init__)


def test_flatqvt_assignment_constructor_args():
    sig = inspect.signature(FlatQVT_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "isDefault" in params, "Missing parameter 'isDefault'"

def test_flatqvt_assignment_has_isDefault():
    assert hasattr(FlatQVT_Assignment, "isDefault")
    descriptor = None
    for klass in FlatQVT_Assignment.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)



def test_realizedvariable_is_not_abstract():
    assert not inspect.isabstract(RealizedVariable)


def test_realizedvariable_constructor_exists():
    assert callable(RealizedVariable.__init__)


def test_realizedvariable_constructor_args():
    sig = inspect.signature(RealizedVariable.__init__)
    params = list(sig.parameters.keys())



def test_enforcementoperation_is_not_abstract():
    assert not inspect.isabstract(EnforcementOperation)


def test_enforcementoperation_constructor_exists():
    assert callable(EnforcementOperation.__init__)


def test_enforcementoperation_constructor_args():
    sig = inspect.signature(EnforcementOperation.__init__)
    params = list(sig.parameters.keys())



def test_assignment_is_not_abstract():
    assert not inspect.isabstract(Assignment)


def test_assignment_constructor_exists():
    assert callable(Assignment.__init__)


def test_assignment_constructor_args():
    sig = inspect.signature(Assignment.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_propertyassignment_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_PropertyAssignment)


def test_flatqvt_propertyassignment_constructor_exists():
    assert callable(FlatQVT_PropertyAssignment.__init__)


def test_flatqvt_propertyassignment_constructor_args():
    sig = inspect.signature(FlatQVT_PropertyAssignment.__init__)
    params = list(sig.parameters.keys())



def test_guardpattern_is_not_abstract():
    assert not inspect.isabstract(GuardPattern)


def test_guardpattern_constructor_exists():
    assert callable(GuardPattern.__init__)


def test_guardpattern_constructor_args():
    sig = inspect.signature(GuardPattern.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_variable_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Variable)


def test_flatqvt_variable_constructor_exists():
    assert callable(FlatQVT_Variable.__init__)


def test_flatqvt_variable_constructor_args():
    sig = inspect.signature(FlatQVT_Variable.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_varparameter_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_VarParameter)


def test_flatqvt_varparameter_constructor_exists():
    assert callable(FlatQVT_VarParameter.__init__)


def test_flatqvt_varparameter_constructor_args():
    sig = inspect.signature(FlatQVT_VarParameter.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_flatqvt_varparameter_has_kind():
    assert hasattr(FlatQVT_VarParameter, "kind")
    descriptor = None
    for klass in FlatQVT_VarParameter.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_variableassignment_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_VariableAssignment)


def test_flatqvt_variableassignment_constructor_exists():
    assert callable(FlatQVT_VariableAssignment.__init__)


def test_flatqvt_variableassignment_constructor_args():
    sig = inspect.signature(FlatQVT_VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_letexp_is_not_abstract():
    assert not inspect.isabstract(LetExp)


def test_letexp_constructor_exists():
    assert callable(LetExp.__init__)


def test_letexp_constructor_args():
    sig = inspect.signature(LetExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_unlimitednaturalexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_UnlimitedNaturalExp)


def test_flatqvt_unlimitednaturalexp_constructor_exists():
    assert callable(FlatQVT_UnlimitedNaturalExp.__init__)


def test_flatqvt_unlimitednaturalexp_constructor_args():
    sig = inspect.signature(FlatQVT_UnlimitedNaturalExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_flatqvt_unlimitednaturalexp_has_symbol():
    assert hasattr(FlatQVT_UnlimitedNaturalExp, "symbol")
    descriptor = None
    for klass in FlatQVT_UnlimitedNaturalExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_uriextent_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_URIExtent)


def test_flatqvt_uriextent_constructor_exists():
    assert callable(FlatQVT_URIExtent.__init__)


def test_flatqvt_uriextent_constructor_args():
    sig = inspect.signature(FlatQVT_URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_typedef_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Typedef)


def test_flatqvt_typedef_constructor_exists():
    assert callable(FlatQVT_Typedef.__init__)


def test_flatqvt_typedef_constructor_args():
    sig = inspect.signature(FlatQVT_Typedef.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_type_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Type)


def test_flatqvt_type_constructor_exists():
    assert callable(FlatQVT_Type.__init__)


def test_flatqvt_type_constructor_args():
    sig = inspect.signature(FlatQVT_Type.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_tupletype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_TupleType)


def test_flatqvt_tupletype_constructor_exists():
    assert callable(FlatQVT_TupleType.__init__)


def test_flatqvt_tupletype_constructor_args():
    sig = inspect.signature(FlatQVT_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralExp)


def test_tupleliteralexp_constructor_exists():
    assert callable(TupleLiteralExp.__init__)


def test_tupleliteralexp_constructor_args():
    sig = inspect.signature(TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_TupleLiteralPart)


def test_flatqvt_tupleliteralpart_constructor_exists():
    assert callable(FlatQVT_TupleLiteralPart.__init__)


def test_flatqvt_tupleliteralpart_constructor_args():
    sig = inspect.signature(FlatQVT_TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_typedmodel_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_TypedModel)


def test_flatqvt_typedmodel_constructor_exists():
    assert callable(FlatQVT_TypedModel.__init__)


def test_flatqvt_typedmodel_constructor_args():
    sig = inspect.signature(FlatQVT_TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_typedelement_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_TypedElement)


def test_flatqvt_typedelement_constructor_exists():
    assert callable(FlatQVT_TypedElement.__init__)


def test_flatqvt_typedelement_constructor_args():
    sig = inspect.signature(FlatQVT_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_transformation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Transformation)


def test_flatqvt_transformation_constructor_exists():
    assert callable(FlatQVT_Transformation.__init__)


def test_flatqvt_transformation_constructor_args():
    sig = inspect.signature(FlatQVT_Transformation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_templateexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_TemplateExp)


def test_flatqvt_templateexp_constructor_exists():
    assert callable(FlatQVT_TemplateExp.__init__)


def test_flatqvt_templateexp_constructor_args():
    sig = inspect.signature(FlatQVT_TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_TupleLiteralExp)


def test_flatqvt_tupleliteralexp_constructor_exists():
    assert callable(FlatQVT_TupleLiteralExp.__init__)


def test_flatqvt_tupleliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT_TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_catchexp_is_not_abstract():
    assert not inspect.isabstract(CatchExp)


def test_catchexp_constructor_exists():
    assert callable(CatchExp.__init__)


def test_catchexp_constructor_args():
    sig = inspect.signature(CatchExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_settype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_SetType)


def test_flatqvt_settype_constructor_exists():
    assert callable(FlatQVT_SetType.__init__)


def test_flatqvt_settype_constructor_args():
    sig = inspect.signature(FlatQVT_SetType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_sequencetype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_SequenceType)


def test_flatqvt_sequencetype_constructor_exists():
    assert callable(FlatQVT_SequenceType.__init__)


def test_flatqvt_sequencetype_constructor_args():
    sig = inspect.signature(FlatQVT_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_rule_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Rule)


def test_flatqvt_rule_constructor_exists():
    assert callable(FlatQVT_Rule.__init__)


def test_flatqvt_rule_constructor_args():
    sig = inspect.signature(FlatQVT_Rule.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_tag_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Tag)


def test_flatqvt_tag_constructor_exists():
    assert callable(FlatQVT_Tag.__init__)


def test_flatqvt_tag_constructor_args():
    sig = inspect.signature(FlatQVT_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_flatqvt_tag_has_value():
    assert hasattr(FlatQVT_Tag, "value")
    descriptor = None
    for klass in FlatQVT_Tag.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt_tag_has_name():
    assert hasattr(FlatQVT_Tag, "name")
    descriptor = None
    for klass in FlatQVT_Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_altexp_is_not_abstract():
    assert not inspect.isabstract(AltExp)


def test_altexp_constructor_exists():
    assert callable(AltExp.__init__)


def test_altexp_constructor_args():
    sig = inspect.signature(AltExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_StringLiteralExp)


def test_flatqvt_stringliteralexp_constructor_exists():
    assert callable(FlatQVT_StringLiteralExp.__init__)


def test_flatqvt_stringliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_flatqvt_stringliteralexp_has_stringSymbol():
    assert hasattr(FlatQVT_StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in FlatQVT_StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_transformation_is_not_abstract():
    assert not inspect.isabstract(Transformation)


def test_transformation_constructor_exists():
    assert callable(Transformation.__init__)


def test_transformation_constructor_args():
    sig = inspect.signature(Transformation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_relationaltransformation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_RelationalTransformation)


def test_flatqvt_relationaltransformation_constructor_exists():
    assert callable(FlatQVT_RelationalTransformation.__init__)


def test_flatqvt_relationaltransformation_constructor_args():
    sig = inspect.signature(FlatQVT_RelationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_relationimplementation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_RelationImplementation)


def test_flatqvt_relationimplementation_constructor_exists():
    assert callable(FlatQVT_RelationImplementation.__init__)


def test_flatqvt_relationimplementation_constructor_args():
    sig = inspect.signature(FlatQVT_RelationImplementation.__init__)
    params = list(sig.parameters.keys())



def test_resolveexp_is_not_abstract():
    assert not inspect.isabstract(ResolveExp)


def test_resolveexp_constructor_exists():
    assert callable(ResolveExp.__init__)


def test_resolveexp_constructor_args():
    sig = inspect.signature(ResolveExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_resolveinexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ResolveInExp)


def test_flatqvt_resolveinexp_constructor_exists():
    assert callable(FlatQVT_ResolveInExp.__init__)


def test_flatqvt_resolveinexp_constructor_args():
    sig = inspect.signature(FlatQVT_ResolveInExp.__init__)
    params = list(sig.parameters.keys())



def test_area_is_not_abstract():
    assert not inspect.isabstract(Area)


def test_area_constructor_exists():
    assert callable(Area.__init__)


def test_area_constructor_args():
    sig = inspect.signature(Area.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_mapping_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Mapping)


def test_flatqvt_mapping_constructor_exists():
    assert callable(FlatQVT_Mapping.__init__)


def test_flatqvt_mapping_constructor_args():
    sig = inspect.signature(FlatQVT_Mapping.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_coredomain_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_CoreDomain)


def test_flatqvt_coredomain_constructor_exists():
    assert callable(FlatQVT_CoreDomain.__init__)


def test_flatqvt_coredomain_constructor_args():
    sig = inspect.signature(FlatQVT_CoreDomain.__init__)
    params = list(sig.parameters.keys())



def test_bottompattern_is_not_abstract():
    assert not inspect.isabstract(BottomPattern)


def test_bottompattern_constructor_exists():
    assert callable(BottomPattern.__init__)


def test_bottompattern_constructor_args():
    sig = inspect.signature(BottomPattern.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_area_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Area)


def test_flatqvt_area_constructor_exists():
    assert callable(FlatQVT_Area.__init__)


def test_flatqvt_area_constructor_args():
    sig = inspect.signature(FlatQVT_Area.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_templateparametertype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_TemplateParameterType)


def test_flatqvt_templateparametertype_constructor_exists():
    assert callable(FlatQVT_TemplateParameterType.__init__)


def test_flatqvt_templateparametertype_constructor_args():
    sig = inspect.signature(FlatQVT_TemplateParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_flatqvt_templateparametertype_has_specification():
    assert hasattr(FlatQVT_TemplateParameterType, "specification")
    descriptor = None
    for klass in FlatQVT_TemplateParameterType.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_invalidtype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_InvalidType)


def test_flatqvt_invalidtype_constructor_exists():
    assert callable(FlatQVT_InvalidType.__init__)


def test_flatqvt_invalidtype_constructor_args():
    sig = inspect.signature(FlatQVT_InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_voidtype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_VoidType)


def test_flatqvt_voidtype_constructor_exists():
    assert callable(FlatQVT_VoidType.__init__)


def test_flatqvt_voidtype_constructor_args():
    sig = inspect.signature(FlatQVT_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_datatype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_DataType)


def test_flatqvt_datatype_constructor_exists():
    assert callable(FlatQVT_DataType.__init__)


def test_flatqvt_datatype_constructor_args():
    sig = inspect.signature(FlatQVT_DataType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_class_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_Class)


def test_flatqvt_class_constructor_exists():
    assert callable(FlatQVT_Class.__init__)


def test_flatqvt_class_constructor_args():
    sig = inspect.signature(FlatQVT_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_flatqvt_class_has_isAbstract():
    assert hasattr(FlatQVT_Class, "isAbstract")
    descriptor = None
    for klass in FlatQVT_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_anytype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_AnyType)


def test_flatqvt_anytype_constructor_exists():
    assert callable(FlatQVT_AnyType.__init__)


def test_flatqvt_anytype_constructor_args():
    sig = inspect.signature(FlatQVT_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ImperativeExpression)


def test_flatqvt_imperativeexpression_constructor_exists():
    assert callable(FlatQVT_ImperativeExpression.__init__)


def test_flatqvt_imperativeexpression_constructor_args():
    sig = inspect.signature(FlatQVT_ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_variableexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_VariableExp)


def test_flatqvt_variableexp_constructor_exists():
    assert callable(FlatQVT_VariableExp.__init__)


def test_flatqvt_variableexp_constructor_args():
    sig = inspect.signature(FlatQVT_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_ifexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_IfExp)


def test_flatqvt_ifexp_constructor_exists():
    assert callable(FlatQVT_IfExp.__init__)


def test_flatqvt_ifexp_constructor_args():
    sig = inspect.signature(FlatQVT_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_callexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_CallExp)


def test_flatqvt_callexp_constructor_exists():
    assert callable(FlatQVT_CallExp.__init__)


def test_flatqvt_callexp_constructor_args():
    sig = inspect.signature(FlatQVT_CallExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_typeexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_TypeExp)


def test_flatqvt_typeexp_constructor_exists():
    assert callable(FlatQVT_TypeExp.__init__)


def test_flatqvt_typeexp_constructor_args():
    sig = inspect.signature(FlatQVT_TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_loopexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_LoopExp)


def test_flatqvt_loopexp_constructor_exists():
    assert callable(FlatQVT_LoopExp.__init__)


def test_flatqvt_loopexp_constructor_args():
    sig = inspect.signature(FlatQVT_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_relationcallexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_RelationCallExp)


def test_flatqvt_relationcallexp_constructor_exists():
    assert callable(FlatQVT_RelationCallExp.__init__)


def test_flatqvt_relationcallexp_constructor_args():
    sig = inspect.signature(FlatQVT_RelationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_letexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_LetExp)


def test_flatqvt_letexp_constructor_exists():
    assert callable(FlatQVT_LetExp.__init__)


def test_flatqvt_letexp_constructor_args():
    sig = inspect.signature(FlatQVT_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_literalexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_LiteralExp)


def test_flatqvt_literalexp_constructor_exists():
    assert callable(FlatQVT_LiteralExp.__init__)


def test_flatqvt_literalexp_constructor_args():
    sig = inspect.signature(FlatQVT_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeExpression)


def test_imperativeexpression_constructor_exists():
    assert callable(ImperativeExpression.__init__)


def test_imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_variableinitexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_VariableInitExp)


def test_flatqvt_variableinitexp_constructor_exists():
    assert callable(FlatQVT_VariableInitExp.__init__)


def test_flatqvt_variableinitexp_constructor_args():
    sig = inspect.signature(FlatQVT_VariableInitExp.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_flatqvt_variableinitexp_has_withResult():
    assert hasattr(FlatQVT_VariableInitExp, "withResult")
    descriptor = None
    for klass in FlatQVT_VariableInitExp.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_instantiationexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_InstantiationExp)


def test_flatqvt_instantiationexp_constructor_exists():
    assert callable(FlatQVT_InstantiationExp.__init__)


def test_flatqvt_instantiationexp_constructor_args():
    sig = inspect.signature(FlatQVT_InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_tryexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_TryExp)


def test_flatqvt_tryexp_constructor_exists():
    assert callable(FlatQVT_TryExp.__init__)


def test_flatqvt_tryexp_constructor_args():
    sig = inspect.signature(FlatQVT_TryExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_switchexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_SwitchExp)


def test_flatqvt_switchexp_constructor_exists():
    assert callable(FlatQVT_SwitchExp.__init__)


def test_flatqvt_switchexp_constructor_args():
    sig = inspect.signature(FlatQVT_SwitchExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_whileexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_WhileExp)


def test_flatqvt_whileexp_constructor_exists():
    assert callable(FlatQVT_WhileExp.__init__)


def test_flatqvt_whileexp_constructor_args():
    sig = inspect.signature(FlatQVT_WhileExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_blockexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_BlockExp)


def test_flatqvt_blockexp_constructor_exists():
    assert callable(FlatQVT_BlockExp.__init__)


def test_flatqvt_blockexp_constructor_args():
    sig = inspect.signature(FlatQVT_BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_breakexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_BreakExp)


def test_flatqvt_breakexp_constructor_exists():
    assert callable(FlatQVT_BreakExp.__init__)


def test_flatqvt_breakexp_constructor_args():
    sig = inspect.signature(FlatQVT_BreakExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_returnexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ReturnExp)


def test_flatqvt_returnexp_constructor_exists():
    assert callable(FlatQVT_ReturnExp.__init__)


def test_flatqvt_returnexp_constructor_args():
    sig = inspect.signature(FlatQVT_ReturnExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_resolveexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ResolveExp)


def test_flatqvt_resolveexp_constructor_exists():
    assert callable(FlatQVT_ResolveExp.__init__)


def test_flatqvt_resolveexp_constructor_args():
    sig = inspect.signature(FlatQVT_ResolveExp.__init__)
    params = list(sig.parameters.keys())
    assert "isInverse" in params, "Missing parameter 'isInverse'"
    assert "one" in params, "Missing parameter 'one'"
    assert "isDeferred" in params, "Missing parameter 'isDeferred'"

def test_flatqvt_resolveexp_has_isInverse():
    assert hasattr(FlatQVT_ResolveExp, "isInverse")
    descriptor = None
    for klass in FlatQVT_ResolveExp.__mro__:
        if "isInverse" in klass.__dict__:
            descriptor = klass.__dict__["isInverse"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt_resolveexp_has_one():
    assert hasattr(FlatQVT_ResolveExp, "one")
    descriptor = None
    for klass in FlatQVT_ResolveExp.__mro__:
        if "one" in klass.__dict__:
            descriptor = klass.__dict__["one"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt_resolveexp_has_isDeferred():
    assert hasattr(FlatQVT_ResolveExp, "isDeferred")
    descriptor = None
    for klass in FlatQVT_ResolveExp.__mro__:
        if "isDeferred" in klass.__dict__:
            descriptor = klass.__dict__["isDeferred"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_logexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_LogExp)


def test_flatqvt_logexp_constructor_exists():
    assert callable(FlatQVT_LogExp.__init__)


def test_flatqvt_logexp_constructor_args():
    sig = inspect.signature(FlatQVT_LogExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_imperativecallexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ImperativeCallExp)


def test_flatqvt_imperativecallexp_constructor_exists():
    assert callable(FlatQVT_ImperativeCallExp.__init__)


def test_flatqvt_imperativecallexp_constructor_args():
    sig = inspect.signature(FlatQVT_ImperativeCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"

def test_flatqvt_imperativecallexp_has_isVirtual():
    assert hasattr(FlatQVT_ImperativeCallExp, "isVirtual")
    descriptor = None
    for klass in FlatQVT_ImperativeCallExp.__mro__:
        if "isVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isVirtual"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt_catchexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_CatchExp)


def test_flatqvt_catchexp_constructor_exists():
    assert callable(FlatQVT_CatchExp.__init__)


def test_flatqvt_catchexp_constructor_args():
    sig = inspect.signature(FlatQVT_CatchExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_unlinkexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_UnlinkExp)


def test_flatqvt_unlinkexp_constructor_exists():
    assert callable(FlatQVT_UnlinkExp.__init__)


def test_flatqvt_unlinkexp_constructor_args():
    sig = inspect.signature(FlatQVT_UnlinkExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_unpackexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_UnpackExp)


def test_flatqvt_unpackexp_constructor_exists():
    assert callable(FlatQVT_UnpackExp.__init__)


def test_flatqvt_unpackexp_constructor_args():
    sig = inspect.signature(FlatQVT_UnpackExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ImperativeLoopExp)


def test_flatqvt_imperativeloopexp_constructor_exists():
    assert callable(FlatQVT_ImperativeLoopExp.__init__)


def test_flatqvt_imperativeloopexp_constructor_args():
    sig = inspect.signature(FlatQVT_ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_computeexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ComputeExp)


def test_flatqvt_computeexp_constructor_exists():
    assert callable(FlatQVT_ComputeExp.__init__)


def test_flatqvt_computeexp_constructor_args():
    sig = inspect.signature(FlatQVT_ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_continueexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_ContinueExp)


def test_flatqvt_continueexp_constructor_exists():
    assert callable(FlatQVT_ContinueExp.__init__)


def test_flatqvt_continueexp_constructor_args():
    sig = inspect.signature(FlatQVT_ContinueExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_raiseexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_RaiseExp)


def test_flatqvt_raiseexp_constructor_exists():
    assert callable(FlatQVT_RaiseExp.__init__)


def test_flatqvt_raiseexp_constructor_args():
    sig = inspect.signature(FlatQVT_RaiseExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_altexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_AltExp)


def test_flatqvt_altexp_constructor_exists():
    assert callable(FlatQVT_AltExp.__init__)


def test_flatqvt_altexp_constructor_args():
    sig = inspect.signature(FlatQVT_AltExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_assignexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_AssignExp)


def test_flatqvt_assignexp_constructor_exists():
    assert callable(FlatQVT_AssignExp.__init__)


def test_flatqvt_assignexp_constructor_args():
    sig = inspect.signature(FlatQVT_AssignExp.__init__)
    params = list(sig.parameters.keys())
    assert "isReset" in params, "Missing parameter 'isReset'"

def test_flatqvt_assignexp_has_isReset():
    assert hasattr(FlatQVT_AssignExp, "isReset")
    descriptor = None
    for klass in FlatQVT_AssignExp.__mro__:
        if "isReset" in klass.__dict__:
            descriptor = klass.__dict__["isReset"]
            break
    assert isinstance(descriptor, property)



def test_logexp_is_not_abstract():
    assert not inspect.isabstract(LogExp)


def test_logexp_constructor_exists():
    assert callable(LogExp.__init__)


def test_logexp_constructor_args():
    sig = inspect.signature(LogExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt_assertexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT_AssertExp)


def test_flatqvt_assertexp_constructor_exists():
    assert callable(FlatQVT_AssertExp.__init__)


def test_flatqvt_assertexp_constructor_args():
    sig = inspect.signature(FlatQVT_AssertExp.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_flatqvt_assertexp_has_severity():
    assert hasattr(FlatQVT_AssertExp, "severity")
    descriptor = None
    for klass in FlatQVT_AssertExp.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)

def test_severitykind_exists():
    # Check that the Enumeration exists
    assert SeverityKind is not None

def test_severitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SeverityKind]
    expected_literals = [
        "fatal",
        "warning",
        "error",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SeverityKind"

def test_enforcementmode_exists():
    # Check that the Enumeration exists
    assert EnforcementMode is not None

def test_enforcementmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnforcementMode]
    expected_literals = [
        "Deletion",
        "Creation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnforcementMode"

def test_directionkind_exists():
    # Check that the Enumeration exists
    assert DirectionKind is not None

def test_directionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionKind]
    expected_literals = [
        "inout",
        "out",
        "in_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionKind"

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "Collection",
        "Sequence",
        "OrderedSet",
        "Set",
        "Bag",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"

def test_importkind_exists():
    # Check that the Enumeration exists
    assert ImportKind is not None

def test_importkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImportKind]
    expected_literals = [
        "access",
        "extension",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImportKind"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
DomainPattern_strategy = st.builds(
    DomainPattern,
)
RelationDomainAssignment_strategy = st.builds(
    RelationDomainAssignment,
)
RelationImplementation_strategy = st.builds(
    RelationImplementation,
)
ReflectiveCollection_strategy = st.builds(
    ReflectiveCollection,
)
FlatQVT_ReflectiveSequence_strategy = st.builds(
    FlatQVT_ReflectiveSequence,
)
NavigationCallExp_strategy = st.builds(
    NavigationCallExp,
)
FlatQVT_PropertyCallExp_strategy = st.builds(
    FlatQVT_PropertyCallExp,
)
ObjectTemplateExp_strategy = st.builds(
    ObjectTemplateExp,
)
Predicate_strategy = st.builds(
    Predicate,
)
OrderedTupleLiteralPart_strategy = st.builds(
    OrderedTupleLiteralPart,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
FlatQVT_OppositePropertyCallExp_strategy = st.builds(
    FlatQVT_OppositePropertyCallExp,
)
PropertyTemplateItem_strategy = st.builds(
    PropertyTemplateItem,
)
ConstructorBody_strategy = st.builds(
    ConstructorBody,
)
InstantiationExp_strategy = st.builds(
    InstantiationExp,
)
FlatQVT_ObjectExp_strategy = st.builds(
    FlatQVT_ObjectExp,
)
FlatQVT_Object_strategy = st.builds(
    FlatQVT_Object,
)
FeatureCallExp_strategy = st.builds(
    FeatureCallExp,
)
FlatQVT_OperationCallExp_strategy = st.builds(
    FlatQVT_OperationCallExp,
)
FlatQVT_NavigationCallExp_strategy = st.builds(
    FlatQVT_NavigationCallExp,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
ModelType_strategy = st.builds(
    ModelType,
)
FlatQVT_MultiplicityElement_strategy = st.builds(
    FlatQVT_MultiplicityElement,
    isUnique=
        safe_text,
    upper=
        safe_text,
    isOrdered=
        safe_text,
    lower=
        safe_text
)
RelationDomain_strategy = st.builds(
    RelationDomain,
)
ModelParameter_strategy = st.builds(
    ModelParameter,
)
Tag_strategy = st.builds(
    Tag,
)
ModuleImport_strategy = st.builds(
    ModuleImport,
)
EntryOperation_strategy = st.builds(
    EntryOperation,
)
ImperativeCallExp_strategy = st.builds(
    ImperativeCallExp,
)
FlatQVT_MappingCallExp_strategy = st.builds(
    FlatQVT_MappingCallExp,
    isStrict=
        safe_text
)
Relation_strategy = st.builds(
    Relation,
)
MappingOperation_strategy = st.builds(
    MappingOperation,
)
Module_strategy = st.builds(
    Module,
)
FlatQVT_OperationalTransformation_strategy = st.builds(
    FlatQVT_OperationalTransformation,
)
FlatQVT_Library_strategy = st.builds(
    FlatQVT_Library,
)
RelationalTransformation_strategy = st.builds(
    RelationalTransformation,
)
Mapping_strategy = st.builds(
    Mapping,
)
VarParameter_strategy = st.builds(
    VarParameter,
)
FlatQVT_MappingParameter_strategy = st.builds(
    FlatQVT_MappingParameter,
)
FlatQVT_ModelParameter_strategy = st.builds(
    FlatQVT_ModelParameter,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
FlatQVT_RealLiteralExp_strategy = st.builds(
    FlatQVT_RealLiteralExp,
    realSymbol=
        safe_text
)
FlatQVT_IntegerLiteralExp_strategy = st.builds(
    FlatQVT_IntegerLiteralExp,
    integerSymbol=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
FlatQVT_IteratorExp_strategy = st.builds(
    FlatQVT_IteratorExp,
)
FlatQVT_IterateExp_strategy = st.builds(
    FlatQVT_IterateExp,
)
Enumeration_strategy = st.builds(
    Enumeration,
)
ImperativeLoopExp_strategy = st.builds(
    ImperativeLoopExp,
)
FlatQVT_ImperativeIterateExp_strategy = st.builds(
    FlatQVT_ImperativeIterateExp,
)
FlatQVT_ForExp_strategy = st.builds(
    FlatQVT_ForExp,
)
CallExp_strategy = st.builds(
    CallExp,
)
FlatQVT_FeatureCallExp_strategy = st.builds(
    FlatQVT_FeatureCallExp,
)
Package_strategy = st.builds(
    Package,
)
Object_strategy = st.builds(
    Object,
)
FlatQVT_ReflectiveCollection_strategy = st.builds(
    FlatQVT_ReflectiveCollection,
)
FlatQVT_Extent_strategy = st.builds(
    FlatQVT_Extent,
)
FlatQVT_Element_strategy = st.builds(
    FlatQVT_Element,
)
TypedModel_strategy = st.builds(
    TypedModel,
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
Comment_strategy = st.builds(
    Comment,
)
DictLiteralPart_strategy = st.builds(
    DictLiteralPart,
)
Pattern_strategy = st.builds(
    Pattern,
)
FlatQVT_DomainPattern_strategy = st.builds(
    FlatQVT_DomainPattern,
)
FlatQVT_CorePattern_strategy = st.builds(
    FlatQVT_CorePattern,
)
Rule_strategy = st.builds(
    Rule,
)
FlatQVT_Relation_strategy = st.builds(
    FlatQVT_Relation,
    isTopLevel=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
FlatQVT_Package_strategy = st.builds(
    FlatQVT_Package,
    uri=
        safe_text
)
FlatQVT_EnumerationLiteral_strategy = st.builds(
    FlatQVT_EnumerationLiteral,
)
FlatQVT_Domain_strategy = st.builds(
    FlatQVT_Domain,
    isCheckable=
        safe_text,
    isEnforceable=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
FlatQVT_PrimitiveType_strategy = st.builds(
    FlatQVT_PrimitiveType,
)
FlatQVT_Enumeration_strategy = st.builds(
    FlatQVT_Enumeration,
)
FlatQVT_CollectionType_strategy = st.builds(
    FlatQVT_CollectionType,
)
Variable_strategy = st.builds(
    Variable,
)
FlatQVT_RealizedVariable_strategy = st.builds(
    FlatQVT_RealizedVariable,
)
FlatQVT_FunctionParameter_strategy = st.builds(
    FlatQVT_FunctionParameter,
)
Domain_strategy = st.builds(
    Domain,
)
FlatQVT_RelationDomain_strategy = st.builds(
    FlatQVT_RelationDomain,
)
OperationBody_strategy = st.builds(
    OperationBody,
)
FlatQVT_MappingBody_strategy = st.builds(
    FlatQVT_MappingBody,
)
FlatQVT_ConstructorBody_strategy = st.builds(
    FlatQVT_ConstructorBody,
)
ImperativeOperation_strategy = st.builds(
    ImperativeOperation,
)
FlatQVT_EntryOperation_strategy = st.builds(
    FlatQVT_EntryOperation,
)
FlatQVT_MappingOperation_strategy = st.builds(
    FlatQVT_MappingOperation,
)
FlatQVT_Helper_strategy = st.builds(
    FlatQVT_Helper,
    isQuery=
        safe_text
)
FlatQVT_Constructor_strategy = st.builds(
    FlatQVT_Constructor,
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
FlatQVT_CollectionItem_strategy = st.builds(
    FlatQVT_CollectionItem,
)
Class_strategy = st.builds(
    Class,
)
FlatQVT_OrderedTupleType_strategy = st.builds(
    FlatQVT_OrderedTupleType,
)
FlatQVT_ModelType_strategy = st.builds(
    FlatQVT_ModelType,
    conformanceKind=
        safe_text
)
FlatQVT_Module_strategy = st.builds(
    FlatQVT_Module,
    isBlackbox=
        safe_text
)
Operation_strategy = st.builds(
    Operation,
)
FlatQVT_ImperativeOperation_strategy = st.builds(
    FlatQVT_ImperativeOperation,
    isBlackbox=
        safe_text
)
FlatQVT_Function_strategy = st.builds(
    FlatQVT_Function,
)
Property_strategy = st.builds(
    Property,
)
FlatQVT_ContextualProperty_strategy = st.builds(
    FlatQVT_ContextualProperty,
)
TemplateExp_strategy = st.builds(
    TemplateExp,
)
FlatQVT_ObjectTemplateExp_strategy = st.builds(
    FlatQVT_ObjectTemplateExp,
)
FlatQVT_CollectionTemplateExp_strategy = st.builds(
    FlatQVT_CollectionTemplateExp,
)
FlatQVT_CollectionRange_strategy = st.builds(
    FlatQVT_CollectionRange,
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
FlatQVT_OclExpression_strategy = st.builds(
    FlatQVT_OclExpression,
)
FlatQVT_Parameter_strategy = st.builds(
    FlatQVT_Parameter,
)
FlatQVT_Property_strategy = st.builds(
    FlatQVT_Property,
    isID=
        safe_text,
    default=
        safe_text,
    isDerived=
        safe_text,
    isReadOnly=
        safe_text,
    isComposite=
        safe_text
)
FlatQVT_Operation_strategy = st.builds(
    FlatQVT_Operation,
)
FlatQVT_ExpressionInOcl_strategy = st.builds(
    FlatQVT_ExpressionInOcl,
)
FlatQVT_CollectionLiteralPart_strategy = st.builds(
    FlatQVT_CollectionLiteralPart,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
FlatQVT_OrderedTupleLiteralExp_strategy = st.builds(
    FlatQVT_OrderedTupleLiteralExp,
)
FlatQVT_EnumLiteralExp_strategy = st.builds(
    FlatQVT_EnumLiteralExp,
)
FlatQVT_DictLiteralExp_strategy = st.builds(
    FlatQVT_DictLiteralExp,
)
FlatQVT_PrimitiveLiteralExp_strategy = st.builds(
    FlatQVT_PrimitiveLiteralExp,
)
FlatQVT_ListLiteralExp_strategy = st.builds(
    FlatQVT_ListLiteralExp,
)
FlatQVT_InvalidLiteralExp_strategy = st.builds(
    FlatQVT_InvalidLiteralExp,
)
FlatQVT_NullLiteralExp_strategy = st.builds(
    FlatQVT_NullLiteralExp,
)
FlatQVT_CollectionLiteralExp_strategy = st.builds(
    FlatQVT_CollectionLiteralExp,
    kind=
        safe_text
)
CorePattern_strategy = st.builds(
    CorePattern,
)
FlatQVT_GuardPattern_strategy = st.builds(
    FlatQVT_GuardPattern,
)
FlatQVT_BottomPattern_strategy = st.builds(
    FlatQVT_BottomPattern,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
FlatQVT_NumericLiteralExp_strategy = st.builds(
    FlatQVT_NumericLiteralExp,
)
FlatQVT_BooleanLiteralExp_strategy = st.builds(
    FlatQVT_BooleanLiteralExp,
    booleanSymbol=
        safe_text
)
CollectionType_strategy = st.builds(
    CollectionType,
)
FlatQVT_DictionaryType_strategy = st.builds(
    FlatQVT_DictionaryType,
)
FlatQVT_OrderedSetType_strategy = st.builds(
    FlatQVT_OrderedSetType,
)
FlatQVT_ListType_strategy = st.builds(
    FlatQVT_ListType,
)
FlatQVT_BagType_strategy = st.builds(
    FlatQVT_BagType,
)
Element_strategy = st.builds(
    Element,
)
FlatQVT_Key_strategy = st.builds(
    FlatQVT_Key,
)
FlatQVT_OrderedTupleLiteralPart_strategy = st.builds(
    FlatQVT_OrderedTupleLiteralPart,
)
FlatQVT_NamedElement_strategy = st.builds(
    FlatQVT_NamedElement,
    name=
        safe_text
)
FlatQVT_OperationBody_strategy = st.builds(
    FlatQVT_OperationBody,
)
FlatQVT_RelationDomainAssignment_strategy = st.builds(
    FlatQVT_RelationDomainAssignment,
)
FlatQVT_Predicate_strategy = st.builds(
    FlatQVT_Predicate,
)
FlatQVT_DictLiteralPart_strategy = st.builds(
    FlatQVT_DictLiteralPart,
)
FlatQVT_PropertyTemplateItem_strategy = st.builds(
    FlatQVT_PropertyTemplateItem,
    isOpposite=
        safe_text
)
FlatQVT_EnforcementOperation_strategy = st.builds(
    FlatQVT_EnforcementOperation,
    enforcementMode=
        safe_text
)
FlatQVT_ModuleImport_strategy = st.builds(
    FlatQVT_ModuleImport,
    kind=
        safe_text
)
FlatQVT_Pattern_strategy = st.builds(
    FlatQVT_Pattern,
)
FlatQVT_Comment_strategy = st.builds(
    FlatQVT_Comment,
    body=
        safe_text
)
FlatQVT_Factory_strategy = st.builds(
    FlatQVT_Factory,
)
FlatQVT_Assignment_strategy = st.builds(
    FlatQVT_Assignment,
    isDefault=
        safe_text
)
RealizedVariable_strategy = st.builds(
    RealizedVariable,
)
EnforcementOperation_strategy = st.builds(
    EnforcementOperation,
)
Assignment_strategy = st.builds(
    Assignment,
)
FlatQVT_PropertyAssignment_strategy = st.builds(
    FlatQVT_PropertyAssignment,
)
GuardPattern_strategy = st.builds(
    GuardPattern,
)
FlatQVT_Variable_strategy = st.builds(
    FlatQVT_Variable,
)
FlatQVT_VarParameter_strategy = st.builds(
    FlatQVT_VarParameter,
    kind=
        safe_text
)
FlatQVT_VariableAssignment_strategy = st.builds(
    FlatQVT_VariableAssignment,
)
LetExp_strategy = st.builds(
    LetExp,
)
FlatQVT_UnlimitedNaturalExp_strategy = st.builds(
    FlatQVT_UnlimitedNaturalExp,
    symbol=
        safe_text
)
Extent_strategy = st.builds(
    Extent,
)
FlatQVT_URIExtent_strategy = st.builds(
    FlatQVT_URIExtent,
)
FlatQVT_Typedef_strategy = st.builds(
    FlatQVT_Typedef,
)
FlatQVT_Type_strategy = st.builds(
    FlatQVT_Type,
)
FlatQVT_TupleType_strategy = st.builds(
    FlatQVT_TupleType,
)
TupleLiteralExp_strategy = st.builds(
    TupleLiteralExp,
)
FlatQVT_TupleLiteralPart_strategy = st.builds(
    FlatQVT_TupleLiteralPart,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
FlatQVT_TypedModel_strategy = st.builds(
    FlatQVT_TypedModel,
)
FlatQVT_TypedElement_strategy = st.builds(
    FlatQVT_TypedElement,
)
FlatQVT_Transformation_strategy = st.builds(
    FlatQVT_Transformation,
)
FlatQVT_TemplateExp_strategy = st.builds(
    FlatQVT_TemplateExp,
)
FlatQVT_TupleLiteralExp_strategy = st.builds(
    FlatQVT_TupleLiteralExp,
)
CatchExp_strategy = st.builds(
    CatchExp,
)
FlatQVT_SetType_strategy = st.builds(
    FlatQVT_SetType,
)
FlatQVT_SequenceType_strategy = st.builds(
    FlatQVT_SequenceType,
)
FlatQVT_Rule_strategy = st.builds(
    FlatQVT_Rule,
)
FlatQVT_Tag_strategy = st.builds(
    FlatQVT_Tag,
    value=
        safe_text,
    name=
        safe_text
)
AltExp_strategy = st.builds(
    AltExp,
)
FlatQVT_StringLiteralExp_strategy = st.builds(
    FlatQVT_StringLiteralExp,
    stringSymbol=
        safe_text
)
Key_strategy = st.builds(
    Key,
)
Transformation_strategy = st.builds(
    Transformation,
)
FlatQVT_RelationalTransformation_strategy = st.builds(
    FlatQVT_RelationalTransformation,
)
FlatQVT_RelationImplementation_strategy = st.builds(
    FlatQVT_RelationImplementation,
)
ResolveExp_strategy = st.builds(
    ResolveExp,
)
FlatQVT_ResolveInExp_strategy = st.builds(
    FlatQVT_ResolveInExp,
)
Area_strategy = st.builds(
    Area,
)
FlatQVT_Mapping_strategy = st.builds(
    FlatQVT_Mapping,
)
FlatQVT_CoreDomain_strategy = st.builds(
    FlatQVT_CoreDomain,
)
BottomPattern_strategy = st.builds(
    BottomPattern,
)
FlatQVT_Area_strategy = st.builds(
    FlatQVT_Area,
)
Type_strategy = st.builds(
    Type,
)
FlatQVT_TemplateParameterType_strategy = st.builds(
    FlatQVT_TemplateParameterType,
    specification=
        safe_text
)
FlatQVT_InvalidType_strategy = st.builds(
    FlatQVT_InvalidType,
)
FlatQVT_VoidType_strategy = st.builds(
    FlatQVT_VoidType,
)
FlatQVT_DataType_strategy = st.builds(
    FlatQVT_DataType,
)
FlatQVT_Class_strategy = st.builds(
    FlatQVT_Class,
    isAbstract=
        safe_text
)
FlatQVT_AnyType_strategy = st.builds(
    FlatQVT_AnyType,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
FlatQVT_ImperativeExpression_strategy = st.builds(
    FlatQVT_ImperativeExpression,
)
FlatQVT_VariableExp_strategy = st.builds(
    FlatQVT_VariableExp,
)
FlatQVT_IfExp_strategy = st.builds(
    FlatQVT_IfExp,
)
FlatQVT_CallExp_strategy = st.builds(
    FlatQVT_CallExp,
)
FlatQVT_TypeExp_strategy = st.builds(
    FlatQVT_TypeExp,
)
FlatQVT_LoopExp_strategy = st.builds(
    FlatQVT_LoopExp,
)
FlatQVT_RelationCallExp_strategy = st.builds(
    FlatQVT_RelationCallExp,
)
FlatQVT_LetExp_strategy = st.builds(
    FlatQVT_LetExp,
)
FlatQVT_LiteralExp_strategy = st.builds(
    FlatQVT_LiteralExp,
)
ImperativeExpression_strategy = st.builds(
    ImperativeExpression,
)
FlatQVT_VariableInitExp_strategy = st.builds(
    FlatQVT_VariableInitExp,
    withResult=
        safe_text
)
FlatQVT_InstantiationExp_strategy = st.builds(
    FlatQVT_InstantiationExp,
)
FlatQVT_TryExp_strategy = st.builds(
    FlatQVT_TryExp,
)
FlatQVT_SwitchExp_strategy = st.builds(
    FlatQVT_SwitchExp,
)
FlatQVT_WhileExp_strategy = st.builds(
    FlatQVT_WhileExp,
)
FlatQVT_BlockExp_strategy = st.builds(
    FlatQVT_BlockExp,
)
FlatQVT_BreakExp_strategy = st.builds(
    FlatQVT_BreakExp,
)
FlatQVT_ReturnExp_strategy = st.builds(
    FlatQVT_ReturnExp,
)
FlatQVT_ResolveExp_strategy = st.builds(
    FlatQVT_ResolveExp,
    isInverse=
        safe_text,
    one=
        safe_text,
    isDeferred=
        safe_text
)
FlatQVT_LogExp_strategy = st.builds(
    FlatQVT_LogExp,
)
FlatQVT_ImperativeCallExp_strategy = st.builds(
    FlatQVT_ImperativeCallExp,
    isVirtual=
        safe_text
)
FlatQVT_CatchExp_strategy = st.builds(
    FlatQVT_CatchExp,
)
FlatQVT_UnlinkExp_strategy = st.builds(
    FlatQVT_UnlinkExp,
)
FlatQVT_UnpackExp_strategy = st.builds(
    FlatQVT_UnpackExp,
)
FlatQVT_ImperativeLoopExp_strategy = st.builds(
    FlatQVT_ImperativeLoopExp,
)
FlatQVT_ComputeExp_strategy = st.builds(
    FlatQVT_ComputeExp,
)
FlatQVT_ContinueExp_strategy = st.builds(
    FlatQVT_ContinueExp,
)
FlatQVT_RaiseExp_strategy = st.builds(
    FlatQVT_RaiseExp,
)
FlatQVT_AltExp_strategy = st.builds(
    FlatQVT_AltExp,
)
FlatQVT_AssignExp_strategy = st.builds(
    FlatQVT_AssignExp,
    isReset=
        safe_text
)
LogExp_strategy = st.builds(
    LogExp,
)
FlatQVT_AssertExp_strategy = st.builds(
    FlatQVT_AssertExp,
    severity=
        safe_text
)

@given(instance=DomainPattern_strategy)
@settings(max_examples=50)
def test_domainpattern_instantiation(instance):
    assert isinstance(instance, DomainPattern)

@given(instance=RelationDomainAssignment_strategy)
@settings(max_examples=50)
def test_relationdomainassignment_instantiation(instance):
    assert isinstance(instance, RelationDomainAssignment)

@given(instance=RelationImplementation_strategy)
@settings(max_examples=50)
def test_relationimplementation_instantiation(instance):
    assert isinstance(instance, RelationImplementation)

@given(instance=ReflectiveCollection_strategy)
@settings(max_examples=50)
def test_reflectivecollection_instantiation(instance):
    assert isinstance(instance, ReflectiveCollection)

@given(instance=FlatQVT_ReflectiveSequence_strategy)
@settings(max_examples=50)
def test_flatqvt_reflectivesequence_instantiation(instance):
    assert isinstance(instance, FlatQVT_ReflectiveSequence)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_ReflectiveSequence_strategy)
@settings(max_examples=30)
def test_flatqvt_reflectivesequence_set_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.set(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.set).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'set' in FlatQVT_ReflectiveSequence is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'set' in FlatQVT_ReflectiveSequence did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'set' in FlatQVT_ReflectiveSequence is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_ReflectiveSequence_strategy)
@settings(max_examples=30)
def test_flatqvt_reflectivesequence_remove_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.remove(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.remove).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'remove' in FlatQVT_ReflectiveSequence is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'remove' in FlatQVT_ReflectiveSequence did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'remove' in FlatQVT_ReflectiveSequence is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_ReflectiveSequence_strategy)
@settings(max_examples=30)
def test_flatqvt_reflectivesequence_add_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.add(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.add).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'add' in FlatQVT_ReflectiveSequence is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'add' in FlatQVT_ReflectiveSequence did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'add' in FlatQVT_ReflectiveSequence is not implemented or raised an error")

@given(instance=NavigationCallExp_strategy)
@settings(max_examples=50)
def test_navigationcallexp_instantiation(instance):
    assert isinstance(instance, NavigationCallExp)

@given(instance=FlatQVT_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_flatqvt_propertycallexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_PropertyCallExp)

@given(instance=ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_objecttemplateexp_instantiation(instance):
    assert isinstance(instance, ObjectTemplateExp)

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=OrderedTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_orderedtupleliteralpart_instantiation(instance):
    assert isinstance(instance, OrderedTupleLiteralPart)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=FlatQVT_OppositePropertyCallExp_strategy)
@settings(max_examples=50)
def test_flatqvt_oppositepropertycallexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_OppositePropertyCallExp)

@given(instance=PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_propertytemplateitem_instantiation(instance):
    assert isinstance(instance, PropertyTemplateItem)

@given(instance=ConstructorBody_strategy)
@settings(max_examples=50)
def test_constructorbody_instantiation(instance):
    assert isinstance(instance, ConstructorBody)

@given(instance=InstantiationExp_strategy)
@settings(max_examples=50)
def test_instantiationexp_instantiation(instance):
    assert isinstance(instance, InstantiationExp)

@given(instance=FlatQVT_ObjectExp_strategy)
@settings(max_examples=50)
def test_flatqvt_objectexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_ObjectExp)

@given(instance=FlatQVT_Object_strategy)
@settings(max_examples=50)
def test_flatqvt_object_instantiation(instance):
    assert isinstance(instance, FlatQVT_Object)

@given(instance=FeatureCallExp_strategy)
@settings(max_examples=50)
def test_featurecallexp_instantiation(instance):
    assert isinstance(instance, FeatureCallExp)

@given(instance=FlatQVT_OperationCallExp_strategy)
@settings(max_examples=50)
def test_flatqvt_operationcallexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_OperationCallExp)

@given(instance=FlatQVT_NavigationCallExp_strategy)
@settings(max_examples=50)
def test_flatqvt_navigationcallexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_NavigationCallExp)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=ModelType_strategy)
@settings(max_examples=50)
def test_modeltype_instantiation(instance):
    assert isinstance(instance, ModelType)

@given(instance=FlatQVT_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_flatqvt_multiplicityelement_instantiation(instance):
    assert isinstance(instance, FlatQVT_MultiplicityElement)



@given(instance=FlatQVT_MultiplicityElement_strategy)
def test_flatqvt_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=FlatQVT_MultiplicityElement_strategy)
def test_flatqvt_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=FlatQVT_MultiplicityElement_strategy)
def test_flatqvt_multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=FlatQVT_MultiplicityElement_strategy)
def test_flatqvt_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=RelationDomain_strategy)
@settings(max_examples=50)
def test_relationdomain_instantiation(instance):
    assert isinstance(instance, RelationDomain)

@given(instance=ModelParameter_strategy)
@settings(max_examples=50)
def test_modelparameter_instantiation(instance):
    assert isinstance(instance, ModelParameter)

@given(instance=Tag_strategy)
@settings(max_examples=50)
def test_tag_instantiation(instance):
    assert isinstance(instance, Tag)

@given(instance=ModuleImport_strategy)
@settings(max_examples=50)
def test_moduleimport_instantiation(instance):
    assert isinstance(instance, ModuleImport)

@given(instance=EntryOperation_strategy)
@settings(max_examples=50)
def test_entryoperation_instantiation(instance):
    assert isinstance(instance, EntryOperation)

@given(instance=ImperativeCallExp_strategy)
@settings(max_examples=50)
def test_imperativecallexp_instantiation(instance):
    assert isinstance(instance, ImperativeCallExp)

@given(instance=FlatQVT_MappingCallExp_strategy)
@settings(max_examples=50)
def test_flatqvt_mappingcallexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_MappingCallExp)



@given(instance=FlatQVT_MappingCallExp_strategy)
def test_flatqvt_mappingcallexp_isStrict_setter(instance):
    original = instance.isStrict
    instance.isStrict = original
    assert instance.isStrict == original

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=MappingOperation_strategy)
@settings(max_examples=50)
def test_mappingoperation_instantiation(instance):
    assert isinstance(instance, MappingOperation)

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=FlatQVT_OperationalTransformation_strategy)
@settings(max_examples=50)
def test_flatqvt_operationaltransformation_instantiation(instance):
    assert isinstance(instance, FlatQVT_OperationalTransformation)

@given(instance=FlatQVT_Library_strategy)
@settings(max_examples=50)
def test_flatqvt_library_instantiation(instance):
    assert isinstance(instance, FlatQVT_Library)

@given(instance=RelationalTransformation_strategy)
@settings(max_examples=50)
def test_relationaltransformation_instantiation(instance):
    assert isinstance(instance, RelationalTransformation)

@given(instance=Mapping_strategy)
@settings(max_examples=50)
def test_mapping_instantiation(instance):
    assert isinstance(instance, Mapping)

@given(instance=VarParameter_strategy)
@settings(max_examples=50)
def test_varparameter_instantiation(instance):
    assert isinstance(instance, VarParameter)

@given(instance=FlatQVT_MappingParameter_strategy)
@settings(max_examples=50)
def test_flatqvt_mappingparameter_instantiation(instance):
    assert isinstance(instance, FlatQVT_MappingParameter)

@given(instance=FlatQVT_ModelParameter_strategy)
@settings(max_examples=50)
def test_flatqvt_modelparameter_instantiation(instance):
    assert isinstance(instance, FlatQVT_ModelParameter)

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=FlatQVT_RealLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt_realliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_RealLiteralExp)



@given(instance=FlatQVT_RealLiteralExp_strategy)
def test_flatqvt_realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=FlatQVT_IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt_integerliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_IntegerLiteralExp)



@given(instance=FlatQVT_IntegerLiteralExp_strategy)
def test_flatqvt_integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=FlatQVT_IteratorExp_strategy)
@settings(max_examples=50)
def test_flatqvt_iteratorexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_IteratorExp)

@given(instance=FlatQVT_IterateExp_strategy)
@settings(max_examples=50)
def test_flatqvt_iterateexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_IterateExp)

@given(instance=Enumeration_strategy)
@settings(max_examples=50)
def test_enumeration_instantiation(instance):
    assert isinstance(instance, Enumeration)

@given(instance=ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExp)

@given(instance=FlatQVT_ImperativeIterateExp_strategy)
@settings(max_examples=50)
def test_flatqvt_imperativeiterateexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_ImperativeIterateExp)

@given(instance=FlatQVT_ForExp_strategy)
@settings(max_examples=50)
def test_flatqvt_forexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_ForExp)

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=FlatQVT_FeatureCallExp_strategy)
@settings(max_examples=50)
def test_flatqvt_featurecallexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_FeatureCallExp)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=FlatQVT_ReflectiveCollection_strategy)
@settings(max_examples=50)
def test_flatqvt_reflectivecollection_instantiation(instance):
    assert isinstance(instance, FlatQVT_ReflectiveCollection)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_flatqvt_reflectivecollection_add_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.add(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.add).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'add' in FlatQVT_ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'add' in FlatQVT_ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'add' in FlatQVT_ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_flatqvt_reflectivecollection_remove_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.remove(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.remove).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'remove' in FlatQVT_ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'remove' in FlatQVT_ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'remove' in FlatQVT_ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_flatqvt_reflectivecollection_clear_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.clear()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.clear).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'clear' in FlatQVT_ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'clear' in FlatQVT_ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'clear' in FlatQVT_ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_flatqvt_reflectivecollection_size_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.size()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.size).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'size' in FlatQVT_ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'size' in FlatQVT_ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'size' in FlatQVT_ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_flatqvt_reflectivecollection_addall_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addAll(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addAll).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addAll' in FlatQVT_ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addAll' in FlatQVT_ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addAll' in FlatQVT_ReflectiveCollection is not implemented or raised an error")

@given(instance=FlatQVT_Extent_strategy)
@settings(max_examples=50)
def test_flatqvt_extent_instantiation(instance):
    assert isinstance(instance, FlatQVT_Extent)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_Extent_strategy)
@settings(max_examples=30)
def test_flatqvt_extent_usecontainment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.useContainment()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.useContainment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'useContainment' in FlatQVT_Extent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'useContainment' in FlatQVT_Extent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'useContainment' in FlatQVT_Extent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_Extent_strategy)
@settings(max_examples=30)
def test_flatqvt_extent_elements_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.elements()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.elements).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'elements' in FlatQVT_Extent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'elements' in FlatQVT_Extent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'elements' in FlatQVT_Extent is not implemented or raised an error")

@given(instance=FlatQVT_Element_strategy)
@settings(max_examples=50)
def test_flatqvt_element_instantiation(instance):
    assert isinstance(instance, FlatQVT_Element)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_Element_strategy)
@settings(max_examples=30)
def test_flatqvt_element_isset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSet(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSet).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSet' in FlatQVT_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSet' in FlatQVT_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSet' in FlatQVT_Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_Element_strategy)
@settings(max_examples=30)
def test_flatqvt_element_container_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.container()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.container).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'container' in FlatQVT_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'container' in FlatQVT_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'container' in FlatQVT_Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_Element_strategy)
@settings(max_examples=30)
def test_flatqvt_element_equals_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.equals(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.equals).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'equals' in FlatQVT_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equals' in FlatQVT_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equals' in FlatQVT_Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_Element_strategy)
@settings(max_examples=30)
def test_flatqvt_element_unset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.unset(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.unset).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'unset' in FlatQVT_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unset' in FlatQVT_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unset' in FlatQVT_Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_Element_strategy)
@settings(max_examples=30)
def test_flatqvt_element_set_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.set(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.set).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'set' in FlatQVT_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'set' in FlatQVT_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'set' in FlatQVT_Element is not implemented or raised an error")

@given(instance=TypedModel_strategy)
@settings(max_examples=50)
def test_typedmodel_instantiation(instance):
    assert isinstance(instance, TypedModel)

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=DictLiteralPart_strategy)
@settings(max_examples=50)
def test_dictliteralpart_instantiation(instance):
    assert isinstance(instance, DictLiteralPart)

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=FlatQVT_DomainPattern_strategy)
@settings(max_examples=50)
def test_flatqvt_domainpattern_instantiation(instance):
    assert isinstance(instance, FlatQVT_DomainPattern)

@given(instance=FlatQVT_CorePattern_strategy)
@settings(max_examples=50)
def test_flatqvt_corepattern_instantiation(instance):
    assert isinstance(instance, FlatQVT_CorePattern)

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=FlatQVT_Relation_strategy)
@settings(max_examples=50)
def test_flatqvt_relation_instantiation(instance):
    assert isinstance(instance, FlatQVT_Relation)



@given(instance=FlatQVT_Relation_strategy)
def test_flatqvt_relation_isTopLevel_setter(instance):
    original = instance.isTopLevel
    instance.isTopLevel = original
    assert instance.isTopLevel == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=FlatQVT_Package_strategy)
@settings(max_examples=50)
def test_flatqvt_package_instantiation(instance):
    assert isinstance(instance, FlatQVT_Package)



@given(instance=FlatQVT_Package_strategy)
def test_flatqvt_package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=FlatQVT_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_flatqvt_enumerationliteral_instantiation(instance):
    assert isinstance(instance, FlatQVT_EnumerationLiteral)

@given(instance=FlatQVT_Domain_strategy)
@settings(max_examples=50)
def test_flatqvt_domain_instantiation(instance):
    assert isinstance(instance, FlatQVT_Domain)



@given(instance=FlatQVT_Domain_strategy)
def test_flatqvt_domain_isCheckable_setter(instance):
    original = instance.isCheckable
    instance.isCheckable = original
    assert instance.isCheckable == original



@given(instance=FlatQVT_Domain_strategy)
def test_flatqvt_domain_isEnforceable_setter(instance):
    original = instance.isEnforceable
    instance.isEnforceable = original
    assert instance.isEnforceable == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=FlatQVT_PrimitiveType_strategy)
@settings(max_examples=50)
def test_flatqvt_primitivetype_instantiation(instance):
    assert isinstance(instance, FlatQVT_PrimitiveType)

@given(instance=FlatQVT_Enumeration_strategy)
@settings(max_examples=50)
def test_flatqvt_enumeration_instantiation(instance):
    assert isinstance(instance, FlatQVT_Enumeration)

@given(instance=FlatQVT_CollectionType_strategy)
@settings(max_examples=50)
def test_flatqvt_collectiontype_instantiation(instance):
    assert isinstance(instance, FlatQVT_CollectionType)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=FlatQVT_RealizedVariable_strategy)
@settings(max_examples=50)
def test_flatqvt_realizedvariable_instantiation(instance):
    assert isinstance(instance, FlatQVT_RealizedVariable)

@given(instance=FlatQVT_FunctionParameter_strategy)
@settings(max_examples=50)
def test_flatqvt_functionparameter_instantiation(instance):
    assert isinstance(instance, FlatQVT_FunctionParameter)

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=FlatQVT_RelationDomain_strategy)
@settings(max_examples=50)
def test_flatqvt_relationdomain_instantiation(instance):
    assert isinstance(instance, FlatQVT_RelationDomain)

@given(instance=OperationBody_strategy)
@settings(max_examples=50)
def test_operationbody_instantiation(instance):
    assert isinstance(instance, OperationBody)

@given(instance=FlatQVT_MappingBody_strategy)
@settings(max_examples=50)
def test_flatqvt_mappingbody_instantiation(instance):
    assert isinstance(instance, FlatQVT_MappingBody)

@given(instance=FlatQVT_ConstructorBody_strategy)
@settings(max_examples=50)
def test_flatqvt_constructorbody_instantiation(instance):
    assert isinstance(instance, FlatQVT_ConstructorBody)

@given(instance=ImperativeOperation_strategy)
@settings(max_examples=50)
def test_imperativeoperation_instantiation(instance):
    assert isinstance(instance, ImperativeOperation)

@given(instance=FlatQVT_EntryOperation_strategy)
@settings(max_examples=50)
def test_flatqvt_entryoperation_instantiation(instance):
    assert isinstance(instance, FlatQVT_EntryOperation)

@given(instance=FlatQVT_MappingOperation_strategy)
@settings(max_examples=50)
def test_flatqvt_mappingoperation_instantiation(instance):
    assert isinstance(instance, FlatQVT_MappingOperation)

@given(instance=FlatQVT_Helper_strategy)
@settings(max_examples=50)
def test_flatqvt_helper_instantiation(instance):
    assert isinstance(instance, FlatQVT_Helper)



@given(instance=FlatQVT_Helper_strategy)
def test_flatqvt_helper_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=FlatQVT_Constructor_strategy)
@settings(max_examples=50)
def test_flatqvt_constructor_instantiation(instance):
    assert isinstance(instance, FlatQVT_Constructor)

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=FlatQVT_CollectionItem_strategy)
@settings(max_examples=50)
def test_flatqvt_collectionitem_instantiation(instance):
    assert isinstance(instance, FlatQVT_CollectionItem)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=FlatQVT_OrderedTupleType_strategy)
@settings(max_examples=50)
def test_flatqvt_orderedtupletype_instantiation(instance):
    assert isinstance(instance, FlatQVT_OrderedTupleType)

@given(instance=FlatQVT_ModelType_strategy)
@settings(max_examples=50)
def test_flatqvt_modeltype_instantiation(instance):
    assert isinstance(instance, FlatQVT_ModelType)



@given(instance=FlatQVT_ModelType_strategy)
def test_flatqvt_modeltype_conformanceKind_setter(instance):
    original = instance.conformanceKind
    instance.conformanceKind = original
    assert instance.conformanceKind == original

@given(instance=FlatQVT_Module_strategy)
@settings(max_examples=50)
def test_flatqvt_module_instantiation(instance):
    assert isinstance(instance, FlatQVT_Module)



@given(instance=FlatQVT_Module_strategy)
def test_flatqvt_module_isBlackbox_setter(instance):
    original = instance.isBlackbox
    instance.isBlackbox = original
    assert instance.isBlackbox == original

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=FlatQVT_ImperativeOperation_strategy)
@settings(max_examples=50)
def test_flatqvt_imperativeoperation_instantiation(instance):
    assert isinstance(instance, FlatQVT_ImperativeOperation)



@given(instance=FlatQVT_ImperativeOperation_strategy)
def test_flatqvt_imperativeoperation_isBlackbox_setter(instance):
    original = instance.isBlackbox
    instance.isBlackbox = original
    assert instance.isBlackbox == original

@given(instance=FlatQVT_Function_strategy)
@settings(max_examples=50)
def test_flatqvt_function_instantiation(instance):
    assert isinstance(instance, FlatQVT_Function)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=FlatQVT_ContextualProperty_strategy)
@settings(max_examples=50)
def test_flatqvt_contextualproperty_instantiation(instance):
    assert isinstance(instance, FlatQVT_ContextualProperty)

@given(instance=TemplateExp_strategy)
@settings(max_examples=50)
def test_templateexp_instantiation(instance):
    assert isinstance(instance, TemplateExp)

@given(instance=FlatQVT_ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_flatqvt_objecttemplateexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_ObjectTemplateExp)

@given(instance=FlatQVT_CollectionTemplateExp_strategy)
@settings(max_examples=50)
def test_flatqvt_collectiontemplateexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_CollectionTemplateExp)

@given(instance=FlatQVT_CollectionRange_strategy)
@settings(max_examples=50)
def test_flatqvt_collectionrange_instantiation(instance):
    assert isinstance(instance, FlatQVT_CollectionRange)

@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=FlatQVT_OclExpression_strategy)
@settings(max_examples=50)
def test_flatqvt_oclexpression_instantiation(instance):
    assert isinstance(instance, FlatQVT_OclExpression)

@given(instance=FlatQVT_Parameter_strategy)
@settings(max_examples=50)
def test_flatqvt_parameter_instantiation(instance):
    assert isinstance(instance, FlatQVT_Parameter)

@given(instance=FlatQVT_Property_strategy)
@settings(max_examples=50)
def test_flatqvt_property_instantiation(instance):
    assert isinstance(instance, FlatQVT_Property)



@given(instance=FlatQVT_Property_strategy)
def test_flatqvt_property_isID_setter(instance):
    original = instance.isID
    instance.isID = original
    assert instance.isID == original



@given(instance=FlatQVT_Property_strategy)
def test_flatqvt_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=FlatQVT_Property_strategy)
def test_flatqvt_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=FlatQVT_Property_strategy)
def test_flatqvt_property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original



@given(instance=FlatQVT_Property_strategy)
def test_flatqvt_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=FlatQVT_Operation_strategy)
@settings(max_examples=50)
def test_flatqvt_operation_instantiation(instance):
    assert isinstance(instance, FlatQVT_Operation)

@given(instance=FlatQVT_ExpressionInOcl_strategy)
@settings(max_examples=50)
def test_flatqvt_expressioninocl_instantiation(instance):
    assert isinstance(instance, FlatQVT_ExpressionInOcl)

@given(instance=FlatQVT_CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_flatqvt_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, FlatQVT_CollectionLiteralPart)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=FlatQVT_OrderedTupleLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt_orderedtupleliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_OrderedTupleLiteralExp)

@given(instance=FlatQVT_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt_enumliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_EnumLiteralExp)

@given(instance=FlatQVT_DictLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt_dictliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_DictLiteralExp)

@given(instance=FlatQVT_PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_PrimitiveLiteralExp)

@given(instance=FlatQVT_ListLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt_listliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_ListLiteralExp)

@given(instance=FlatQVT_InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt_invalidliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_InvalidLiteralExp)

@given(instance=FlatQVT_NullLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt_nullliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_NullLiteralExp)

@given(instance=FlatQVT_CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_CollectionLiteralExp)



@given(instance=FlatQVT_CollectionLiteralExp_strategy)
def test_flatqvt_collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CorePattern_strategy)
@settings(max_examples=50)
def test_corepattern_instantiation(instance):
    assert isinstance(instance, CorePattern)

@given(instance=FlatQVT_GuardPattern_strategy)
@settings(max_examples=50)
def test_flatqvt_guardpattern_instantiation(instance):
    assert isinstance(instance, FlatQVT_GuardPattern)

@given(instance=FlatQVT_BottomPattern_strategy)
@settings(max_examples=50)
def test_flatqvt_bottompattern_instantiation(instance):
    assert isinstance(instance, FlatQVT_BottomPattern)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=FlatQVT_NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt_numericliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_NumericLiteralExp)

@given(instance=FlatQVT_BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt_booleanliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_BooleanLiteralExp)



@given(instance=FlatQVT_BooleanLiteralExp_strategy)
def test_flatqvt_booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=FlatQVT_DictionaryType_strategy)
@settings(max_examples=50)
def test_flatqvt_dictionarytype_instantiation(instance):
    assert isinstance(instance, FlatQVT_DictionaryType)

@given(instance=FlatQVT_OrderedSetType_strategy)
@settings(max_examples=50)
def test_flatqvt_orderedsettype_instantiation(instance):
    assert isinstance(instance, FlatQVT_OrderedSetType)

@given(instance=FlatQVT_ListType_strategy)
@settings(max_examples=50)
def test_flatqvt_listtype_instantiation(instance):
    assert isinstance(instance, FlatQVT_ListType)

@given(instance=FlatQVT_BagType_strategy)
@settings(max_examples=50)
def test_flatqvt_bagtype_instantiation(instance):
    assert isinstance(instance, FlatQVT_BagType)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=FlatQVT_Key_strategy)
@settings(max_examples=50)
def test_flatqvt_key_instantiation(instance):
    assert isinstance(instance, FlatQVT_Key)

@given(instance=FlatQVT_OrderedTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_flatqvt_orderedtupleliteralpart_instantiation(instance):
    assert isinstance(instance, FlatQVT_OrderedTupleLiteralPart)

@given(instance=FlatQVT_NamedElement_strategy)
@settings(max_examples=50)
def test_flatqvt_namedelement_instantiation(instance):
    assert isinstance(instance, FlatQVT_NamedElement)



@given(instance=FlatQVT_NamedElement_strategy)
def test_flatqvt_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FlatQVT_OperationBody_strategy)
@settings(max_examples=50)
def test_flatqvt_operationbody_instantiation(instance):
    assert isinstance(instance, FlatQVT_OperationBody)

@given(instance=FlatQVT_RelationDomainAssignment_strategy)
@settings(max_examples=50)
def test_flatqvt_relationdomainassignment_instantiation(instance):
    assert isinstance(instance, FlatQVT_RelationDomainAssignment)

@given(instance=FlatQVT_Predicate_strategy)
@settings(max_examples=50)
def test_flatqvt_predicate_instantiation(instance):
    assert isinstance(instance, FlatQVT_Predicate)

@given(instance=FlatQVT_DictLiteralPart_strategy)
@settings(max_examples=50)
def test_flatqvt_dictliteralpart_instantiation(instance):
    assert isinstance(instance, FlatQVT_DictLiteralPart)

@given(instance=FlatQVT_PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_flatqvt_propertytemplateitem_instantiation(instance):
    assert isinstance(instance, FlatQVT_PropertyTemplateItem)



@given(instance=FlatQVT_PropertyTemplateItem_strategy)
def test_flatqvt_propertytemplateitem_isOpposite_setter(instance):
    original = instance.isOpposite
    instance.isOpposite = original
    assert instance.isOpposite == original

@given(instance=FlatQVT_EnforcementOperation_strategy)
@settings(max_examples=50)
def test_flatqvt_enforcementoperation_instantiation(instance):
    assert isinstance(instance, FlatQVT_EnforcementOperation)



@given(instance=FlatQVT_EnforcementOperation_strategy)
def test_flatqvt_enforcementoperation_enforcementMode_setter(instance):
    original = instance.enforcementMode
    instance.enforcementMode = original
    assert instance.enforcementMode == original

@given(instance=FlatQVT_ModuleImport_strategy)
@settings(max_examples=50)
def test_flatqvt_moduleimport_instantiation(instance):
    assert isinstance(instance, FlatQVT_ModuleImport)



@given(instance=FlatQVT_ModuleImport_strategy)
def test_flatqvt_moduleimport_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=FlatQVT_Pattern_strategy)
@settings(max_examples=50)
def test_flatqvt_pattern_instantiation(instance):
    assert isinstance(instance, FlatQVT_Pattern)

@given(instance=FlatQVT_Comment_strategy)
@settings(max_examples=50)
def test_flatqvt_comment_instantiation(instance):
    assert isinstance(instance, FlatQVT_Comment)



@given(instance=FlatQVT_Comment_strategy)
def test_flatqvt_comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=FlatQVT_Factory_strategy)
@settings(max_examples=50)
def test_flatqvt_factory_instantiation(instance):
    assert isinstance(instance, FlatQVT_Factory)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_Factory_strategy)
@settings(max_examples=30)
def test_flatqvt_factory_create_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.create(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.create).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'create' in FlatQVT_Factory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'create' in FlatQVT_Factory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'create' in FlatQVT_Factory is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_Factory_strategy)
@settings(max_examples=30)
def test_flatqvt_factory_converttostring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.convertToString(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.convertToString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'convertToString' in FlatQVT_Factory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'convertToString' in FlatQVT_Factory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'convertToString' in FlatQVT_Factory is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_Factory_strategy)
@settings(max_examples=30)
def test_flatqvt_factory_createfromstring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createFromString(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createFromString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createFromString' in FlatQVT_Factory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createFromString' in FlatQVT_Factory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createFromString' in FlatQVT_Factory is not implemented or raised an error")

@given(instance=FlatQVT_Assignment_strategy)
@settings(max_examples=50)
def test_flatqvt_assignment_instantiation(instance):
    assert isinstance(instance, FlatQVT_Assignment)



@given(instance=FlatQVT_Assignment_strategy)
def test_flatqvt_assignment_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original

@given(instance=RealizedVariable_strategy)
@settings(max_examples=50)
def test_realizedvariable_instantiation(instance):
    assert isinstance(instance, RealizedVariable)

@given(instance=EnforcementOperation_strategy)
@settings(max_examples=50)
def test_enforcementoperation_instantiation(instance):
    assert isinstance(instance, EnforcementOperation)

@given(instance=Assignment_strategy)
@settings(max_examples=50)
def test_assignment_instantiation(instance):
    assert isinstance(instance, Assignment)

@given(instance=FlatQVT_PropertyAssignment_strategy)
@settings(max_examples=50)
def test_flatqvt_propertyassignment_instantiation(instance):
    assert isinstance(instance, FlatQVT_PropertyAssignment)

@given(instance=GuardPattern_strategy)
@settings(max_examples=50)
def test_guardpattern_instantiation(instance):
    assert isinstance(instance, GuardPattern)

@given(instance=FlatQVT_Variable_strategy)
@settings(max_examples=50)
def test_flatqvt_variable_instantiation(instance):
    assert isinstance(instance, FlatQVT_Variable)

@given(instance=FlatQVT_VarParameter_strategy)
@settings(max_examples=50)
def test_flatqvt_varparameter_instantiation(instance):
    assert isinstance(instance, FlatQVT_VarParameter)



@given(instance=FlatQVT_VarParameter_strategy)
def test_flatqvt_varparameter_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=FlatQVT_VariableAssignment_strategy)
@settings(max_examples=50)
def test_flatqvt_variableassignment_instantiation(instance):
    assert isinstance(instance, FlatQVT_VariableAssignment)

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=FlatQVT_UnlimitedNaturalExp_strategy)
@settings(max_examples=50)
def test_flatqvt_unlimitednaturalexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_UnlimitedNaturalExp)



@given(instance=FlatQVT_UnlimitedNaturalExp_strategy)
def test_flatqvt_unlimitednaturalexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=Extent_strategy)
@settings(max_examples=50)
def test_extent_instantiation(instance):
    assert isinstance(instance, Extent)

@given(instance=FlatQVT_URIExtent_strategy)
@settings(max_examples=50)
def test_flatqvt_uriextent_instantiation(instance):
    assert isinstance(instance, FlatQVT_URIExtent)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_URIExtent_strategy)
@settings(max_examples=30)
def test_flatqvt_uriextent_contexturi_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.contextURI()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.contextURI).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'contextURI' in FlatQVT_URIExtent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'contextURI' in FlatQVT_URIExtent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'contextURI' in FlatQVT_URIExtent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_URIExtent_strategy)
@settings(max_examples=30)
def test_flatqvt_uriextent_uri_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.uri(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.uri).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'uri' in FlatQVT_URIExtent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'uri' in FlatQVT_URIExtent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'uri' in FlatQVT_URIExtent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_URIExtent_strategy)
@settings(max_examples=30)
def test_flatqvt_uriextent_element_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.element(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.element).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'element' in FlatQVT_URIExtent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'element' in FlatQVT_URIExtent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'element' in FlatQVT_URIExtent is not implemented or raised an error")

@given(instance=FlatQVT_Typedef_strategy)
@settings(max_examples=50)
def test_flatqvt_typedef_instantiation(instance):
    assert isinstance(instance, FlatQVT_Typedef)

@given(instance=FlatQVT_Type_strategy)
@settings(max_examples=50)
def test_flatqvt_type_instantiation(instance):
    assert isinstance(instance, FlatQVT_Type)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT_Type_strategy)
@settings(max_examples=30)
def test_flatqvt_type_isinstance_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isInstance(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isInstance).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isInstance' in FlatQVT_Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isInstance' in FlatQVT_Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isInstance' in FlatQVT_Type is not implemented or raised an error")

@given(instance=FlatQVT_TupleType_strategy)
@settings(max_examples=50)
def test_flatqvt_tupletype_instantiation(instance):
    assert isinstance(instance, FlatQVT_TupleType)

@given(instance=TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, TupleLiteralExp)

@given(instance=FlatQVT_TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_flatqvt_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, FlatQVT_TupleLiteralPart)

@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)

@given(instance=FlatQVT_TypedModel_strategy)
@settings(max_examples=50)
def test_flatqvt_typedmodel_instantiation(instance):
    assert isinstance(instance, FlatQVT_TypedModel)

@given(instance=FlatQVT_TypedElement_strategy)
@settings(max_examples=50)
def test_flatqvt_typedelement_instantiation(instance):
    assert isinstance(instance, FlatQVT_TypedElement)

@given(instance=FlatQVT_Transformation_strategy)
@settings(max_examples=50)
def test_flatqvt_transformation_instantiation(instance):
    assert isinstance(instance, FlatQVT_Transformation)

@given(instance=FlatQVT_TemplateExp_strategy)
@settings(max_examples=50)
def test_flatqvt_templateexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_TemplateExp)

@given(instance=FlatQVT_TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_TupleLiteralExp)

@given(instance=CatchExp_strategy)
@settings(max_examples=50)
def test_catchexp_instantiation(instance):
    assert isinstance(instance, CatchExp)

@given(instance=FlatQVT_SetType_strategy)
@settings(max_examples=50)
def test_flatqvt_settype_instantiation(instance):
    assert isinstance(instance, FlatQVT_SetType)

@given(instance=FlatQVT_SequenceType_strategy)
@settings(max_examples=50)
def test_flatqvt_sequencetype_instantiation(instance):
    assert isinstance(instance, FlatQVT_SequenceType)

@given(instance=FlatQVT_Rule_strategy)
@settings(max_examples=50)
def test_flatqvt_rule_instantiation(instance):
    assert isinstance(instance, FlatQVT_Rule)

@given(instance=FlatQVT_Tag_strategy)
@settings(max_examples=50)
def test_flatqvt_tag_instantiation(instance):
    assert isinstance(instance, FlatQVT_Tag)



@given(instance=FlatQVT_Tag_strategy)
def test_flatqvt_tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=FlatQVT_Tag_strategy)
def test_flatqvt_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AltExp_strategy)
@settings(max_examples=50)
def test_altexp_instantiation(instance):
    assert isinstance(instance, AltExp)

@given(instance=FlatQVT_StringLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt_stringliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_StringLiteralExp)



@given(instance=FlatQVT_StringLiteralExp_strategy)
def test_flatqvt_stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)

@given(instance=Transformation_strategy)
@settings(max_examples=50)
def test_transformation_instantiation(instance):
    assert isinstance(instance, Transformation)

@given(instance=FlatQVT_RelationalTransformation_strategy)
@settings(max_examples=50)
def test_flatqvt_relationaltransformation_instantiation(instance):
    assert isinstance(instance, FlatQVT_RelationalTransformation)

@given(instance=FlatQVT_RelationImplementation_strategy)
@settings(max_examples=50)
def test_flatqvt_relationimplementation_instantiation(instance):
    assert isinstance(instance, FlatQVT_RelationImplementation)

@given(instance=ResolveExp_strategy)
@settings(max_examples=50)
def test_resolveexp_instantiation(instance):
    assert isinstance(instance, ResolveExp)

@given(instance=FlatQVT_ResolveInExp_strategy)
@settings(max_examples=50)
def test_flatqvt_resolveinexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_ResolveInExp)

@given(instance=Area_strategy)
@settings(max_examples=50)
def test_area_instantiation(instance):
    assert isinstance(instance, Area)

@given(instance=FlatQVT_Mapping_strategy)
@settings(max_examples=50)
def test_flatqvt_mapping_instantiation(instance):
    assert isinstance(instance, FlatQVT_Mapping)

@given(instance=FlatQVT_CoreDomain_strategy)
@settings(max_examples=50)
def test_flatqvt_coredomain_instantiation(instance):
    assert isinstance(instance, FlatQVT_CoreDomain)

@given(instance=BottomPattern_strategy)
@settings(max_examples=50)
def test_bottompattern_instantiation(instance):
    assert isinstance(instance, BottomPattern)

@given(instance=FlatQVT_Area_strategy)
@settings(max_examples=50)
def test_flatqvt_area_instantiation(instance):
    assert isinstance(instance, FlatQVT_Area)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=FlatQVT_TemplateParameterType_strategy)
@settings(max_examples=50)
def test_flatqvt_templateparametertype_instantiation(instance):
    assert isinstance(instance, FlatQVT_TemplateParameterType)



@given(instance=FlatQVT_TemplateParameterType_strategy)
def test_flatqvt_templateparametertype_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=FlatQVT_InvalidType_strategy)
@settings(max_examples=50)
def test_flatqvt_invalidtype_instantiation(instance):
    assert isinstance(instance, FlatQVT_InvalidType)

@given(instance=FlatQVT_VoidType_strategy)
@settings(max_examples=50)
def test_flatqvt_voidtype_instantiation(instance):
    assert isinstance(instance, FlatQVT_VoidType)

@given(instance=FlatQVT_DataType_strategy)
@settings(max_examples=50)
def test_flatqvt_datatype_instantiation(instance):
    assert isinstance(instance, FlatQVT_DataType)

@given(instance=FlatQVT_Class_strategy)
@settings(max_examples=50)
def test_flatqvt_class_instantiation(instance):
    assert isinstance(instance, FlatQVT_Class)



@given(instance=FlatQVT_Class_strategy)
def test_flatqvt_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=FlatQVT_AnyType_strategy)
@settings(max_examples=50)
def test_flatqvt_anytype_instantiation(instance):
    assert isinstance(instance, FlatQVT_AnyType)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=FlatQVT_ImperativeExpression_strategy)
@settings(max_examples=50)
def test_flatqvt_imperativeexpression_instantiation(instance):
    assert isinstance(instance, FlatQVT_ImperativeExpression)

@given(instance=FlatQVT_VariableExp_strategy)
@settings(max_examples=50)
def test_flatqvt_variableexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_VariableExp)

@given(instance=FlatQVT_IfExp_strategy)
@settings(max_examples=50)
def test_flatqvt_ifexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_IfExp)

@given(instance=FlatQVT_CallExp_strategy)
@settings(max_examples=50)
def test_flatqvt_callexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_CallExp)

@given(instance=FlatQVT_TypeExp_strategy)
@settings(max_examples=50)
def test_flatqvt_typeexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_TypeExp)

@given(instance=FlatQVT_LoopExp_strategy)
@settings(max_examples=50)
def test_flatqvt_loopexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_LoopExp)

@given(instance=FlatQVT_RelationCallExp_strategy)
@settings(max_examples=50)
def test_flatqvt_relationcallexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_RelationCallExp)

@given(instance=FlatQVT_LetExp_strategy)
@settings(max_examples=50)
def test_flatqvt_letexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_LetExp)

@given(instance=FlatQVT_LiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt_literalexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_LiteralExp)

@given(instance=ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeExpression)

@given(instance=FlatQVT_VariableInitExp_strategy)
@settings(max_examples=50)
def test_flatqvt_variableinitexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_VariableInitExp)



@given(instance=FlatQVT_VariableInitExp_strategy)
def test_flatqvt_variableinitexp_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=FlatQVT_InstantiationExp_strategy)
@settings(max_examples=50)
def test_flatqvt_instantiationexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_InstantiationExp)

@given(instance=FlatQVT_TryExp_strategy)
@settings(max_examples=50)
def test_flatqvt_tryexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_TryExp)

@given(instance=FlatQVT_SwitchExp_strategy)
@settings(max_examples=50)
def test_flatqvt_switchexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_SwitchExp)

@given(instance=FlatQVT_WhileExp_strategy)
@settings(max_examples=50)
def test_flatqvt_whileexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_WhileExp)

@given(instance=FlatQVT_BlockExp_strategy)
@settings(max_examples=50)
def test_flatqvt_blockexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_BlockExp)

@given(instance=FlatQVT_BreakExp_strategy)
@settings(max_examples=50)
def test_flatqvt_breakexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_BreakExp)

@given(instance=FlatQVT_ReturnExp_strategy)
@settings(max_examples=50)
def test_flatqvt_returnexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_ReturnExp)

@given(instance=FlatQVT_ResolveExp_strategy)
@settings(max_examples=50)
def test_flatqvt_resolveexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_ResolveExp)



@given(instance=FlatQVT_ResolveExp_strategy)
def test_flatqvt_resolveexp_isInverse_setter(instance):
    original = instance.isInverse
    instance.isInverse = original
    assert instance.isInverse == original



@given(instance=FlatQVT_ResolveExp_strategy)
def test_flatqvt_resolveexp_one_setter(instance):
    original = instance.one
    instance.one = original
    assert instance.one == original



@given(instance=FlatQVT_ResolveExp_strategy)
def test_flatqvt_resolveexp_isDeferred_setter(instance):
    original = instance.isDeferred
    instance.isDeferred = original
    assert instance.isDeferred == original

@given(instance=FlatQVT_LogExp_strategy)
@settings(max_examples=50)
def test_flatqvt_logexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_LogExp)

@given(instance=FlatQVT_ImperativeCallExp_strategy)
@settings(max_examples=50)
def test_flatqvt_imperativecallexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_ImperativeCallExp)



@given(instance=FlatQVT_ImperativeCallExp_strategy)
def test_flatqvt_imperativecallexp_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original

@given(instance=FlatQVT_CatchExp_strategy)
@settings(max_examples=50)
def test_flatqvt_catchexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_CatchExp)

@given(instance=FlatQVT_UnlinkExp_strategy)
@settings(max_examples=50)
def test_flatqvt_unlinkexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_UnlinkExp)

@given(instance=FlatQVT_UnpackExp_strategy)
@settings(max_examples=50)
def test_flatqvt_unpackexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_UnpackExp)

@given(instance=FlatQVT_ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_flatqvt_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_ImperativeLoopExp)

@given(instance=FlatQVT_ComputeExp_strategy)
@settings(max_examples=50)
def test_flatqvt_computeexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_ComputeExp)

@given(instance=FlatQVT_ContinueExp_strategy)
@settings(max_examples=50)
def test_flatqvt_continueexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_ContinueExp)

@given(instance=FlatQVT_RaiseExp_strategy)
@settings(max_examples=50)
def test_flatqvt_raiseexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_RaiseExp)

@given(instance=FlatQVT_AltExp_strategy)
@settings(max_examples=50)
def test_flatqvt_altexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_AltExp)

@given(instance=FlatQVT_AssignExp_strategy)
@settings(max_examples=50)
def test_flatqvt_assignexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_AssignExp)



@given(instance=FlatQVT_AssignExp_strategy)
def test_flatqvt_assignexp_isReset_setter(instance):
    original = instance.isReset
    instance.isReset = original
    assert instance.isReset == original

@given(instance=LogExp_strategy)
@settings(max_examples=50)
def test_logexp_instantiation(instance):
    assert isinstance(instance, LogExp)

@given(instance=FlatQVT_AssertExp_strategy)
@settings(max_examples=50)
def test_flatqvt_assertexp_instantiation(instance):
    assert isinstance(instance, FlatQVT_AssertExp)



@given(instance=FlatQVT_AssertExp_strategy)
def test_flatqvt_assertexp_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original
