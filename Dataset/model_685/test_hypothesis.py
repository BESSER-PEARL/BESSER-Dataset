import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TryExp,
    TypedElement,
    JTL_essentialocl_OclExpression,
    PrimitiveLiteralExp,
    JTL_essentialocl_BooleanLiteralExp,
    Relation,
    Model,
    emof_Package,
    emof_Class,
    JTL_JTL_Transformation,
    Extent,
    JTL_emof_URIExtent,
    Pattern,
    Variable,
    When,
    Where,
    Domain,
    Transformation,
    JTL_emof_MultiplicityElement,
    Parameter,
    emof_TypedElement,
    emof_MultiplicityElement,
    JTL_emof_Operation,
    JTL_emof_Object,
    JTL_emof_Property,
    Enumeration,
    JTL_emof_Parameter,
    Package,
    NamedElement,
    JTL_JTL_Model,
    JTL_emof_EnumerationLiteral,
    JTL_JTL_Relation,
    JTL_JTL_Domain,
    JTL_emof_TypedElement,
    JTL_emof_Type,
    JTL_emof_Package,
    Property,
    Type,
    JTL_emof_Class,
    EnumerationLiteral,
    DataType,
    JTL_emof_PrimitiveType,
    JTL_emof_Enumeration,
    Element,
    JTL_emof_NamedElement,
    JTL_emof_Comment,
    JTL_emof_Tag,
    Comment,
    Tag,
    Object,
    JTL_emof_Extent,
    JTL_emof_Element,
    JTL_emof_DataType,
    Class,
    Operation,
    JTL_imperativeocl_AnonymousTupleLiteralPart,
    AnonymousTupleLiteralPart,
    JTL_imperativeocl_AnonymousTupleType,
    JTL_imperativeocl_TemplateParameterType,
    JTL_imperativeocl_DictLiteralPart,
    DictLiteralPart,
    essentialocl_LoopExp,
    LogExp,
    JTL_imperativeocl_Typedef,
    AltExp,
    imperativeocl_ImperativeExpression,
    JTL_imperativeocl_ImperativeLoopExp,
    AssignExp,
    PropertyTemplateItem,
    ImperativeExpression,
    JTL_imperativeocl_ContinueExp,
    JTL_imperativeocl_RaiseExp,
    JTL_imperativeocl_BlockExp,
    JTL_imperativeocl_AltExp,
    JTL_imperativeocl_UnlinkExp,
    JTL_imperativeocl_WhileExp,
    JTL_imperativeocl_UnpackExp,
    JTL_imperativeocl_InstantiationExp,
    JTL_imperativeocl_BreakExp,
    JTL_imperativeocl_TryExp,
    JTL_imperativeocl_VariableInitExp,
    JTL_imperativeocl_TupleExp,
    JTL_imperativeocl_LogExp,
    JTL_imperativeocl_ComputeExp,
    JTL_imperativeocl_AssertExp,
    JTL_imperativeocl_ReturnExp,
    JTL_imperativeocl_AssignExp,
    ImperativeLoopExp,
    JTL_imperativeocl_CollectorExp,
    JTL_imperativeocl_ForExp,
    JTL_imperativeocl_ImperativeIterateExp,
    ObjectTemplateExp,
    JTL_template_PropertyTemplateItem,
    JTL_essentialocl_CollectionType,
    CollectionType,
    JTL_imperativeocl_DictionaryType,
    JTL_imperativeocl_ListType,
    JTL_essentialocl_BagType,
    TupleLiteralExp,
    JTL_essentialocl_TupleLiteralPart,
    CallExp,
    JTL_essentialocl_FeaturePropertyCall,
    JTL_essentialocl_OpaqueExpression,
    emof_Type,
    JTL_essentialocl_AnyType,
    JTL_essentialocl_VoidType,
    emof_DataType,
    JTL_essentialocl_TupleType,
    JTL_essentialocl_SetType,
    JTL_essentialocl_SequenceType,
    JTL_essentialocl_OrderedSetType,
    JTL_essentialocl_InvalidType,
    CollectionLiteralExp,
    JTL_essentialocl_CollectionLiteralPart,
    CollectionLiteralPart,
    JTL_essentialocl_NumericLiteralExp,
    LiteralExp,
    JTL_essentialocl_EnumLiteralExp,
    JTL_essentialocl_InvalidLiteralExp,
    JTL_essentialocl_CollectionLiteralExp,
    JTL_imperativeocl_AnonymousTupleLiteralExp,
    JTL_imperativeocl_DictLiteralExp,
    JTL_template_TemplateExp,
    JTL_essentialocl_PrimitiveLiteralExp,
    OpaqueExpression,
    JTL_essentialocl_ExpressionInOcl,
    JTL_essentialocl_NullLiteralExp,
    TupleLiteralPart,
    JTL_essentialocl_TupleLiteralExp,
    JTL_essentialocl_CollectionRange,
    JTL_essentialocl_CollectionItem,
    FeaturePropertyCall,
    JTL_essentialocl_PropertyCallExp,
    ComputeExp,
    LetExp,
    JTL_essentialocl_Variable,
    JTL_essentialocl_OperationCallExp,
    JTL_essentialocl_StringLiteralExp,
    LoopExp,
    JTL_essentialocl_IterateExp,
    JTL_essentialocl_IteratorExp,
    essentialocl_OclExpression,
    essentialocl_CallExp,
    JTL_imperativeocl_SwitchExp,
    JTL_essentialocl_LoopExp,
    JTL_JTL_Where,
    JTL_JTL_When,
    OclExpression,
    JTL_essentialocl_LetExp,
    JTL_essentialocl_TypeExp,
    JTL_imperativeocl_ImperativeExpression,
    JTL_essentialocl_VariableExp,
    JTL_essentialocl_LiteralExp,
    JTL_essentialocl_CallExp,
    JTL_JTL_Predicate,
    TemplateExp,
    JTL_template_CollectionTemplateExp,
    JTL_template_ObjectTemplateExp,
    Predicate,
    JTL_JTL_Pattern,
    JTL_essentialocl_IfExp,
    NumericLiteralExp,
    JTL_essentialocl_IntegerLiteralExp,
    JTL_essentialocl_RealLiteralExp,
    JTL_essentialocl_UnlimitedNaturalExp,
    SeverityKind,
    CollectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tryexp_is_not_abstract():
    assert not inspect.isabstract(TryExp)


def test_tryexp_constructor_exists():
    assert callable(TryExp.__init__)


def test_tryexp_constructor_args():
    sig = inspect.signature(TryExp.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_OclExpression)


def test_jtl_essentialocl_oclexpression_constructor_exists():
    assert callable(JTL_essentialocl_OclExpression.__init__)


def test_jtl_essentialocl_oclexpression_constructor_args():
    sig = inspect.signature(JTL_essentialocl_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_BooleanLiteralExp)


def test_jtl_essentialocl_booleanliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_BooleanLiteralExp.__init__)


def test_jtl_essentialocl_booleanliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_jtl_essentialocl_booleanliteralexp_has_booleanSymbol():
    assert hasattr(JTL_essentialocl_BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in JTL_essentialocl_BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_model_is_not_abstract():
    assert not inspect.isabstract(Model)


def test_model_constructor_exists():
    assert callable(Model.__init__)


def test_model_constructor_args():
    sig = inspect.signature(Model.__init__)
    params = list(sig.parameters.keys())



def test_emof_package_is_not_abstract():
    assert not inspect.isabstract(emof_Package)


def test_emof_package_constructor_exists():
    assert callable(emof_Package.__init__)


def test_emof_package_constructor_args():
    sig = inspect.signature(emof_Package.__init__)
    params = list(sig.parameters.keys())



def test_emof_class_is_not_abstract():
    assert not inspect.isabstract(emof_Class)


def test_emof_class_constructor_exists():
    assert callable(emof_Class.__init__)


def test_emof_class_constructor_args():
    sig = inspect.signature(emof_Class.__init__)
    params = list(sig.parameters.keys())



def test_jtl_jtl_transformation_is_not_abstract():
    assert not inspect.isabstract(JTL_JTL_Transformation)


def test_jtl_jtl_transformation_constructor_exists():
    assert callable(JTL_JTL_Transformation.__init__)


def test_jtl_jtl_transformation_constructor_args():
    sig = inspect.signature(JTL_JTL_Transformation.__init__)
    params = list(sig.parameters.keys())



def test_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_jtl_emof_uriextent_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_URIExtent)


def test_jtl_emof_uriextent_constructor_exists():
    assert callable(JTL_emof_URIExtent.__init__)


def test_jtl_emof_uriextent_constructor_args():
    sig = inspect.signature(JTL_emof_URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_when_is_not_abstract():
    assert not inspect.isabstract(When)


def test_when_constructor_exists():
    assert callable(When.__init__)


def test_when_constructor_args():
    sig = inspect.signature(When.__init__)
    params = list(sig.parameters.keys())



def test_where_is_not_abstract():
    assert not inspect.isabstract(Where)


def test_where_constructor_exists():
    assert callable(Where.__init__)


def test_where_constructor_args():
    sig = inspect.signature(Where.__init__)
    params = list(sig.parameters.keys())



def test_domain_is_not_abstract():
    assert not inspect.isabstract(Domain)


def test_domain_constructor_exists():
    assert callable(Domain.__init__)


def test_domain_constructor_args():
    sig = inspect.signature(Domain.__init__)
    params = list(sig.parameters.keys())



def test_transformation_is_not_abstract():
    assert not inspect.isabstract(Transformation)


def test_transformation_constructor_exists():
    assert callable(Transformation.__init__)


def test_transformation_constructor_args():
    sig = inspect.signature(Transformation.__init__)
    params = list(sig.parameters.keys())



def test_jtl_emof_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_MultiplicityElement)


def test_jtl_emof_multiplicityelement_constructor_exists():
    assert callable(JTL_emof_MultiplicityElement.__init__)


def test_jtl_emof_multiplicityelement_constructor_args():
    sig = inspect.signature(JTL_emof_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_jtl_emof_multiplicityelement_has_isUnique():
    assert hasattr(JTL_emof_MultiplicityElement, "isUnique")
    descriptor = None
    for klass in JTL_emof_MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_jtl_emof_multiplicityelement_has_upper():
    assert hasattr(JTL_emof_MultiplicityElement, "upper")
    descriptor = None
    for klass in JTL_emof_MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_jtl_emof_multiplicityelement_has_isOrdered():
    assert hasattr(JTL_emof_MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in JTL_emof_MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_jtl_emof_multiplicityelement_has_lower():
    assert hasattr(JTL_emof_MultiplicityElement, "lower")
    descriptor = None
    for klass in JTL_emof_MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_emof_typedelement_is_not_abstract():
    assert not inspect.isabstract(emof_TypedElement)


def test_emof_typedelement_constructor_exists():
    assert callable(emof_TypedElement.__init__)


def test_emof_typedelement_constructor_args():
    sig = inspect.signature(emof_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_emof_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(emof_MultiplicityElement)


def test_emof_multiplicityelement_constructor_exists():
    assert callable(emof_MultiplicityElement.__init__)


def test_emof_multiplicityelement_constructor_args():
    sig = inspect.signature(emof_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_jtl_emof_operation_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Operation)


def test_jtl_emof_operation_constructor_exists():
    assert callable(JTL_emof_Operation.__init__)


def test_jtl_emof_operation_constructor_args():
    sig = inspect.signature(JTL_emof_Operation.__init__)
    params = list(sig.parameters.keys())



def test_jtl_emof_object_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Object)


def test_jtl_emof_object_constructor_exists():
    assert callable(JTL_emof_Object.__init__)


def test_jtl_emof_object_constructor_args():
    sig = inspect.signature(JTL_emof_Object.__init__)
    params = list(sig.parameters.keys())



def test_jtl_emof_property_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Property)


def test_jtl_emof_property_constructor_exists():
    assert callable(JTL_emof_Property.__init__)


def test_jtl_emof_property_constructor_args():
    sig = inspect.signature(JTL_emof_Property.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isId" in params, "Missing parameter 'isId'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "default" in params, "Missing parameter 'default'"

def test_jtl_emof_property_has_isDerived():
    assert hasattr(JTL_emof_Property, "isDerived")
    descriptor = None
    for klass in JTL_emof_Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_jtl_emof_property_has_isId():
    assert hasattr(JTL_emof_Property, "isId")
    descriptor = None
    for klass in JTL_emof_Property.__mro__:
        if "isId" in klass.__dict__:
            descriptor = klass.__dict__["isId"]
            break
    assert isinstance(descriptor, property)

def test_jtl_emof_property_has_isReadOnly():
    assert hasattr(JTL_emof_Property, "isReadOnly")
    descriptor = None
    for klass in JTL_emof_Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_jtl_emof_property_has_isComposite():
    assert hasattr(JTL_emof_Property, "isComposite")
    descriptor = None
    for klass in JTL_emof_Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_jtl_emof_property_has_default():
    assert hasattr(JTL_emof_Property, "default")
    descriptor = None
    for klass in JTL_emof_Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_enumeration_is_not_abstract():
    assert not inspect.isabstract(Enumeration)


def test_enumeration_constructor_exists():
    assert callable(Enumeration.__init__)


def test_enumeration_constructor_args():
    sig = inspect.signature(Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_jtl_emof_parameter_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Parameter)


def test_jtl_emof_parameter_constructor_exists():
    assert callable(JTL_emof_Parameter.__init__)


def test_jtl_emof_parameter_constructor_args():
    sig = inspect.signature(JTL_emof_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_jtl_jtl_model_is_not_abstract():
    assert not inspect.isabstract(JTL_JTL_Model)


def test_jtl_jtl_model_constructor_exists():
    assert callable(JTL_JTL_Model.__init__)


def test_jtl_jtl_model_constructor_args():
    sig = inspect.signature(JTL_JTL_Model.__init__)
    params = list(sig.parameters.keys())
    assert "usedPackage" in params, "Missing parameter 'usedPackage'"

def test_jtl_jtl_model_has_usedPackage():
    assert hasattr(JTL_JTL_Model, "usedPackage")
    descriptor = None
    for klass in JTL_JTL_Model.__mro__:
        if "usedPackage" in klass.__dict__:
            descriptor = klass.__dict__["usedPackage"]
            break
    assert isinstance(descriptor, property)



def test_jtl_emof_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_EnumerationLiteral)


def test_jtl_emof_enumerationliteral_constructor_exists():
    assert callable(JTL_emof_EnumerationLiteral.__init__)


def test_jtl_emof_enumerationliteral_constructor_args():
    sig = inspect.signature(JTL_emof_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_jtl_jtl_relation_is_not_abstract():
    assert not inspect.isabstract(JTL_JTL_Relation)


def test_jtl_jtl_relation_constructor_exists():
    assert callable(JTL_JTL_Relation.__init__)


def test_jtl_jtl_relation_constructor_args():
    sig = inspect.signature(JTL_JTL_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "isTopLevel" in params, "Missing parameter 'isTopLevel'"

def test_jtl_jtl_relation_has_isTopLevel():
    assert hasattr(JTL_JTL_Relation, "isTopLevel")
    descriptor = None
    for klass in JTL_JTL_Relation.__mro__:
        if "isTopLevel" in klass.__dict__:
            descriptor = klass.__dict__["isTopLevel"]
            break
    assert isinstance(descriptor, property)



def test_jtl_jtl_domain_is_not_abstract():
    assert not inspect.isabstract(JTL_JTL_Domain)


def test_jtl_jtl_domain_constructor_exists():
    assert callable(JTL_JTL_Domain.__init__)


def test_jtl_jtl_domain_constructor_args():
    sig = inspect.signature(JTL_JTL_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "isEnforceable" in params, "Missing parameter 'isEnforceable'"
    assert "isCheckable" in params, "Missing parameter 'isCheckable'"

def test_jtl_jtl_domain_has_isEnforceable():
    assert hasattr(JTL_JTL_Domain, "isEnforceable")
    descriptor = None
    for klass in JTL_JTL_Domain.__mro__:
        if "isEnforceable" in klass.__dict__:
            descriptor = klass.__dict__["isEnforceable"]
            break
    assert isinstance(descriptor, property)

def test_jtl_jtl_domain_has_isCheckable():
    assert hasattr(JTL_JTL_Domain, "isCheckable")
    descriptor = None
    for klass in JTL_JTL_Domain.__mro__:
        if "isCheckable" in klass.__dict__:
            descriptor = klass.__dict__["isCheckable"]
            break
    assert isinstance(descriptor, property)



def test_jtl_emof_typedelement_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_TypedElement)


def test_jtl_emof_typedelement_constructor_exists():
    assert callable(JTL_emof_TypedElement.__init__)


def test_jtl_emof_typedelement_constructor_args():
    sig = inspect.signature(JTL_emof_TypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_jtl_emof_typedelement_has_type():
    assert hasattr(JTL_emof_TypedElement, "type")
    descriptor = None
    for klass in JTL_emof_TypedElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_jtl_emof_type_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Type)


def test_jtl_emof_type_constructor_exists():
    assert callable(JTL_emof_Type.__init__)


def test_jtl_emof_type_constructor_args():
    sig = inspect.signature(JTL_emof_Type.__init__)
    params = list(sig.parameters.keys())



def test_jtl_emof_package_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Package)


def test_jtl_emof_package_constructor_exists():
    assert callable(JTL_emof_Package.__init__)


def test_jtl_emof_package_constructor_args():
    sig = inspect.signature(JTL_emof_Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_jtl_emof_package_has_uri():
    assert hasattr(JTL_emof_Package, "uri")
    descriptor = None
    for klass in JTL_emof_Package.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_jtl_emof_class_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Class)


def test_jtl_emof_class_constructor_exists():
    assert callable(JTL_emof_Class.__init__)


def test_jtl_emof_class_constructor_args():
    sig = inspect.signature(JTL_emof_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_jtl_emof_class_has_isAbstract():
    assert hasattr(JTL_emof_Class, "isAbstract")
    descriptor = None
    for klass in JTL_emof_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
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



def test_jtl_emof_primitivetype_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_PrimitiveType)


def test_jtl_emof_primitivetype_constructor_exists():
    assert callable(JTL_emof_PrimitiveType.__init__)


def test_jtl_emof_primitivetype_constructor_args():
    sig = inspect.signature(JTL_emof_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_jtl_emof_enumeration_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Enumeration)


def test_jtl_emof_enumeration_constructor_exists():
    assert callable(JTL_emof_Enumeration.__init__)


def test_jtl_emof_enumeration_constructor_args():
    sig = inspect.signature(JTL_emof_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_jtl_emof_namedelement_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_NamedElement)


def test_jtl_emof_namedelement_constructor_exists():
    assert callable(JTL_emof_NamedElement.__init__)


def test_jtl_emof_namedelement_constructor_args():
    sig = inspect.signature(JTL_emof_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jtl_emof_namedelement_has_name():
    assert hasattr(JTL_emof_NamedElement, "name")
    descriptor = None
    for klass in JTL_emof_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jtl_emof_comment_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Comment)


def test_jtl_emof_comment_constructor_exists():
    assert callable(JTL_emof_Comment.__init__)


def test_jtl_emof_comment_constructor_args():
    sig = inspect.signature(JTL_emof_Comment.__init__)
    params = list(sig.parameters.keys())



def test_jtl_emof_tag_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Tag)


def test_jtl_emof_tag_constructor_exists():
    assert callable(JTL_emof_Tag.__init__)


def test_jtl_emof_tag_constructor_args():
    sig = inspect.signature(JTL_emof_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_jtl_emof_tag_has_name():
    assert hasattr(JTL_emof_Tag, "name")
    descriptor = None
    for klass in JTL_emof_Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jtl_emof_tag_has_value():
    assert hasattr(JTL_emof_Tag, "value")
    descriptor = None
    for klass in JTL_emof_Tag.__mro__:
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



def test_jtl_emof_extent_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Extent)


def test_jtl_emof_extent_constructor_exists():
    assert callable(JTL_emof_Extent.__init__)


def test_jtl_emof_extent_constructor_args():
    sig = inspect.signature(JTL_emof_Extent.__init__)
    params = list(sig.parameters.keys())



def test_jtl_emof_element_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_Element)


def test_jtl_emof_element_constructor_exists():
    assert callable(JTL_emof_Element.__init__)


def test_jtl_emof_element_constructor_args():
    sig = inspect.signature(JTL_emof_Element.__init__)
    params = list(sig.parameters.keys())



def test_jtl_emof_datatype_is_not_abstract():
    assert not inspect.isabstract(JTL_emof_DataType)


def test_jtl_emof_datatype_constructor_exists():
    assert callable(JTL_emof_DataType.__init__)


def test_jtl_emof_datatype_constructor_args():
    sig = inspect.signature(JTL_emof_DataType.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_anonymoustupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_AnonymousTupleLiteralPart)


def test_jtl_imperativeocl_anonymoustupleliteralpart_constructor_exists():
    assert callable(JTL_imperativeocl_AnonymousTupleLiteralPart.__init__)


def test_jtl_imperativeocl_anonymoustupleliteralpart_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_AnonymousTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_anonymoustupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(AnonymousTupleLiteralPart)


def test_anonymoustupleliteralpart_constructor_exists():
    assert callable(AnonymousTupleLiteralPart.__init__)


def test_anonymoustupleliteralpart_constructor_args():
    sig = inspect.signature(AnonymousTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_anonymoustupletype_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_AnonymousTupleType)


def test_jtl_imperativeocl_anonymoustupletype_constructor_exists():
    assert callable(JTL_imperativeocl_AnonymousTupleType.__init__)


def test_jtl_imperativeocl_anonymoustupletype_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_AnonymousTupleType.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_templateparametertype_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_TemplateParameterType)


def test_jtl_imperativeocl_templateparametertype_constructor_exists():
    assert callable(JTL_imperativeocl_TemplateParameterType.__init__)


def test_jtl_imperativeocl_templateparametertype_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_TemplateParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_jtl_imperativeocl_templateparametertype_has_specification():
    assert hasattr(JTL_imperativeocl_TemplateParameterType, "specification")
    descriptor = None
    for klass in JTL_imperativeocl_TemplateParameterType.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_jtl_imperativeocl_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_DictLiteralPart)


def test_jtl_imperativeocl_dictliteralpart_constructor_exists():
    assert callable(JTL_imperativeocl_DictLiteralPart.__init__)


def test_jtl_imperativeocl_dictliteralpart_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(DictLiteralPart)


def test_dictliteralpart_constructor_exists():
    assert callable(DictLiteralPart.__init__)


def test_dictliteralpart_constructor_args():
    sig = inspect.signature(DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_loopexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_LoopExp)


def test_essentialocl_loopexp_constructor_exists():
    assert callable(essentialocl_LoopExp.__init__)


def test_essentialocl_loopexp_constructor_args():
    sig = inspect.signature(essentialocl_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_logexp_is_not_abstract():
    assert not inspect.isabstract(LogExp)


def test_logexp_constructor_exists():
    assert callable(LogExp.__init__)


def test_logexp_constructor_args():
    sig = inspect.signature(LogExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_typedef_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_Typedef)


def test_jtl_imperativeocl_typedef_constructor_exists():
    assert callable(JTL_imperativeocl_Typedef.__init__)


def test_jtl_imperativeocl_typedef_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_Typedef.__init__)
    params = list(sig.parameters.keys())



def test_altexp_is_not_abstract():
    assert not inspect.isabstract(AltExp)


def test_altexp_constructor_exists():
    assert callable(AltExp.__init__)


def test_altexp_constructor_args():
    sig = inspect.signature(AltExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ImperativeExpression)


def test_imperativeocl_imperativeexpression_constructor_exists():
    assert callable(imperativeocl_ImperativeExpression.__init__)


def test_imperativeocl_imperativeexpression_constructor_args():
    sig = inspect.signature(imperativeocl_ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_ImperativeLoopExp)


def test_jtl_imperativeocl_imperativeloopexp_constructor_exists():
    assert callable(JTL_imperativeocl_ImperativeLoopExp.__init__)


def test_jtl_imperativeocl_imperativeloopexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_assignexp_is_not_abstract():
    assert not inspect.isabstract(AssignExp)


def test_assignexp_constructor_exists():
    assert callable(AssignExp.__init__)


def test_assignexp_constructor_args():
    sig = inspect.signature(AssignExp.__init__)
    params = list(sig.parameters.keys())



def test_propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(PropertyTemplateItem)


def test_propertytemplateitem_constructor_exists():
    assert callable(PropertyTemplateItem.__init__)


def test_propertytemplateitem_constructor_args():
    sig = inspect.signature(PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())



def test_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeExpression)


def test_imperativeexpression_constructor_exists():
    assert callable(ImperativeExpression.__init__)


def test_imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_continueexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_ContinueExp)


def test_jtl_imperativeocl_continueexp_constructor_exists():
    assert callable(JTL_imperativeocl_ContinueExp.__init__)


def test_jtl_imperativeocl_continueexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_ContinueExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_raiseexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_RaiseExp)


def test_jtl_imperativeocl_raiseexp_constructor_exists():
    assert callable(JTL_imperativeocl_RaiseExp.__init__)


def test_jtl_imperativeocl_raiseexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_RaiseExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_blockexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_BlockExp)


def test_jtl_imperativeocl_blockexp_constructor_exists():
    assert callable(JTL_imperativeocl_BlockExp.__init__)


def test_jtl_imperativeocl_blockexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_altexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_AltExp)


def test_jtl_imperativeocl_altexp_constructor_exists():
    assert callable(JTL_imperativeocl_AltExp.__init__)


def test_jtl_imperativeocl_altexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_AltExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_unlinkexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_UnlinkExp)


def test_jtl_imperativeocl_unlinkexp_constructor_exists():
    assert callable(JTL_imperativeocl_UnlinkExp.__init__)


def test_jtl_imperativeocl_unlinkexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_UnlinkExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_whileexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_WhileExp)


def test_jtl_imperativeocl_whileexp_constructor_exists():
    assert callable(JTL_imperativeocl_WhileExp.__init__)


def test_jtl_imperativeocl_whileexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_WhileExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_unpackexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_UnpackExp)


def test_jtl_imperativeocl_unpackexp_constructor_exists():
    assert callable(JTL_imperativeocl_UnpackExp.__init__)


def test_jtl_imperativeocl_unpackexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_UnpackExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_instantiationexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_InstantiationExp)


def test_jtl_imperativeocl_instantiationexp_constructor_exists():
    assert callable(JTL_imperativeocl_InstantiationExp.__init__)


def test_jtl_imperativeocl_instantiationexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_breakexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_BreakExp)


def test_jtl_imperativeocl_breakexp_constructor_exists():
    assert callable(JTL_imperativeocl_BreakExp.__init__)


def test_jtl_imperativeocl_breakexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_BreakExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_tryexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_TryExp)


def test_jtl_imperativeocl_tryexp_constructor_exists():
    assert callable(JTL_imperativeocl_TryExp.__init__)


def test_jtl_imperativeocl_tryexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_TryExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_variableinitexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_VariableInitExp)


def test_jtl_imperativeocl_variableinitexp_constructor_exists():
    assert callable(JTL_imperativeocl_VariableInitExp.__init__)


def test_jtl_imperativeocl_variableinitexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_VariableInitExp.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_jtl_imperativeocl_variableinitexp_has_withResult():
    assert hasattr(JTL_imperativeocl_VariableInitExp, "withResult")
    descriptor = None
    for klass in JTL_imperativeocl_VariableInitExp.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_jtl_imperativeocl_tupleexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_TupleExp)


def test_jtl_imperativeocl_tupleexp_constructor_exists():
    assert callable(JTL_imperativeocl_TupleExp.__init__)


def test_jtl_imperativeocl_tupleexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_logexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_LogExp)


def test_jtl_imperativeocl_logexp_constructor_exists():
    assert callable(JTL_imperativeocl_LogExp.__init__)


def test_jtl_imperativeocl_logexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_LogExp.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "level" in params, "Missing parameter 'level'"

def test_jtl_imperativeocl_logexp_has_text():
    assert hasattr(JTL_imperativeocl_LogExp, "text")
    descriptor = None
    for klass in JTL_imperativeocl_LogExp.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_jtl_imperativeocl_logexp_has_level():
    assert hasattr(JTL_imperativeocl_LogExp, "level")
    descriptor = None
    for klass in JTL_imperativeocl_LogExp.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_jtl_imperativeocl_computeexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_ComputeExp)


def test_jtl_imperativeocl_computeexp_constructor_exists():
    assert callable(JTL_imperativeocl_ComputeExp.__init__)


def test_jtl_imperativeocl_computeexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_assertexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_AssertExp)


def test_jtl_imperativeocl_assertexp_constructor_exists():
    assert callable(JTL_imperativeocl_AssertExp.__init__)


def test_jtl_imperativeocl_assertexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_AssertExp.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_jtl_imperativeocl_assertexp_has_severity():
    assert hasattr(JTL_imperativeocl_AssertExp, "severity")
    descriptor = None
    for klass in JTL_imperativeocl_AssertExp.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_jtl_imperativeocl_returnexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_ReturnExp)


def test_jtl_imperativeocl_returnexp_constructor_exists():
    assert callable(JTL_imperativeocl_ReturnExp.__init__)


def test_jtl_imperativeocl_returnexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_ReturnExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_assignexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_AssignExp)


def test_jtl_imperativeocl_assignexp_constructor_exists():
    assert callable(JTL_imperativeocl_AssignExp.__init__)


def test_jtl_imperativeocl_assignexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_AssignExp.__init__)
    params = list(sig.parameters.keys())
    assert "isReset" in params, "Missing parameter 'isReset'"

def test_jtl_imperativeocl_assignexp_has_isReset():
    assert hasattr(JTL_imperativeocl_AssignExp, "isReset")
    descriptor = None
    for klass in JTL_imperativeocl_AssignExp.__mro__:
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



def test_jtl_imperativeocl_collectorexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_CollectorExp)


def test_jtl_imperativeocl_collectorexp_constructor_exists():
    assert callable(JTL_imperativeocl_CollectorExp.__init__)


def test_jtl_imperativeocl_collectorexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_CollectorExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_forexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_ForExp)


def test_jtl_imperativeocl_forexp_constructor_exists():
    assert callable(JTL_imperativeocl_ForExp.__init__)


def test_jtl_imperativeocl_forexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_ForExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_imperativeiterateexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_ImperativeIterateExp)


def test_jtl_imperativeocl_imperativeiterateexp_constructor_exists():
    assert callable(JTL_imperativeocl_ImperativeIterateExp.__init__)


def test_jtl_imperativeocl_imperativeiterateexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_ImperativeIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(ObjectTemplateExp)


def test_objecttemplateexp_constructor_exists():
    assert callable(ObjectTemplateExp.__init__)


def test_objecttemplateexp_constructor_args():
    sig = inspect.signature(ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_template_propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(JTL_template_PropertyTemplateItem)


def test_jtl_template_propertytemplateitem_constructor_exists():
    assert callable(JTL_template_PropertyTemplateItem.__init__)


def test_jtl_template_propertytemplateitem_constructor_args():
    sig = inspect.signature(JTL_template_PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_collectiontype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_CollectionType)


def test_jtl_essentialocl_collectiontype_constructor_exists():
    assert callable(JTL_essentialocl_CollectionType.__init__)


def test_jtl_essentialocl_collectiontype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_dictionarytype_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_DictionaryType)


def test_jtl_imperativeocl_dictionarytype_constructor_exists():
    assert callable(JTL_imperativeocl_DictionaryType.__init__)


def test_jtl_imperativeocl_dictionarytype_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_DictionaryType.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_listtype_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_ListType)


def test_jtl_imperativeocl_listtype_constructor_exists():
    assert callable(JTL_imperativeocl_ListType.__init__)


def test_jtl_imperativeocl_listtype_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_ListType.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_bagtype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_BagType)


def test_jtl_essentialocl_bagtype_constructor_exists():
    assert callable(JTL_essentialocl_BagType.__init__)


def test_jtl_essentialocl_bagtype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_BagType.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralExp)


def test_tupleliteralexp_constructor_exists():
    assert callable(TupleLiteralExp.__init__)


def test_tupleliteralexp_constructor_args():
    sig = inspect.signature(TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_TupleLiteralPart)


def test_jtl_essentialocl_tupleliteralpart_constructor_exists():
    assert callable(JTL_essentialocl_TupleLiteralPart.__init__)


def test_jtl_essentialocl_tupleliteralpart_constructor_args():
    sig = inspect.signature(JTL_essentialocl_TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_FeaturePropertyCall)


def test_jtl_essentialocl_featurepropertycall_constructor_exists():
    assert callable(JTL_essentialocl_FeaturePropertyCall.__init__)


def test_jtl_essentialocl_featurepropertycall_constructor_args():
    sig = inspect.signature(JTL_essentialocl_FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_OpaqueExpression)


def test_jtl_essentialocl_opaqueexpression_constructor_exists():
    assert callable(JTL_essentialocl_OpaqueExpression.__init__)


def test_jtl_essentialocl_opaqueexpression_constructor_args():
    sig = inspect.signature(JTL_essentialocl_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_emof_type_is_not_abstract():
    assert not inspect.isabstract(emof_Type)


def test_emof_type_constructor_exists():
    assert callable(emof_Type.__init__)


def test_emof_type_constructor_args():
    sig = inspect.signature(emof_Type.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_anytype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_AnyType)


def test_jtl_essentialocl_anytype_constructor_exists():
    assert callable(JTL_essentialocl_AnyType.__init__)


def test_jtl_essentialocl_anytype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_voidtype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_VoidType)


def test_jtl_essentialocl_voidtype_constructor_exists():
    assert callable(JTL_essentialocl_VoidType.__init__)


def test_jtl_essentialocl_voidtype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_emof_datatype_is_not_abstract():
    assert not inspect.isabstract(emof_DataType)


def test_emof_datatype_constructor_exists():
    assert callable(emof_DataType.__init__)


def test_emof_datatype_constructor_args():
    sig = inspect.signature(emof_DataType.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_tupletype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_TupleType)


def test_jtl_essentialocl_tupletype_constructor_exists():
    assert callable(JTL_essentialocl_TupleType.__init__)


def test_jtl_essentialocl_tupletype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_settype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_SetType)


def test_jtl_essentialocl_settype_constructor_exists():
    assert callable(JTL_essentialocl_SetType.__init__)


def test_jtl_essentialocl_settype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_SetType.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_sequencetype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_SequenceType)


def test_jtl_essentialocl_sequencetype_constructor_exists():
    assert callable(JTL_essentialocl_SequenceType.__init__)


def test_jtl_essentialocl_sequencetype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_OrderedSetType)


def test_jtl_essentialocl_orderedsettype_constructor_exists():
    assert callable(JTL_essentialocl_OrderedSetType.__init__)


def test_jtl_essentialocl_orderedsettype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_invalidtype_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_InvalidType)


def test_jtl_essentialocl_invalidtype_constructor_exists():
    assert callable(JTL_essentialocl_InvalidType.__init__)


def test_jtl_essentialocl_invalidtype_constructor_args():
    sig = inspect.signature(JTL_essentialocl_InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExp)


def test_collectionliteralexp_constructor_exists():
    assert callable(CollectionLiteralExp.__init__)


def test_collectionliteralexp_constructor_args():
    sig = inspect.signature(CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_CollectionLiteralPart)


def test_jtl_essentialocl_collectionliteralpart_constructor_exists():
    assert callable(JTL_essentialocl_CollectionLiteralPart.__init__)


def test_jtl_essentialocl_collectionliteralpart_constructor_args():
    sig = inspect.signature(JTL_essentialocl_CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_NumericLiteralExp)


def test_jtl_essentialocl_numericliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_NumericLiteralExp.__init__)


def test_jtl_essentialocl_numericliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_EnumLiteralExp)


def test_jtl_essentialocl_enumliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_EnumLiteralExp.__init__)


def test_jtl_essentialocl_enumliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_InvalidLiteralExp)


def test_jtl_essentialocl_invalidliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_InvalidLiteralExp.__init__)


def test_jtl_essentialocl_invalidliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_CollectionLiteralExp)


def test_jtl_essentialocl_collectionliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_CollectionLiteralExp.__init__)


def test_jtl_essentialocl_collectionliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_jtl_essentialocl_collectionliteralexp_has_kind():
    assert hasattr(JTL_essentialocl_CollectionLiteralExp, "kind")
    descriptor = None
    for klass in JTL_essentialocl_CollectionLiteralExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_jtl_imperativeocl_anonymoustupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_AnonymousTupleLiteralExp)


def test_jtl_imperativeocl_anonymoustupleliteralexp_constructor_exists():
    assert callable(JTL_imperativeocl_AnonymousTupleLiteralExp.__init__)


def test_jtl_imperativeocl_anonymoustupleliteralexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_AnonymousTupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_DictLiteralExp)


def test_jtl_imperativeocl_dictliteralexp_constructor_exists():
    assert callable(JTL_imperativeocl_DictLiteralExp.__init__)


def test_jtl_imperativeocl_dictliteralexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_template_templateexp_is_not_abstract():
    assert not inspect.isabstract(JTL_template_TemplateExp)


def test_jtl_template_templateexp_constructor_exists():
    assert callable(JTL_template_TemplateExp.__init__)


def test_jtl_template_templateexp_constructor_args():
    sig = inspect.signature(JTL_template_TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_PrimitiveLiteralExp)


def test_jtl_essentialocl_primitiveliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_PrimitiveLiteralExp.__init__)


def test_jtl_essentialocl_primitiveliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(OpaqueExpression)


def test_opaqueexpression_constructor_exists():
    assert callable(OpaqueExpression.__init__)


def test_opaqueexpression_constructor_args():
    sig = inspect.signature(OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_expressioninocl_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_ExpressionInOcl)


def test_jtl_essentialocl_expressioninocl_constructor_exists():
    assert callable(JTL_essentialocl_ExpressionInOcl.__init__)


def test_jtl_essentialocl_expressioninocl_constructor_args():
    sig = inspect.signature(JTL_essentialocl_ExpressionInOcl.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_NullLiteralExp)


def test_jtl_essentialocl_nullliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_NullLiteralExp.__init__)


def test_jtl_essentialocl_nullliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_TupleLiteralExp)


def test_jtl_essentialocl_tupleliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_TupleLiteralExp.__init__)


def test_jtl_essentialocl_tupleliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_collectionrange_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_CollectionRange)


def test_jtl_essentialocl_collectionrange_constructor_exists():
    assert callable(JTL_essentialocl_CollectionRange.__init__)


def test_jtl_essentialocl_collectionrange_constructor_args():
    sig = inspect.signature(JTL_essentialocl_CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_collectionitem_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_CollectionItem)


def test_jtl_essentialocl_collectionitem_constructor_exists():
    assert callable(JTL_essentialocl_CollectionItem.__init__)


def test_jtl_essentialocl_collectionitem_constructor_args():
    sig = inspect.signature(JTL_essentialocl_CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(FeaturePropertyCall)


def test_featurepropertycall_constructor_exists():
    assert callable(FeaturePropertyCall.__init__)


def test_featurepropertycall_constructor_args():
    sig = inspect.signature(FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_PropertyCallExp)


def test_jtl_essentialocl_propertycallexp_constructor_exists():
    assert callable(JTL_essentialocl_PropertyCallExp.__init__)


def test_jtl_essentialocl_propertycallexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_PropertyCallExp.__init__)
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



def test_jtl_essentialocl_variable_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_Variable)


def test_jtl_essentialocl_variable_constructor_exists():
    assert callable(JTL_essentialocl_Variable.__init__)


def test_jtl_essentialocl_variable_constructor_args():
    sig = inspect.signature(JTL_essentialocl_Variable.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_OperationCallExp)


def test_jtl_essentialocl_operationcallexp_constructor_exists():
    assert callable(JTL_essentialocl_OperationCallExp.__init__)


def test_jtl_essentialocl_operationcallexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_StringLiteralExp)


def test_jtl_essentialocl_stringliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_StringLiteralExp.__init__)


def test_jtl_essentialocl_stringliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_jtl_essentialocl_stringliteralexp_has_stringSymbol():
    assert hasattr(JTL_essentialocl_StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in JTL_essentialocl_StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_iterateexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_IterateExp)


def test_jtl_essentialocl_iterateexp_constructor_exists():
    assert callable(JTL_essentialocl_IterateExp.__init__)


def test_jtl_essentialocl_iterateexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_IteratorExp)


def test_jtl_essentialocl_iteratorexp_constructor_exists():
    assert callable(JTL_essentialocl_IteratorExp.__init__)


def test_jtl_essentialocl_iteratorexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(essentialocl_OclExpression)


def test_essentialocl_oclexpression_constructor_exists():
    assert callable(essentialocl_OclExpression.__init__)


def test_essentialocl_oclexpression_constructor_args():
    sig = inspect.signature(essentialocl_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_callexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl_CallExp)


def test_essentialocl_callexp_constructor_exists():
    assert callable(essentialocl_CallExp.__init__)


def test_essentialocl_callexp_constructor_args():
    sig = inspect.signature(essentialocl_CallExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_switchexp_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_SwitchExp)


def test_jtl_imperativeocl_switchexp_constructor_exists():
    assert callable(JTL_imperativeocl_SwitchExp.__init__)


def test_jtl_imperativeocl_switchexp_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_SwitchExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_loopexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_LoopExp)


def test_jtl_essentialocl_loopexp_constructor_exists():
    assert callable(JTL_essentialocl_LoopExp.__init__)


def test_jtl_essentialocl_loopexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_jtl_where_is_not_abstract():
    assert not inspect.isabstract(JTL_JTL_Where)


def test_jtl_jtl_where_constructor_exists():
    assert callable(JTL_JTL_Where.__init__)


def test_jtl_jtl_where_constructor_args():
    sig = inspect.signature(JTL_JTL_Where.__init__)
    params = list(sig.parameters.keys())



def test_jtl_jtl_when_is_not_abstract():
    assert not inspect.isabstract(JTL_JTL_When)


def test_jtl_jtl_when_constructor_exists():
    assert callable(JTL_JTL_When.__init__)


def test_jtl_jtl_when_constructor_args():
    sig = inspect.signature(JTL_JTL_When.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_letexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_LetExp)


def test_jtl_essentialocl_letexp_constructor_exists():
    assert callable(JTL_essentialocl_LetExp.__init__)


def test_jtl_essentialocl_letexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_typeexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_TypeExp)


def test_jtl_essentialocl_typeexp_constructor_exists():
    assert callable(JTL_essentialocl_TypeExp.__init__)


def test_jtl_essentialocl_typeexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_imperativeocl_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(JTL_imperativeocl_ImperativeExpression)


def test_jtl_imperativeocl_imperativeexpression_constructor_exists():
    assert callable(JTL_imperativeocl_ImperativeExpression.__init__)


def test_jtl_imperativeocl_imperativeexpression_constructor_args():
    sig = inspect.signature(JTL_imperativeocl_ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_variableexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_VariableExp)


def test_jtl_essentialocl_variableexp_constructor_exists():
    assert callable(JTL_essentialocl_VariableExp.__init__)


def test_jtl_essentialocl_variableexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_literalexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_LiteralExp)


def test_jtl_essentialocl_literalexp_constructor_exists():
    assert callable(JTL_essentialocl_LiteralExp.__init__)


def test_jtl_essentialocl_literalexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_callexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_CallExp)


def test_jtl_essentialocl_callexp_constructor_exists():
    assert callable(JTL_essentialocl_CallExp.__init__)


def test_jtl_essentialocl_callexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_CallExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_jtl_predicate_is_not_abstract():
    assert not inspect.isabstract(JTL_JTL_Predicate)


def test_jtl_jtl_predicate_constructor_exists():
    assert callable(JTL_JTL_Predicate.__init__)


def test_jtl_jtl_predicate_constructor_args():
    sig = inspect.signature(JTL_JTL_Predicate.__init__)
    params = list(sig.parameters.keys())



def test_templateexp_is_not_abstract():
    assert not inspect.isabstract(TemplateExp)


def test_templateexp_constructor_exists():
    assert callable(TemplateExp.__init__)


def test_templateexp_constructor_args():
    sig = inspect.signature(TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_template_collectiontemplateexp_is_not_abstract():
    assert not inspect.isabstract(JTL_template_CollectionTemplateExp)


def test_jtl_template_collectiontemplateexp_constructor_exists():
    assert callable(JTL_template_CollectionTemplateExp.__init__)


def test_jtl_template_collectiontemplateexp_constructor_args():
    sig = inspect.signature(JTL_template_CollectionTemplateExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_jtl_template_collectiontemplateexp_has_kind():
    assert hasattr(JTL_template_CollectionTemplateExp, "kind")
    descriptor = None
    for klass in JTL_template_CollectionTemplateExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_jtl_template_objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(JTL_template_ObjectTemplateExp)


def test_jtl_template_objecttemplateexp_constructor_exists():
    assert callable(JTL_template_ObjectTemplateExp.__init__)


def test_jtl_template_objecttemplateexp_constructor_args():
    sig = inspect.signature(JTL_template_ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())
    assert "referredClass" in params, "Missing parameter 'referredClass'"

def test_jtl_template_objecttemplateexp_has_referredClass():
    assert hasattr(JTL_template_ObjectTemplateExp, "referredClass")
    descriptor = None
    for klass in JTL_template_ObjectTemplateExp.__mro__:
        if "referredClass" in klass.__dict__:
            descriptor = klass.__dict__["referredClass"]
            break
    assert isinstance(descriptor, property)



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_jtl_jtl_pattern_is_not_abstract():
    assert not inspect.isabstract(JTL_JTL_Pattern)


def test_jtl_jtl_pattern_constructor_exists():
    assert callable(JTL_JTL_Pattern.__init__)


def test_jtl_jtl_pattern_constructor_args():
    sig = inspect.signature(JTL_JTL_Pattern.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_ifexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_IfExp)


def test_jtl_essentialocl_ifexp_constructor_exists():
    assert callable(JTL_essentialocl_IfExp.__init__)


def test_jtl_essentialocl_ifexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl_essentialocl_integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_IntegerLiteralExp)


def test_jtl_essentialocl_integerliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_IntegerLiteralExp.__init__)


def test_jtl_essentialocl_integerliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_jtl_essentialocl_integerliteralexp_has_integerSymbol():
    assert hasattr(JTL_essentialocl_IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in JTL_essentialocl_IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_jtl_essentialocl_realliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_RealLiteralExp)


def test_jtl_essentialocl_realliteralexp_constructor_exists():
    assert callable(JTL_essentialocl_RealLiteralExp.__init__)


def test_jtl_essentialocl_realliteralexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_jtl_essentialocl_realliteralexp_has_realSymbol():
    assert hasattr(JTL_essentialocl_RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in JTL_essentialocl_RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_jtl_essentialocl_unlimitednaturalexp_is_not_abstract():
    assert not inspect.isabstract(JTL_essentialocl_UnlimitedNaturalExp)


def test_jtl_essentialocl_unlimitednaturalexp_constructor_exists():
    assert callable(JTL_essentialocl_UnlimitedNaturalExp.__init__)


def test_jtl_essentialocl_unlimitednaturalexp_constructor_args():
    sig = inspect.signature(JTL_essentialocl_UnlimitedNaturalExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_jtl_essentialocl_unlimitednaturalexp_has_symbol():
    assert hasattr(JTL_essentialocl_UnlimitedNaturalExp, "symbol")
    descriptor = None
    for klass in JTL_essentialocl_UnlimitedNaturalExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
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

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "Set",
        "OrderedSet",
        "Bag",
        "Sequence",
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
TryExp_strategy = st.builds(
    TryExp,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
JTL_essentialocl_OclExpression_strategy = st.builds(
    JTL_essentialocl_OclExpression,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
JTL_essentialocl_BooleanLiteralExp_strategy = st.builds(
    JTL_essentialocl_BooleanLiteralExp,
    booleanSymbol=
        st.booleans()
)
Relation_strategy = st.builds(
    Relation,
)
Model_strategy = st.builds(
    Model,
)
emof_Package_strategy = st.builds(
    emof_Package,
)
emof_Class_strategy = st.builds(
    emof_Class,
)
JTL_JTL_Transformation_strategy = st.builds(
    JTL_JTL_Transformation,
)
Extent_strategy = st.builds(
    Extent,
)
JTL_emof_URIExtent_strategy = st.builds(
    JTL_emof_URIExtent,
)
Pattern_strategy = st.builds(
    Pattern,
)
Variable_strategy = st.builds(
    Variable,
)
When_strategy = st.builds(
    When,
)
Where_strategy = st.builds(
    Where,
)
Domain_strategy = st.builds(
    Domain,
)
Transformation_strategy = st.builds(
    Transformation,
)
JTL_emof_MultiplicityElement_strategy = st.builds(
    JTL_emof_MultiplicityElement,
    isUnique=
        safe_text,
    upper=
        safe_text,
    isOrdered=
        safe_text,
    lower=
        st.integers()
)
Parameter_strategy = st.builds(
    Parameter,
)
emof_TypedElement_strategy = st.builds(
    emof_TypedElement,
)
emof_MultiplicityElement_strategy = st.builds(
    emof_MultiplicityElement,
)
JTL_emof_Operation_strategy = st.builds(
    JTL_emof_Operation,
)
JTL_emof_Object_strategy = st.builds(
    JTL_emof_Object,
)
JTL_emof_Property_strategy = st.builds(
    JTL_emof_Property,
    isDerived=
        st.booleans(),
    isId=
        st.booleans(),
    isReadOnly=
        st.booleans(),
    isComposite=
        st.booleans(),
    default=
        safe_text
)
Enumeration_strategy = st.builds(
    Enumeration,
)
JTL_emof_Parameter_strategy = st.builds(
    JTL_emof_Parameter,
)
Package_strategy = st.builds(
    Package,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
JTL_JTL_Model_strategy = st.builds(
    JTL_JTL_Model,
    usedPackage=
        safe_text
)
JTL_emof_EnumerationLiteral_strategy = st.builds(
    JTL_emof_EnumerationLiteral,
)
JTL_JTL_Relation_strategy = st.builds(
    JTL_JTL_Relation,
    isTopLevel=
        st.booleans()
)
JTL_JTL_Domain_strategy = st.builds(
    JTL_JTL_Domain,
    isEnforceable=
        st.booleans(),
    isCheckable=
        st.booleans()
)
JTL_emof_TypedElement_strategy = st.builds(
    JTL_emof_TypedElement,
    type=
        safe_text
)
JTL_emof_Type_strategy = st.builds(
    JTL_emof_Type,
)
JTL_emof_Package_strategy = st.builds(
    JTL_emof_Package,
    uri=
        safe_text
)
Property_strategy = st.builds(
    Property,
)
Type_strategy = st.builds(
    Type,
)
JTL_emof_Class_strategy = st.builds(
    JTL_emof_Class,
    isAbstract=
        st.booleans()
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
JTL_emof_PrimitiveType_strategy = st.builds(
    JTL_emof_PrimitiveType,
)
JTL_emof_Enumeration_strategy = st.builds(
    JTL_emof_Enumeration,
)
Element_strategy = st.builds(
    Element,
)
JTL_emof_NamedElement_strategy = st.builds(
    JTL_emof_NamedElement,
    name=
        safe_text
)
JTL_emof_Comment_strategy = st.builds(
    JTL_emof_Comment,
)
JTL_emof_Tag_strategy = st.builds(
    JTL_emof_Tag,
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
JTL_emof_Extent_strategy = st.builds(
    JTL_emof_Extent,
)
JTL_emof_Element_strategy = st.builds(
    JTL_emof_Element,
)
JTL_emof_DataType_strategy = st.builds(
    JTL_emof_DataType,
)
Class_strategy = st.builds(
    Class,
)
Operation_strategy = st.builds(
    Operation,
)
JTL_imperativeocl_AnonymousTupleLiteralPart_strategy = st.builds(
    JTL_imperativeocl_AnonymousTupleLiteralPart,
)
AnonymousTupleLiteralPart_strategy = st.builds(
    AnonymousTupleLiteralPart,
)
JTL_imperativeocl_AnonymousTupleType_strategy = st.builds(
    JTL_imperativeocl_AnonymousTupleType,
)
JTL_imperativeocl_TemplateParameterType_strategy = st.builds(
    JTL_imperativeocl_TemplateParameterType,
    specification=
        safe_text
)
JTL_imperativeocl_DictLiteralPart_strategy = st.builds(
    JTL_imperativeocl_DictLiteralPart,
)
DictLiteralPart_strategy = st.builds(
    DictLiteralPart,
)
essentialocl_LoopExp_strategy = st.builds(
    essentialocl_LoopExp,
)
LogExp_strategy = st.builds(
    LogExp,
)
JTL_imperativeocl_Typedef_strategy = st.builds(
    JTL_imperativeocl_Typedef,
)
AltExp_strategy = st.builds(
    AltExp,
)
imperativeocl_ImperativeExpression_strategy = st.builds(
    imperativeocl_ImperativeExpression,
)
JTL_imperativeocl_ImperativeLoopExp_strategy = st.builds(
    JTL_imperativeocl_ImperativeLoopExp,
)
AssignExp_strategy = st.builds(
    AssignExp,
)
PropertyTemplateItem_strategy = st.builds(
    PropertyTemplateItem,
)
ImperativeExpression_strategy = st.builds(
    ImperativeExpression,
)
JTL_imperativeocl_ContinueExp_strategy = st.builds(
    JTL_imperativeocl_ContinueExp,
)
JTL_imperativeocl_RaiseExp_strategy = st.builds(
    JTL_imperativeocl_RaiseExp,
)
JTL_imperativeocl_BlockExp_strategy = st.builds(
    JTL_imperativeocl_BlockExp,
)
JTL_imperativeocl_AltExp_strategy = st.builds(
    JTL_imperativeocl_AltExp,
)
JTL_imperativeocl_UnlinkExp_strategy = st.builds(
    JTL_imperativeocl_UnlinkExp,
)
JTL_imperativeocl_WhileExp_strategy = st.builds(
    JTL_imperativeocl_WhileExp,
)
JTL_imperativeocl_UnpackExp_strategy = st.builds(
    JTL_imperativeocl_UnpackExp,
)
JTL_imperativeocl_InstantiationExp_strategy = st.builds(
    JTL_imperativeocl_InstantiationExp,
)
JTL_imperativeocl_BreakExp_strategy = st.builds(
    JTL_imperativeocl_BreakExp,
)
JTL_imperativeocl_TryExp_strategy = st.builds(
    JTL_imperativeocl_TryExp,
)
JTL_imperativeocl_VariableInitExp_strategy = st.builds(
    JTL_imperativeocl_VariableInitExp,
    withResult=
        st.booleans()
)
JTL_imperativeocl_TupleExp_strategy = st.builds(
    JTL_imperativeocl_TupleExp,
)
JTL_imperativeocl_LogExp_strategy = st.builds(
    JTL_imperativeocl_LogExp,
    text=
        safe_text,
    level=
        st.integers()
)
JTL_imperativeocl_ComputeExp_strategy = st.builds(
    JTL_imperativeocl_ComputeExp,
)
JTL_imperativeocl_AssertExp_strategy = st.builds(
    JTL_imperativeocl_AssertExp,
    severity=
        safe_text
)
JTL_imperativeocl_ReturnExp_strategy = st.builds(
    JTL_imperativeocl_ReturnExp,
)
JTL_imperativeocl_AssignExp_strategy = st.builds(
    JTL_imperativeocl_AssignExp,
    isReset=
        st.booleans()
)
ImperativeLoopExp_strategy = st.builds(
    ImperativeLoopExp,
)
JTL_imperativeocl_CollectorExp_strategy = st.builds(
    JTL_imperativeocl_CollectorExp,
)
JTL_imperativeocl_ForExp_strategy = st.builds(
    JTL_imperativeocl_ForExp,
)
JTL_imperativeocl_ImperativeIterateExp_strategy = st.builds(
    JTL_imperativeocl_ImperativeIterateExp,
)
ObjectTemplateExp_strategy = st.builds(
    ObjectTemplateExp,
)
JTL_template_PropertyTemplateItem_strategy = st.builds(
    JTL_template_PropertyTemplateItem,
)
JTL_essentialocl_CollectionType_strategy = st.builds(
    JTL_essentialocl_CollectionType,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
JTL_imperativeocl_DictionaryType_strategy = st.builds(
    JTL_imperativeocl_DictionaryType,
)
JTL_imperativeocl_ListType_strategy = st.builds(
    JTL_imperativeocl_ListType,
)
JTL_essentialocl_BagType_strategy = st.builds(
    JTL_essentialocl_BagType,
)
TupleLiteralExp_strategy = st.builds(
    TupleLiteralExp,
)
JTL_essentialocl_TupleLiteralPart_strategy = st.builds(
    JTL_essentialocl_TupleLiteralPart,
)
CallExp_strategy = st.builds(
    CallExp,
)
JTL_essentialocl_FeaturePropertyCall_strategy = st.builds(
    JTL_essentialocl_FeaturePropertyCall,
)
JTL_essentialocl_OpaqueExpression_strategy = st.builds(
    JTL_essentialocl_OpaqueExpression,
)
emof_Type_strategy = st.builds(
    emof_Type,
)
JTL_essentialocl_AnyType_strategy = st.builds(
    JTL_essentialocl_AnyType,
)
JTL_essentialocl_VoidType_strategy = st.builds(
    JTL_essentialocl_VoidType,
)
emof_DataType_strategy = st.builds(
    emof_DataType,
)
JTL_essentialocl_TupleType_strategy = st.builds(
    JTL_essentialocl_TupleType,
)
JTL_essentialocl_SetType_strategy = st.builds(
    JTL_essentialocl_SetType,
)
JTL_essentialocl_SequenceType_strategy = st.builds(
    JTL_essentialocl_SequenceType,
)
JTL_essentialocl_OrderedSetType_strategy = st.builds(
    JTL_essentialocl_OrderedSetType,
)
JTL_essentialocl_InvalidType_strategy = st.builds(
    JTL_essentialocl_InvalidType,
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
JTL_essentialocl_CollectionLiteralPart_strategy = st.builds(
    JTL_essentialocl_CollectionLiteralPart,
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
JTL_essentialocl_NumericLiteralExp_strategy = st.builds(
    JTL_essentialocl_NumericLiteralExp,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
JTL_essentialocl_EnumLiteralExp_strategy = st.builds(
    JTL_essentialocl_EnumLiteralExp,
)
JTL_essentialocl_InvalidLiteralExp_strategy = st.builds(
    JTL_essentialocl_InvalidLiteralExp,
)
JTL_essentialocl_CollectionLiteralExp_strategy = st.builds(
    JTL_essentialocl_CollectionLiteralExp,
    kind=
        safe_text
)
JTL_imperativeocl_AnonymousTupleLiteralExp_strategy = st.builds(
    JTL_imperativeocl_AnonymousTupleLiteralExp,
)
JTL_imperativeocl_DictLiteralExp_strategy = st.builds(
    JTL_imperativeocl_DictLiteralExp,
)
JTL_template_TemplateExp_strategy = st.builds(
    JTL_template_TemplateExp,
)
JTL_essentialocl_PrimitiveLiteralExp_strategy = st.builds(
    JTL_essentialocl_PrimitiveLiteralExp,
)
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
JTL_essentialocl_ExpressionInOcl_strategy = st.builds(
    JTL_essentialocl_ExpressionInOcl,
)
JTL_essentialocl_NullLiteralExp_strategy = st.builds(
    JTL_essentialocl_NullLiteralExp,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
JTL_essentialocl_TupleLiteralExp_strategy = st.builds(
    JTL_essentialocl_TupleLiteralExp,
)
JTL_essentialocl_CollectionRange_strategy = st.builds(
    JTL_essentialocl_CollectionRange,
)
JTL_essentialocl_CollectionItem_strategy = st.builds(
    JTL_essentialocl_CollectionItem,
)
FeaturePropertyCall_strategy = st.builds(
    FeaturePropertyCall,
)
JTL_essentialocl_PropertyCallExp_strategy = st.builds(
    JTL_essentialocl_PropertyCallExp,
)
ComputeExp_strategy = st.builds(
    ComputeExp,
)
LetExp_strategy = st.builds(
    LetExp,
)
JTL_essentialocl_Variable_strategy = st.builds(
    JTL_essentialocl_Variable,
)
JTL_essentialocl_OperationCallExp_strategy = st.builds(
    JTL_essentialocl_OperationCallExp,
)
JTL_essentialocl_StringLiteralExp_strategy = st.builds(
    JTL_essentialocl_StringLiteralExp,
    stringSymbol=
        safe_text
)
LoopExp_strategy = st.builds(
    LoopExp,
)
JTL_essentialocl_IterateExp_strategy = st.builds(
    JTL_essentialocl_IterateExp,
)
JTL_essentialocl_IteratorExp_strategy = st.builds(
    JTL_essentialocl_IteratorExp,
)
essentialocl_OclExpression_strategy = st.builds(
    essentialocl_OclExpression,
)
essentialocl_CallExp_strategy = st.builds(
    essentialocl_CallExp,
)
JTL_imperativeocl_SwitchExp_strategy = st.builds(
    JTL_imperativeocl_SwitchExp,
)
JTL_essentialocl_LoopExp_strategy = st.builds(
    JTL_essentialocl_LoopExp,
)
JTL_JTL_Where_strategy = st.builds(
    JTL_JTL_Where,
)
JTL_JTL_When_strategy = st.builds(
    JTL_JTL_When,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
JTL_essentialocl_LetExp_strategy = st.builds(
    JTL_essentialocl_LetExp,
)
JTL_essentialocl_TypeExp_strategy = st.builds(
    JTL_essentialocl_TypeExp,
)
JTL_imperativeocl_ImperativeExpression_strategy = st.builds(
    JTL_imperativeocl_ImperativeExpression,
)
JTL_essentialocl_VariableExp_strategy = st.builds(
    JTL_essentialocl_VariableExp,
)
JTL_essentialocl_LiteralExp_strategy = st.builds(
    JTL_essentialocl_LiteralExp,
)
JTL_essentialocl_CallExp_strategy = st.builds(
    JTL_essentialocl_CallExp,
)
JTL_JTL_Predicate_strategy = st.builds(
    JTL_JTL_Predicate,
)
TemplateExp_strategy = st.builds(
    TemplateExp,
)
JTL_template_CollectionTemplateExp_strategy = st.builds(
    JTL_template_CollectionTemplateExp,
    kind=
        safe_text
)
JTL_template_ObjectTemplateExp_strategy = st.builds(
    JTL_template_ObjectTemplateExp,
    referredClass=
        safe_text
)
Predicate_strategy = st.builds(
    Predicate,
)
JTL_JTL_Pattern_strategy = st.builds(
    JTL_JTL_Pattern,
)
JTL_essentialocl_IfExp_strategy = st.builds(
    JTL_essentialocl_IfExp,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
JTL_essentialocl_IntegerLiteralExp_strategy = st.builds(
    JTL_essentialocl_IntegerLiteralExp,
    integerSymbol=
        st.integers()
)
JTL_essentialocl_RealLiteralExp_strategy = st.builds(
    JTL_essentialocl_RealLiteralExp,
    realSymbol=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
JTL_essentialocl_UnlimitedNaturalExp_strategy = st.builds(
    JTL_essentialocl_UnlimitedNaturalExp,
    symbol=
        safe_text
)

@given(instance=TryExp_strategy)
@settings(max_examples=50)
def test_tryexp_instantiation(instance):
    assert isinstance(instance, TryExp)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=JTL_essentialocl_OclExpression_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_oclexpression_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_OclExpression)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=JTL_essentialocl_BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_booleanliteralexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_BooleanLiteralExp)



@given(instance=JTL_essentialocl_BooleanLiteralExp_strategy)
def test_jtl_essentialocl_booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=Model_strategy)
@settings(max_examples=50)
def test_model_instantiation(instance):
    assert isinstance(instance, Model)

@given(instance=emof_Package_strategy)
@settings(max_examples=50)
def test_emof_package_instantiation(instance):
    assert isinstance(instance, emof_Package)

@given(instance=emof_Class_strategy)
@settings(max_examples=50)
def test_emof_class_instantiation(instance):
    assert isinstance(instance, emof_Class)

@given(instance=JTL_JTL_Transformation_strategy)
@settings(max_examples=50)
def test_jtl_jtl_transformation_instantiation(instance):
    assert isinstance(instance, JTL_JTL_Transformation)

@given(instance=Extent_strategy)
@settings(max_examples=50)
def test_extent_instantiation(instance):
    assert isinstance(instance, Extent)

@given(instance=JTL_emof_URIExtent_strategy)
@settings(max_examples=50)
def test_jtl_emof_uriextent_instantiation(instance):
    assert isinstance(instance, JTL_emof_URIExtent)

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=When_strategy)
@settings(max_examples=50)
def test_when_instantiation(instance):
    assert isinstance(instance, When)

@given(instance=Where_strategy)
@settings(max_examples=50)
def test_where_instantiation(instance):
    assert isinstance(instance, Where)

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=Transformation_strategy)
@settings(max_examples=50)
def test_transformation_instantiation(instance):
    assert isinstance(instance, Transformation)

@given(instance=JTL_emof_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_jtl_emof_multiplicityelement_instantiation(instance):
    assert isinstance(instance, JTL_emof_MultiplicityElement)



@given(instance=JTL_emof_MultiplicityElement_strategy)
def test_jtl_emof_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=JTL_emof_MultiplicityElement_strategy)
def test_jtl_emof_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=JTL_emof_MultiplicityElement_strategy)
def test_jtl_emof_multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=JTL_emof_MultiplicityElement_strategy)
def test_jtl_emof_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=emof_TypedElement_strategy)
@settings(max_examples=50)
def test_emof_typedelement_instantiation(instance):
    assert isinstance(instance, emof_TypedElement)

@given(instance=emof_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_emof_multiplicityelement_instantiation(instance):
    assert isinstance(instance, emof_MultiplicityElement)

@given(instance=JTL_emof_Operation_strategy)
@settings(max_examples=50)
def test_jtl_emof_operation_instantiation(instance):
    assert isinstance(instance, JTL_emof_Operation)

@given(instance=JTL_emof_Object_strategy)
@settings(max_examples=50)
def test_jtl_emof_object_instantiation(instance):
    assert isinstance(instance, JTL_emof_Object)

@given(instance=JTL_emof_Property_strategy)
@settings(max_examples=50)
def test_jtl_emof_property_instantiation(instance):
    assert isinstance(instance, JTL_emof_Property)



@given(instance=JTL_emof_Property_strategy)
def test_jtl_emof_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=JTL_emof_Property_strategy)
def test_jtl_emof_property_isId_setter(instance):
    original = instance.isId
    instance.isId = original
    assert instance.isId == original



@given(instance=JTL_emof_Property_strategy)
def test_jtl_emof_property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original



@given(instance=JTL_emof_Property_strategy)
def test_jtl_emof_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=JTL_emof_Property_strategy)
def test_jtl_emof_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=Enumeration_strategy)
@settings(max_examples=50)
def test_enumeration_instantiation(instance):
    assert isinstance(instance, Enumeration)

@given(instance=JTL_emof_Parameter_strategy)
@settings(max_examples=50)
def test_jtl_emof_parameter_instantiation(instance):
    assert isinstance(instance, JTL_emof_Parameter)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=JTL_JTL_Model_strategy)
@settings(max_examples=50)
def test_jtl_jtl_model_instantiation(instance):
    assert isinstance(instance, JTL_JTL_Model)



@given(instance=JTL_JTL_Model_strategy)
def test_jtl_jtl_model_usedPackage_setter(instance):
    original = instance.usedPackage
    instance.usedPackage = original
    assert instance.usedPackage == original

@given(instance=JTL_emof_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_jtl_emof_enumerationliteral_instantiation(instance):
    assert isinstance(instance, JTL_emof_EnumerationLiteral)

@given(instance=JTL_JTL_Relation_strategy)
@settings(max_examples=50)
def test_jtl_jtl_relation_instantiation(instance):
    assert isinstance(instance, JTL_JTL_Relation)



@given(instance=JTL_JTL_Relation_strategy)
def test_jtl_jtl_relation_isTopLevel_setter(instance):
    original = instance.isTopLevel
    instance.isTopLevel = original
    assert instance.isTopLevel == original

@given(instance=JTL_JTL_Domain_strategy)
@settings(max_examples=50)
def test_jtl_jtl_domain_instantiation(instance):
    assert isinstance(instance, JTL_JTL_Domain)



@given(instance=JTL_JTL_Domain_strategy)
def test_jtl_jtl_domain_isEnforceable_setter(instance):
    original = instance.isEnforceable
    instance.isEnforceable = original
    assert instance.isEnforceable == original



@given(instance=JTL_JTL_Domain_strategy)
def test_jtl_jtl_domain_isCheckable_setter(instance):
    original = instance.isCheckable
    instance.isCheckable = original
    assert instance.isCheckable == original

@given(instance=JTL_emof_TypedElement_strategy)
@settings(max_examples=50)
def test_jtl_emof_typedelement_instantiation(instance):
    assert isinstance(instance, JTL_emof_TypedElement)



@given(instance=JTL_emof_TypedElement_strategy)
def test_jtl_emof_typedelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=JTL_emof_Type_strategy)
@settings(max_examples=50)
def test_jtl_emof_type_instantiation(instance):
    assert isinstance(instance, JTL_emof_Type)

@given(instance=JTL_emof_Package_strategy)
@settings(max_examples=50)
def test_jtl_emof_package_instantiation(instance):
    assert isinstance(instance, JTL_emof_Package)



@given(instance=JTL_emof_Package_strategy)
def test_jtl_emof_package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=JTL_emof_Class_strategy)
@settings(max_examples=50)
def test_jtl_emof_class_instantiation(instance):
    assert isinstance(instance, JTL_emof_Class)



@given(instance=JTL_emof_Class_strategy)
def test_jtl_emof_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=JTL_emof_PrimitiveType_strategy)
@settings(max_examples=50)
def test_jtl_emof_primitivetype_instantiation(instance):
    assert isinstance(instance, JTL_emof_PrimitiveType)

@given(instance=JTL_emof_Enumeration_strategy)
@settings(max_examples=50)
def test_jtl_emof_enumeration_instantiation(instance):
    assert isinstance(instance, JTL_emof_Enumeration)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=JTL_emof_NamedElement_strategy)
@settings(max_examples=50)
def test_jtl_emof_namedelement_instantiation(instance):
    assert isinstance(instance, JTL_emof_NamedElement)



@given(instance=JTL_emof_NamedElement_strategy)
def test_jtl_emof_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JTL_emof_Comment_strategy)
@settings(max_examples=50)
def test_jtl_emof_comment_instantiation(instance):
    assert isinstance(instance, JTL_emof_Comment)

@given(instance=JTL_emof_Tag_strategy)
@settings(max_examples=50)
def test_jtl_emof_tag_instantiation(instance):
    assert isinstance(instance, JTL_emof_Tag)



@given(instance=JTL_emof_Tag_strategy)
def test_jtl_emof_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=JTL_emof_Tag_strategy)
def test_jtl_emof_tag_value_setter(instance):
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

@given(instance=JTL_emof_Extent_strategy)
@settings(max_examples=50)
def test_jtl_emof_extent_instantiation(instance):
    assert isinstance(instance, JTL_emof_Extent)

@given(instance=JTL_emof_Element_strategy)
@settings(max_examples=50)
def test_jtl_emof_element_instantiation(instance):
    assert isinstance(instance, JTL_emof_Element)

@given(instance=JTL_emof_DataType_strategy)
@settings(max_examples=50)
def test_jtl_emof_datatype_instantiation(instance):
    assert isinstance(instance, JTL_emof_DataType)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=JTL_imperativeocl_AnonymousTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_anonymoustupleliteralpart_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_AnonymousTupleLiteralPart)

@given(instance=AnonymousTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_anonymoustupleliteralpart_instantiation(instance):
    assert isinstance(instance, AnonymousTupleLiteralPart)

@given(instance=JTL_imperativeocl_AnonymousTupleType_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_anonymoustupletype_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_AnonymousTupleType)

@given(instance=JTL_imperativeocl_TemplateParameterType_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_templateparametertype_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_TemplateParameterType)



@given(instance=JTL_imperativeocl_TemplateParameterType_strategy)
def test_jtl_imperativeocl_templateparametertype_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=JTL_imperativeocl_DictLiteralPart_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_dictliteralpart_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_DictLiteralPart)

@given(instance=DictLiteralPart_strategy)
@settings(max_examples=50)
def test_dictliteralpart_instantiation(instance):
    assert isinstance(instance, DictLiteralPart)

@given(instance=essentialocl_LoopExp_strategy)
@settings(max_examples=50)
def test_essentialocl_loopexp_instantiation(instance):
    assert isinstance(instance, essentialocl_LoopExp)

@given(instance=LogExp_strategy)
@settings(max_examples=50)
def test_logexp_instantiation(instance):
    assert isinstance(instance, LogExp)

@given(instance=JTL_imperativeocl_Typedef_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_typedef_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_Typedef)

@given(instance=AltExp_strategy)
@settings(max_examples=50)
def test_altexp_instantiation(instance):
    assert isinstance(instance, AltExp)

@given(instance=imperativeocl_ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeocl_imperativeexpression_instantiation(instance):
    assert isinstance(instance, imperativeocl_ImperativeExpression)

@given(instance=JTL_imperativeocl_ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_ImperativeLoopExp)

@given(instance=AssignExp_strategy)
@settings(max_examples=50)
def test_assignexp_instantiation(instance):
    assert isinstance(instance, AssignExp)

@given(instance=PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_propertytemplateitem_instantiation(instance):
    assert isinstance(instance, PropertyTemplateItem)

@given(instance=ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeExpression)

@given(instance=JTL_imperativeocl_ContinueExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_continueexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_ContinueExp)

@given(instance=JTL_imperativeocl_RaiseExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_raiseexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_RaiseExp)

@given(instance=JTL_imperativeocl_BlockExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_blockexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_BlockExp)

@given(instance=JTL_imperativeocl_AltExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_altexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_AltExp)

@given(instance=JTL_imperativeocl_UnlinkExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_unlinkexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_UnlinkExp)

@given(instance=JTL_imperativeocl_WhileExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_whileexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_WhileExp)

@given(instance=JTL_imperativeocl_UnpackExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_unpackexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_UnpackExp)

@given(instance=JTL_imperativeocl_InstantiationExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_instantiationexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_InstantiationExp)

@given(instance=JTL_imperativeocl_BreakExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_breakexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_BreakExp)

@given(instance=JTL_imperativeocl_TryExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_tryexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_TryExp)

@given(instance=JTL_imperativeocl_VariableInitExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_variableinitexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_VariableInitExp)



@given(instance=JTL_imperativeocl_VariableInitExp_strategy)
def test_jtl_imperativeocl_variableinitexp_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=JTL_imperativeocl_TupleExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_tupleexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_TupleExp)

@given(instance=JTL_imperativeocl_LogExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_logexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_LogExp)



@given(instance=JTL_imperativeocl_LogExp_strategy)
def test_jtl_imperativeocl_logexp_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=JTL_imperativeocl_LogExp_strategy)
def test_jtl_imperativeocl_logexp_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=JTL_imperativeocl_ComputeExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_computeexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_ComputeExp)

@given(instance=JTL_imperativeocl_AssertExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_assertexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_AssertExp)



@given(instance=JTL_imperativeocl_AssertExp_strategy)
def test_jtl_imperativeocl_assertexp_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=JTL_imperativeocl_ReturnExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_returnexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_ReturnExp)

@given(instance=JTL_imperativeocl_AssignExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_assignexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_AssignExp)



@given(instance=JTL_imperativeocl_AssignExp_strategy)
def test_jtl_imperativeocl_assignexp_isReset_setter(instance):
    original = instance.isReset
    instance.isReset = original
    assert instance.isReset == original

@given(instance=ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExp)

@given(instance=JTL_imperativeocl_CollectorExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_collectorexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_CollectorExp)

@given(instance=JTL_imperativeocl_ForExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_forexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_ForExp)

@given(instance=JTL_imperativeocl_ImperativeIterateExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_imperativeiterateexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_ImperativeIterateExp)

@given(instance=ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_objecttemplateexp_instantiation(instance):
    assert isinstance(instance, ObjectTemplateExp)

@given(instance=JTL_template_PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_jtl_template_propertytemplateitem_instantiation(instance):
    assert isinstance(instance, JTL_template_PropertyTemplateItem)

@given(instance=JTL_essentialocl_CollectionType_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_collectiontype_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_CollectionType)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=JTL_imperativeocl_DictionaryType_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_dictionarytype_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_DictionaryType)

@given(instance=JTL_imperativeocl_ListType_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_listtype_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_ListType)

@given(instance=JTL_essentialocl_BagType_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_bagtype_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_BagType)

@given(instance=TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, TupleLiteralExp)

@given(instance=JTL_essentialocl_TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_TupleLiteralPart)

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=JTL_essentialocl_FeaturePropertyCall_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_featurepropertycall_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_FeaturePropertyCall)

@given(instance=JTL_essentialocl_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_opaqueexpression_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_OpaqueExpression)

@given(instance=emof_Type_strategy)
@settings(max_examples=50)
def test_emof_type_instantiation(instance):
    assert isinstance(instance, emof_Type)

@given(instance=JTL_essentialocl_AnyType_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_anytype_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_AnyType)

@given(instance=JTL_essentialocl_VoidType_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_voidtype_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_VoidType)

@given(instance=emof_DataType_strategy)
@settings(max_examples=50)
def test_emof_datatype_instantiation(instance):
    assert isinstance(instance, emof_DataType)

@given(instance=JTL_essentialocl_TupleType_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_tupletype_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_TupleType)

@given(instance=JTL_essentialocl_SetType_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_settype_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_SetType)

@given(instance=JTL_essentialocl_SequenceType_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_sequencetype_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_SequenceType)

@given(instance=JTL_essentialocl_OrderedSetType_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_orderedsettype_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_OrderedSetType)

@given(instance=JTL_essentialocl_InvalidType_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_invalidtype_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_InvalidType)

@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)

@given(instance=JTL_essentialocl_CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_CollectionLiteralPart)

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=JTL_essentialocl_NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_numericliteralexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_NumericLiteralExp)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=JTL_essentialocl_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_enumliteralexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_EnumLiteralExp)

@given(instance=JTL_essentialocl_InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_invalidliteralexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_InvalidLiteralExp)

@given(instance=JTL_essentialocl_CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_CollectionLiteralExp)



@given(instance=JTL_essentialocl_CollectionLiteralExp_strategy)
def test_jtl_essentialocl_collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=JTL_imperativeocl_AnonymousTupleLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_anonymoustupleliteralexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_AnonymousTupleLiteralExp)

@given(instance=JTL_imperativeocl_DictLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_dictliteralexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_DictLiteralExp)

@given(instance=JTL_template_TemplateExp_strategy)
@settings(max_examples=50)
def test_jtl_template_templateexp_instantiation(instance):
    assert isinstance(instance, JTL_template_TemplateExp)

@given(instance=JTL_essentialocl_PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_PrimitiveLiteralExp)

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=JTL_essentialocl_ExpressionInOcl_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_expressioninocl_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_ExpressionInOcl)

@given(instance=JTL_essentialocl_NullLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_nullliteralexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_NullLiteralExp)

@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)

@given(instance=JTL_essentialocl_TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_TupleLiteralExp)

@given(instance=JTL_essentialocl_CollectionRange_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_collectionrange_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_CollectionRange)

@given(instance=JTL_essentialocl_CollectionItem_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_collectionitem_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_CollectionItem)

@given(instance=FeaturePropertyCall_strategy)
@settings(max_examples=50)
def test_featurepropertycall_instantiation(instance):
    assert isinstance(instance, FeaturePropertyCall)

@given(instance=JTL_essentialocl_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_propertycallexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_PropertyCallExp)

@given(instance=ComputeExp_strategy)
@settings(max_examples=50)
def test_computeexp_instantiation(instance):
    assert isinstance(instance, ComputeExp)

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=JTL_essentialocl_Variable_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_variable_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_Variable)

@given(instance=JTL_essentialocl_OperationCallExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_operationcallexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_OperationCallExp)

@given(instance=JTL_essentialocl_StringLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_stringliteralexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_StringLiteralExp)



@given(instance=JTL_essentialocl_StringLiteralExp_strategy)
def test_jtl_essentialocl_stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=JTL_essentialocl_IterateExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_iterateexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_IterateExp)

@given(instance=JTL_essentialocl_IteratorExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_iteratorexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_IteratorExp)

@given(instance=essentialocl_OclExpression_strategy)
@settings(max_examples=50)
def test_essentialocl_oclexpression_instantiation(instance):
    assert isinstance(instance, essentialocl_OclExpression)

@given(instance=essentialocl_CallExp_strategy)
@settings(max_examples=50)
def test_essentialocl_callexp_instantiation(instance):
    assert isinstance(instance, essentialocl_CallExp)

@given(instance=JTL_imperativeocl_SwitchExp_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_switchexp_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_SwitchExp)

@given(instance=JTL_essentialocl_LoopExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_loopexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_LoopExp)

@given(instance=JTL_JTL_Where_strategy)
@settings(max_examples=50)
def test_jtl_jtl_where_instantiation(instance):
    assert isinstance(instance, JTL_JTL_Where)

@given(instance=JTL_JTL_When_strategy)
@settings(max_examples=50)
def test_jtl_jtl_when_instantiation(instance):
    assert isinstance(instance, JTL_JTL_When)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=JTL_essentialocl_LetExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_letexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_LetExp)

@given(instance=JTL_essentialocl_TypeExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_typeexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_TypeExp)

@given(instance=JTL_imperativeocl_ImperativeExpression_strategy)
@settings(max_examples=50)
def test_jtl_imperativeocl_imperativeexpression_instantiation(instance):
    assert isinstance(instance, JTL_imperativeocl_ImperativeExpression)

@given(instance=JTL_essentialocl_VariableExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_variableexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_VariableExp)

@given(instance=JTL_essentialocl_LiteralExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_literalexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_LiteralExp)

@given(instance=JTL_essentialocl_CallExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_callexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_CallExp)

@given(instance=JTL_JTL_Predicate_strategy)
@settings(max_examples=50)
def test_jtl_jtl_predicate_instantiation(instance):
    assert isinstance(instance, JTL_JTL_Predicate)

@given(instance=TemplateExp_strategy)
@settings(max_examples=50)
def test_templateexp_instantiation(instance):
    assert isinstance(instance, TemplateExp)

@given(instance=JTL_template_CollectionTemplateExp_strategy)
@settings(max_examples=50)
def test_jtl_template_collectiontemplateexp_instantiation(instance):
    assert isinstance(instance, JTL_template_CollectionTemplateExp)



@given(instance=JTL_template_CollectionTemplateExp_strategy)
def test_jtl_template_collectiontemplateexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=JTL_template_ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_jtl_template_objecttemplateexp_instantiation(instance):
    assert isinstance(instance, JTL_template_ObjectTemplateExp)



@given(instance=JTL_template_ObjectTemplateExp_strategy)
def test_jtl_template_objecttemplateexp_referredClass_setter(instance):
    original = instance.referredClass
    instance.referredClass = original
    assert instance.referredClass == original

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=JTL_JTL_Pattern_strategy)
@settings(max_examples=50)
def test_jtl_jtl_pattern_instantiation(instance):
    assert isinstance(instance, JTL_JTL_Pattern)

@given(instance=JTL_essentialocl_IfExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_ifexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_IfExp)

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=JTL_essentialocl_IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_integerliteralexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_IntegerLiteralExp)



@given(instance=JTL_essentialocl_IntegerLiteralExp_strategy)
def test_jtl_essentialocl_integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=JTL_essentialocl_RealLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_realliteralexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_RealLiteralExp)



@given(instance=JTL_essentialocl_RealLiteralExp_strategy)
def test_jtl_essentialocl_realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=JTL_essentialocl_UnlimitedNaturalExp_strategy)
@settings(max_examples=50)
def test_jtl_essentialocl_unlimitednaturalexp_instantiation(instance):
    assert isinstance(instance, JTL_essentialocl_UnlimitedNaturalExp)



@given(instance=JTL_essentialocl_UnlimitedNaturalExp_strategy)
def test_jtl_essentialocl_unlimitednaturalexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original
