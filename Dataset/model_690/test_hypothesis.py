import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TupleLiteralExp,
    essentialocl_OpaqueExpression,
    OpaqueExpression,
    essentialocl_ExpressionInOcl,
    TupleLiteralPart,
    CollectionLiteralExp,
    CollectionLiteralPart,
    essentialocl_CollectionItem,
    essentialocl_CollectionRange,
    FeaturePropertyCall,
    essentialocl_OperationCallExp,
    essentialocl_PropertyCallExp,
    ComputeExp,
    LetExp,
    PrimitiveLiteralExp,
    essentialocl_StringLiteralExp,
    essentialocl_NumericLiteralExp,
    essentialocl_BooleanLiteralExp,
    NumericLiteralExp,
    essentialocl_RealLiteralExp,
    essentialocl_IntegerLiteralExp,
    essentialocl_UnlimitedNaturalExp,
    TryExp,
    RelationalTransformation,
    DomainPattern,
    RelationImplementation,
    Key,
    Predicate,
    qvtcore_EnforcementOperation,
    TypedModel,
    qvtcore_Assignment,
    BottomPattern,
    Pattern,
    qvtrelation_DomainPattern,
    qvtcore_CorePattern,
    Domain,
    qvtrelation_RelationDomain,
    Mapping,
    Rule,
    qvtrelation_Relation,
    EnforcementOperation,
    RealizedVariable,
    Assignment,
    CollectionType,
    essentialocl_BagType,
    essentialocl_SetType,
    essentialocl_SequenceType,
    essentialocl_OrderedSetType,
    AltExp,
    CallExp,
    essentialocl_FeaturePropertyCall,
    ImperativeExpression,
    imperativeocl_AltExp,
    imperativeocl_UnlinkExp,
    imperativeocl_ComputeExp,
    imperativeocl_BreakExp,
    imperativeocl_SwitchExp,
    imperativeocl_VariableInitExp,
    imperativeocl_ReturnExp,
    imperativeocl_BlockExp,
    imperativeocl_AssignExp,
    ImperativeLoopExp,
    imperativeocl_ImperativeIterateExp,
    Property,
    ObjectTemplateExp,
    Element,
    qvtrelation_Key,
    qvtbase_Pattern,
    qvtbase_Predicate,
    qvtrelation_RelationImplementation,
    qvttemplate_PropertyTemplateItem,
    Class,
    Area,
    qvtcore_Mapping,
    qvtcore_CoreDomain,
    CorePattern,
    qvtcore_GuardPattern,
    qvtcore_BottomPattern,
    qvtoperational_ModuleImport,
    GuardPattern,
    qvtcore_Area,
    ConstructorBody,
    InstantiationExp,
    qvtoperational_ObjectExp,
    qvtoperational_OperationBody,
    OperationCallExp,
    qvtoperational_ImperativeCallExp,
    ModelType,
    ModuleImport,
    URIExtent,
    qvtoperational_ModelType,
    EntryOperation,
    ModelParameter,
    qvtoperational_ContextualProperty,
    ImperativeCallExp,
    qvtoperational_MappingCallExp,
    RelationDomain,
    VarParameter,
    qvtoperational_ModelParameter,
    qvtoperational_MappingParameter,
    Relation,
    MappingOperation,
    ResolveExp,
    qvtoperational_ResolveInExp,
    qvtoperational_ResolveExp,
    ImperativeOperation,
    qvtoperational_EntryOperation,
    qvtoperational_Constructor,
    qvtoperational_Helper,
    OperationBody,
    qvtoperational_ConstructorBody,
    qvtoperational_MappingBody,
    emof_Comment,
    Extent,
    emof_URIExtent,
    Parameter,
    Enumeration,
    Package,
    qvtoperational_Module,
    qvtbase_Transformation,
    NamedElement,
    emof_TypedElement,
    qvtbase_Domain,
    qvtbase_Rule,
    emof_EnumerationLiteral,
    emof_Type,
    qvtbase_TypedModel,
    emof_Package,
    emof_MultiplicityElement,
    imperativeocl_ListType,
    TypedElement,
    essentialocl_CollectionLiteralPart,
    essentialocl_TupleLiteralPart,
    essentialocl_OclExpression,
    essentialocl_Variable,
    MultiplicityElement,
    emof_Property,
    emof_Parameter,
    emof_Operation,
    emof_Object,
    emof_NamedElement,
    EnumerationLiteral,
    DataType,
    essentialocl_TupleType,
    emof_PrimitiveType,
    essentialocl_CollectionType,
    emof_Enumeration,
    Module,
    qvtoperational_Library,
    qvtoperational_OperationalTransformation,
    Transformation,
    qvtrelation_RelationalTransformation,
    emof_Tag,
    Comment,
    Tag,
    Object,
    emof_Extent,
    emof_Element,
    Operation,
    qvtoperational_ImperativeOperation,
    qvtoperational_MappingOperation,
    qvtbase_Function,
    imperativeocl_AnonymousTupleLiteralPart,
    AnonymousTupleLiteralPart,
    imperativeocl_AnonymousTupleType,
    imperativeocl_UnpackExp,
    imperativeocl_CollectorExp,
    LoopExp,
    essentialocl_IteratorExp,
    essentialocl_IterateExp,
    imperativeocl_ImperativeLoopExp,
    LogExp,
    imperativeocl_AssertExp,
    imperativeocl_TupleExp,
    imperativeocl_ForExp,
    imperativeocl_ContinueExp,
    imperativeocl_LogExp,
    imperativeocl_DictLiteralPart,
    DictLiteralPart,
    imperativeocl_DictionaryType,
    imperativeocl_InstantiationExp,
    imperativeocl_Typedef,
    imperativeocl_WhileExp,
    imperativeocl_RaiseExp,
    Type,
    emof_Class,
    imperativeocl_TemplateParameterType,
    essentialocl_InvalidType,
    essentialocl_AnyType,
    essentialocl_VoidType,
    emof_DataType,
    imperativeocl_TryExp,
    PropertyTemplateItem,
    TemplateExp,
    qvttemplate_CollectionTemplateExp,
    qvttemplate_ObjectTemplateExp,
    OclExpression,
    essentialocl_CallExp,
    essentialocl_TypeExp,
    essentialocl_LoopExp,
    essentialocl_LiteralExp,
    essentialocl_VariableExp,
    imperativeocl_ImperativeExpression,
    essentialocl_IfExp,
    essentialocl_LetExp,
    Variable,
    qvtoperational_VarParameter,
    qvtbase_FunctionParameter,
    qvtcore_RealizedVariable,
    LiteralExp,
    essentialocl_InvalidLiteralExp,
    imperativeocl_DictLiteralExp,
    essentialocl_NullLiteralExp,
    essentialocl_TupleLiteralExp,
    essentialocl_EnumLiteralExp,
    essentialocl_PrimitiveLiteralExp,
    essentialocl_CollectionLiteralExp,
    imperativeocl_AnonymousTupleLiteralExp,
    qvttemplate_TemplateExp,
    SeverityKind,
    EnforcementMode,
    ImportKind,
    DirectionKind,
    CollectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralExp)


def test_tupleliteralexp_constructor_exists():
    assert callable(TupleLiteralExp.__init__)


def test_tupleliteralexp_constructor_args():
    sig = inspect.signature(TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(essentialocl_OpaqueExpression)


def test_essentialocl_opaqueexpression_constructor_exists():
    assert callable(essentialocl_OpaqueExpression.__init__)


def test_essentialocl_opaqueexpression_constructor_args():
    sig = inspect.signature(essentialocl_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(OpaqueExpression)


def test_opaqueexpression_constructor_exists():
    assert callable(OpaqueExpression.__init__)


def test_opaqueexpression_constructor_args():
    sig = inspect.signature(OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_expressioninocl_is_not_abstract():
    assert not inspect.isabstract(essentialocl_ExpressionInOcl)


def test_essentialocl_expressioninocl_constructor_exists():
    assert callable(essentialocl_ExpressionInOcl.__init__)


def test_essentialocl_expressioninocl_constructor_args():
    sig = inspect.signature(essentialocl_ExpressionInOcl.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExp)


def test_collectionliteralexp_constructor_exists():
    assert callable(CollectionLiteralExp.__init__)


def test_collectionliteralexp_constructor_args():
    sig = inspect.signature(CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_collectionitem_is_not_abstract():
    assert not inspect.isabstract(essentialocl_CollectionItem)


def test_essentialocl_collectionitem_constructor_exists():
    assert callable(essentialocl_CollectionItem.__init__)


def test_essentialocl_collectionitem_constructor_args():
    sig = inspect.signature(essentialocl_CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_collectionrange_is_not_abstract():
    assert not inspect.isabstract(essentialocl_CollectionRange)


def test_essentialocl_collectionrange_constructor_exists():
    assert callable(essentialocl_CollectionRange.__init__)


def test_essentialocl_collectionrange_constructor_args():
    sig = inspect.signature(essentialocl_CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(FeaturePropertyCall)


def test_featurepropertycall_constructor_exists():
    assert callable(FeaturePropertyCall.__init__)


def test_featurepropertycall_constructor_args():
    sig = inspect.signature(FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_OperationCallExp)


def test_essentialocl_operationcallexp_constructor_exists():
    assert callable(essentialocl_OperationCallExp.__init__)


def test_essentialocl_operationcallexp_constructor_args():
    sig = inspect.signature(essentialocl_OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_PropertyCallExp)


def test_essentialocl_propertycallexp_constructor_exists():
    assert callable(essentialocl_PropertyCallExp.__init__)


def test_essentialocl_propertycallexp_constructor_args():
    sig = inspect.signature(essentialocl_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_computeexp_is_not_abstract():
    assert not inspect.isabstract(ComputeExp)


def test_computeexp_constructor_exists():
    assert callable(ComputeExp.__init__)


def test_computeexp_constructor_args():
    sig = inspect.signature(ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_letexp_is_not_abstract():
    assert not inspect.isabstract(LetExp)


def test_letexp_constructor_exists():
    assert callable(LetExp.__init__)


def test_letexp_constructor_args():
    sig = inspect.signature(LetExp.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_StringLiteralExp)


def test_essentialocl_stringliteralexp_constructor_exists():
    assert callable(essentialocl_StringLiteralExp.__init__)


def test_essentialocl_stringliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_essentialocl_stringliteralexp_has_stringSymbol():
    assert hasattr(essentialocl_StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in essentialocl_StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_NumericLiteralExp)


def test_essentialocl_numericliteralexp_constructor_exists():
    assert callable(essentialocl_NumericLiteralExp.__init__)


def test_essentialocl_numericliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_BooleanLiteralExp)


def test_essentialocl_booleanliteralexp_constructor_exists():
    assert callable(essentialocl_BooleanLiteralExp.__init__)


def test_essentialocl_booleanliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_essentialocl_booleanliteralexp_has_booleanSymbol():
    assert hasattr(essentialocl_BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in essentialocl_BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_realliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_RealLiteralExp)


def test_essentialocl_realliteralexp_constructor_exists():
    assert callable(essentialocl_RealLiteralExp.__init__)


def test_essentialocl_realliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_essentialocl_realliteralexp_has_realSymbol():
    assert hasattr(essentialocl_RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in essentialocl_RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl_integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_IntegerLiteralExp)


def test_essentialocl_integerliteralexp_constructor_exists():
    assert callable(essentialocl_IntegerLiteralExp.__init__)


def test_essentialocl_integerliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_essentialocl_integerliteralexp_has_integerSymbol():
    assert hasattr(essentialocl_IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in essentialocl_IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl_unlimitednaturalexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_UnlimitedNaturalExp)


def test_essentialocl_unlimitednaturalexp_constructor_exists():
    assert callable(essentialocl_UnlimitedNaturalExp.__init__)


def test_essentialocl_unlimitednaturalexp_constructor_args():
    sig = inspect.signature(essentialocl_UnlimitedNaturalExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_essentialocl_unlimitednaturalexp_has_symbol():
    assert hasattr(essentialocl_UnlimitedNaturalExp, "symbol")
    descriptor = None
    for klass in essentialocl_UnlimitedNaturalExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_tryexp_is_not_abstract():
    assert not inspect.isabstract(TryExp)


def test_tryexp_constructor_exists():
    assert callable(TryExp.__init__)


def test_tryexp_constructor_args():
    sig = inspect.signature(TryExp.__init__)
    params = list(sig.parameters.keys())



def test_relationaltransformation_is_not_abstract():
    assert not inspect.isabstract(RelationalTransformation)


def test_relationaltransformation_constructor_exists():
    assert callable(RelationalTransformation.__init__)


def test_relationaltransformation_constructor_args():
    sig = inspect.signature(RelationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_domainpattern_is_not_abstract():
    assert not inspect.isabstract(DomainPattern)


def test_domainpattern_constructor_exists():
    assert callable(DomainPattern.__init__)


def test_domainpattern_constructor_args():
    sig = inspect.signature(DomainPattern.__init__)
    params = list(sig.parameters.keys())



def test_relationimplementation_is_not_abstract():
    assert not inspect.isabstract(RelationImplementation)


def test_relationimplementation_constructor_exists():
    assert callable(RelationImplementation.__init__)


def test_relationimplementation_constructor_args():
    sig = inspect.signature(RelationImplementation.__init__)
    params = list(sig.parameters.keys())



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_enforcementoperation_is_not_abstract():
    assert not inspect.isabstract(qvtcore_EnforcementOperation)


def test_qvtcore_enforcementoperation_constructor_exists():
    assert callable(qvtcore_EnforcementOperation.__init__)


def test_qvtcore_enforcementoperation_constructor_args():
    sig = inspect.signature(qvtcore_EnforcementOperation.__init__)
    params = list(sig.parameters.keys())
    assert "enforcementMode" in params, "Missing parameter 'enforcementMode'"

def test_qvtcore_enforcementoperation_has_enforcementMode():
    assert hasattr(qvtcore_EnforcementOperation, "enforcementMode")
    descriptor = None
    for klass in qvtcore_EnforcementOperation.__mro__:
        if "enforcementMode" in klass.__dict__:
            descriptor = klass.__dict__["enforcementMode"]
            break
    assert isinstance(descriptor, property)



def test_typedmodel_is_not_abstract():
    assert not inspect.isabstract(TypedModel)


def test_typedmodel_constructor_exists():
    assert callable(TypedModel.__init__)


def test_typedmodel_constructor_args():
    sig = inspect.signature(TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_assignment_is_not_abstract():
    assert not inspect.isabstract(qvtcore_Assignment)


def test_qvtcore_assignment_constructor_exists():
    assert callable(qvtcore_Assignment.__init__)


def test_qvtcore_assignment_constructor_args():
    sig = inspect.signature(qvtcore_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "isDefault" in params, "Missing parameter 'isDefault'"

def test_qvtcore_assignment_has_isDefault():
    assert hasattr(qvtcore_Assignment, "isDefault")
    descriptor = None
    for klass in qvtcore_Assignment.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)



def test_bottompattern_is_not_abstract():
    assert not inspect.isabstract(BottomPattern)


def test_bottompattern_constructor_exists():
    assert callable(BottomPattern.__init__)


def test_bottompattern_constructor_args():
    sig = inspect.signature(BottomPattern.__init__)
    params = list(sig.parameters.keys())



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_domainpattern_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_DomainPattern)


def test_qvtrelation_domainpattern_constructor_exists():
    assert callable(qvtrelation_DomainPattern.__init__)


def test_qvtrelation_domainpattern_constructor_args():
    sig = inspect.signature(qvtrelation_DomainPattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_corepattern_is_not_abstract():
    assert not inspect.isabstract(qvtcore_CorePattern)


def test_qvtcore_corepattern_constructor_exists():
    assert callable(qvtcore_CorePattern.__init__)


def test_qvtcore_corepattern_constructor_args():
    sig = inspect.signature(qvtcore_CorePattern.__init__)
    params = list(sig.parameters.keys())



def test_domain_is_not_abstract():
    assert not inspect.isabstract(Domain)


def test_domain_constructor_exists():
    assert callable(Domain.__init__)


def test_domain_constructor_args():
    sig = inspect.signature(Domain.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_relationdomain_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_RelationDomain)


def test_qvtrelation_relationdomain_constructor_exists():
    assert callable(qvtrelation_RelationDomain.__init__)


def test_qvtrelation_relationdomain_constructor_args():
    sig = inspect.signature(qvtrelation_RelationDomain.__init__)
    params = list(sig.parameters.keys())



def test_mapping_is_not_abstract():
    assert not inspect.isabstract(Mapping)


def test_mapping_constructor_exists():
    assert callable(Mapping.__init__)


def test_mapping_constructor_args():
    sig = inspect.signature(Mapping.__init__)
    params = list(sig.parameters.keys())



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_relation_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_Relation)


def test_qvtrelation_relation_constructor_exists():
    assert callable(qvtrelation_Relation.__init__)


def test_qvtrelation_relation_constructor_args():
    sig = inspect.signature(qvtrelation_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "isTopLevel" in params, "Missing parameter 'isTopLevel'"

def test_qvtrelation_relation_has_isTopLevel():
    assert hasattr(qvtrelation_Relation, "isTopLevel")
    descriptor = None
    for klass in qvtrelation_Relation.__mro__:
        if "isTopLevel" in klass.__dict__:
            descriptor = klass.__dict__["isTopLevel"]
            break
    assert isinstance(descriptor, property)



def test_enforcementoperation_is_not_abstract():
    assert not inspect.isabstract(EnforcementOperation)


def test_enforcementoperation_constructor_exists():
    assert callable(EnforcementOperation.__init__)


def test_enforcementoperation_constructor_args():
    sig = inspect.signature(EnforcementOperation.__init__)
    params = list(sig.parameters.keys())



def test_realizedvariable_is_not_abstract():
    assert not inspect.isabstract(RealizedVariable)


def test_realizedvariable_constructor_exists():
    assert callable(RealizedVariable.__init__)


def test_realizedvariable_constructor_args():
    sig = inspect.signature(RealizedVariable.__init__)
    params = list(sig.parameters.keys())



def test_assignment_is_not_abstract():
    assert not inspect.isabstract(Assignment)


def test_assignment_constructor_exists():
    assert callable(Assignment.__init__)


def test_assignment_constructor_args():
    sig = inspect.signature(Assignment.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_bagtype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_BagType)


def test_essentialocl_bagtype_constructor_exists():
    assert callable(essentialocl_BagType.__init__)


def test_essentialocl_bagtype_constructor_args():
    sig = inspect.signature(essentialocl_BagType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_settype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_SetType)


def test_essentialocl_settype_constructor_exists():
    assert callable(essentialocl_SetType.__init__)


def test_essentialocl_settype_constructor_args():
    sig = inspect.signature(essentialocl_SetType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_sequencetype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_SequenceType)


def test_essentialocl_sequencetype_constructor_exists():
    assert callable(essentialocl_SequenceType.__init__)


def test_essentialocl_sequencetype_constructor_args():
    sig = inspect.signature(essentialocl_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_OrderedSetType)


def test_essentialocl_orderedsettype_constructor_exists():
    assert callable(essentialocl_OrderedSetType.__init__)


def test_essentialocl_orderedsettype_constructor_args():
    sig = inspect.signature(essentialocl_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_altexp_is_not_abstract():
    assert not inspect.isabstract(AltExp)


def test_altexp_constructor_exists():
    assert callable(AltExp.__init__)


def test_altexp_constructor_args():
    sig = inspect.signature(AltExp.__init__)
    params = list(sig.parameters.keys())



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(essentialocl_FeaturePropertyCall)


def test_essentialocl_featurepropertycall_constructor_exists():
    assert callable(essentialocl_FeaturePropertyCall.__init__)


def test_essentialocl_featurepropertycall_constructor_args():
    sig = inspect.signature(essentialocl_FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeExpression)


def test_imperativeexpression_constructor_exists():
    assert callable(ImperativeExpression.__init__)


def test_imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_altexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_AltExp)


def test_imperativeocl_altexp_constructor_exists():
    assert callable(imperativeocl_AltExp.__init__)


def test_imperativeocl_altexp_constructor_args():
    sig = inspect.signature(imperativeocl_AltExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_unlinkexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_UnlinkExp)


def test_imperativeocl_unlinkexp_constructor_exists():
    assert callable(imperativeocl_UnlinkExp.__init__)


def test_imperativeocl_unlinkexp_constructor_args():
    sig = inspect.signature(imperativeocl_UnlinkExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_computeexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ComputeExp)


def test_imperativeocl_computeexp_constructor_exists():
    assert callable(imperativeocl_ComputeExp.__init__)


def test_imperativeocl_computeexp_constructor_args():
    sig = inspect.signature(imperativeocl_ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_breakexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_BreakExp)


def test_imperativeocl_breakexp_constructor_exists():
    assert callable(imperativeocl_BreakExp.__init__)


def test_imperativeocl_breakexp_constructor_args():
    sig = inspect.signature(imperativeocl_BreakExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_switchexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_SwitchExp)


def test_imperativeocl_switchexp_constructor_exists():
    assert callable(imperativeocl_SwitchExp.__init__)


def test_imperativeocl_switchexp_constructor_args():
    sig = inspect.signature(imperativeocl_SwitchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_variableinitexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_VariableInitExp)


def test_imperativeocl_variableinitexp_constructor_exists():
    assert callable(imperativeocl_VariableInitExp.__init__)


def test_imperativeocl_variableinitexp_constructor_args():
    sig = inspect.signature(imperativeocl_VariableInitExp.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_imperativeocl_variableinitexp_has_withResult():
    assert hasattr(imperativeocl_VariableInitExp, "withResult")
    descriptor = None
    for klass in imperativeocl_VariableInitExp.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl_returnexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ReturnExp)


def test_imperativeocl_returnexp_constructor_exists():
    assert callable(imperativeocl_ReturnExp.__init__)


def test_imperativeocl_returnexp_constructor_args():
    sig = inspect.signature(imperativeocl_ReturnExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_blockexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_BlockExp)


def test_imperativeocl_blockexp_constructor_exists():
    assert callable(imperativeocl_BlockExp.__init__)


def test_imperativeocl_blockexp_constructor_args():
    sig = inspect.signature(imperativeocl_BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_assignexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_AssignExp)


def test_imperativeocl_assignexp_constructor_exists():
    assert callable(imperativeocl_AssignExp.__init__)


def test_imperativeocl_assignexp_constructor_args():
    sig = inspect.signature(imperativeocl_AssignExp.__init__)
    params = list(sig.parameters.keys())
    assert "isReset" in params, "Missing parameter 'isReset'"

def test_imperativeocl_assignexp_has_isReset():
    assert hasattr(imperativeocl_AssignExp, "isReset")
    descriptor = None
    for klass in imperativeocl_AssignExp.__mro__:
        if "isReset" in klass.__dict__:
            descriptor = klass.__dict__["isReset"]
            break
    assert isinstance(descriptor, property)



def test_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExp)


def test_imperativeloopexp_constructor_exists():
    assert callable(ImperativeLoopExp.__init__)


def test_imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_imperativeiterateexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ImperativeIterateExp)


def test_imperativeocl_imperativeiterateexp_constructor_exists():
    assert callable(imperativeocl_ImperativeIterateExp.__init__)


def test_imperativeocl_imperativeiterateexp_constructor_args():
    sig = inspect.signature(imperativeocl_ImperativeIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(ObjectTemplateExp)


def test_objecttemplateexp_constructor_exists():
    assert callable(ObjectTemplateExp.__init__)


def test_objecttemplateexp_constructor_args():
    sig = inspect.signature(ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_key_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_Key)


def test_qvtrelation_key_constructor_exists():
    assert callable(qvtrelation_Key.__init__)


def test_qvtrelation_key_constructor_args():
    sig = inspect.signature(qvtrelation_Key.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase_pattern_is_not_abstract():
    assert not inspect.isabstract(qvtbase_Pattern)


def test_qvtbase_pattern_constructor_exists():
    assert callable(qvtbase_Pattern.__init__)


def test_qvtbase_pattern_constructor_args():
    sig = inspect.signature(qvtbase_Pattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase_predicate_is_not_abstract():
    assert not inspect.isabstract(qvtbase_Predicate)


def test_qvtbase_predicate_constructor_exists():
    assert callable(qvtbase_Predicate.__init__)


def test_qvtbase_predicate_constructor_args():
    sig = inspect.signature(qvtbase_Predicate.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_relationimplementation_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_RelationImplementation)


def test_qvtrelation_relationimplementation_constructor_exists():
    assert callable(qvtrelation_RelationImplementation.__init__)


def test_qvtrelation_relationimplementation_constructor_args():
    sig = inspect.signature(qvtrelation_RelationImplementation.__init__)
    params = list(sig.parameters.keys())



def test_qvttemplate_propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(qvttemplate_PropertyTemplateItem)


def test_qvttemplate_propertytemplateitem_constructor_exists():
    assert callable(qvttemplate_PropertyTemplateItem.__init__)


def test_qvttemplate_propertytemplateitem_constructor_args():
    sig = inspect.signature(qvttemplate_PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_area_is_not_abstract():
    assert not inspect.isabstract(Area)


def test_area_constructor_exists():
    assert callable(Area.__init__)


def test_area_constructor_args():
    sig = inspect.signature(Area.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_mapping_is_not_abstract():
    assert not inspect.isabstract(qvtcore_Mapping)


def test_qvtcore_mapping_constructor_exists():
    assert callable(qvtcore_Mapping.__init__)


def test_qvtcore_mapping_constructor_args():
    sig = inspect.signature(qvtcore_Mapping.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_coredomain_is_not_abstract():
    assert not inspect.isabstract(qvtcore_CoreDomain)


def test_qvtcore_coredomain_constructor_exists():
    assert callable(qvtcore_CoreDomain.__init__)


def test_qvtcore_coredomain_constructor_args():
    sig = inspect.signature(qvtcore_CoreDomain.__init__)
    params = list(sig.parameters.keys())



def test_corepattern_is_not_abstract():
    assert not inspect.isabstract(CorePattern)


def test_corepattern_constructor_exists():
    assert callable(CorePattern.__init__)


def test_corepattern_constructor_args():
    sig = inspect.signature(CorePattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_guardpattern_is_not_abstract():
    assert not inspect.isabstract(qvtcore_GuardPattern)


def test_qvtcore_guardpattern_constructor_exists():
    assert callable(qvtcore_GuardPattern.__init__)


def test_qvtcore_guardpattern_constructor_args():
    sig = inspect.signature(qvtcore_GuardPattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_bottompattern_is_not_abstract():
    assert not inspect.isabstract(qvtcore_BottomPattern)


def test_qvtcore_bottompattern_constructor_exists():
    assert callable(qvtcore_BottomPattern.__init__)


def test_qvtcore_bottompattern_constructor_args():
    sig = inspect.signature(qvtcore_BottomPattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_moduleimport_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_ModuleImport)


def test_qvtoperational_moduleimport_constructor_exists():
    assert callable(qvtoperational_ModuleImport.__init__)


def test_qvtoperational_moduleimport_constructor_args():
    sig = inspect.signature(qvtoperational_ModuleImport.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_qvtoperational_moduleimport_has_kind():
    assert hasattr(qvtoperational_ModuleImport, "kind")
    descriptor = None
    for klass in qvtoperational_ModuleImport.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_guardpattern_is_not_abstract():
    assert not inspect.isabstract(GuardPattern)


def test_guardpattern_constructor_exists():
    assert callable(GuardPattern.__init__)


def test_guardpattern_constructor_args():
    sig = inspect.signature(GuardPattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_area_is_not_abstract():
    assert not inspect.isabstract(qvtcore_Area)


def test_qvtcore_area_constructor_exists():
    assert callable(qvtcore_Area.__init__)


def test_qvtcore_area_constructor_args():
    sig = inspect.signature(qvtcore_Area.__init__)
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



def test_qvtoperational_objectexp_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_ObjectExp)


def test_qvtoperational_objectexp_constructor_exists():
    assert callable(qvtoperational_ObjectExp.__init__)


def test_qvtoperational_objectexp_constructor_args():
    sig = inspect.signature(qvtoperational_ObjectExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_operationbody_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_OperationBody)


def test_qvtoperational_operationbody_constructor_exists():
    assert callable(qvtoperational_OperationBody.__init__)


def test_qvtoperational_operationbody_constructor_args():
    sig = inspect.signature(qvtoperational_OperationBody.__init__)
    params = list(sig.parameters.keys())



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_imperativecallexp_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_ImperativeCallExp)


def test_qvtoperational_imperativecallexp_constructor_exists():
    assert callable(qvtoperational_ImperativeCallExp.__init__)


def test_qvtoperational_imperativecallexp_constructor_args():
    sig = inspect.signature(qvtoperational_ImperativeCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"

def test_qvtoperational_imperativecallexp_has_isVirtual():
    assert hasattr(qvtoperational_ImperativeCallExp, "isVirtual")
    descriptor = None
    for klass in qvtoperational_ImperativeCallExp.__mro__:
        if "isVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isVirtual"]
            break
    assert isinstance(descriptor, property)



def test_modeltype_is_not_abstract():
    assert not inspect.isabstract(ModelType)


def test_modeltype_constructor_exists():
    assert callable(ModelType.__init__)


def test_modeltype_constructor_args():
    sig = inspect.signature(ModelType.__init__)
    params = list(sig.parameters.keys())



def test_moduleimport_is_not_abstract():
    assert not inspect.isabstract(ModuleImport)


def test_moduleimport_constructor_exists():
    assert callable(ModuleImport.__init__)


def test_moduleimport_constructor_args():
    sig = inspect.signature(ModuleImport.__init__)
    params = list(sig.parameters.keys())



def test_uriextent_is_not_abstract():
    assert not inspect.isabstract(URIExtent)


def test_uriextent_constructor_exists():
    assert callable(URIExtent.__init__)


def test_uriextent_constructor_args():
    sig = inspect.signature(URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_modeltype_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_ModelType)


def test_qvtoperational_modeltype_constructor_exists():
    assert callable(qvtoperational_ModelType.__init__)


def test_qvtoperational_modeltype_constructor_args():
    sig = inspect.signature(qvtoperational_ModelType.__init__)
    params = list(sig.parameters.keys())
    assert "conformanceKind" in params, "Missing parameter 'conformanceKind'"

def test_qvtoperational_modeltype_has_conformanceKind():
    assert hasattr(qvtoperational_ModelType, "conformanceKind")
    descriptor = None
    for klass in qvtoperational_ModelType.__mro__:
        if "conformanceKind" in klass.__dict__:
            descriptor = klass.__dict__["conformanceKind"]
            break
    assert isinstance(descriptor, property)



def test_entryoperation_is_not_abstract():
    assert not inspect.isabstract(EntryOperation)


def test_entryoperation_constructor_exists():
    assert callable(EntryOperation.__init__)


def test_entryoperation_constructor_args():
    sig = inspect.signature(EntryOperation.__init__)
    params = list(sig.parameters.keys())



def test_modelparameter_is_not_abstract():
    assert not inspect.isabstract(ModelParameter)


def test_modelparameter_constructor_exists():
    assert callable(ModelParameter.__init__)


def test_modelparameter_constructor_args():
    sig = inspect.signature(ModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_contextualproperty_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_ContextualProperty)


def test_qvtoperational_contextualproperty_constructor_exists():
    assert callable(qvtoperational_ContextualProperty.__init__)


def test_qvtoperational_contextualproperty_constructor_args():
    sig = inspect.signature(qvtoperational_ContextualProperty.__init__)
    params = list(sig.parameters.keys())



def test_imperativecallexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeCallExp)


def test_imperativecallexp_constructor_exists():
    assert callable(ImperativeCallExp.__init__)


def test_imperativecallexp_constructor_args():
    sig = inspect.signature(ImperativeCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_mappingcallexp_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_MappingCallExp)


def test_qvtoperational_mappingcallexp_constructor_exists():
    assert callable(qvtoperational_MappingCallExp.__init__)


def test_qvtoperational_mappingcallexp_constructor_args():
    sig = inspect.signature(qvtoperational_MappingCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isStrict" in params, "Missing parameter 'isStrict'"

def test_qvtoperational_mappingcallexp_has_isStrict():
    assert hasattr(qvtoperational_MappingCallExp, "isStrict")
    descriptor = None
    for klass in qvtoperational_MappingCallExp.__mro__:
        if "isStrict" in klass.__dict__:
            descriptor = klass.__dict__["isStrict"]
            break
    assert isinstance(descriptor, property)



def test_relationdomain_is_not_abstract():
    assert not inspect.isabstract(RelationDomain)


def test_relationdomain_constructor_exists():
    assert callable(RelationDomain.__init__)


def test_relationdomain_constructor_args():
    sig = inspect.signature(RelationDomain.__init__)
    params = list(sig.parameters.keys())



def test_varparameter_is_not_abstract():
    assert not inspect.isabstract(VarParameter)


def test_varparameter_constructor_exists():
    assert callable(VarParameter.__init__)


def test_varparameter_constructor_args():
    sig = inspect.signature(VarParameter.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_modelparameter_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_ModelParameter)


def test_qvtoperational_modelparameter_constructor_exists():
    assert callable(qvtoperational_ModelParameter.__init__)


def test_qvtoperational_modelparameter_constructor_args():
    sig = inspect.signature(qvtoperational_ModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_mappingparameter_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_MappingParameter)


def test_qvtoperational_mappingparameter_constructor_exists():
    assert callable(qvtoperational_MappingParameter.__init__)


def test_qvtoperational_mappingparameter_constructor_args():
    sig = inspect.signature(qvtoperational_MappingParameter.__init__)
    params = list(sig.parameters.keys())



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



def test_resolveexp_is_not_abstract():
    assert not inspect.isabstract(ResolveExp)


def test_resolveexp_constructor_exists():
    assert callable(ResolveExp.__init__)


def test_resolveexp_constructor_args():
    sig = inspect.signature(ResolveExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_resolveinexp_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_ResolveInExp)


def test_qvtoperational_resolveinexp_constructor_exists():
    assert callable(qvtoperational_ResolveInExp.__init__)


def test_qvtoperational_resolveinexp_constructor_args():
    sig = inspect.signature(qvtoperational_ResolveInExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_resolveexp_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_ResolveExp)


def test_qvtoperational_resolveexp_constructor_exists():
    assert callable(qvtoperational_ResolveExp.__init__)


def test_qvtoperational_resolveexp_constructor_args():
    sig = inspect.signature(qvtoperational_ResolveExp.__init__)
    params = list(sig.parameters.keys())
    assert "isDeferred" in params, "Missing parameter 'isDeferred'"
    assert "one" in params, "Missing parameter 'one'"
    assert "isInverse" in params, "Missing parameter 'isInverse'"

def test_qvtoperational_resolveexp_has_isDeferred():
    assert hasattr(qvtoperational_ResolveExp, "isDeferred")
    descriptor = None
    for klass in qvtoperational_ResolveExp.__mro__:
        if "isDeferred" in klass.__dict__:
            descriptor = klass.__dict__["isDeferred"]
            break
    assert isinstance(descriptor, property)

def test_qvtoperational_resolveexp_has_one():
    assert hasattr(qvtoperational_ResolveExp, "one")
    descriptor = None
    for klass in qvtoperational_ResolveExp.__mro__:
        if "one" in klass.__dict__:
            descriptor = klass.__dict__["one"]
            break
    assert isinstance(descriptor, property)

def test_qvtoperational_resolveexp_has_isInverse():
    assert hasattr(qvtoperational_ResolveExp, "isInverse")
    descriptor = None
    for klass in qvtoperational_ResolveExp.__mro__:
        if "isInverse" in klass.__dict__:
            descriptor = klass.__dict__["isInverse"]
            break
    assert isinstance(descriptor, property)



def test_imperativeoperation_is_not_abstract():
    assert not inspect.isabstract(ImperativeOperation)


def test_imperativeoperation_constructor_exists():
    assert callable(ImperativeOperation.__init__)


def test_imperativeoperation_constructor_args():
    sig = inspect.signature(ImperativeOperation.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_entryoperation_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_EntryOperation)


def test_qvtoperational_entryoperation_constructor_exists():
    assert callable(qvtoperational_EntryOperation.__init__)


def test_qvtoperational_entryoperation_constructor_args():
    sig = inspect.signature(qvtoperational_EntryOperation.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_constructor_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_Constructor)


def test_qvtoperational_constructor_constructor_exists():
    assert callable(qvtoperational_Constructor.__init__)


def test_qvtoperational_constructor_constructor_args():
    sig = inspect.signature(qvtoperational_Constructor.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_helper_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_Helper)


def test_qvtoperational_helper_constructor_exists():
    assert callable(qvtoperational_Helper.__init__)


def test_qvtoperational_helper_constructor_args():
    sig = inspect.signature(qvtoperational_Helper.__init__)
    params = list(sig.parameters.keys())
    assert "isQuery" in params, "Missing parameter 'isQuery'"

def test_qvtoperational_helper_has_isQuery():
    assert hasattr(qvtoperational_Helper, "isQuery")
    descriptor = None
    for klass in qvtoperational_Helper.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)



def test_operationbody_is_not_abstract():
    assert not inspect.isabstract(OperationBody)


def test_operationbody_constructor_exists():
    assert callable(OperationBody.__init__)


def test_operationbody_constructor_args():
    sig = inspect.signature(OperationBody.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_constructorbody_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_ConstructorBody)


def test_qvtoperational_constructorbody_constructor_exists():
    assert callable(qvtoperational_ConstructorBody.__init__)


def test_qvtoperational_constructorbody_constructor_args():
    sig = inspect.signature(qvtoperational_ConstructorBody.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_mappingbody_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_MappingBody)


def test_qvtoperational_mappingbody_constructor_exists():
    assert callable(qvtoperational_MappingBody.__init__)


def test_qvtoperational_mappingbody_constructor_args():
    sig = inspect.signature(qvtoperational_MappingBody.__init__)
    params = list(sig.parameters.keys())



def test_emof_comment_is_not_abstract():
    assert not inspect.isabstract(emof_Comment)


def test_emof_comment_constructor_exists():
    assert callable(emof_Comment.__init__)


def test_emof_comment_constructor_args():
    sig = inspect.signature(emof_Comment.__init__)
    params = list(sig.parameters.keys())



def test_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_emof_uriextent_is_not_abstract():
    assert not inspect.isabstract(emof_URIExtent)


def test_emof_uriextent_constructor_exists():
    assert callable(emof_URIExtent.__init__)


def test_emof_uriextent_constructor_args():
    sig = inspect.signature(emof_URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_enumeration_is_not_abstract():
    assert not inspect.isabstract(Enumeration)


def test_enumeration_constructor_exists():
    assert callable(Enumeration.__init__)


def test_enumeration_constructor_args():
    sig = inspect.signature(Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_module_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_Module)


def test_qvtoperational_module_constructor_exists():
    assert callable(qvtoperational_Module.__init__)


def test_qvtoperational_module_constructor_args():
    sig = inspect.signature(qvtoperational_Module.__init__)
    params = list(sig.parameters.keys())
    assert "isBlackbox" in params, "Missing parameter 'isBlackbox'"

def test_qvtoperational_module_has_isBlackbox():
    assert hasattr(qvtoperational_Module, "isBlackbox")
    descriptor = None
    for klass in qvtoperational_Module.__mro__:
        if "isBlackbox" in klass.__dict__:
            descriptor = klass.__dict__["isBlackbox"]
            break
    assert isinstance(descriptor, property)



def test_qvtbase_transformation_is_not_abstract():
    assert not inspect.isabstract(qvtbase_Transformation)


def test_qvtbase_transformation_constructor_exists():
    assert callable(qvtbase_Transformation.__init__)


def test_qvtbase_transformation_constructor_args():
    sig = inspect.signature(qvtbase_Transformation.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_emof_typedelement_is_not_abstract():
    assert not inspect.isabstract(emof_TypedElement)


def test_emof_typedelement_constructor_exists():
    assert callable(emof_TypedElement.__init__)


def test_emof_typedelement_constructor_args():
    sig = inspect.signature(emof_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase_domain_is_not_abstract():
    assert not inspect.isabstract(qvtbase_Domain)


def test_qvtbase_domain_constructor_exists():
    assert callable(qvtbase_Domain.__init__)


def test_qvtbase_domain_constructor_args():
    sig = inspect.signature(qvtbase_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "isCheckable" in params, "Missing parameter 'isCheckable'"
    assert "isEnforceable" in params, "Missing parameter 'isEnforceable'"

def test_qvtbase_domain_has_isCheckable():
    assert hasattr(qvtbase_Domain, "isCheckable")
    descriptor = None
    for klass in qvtbase_Domain.__mro__:
        if "isCheckable" in klass.__dict__:
            descriptor = klass.__dict__["isCheckable"]
            break
    assert isinstance(descriptor, property)

def test_qvtbase_domain_has_isEnforceable():
    assert hasattr(qvtbase_Domain, "isEnforceable")
    descriptor = None
    for klass in qvtbase_Domain.__mro__:
        if "isEnforceable" in klass.__dict__:
            descriptor = klass.__dict__["isEnforceable"]
            break
    assert isinstance(descriptor, property)



def test_qvtbase_rule_is_not_abstract():
    assert not inspect.isabstract(qvtbase_Rule)


def test_qvtbase_rule_constructor_exists():
    assert callable(qvtbase_Rule.__init__)


def test_qvtbase_rule_constructor_args():
    sig = inspect.signature(qvtbase_Rule.__init__)
    params = list(sig.parameters.keys())



def test_emof_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(emof_EnumerationLiteral)


def test_emof_enumerationliteral_constructor_exists():
    assert callable(emof_EnumerationLiteral.__init__)


def test_emof_enumerationliteral_constructor_args():
    sig = inspect.signature(emof_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_emof_type_is_not_abstract():
    assert not inspect.isabstract(emof_Type)


def test_emof_type_constructor_exists():
    assert callable(emof_Type.__init__)


def test_emof_type_constructor_args():
    sig = inspect.signature(emof_Type.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase_typedmodel_is_not_abstract():
    assert not inspect.isabstract(qvtbase_TypedModel)


def test_qvtbase_typedmodel_constructor_exists():
    assert callable(qvtbase_TypedModel.__init__)


def test_qvtbase_typedmodel_constructor_args():
    sig = inspect.signature(qvtbase_TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_emof_package_is_not_abstract():
    assert not inspect.isabstract(emof_Package)


def test_emof_package_constructor_exists():
    assert callable(emof_Package.__init__)


def test_emof_package_constructor_args():
    sig = inspect.signature(emof_Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_emof_package_has_uri():
    assert hasattr(emof_Package, "uri")
    descriptor = None
    for klass in emof_Package.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_emof_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(emof_MultiplicityElement)


def test_emof_multiplicityelement_constructor_exists():
    assert callable(emof_MultiplicityElement.__init__)


def test_emof_multiplicityelement_constructor_args():
    sig = inspect.signature(emof_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_emof_multiplicityelement_has_isOrdered():
    assert hasattr(emof_MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in emof_MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_emof_multiplicityelement_has_isUnique():
    assert hasattr(emof_MultiplicityElement, "isUnique")
    descriptor = None
    for klass in emof_MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_emof_multiplicityelement_has_upper():
    assert hasattr(emof_MultiplicityElement, "upper")
    descriptor = None
    for klass in emof_MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_emof_multiplicityelement_has_lower():
    assert hasattr(emof_MultiplicityElement, "lower")
    descriptor = None
    for klass in emof_MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl_listtype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ListType)


def test_imperativeocl_listtype_constructor_exists():
    assert callable(imperativeocl_ListType.__init__)


def test_imperativeocl_listtype_constructor_args():
    sig = inspect.signature(imperativeocl_ListType.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(essentialocl_CollectionLiteralPart)


def test_essentialocl_collectionliteralpart_constructor_exists():
    assert callable(essentialocl_CollectionLiteralPart.__init__)


def test_essentialocl_collectionliteralpart_constructor_args():
    sig = inspect.signature(essentialocl_CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(essentialocl_TupleLiteralPart)


def test_essentialocl_tupleliteralpart_constructor_exists():
    assert callable(essentialocl_TupleLiteralPart.__init__)


def test_essentialocl_tupleliteralpart_constructor_args():
    sig = inspect.signature(essentialocl_TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(essentialocl_OclExpression)


def test_essentialocl_oclexpression_constructor_exists():
    assert callable(essentialocl_OclExpression.__init__)


def test_essentialocl_oclexpression_constructor_args():
    sig = inspect.signature(essentialocl_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_variable_is_not_abstract():
    assert not inspect.isabstract(essentialocl_Variable)


def test_essentialocl_variable_constructor_exists():
    assert callable(essentialocl_Variable.__init__)


def test_essentialocl_variable_constructor_args():
    sig = inspect.signature(essentialocl_Variable.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_emof_property_is_not_abstract():
    assert not inspect.isabstract(emof_Property)


def test_emof_property_constructor_exists():
    assert callable(emof_Property.__init__)


def test_emof_property_constructor_args():
    sig = inspect.signature(emof_Property.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isId" in params, "Missing parameter 'isId'"

def test_emof_property_has_default():
    assert hasattr(emof_Property, "default")
    descriptor = None
    for klass in emof_Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_emof_property_has_isDerived():
    assert hasattr(emof_Property, "isDerived")
    descriptor = None
    for klass in emof_Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_emof_property_has_isReadOnly():
    assert hasattr(emof_Property, "isReadOnly")
    descriptor = None
    for klass in emof_Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_emof_property_has_isComposite():
    assert hasattr(emof_Property, "isComposite")
    descriptor = None
    for klass in emof_Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_emof_property_has_isId():
    assert hasattr(emof_Property, "isId")
    descriptor = None
    for klass in emof_Property.__mro__:
        if "isId" in klass.__dict__:
            descriptor = klass.__dict__["isId"]
            break
    assert isinstance(descriptor, property)



def test_emof_parameter_is_not_abstract():
    assert not inspect.isabstract(emof_Parameter)


def test_emof_parameter_constructor_exists():
    assert callable(emof_Parameter.__init__)


def test_emof_parameter_constructor_args():
    sig = inspect.signature(emof_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_emof_operation_is_not_abstract():
    assert not inspect.isabstract(emof_Operation)


def test_emof_operation_constructor_exists():
    assert callable(emof_Operation.__init__)


def test_emof_operation_constructor_args():
    sig = inspect.signature(emof_Operation.__init__)
    params = list(sig.parameters.keys())



def test_emof_object_is_not_abstract():
    assert not inspect.isabstract(emof_Object)


def test_emof_object_constructor_exists():
    assert callable(emof_Object.__init__)


def test_emof_object_constructor_args():
    sig = inspect.signature(emof_Object.__init__)
    params = list(sig.parameters.keys())



def test_emof_namedelement_is_not_abstract():
    assert not inspect.isabstract(emof_NamedElement)


def test_emof_namedelement_constructor_exists():
    assert callable(emof_NamedElement.__init__)


def test_emof_namedelement_constructor_args():
    sig = inspect.signature(emof_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emof_namedelement_has_name():
    assert hasattr(emof_NamedElement, "name")
    descriptor = None
    for klass in emof_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_tupletype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_TupleType)


def test_essentialocl_tupletype_constructor_exists():
    assert callable(essentialocl_TupleType.__init__)


def test_essentialocl_tupletype_constructor_args():
    sig = inspect.signature(essentialocl_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_emof_primitivetype_is_not_abstract():
    assert not inspect.isabstract(emof_PrimitiveType)


def test_emof_primitivetype_constructor_exists():
    assert callable(emof_PrimitiveType.__init__)


def test_emof_primitivetype_constructor_args():
    sig = inspect.signature(emof_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_collectiontype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_CollectionType)


def test_essentialocl_collectiontype_constructor_exists():
    assert callable(essentialocl_CollectionType.__init__)


def test_essentialocl_collectiontype_constructor_args():
    sig = inspect.signature(essentialocl_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_emof_enumeration_is_not_abstract():
    assert not inspect.isabstract(emof_Enumeration)


def test_emof_enumeration_constructor_exists():
    assert callable(emof_Enumeration.__init__)


def test_emof_enumeration_constructor_args():
    sig = inspect.signature(emof_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_library_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_Library)


def test_qvtoperational_library_constructor_exists():
    assert callable(qvtoperational_Library.__init__)


def test_qvtoperational_library_constructor_args():
    sig = inspect.signature(qvtoperational_Library.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_operationaltransformation_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_OperationalTransformation)


def test_qvtoperational_operationaltransformation_constructor_exists():
    assert callable(qvtoperational_OperationalTransformation.__init__)


def test_qvtoperational_operationaltransformation_constructor_args():
    sig = inspect.signature(qvtoperational_OperationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_transformation_is_not_abstract():
    assert not inspect.isabstract(Transformation)


def test_transformation_constructor_exists():
    assert callable(Transformation.__init__)


def test_transformation_constructor_args():
    sig = inspect.signature(Transformation.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_relationaltransformation_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_RelationalTransformation)


def test_qvtrelation_relationaltransformation_constructor_exists():
    assert callable(qvtrelation_RelationalTransformation.__init__)


def test_qvtrelation_relationaltransformation_constructor_args():
    sig = inspect.signature(qvtrelation_RelationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_emof_tag_is_not_abstract():
    assert not inspect.isabstract(emof_Tag)


def test_emof_tag_constructor_exists():
    assert callable(emof_Tag.__init__)


def test_emof_tag_constructor_args():
    sig = inspect.signature(emof_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_emof_tag_has_name():
    assert hasattr(emof_Tag, "name")
    descriptor = None
    for klass in emof_Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_emof_tag_has_value():
    assert hasattr(emof_Tag, "value")
    descriptor = None
    for klass in emof_Tag.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_tag_is_not_abstract():
    assert not inspect.isabstract(Tag)


def test_tag_constructor_exists():
    assert callable(Tag.__init__)


def test_tag_constructor_args():
    sig = inspect.signature(Tag.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_emof_extent_is_not_abstract():
    assert not inspect.isabstract(emof_Extent)


def test_emof_extent_constructor_exists():
    assert callable(emof_Extent.__init__)


def test_emof_extent_constructor_args():
    sig = inspect.signature(emof_Extent.__init__)
    params = list(sig.parameters.keys())



def test_emof_element_is_not_abstract():
    assert not inspect.isabstract(emof_Element)


def test_emof_element_constructor_exists():
    assert callable(emof_Element.__init__)


def test_emof_element_constructor_args():
    sig = inspect.signature(emof_Element.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_imperativeoperation_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_ImperativeOperation)


def test_qvtoperational_imperativeoperation_constructor_exists():
    assert callable(qvtoperational_ImperativeOperation.__init__)


def test_qvtoperational_imperativeoperation_constructor_args():
    sig = inspect.signature(qvtoperational_ImperativeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "isBlackbox" in params, "Missing parameter 'isBlackbox'"

def test_qvtoperational_imperativeoperation_has_isBlackbox():
    assert hasattr(qvtoperational_ImperativeOperation, "isBlackbox")
    descriptor = None
    for klass in qvtoperational_ImperativeOperation.__mro__:
        if "isBlackbox" in klass.__dict__:
            descriptor = klass.__dict__["isBlackbox"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_mappingoperation_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_MappingOperation)


def test_qvtoperational_mappingoperation_constructor_exists():
    assert callable(qvtoperational_MappingOperation.__init__)


def test_qvtoperational_mappingoperation_constructor_args():
    sig = inspect.signature(qvtoperational_MappingOperation.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase_function_is_not_abstract():
    assert not inspect.isabstract(qvtbase_Function)


def test_qvtbase_function_constructor_exists():
    assert callable(qvtbase_Function.__init__)


def test_qvtbase_function_constructor_args():
    sig = inspect.signature(qvtbase_Function.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_anonymoustupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_AnonymousTupleLiteralPart)


def test_imperativeocl_anonymoustupleliteralpart_constructor_exists():
    assert callable(imperativeocl_AnonymousTupleLiteralPart.__init__)


def test_imperativeocl_anonymoustupleliteralpart_constructor_args():
    sig = inspect.signature(imperativeocl_AnonymousTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_anonymoustupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(AnonymousTupleLiteralPart)


def test_anonymoustupleliteralpart_constructor_exists():
    assert callable(AnonymousTupleLiteralPart.__init__)


def test_anonymoustupleliteralpart_constructor_args():
    sig = inspect.signature(AnonymousTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_anonymoustupletype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_AnonymousTupleType)


def test_imperativeocl_anonymoustupletype_constructor_exists():
    assert callable(imperativeocl_AnonymousTupleType.__init__)


def test_imperativeocl_anonymoustupletype_constructor_args():
    sig = inspect.signature(imperativeocl_AnonymousTupleType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_unpackexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_UnpackExp)


def test_imperativeocl_unpackexp_constructor_exists():
    assert callable(imperativeocl_UnpackExp.__init__)


def test_imperativeocl_unpackexp_constructor_args():
    sig = inspect.signature(imperativeocl_UnpackExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_collectorexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_CollectorExp)


def test_imperativeocl_collectorexp_constructor_exists():
    assert callable(imperativeocl_CollectorExp.__init__)


def test_imperativeocl_collectorexp_constructor_args():
    sig = inspect.signature(imperativeocl_CollectorExp.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_IteratorExp)


def test_essentialocl_iteratorexp_constructor_exists():
    assert callable(essentialocl_IteratorExp.__init__)


def test_essentialocl_iteratorexp_constructor_args():
    sig = inspect.signature(essentialocl_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_iterateexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_IterateExp)


def test_essentialocl_iterateexp_constructor_exists():
    assert callable(essentialocl_IterateExp.__init__)


def test_essentialocl_iterateexp_constructor_args():
    sig = inspect.signature(essentialocl_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ImperativeLoopExp)


def test_imperativeocl_imperativeloopexp_constructor_exists():
    assert callable(imperativeocl_ImperativeLoopExp.__init__)


def test_imperativeocl_imperativeloopexp_constructor_args():
    sig = inspect.signature(imperativeocl_ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_logexp_is_not_abstract():
    assert not inspect.isabstract(LogExp)


def test_logexp_constructor_exists():
    assert callable(LogExp.__init__)


def test_logexp_constructor_args():
    sig = inspect.signature(LogExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_assertexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_AssertExp)


def test_imperativeocl_assertexp_constructor_exists():
    assert callable(imperativeocl_AssertExp.__init__)


def test_imperativeocl_assertexp_constructor_args():
    sig = inspect.signature(imperativeocl_AssertExp.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_imperativeocl_assertexp_has_severity():
    assert hasattr(imperativeocl_AssertExp, "severity")
    descriptor = None
    for klass in imperativeocl_AssertExp.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl_tupleexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_TupleExp)


def test_imperativeocl_tupleexp_constructor_exists():
    assert callable(imperativeocl_TupleExp.__init__)


def test_imperativeocl_tupleexp_constructor_args():
    sig = inspect.signature(imperativeocl_TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_forexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ForExp)


def test_imperativeocl_forexp_constructor_exists():
    assert callable(imperativeocl_ForExp.__init__)


def test_imperativeocl_forexp_constructor_args():
    sig = inspect.signature(imperativeocl_ForExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_continueexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ContinueExp)


def test_imperativeocl_continueexp_constructor_exists():
    assert callable(imperativeocl_ContinueExp.__init__)


def test_imperativeocl_continueexp_constructor_args():
    sig = inspect.signature(imperativeocl_ContinueExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_logexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_LogExp)


def test_imperativeocl_logexp_constructor_exists():
    assert callable(imperativeocl_LogExp.__init__)


def test_imperativeocl_logexp_constructor_args():
    sig = inspect.signature(imperativeocl_LogExp.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "text" in params, "Missing parameter 'text'"

def test_imperativeocl_logexp_has_level():
    assert hasattr(imperativeocl_LogExp, "level")
    descriptor = None
    for klass in imperativeocl_LogExp.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_imperativeocl_logexp_has_text():
    assert hasattr(imperativeocl_LogExp, "text")
    descriptor = None
    for klass in imperativeocl_LogExp.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_DictLiteralPart)


def test_imperativeocl_dictliteralpart_constructor_exists():
    assert callable(imperativeocl_DictLiteralPart.__init__)


def test_imperativeocl_dictliteralpart_constructor_args():
    sig = inspect.signature(imperativeocl_DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(DictLiteralPart)


def test_dictliteralpart_constructor_exists():
    assert callable(DictLiteralPart.__init__)


def test_dictliteralpart_constructor_args():
    sig = inspect.signature(DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_dictionarytype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_DictionaryType)


def test_imperativeocl_dictionarytype_constructor_exists():
    assert callable(imperativeocl_DictionaryType.__init__)


def test_imperativeocl_dictionarytype_constructor_args():
    sig = inspect.signature(imperativeocl_DictionaryType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_instantiationexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_InstantiationExp)


def test_imperativeocl_instantiationexp_constructor_exists():
    assert callable(imperativeocl_InstantiationExp.__init__)


def test_imperativeocl_instantiationexp_constructor_args():
    sig = inspect.signature(imperativeocl_InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_typedef_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_Typedef)


def test_imperativeocl_typedef_constructor_exists():
    assert callable(imperativeocl_Typedef.__init__)


def test_imperativeocl_typedef_constructor_args():
    sig = inspect.signature(imperativeocl_Typedef.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_whileexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_WhileExp)


def test_imperativeocl_whileexp_constructor_exists():
    assert callable(imperativeocl_WhileExp.__init__)


def test_imperativeocl_whileexp_constructor_args():
    sig = inspect.signature(imperativeocl_WhileExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_raiseexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_RaiseExp)


def test_imperativeocl_raiseexp_constructor_exists():
    assert callable(imperativeocl_RaiseExp.__init__)


def test_imperativeocl_raiseexp_constructor_args():
    sig = inspect.signature(imperativeocl_RaiseExp.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_emof_class_is_not_abstract():
    assert not inspect.isabstract(emof_Class)


def test_emof_class_constructor_exists():
    assert callable(emof_Class.__init__)


def test_emof_class_constructor_args():
    sig = inspect.signature(emof_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_emof_class_has_isAbstract():
    assert hasattr(emof_Class, "isAbstract")
    descriptor = None
    for klass in emof_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl_templateparametertype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_TemplateParameterType)


def test_imperativeocl_templateparametertype_constructor_exists():
    assert callable(imperativeocl_TemplateParameterType.__init__)


def test_imperativeocl_templateparametertype_constructor_args():
    sig = inspect.signature(imperativeocl_TemplateParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_imperativeocl_templateparametertype_has_specification():
    assert hasattr(imperativeocl_TemplateParameterType, "specification")
    descriptor = None
    for klass in imperativeocl_TemplateParameterType.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl_invalidtype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_InvalidType)


def test_essentialocl_invalidtype_constructor_exists():
    assert callable(essentialocl_InvalidType.__init__)


def test_essentialocl_invalidtype_constructor_args():
    sig = inspect.signature(essentialocl_InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_anytype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_AnyType)


def test_essentialocl_anytype_constructor_exists():
    assert callable(essentialocl_AnyType.__init__)


def test_essentialocl_anytype_constructor_args():
    sig = inspect.signature(essentialocl_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_voidtype_is_not_abstract():
    assert not inspect.isabstract(essentialocl_VoidType)


def test_essentialocl_voidtype_constructor_exists():
    assert callable(essentialocl_VoidType.__init__)


def test_essentialocl_voidtype_constructor_args():
    sig = inspect.signature(essentialocl_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_emof_datatype_is_not_abstract():
    assert not inspect.isabstract(emof_DataType)


def test_emof_datatype_constructor_exists():
    assert callable(emof_DataType.__init__)


def test_emof_datatype_constructor_args():
    sig = inspect.signature(emof_DataType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_tryexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_TryExp)


def test_imperativeocl_tryexp_constructor_exists():
    assert callable(imperativeocl_TryExp.__init__)


def test_imperativeocl_tryexp_constructor_args():
    sig = inspect.signature(imperativeocl_TryExp.__init__)
    params = list(sig.parameters.keys())



def test_propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(PropertyTemplateItem)


def test_propertytemplateitem_constructor_exists():
    assert callable(PropertyTemplateItem.__init__)


def test_propertytemplateitem_constructor_args():
    sig = inspect.signature(PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())



def test_templateexp_is_not_abstract():
    assert not inspect.isabstract(TemplateExp)


def test_templateexp_constructor_exists():
    assert callable(TemplateExp.__init__)


def test_templateexp_constructor_args():
    sig = inspect.signature(TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_qvttemplate_collectiontemplateexp_is_not_abstract():
    assert not inspect.isabstract(qvttemplate_CollectionTemplateExp)


def test_qvttemplate_collectiontemplateexp_constructor_exists():
    assert callable(qvttemplate_CollectionTemplateExp.__init__)


def test_qvttemplate_collectiontemplateexp_constructor_args():
    sig = inspect.signature(qvttemplate_CollectionTemplateExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_qvttemplate_collectiontemplateexp_has_kind():
    assert hasattr(qvttemplate_CollectionTemplateExp, "kind")
    descriptor = None
    for klass in qvttemplate_CollectionTemplateExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_qvttemplate_objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(qvttemplate_ObjectTemplateExp)


def test_qvttemplate_objecttemplateexp_constructor_exists():
    assert callable(qvttemplate_ObjectTemplateExp.__init__)


def test_qvttemplate_objecttemplateexp_constructor_args():
    sig = inspect.signature(qvttemplate_ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_callexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_CallExp)


def test_essentialocl_callexp_constructor_exists():
    assert callable(essentialocl_CallExp.__init__)


def test_essentialocl_callexp_constructor_args():
    sig = inspect.signature(essentialocl_CallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_typeexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_TypeExp)


def test_essentialocl_typeexp_constructor_exists():
    assert callable(essentialocl_TypeExp.__init__)


def test_essentialocl_typeexp_constructor_args():
    sig = inspect.signature(essentialocl_TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_loopexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_LoopExp)


def test_essentialocl_loopexp_constructor_exists():
    assert callable(essentialocl_LoopExp.__init__)


def test_essentialocl_loopexp_constructor_args():
    sig = inspect.signature(essentialocl_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_literalexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_LiteralExp)


def test_essentialocl_literalexp_constructor_exists():
    assert callable(essentialocl_LiteralExp.__init__)


def test_essentialocl_literalexp_constructor_args():
    sig = inspect.signature(essentialocl_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_variableexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_VariableExp)


def test_essentialocl_variableexp_constructor_exists():
    assert callable(essentialocl_VariableExp.__init__)


def test_essentialocl_variableexp_constructor_args():
    sig = inspect.signature(essentialocl_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ImperativeExpression)


def test_imperativeocl_imperativeexpression_constructor_exists():
    assert callable(imperativeocl_ImperativeExpression.__init__)


def test_imperativeocl_imperativeexpression_constructor_args():
    sig = inspect.signature(imperativeocl_ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_ifexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_IfExp)


def test_essentialocl_ifexp_constructor_exists():
    assert callable(essentialocl_IfExp.__init__)


def test_essentialocl_ifexp_constructor_args():
    sig = inspect.signature(essentialocl_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_letexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_LetExp)


def test_essentialocl_letexp_constructor_exists():
    assert callable(essentialocl_LetExp.__init__)


def test_essentialocl_letexp_constructor_args():
    sig = inspect.signature(essentialocl_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_varparameter_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_VarParameter)


def test_qvtoperational_varparameter_constructor_exists():
    assert callable(qvtoperational_VarParameter.__init__)


def test_qvtoperational_varparameter_constructor_args():
    sig = inspect.signature(qvtoperational_VarParameter.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_qvtoperational_varparameter_has_kind():
    assert hasattr(qvtoperational_VarParameter, "kind")
    descriptor = None
    for klass in qvtoperational_VarParameter.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_qvtbase_functionparameter_is_not_abstract():
    assert not inspect.isabstract(qvtbase_FunctionParameter)


def test_qvtbase_functionparameter_constructor_exists():
    assert callable(qvtbase_FunctionParameter.__init__)


def test_qvtbase_functionparameter_constructor_args():
    sig = inspect.signature(qvtbase_FunctionParameter.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_realizedvariable_is_not_abstract():
    assert not inspect.isabstract(qvtcore_RealizedVariable)


def test_qvtcore_realizedvariable_constructor_exists():
    assert callable(qvtcore_RealizedVariable.__init__)


def test_qvtcore_realizedvariable_constructor_args():
    sig = inspect.signature(qvtcore_RealizedVariable.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_InvalidLiteralExp)


def test_essentialocl_invalidliteralexp_constructor_exists():
    assert callable(essentialocl_InvalidLiteralExp.__init__)


def test_essentialocl_invalidliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_DictLiteralExp)


def test_imperativeocl_dictliteralexp_constructor_exists():
    assert callable(imperativeocl_DictLiteralExp.__init__)


def test_imperativeocl_dictliteralexp_constructor_args():
    sig = inspect.signature(imperativeocl_DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_NullLiteralExp)


def test_essentialocl_nullliteralexp_constructor_exists():
    assert callable(essentialocl_NullLiteralExp.__init__)


def test_essentialocl_nullliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_TupleLiteralExp)


def test_essentialocl_tupleliteralexp_constructor_exists():
    assert callable(essentialocl_TupleLiteralExp.__init__)


def test_essentialocl_tupleliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_EnumLiteralExp)


def test_essentialocl_enumliteralexp_constructor_exists():
    assert callable(essentialocl_EnumLiteralExp.__init__)


def test_essentialocl_enumliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_PrimitiveLiteralExp)


def test_essentialocl_primitiveliteralexp_constructor_exists():
    assert callable(essentialocl_PrimitiveLiteralExp.__init__)


def test_essentialocl_primitiveliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_CollectionLiteralExp)


def test_essentialocl_collectionliteralexp_constructor_exists():
    assert callable(essentialocl_CollectionLiteralExp.__init__)


def test_essentialocl_collectionliteralexp_constructor_args():
    sig = inspect.signature(essentialocl_CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_essentialocl_collectionliteralexp_has_kind():
    assert hasattr(essentialocl_CollectionLiteralExp, "kind")
    descriptor = None
    for klass in essentialocl_CollectionLiteralExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl_anonymoustupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_AnonymousTupleLiteralExp)


def test_imperativeocl_anonymoustupleliteralexp_constructor_exists():
    assert callable(imperativeocl_AnonymousTupleLiteralExp.__init__)


def test_imperativeocl_anonymoustupleliteralexp_constructor_args():
    sig = inspect.signature(imperativeocl_AnonymousTupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_qvttemplate_templateexp_is_not_abstract():
    assert not inspect.isabstract(qvttemplate_TemplateExp)


def test_qvttemplate_templateexp_constructor_exists():
    assert callable(qvttemplate_TemplateExp.__init__)


def test_qvttemplate_templateexp_constructor_args():
    sig = inspect.signature(qvttemplate_TemplateExp.__init__)
    params = list(sig.parameters.keys())

def test_severitykind_exists():
    # Check that the Enumeration exists
    assert SeverityKind is not None

def test_severitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SeverityKind]
    expected_literals = [
        "fatal",
        "error",
        "warning",
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
        "Creation",
        "Deletion",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnforcementMode"

def test_importkind_exists():
    # Check that the Enumeration exists
    assert ImportKind is not None

def test_importkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImportKind]
    expected_literals = [
        "extension",
        "access",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImportKind"

def test_directionkind_exists():
    # Check that the Enumeration exists
    assert DirectionKind is not None

def test_directionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionKind]
    expected_literals = [
        "in_",
        "out",
        "inout",
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
        "OrderedSet",
        "Sequence",
        "Set",
        "Bag",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"


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
TupleLiteralExp_strategy = st.builds(
    TupleLiteralExp,
)
essentialocl_OpaqueExpression_strategy = st.builds(
    essentialocl_OpaqueExpression,
)
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
essentialocl_ExpressionInOcl_strategy = st.builds(
    essentialocl_ExpressionInOcl,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
essentialocl_CollectionItem_strategy = st.builds(
    essentialocl_CollectionItem,
)
essentialocl_CollectionRange_strategy = st.builds(
    essentialocl_CollectionRange,
)
FeaturePropertyCall_strategy = st.builds(
    FeaturePropertyCall,
)
essentialocl_OperationCallExp_strategy = st.builds(
    essentialocl_OperationCallExp,
)
essentialocl_PropertyCallExp_strategy = st.builds(
    essentialocl_PropertyCallExp,
)
ComputeExp_strategy = st.builds(
    ComputeExp,
)
LetExp_strategy = st.builds(
    LetExp,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
essentialocl_StringLiteralExp_strategy = st.builds(
    essentialocl_StringLiteralExp,
    stringSymbol=
        safe_text
)
essentialocl_NumericLiteralExp_strategy = st.builds(
    essentialocl_NumericLiteralExp,
)
essentialocl_BooleanLiteralExp_strategy = st.builds(
    essentialocl_BooleanLiteralExp,
    booleanSymbol=
        safe_text
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
essentialocl_RealLiteralExp_strategy = st.builds(
    essentialocl_RealLiteralExp,
    realSymbol=
        safe_text
)
essentialocl_IntegerLiteralExp_strategy = st.builds(
    essentialocl_IntegerLiteralExp,
    integerSymbol=
        safe_text
)
essentialocl_UnlimitedNaturalExp_strategy = st.builds(
    essentialocl_UnlimitedNaturalExp,
    symbol=
        safe_text
)
TryExp_strategy = st.builds(
    TryExp,
)
RelationalTransformation_strategy = st.builds(
    RelationalTransformation,
)
DomainPattern_strategy = st.builds(
    DomainPattern,
)
RelationImplementation_strategy = st.builds(
    RelationImplementation,
)
Key_strategy = st.builds(
    Key,
)
Predicate_strategy = st.builds(
    Predicate,
)
qvtcore_EnforcementOperation_strategy = st.builds(
    qvtcore_EnforcementOperation,
    enforcementMode=
        safe_text
)
TypedModel_strategy = st.builds(
    TypedModel,
)
qvtcore_Assignment_strategy = st.builds(
    qvtcore_Assignment,
    isDefault=
        safe_text
)
BottomPattern_strategy = st.builds(
    BottomPattern,
)
Pattern_strategy = st.builds(
    Pattern,
)
qvtrelation_DomainPattern_strategy = st.builds(
    qvtrelation_DomainPattern,
)
qvtcore_CorePattern_strategy = st.builds(
    qvtcore_CorePattern,
)
Domain_strategy = st.builds(
    Domain,
)
qvtrelation_RelationDomain_strategy = st.builds(
    qvtrelation_RelationDomain,
)
Mapping_strategy = st.builds(
    Mapping,
)
Rule_strategy = st.builds(
    Rule,
)
qvtrelation_Relation_strategy = st.builds(
    qvtrelation_Relation,
    isTopLevel=
        safe_text
)
EnforcementOperation_strategy = st.builds(
    EnforcementOperation,
)
RealizedVariable_strategy = st.builds(
    RealizedVariable,
)
Assignment_strategy = st.builds(
    Assignment,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
essentialocl_BagType_strategy = st.builds(
    essentialocl_BagType,
)
essentialocl_SetType_strategy = st.builds(
    essentialocl_SetType,
)
essentialocl_SequenceType_strategy = st.builds(
    essentialocl_SequenceType,
)
essentialocl_OrderedSetType_strategy = st.builds(
    essentialocl_OrderedSetType,
)
AltExp_strategy = st.builds(
    AltExp,
)
CallExp_strategy = st.builds(
    CallExp,
)
essentialocl_FeaturePropertyCall_strategy = st.builds(
    essentialocl_FeaturePropertyCall,
)
ImperativeExpression_strategy = st.builds(
    ImperativeExpression,
)
imperativeocl_AltExp_strategy = st.builds(
    imperativeocl_AltExp,
)
imperativeocl_UnlinkExp_strategy = st.builds(
    imperativeocl_UnlinkExp,
)
imperativeocl_ComputeExp_strategy = st.builds(
    imperativeocl_ComputeExp,
)
imperativeocl_BreakExp_strategy = st.builds(
    imperativeocl_BreakExp,
)
imperativeocl_SwitchExp_strategy = st.builds(
    imperativeocl_SwitchExp,
)
imperativeocl_VariableInitExp_strategy = st.builds(
    imperativeocl_VariableInitExp,
    withResult=
        safe_text
)
imperativeocl_ReturnExp_strategy = st.builds(
    imperativeocl_ReturnExp,
)
imperativeocl_BlockExp_strategy = st.builds(
    imperativeocl_BlockExp,
)
imperativeocl_AssignExp_strategy = st.builds(
    imperativeocl_AssignExp,
    isReset=
        safe_text
)
ImperativeLoopExp_strategy = st.builds(
    ImperativeLoopExp,
)
imperativeocl_ImperativeIterateExp_strategy = st.builds(
    imperativeocl_ImperativeIterateExp,
)
Property_strategy = st.builds(
    Property,
)
ObjectTemplateExp_strategy = st.builds(
    ObjectTemplateExp,
)
Element_strategy = st.builds(
    Element,
)
qvtrelation_Key_strategy = st.builds(
    qvtrelation_Key,
)
qvtbase_Pattern_strategy = st.builds(
    qvtbase_Pattern,
)
qvtbase_Predicate_strategy = st.builds(
    qvtbase_Predicate,
)
qvtrelation_RelationImplementation_strategy = st.builds(
    qvtrelation_RelationImplementation,
)
qvttemplate_PropertyTemplateItem_strategy = st.builds(
    qvttemplate_PropertyTemplateItem,
)
Class_strategy = st.builds(
    Class,
)
Area_strategy = st.builds(
    Area,
)
qvtcore_Mapping_strategy = st.builds(
    qvtcore_Mapping,
)
qvtcore_CoreDomain_strategy = st.builds(
    qvtcore_CoreDomain,
)
CorePattern_strategy = st.builds(
    CorePattern,
)
qvtcore_GuardPattern_strategy = st.builds(
    qvtcore_GuardPattern,
)
qvtcore_BottomPattern_strategy = st.builds(
    qvtcore_BottomPattern,
)
qvtoperational_ModuleImport_strategy = st.builds(
    qvtoperational_ModuleImport,
    kind=
        safe_text
)
GuardPattern_strategy = st.builds(
    GuardPattern,
)
qvtcore_Area_strategy = st.builds(
    qvtcore_Area,
)
ConstructorBody_strategy = st.builds(
    ConstructorBody,
)
InstantiationExp_strategy = st.builds(
    InstantiationExp,
)
qvtoperational_ObjectExp_strategy = st.builds(
    qvtoperational_ObjectExp,
)
qvtoperational_OperationBody_strategy = st.builds(
    qvtoperational_OperationBody,
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
qvtoperational_ImperativeCallExp_strategy = st.builds(
    qvtoperational_ImperativeCallExp,
    isVirtual=
        safe_text
)
ModelType_strategy = st.builds(
    ModelType,
)
ModuleImport_strategy = st.builds(
    ModuleImport,
)
URIExtent_strategy = st.builds(
    URIExtent,
)
qvtoperational_ModelType_strategy = st.builds(
    qvtoperational_ModelType,
    conformanceKind=
        safe_text
)
EntryOperation_strategy = st.builds(
    EntryOperation,
)
ModelParameter_strategy = st.builds(
    ModelParameter,
)
qvtoperational_ContextualProperty_strategy = st.builds(
    qvtoperational_ContextualProperty,
)
ImperativeCallExp_strategy = st.builds(
    ImperativeCallExp,
)
qvtoperational_MappingCallExp_strategy = st.builds(
    qvtoperational_MappingCallExp,
    isStrict=
        safe_text
)
RelationDomain_strategy = st.builds(
    RelationDomain,
)
VarParameter_strategy = st.builds(
    VarParameter,
)
qvtoperational_ModelParameter_strategy = st.builds(
    qvtoperational_ModelParameter,
)
qvtoperational_MappingParameter_strategy = st.builds(
    qvtoperational_MappingParameter,
)
Relation_strategy = st.builds(
    Relation,
)
MappingOperation_strategy = st.builds(
    MappingOperation,
)
ResolveExp_strategy = st.builds(
    ResolveExp,
)
qvtoperational_ResolveInExp_strategy = st.builds(
    qvtoperational_ResolveInExp,
)
qvtoperational_ResolveExp_strategy = st.builds(
    qvtoperational_ResolveExp,
    isDeferred=
        safe_text,
    one=
        safe_text,
    isInverse=
        safe_text
)
ImperativeOperation_strategy = st.builds(
    ImperativeOperation,
)
qvtoperational_EntryOperation_strategy = st.builds(
    qvtoperational_EntryOperation,
)
qvtoperational_Constructor_strategy = st.builds(
    qvtoperational_Constructor,
)
qvtoperational_Helper_strategy = st.builds(
    qvtoperational_Helper,
    isQuery=
        safe_text
)
OperationBody_strategy = st.builds(
    OperationBody,
)
qvtoperational_ConstructorBody_strategy = st.builds(
    qvtoperational_ConstructorBody,
)
qvtoperational_MappingBody_strategy = st.builds(
    qvtoperational_MappingBody,
)
emof_Comment_strategy = st.builds(
    emof_Comment,
)
Extent_strategy = st.builds(
    Extent,
)
emof_URIExtent_strategy = st.builds(
    emof_URIExtent,
)
Parameter_strategy = st.builds(
    Parameter,
)
Enumeration_strategy = st.builds(
    Enumeration,
)
Package_strategy = st.builds(
    Package,
)
qvtoperational_Module_strategy = st.builds(
    qvtoperational_Module,
    isBlackbox=
        safe_text
)
qvtbase_Transformation_strategy = st.builds(
    qvtbase_Transformation,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
emof_TypedElement_strategy = st.builds(
    emof_TypedElement,
)
qvtbase_Domain_strategy = st.builds(
    qvtbase_Domain,
    isCheckable=
        safe_text,
    isEnforceable=
        safe_text
)
qvtbase_Rule_strategy = st.builds(
    qvtbase_Rule,
)
emof_EnumerationLiteral_strategy = st.builds(
    emof_EnumerationLiteral,
)
emof_Type_strategy = st.builds(
    emof_Type,
)
qvtbase_TypedModel_strategy = st.builds(
    qvtbase_TypedModel,
)
emof_Package_strategy = st.builds(
    emof_Package,
    uri=
        safe_text
)
emof_MultiplicityElement_strategy = st.builds(
    emof_MultiplicityElement,
    isOrdered=
        safe_text,
    isUnique=
        safe_text,
    upper=
        safe_text,
    lower=
        safe_text
)
imperativeocl_ListType_strategy = st.builds(
    imperativeocl_ListType,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
essentialocl_CollectionLiteralPart_strategy = st.builds(
    essentialocl_CollectionLiteralPart,
)
essentialocl_TupleLiteralPart_strategy = st.builds(
    essentialocl_TupleLiteralPart,
)
essentialocl_OclExpression_strategy = st.builds(
    essentialocl_OclExpression,
)
essentialocl_Variable_strategy = st.builds(
    essentialocl_Variable,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
emof_Property_strategy = st.builds(
    emof_Property,
    default=
        safe_text,
    isDerived=
        safe_text,
    isReadOnly=
        safe_text,
    isComposite=
        safe_text,
    isId=
        safe_text
)
emof_Parameter_strategy = st.builds(
    emof_Parameter,
)
emof_Operation_strategy = st.builds(
    emof_Operation,
)
emof_Object_strategy = st.builds(
    emof_Object,
)
emof_NamedElement_strategy = st.builds(
    emof_NamedElement,
    name=
        safe_text
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
essentialocl_TupleType_strategy = st.builds(
    essentialocl_TupleType,
)
emof_PrimitiveType_strategy = st.builds(
    emof_PrimitiveType,
)
essentialocl_CollectionType_strategy = st.builds(
    essentialocl_CollectionType,
)
emof_Enumeration_strategy = st.builds(
    emof_Enumeration,
)
Module_strategy = st.builds(
    Module,
)
qvtoperational_Library_strategy = st.builds(
    qvtoperational_Library,
)
qvtoperational_OperationalTransformation_strategy = st.builds(
    qvtoperational_OperationalTransformation,
)
Transformation_strategy = st.builds(
    Transformation,
)
qvtrelation_RelationalTransformation_strategy = st.builds(
    qvtrelation_RelationalTransformation,
)
emof_Tag_strategy = st.builds(
    emof_Tag,
    name=
        safe_text,
    value=
        safe_text
)
Comment_strategy = st.builds(
    Comment,
)
Tag_strategy = st.builds(
    Tag,
)
Object_strategy = st.builds(
    Object,
)
emof_Extent_strategy = st.builds(
    emof_Extent,
)
emof_Element_strategy = st.builds(
    emof_Element,
)
Operation_strategy = st.builds(
    Operation,
)
qvtoperational_ImperativeOperation_strategy = st.builds(
    qvtoperational_ImperativeOperation,
    isBlackbox=
        safe_text
)
qvtoperational_MappingOperation_strategy = st.builds(
    qvtoperational_MappingOperation,
)
qvtbase_Function_strategy = st.builds(
    qvtbase_Function,
)
imperativeocl_AnonymousTupleLiteralPart_strategy = st.builds(
    imperativeocl_AnonymousTupleLiteralPart,
)
AnonymousTupleLiteralPart_strategy = st.builds(
    AnonymousTupleLiteralPart,
)
imperativeocl_AnonymousTupleType_strategy = st.builds(
    imperativeocl_AnonymousTupleType,
)
imperativeocl_UnpackExp_strategy = st.builds(
    imperativeocl_UnpackExp,
)
imperativeocl_CollectorExp_strategy = st.builds(
    imperativeocl_CollectorExp,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
essentialocl_IteratorExp_strategy = st.builds(
    essentialocl_IteratorExp,
)
essentialocl_IterateExp_strategy = st.builds(
    essentialocl_IterateExp,
)
imperativeocl_ImperativeLoopExp_strategy = st.builds(
    imperativeocl_ImperativeLoopExp,
)
LogExp_strategy = st.builds(
    LogExp,
)
imperativeocl_AssertExp_strategy = st.builds(
    imperativeocl_AssertExp,
    severity=
        safe_text
)
imperativeocl_TupleExp_strategy = st.builds(
    imperativeocl_TupleExp,
)
imperativeocl_ForExp_strategy = st.builds(
    imperativeocl_ForExp,
)
imperativeocl_ContinueExp_strategy = st.builds(
    imperativeocl_ContinueExp,
)
imperativeocl_LogExp_strategy = st.builds(
    imperativeocl_LogExp,
    level=
        safe_text,
    text=
        safe_text
)
imperativeocl_DictLiteralPart_strategy = st.builds(
    imperativeocl_DictLiteralPart,
)
DictLiteralPart_strategy = st.builds(
    DictLiteralPart,
)
imperativeocl_DictionaryType_strategy = st.builds(
    imperativeocl_DictionaryType,
)
imperativeocl_InstantiationExp_strategy = st.builds(
    imperativeocl_InstantiationExp,
)
imperativeocl_Typedef_strategy = st.builds(
    imperativeocl_Typedef,
)
imperativeocl_WhileExp_strategy = st.builds(
    imperativeocl_WhileExp,
)
imperativeocl_RaiseExp_strategy = st.builds(
    imperativeocl_RaiseExp,
)
Type_strategy = st.builds(
    Type,
)
emof_Class_strategy = st.builds(
    emof_Class,
    isAbstract=
        safe_text
)
imperativeocl_TemplateParameterType_strategy = st.builds(
    imperativeocl_TemplateParameterType,
    specification=
        safe_text
)
essentialocl_InvalidType_strategy = st.builds(
    essentialocl_InvalidType,
)
essentialocl_AnyType_strategy = st.builds(
    essentialocl_AnyType,
)
essentialocl_VoidType_strategy = st.builds(
    essentialocl_VoidType,
)
emof_DataType_strategy = st.builds(
    emof_DataType,
)
imperativeocl_TryExp_strategy = st.builds(
    imperativeocl_TryExp,
)
PropertyTemplateItem_strategy = st.builds(
    PropertyTemplateItem,
)
TemplateExp_strategy = st.builds(
    TemplateExp,
)
qvttemplate_CollectionTemplateExp_strategy = st.builds(
    qvttemplate_CollectionTemplateExp,
    kind=
        safe_text
)
qvttemplate_ObjectTemplateExp_strategy = st.builds(
    qvttemplate_ObjectTemplateExp,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
essentialocl_CallExp_strategy = st.builds(
    essentialocl_CallExp,
)
essentialocl_TypeExp_strategy = st.builds(
    essentialocl_TypeExp,
)
essentialocl_LoopExp_strategy = st.builds(
    essentialocl_LoopExp,
)
essentialocl_LiteralExp_strategy = st.builds(
    essentialocl_LiteralExp,
)
essentialocl_VariableExp_strategy = st.builds(
    essentialocl_VariableExp,
)
imperativeocl_ImperativeExpression_strategy = st.builds(
    imperativeocl_ImperativeExpression,
)
essentialocl_IfExp_strategy = st.builds(
    essentialocl_IfExp,
)
essentialocl_LetExp_strategy = st.builds(
    essentialocl_LetExp,
)
Variable_strategy = st.builds(
    Variable,
)
qvtoperational_VarParameter_strategy = st.builds(
    qvtoperational_VarParameter,
    kind=
        safe_text
)
qvtbase_FunctionParameter_strategy = st.builds(
    qvtbase_FunctionParameter,
)
qvtcore_RealizedVariable_strategy = st.builds(
    qvtcore_RealizedVariable,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
essentialocl_InvalidLiteralExp_strategy = st.builds(
    essentialocl_InvalidLiteralExp,
)
imperativeocl_DictLiteralExp_strategy = st.builds(
    imperativeocl_DictLiteralExp,
)
essentialocl_NullLiteralExp_strategy = st.builds(
    essentialocl_NullLiteralExp,
)
essentialocl_TupleLiteralExp_strategy = st.builds(
    essentialocl_TupleLiteralExp,
)
essentialocl_EnumLiteralExp_strategy = st.builds(
    essentialocl_EnumLiteralExp,
)
essentialocl_PrimitiveLiteralExp_strategy = st.builds(
    essentialocl_PrimitiveLiteralExp,
)
essentialocl_CollectionLiteralExp_strategy = st.builds(
    essentialocl_CollectionLiteralExp,
    kind=
        safe_text
)
imperativeocl_AnonymousTupleLiteralExp_strategy = st.builds(
    imperativeocl_AnonymousTupleLiteralExp,
)
qvttemplate_TemplateExp_strategy = st.builds(
    qvttemplate_TemplateExp,
)

@given(instance=TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, TupleLiteralExp)

@given(instance=essentialocl_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_essentialocl_opaqueexpression_instantiation(instance):
    assert isinstance(instance, essentialocl_OpaqueExpression)

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=essentialocl_ExpressionInOcl_strategy)
@settings(max_examples=50)
def test_essentialocl_expressioninocl_instantiation(instance):
    assert isinstance(instance, essentialocl_ExpressionInOcl)

@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)

@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=essentialocl_CollectionItem_strategy)
@settings(max_examples=50)
def test_essentialocl_collectionitem_instantiation(instance):
    assert isinstance(instance, essentialocl_CollectionItem)

@given(instance=essentialocl_CollectionRange_strategy)
@settings(max_examples=50)
def test_essentialocl_collectionrange_instantiation(instance):
    assert isinstance(instance, essentialocl_CollectionRange)

@given(instance=FeaturePropertyCall_strategy)
@settings(max_examples=50)
def test_featurepropertycall_instantiation(instance):
    assert isinstance(instance, FeaturePropertyCall)

@given(instance=essentialocl_OperationCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl_operationcallexp_instantiation(instance):
    assert isinstance(instance, essentialocl_OperationCallExp)

@given(instance=essentialocl_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl_propertycallexp_instantiation(instance):
    assert isinstance(instance, essentialocl_PropertyCallExp)

@given(instance=ComputeExp_strategy)
@settings(max_examples=50)
def test_computeexp_instantiation(instance):
    assert isinstance(instance, ComputeExp)

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=essentialocl_StringLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_stringliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl_StringLiteralExp)



@given(instance=essentialocl_StringLiteralExp_strategy)
def test_essentialocl_stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=essentialocl_NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_numericliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl_NumericLiteralExp)

@given(instance=essentialocl_BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_booleanliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl_BooleanLiteralExp)



@given(instance=essentialocl_BooleanLiteralExp_strategy)
def test_essentialocl_booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=essentialocl_RealLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_realliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl_RealLiteralExp)



@given(instance=essentialocl_RealLiteralExp_strategy)
def test_essentialocl_realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=essentialocl_IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_integerliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl_IntegerLiteralExp)



@given(instance=essentialocl_IntegerLiteralExp_strategy)
def test_essentialocl_integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=essentialocl_UnlimitedNaturalExp_strategy)
@settings(max_examples=50)
def test_essentialocl_unlimitednaturalexp_instantiation(instance):
    assert isinstance(instance, essentialocl_UnlimitedNaturalExp)



@given(instance=essentialocl_UnlimitedNaturalExp_strategy)
def test_essentialocl_unlimitednaturalexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=TryExp_strategy)
@settings(max_examples=50)
def test_tryexp_instantiation(instance):
    assert isinstance(instance, TryExp)

@given(instance=RelationalTransformation_strategy)
@settings(max_examples=50)
def test_relationaltransformation_instantiation(instance):
    assert isinstance(instance, RelationalTransformation)

@given(instance=DomainPattern_strategy)
@settings(max_examples=50)
def test_domainpattern_instantiation(instance):
    assert isinstance(instance, DomainPattern)

@given(instance=RelationImplementation_strategy)
@settings(max_examples=50)
def test_relationimplementation_instantiation(instance):
    assert isinstance(instance, RelationImplementation)

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=qvtcore_EnforcementOperation_strategy)
@settings(max_examples=50)
def test_qvtcore_enforcementoperation_instantiation(instance):
    assert isinstance(instance, qvtcore_EnforcementOperation)



@given(instance=qvtcore_EnforcementOperation_strategy)
def test_qvtcore_enforcementoperation_enforcementMode_setter(instance):
    original = instance.enforcementMode
    instance.enforcementMode = original
    assert instance.enforcementMode == original

@given(instance=TypedModel_strategy)
@settings(max_examples=50)
def test_typedmodel_instantiation(instance):
    assert isinstance(instance, TypedModel)

@given(instance=qvtcore_Assignment_strategy)
@settings(max_examples=50)
def test_qvtcore_assignment_instantiation(instance):
    assert isinstance(instance, qvtcore_Assignment)



@given(instance=qvtcore_Assignment_strategy)
def test_qvtcore_assignment_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original

@given(instance=BottomPattern_strategy)
@settings(max_examples=50)
def test_bottompattern_instantiation(instance):
    assert isinstance(instance, BottomPattern)

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=qvtrelation_DomainPattern_strategy)
@settings(max_examples=50)
def test_qvtrelation_domainpattern_instantiation(instance):
    assert isinstance(instance, qvtrelation_DomainPattern)

@given(instance=qvtcore_CorePattern_strategy)
@settings(max_examples=50)
def test_qvtcore_corepattern_instantiation(instance):
    assert isinstance(instance, qvtcore_CorePattern)

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=qvtrelation_RelationDomain_strategy)
@settings(max_examples=50)
def test_qvtrelation_relationdomain_instantiation(instance):
    assert isinstance(instance, qvtrelation_RelationDomain)

@given(instance=Mapping_strategy)
@settings(max_examples=50)
def test_mapping_instantiation(instance):
    assert isinstance(instance, Mapping)

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=qvtrelation_Relation_strategy)
@settings(max_examples=50)
def test_qvtrelation_relation_instantiation(instance):
    assert isinstance(instance, qvtrelation_Relation)



@given(instance=qvtrelation_Relation_strategy)
def test_qvtrelation_relation_isTopLevel_setter(instance):
    original = instance.isTopLevel
    instance.isTopLevel = original
    assert instance.isTopLevel == original

@given(instance=EnforcementOperation_strategy)
@settings(max_examples=50)
def test_enforcementoperation_instantiation(instance):
    assert isinstance(instance, EnforcementOperation)

@given(instance=RealizedVariable_strategy)
@settings(max_examples=50)
def test_realizedvariable_instantiation(instance):
    assert isinstance(instance, RealizedVariable)

@given(instance=Assignment_strategy)
@settings(max_examples=50)
def test_assignment_instantiation(instance):
    assert isinstance(instance, Assignment)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=essentialocl_BagType_strategy)
@settings(max_examples=50)
def test_essentialocl_bagtype_instantiation(instance):
    assert isinstance(instance, essentialocl_BagType)

@given(instance=essentialocl_SetType_strategy)
@settings(max_examples=50)
def test_essentialocl_settype_instantiation(instance):
    assert isinstance(instance, essentialocl_SetType)

@given(instance=essentialocl_SequenceType_strategy)
@settings(max_examples=50)
def test_essentialocl_sequencetype_instantiation(instance):
    assert isinstance(instance, essentialocl_SequenceType)

@given(instance=essentialocl_OrderedSetType_strategy)
@settings(max_examples=50)
def test_essentialocl_orderedsettype_instantiation(instance):
    assert isinstance(instance, essentialocl_OrderedSetType)

@given(instance=AltExp_strategy)
@settings(max_examples=50)
def test_altexp_instantiation(instance):
    assert isinstance(instance, AltExp)

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=essentialocl_FeaturePropertyCall_strategy)
@settings(max_examples=50)
def test_essentialocl_featurepropertycall_instantiation(instance):
    assert isinstance(instance, essentialocl_FeaturePropertyCall)

@given(instance=ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeExpression)

@given(instance=imperativeocl_AltExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_altexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_AltExp)

@given(instance=imperativeocl_UnlinkExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_unlinkexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_UnlinkExp)

@given(instance=imperativeocl_ComputeExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_computeexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_ComputeExp)

@given(instance=imperativeocl_BreakExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_breakexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_BreakExp)

@given(instance=imperativeocl_SwitchExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_switchexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_SwitchExp)

@given(instance=imperativeocl_VariableInitExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_variableinitexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_VariableInitExp)



@given(instance=imperativeocl_VariableInitExp_strategy)
def test_imperativeocl_variableinitexp_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=imperativeocl_ReturnExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_returnexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_ReturnExp)

@given(instance=imperativeocl_BlockExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_blockexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_BlockExp)

@given(instance=imperativeocl_AssignExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_assignexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_AssignExp)



@given(instance=imperativeocl_AssignExp_strategy)
def test_imperativeocl_assignexp_isReset_setter(instance):
    original = instance.isReset
    instance.isReset = original
    assert instance.isReset == original

@given(instance=ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExp)

@given(instance=imperativeocl_ImperativeIterateExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_imperativeiterateexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_ImperativeIterateExp)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_objecttemplateexp_instantiation(instance):
    assert isinstance(instance, ObjectTemplateExp)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=qvtrelation_Key_strategy)
@settings(max_examples=50)
def test_qvtrelation_key_instantiation(instance):
    assert isinstance(instance, qvtrelation_Key)

@given(instance=qvtbase_Pattern_strategy)
@settings(max_examples=50)
def test_qvtbase_pattern_instantiation(instance):
    assert isinstance(instance, qvtbase_Pattern)

@given(instance=qvtbase_Predicate_strategy)
@settings(max_examples=50)
def test_qvtbase_predicate_instantiation(instance):
    assert isinstance(instance, qvtbase_Predicate)

@given(instance=qvtrelation_RelationImplementation_strategy)
@settings(max_examples=50)
def test_qvtrelation_relationimplementation_instantiation(instance):
    assert isinstance(instance, qvtrelation_RelationImplementation)

@given(instance=qvttemplate_PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_qvttemplate_propertytemplateitem_instantiation(instance):
    assert isinstance(instance, qvttemplate_PropertyTemplateItem)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Area_strategy)
@settings(max_examples=50)
def test_area_instantiation(instance):
    assert isinstance(instance, Area)

@given(instance=qvtcore_Mapping_strategy)
@settings(max_examples=50)
def test_qvtcore_mapping_instantiation(instance):
    assert isinstance(instance, qvtcore_Mapping)

@given(instance=qvtcore_CoreDomain_strategy)
@settings(max_examples=50)
def test_qvtcore_coredomain_instantiation(instance):
    assert isinstance(instance, qvtcore_CoreDomain)

@given(instance=CorePattern_strategy)
@settings(max_examples=50)
def test_corepattern_instantiation(instance):
    assert isinstance(instance, CorePattern)

@given(instance=qvtcore_GuardPattern_strategy)
@settings(max_examples=50)
def test_qvtcore_guardpattern_instantiation(instance):
    assert isinstance(instance, qvtcore_GuardPattern)

@given(instance=qvtcore_BottomPattern_strategy)
@settings(max_examples=50)
def test_qvtcore_bottompattern_instantiation(instance):
    assert isinstance(instance, qvtcore_BottomPattern)

@given(instance=qvtoperational_ModuleImport_strategy)
@settings(max_examples=50)
def test_qvtoperational_moduleimport_instantiation(instance):
    assert isinstance(instance, qvtoperational_ModuleImport)



@given(instance=qvtoperational_ModuleImport_strategy)
def test_qvtoperational_moduleimport_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=GuardPattern_strategy)
@settings(max_examples=50)
def test_guardpattern_instantiation(instance):
    assert isinstance(instance, GuardPattern)

@given(instance=qvtcore_Area_strategy)
@settings(max_examples=50)
def test_qvtcore_area_instantiation(instance):
    assert isinstance(instance, qvtcore_Area)

@given(instance=ConstructorBody_strategy)
@settings(max_examples=50)
def test_constructorbody_instantiation(instance):
    assert isinstance(instance, ConstructorBody)

@given(instance=InstantiationExp_strategy)
@settings(max_examples=50)
def test_instantiationexp_instantiation(instance):
    assert isinstance(instance, InstantiationExp)

@given(instance=qvtoperational_ObjectExp_strategy)
@settings(max_examples=50)
def test_qvtoperational_objectexp_instantiation(instance):
    assert isinstance(instance, qvtoperational_ObjectExp)

@given(instance=qvtoperational_OperationBody_strategy)
@settings(max_examples=50)
def test_qvtoperational_operationbody_instantiation(instance):
    assert isinstance(instance, qvtoperational_OperationBody)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=qvtoperational_ImperativeCallExp_strategy)
@settings(max_examples=50)
def test_qvtoperational_imperativecallexp_instantiation(instance):
    assert isinstance(instance, qvtoperational_ImperativeCallExp)



@given(instance=qvtoperational_ImperativeCallExp_strategy)
def test_qvtoperational_imperativecallexp_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original

@given(instance=ModelType_strategy)
@settings(max_examples=50)
def test_modeltype_instantiation(instance):
    assert isinstance(instance, ModelType)

@given(instance=ModuleImport_strategy)
@settings(max_examples=50)
def test_moduleimport_instantiation(instance):
    assert isinstance(instance, ModuleImport)

@given(instance=URIExtent_strategy)
@settings(max_examples=50)
def test_uriextent_instantiation(instance):
    assert isinstance(instance, URIExtent)

@given(instance=qvtoperational_ModelType_strategy)
@settings(max_examples=50)
def test_qvtoperational_modeltype_instantiation(instance):
    assert isinstance(instance, qvtoperational_ModelType)



@given(instance=qvtoperational_ModelType_strategy)
def test_qvtoperational_modeltype_conformanceKind_setter(instance):
    original = instance.conformanceKind
    instance.conformanceKind = original
    assert instance.conformanceKind == original

@given(instance=EntryOperation_strategy)
@settings(max_examples=50)
def test_entryoperation_instantiation(instance):
    assert isinstance(instance, EntryOperation)

@given(instance=ModelParameter_strategy)
@settings(max_examples=50)
def test_modelparameter_instantiation(instance):
    assert isinstance(instance, ModelParameter)

@given(instance=qvtoperational_ContextualProperty_strategy)
@settings(max_examples=50)
def test_qvtoperational_contextualproperty_instantiation(instance):
    assert isinstance(instance, qvtoperational_ContextualProperty)

@given(instance=ImperativeCallExp_strategy)
@settings(max_examples=50)
def test_imperativecallexp_instantiation(instance):
    assert isinstance(instance, ImperativeCallExp)

@given(instance=qvtoperational_MappingCallExp_strategy)
@settings(max_examples=50)
def test_qvtoperational_mappingcallexp_instantiation(instance):
    assert isinstance(instance, qvtoperational_MappingCallExp)



@given(instance=qvtoperational_MappingCallExp_strategy)
def test_qvtoperational_mappingcallexp_isStrict_setter(instance):
    original = instance.isStrict
    instance.isStrict = original
    assert instance.isStrict == original

@given(instance=RelationDomain_strategy)
@settings(max_examples=50)
def test_relationdomain_instantiation(instance):
    assert isinstance(instance, RelationDomain)

@given(instance=VarParameter_strategy)
@settings(max_examples=50)
def test_varparameter_instantiation(instance):
    assert isinstance(instance, VarParameter)

@given(instance=qvtoperational_ModelParameter_strategy)
@settings(max_examples=50)
def test_qvtoperational_modelparameter_instantiation(instance):
    assert isinstance(instance, qvtoperational_ModelParameter)

@given(instance=qvtoperational_MappingParameter_strategy)
@settings(max_examples=50)
def test_qvtoperational_mappingparameter_instantiation(instance):
    assert isinstance(instance, qvtoperational_MappingParameter)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=MappingOperation_strategy)
@settings(max_examples=50)
def test_mappingoperation_instantiation(instance):
    assert isinstance(instance, MappingOperation)

@given(instance=ResolveExp_strategy)
@settings(max_examples=50)
def test_resolveexp_instantiation(instance):
    assert isinstance(instance, ResolveExp)

@given(instance=qvtoperational_ResolveInExp_strategy)
@settings(max_examples=50)
def test_qvtoperational_resolveinexp_instantiation(instance):
    assert isinstance(instance, qvtoperational_ResolveInExp)

@given(instance=qvtoperational_ResolveExp_strategy)
@settings(max_examples=50)
def test_qvtoperational_resolveexp_instantiation(instance):
    assert isinstance(instance, qvtoperational_ResolveExp)



@given(instance=qvtoperational_ResolveExp_strategy)
def test_qvtoperational_resolveexp_isDeferred_setter(instance):
    original = instance.isDeferred
    instance.isDeferred = original
    assert instance.isDeferred == original



@given(instance=qvtoperational_ResolveExp_strategy)
def test_qvtoperational_resolveexp_one_setter(instance):
    original = instance.one
    instance.one = original
    assert instance.one == original



@given(instance=qvtoperational_ResolveExp_strategy)
def test_qvtoperational_resolveexp_isInverse_setter(instance):
    original = instance.isInverse
    instance.isInverse = original
    assert instance.isInverse == original

@given(instance=ImperativeOperation_strategy)
@settings(max_examples=50)
def test_imperativeoperation_instantiation(instance):
    assert isinstance(instance, ImperativeOperation)

@given(instance=qvtoperational_EntryOperation_strategy)
@settings(max_examples=50)
def test_qvtoperational_entryoperation_instantiation(instance):
    assert isinstance(instance, qvtoperational_EntryOperation)

@given(instance=qvtoperational_Constructor_strategy)
@settings(max_examples=50)
def test_qvtoperational_constructor_instantiation(instance):
    assert isinstance(instance, qvtoperational_Constructor)

@given(instance=qvtoperational_Helper_strategy)
@settings(max_examples=50)
def test_qvtoperational_helper_instantiation(instance):
    assert isinstance(instance, qvtoperational_Helper)



@given(instance=qvtoperational_Helper_strategy)
def test_qvtoperational_helper_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=OperationBody_strategy)
@settings(max_examples=50)
def test_operationbody_instantiation(instance):
    assert isinstance(instance, OperationBody)

@given(instance=qvtoperational_ConstructorBody_strategy)
@settings(max_examples=50)
def test_qvtoperational_constructorbody_instantiation(instance):
    assert isinstance(instance, qvtoperational_ConstructorBody)

@given(instance=qvtoperational_MappingBody_strategy)
@settings(max_examples=50)
def test_qvtoperational_mappingbody_instantiation(instance):
    assert isinstance(instance, qvtoperational_MappingBody)

@given(instance=emof_Comment_strategy)
@settings(max_examples=50)
def test_emof_comment_instantiation(instance):
    assert isinstance(instance, emof_Comment)

@given(instance=Extent_strategy)
@settings(max_examples=50)
def test_extent_instantiation(instance):
    assert isinstance(instance, Extent)

@given(instance=emof_URIExtent_strategy)
@settings(max_examples=50)
def test_emof_uriextent_instantiation(instance):
    assert isinstance(instance, emof_URIExtent)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=Enumeration_strategy)
@settings(max_examples=50)
def test_enumeration_instantiation(instance):
    assert isinstance(instance, Enumeration)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=qvtoperational_Module_strategy)
@settings(max_examples=50)
def test_qvtoperational_module_instantiation(instance):
    assert isinstance(instance, qvtoperational_Module)



@given(instance=qvtoperational_Module_strategy)
def test_qvtoperational_module_isBlackbox_setter(instance):
    original = instance.isBlackbox
    instance.isBlackbox = original
    assert instance.isBlackbox == original

@given(instance=qvtbase_Transformation_strategy)
@settings(max_examples=50)
def test_qvtbase_transformation_instantiation(instance):
    assert isinstance(instance, qvtbase_Transformation)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=emof_TypedElement_strategy)
@settings(max_examples=50)
def test_emof_typedelement_instantiation(instance):
    assert isinstance(instance, emof_TypedElement)

@given(instance=qvtbase_Domain_strategy)
@settings(max_examples=50)
def test_qvtbase_domain_instantiation(instance):
    assert isinstance(instance, qvtbase_Domain)



@given(instance=qvtbase_Domain_strategy)
def test_qvtbase_domain_isCheckable_setter(instance):
    original = instance.isCheckable
    instance.isCheckable = original
    assert instance.isCheckable == original



@given(instance=qvtbase_Domain_strategy)
def test_qvtbase_domain_isEnforceable_setter(instance):
    original = instance.isEnforceable
    instance.isEnforceable = original
    assert instance.isEnforceable == original

@given(instance=qvtbase_Rule_strategy)
@settings(max_examples=50)
def test_qvtbase_rule_instantiation(instance):
    assert isinstance(instance, qvtbase_Rule)

@given(instance=emof_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_emof_enumerationliteral_instantiation(instance):
    assert isinstance(instance, emof_EnumerationLiteral)

@given(instance=emof_Type_strategy)
@settings(max_examples=50)
def test_emof_type_instantiation(instance):
    assert isinstance(instance, emof_Type)

@given(instance=qvtbase_TypedModel_strategy)
@settings(max_examples=50)
def test_qvtbase_typedmodel_instantiation(instance):
    assert isinstance(instance, qvtbase_TypedModel)

@given(instance=emof_Package_strategy)
@settings(max_examples=50)
def test_emof_package_instantiation(instance):
    assert isinstance(instance, emof_Package)



@given(instance=emof_Package_strategy)
def test_emof_package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=emof_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_emof_multiplicityelement_instantiation(instance):
    assert isinstance(instance, emof_MultiplicityElement)



@given(instance=emof_MultiplicityElement_strategy)
def test_emof_multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=emof_MultiplicityElement_strategy)
def test_emof_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=emof_MultiplicityElement_strategy)
def test_emof_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=emof_MultiplicityElement_strategy)
def test_emof_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=imperativeocl_ListType_strategy)
@settings(max_examples=50)
def test_imperativeocl_listtype_instantiation(instance):
    assert isinstance(instance, imperativeocl_ListType)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=essentialocl_CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_essentialocl_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, essentialocl_CollectionLiteralPart)

@given(instance=essentialocl_TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_essentialocl_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, essentialocl_TupleLiteralPart)

@given(instance=essentialocl_OclExpression_strategy)
@settings(max_examples=50)
def test_essentialocl_oclexpression_instantiation(instance):
    assert isinstance(instance, essentialocl_OclExpression)

@given(instance=essentialocl_Variable_strategy)
@settings(max_examples=50)
def test_essentialocl_variable_instantiation(instance):
    assert isinstance(instance, essentialocl_Variable)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=emof_Property_strategy)
@settings(max_examples=50)
def test_emof_property_instantiation(instance):
    assert isinstance(instance, emof_Property)



@given(instance=emof_Property_strategy)
def test_emof_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=emof_Property_strategy)
def test_emof_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=emof_Property_strategy)
def test_emof_property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original



@given(instance=emof_Property_strategy)
def test_emof_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=emof_Property_strategy)
def test_emof_property_isId_setter(instance):
    original = instance.isId
    instance.isId = original
    assert instance.isId == original

@given(instance=emof_Parameter_strategy)
@settings(max_examples=50)
def test_emof_parameter_instantiation(instance):
    assert isinstance(instance, emof_Parameter)

@given(instance=emof_Operation_strategy)
@settings(max_examples=50)
def test_emof_operation_instantiation(instance):
    assert isinstance(instance, emof_Operation)

@given(instance=emof_Object_strategy)
@settings(max_examples=50)
def test_emof_object_instantiation(instance):
    assert isinstance(instance, emof_Object)

@given(instance=emof_NamedElement_strategy)
@settings(max_examples=50)
def test_emof_namedelement_instantiation(instance):
    assert isinstance(instance, emof_NamedElement)



@given(instance=emof_NamedElement_strategy)
def test_emof_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=essentialocl_TupleType_strategy)
@settings(max_examples=50)
def test_essentialocl_tupletype_instantiation(instance):
    assert isinstance(instance, essentialocl_TupleType)

@given(instance=emof_PrimitiveType_strategy)
@settings(max_examples=50)
def test_emof_primitivetype_instantiation(instance):
    assert isinstance(instance, emof_PrimitiveType)

@given(instance=essentialocl_CollectionType_strategy)
@settings(max_examples=50)
def test_essentialocl_collectiontype_instantiation(instance):
    assert isinstance(instance, essentialocl_CollectionType)

@given(instance=emof_Enumeration_strategy)
@settings(max_examples=50)
def test_emof_enumeration_instantiation(instance):
    assert isinstance(instance, emof_Enumeration)

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=qvtoperational_Library_strategy)
@settings(max_examples=50)
def test_qvtoperational_library_instantiation(instance):
    assert isinstance(instance, qvtoperational_Library)

@given(instance=qvtoperational_OperationalTransformation_strategy)
@settings(max_examples=50)
def test_qvtoperational_operationaltransformation_instantiation(instance):
    assert isinstance(instance, qvtoperational_OperationalTransformation)

@given(instance=Transformation_strategy)
@settings(max_examples=50)
def test_transformation_instantiation(instance):
    assert isinstance(instance, Transformation)

@given(instance=qvtrelation_RelationalTransformation_strategy)
@settings(max_examples=50)
def test_qvtrelation_relationaltransformation_instantiation(instance):
    assert isinstance(instance, qvtrelation_RelationalTransformation)

@given(instance=emof_Tag_strategy)
@settings(max_examples=50)
def test_emof_tag_instantiation(instance):
    assert isinstance(instance, emof_Tag)



@given(instance=emof_Tag_strategy)
def test_emof_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=emof_Tag_strategy)
def test_emof_tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=Tag_strategy)
@settings(max_examples=50)
def test_tag_instantiation(instance):
    assert isinstance(instance, Tag)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=emof_Extent_strategy)
@settings(max_examples=50)
def test_emof_extent_instantiation(instance):
    assert isinstance(instance, emof_Extent)

@given(instance=emof_Element_strategy)
@settings(max_examples=50)
def test_emof_element_instantiation(instance):
    assert isinstance(instance, emof_Element)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=qvtoperational_ImperativeOperation_strategy)
@settings(max_examples=50)
def test_qvtoperational_imperativeoperation_instantiation(instance):
    assert isinstance(instance, qvtoperational_ImperativeOperation)



@given(instance=qvtoperational_ImperativeOperation_strategy)
def test_qvtoperational_imperativeoperation_isBlackbox_setter(instance):
    original = instance.isBlackbox
    instance.isBlackbox = original
    assert instance.isBlackbox == original

@given(instance=qvtoperational_MappingOperation_strategy)
@settings(max_examples=50)
def test_qvtoperational_mappingoperation_instantiation(instance):
    assert isinstance(instance, qvtoperational_MappingOperation)

@given(instance=qvtbase_Function_strategy)
@settings(max_examples=50)
def test_qvtbase_function_instantiation(instance):
    assert isinstance(instance, qvtbase_Function)

@given(instance=imperativeocl_AnonymousTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl_anonymoustupleliteralpart_instantiation(instance):
    assert isinstance(instance, imperativeocl_AnonymousTupleLiteralPart)

@given(instance=AnonymousTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_anonymoustupleliteralpart_instantiation(instance):
    assert isinstance(instance, AnonymousTupleLiteralPart)

@given(instance=imperativeocl_AnonymousTupleType_strategy)
@settings(max_examples=50)
def test_imperativeocl_anonymoustupletype_instantiation(instance):
    assert isinstance(instance, imperativeocl_AnonymousTupleType)

@given(instance=imperativeocl_UnpackExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_unpackexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_UnpackExp)

@given(instance=imperativeocl_CollectorExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_collectorexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_CollectorExp)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=essentialocl_IteratorExp_strategy)
@settings(max_examples=50)
def test_essentialocl_iteratorexp_instantiation(instance):
    assert isinstance(instance, essentialocl_IteratorExp)

@given(instance=essentialocl_IterateExp_strategy)
@settings(max_examples=50)
def test_essentialocl_iterateexp_instantiation(instance):
    assert isinstance(instance, essentialocl_IterateExp)

@given(instance=imperativeocl_ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_ImperativeLoopExp)

@given(instance=LogExp_strategy)
@settings(max_examples=50)
def test_logexp_instantiation(instance):
    assert isinstance(instance, LogExp)

@given(instance=imperativeocl_AssertExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_assertexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_AssertExp)



@given(instance=imperativeocl_AssertExp_strategy)
def test_imperativeocl_assertexp_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=imperativeocl_TupleExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_tupleexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_TupleExp)

@given(instance=imperativeocl_ForExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_forexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_ForExp)

@given(instance=imperativeocl_ContinueExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_continueexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_ContinueExp)

@given(instance=imperativeocl_LogExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_logexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_LogExp)



@given(instance=imperativeocl_LogExp_strategy)
def test_imperativeocl_logexp_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=imperativeocl_LogExp_strategy)
def test_imperativeocl_logexp_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=imperativeocl_DictLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl_dictliteralpart_instantiation(instance):
    assert isinstance(instance, imperativeocl_DictLiteralPart)

@given(instance=DictLiteralPart_strategy)
@settings(max_examples=50)
def test_dictliteralpart_instantiation(instance):
    assert isinstance(instance, DictLiteralPart)

@given(instance=imperativeocl_DictionaryType_strategy)
@settings(max_examples=50)
def test_imperativeocl_dictionarytype_instantiation(instance):
    assert isinstance(instance, imperativeocl_DictionaryType)

@given(instance=imperativeocl_InstantiationExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_instantiationexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_InstantiationExp)

@given(instance=imperativeocl_Typedef_strategy)
@settings(max_examples=50)
def test_imperativeocl_typedef_instantiation(instance):
    assert isinstance(instance, imperativeocl_Typedef)

@given(instance=imperativeocl_WhileExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_whileexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_WhileExp)

@given(instance=imperativeocl_RaiseExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_raiseexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_RaiseExp)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=emof_Class_strategy)
@settings(max_examples=50)
def test_emof_class_instantiation(instance):
    assert isinstance(instance, emof_Class)



@given(instance=emof_Class_strategy)
def test_emof_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=imperativeocl_TemplateParameterType_strategy)
@settings(max_examples=50)
def test_imperativeocl_templateparametertype_instantiation(instance):
    assert isinstance(instance, imperativeocl_TemplateParameterType)



@given(instance=imperativeocl_TemplateParameterType_strategy)
def test_imperativeocl_templateparametertype_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=essentialocl_InvalidType_strategy)
@settings(max_examples=50)
def test_essentialocl_invalidtype_instantiation(instance):
    assert isinstance(instance, essentialocl_InvalidType)

@given(instance=essentialocl_AnyType_strategy)
@settings(max_examples=50)
def test_essentialocl_anytype_instantiation(instance):
    assert isinstance(instance, essentialocl_AnyType)

@given(instance=essentialocl_VoidType_strategy)
@settings(max_examples=50)
def test_essentialocl_voidtype_instantiation(instance):
    assert isinstance(instance, essentialocl_VoidType)

@given(instance=emof_DataType_strategy)
@settings(max_examples=50)
def test_emof_datatype_instantiation(instance):
    assert isinstance(instance, emof_DataType)

@given(instance=imperativeocl_TryExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_tryexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_TryExp)

@given(instance=PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_propertytemplateitem_instantiation(instance):
    assert isinstance(instance, PropertyTemplateItem)

@given(instance=TemplateExp_strategy)
@settings(max_examples=50)
def test_templateexp_instantiation(instance):
    assert isinstance(instance, TemplateExp)

@given(instance=qvttemplate_CollectionTemplateExp_strategy)
@settings(max_examples=50)
def test_qvttemplate_collectiontemplateexp_instantiation(instance):
    assert isinstance(instance, qvttemplate_CollectionTemplateExp)



@given(instance=qvttemplate_CollectionTemplateExp_strategy)
def test_qvttemplate_collectiontemplateexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=qvttemplate_ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_qvttemplate_objecttemplateexp_instantiation(instance):
    assert isinstance(instance, qvttemplate_ObjectTemplateExp)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=essentialocl_CallExp_strategy)
@settings(max_examples=50)
def test_essentialocl_callexp_instantiation(instance):
    assert isinstance(instance, essentialocl_CallExp)

@given(instance=essentialocl_TypeExp_strategy)
@settings(max_examples=50)
def test_essentialocl_typeexp_instantiation(instance):
    assert isinstance(instance, essentialocl_TypeExp)

@given(instance=essentialocl_LoopExp_strategy)
@settings(max_examples=50)
def test_essentialocl_loopexp_instantiation(instance):
    assert isinstance(instance, essentialocl_LoopExp)

@given(instance=essentialocl_LiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_literalexp_instantiation(instance):
    assert isinstance(instance, essentialocl_LiteralExp)

@given(instance=essentialocl_VariableExp_strategy)
@settings(max_examples=50)
def test_essentialocl_variableexp_instantiation(instance):
    assert isinstance(instance, essentialocl_VariableExp)

@given(instance=imperativeocl_ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeocl_imperativeexpression_instantiation(instance):
    assert isinstance(instance, imperativeocl_ImperativeExpression)

@given(instance=essentialocl_IfExp_strategy)
@settings(max_examples=50)
def test_essentialocl_ifexp_instantiation(instance):
    assert isinstance(instance, essentialocl_IfExp)

@given(instance=essentialocl_LetExp_strategy)
@settings(max_examples=50)
def test_essentialocl_letexp_instantiation(instance):
    assert isinstance(instance, essentialocl_LetExp)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=qvtoperational_VarParameter_strategy)
@settings(max_examples=50)
def test_qvtoperational_varparameter_instantiation(instance):
    assert isinstance(instance, qvtoperational_VarParameter)



@given(instance=qvtoperational_VarParameter_strategy)
def test_qvtoperational_varparameter_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=qvtbase_FunctionParameter_strategy)
@settings(max_examples=50)
def test_qvtbase_functionparameter_instantiation(instance):
    assert isinstance(instance, qvtbase_FunctionParameter)

@given(instance=qvtcore_RealizedVariable_strategy)
@settings(max_examples=50)
def test_qvtcore_realizedvariable_instantiation(instance):
    assert isinstance(instance, qvtcore_RealizedVariable)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=essentialocl_InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_invalidliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl_InvalidLiteralExp)

@given(instance=imperativeocl_DictLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_dictliteralexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_DictLiteralExp)

@given(instance=essentialocl_NullLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_nullliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl_NullLiteralExp)

@given(instance=essentialocl_TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl_TupleLiteralExp)

@given(instance=essentialocl_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_enumliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl_EnumLiteralExp)

@given(instance=essentialocl_PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl_PrimitiveLiteralExp)

@given(instance=essentialocl_CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl_CollectionLiteralExp)



@given(instance=essentialocl_CollectionLiteralExp_strategy)
def test_essentialocl_collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=imperativeocl_AnonymousTupleLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_anonymoustupleliteralexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_AnonymousTupleLiteralExp)

@given(instance=qvttemplate_TemplateExp_strategy)
@settings(max_examples=50)
def test_qvttemplate_templateexp_instantiation(instance):
    assert isinstance(instance, qvttemplate_TemplateExp)
