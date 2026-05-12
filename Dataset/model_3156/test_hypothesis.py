import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SadlResource,
    sADL_Name,
    ExpressionScope,
    sADL_QueryStatement,
    sADL_RuleStatement,
    sADL_TestStatement,
    sADL_ExpressionStatement,
    SadlInstance,
    sADL_SadlNestedInstance,
    sADL_ValueRow,
    sADL_OrderElement,
    sADL_NamedStructureAnnotation,
    SadlExplicitValue,
    sADL_SadlUnaryExpression,
    sADL_SadlExplicitValueLiteral,
    sADL_SadlExplicitValue,
    SadlCondition,
    sADL_SadlHasValueCondition,
    sADL_SadlCardinalityCondition,
    sADL_SadlAllValuesCondition,
    SadlPropertyRestriction,
    sADL_SadlIsAnnotation,
    sADL_SadlMustBeOneOf,
    sADL_SadlTypeAssociation,
    sADL_SadlCanOnlyBeOneOf,
    sADL_SadlIsInverseOf,
    sADL_SadlIsSymmetrical,
    sADL_SadlIsTransitive,
    sADL_SadlRangeRestriction,
    sADL_SadlIsFunctional,
    sADL_SadlDefaultValue,
    sADL_SadlDataTypeFacet,
    sADL_SadlPropertyRestriction,
    sADL_SadlPropertyInitializer,
    sADL_SadlCondition,
    SadlTypeReference,
    sADL_SadlIntersectionType,
    sADL_SadlSimpleTypeReference,
    sADL_SadlPrimitiveDataType,
    sADL_SadlUnionType,
    sADL_SadlPropertyCondition,
    sADL_SadlParameterDeclaration,
    sADL_AbstractSadlEquation,
    Expression,
    sADL_ConstructExpression,
    sADL_PropOfSubject,
    sADL_Sublist,
    sADL_BinaryOperation,
    sADL_Constant,
    sADL_ElementInList,
    sADL_SubjHasProp,
    sADL_NumberLiteral,
    sADL_ValueTable,
    sADL_UnaryExpression,
    sADL_Declaration,
    sADL_StringLiteral,
    sADL_UnitExpression,
    sADL_SelectExpression,
    sADL_AskExpression,
    sADL_BooleanLiteral,
    SadlExplicitValueLiteral,
    sADL_SadlBooleanLiteral,
    sADL_SadlConstantLiteral,
    sADL_SadlNumberLiteral,
    sADL_SadlStringLiteral,
    sADL_SadlValueList,
    SadlStatement,
    sADL_SadlNecessaryAndSufficient,
    sADL_SadlTypeReference,
    sADL_SadlSameAs,
    sADL_SadlProperty,
    sADL_SadlClassOrPropertyDeclaration,
    sADL_SadlDisjointClasses,
    sADL_SadlDifferentFrom,
    sADL_SadlResource,
    sADL_SadlInstance,
    sADL_EObject,
    sADL_SadlModel,
    sADL_Expression,
    AbstractSadlEquation,
    SadlModelElement,
    sADL_ExternalEquationStatement,
    sADL_StartWriteStatement,
    sADL_ExpressionScope,
    sADL_PrintStatement,
    sADL_SadlStatement,
    sADL_EndWriteStatement,
    sADL_ReadStatement,
    sADL_ExplainStatement,
    sADL_EquationStatement,
    sADL_SadlModelElement,
    sADL_SadlImport,
    sADL_SadlAnnotation,
    SadlDataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sadlresource_is_not_abstract():
    assert not inspect.isabstract(SadlResource)


def test_sadlresource_constructor_exists():
    assert callable(SadlResource.__init__)


def test_sadlresource_constructor_args():
    sig = inspect.signature(SadlResource.__init__)
    params = list(sig.parameters.keys())



def test_sadl_name_is_not_abstract():
    assert not inspect.isabstract(sADL_Name)


def test_sadl_name_constructor_exists():
    assert callable(sADL_Name.__init__)


def test_sadl_name_constructor_args():
    sig = inspect.signature(sADL_Name.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_sadl_name_has_function():
    assert hasattr(sADL_Name, "function")
    descriptor = None
    for klass in sADL_Name.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_expressionscope_is_not_abstract():
    assert not inspect.isabstract(ExpressionScope)


def test_expressionscope_constructor_exists():
    assert callable(ExpressionScope.__init__)


def test_expressionscope_constructor_args():
    sig = inspect.signature(ExpressionScope.__init__)
    params = list(sig.parameters.keys())



def test_sadl_querystatement_is_not_abstract():
    assert not inspect.isabstract(sADL_QueryStatement)


def test_sadl_querystatement_constructor_exists():
    assert callable(sADL_QueryStatement.__init__)


def test_sadl_querystatement_constructor_args():
    sig = inspect.signature(sADL_QueryStatement.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"

def test_sadl_querystatement_has_start():
    assert hasattr(sADL_QueryStatement, "start")
    descriptor = None
    for klass in sADL_QueryStatement.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_sadl_rulestatement_is_not_abstract():
    assert not inspect.isabstract(sADL_RuleStatement)


def test_sadl_rulestatement_constructor_exists():
    assert callable(sADL_RuleStatement.__init__)


def test_sadl_rulestatement_constructor_args():
    sig = inspect.signature(sADL_RuleStatement.__init__)
    params = list(sig.parameters.keys())



def test_sadl_teststatement_is_not_abstract():
    assert not inspect.isabstract(sADL_TestStatement)


def test_sadl_teststatement_constructor_exists():
    assert callable(sADL_TestStatement.__init__)


def test_sadl_teststatement_constructor_args():
    sig = inspect.signature(sADL_TestStatement.__init__)
    params = list(sig.parameters.keys())



def test_sadl_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(sADL_ExpressionStatement)


def test_sadl_expressionstatement_constructor_exists():
    assert callable(sADL_ExpressionStatement.__init__)


def test_sadl_expressionstatement_constructor_args():
    sig = inspect.signature(sADL_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())
    assert "evaluatesTo" in params, "Missing parameter 'evaluatesTo'"

def test_sadl_expressionstatement_has_evaluatesTo():
    assert hasattr(sADL_ExpressionStatement, "evaluatesTo")
    descriptor = None
    for klass in sADL_ExpressionStatement.__mro__:
        if "evaluatesTo" in klass.__dict__:
            descriptor = klass.__dict__["evaluatesTo"]
            break
    assert isinstance(descriptor, property)



def test_sadlinstance_is_not_abstract():
    assert not inspect.isabstract(SadlInstance)


def test_sadlinstance_constructor_exists():
    assert callable(SadlInstance.__init__)


def test_sadlinstance_constructor_args():
    sig = inspect.signature(SadlInstance.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlnestedinstance_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlNestedInstance)


def test_sadl_sadlnestedinstance_constructor_exists():
    assert callable(sADL_SadlNestedInstance.__init__)


def test_sadl_sadlnestedinstance_constructor_args():
    sig = inspect.signature(sADL_SadlNestedInstance.__init__)
    params = list(sig.parameters.keys())
    assert "article" in params, "Missing parameter 'article'"

def test_sadl_sadlnestedinstance_has_article():
    assert hasattr(sADL_SadlNestedInstance, "article")
    descriptor = None
    for klass in sADL_SadlNestedInstance.__mro__:
        if "article" in klass.__dict__:
            descriptor = klass.__dict__["article"]
            break
    assert isinstance(descriptor, property)



def test_sadl_valuerow_is_not_abstract():
    assert not inspect.isabstract(sADL_ValueRow)


def test_sadl_valuerow_constructor_exists():
    assert callable(sADL_ValueRow.__init__)


def test_sadl_valuerow_constructor_args():
    sig = inspect.signature(sADL_ValueRow.__init__)
    params = list(sig.parameters.keys())



def test_sadl_orderelement_is_not_abstract():
    assert not inspect.isabstract(sADL_OrderElement)


def test_sadl_orderelement_constructor_exists():
    assert callable(sADL_OrderElement.__init__)


def test_sadl_orderelement_constructor_args():
    sig = inspect.signature(sADL_OrderElement.__init__)
    params = list(sig.parameters.keys())
    assert "desc" in params, "Missing parameter 'desc'"

def test_sadl_orderelement_has_desc():
    assert hasattr(sADL_OrderElement, "desc")
    descriptor = None
    for klass in sADL_OrderElement.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)



def test_sadl_namedstructureannotation_is_not_abstract():
    assert not inspect.isabstract(sADL_NamedStructureAnnotation)


def test_sadl_namedstructureannotation_constructor_exists():
    assert callable(sADL_NamedStructureAnnotation.__init__)


def test_sadl_namedstructureannotation_constructor_args():
    sig = inspect.signature(sADL_NamedStructureAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_sadlexplicitvalue_is_not_abstract():
    assert not inspect.isabstract(SadlExplicitValue)


def test_sadlexplicitvalue_constructor_exists():
    assert callable(SadlExplicitValue.__init__)


def test_sadlexplicitvalue_constructor_args():
    sig = inspect.signature(SadlExplicitValue.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlunaryexpression_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlUnaryExpression)


def test_sadl_sadlunaryexpression_constructor_exists():
    assert callable(sADL_SadlUnaryExpression.__init__)


def test_sadl_sadlunaryexpression_constructor_args():
    sig = inspect.signature(sADL_SadlUnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_sadl_sadlunaryexpression_has_operator():
    assert hasattr(sADL_SadlUnaryExpression, "operator")
    descriptor = None
    for klass in sADL_SadlUnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadlexplicitvalueliteral_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlExplicitValueLiteral)


def test_sadl_sadlexplicitvalueliteral_constructor_exists():
    assert callable(sADL_SadlExplicitValueLiteral.__init__)


def test_sadl_sadlexplicitvalueliteral_constructor_args():
    sig = inspect.signature(sADL_SadlExplicitValueLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlexplicitvalue_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlExplicitValue)


def test_sadl_sadlexplicitvalue_constructor_exists():
    assert callable(sADL_SadlExplicitValue.__init__)


def test_sadl_sadlexplicitvalue_constructor_args():
    sig = inspect.signature(sADL_SadlExplicitValue.__init__)
    params = list(sig.parameters.keys())



def test_sadlcondition_is_not_abstract():
    assert not inspect.isabstract(SadlCondition)


def test_sadlcondition_constructor_exists():
    assert callable(SadlCondition.__init__)


def test_sadlcondition_constructor_args():
    sig = inspect.signature(SadlCondition.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlhasvaluecondition_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlHasValueCondition)


def test_sadl_sadlhasvaluecondition_constructor_exists():
    assert callable(sADL_SadlHasValueCondition.__init__)


def test_sadl_sadlhasvaluecondition_constructor_args():
    sig = inspect.signature(sADL_SadlHasValueCondition.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlcardinalitycondition_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlCardinalityCondition)


def test_sadl_sadlcardinalitycondition_constructor_exists():
    assert callable(sADL_SadlCardinalityCondition.__init__)


def test_sadl_sadlcardinalitycondition_constructor_args():
    sig = inspect.signature(sADL_SadlCardinalityCondition.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_sadl_sadlcardinalitycondition_has_cardinality():
    assert hasattr(sADL_SadlCardinalityCondition, "cardinality")
    descriptor = None
    for klass in sADL_SadlCardinalityCondition.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)

def test_sadl_sadlcardinalitycondition_has_operator():
    assert hasattr(sADL_SadlCardinalityCondition, "operator")
    descriptor = None
    for klass in sADL_SadlCardinalityCondition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadlallvaluescondition_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlAllValuesCondition)


def test_sadl_sadlallvaluescondition_constructor_exists():
    assert callable(sADL_SadlAllValuesCondition.__init__)


def test_sadl_sadlallvaluescondition_constructor_args():
    sig = inspect.signature(sADL_SadlAllValuesCondition.__init__)
    params = list(sig.parameters.keys())



def test_sadlpropertyrestriction_is_not_abstract():
    assert not inspect.isabstract(SadlPropertyRestriction)


def test_sadlpropertyrestriction_constructor_exists():
    assert callable(SadlPropertyRestriction.__init__)


def test_sadlpropertyrestriction_constructor_args():
    sig = inspect.signature(SadlPropertyRestriction.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlisannotation_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlIsAnnotation)


def test_sadl_sadlisannotation_constructor_exists():
    assert callable(sADL_SadlIsAnnotation.__init__)


def test_sadl_sadlisannotation_constructor_args():
    sig = inspect.signature(sADL_SadlIsAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlmustbeoneof_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlMustBeOneOf)


def test_sadl_sadlmustbeoneof_constructor_exists():
    assert callable(sADL_SadlMustBeOneOf.__init__)


def test_sadl_sadlmustbeoneof_constructor_args():
    sig = inspect.signature(sADL_SadlMustBeOneOf.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadltypeassociation_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlTypeAssociation)


def test_sadl_sadltypeassociation_constructor_exists():
    assert callable(sADL_SadlTypeAssociation.__init__)


def test_sadl_sadltypeassociation_constructor_args():
    sig = inspect.signature(sADL_SadlTypeAssociation.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlcanonlybeoneof_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlCanOnlyBeOneOf)


def test_sadl_sadlcanonlybeoneof_constructor_exists():
    assert callable(sADL_SadlCanOnlyBeOneOf.__init__)


def test_sadl_sadlcanonlybeoneof_constructor_args():
    sig = inspect.signature(sADL_SadlCanOnlyBeOneOf.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlisinverseof_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlIsInverseOf)


def test_sadl_sadlisinverseof_constructor_exists():
    assert callable(sADL_SadlIsInverseOf.__init__)


def test_sadl_sadlisinverseof_constructor_args():
    sig = inspect.signature(sADL_SadlIsInverseOf.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlissymmetrical_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlIsSymmetrical)


def test_sadl_sadlissymmetrical_constructor_exists():
    assert callable(sADL_SadlIsSymmetrical.__init__)


def test_sadl_sadlissymmetrical_constructor_args():
    sig = inspect.signature(sADL_SadlIsSymmetrical.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlistransitive_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlIsTransitive)


def test_sadl_sadlistransitive_constructor_exists():
    assert callable(sADL_SadlIsTransitive.__init__)


def test_sadl_sadlistransitive_constructor_args():
    sig = inspect.signature(sADL_SadlIsTransitive.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlrangerestriction_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlRangeRestriction)


def test_sadl_sadlrangerestriction_constructor_exists():
    assert callable(sADL_SadlRangeRestriction.__init__)


def test_sadl_sadlrangerestriction_constructor_args():
    sig = inspect.signature(sADL_SadlRangeRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "singleValued" in params, "Missing parameter 'singleValued'"
    assert "typeonly" in params, "Missing parameter 'typeonly'"

def test_sadl_sadlrangerestriction_has_singleValued():
    assert hasattr(sADL_SadlRangeRestriction, "singleValued")
    descriptor = None
    for klass in sADL_SadlRangeRestriction.__mro__:
        if "singleValued" in klass.__dict__:
            descriptor = klass.__dict__["singleValued"]
            break
    assert isinstance(descriptor, property)

def test_sadl_sadlrangerestriction_has_typeonly():
    assert hasattr(sADL_SadlRangeRestriction, "typeonly")
    descriptor = None
    for klass in sADL_SadlRangeRestriction.__mro__:
        if "typeonly" in klass.__dict__:
            descriptor = klass.__dict__["typeonly"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadlisfunctional_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlIsFunctional)


def test_sadl_sadlisfunctional_constructor_exists():
    assert callable(sADL_SadlIsFunctional.__init__)


def test_sadl_sadlisfunctional_constructor_args():
    sig = inspect.signature(sADL_SadlIsFunctional.__init__)
    params = list(sig.parameters.keys())
    assert "inverse" in params, "Missing parameter 'inverse'"

def test_sadl_sadlisfunctional_has_inverse():
    assert hasattr(sADL_SadlIsFunctional, "inverse")
    descriptor = None
    for klass in sADL_SadlIsFunctional.__mro__:
        if "inverse" in klass.__dict__:
            descriptor = klass.__dict__["inverse"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadldefaultvalue_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlDefaultValue)


def test_sadl_sadldefaultvalue_constructor_exists():
    assert callable(sADL_SadlDefaultValue.__init__)


def test_sadl_sadldefaultvalue_constructor_args():
    sig = inspect.signature(sADL_SadlDefaultValue.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_sadl_sadldefaultvalue_has_level():
    assert hasattr(sADL_SadlDefaultValue, "level")
    descriptor = None
    for klass in sADL_SadlDefaultValue.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadldatatypefacet_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlDataTypeFacet)


def test_sadl_sadldatatypefacet_constructor_exists():
    assert callable(sADL_SadlDataTypeFacet.__init__)


def test_sadl_sadldatatypefacet_constructor_args():
    sig = inspect.signature(sADL_SadlDataTypeFacet.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "values" in params, "Missing parameter 'values'"
    assert "maxlen" in params, "Missing parameter 'maxlen'"
    assert "len" in params, "Missing parameter 'len'"
    assert "regex" in params, "Missing parameter 'regex'"
    assert "minlen" in params, "Missing parameter 'minlen'"
    assert "minInclusive" in params, "Missing parameter 'minInclusive'"
    assert "min" in params, "Missing parameter 'min'"
    assert "maxInclusive" in params, "Missing parameter 'maxInclusive'"

def test_sadl_sadldatatypefacet_has_max():
    assert hasattr(sADL_SadlDataTypeFacet, "max")
    descriptor = None
    for klass in sADL_SadlDataTypeFacet.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_sadl_sadldatatypefacet_has_values():
    assert hasattr(sADL_SadlDataTypeFacet, "values")
    descriptor = None
    for klass in sADL_SadlDataTypeFacet.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)

def test_sadl_sadldatatypefacet_has_maxlen():
    assert hasattr(sADL_SadlDataTypeFacet, "maxlen")
    descriptor = None
    for klass in sADL_SadlDataTypeFacet.__mro__:
        if "maxlen" in klass.__dict__:
            descriptor = klass.__dict__["maxlen"]
            break
    assert isinstance(descriptor, property)

def test_sadl_sadldatatypefacet_has_len():
    assert hasattr(sADL_SadlDataTypeFacet, "len")
    descriptor = None
    for klass in sADL_SadlDataTypeFacet.__mro__:
        if "len" in klass.__dict__:
            descriptor = klass.__dict__["len"]
            break
    assert isinstance(descriptor, property)

def test_sadl_sadldatatypefacet_has_regex():
    assert hasattr(sADL_SadlDataTypeFacet, "regex")
    descriptor = None
    for klass in sADL_SadlDataTypeFacet.__mro__:
        if "regex" in klass.__dict__:
            descriptor = klass.__dict__["regex"]
            break
    assert isinstance(descriptor, property)

def test_sadl_sadldatatypefacet_has_minlen():
    assert hasattr(sADL_SadlDataTypeFacet, "minlen")
    descriptor = None
    for klass in sADL_SadlDataTypeFacet.__mro__:
        if "minlen" in klass.__dict__:
            descriptor = klass.__dict__["minlen"]
            break
    assert isinstance(descriptor, property)

def test_sadl_sadldatatypefacet_has_minInclusive():
    assert hasattr(sADL_SadlDataTypeFacet, "minInclusive")
    descriptor = None
    for klass in sADL_SadlDataTypeFacet.__mro__:
        if "minInclusive" in klass.__dict__:
            descriptor = klass.__dict__["minInclusive"]
            break
    assert isinstance(descriptor, property)

def test_sadl_sadldatatypefacet_has_min():
    assert hasattr(sADL_SadlDataTypeFacet, "min")
    descriptor = None
    for klass in sADL_SadlDataTypeFacet.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_sadl_sadldatatypefacet_has_maxInclusive():
    assert hasattr(sADL_SadlDataTypeFacet, "maxInclusive")
    descriptor = None
    for klass in sADL_SadlDataTypeFacet.__mro__:
        if "maxInclusive" in klass.__dict__:
            descriptor = klass.__dict__["maxInclusive"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadlpropertyrestriction_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlPropertyRestriction)


def test_sadl_sadlpropertyrestriction_constructor_exists():
    assert callable(sADL_SadlPropertyRestriction.__init__)


def test_sadl_sadlpropertyrestriction_constructor_args():
    sig = inspect.signature(sADL_SadlPropertyRestriction.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlpropertyinitializer_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlPropertyInitializer)


def test_sadl_sadlpropertyinitializer_constructor_exists():
    assert callable(sADL_SadlPropertyInitializer.__init__)


def test_sadl_sadlpropertyinitializer_constructor_args():
    sig = inspect.signature(sADL_SadlPropertyInitializer.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlcondition_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlCondition)


def test_sadl_sadlcondition_constructor_exists():
    assert callable(sADL_SadlCondition.__init__)


def test_sadl_sadlcondition_constructor_args():
    sig = inspect.signature(sADL_SadlCondition.__init__)
    params = list(sig.parameters.keys())



def test_sadltypereference_is_not_abstract():
    assert not inspect.isabstract(SadlTypeReference)


def test_sadltypereference_constructor_exists():
    assert callable(SadlTypeReference.__init__)


def test_sadltypereference_constructor_args():
    sig = inspect.signature(SadlTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlintersectiontype_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlIntersectionType)


def test_sadl_sadlintersectiontype_constructor_exists():
    assert callable(sADL_SadlIntersectionType.__init__)


def test_sadl_sadlintersectiontype_constructor_args():
    sig = inspect.signature(sADL_SadlIntersectionType.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlsimpletypereference_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlSimpleTypeReference)


def test_sadl_sadlsimpletypereference_constructor_exists():
    assert callable(sADL_SadlSimpleTypeReference.__init__)


def test_sadl_sadlsimpletypereference_constructor_args():
    sig = inspect.signature(sADL_SadlSimpleTypeReference.__init__)
    params = list(sig.parameters.keys())
    assert "list" in params, "Missing parameter 'list'"

def test_sadl_sadlsimpletypereference_has_list():
    assert hasattr(sADL_SadlSimpleTypeReference, "list")
    descriptor = None
    for klass in sADL_SadlSimpleTypeReference.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadlprimitivedatatype_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlPrimitiveDataType)


def test_sadl_sadlprimitivedatatype_constructor_exists():
    assert callable(sADL_SadlPrimitiveDataType.__init__)


def test_sadl_sadlprimitivedatatype_constructor_args():
    sig = inspect.signature(sADL_SadlPrimitiveDataType.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"
    assert "list" in params, "Missing parameter 'list'"

def test_sadl_sadlprimitivedatatype_has_primitiveType():
    assert hasattr(sADL_SadlPrimitiveDataType, "primitiveType")
    descriptor = None
    for klass in sADL_SadlPrimitiveDataType.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)

def test_sadl_sadlprimitivedatatype_has_list():
    assert hasattr(sADL_SadlPrimitiveDataType, "list")
    descriptor = None
    for klass in sADL_SadlPrimitiveDataType.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadluniontype_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlUnionType)


def test_sadl_sadluniontype_constructor_exists():
    assert callable(sADL_SadlUnionType.__init__)


def test_sadl_sadluniontype_constructor_args():
    sig = inspect.signature(sADL_SadlUnionType.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlpropertycondition_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlPropertyCondition)


def test_sadl_sadlpropertycondition_constructor_exists():
    assert callable(sADL_SadlPropertyCondition.__init__)


def test_sadl_sadlpropertycondition_constructor_args():
    sig = inspect.signature(sADL_SadlPropertyCondition.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlParameterDeclaration)


def test_sadl_sadlparameterdeclaration_constructor_exists():
    assert callable(sADL_SadlParameterDeclaration.__init__)


def test_sadl_sadlparameterdeclaration_constructor_args():
    sig = inspect.signature(sADL_SadlParameterDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "unknown" in params, "Missing parameter 'unknown'"
    assert "ellipsis" in params, "Missing parameter 'ellipsis'"

def test_sadl_sadlparameterdeclaration_has_unknown():
    assert hasattr(sADL_SadlParameterDeclaration, "unknown")
    descriptor = None
    for klass in sADL_SadlParameterDeclaration.__mro__:
        if "unknown" in klass.__dict__:
            descriptor = klass.__dict__["unknown"]
            break
    assert isinstance(descriptor, property)

def test_sadl_sadlparameterdeclaration_has_ellipsis():
    assert hasattr(sADL_SadlParameterDeclaration, "ellipsis")
    descriptor = None
    for klass in sADL_SadlParameterDeclaration.__mro__:
        if "ellipsis" in klass.__dict__:
            descriptor = klass.__dict__["ellipsis"]
            break
    assert isinstance(descriptor, property)



def test_sadl_abstractsadlequation_is_not_abstract():
    assert not inspect.isabstract(sADL_AbstractSadlEquation)


def test_sadl_abstractsadlequation_constructor_exists():
    assert callable(sADL_AbstractSadlEquation.__init__)


def test_sadl_abstractsadlequation_constructor_args():
    sig = inspect.signature(sADL_AbstractSadlEquation.__init__)
    params = list(sig.parameters.keys())
    assert "unknown" in params, "Missing parameter 'unknown'"

def test_sadl_abstractsadlequation_has_unknown():
    assert hasattr(sADL_AbstractSadlEquation, "unknown")
    descriptor = None
    for klass in sADL_AbstractSadlEquation.__mro__:
        if "unknown" in klass.__dict__:
            descriptor = klass.__dict__["unknown"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_sadl_constructexpression_is_not_abstract():
    assert not inspect.isabstract(sADL_ConstructExpression)


def test_sadl_constructexpression_constructor_exists():
    assert callable(sADL_ConstructExpression.__init__)


def test_sadl_constructexpression_constructor_args():
    sig = inspect.signature(sADL_ConstructExpression.__init__)
    params = list(sig.parameters.keys())



def test_sadl_propofsubject_is_not_abstract():
    assert not inspect.isabstract(sADL_PropOfSubject)


def test_sadl_propofsubject_constructor_exists():
    assert callable(sADL_PropOfSubject.__init__)


def test_sadl_propofsubject_constructor_args():
    sig = inspect.signature(sADL_PropOfSubject.__init__)
    params = list(sig.parameters.keys())
    assert "of" in params, "Missing parameter 'of'"

def test_sadl_propofsubject_has_of():
    assert hasattr(sADL_PropOfSubject, "of")
    descriptor = None
    for klass in sADL_PropOfSubject.__mro__:
        if "of" in klass.__dict__:
            descriptor = klass.__dict__["of"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sublist_is_not_abstract():
    assert not inspect.isabstract(sADL_Sublist)


def test_sadl_sublist_constructor_exists():
    assert callable(sADL_Sublist.__init__)


def test_sadl_sublist_constructor_args():
    sig = inspect.signature(sADL_Sublist.__init__)
    params = list(sig.parameters.keys())



def test_sadl_binaryoperation_is_not_abstract():
    assert not inspect.isabstract(sADL_BinaryOperation)


def test_sadl_binaryoperation_constructor_exists():
    assert callable(sADL_BinaryOperation.__init__)


def test_sadl_binaryoperation_constructor_args():
    sig = inspect.signature(sADL_BinaryOperation.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sadl_binaryoperation_has_op():
    assert hasattr(sADL_BinaryOperation, "op")
    descriptor = None
    for klass in sADL_BinaryOperation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sadl_constant_is_not_abstract():
    assert not inspect.isabstract(sADL_Constant)


def test_sadl_constant_constructor_exists():
    assert callable(sADL_Constant.__init__)


def test_sadl_constant_constructor_args():
    sig = inspect.signature(sADL_Constant.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"

def test_sadl_constant_has_constant():
    assert hasattr(sADL_Constant, "constant")
    descriptor = None
    for klass in sADL_Constant.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_sadl_elementinlist_is_not_abstract():
    assert not inspect.isabstract(sADL_ElementInList)


def test_sadl_elementinlist_constructor_exists():
    assert callable(sADL_ElementInList.__init__)


def test_sadl_elementinlist_constructor_args():
    sig = inspect.signature(sADL_ElementInList.__init__)
    params = list(sig.parameters.keys())
    assert "after" in params, "Missing parameter 'after'"
    assert "before" in params, "Missing parameter 'before'"

def test_sadl_elementinlist_has_after():
    assert hasattr(sADL_ElementInList, "after")
    descriptor = None
    for klass in sADL_ElementInList.__mro__:
        if "after" in klass.__dict__:
            descriptor = klass.__dict__["after"]
            break
    assert isinstance(descriptor, property)

def test_sadl_elementinlist_has_before():
    assert hasattr(sADL_ElementInList, "before")
    descriptor = None
    for klass in sADL_ElementInList.__mro__:
        if "before" in klass.__dict__:
            descriptor = klass.__dict__["before"]
            break
    assert isinstance(descriptor, property)



def test_sadl_subjhasprop_is_not_abstract():
    assert not inspect.isabstract(sADL_SubjHasProp)


def test_sadl_subjhasprop_constructor_exists():
    assert callable(sADL_SubjHasProp.__init__)


def test_sadl_subjhasprop_constructor_args():
    sig = inspect.signature(sADL_SubjHasProp.__init__)
    params = list(sig.parameters.keys())
    assert "comma" in params, "Missing parameter 'comma'"

def test_sadl_subjhasprop_has_comma():
    assert hasattr(sADL_SubjHasProp, "comma")
    descriptor = None
    for klass in sADL_SubjHasProp.__mro__:
        if "comma" in klass.__dict__:
            descriptor = klass.__dict__["comma"]
            break
    assert isinstance(descriptor, property)



def test_sadl_numberliteral_is_not_abstract():
    assert not inspect.isabstract(sADL_NumberLiteral)


def test_sadl_numberliteral_constructor_exists():
    assert callable(sADL_NumberLiteral.__init__)


def test_sadl_numberliteral_constructor_args():
    sig = inspect.signature(sADL_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sadl_numberliteral_has_value():
    assert hasattr(sADL_NumberLiteral, "value")
    descriptor = None
    for klass in sADL_NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sadl_valuetable_is_not_abstract():
    assert not inspect.isabstract(sADL_ValueTable)


def test_sadl_valuetable_constructor_exists():
    assert callable(sADL_ValueTable.__init__)


def test_sadl_valuetable_constructor_args():
    sig = inspect.signature(sADL_ValueTable.__init__)
    params = list(sig.parameters.keys())



def test_sadl_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(sADL_UnaryExpression)


def test_sadl_unaryexpression_constructor_exists():
    assert callable(sADL_UnaryExpression.__init__)


def test_sadl_unaryexpression_constructor_args():
    sig = inspect.signature(sADL_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sadl_unaryexpression_has_op():
    assert hasattr(sADL_UnaryExpression, "op")
    descriptor = None
    for klass in sADL_UnaryExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sadl_declaration_is_not_abstract():
    assert not inspect.isabstract(sADL_Declaration)


def test_sadl_declaration_constructor_exists():
    assert callable(sADL_Declaration.__init__)


def test_sadl_declaration_constructor_args():
    sig = inspect.signature(sADL_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "ordinal" in params, "Missing parameter 'ordinal'"
    assert "len" in params, "Missing parameter 'len'"
    assert "maxlen" in params, "Missing parameter 'maxlen'"
    assert "article" in params, "Missing parameter 'article'"

def test_sadl_declaration_has_ordinal():
    assert hasattr(sADL_Declaration, "ordinal")
    descriptor = None
    for klass in sADL_Declaration.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)

def test_sadl_declaration_has_len():
    assert hasattr(sADL_Declaration, "len")
    descriptor = None
    for klass in sADL_Declaration.__mro__:
        if "len" in klass.__dict__:
            descriptor = klass.__dict__["len"]
            break
    assert isinstance(descriptor, property)

def test_sadl_declaration_has_maxlen():
    assert hasattr(sADL_Declaration, "maxlen")
    descriptor = None
    for klass in sADL_Declaration.__mro__:
        if "maxlen" in klass.__dict__:
            descriptor = klass.__dict__["maxlen"]
            break
    assert isinstance(descriptor, property)

def test_sadl_declaration_has_article():
    assert hasattr(sADL_Declaration, "article")
    descriptor = None
    for klass in sADL_Declaration.__mro__:
        if "article" in klass.__dict__:
            descriptor = klass.__dict__["article"]
            break
    assert isinstance(descriptor, property)



def test_sadl_stringliteral_is_not_abstract():
    assert not inspect.isabstract(sADL_StringLiteral)


def test_sadl_stringliteral_constructor_exists():
    assert callable(sADL_StringLiteral.__init__)


def test_sadl_stringliteral_constructor_args():
    sig = inspect.signature(sADL_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sadl_stringliteral_has_value():
    assert hasattr(sADL_StringLiteral, "value")
    descriptor = None
    for klass in sADL_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sadl_unitexpression_is_not_abstract():
    assert not inspect.isabstract(sADL_UnitExpression)


def test_sadl_unitexpression_constructor_exists():
    assert callable(sADL_UnitExpression.__init__)


def test_sadl_unitexpression_constructor_args():
    sig = inspect.signature(sADL_UnitExpression.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_sadl_unitexpression_has_unit():
    assert hasattr(sADL_UnitExpression, "unit")
    descriptor = None
    for klass in sADL_UnitExpression.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_sadl_selectexpression_is_not_abstract():
    assert not inspect.isabstract(sADL_SelectExpression)


def test_sadl_selectexpression_constructor_exists():
    assert callable(sADL_SelectExpression.__init__)


def test_sadl_selectexpression_constructor_args():
    sig = inspect.signature(sADL_SelectExpression.__init__)
    params = list(sig.parameters.keys())
    assert "orderby" in params, "Missing parameter 'orderby'"
    assert "distinct" in params, "Missing parameter 'distinct'"

def test_sadl_selectexpression_has_orderby():
    assert hasattr(sADL_SelectExpression, "orderby")
    descriptor = None
    for klass in sADL_SelectExpression.__mro__:
        if "orderby" in klass.__dict__:
            descriptor = klass.__dict__["orderby"]
            break
    assert isinstance(descriptor, property)

def test_sadl_selectexpression_has_distinct():
    assert hasattr(sADL_SelectExpression, "distinct")
    descriptor = None
    for klass in sADL_SelectExpression.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)



def test_sadl_askexpression_is_not_abstract():
    assert not inspect.isabstract(sADL_AskExpression)


def test_sadl_askexpression_constructor_exists():
    assert callable(sADL_AskExpression.__init__)


def test_sadl_askexpression_constructor_args():
    sig = inspect.signature(sADL_AskExpression.__init__)
    params = list(sig.parameters.keys())



def test_sadl_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(sADL_BooleanLiteral)


def test_sadl_booleanliteral_constructor_exists():
    assert callable(sADL_BooleanLiteral.__init__)


def test_sadl_booleanliteral_constructor_args():
    sig = inspect.signature(sADL_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sadl_booleanliteral_has_value():
    assert hasattr(sADL_BooleanLiteral, "value")
    descriptor = None
    for klass in sADL_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sadlexplicitvalueliteral_is_not_abstract():
    assert not inspect.isabstract(SadlExplicitValueLiteral)


def test_sadlexplicitvalueliteral_constructor_exists():
    assert callable(SadlExplicitValueLiteral.__init__)


def test_sadlexplicitvalueliteral_constructor_args():
    sig = inspect.signature(SadlExplicitValueLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlbooleanliteral_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlBooleanLiteral)


def test_sadl_sadlbooleanliteral_constructor_exists():
    assert callable(sADL_SadlBooleanLiteral.__init__)


def test_sadl_sadlbooleanliteral_constructor_args():
    sig = inspect.signature(sADL_SadlBooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "truethy" in params, "Missing parameter 'truethy'"

def test_sadl_sadlbooleanliteral_has_truethy():
    assert hasattr(sADL_SadlBooleanLiteral, "truethy")
    descriptor = None
    for klass in sADL_SadlBooleanLiteral.__mro__:
        if "truethy" in klass.__dict__:
            descriptor = klass.__dict__["truethy"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadlconstantliteral_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlConstantLiteral)


def test_sadl_sadlconstantliteral_constructor_exists():
    assert callable(sADL_SadlConstantLiteral.__init__)


def test_sadl_sadlconstantliteral_constructor_args():
    sig = inspect.signature(sADL_SadlConstantLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "term" in params, "Missing parameter 'term'"

def test_sadl_sadlconstantliteral_has_term():
    assert hasattr(sADL_SadlConstantLiteral, "term")
    descriptor = None
    for klass in sADL_SadlConstantLiteral.__mro__:
        if "term" in klass.__dict__:
            descriptor = klass.__dict__["term"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadlnumberliteral_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlNumberLiteral)


def test_sadl_sadlnumberliteral_constructor_exists():
    assert callable(sADL_SadlNumberLiteral.__init__)


def test_sadl_sadlnumberliteral_constructor_args():
    sig = inspect.signature(sADL_SadlNumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literalNumber" in params, "Missing parameter 'literalNumber'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_sadl_sadlnumberliteral_has_literalNumber():
    assert hasattr(sADL_SadlNumberLiteral, "literalNumber")
    descriptor = None
    for klass in sADL_SadlNumberLiteral.__mro__:
        if "literalNumber" in klass.__dict__:
            descriptor = klass.__dict__["literalNumber"]
            break
    assert isinstance(descriptor, property)

def test_sadl_sadlnumberliteral_has_unit():
    assert hasattr(sADL_SadlNumberLiteral, "unit")
    descriptor = None
    for klass in sADL_SadlNumberLiteral.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadlstringliteral_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlStringLiteral)


def test_sadl_sadlstringliteral_constructor_exists():
    assert callable(sADL_SadlStringLiteral.__init__)


def test_sadl_sadlstringliteral_constructor_args():
    sig = inspect.signature(sADL_SadlStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literalString" in params, "Missing parameter 'literalString'"

def test_sadl_sadlstringliteral_has_literalString():
    assert hasattr(sADL_SadlStringLiteral, "literalString")
    descriptor = None
    for klass in sADL_SadlStringLiteral.__mro__:
        if "literalString" in klass.__dict__:
            descriptor = klass.__dict__["literalString"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadlvaluelist_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlValueList)


def test_sadl_sadlvaluelist_constructor_exists():
    assert callable(sADL_SadlValueList.__init__)


def test_sadl_sadlvaluelist_constructor_args():
    sig = inspect.signature(sADL_SadlValueList.__init__)
    params = list(sig.parameters.keys())



def test_sadlstatement_is_not_abstract():
    assert not inspect.isabstract(SadlStatement)


def test_sadlstatement_constructor_exists():
    assert callable(SadlStatement.__init__)


def test_sadlstatement_constructor_args():
    sig = inspect.signature(SadlStatement.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlnecessaryandsufficient_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlNecessaryAndSufficient)


def test_sadl_sadlnecessaryandsufficient_constructor_exists():
    assert callable(sADL_SadlNecessaryAndSufficient.__init__)


def test_sadl_sadlnecessaryandsufficient_constructor_args():
    sig = inspect.signature(sADL_SadlNecessaryAndSufficient.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadltypereference_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlTypeReference)


def test_sadl_sadltypereference_constructor_exists():
    assert callable(sADL_SadlTypeReference.__init__)


def test_sadl_sadltypereference_constructor_args():
    sig = inspect.signature(sADL_SadlTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlsameas_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlSameAs)


def test_sadl_sadlsameas_constructor_exists():
    assert callable(sADL_SadlSameAs.__init__)


def test_sadl_sadlsameas_constructor_args():
    sig = inspect.signature(sADL_SadlSameAs.__init__)
    params = list(sig.parameters.keys())
    assert "complement" in params, "Missing parameter 'complement'"

def test_sadl_sadlsameas_has_complement():
    assert hasattr(sADL_SadlSameAs, "complement")
    descriptor = None
    for klass in sADL_SadlSameAs.__mro__:
        if "complement" in klass.__dict__:
            descriptor = klass.__dict__["complement"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadlproperty_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlProperty)


def test_sadl_sadlproperty_constructor_exists():
    assert callable(sADL_SadlProperty.__init__)


def test_sadl_sadlproperty_constructor_args():
    sig = inspect.signature(sADL_SadlProperty.__init__)
    params = list(sig.parameters.keys())
    assert "primaryDeclaration" in params, "Missing parameter 'primaryDeclaration'"

def test_sadl_sadlproperty_has_primaryDeclaration():
    assert hasattr(sADL_SadlProperty, "primaryDeclaration")
    descriptor = None
    for klass in sADL_SadlProperty.__mro__:
        if "primaryDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["primaryDeclaration"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadlclassorpropertydeclaration_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlClassOrPropertyDeclaration)


def test_sadl_sadlclassorpropertydeclaration_constructor_exists():
    assert callable(sADL_SadlClassOrPropertyDeclaration.__init__)


def test_sadl_sadlclassorpropertydeclaration_constructor_args():
    sig = inspect.signature(sADL_SadlClassOrPropertyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadldisjointclasses_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlDisjointClasses)


def test_sadl_sadldisjointclasses_constructor_exists():
    assert callable(sADL_SadlDisjointClasses.__init__)


def test_sadl_sadldisjointclasses_constructor_args():
    sig = inspect.signature(sADL_SadlDisjointClasses.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadldifferentfrom_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlDifferentFrom)


def test_sadl_sadldifferentfrom_constructor_exists():
    assert callable(sADL_SadlDifferentFrom.__init__)


def test_sadl_sadldifferentfrom_constructor_args():
    sig = inspect.signature(sADL_SadlDifferentFrom.__init__)
    params = list(sig.parameters.keys())
    assert "complement" in params, "Missing parameter 'complement'"

def test_sadl_sadldifferentfrom_has_complement():
    assert hasattr(sADL_SadlDifferentFrom, "complement")
    descriptor = None
    for klass in sADL_SadlDifferentFrom.__mro__:
        if "complement" in klass.__dict__:
            descriptor = klass.__dict__["complement"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadlresource_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlResource)


def test_sadl_sadlresource_constructor_exists():
    assert callable(sADL_SadlResource.__init__)


def test_sadl_sadlresource_constructor_args():
    sig = inspect.signature(sADL_SadlResource.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlinstance_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlInstance)


def test_sadl_sadlinstance_constructor_exists():
    assert callable(sADL_SadlInstance.__init__)


def test_sadl_sadlinstance_constructor_args():
    sig = inspect.signature(sADL_SadlInstance.__init__)
    params = list(sig.parameters.keys())



def test_sadl_eobject_is_not_abstract():
    assert not inspect.isabstract(sADL_EObject)


def test_sadl_eobject_constructor_exists():
    assert callable(sADL_EObject.__init__)


def test_sadl_eobject_constructor_args():
    sig = inspect.signature(sADL_EObject.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlmodel_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlModel)


def test_sadl_sadlmodel_constructor_exists():
    assert callable(sADL_SadlModel.__init__)


def test_sadl_sadlmodel_constructor_args():
    sig = inspect.signature(sADL_SadlModel.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "baseUri" in params, "Missing parameter 'baseUri'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_sadl_sadlmodel_has_version():
    assert hasattr(sADL_SadlModel, "version")
    descriptor = None
    for klass in sADL_SadlModel.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_sadl_sadlmodel_has_baseUri():
    assert hasattr(sADL_SadlModel, "baseUri")
    descriptor = None
    for klass in sADL_SadlModel.__mro__:
        if "baseUri" in klass.__dict__:
            descriptor = klass.__dict__["baseUri"]
            break
    assert isinstance(descriptor, property)

def test_sadl_sadlmodel_has_alias():
    assert hasattr(sADL_SadlModel, "alias")
    descriptor = None
    for klass in sADL_SadlModel.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_sadl_expression_is_not_abstract():
    assert not inspect.isabstract(sADL_Expression)


def test_sadl_expression_constructor_exists():
    assert callable(sADL_Expression.__init__)


def test_sadl_expression_constructor_args():
    sig = inspect.signature(sADL_Expression.__init__)
    params = list(sig.parameters.keys())



def test_abstractsadlequation_is_not_abstract():
    assert not inspect.isabstract(AbstractSadlEquation)


def test_abstractsadlequation_constructor_exists():
    assert callable(AbstractSadlEquation.__init__)


def test_abstractsadlequation_constructor_args():
    sig = inspect.signature(AbstractSadlEquation.__init__)
    params = list(sig.parameters.keys())



def test_sadlmodelelement_is_not_abstract():
    assert not inspect.isabstract(SadlModelElement)


def test_sadlmodelelement_constructor_exists():
    assert callable(SadlModelElement.__init__)


def test_sadlmodelelement_constructor_args():
    sig = inspect.signature(SadlModelElement.__init__)
    params = list(sig.parameters.keys())



def test_sadl_externalequationstatement_is_not_abstract():
    assert not inspect.isabstract(sADL_ExternalEquationStatement)


def test_sadl_externalequationstatement_constructor_exists():
    assert callable(sADL_ExternalEquationStatement.__init__)


def test_sadl_externalequationstatement_constructor_args():
    sig = inspect.signature(sADL_ExternalEquationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "uri" in params, "Missing parameter 'uri'"

def test_sadl_externalequationstatement_has_location():
    assert hasattr(sADL_ExternalEquationStatement, "location")
    descriptor = None
    for klass in sADL_ExternalEquationStatement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_sadl_externalequationstatement_has_uri():
    assert hasattr(sADL_ExternalEquationStatement, "uri")
    descriptor = None
    for klass in sADL_ExternalEquationStatement.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_sadl_startwritestatement_is_not_abstract():
    assert not inspect.isabstract(sADL_StartWriteStatement)


def test_sadl_startwritestatement_constructor_exists():
    assert callable(sADL_StartWriteStatement.__init__)


def test_sadl_startwritestatement_constructor_args():
    sig = inspect.signature(sADL_StartWriteStatement.__init__)
    params = list(sig.parameters.keys())
    assert "write" in params, "Missing parameter 'write'"
    assert "dataOnly" in params, "Missing parameter 'dataOnly'"

def test_sadl_startwritestatement_has_write():
    assert hasattr(sADL_StartWriteStatement, "write")
    descriptor = None
    for klass in sADL_StartWriteStatement.__mro__:
        if "write" in klass.__dict__:
            descriptor = klass.__dict__["write"]
            break
    assert isinstance(descriptor, property)

def test_sadl_startwritestatement_has_dataOnly():
    assert hasattr(sADL_StartWriteStatement, "dataOnly")
    descriptor = None
    for klass in sADL_StartWriteStatement.__mro__:
        if "dataOnly" in klass.__dict__:
            descriptor = klass.__dict__["dataOnly"]
            break
    assert isinstance(descriptor, property)



def test_sadl_expressionscope_is_not_abstract():
    assert not inspect.isabstract(sADL_ExpressionScope)


def test_sadl_expressionscope_constructor_exists():
    assert callable(sADL_ExpressionScope.__init__)


def test_sadl_expressionscope_constructor_args():
    sig = inspect.signature(sADL_ExpressionScope.__init__)
    params = list(sig.parameters.keys())



def test_sadl_printstatement_is_not_abstract():
    assert not inspect.isabstract(sADL_PrintStatement)


def test_sadl_printstatement_constructor_exists():
    assert callable(sADL_PrintStatement.__init__)


def test_sadl_printstatement_constructor_args():
    sig = inspect.signature(sADL_PrintStatement.__init__)
    params = list(sig.parameters.keys())
    assert "displayString" in params, "Missing parameter 'displayString'"
    assert "model" in params, "Missing parameter 'model'"

def test_sadl_printstatement_has_displayString():
    assert hasattr(sADL_PrintStatement, "displayString")
    descriptor = None
    for klass in sADL_PrintStatement.__mro__:
        if "displayString" in klass.__dict__:
            descriptor = klass.__dict__["displayString"]
            break
    assert isinstance(descriptor, property)

def test_sadl_printstatement_has_model():
    assert hasattr(sADL_PrintStatement, "model")
    descriptor = None
    for klass in sADL_PrintStatement.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadlstatement_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlStatement)


def test_sadl_sadlstatement_constructor_exists():
    assert callable(sADL_SadlStatement.__init__)


def test_sadl_sadlstatement_constructor_args():
    sig = inspect.signature(sADL_SadlStatement.__init__)
    params = list(sig.parameters.keys())



def test_sadl_endwritestatement_is_not_abstract():
    assert not inspect.isabstract(sADL_EndWriteStatement)


def test_sadl_endwritestatement_constructor_exists():
    assert callable(sADL_EndWriteStatement.__init__)


def test_sadl_endwritestatement_constructor_args():
    sig = inspect.signature(sADL_EndWriteStatement.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_sadl_endwritestatement_has_filename():
    assert hasattr(sADL_EndWriteStatement, "filename")
    descriptor = None
    for klass in sADL_EndWriteStatement.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_sadl_readstatement_is_not_abstract():
    assert not inspect.isabstract(sADL_ReadStatement)


def test_sadl_readstatement_constructor_exists():
    assert callable(sADL_ReadStatement.__init__)


def test_sadl_readstatement_constructor_args():
    sig = inspect.signature(sADL_ReadStatement.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"
    assert "templateFilename" in params, "Missing parameter 'templateFilename'"

def test_sadl_readstatement_has_filename():
    assert hasattr(sADL_ReadStatement, "filename")
    descriptor = None
    for klass in sADL_ReadStatement.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_sadl_readstatement_has_templateFilename():
    assert hasattr(sADL_ReadStatement, "templateFilename")
    descriptor = None
    for klass in sADL_ReadStatement.__mro__:
        if "templateFilename" in klass.__dict__:
            descriptor = klass.__dict__["templateFilename"]
            break
    assert isinstance(descriptor, property)



def test_sadl_explainstatement_is_not_abstract():
    assert not inspect.isabstract(sADL_ExplainStatement)


def test_sadl_explainstatement_constructor_exists():
    assert callable(sADL_ExplainStatement.__init__)


def test_sadl_explainstatement_constructor_args():
    sig = inspect.signature(sADL_ExplainStatement.__init__)
    params = list(sig.parameters.keys())



def test_sadl_equationstatement_is_not_abstract():
    assert not inspect.isabstract(sADL_EquationStatement)


def test_sadl_equationstatement_constructor_exists():
    assert callable(sADL_EquationStatement.__init__)


def test_sadl_equationstatement_constructor_args():
    sig = inspect.signature(sADL_EquationStatement.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlmodelelement_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlModelElement)


def test_sadl_sadlmodelelement_constructor_exists():
    assert callable(sADL_SadlModelElement.__init__)


def test_sadl_sadlmodelelement_constructor_args():
    sig = inspect.signature(sADL_SadlModelElement.__init__)
    params = list(sig.parameters.keys())



def test_sadl_sadlimport_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlImport)


def test_sadl_sadlimport_constructor_exists():
    assert callable(sADL_SadlImport.__init__)


def test_sadl_sadlimport_constructor_args():
    sig = inspect.signature(sADL_SadlImport.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_sadl_sadlimport_has_alias():
    assert hasattr(sADL_SadlImport, "alias")
    descriptor = None
    for klass in sADL_SadlImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_sadl_sadlannotation_is_not_abstract():
    assert not inspect.isabstract(sADL_SadlAnnotation)


def test_sadl_sadlannotation_constructor_exists():
    assert callable(sADL_SadlAnnotation.__init__)


def test_sadl_sadlannotation_constructor_args():
    sig = inspect.signature(sADL_SadlAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "contents" in params, "Missing parameter 'contents'"
    assert "type" in params, "Missing parameter 'type'"

def test_sadl_sadlannotation_has_contents():
    assert hasattr(sADL_SadlAnnotation, "contents")
    descriptor = None
    for klass in sADL_SadlAnnotation.__mro__:
        if "contents" in klass.__dict__:
            descriptor = klass.__dict__["contents"]
            break
    assert isinstance(descriptor, property)

def test_sadl_sadlannotation_has_type():
    assert hasattr(sADL_SadlAnnotation, "type")
    descriptor = None
    for klass in sADL_SadlAnnotation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_sadldatatype_exists():
    # Check that the Enumeration exists
    assert SadlDataType is not None

def test_sadldatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SadlDataType]
    expected_literals = [
        "duration",
        "integer",
        "time",
        "anyURI",
        "boolean",
        "long",
        "positiveInteger",
        "double",
        "anySimpleType",
        "byte",
        "gYearMonth",
        "decimal",
        "float",
        "unsignedByte",
        "dateTime",
        "nonPositiveInteger",
        "string",
        "gDay",
        "hexBinary",
        "gMonthDay",
        "gYear",
        "unsignedInt",
        "nonNegativeInteger",
        "int",
        "negativeInteger",
        "gMonth",
        "base64Binary",
        "date",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SadlDataType"


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
SadlResource_strategy = st.builds(
    SadlResource,
)
sADL_Name_strategy = st.builds(
    sADL_Name,
    function=
        st.booleans()
)
ExpressionScope_strategy = st.builds(
    ExpressionScope,
)
sADL_QueryStatement_strategy = st.builds(
    sADL_QueryStatement,
    start=
        safe_text
)
sADL_RuleStatement_strategy = st.builds(
    sADL_RuleStatement,
)
sADL_TestStatement_strategy = st.builds(
    sADL_TestStatement,
)
sADL_ExpressionStatement_strategy = st.builds(
    sADL_ExpressionStatement,
    evaluatesTo=
        safe_text
)
SadlInstance_strategy = st.builds(
    SadlInstance,
)
sADL_SadlNestedInstance_strategy = st.builds(
    sADL_SadlNestedInstance,
    article=
        safe_text
)
sADL_ValueRow_strategy = st.builds(
    sADL_ValueRow,
)
sADL_OrderElement_strategy = st.builds(
    sADL_OrderElement,
    desc=
        st.booleans()
)
sADL_NamedStructureAnnotation_strategy = st.builds(
    sADL_NamedStructureAnnotation,
)
SadlExplicitValue_strategy = st.builds(
    SadlExplicitValue,
)
sADL_SadlUnaryExpression_strategy = st.builds(
    sADL_SadlUnaryExpression,
    operator=
        safe_text
)
sADL_SadlExplicitValueLiteral_strategy = st.builds(
    sADL_SadlExplicitValueLiteral,
)
sADL_SadlExplicitValue_strategy = st.builds(
    sADL_SadlExplicitValue,
)
SadlCondition_strategy = st.builds(
    SadlCondition,
)
sADL_SadlHasValueCondition_strategy = st.builds(
    sADL_SadlHasValueCondition,
)
sADL_SadlCardinalityCondition_strategy = st.builds(
    sADL_SadlCardinalityCondition,
    cardinality=
        safe_text,
    operator=
        safe_text
)
sADL_SadlAllValuesCondition_strategy = st.builds(
    sADL_SadlAllValuesCondition,
)
SadlPropertyRestriction_strategy = st.builds(
    SadlPropertyRestriction,
)
sADL_SadlIsAnnotation_strategy = st.builds(
    sADL_SadlIsAnnotation,
)
sADL_SadlMustBeOneOf_strategy = st.builds(
    sADL_SadlMustBeOneOf,
)
sADL_SadlTypeAssociation_strategy = st.builds(
    sADL_SadlTypeAssociation,
)
sADL_SadlCanOnlyBeOneOf_strategy = st.builds(
    sADL_SadlCanOnlyBeOneOf,
)
sADL_SadlIsInverseOf_strategy = st.builds(
    sADL_SadlIsInverseOf,
)
sADL_SadlIsSymmetrical_strategy = st.builds(
    sADL_SadlIsSymmetrical,
)
sADL_SadlIsTransitive_strategy = st.builds(
    sADL_SadlIsTransitive,
)
sADL_SadlRangeRestriction_strategy = st.builds(
    sADL_SadlRangeRestriction,
    singleValued=
        st.booleans(),
    typeonly=
        safe_text
)
sADL_SadlIsFunctional_strategy = st.builds(
    sADL_SadlIsFunctional,
    inverse=
        st.booleans()
)
sADL_SadlDefaultValue_strategy = st.builds(
    sADL_SadlDefaultValue,
    level=
        st.integers()
)
sADL_SadlDataTypeFacet_strategy = st.builds(
    sADL_SadlDataTypeFacet,
    max=
        safe_text,
    values=
        safe_text,
    maxlen=
        safe_text,
    len=
        safe_text,
    regex=
        safe_text,
    minlen=
        safe_text,
    minInclusive=
        st.booleans(),
    min=
        safe_text,
    maxInclusive=
        st.booleans()
)
sADL_SadlPropertyRestriction_strategy = st.builds(
    sADL_SadlPropertyRestriction,
)
sADL_SadlPropertyInitializer_strategy = st.builds(
    sADL_SadlPropertyInitializer,
)
sADL_SadlCondition_strategy = st.builds(
    sADL_SadlCondition,
)
SadlTypeReference_strategy = st.builds(
    SadlTypeReference,
)
sADL_SadlIntersectionType_strategy = st.builds(
    sADL_SadlIntersectionType,
)
sADL_SadlSimpleTypeReference_strategy = st.builds(
    sADL_SadlSimpleTypeReference,
    list=
        st.booleans()
)
sADL_SadlPrimitiveDataType_strategy = st.builds(
    sADL_SadlPrimitiveDataType,
    primitiveType=
        safe_text,
    list=
        st.booleans()
)
sADL_SadlUnionType_strategy = st.builds(
    sADL_SadlUnionType,
)
sADL_SadlPropertyCondition_strategy = st.builds(
    sADL_SadlPropertyCondition,
)
sADL_SadlParameterDeclaration_strategy = st.builds(
    sADL_SadlParameterDeclaration,
    unknown=
        safe_text,
    ellipsis=
        safe_text
)
sADL_AbstractSadlEquation_strategy = st.builds(
    sADL_AbstractSadlEquation,
    unknown=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
sADL_ConstructExpression_strategy = st.builds(
    sADL_ConstructExpression,
)
sADL_PropOfSubject_strategy = st.builds(
    sADL_PropOfSubject,
    of=
        safe_text
)
sADL_Sublist_strategy = st.builds(
    sADL_Sublist,
)
sADL_BinaryOperation_strategy = st.builds(
    sADL_BinaryOperation,
    op=
        safe_text
)
sADL_Constant_strategy = st.builds(
    sADL_Constant,
    constant=
        safe_text
)
sADL_ElementInList_strategy = st.builds(
    sADL_ElementInList,
    after=
        st.booleans(),
    before=
        st.booleans()
)
sADL_SubjHasProp_strategy = st.builds(
    sADL_SubjHasProp,
    comma=
        st.booleans()
)
sADL_NumberLiteral_strategy = st.builds(
    sADL_NumberLiteral,
    value=
        safe_text
)
sADL_ValueTable_strategy = st.builds(
    sADL_ValueTable,
)
sADL_UnaryExpression_strategy = st.builds(
    sADL_UnaryExpression,
    op=
        safe_text
)
sADL_Declaration_strategy = st.builds(
    sADL_Declaration,
    ordinal=
        safe_text,
    len=
        safe_text,
    maxlen=
        safe_text,
    article=
        safe_text
)
sADL_StringLiteral_strategy = st.builds(
    sADL_StringLiteral,
    value=
        safe_text
)
sADL_UnitExpression_strategy = st.builds(
    sADL_UnitExpression,
    unit=
        safe_text
)
sADL_SelectExpression_strategy = st.builds(
    sADL_SelectExpression,
    orderby=
        safe_text,
    distinct=
        st.booleans()
)
sADL_AskExpression_strategy = st.builds(
    sADL_AskExpression,
)
sADL_BooleanLiteral_strategy = st.builds(
    sADL_BooleanLiteral,
    value=
        safe_text
)
SadlExplicitValueLiteral_strategy = st.builds(
    SadlExplicitValueLiteral,
)
sADL_SadlBooleanLiteral_strategy = st.builds(
    sADL_SadlBooleanLiteral,
    truethy=
        st.booleans()
)
sADL_SadlConstantLiteral_strategy = st.builds(
    sADL_SadlConstantLiteral,
    term=
        safe_text
)
sADL_SadlNumberLiteral_strategy = st.builds(
    sADL_SadlNumberLiteral,
    literalNumber=
        safe_text,
    unit=
        safe_text
)
sADL_SadlStringLiteral_strategy = st.builds(
    sADL_SadlStringLiteral,
    literalString=
        safe_text
)
sADL_SadlValueList_strategy = st.builds(
    sADL_SadlValueList,
)
SadlStatement_strategy = st.builds(
    SadlStatement,
)
sADL_SadlNecessaryAndSufficient_strategy = st.builds(
    sADL_SadlNecessaryAndSufficient,
)
sADL_SadlTypeReference_strategy = st.builds(
    sADL_SadlTypeReference,
)
sADL_SadlSameAs_strategy = st.builds(
    sADL_SadlSameAs,
    complement=
        st.booleans()
)
sADL_SadlProperty_strategy = st.builds(
    sADL_SadlProperty,
    primaryDeclaration=
        st.booleans()
)
sADL_SadlClassOrPropertyDeclaration_strategy = st.builds(
    sADL_SadlClassOrPropertyDeclaration,
)
sADL_SadlDisjointClasses_strategy = st.builds(
    sADL_SadlDisjointClasses,
)
sADL_SadlDifferentFrom_strategy = st.builds(
    sADL_SadlDifferentFrom,
    complement=
        st.booleans()
)
sADL_SadlResource_strategy = st.builds(
    sADL_SadlResource,
)
sADL_SadlInstance_strategy = st.builds(
    sADL_SadlInstance,
)
sADL_EObject_strategy = st.builds(
    sADL_EObject,
)
sADL_SadlModel_strategy = st.builds(
    sADL_SadlModel,
    version=
        safe_text,
    baseUri=
        safe_text,
    alias=
        safe_text
)
sADL_Expression_strategy = st.builds(
    sADL_Expression,
)
AbstractSadlEquation_strategy = st.builds(
    AbstractSadlEquation,
)
SadlModelElement_strategy = st.builds(
    SadlModelElement,
)
sADL_ExternalEquationStatement_strategy = st.builds(
    sADL_ExternalEquationStatement,
    location=
        safe_text,
    uri=
        safe_text
)
sADL_StartWriteStatement_strategy = st.builds(
    sADL_StartWriteStatement,
    write=
        safe_text,
    dataOnly=
        safe_text
)
sADL_ExpressionScope_strategy = st.builds(
    sADL_ExpressionScope,
)
sADL_PrintStatement_strategy = st.builds(
    sADL_PrintStatement,
    displayString=
        safe_text,
    model=
        safe_text
)
sADL_SadlStatement_strategy = st.builds(
    sADL_SadlStatement,
)
sADL_EndWriteStatement_strategy = st.builds(
    sADL_EndWriteStatement,
    filename=
        safe_text
)
sADL_ReadStatement_strategy = st.builds(
    sADL_ReadStatement,
    filename=
        safe_text,
    templateFilename=
        safe_text
)
sADL_ExplainStatement_strategy = st.builds(
    sADL_ExplainStatement,
)
sADL_EquationStatement_strategy = st.builds(
    sADL_EquationStatement,
)
sADL_SadlModelElement_strategy = st.builds(
    sADL_SadlModelElement,
)
sADL_SadlImport_strategy = st.builds(
    sADL_SadlImport,
    alias=
        safe_text
)
sADL_SadlAnnotation_strategy = st.builds(
    sADL_SadlAnnotation,
    contents=
        safe_text,
    type=
        safe_text
)

@given(instance=SadlResource_strategy)
@settings(max_examples=50)
def test_sadlresource_instantiation(instance):
    assert isinstance(instance, SadlResource)

@given(instance=sADL_Name_strategy)
@settings(max_examples=50)
def test_sadl_name_instantiation(instance):
    assert isinstance(instance, sADL_Name)



@given(instance=sADL_Name_strategy)
def test_sadl_name_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=ExpressionScope_strategy)
@settings(max_examples=50)
def test_expressionscope_instantiation(instance):
    assert isinstance(instance, ExpressionScope)

@given(instance=sADL_QueryStatement_strategy)
@settings(max_examples=50)
def test_sadl_querystatement_instantiation(instance):
    assert isinstance(instance, sADL_QueryStatement)



@given(instance=sADL_QueryStatement_strategy)
def test_sadl_querystatement_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=sADL_RuleStatement_strategy)
@settings(max_examples=50)
def test_sadl_rulestatement_instantiation(instance):
    assert isinstance(instance, sADL_RuleStatement)

@given(instance=sADL_TestStatement_strategy)
@settings(max_examples=50)
def test_sadl_teststatement_instantiation(instance):
    assert isinstance(instance, sADL_TestStatement)

@given(instance=sADL_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_sadl_expressionstatement_instantiation(instance):
    assert isinstance(instance, sADL_ExpressionStatement)



@given(instance=sADL_ExpressionStatement_strategy)
def test_sadl_expressionstatement_evaluatesTo_setter(instance):
    original = instance.evaluatesTo
    instance.evaluatesTo = original
    assert instance.evaluatesTo == original

@given(instance=SadlInstance_strategy)
@settings(max_examples=50)
def test_sadlinstance_instantiation(instance):
    assert isinstance(instance, SadlInstance)

@given(instance=sADL_SadlNestedInstance_strategy)
@settings(max_examples=50)
def test_sadl_sadlnestedinstance_instantiation(instance):
    assert isinstance(instance, sADL_SadlNestedInstance)



@given(instance=sADL_SadlNestedInstance_strategy)
def test_sadl_sadlnestedinstance_article_setter(instance):
    original = instance.article
    instance.article = original
    assert instance.article == original

@given(instance=sADL_ValueRow_strategy)
@settings(max_examples=50)
def test_sadl_valuerow_instantiation(instance):
    assert isinstance(instance, sADL_ValueRow)

@given(instance=sADL_OrderElement_strategy)
@settings(max_examples=50)
def test_sadl_orderelement_instantiation(instance):
    assert isinstance(instance, sADL_OrderElement)



@given(instance=sADL_OrderElement_strategy)
def test_sadl_orderelement_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=sADL_NamedStructureAnnotation_strategy)
@settings(max_examples=50)
def test_sadl_namedstructureannotation_instantiation(instance):
    assert isinstance(instance, sADL_NamedStructureAnnotation)

@given(instance=SadlExplicitValue_strategy)
@settings(max_examples=50)
def test_sadlexplicitvalue_instantiation(instance):
    assert isinstance(instance, SadlExplicitValue)

@given(instance=sADL_SadlUnaryExpression_strategy)
@settings(max_examples=50)
def test_sadl_sadlunaryexpression_instantiation(instance):
    assert isinstance(instance, sADL_SadlUnaryExpression)



@given(instance=sADL_SadlUnaryExpression_strategy)
def test_sadl_sadlunaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=sADL_SadlExplicitValueLiteral_strategy)
@settings(max_examples=50)
def test_sadl_sadlexplicitvalueliteral_instantiation(instance):
    assert isinstance(instance, sADL_SadlExplicitValueLiteral)

@given(instance=sADL_SadlExplicitValue_strategy)
@settings(max_examples=50)
def test_sadl_sadlexplicitvalue_instantiation(instance):
    assert isinstance(instance, sADL_SadlExplicitValue)

@given(instance=SadlCondition_strategy)
@settings(max_examples=50)
def test_sadlcondition_instantiation(instance):
    assert isinstance(instance, SadlCondition)

@given(instance=sADL_SadlHasValueCondition_strategy)
@settings(max_examples=50)
def test_sadl_sadlhasvaluecondition_instantiation(instance):
    assert isinstance(instance, sADL_SadlHasValueCondition)

@given(instance=sADL_SadlCardinalityCondition_strategy)
@settings(max_examples=50)
def test_sadl_sadlcardinalitycondition_instantiation(instance):
    assert isinstance(instance, sADL_SadlCardinalityCondition)



@given(instance=sADL_SadlCardinalityCondition_strategy)
def test_sadl_sadlcardinalitycondition_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original



@given(instance=sADL_SadlCardinalityCondition_strategy)
def test_sadl_sadlcardinalitycondition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=sADL_SadlAllValuesCondition_strategy)
@settings(max_examples=50)
def test_sadl_sadlallvaluescondition_instantiation(instance):
    assert isinstance(instance, sADL_SadlAllValuesCondition)

@given(instance=SadlPropertyRestriction_strategy)
@settings(max_examples=50)
def test_sadlpropertyrestriction_instantiation(instance):
    assert isinstance(instance, SadlPropertyRestriction)

@given(instance=sADL_SadlIsAnnotation_strategy)
@settings(max_examples=50)
def test_sadl_sadlisannotation_instantiation(instance):
    assert isinstance(instance, sADL_SadlIsAnnotation)

@given(instance=sADL_SadlMustBeOneOf_strategy)
@settings(max_examples=50)
def test_sadl_sadlmustbeoneof_instantiation(instance):
    assert isinstance(instance, sADL_SadlMustBeOneOf)

@given(instance=sADL_SadlTypeAssociation_strategy)
@settings(max_examples=50)
def test_sadl_sadltypeassociation_instantiation(instance):
    assert isinstance(instance, sADL_SadlTypeAssociation)

@given(instance=sADL_SadlCanOnlyBeOneOf_strategy)
@settings(max_examples=50)
def test_sadl_sadlcanonlybeoneof_instantiation(instance):
    assert isinstance(instance, sADL_SadlCanOnlyBeOneOf)

@given(instance=sADL_SadlIsInverseOf_strategy)
@settings(max_examples=50)
def test_sadl_sadlisinverseof_instantiation(instance):
    assert isinstance(instance, sADL_SadlIsInverseOf)

@given(instance=sADL_SadlIsSymmetrical_strategy)
@settings(max_examples=50)
def test_sadl_sadlissymmetrical_instantiation(instance):
    assert isinstance(instance, sADL_SadlIsSymmetrical)

@given(instance=sADL_SadlIsTransitive_strategy)
@settings(max_examples=50)
def test_sadl_sadlistransitive_instantiation(instance):
    assert isinstance(instance, sADL_SadlIsTransitive)

@given(instance=sADL_SadlRangeRestriction_strategy)
@settings(max_examples=50)
def test_sadl_sadlrangerestriction_instantiation(instance):
    assert isinstance(instance, sADL_SadlRangeRestriction)



@given(instance=sADL_SadlRangeRestriction_strategy)
def test_sadl_sadlrangerestriction_singleValued_setter(instance):
    original = instance.singleValued
    instance.singleValued = original
    assert instance.singleValued == original



@given(instance=sADL_SadlRangeRestriction_strategy)
def test_sadl_sadlrangerestriction_typeonly_setter(instance):
    original = instance.typeonly
    instance.typeonly = original
    assert instance.typeonly == original

@given(instance=sADL_SadlIsFunctional_strategy)
@settings(max_examples=50)
def test_sadl_sadlisfunctional_instantiation(instance):
    assert isinstance(instance, sADL_SadlIsFunctional)



@given(instance=sADL_SadlIsFunctional_strategy)
def test_sadl_sadlisfunctional_inverse_setter(instance):
    original = instance.inverse
    instance.inverse = original
    assert instance.inverse == original

@given(instance=sADL_SadlDefaultValue_strategy)
@settings(max_examples=50)
def test_sadl_sadldefaultvalue_instantiation(instance):
    assert isinstance(instance, sADL_SadlDefaultValue)



@given(instance=sADL_SadlDefaultValue_strategy)
def test_sadl_sadldefaultvalue_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=sADL_SadlDataTypeFacet_strategy)
@settings(max_examples=50)
def test_sadl_sadldatatypefacet_instantiation(instance):
    assert isinstance(instance, sADL_SadlDataTypeFacet)



@given(instance=sADL_SadlDataTypeFacet_strategy)
def test_sadl_sadldatatypefacet_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=sADL_SadlDataTypeFacet_strategy)
def test_sadl_sadldatatypefacet_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original



@given(instance=sADL_SadlDataTypeFacet_strategy)
def test_sadl_sadldatatypefacet_maxlen_setter(instance):
    original = instance.maxlen
    instance.maxlen = original
    assert instance.maxlen == original



@given(instance=sADL_SadlDataTypeFacet_strategy)
def test_sadl_sadldatatypefacet_len_setter(instance):
    original = instance.len
    instance.len = original
    assert instance.len == original



@given(instance=sADL_SadlDataTypeFacet_strategy)
def test_sadl_sadldatatypefacet_regex_setter(instance):
    original = instance.regex
    instance.regex = original
    assert instance.regex == original



@given(instance=sADL_SadlDataTypeFacet_strategy)
def test_sadl_sadldatatypefacet_minlen_setter(instance):
    original = instance.minlen
    instance.minlen = original
    assert instance.minlen == original



@given(instance=sADL_SadlDataTypeFacet_strategy)
def test_sadl_sadldatatypefacet_minInclusive_setter(instance):
    original = instance.minInclusive
    instance.minInclusive = original
    assert instance.minInclusive == original



@given(instance=sADL_SadlDataTypeFacet_strategy)
def test_sadl_sadldatatypefacet_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=sADL_SadlDataTypeFacet_strategy)
def test_sadl_sadldatatypefacet_maxInclusive_setter(instance):
    original = instance.maxInclusive
    instance.maxInclusive = original
    assert instance.maxInclusive == original

@given(instance=sADL_SadlPropertyRestriction_strategy)
@settings(max_examples=50)
def test_sadl_sadlpropertyrestriction_instantiation(instance):
    assert isinstance(instance, sADL_SadlPropertyRestriction)

@given(instance=sADL_SadlPropertyInitializer_strategy)
@settings(max_examples=50)
def test_sadl_sadlpropertyinitializer_instantiation(instance):
    assert isinstance(instance, sADL_SadlPropertyInitializer)

@given(instance=sADL_SadlCondition_strategy)
@settings(max_examples=50)
def test_sadl_sadlcondition_instantiation(instance):
    assert isinstance(instance, sADL_SadlCondition)

@given(instance=SadlTypeReference_strategy)
@settings(max_examples=50)
def test_sadltypereference_instantiation(instance):
    assert isinstance(instance, SadlTypeReference)

@given(instance=sADL_SadlIntersectionType_strategy)
@settings(max_examples=50)
def test_sadl_sadlintersectiontype_instantiation(instance):
    assert isinstance(instance, sADL_SadlIntersectionType)

@given(instance=sADL_SadlSimpleTypeReference_strategy)
@settings(max_examples=50)
def test_sadl_sadlsimpletypereference_instantiation(instance):
    assert isinstance(instance, sADL_SadlSimpleTypeReference)



@given(instance=sADL_SadlSimpleTypeReference_strategy)
def test_sadl_sadlsimpletypereference_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=sADL_SadlPrimitiveDataType_strategy)
@settings(max_examples=50)
def test_sadl_sadlprimitivedatatype_instantiation(instance):
    assert isinstance(instance, sADL_SadlPrimitiveDataType)



@given(instance=sADL_SadlPrimitiveDataType_strategy)
def test_sadl_sadlprimitivedatatype_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original



@given(instance=sADL_SadlPrimitiveDataType_strategy)
def test_sadl_sadlprimitivedatatype_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=sADL_SadlUnionType_strategy)
@settings(max_examples=50)
def test_sadl_sadluniontype_instantiation(instance):
    assert isinstance(instance, sADL_SadlUnionType)

@given(instance=sADL_SadlPropertyCondition_strategy)
@settings(max_examples=50)
def test_sadl_sadlpropertycondition_instantiation(instance):
    assert isinstance(instance, sADL_SadlPropertyCondition)

@given(instance=sADL_SadlParameterDeclaration_strategy)
@settings(max_examples=50)
def test_sadl_sadlparameterdeclaration_instantiation(instance):
    assert isinstance(instance, sADL_SadlParameterDeclaration)



@given(instance=sADL_SadlParameterDeclaration_strategy)
def test_sadl_sadlparameterdeclaration_unknown_setter(instance):
    original = instance.unknown
    instance.unknown = original
    assert instance.unknown == original



@given(instance=sADL_SadlParameterDeclaration_strategy)
def test_sadl_sadlparameterdeclaration_ellipsis_setter(instance):
    original = instance.ellipsis
    instance.ellipsis = original
    assert instance.ellipsis == original

@given(instance=sADL_AbstractSadlEquation_strategy)
@settings(max_examples=50)
def test_sadl_abstractsadlequation_instantiation(instance):
    assert isinstance(instance, sADL_AbstractSadlEquation)



@given(instance=sADL_AbstractSadlEquation_strategy)
def test_sadl_abstractsadlequation_unknown_setter(instance):
    original = instance.unknown
    instance.unknown = original
    assert instance.unknown == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=sADL_ConstructExpression_strategy)
@settings(max_examples=50)
def test_sadl_constructexpression_instantiation(instance):
    assert isinstance(instance, sADL_ConstructExpression)

@given(instance=sADL_PropOfSubject_strategy)
@settings(max_examples=50)
def test_sadl_propofsubject_instantiation(instance):
    assert isinstance(instance, sADL_PropOfSubject)



@given(instance=sADL_PropOfSubject_strategy)
def test_sadl_propofsubject_of_setter(instance):
    original = instance.of
    instance.of = original
    assert instance.of == original

@given(instance=sADL_Sublist_strategy)
@settings(max_examples=50)
def test_sadl_sublist_instantiation(instance):
    assert isinstance(instance, sADL_Sublist)

@given(instance=sADL_BinaryOperation_strategy)
@settings(max_examples=50)
def test_sadl_binaryoperation_instantiation(instance):
    assert isinstance(instance, sADL_BinaryOperation)



@given(instance=sADL_BinaryOperation_strategy)
def test_sadl_binaryoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sADL_Constant_strategy)
@settings(max_examples=50)
def test_sadl_constant_instantiation(instance):
    assert isinstance(instance, sADL_Constant)



@given(instance=sADL_Constant_strategy)
def test_sadl_constant_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=sADL_ElementInList_strategy)
@settings(max_examples=50)
def test_sadl_elementinlist_instantiation(instance):
    assert isinstance(instance, sADL_ElementInList)



@given(instance=sADL_ElementInList_strategy)
def test_sadl_elementinlist_after_setter(instance):
    original = instance.after
    instance.after = original
    assert instance.after == original



@given(instance=sADL_ElementInList_strategy)
def test_sadl_elementinlist_before_setter(instance):
    original = instance.before
    instance.before = original
    assert instance.before == original

@given(instance=sADL_SubjHasProp_strategy)
@settings(max_examples=50)
def test_sadl_subjhasprop_instantiation(instance):
    assert isinstance(instance, sADL_SubjHasProp)



@given(instance=sADL_SubjHasProp_strategy)
def test_sadl_subjhasprop_comma_setter(instance):
    original = instance.comma
    instance.comma = original
    assert instance.comma == original

@given(instance=sADL_NumberLiteral_strategy)
@settings(max_examples=50)
def test_sadl_numberliteral_instantiation(instance):
    assert isinstance(instance, sADL_NumberLiteral)



@given(instance=sADL_NumberLiteral_strategy)
def test_sadl_numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sADL_ValueTable_strategy)
@settings(max_examples=50)
def test_sadl_valuetable_instantiation(instance):
    assert isinstance(instance, sADL_ValueTable)

@given(instance=sADL_UnaryExpression_strategy)
@settings(max_examples=50)
def test_sadl_unaryexpression_instantiation(instance):
    assert isinstance(instance, sADL_UnaryExpression)



@given(instance=sADL_UnaryExpression_strategy)
def test_sadl_unaryexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sADL_Declaration_strategy)
@settings(max_examples=50)
def test_sadl_declaration_instantiation(instance):
    assert isinstance(instance, sADL_Declaration)



@given(instance=sADL_Declaration_strategy)
def test_sadl_declaration_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original



@given(instance=sADL_Declaration_strategy)
def test_sadl_declaration_len_setter(instance):
    original = instance.len
    instance.len = original
    assert instance.len == original



@given(instance=sADL_Declaration_strategy)
def test_sadl_declaration_maxlen_setter(instance):
    original = instance.maxlen
    instance.maxlen = original
    assert instance.maxlen == original



@given(instance=sADL_Declaration_strategy)
def test_sadl_declaration_article_setter(instance):
    original = instance.article
    instance.article = original
    assert instance.article == original

@given(instance=sADL_StringLiteral_strategy)
@settings(max_examples=50)
def test_sadl_stringliteral_instantiation(instance):
    assert isinstance(instance, sADL_StringLiteral)



@given(instance=sADL_StringLiteral_strategy)
def test_sadl_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sADL_UnitExpression_strategy)
@settings(max_examples=50)
def test_sadl_unitexpression_instantiation(instance):
    assert isinstance(instance, sADL_UnitExpression)



@given(instance=sADL_UnitExpression_strategy)
def test_sadl_unitexpression_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=sADL_SelectExpression_strategy)
@settings(max_examples=50)
def test_sadl_selectexpression_instantiation(instance):
    assert isinstance(instance, sADL_SelectExpression)



@given(instance=sADL_SelectExpression_strategy)
def test_sadl_selectexpression_orderby_setter(instance):
    original = instance.orderby
    instance.orderby = original
    assert instance.orderby == original



@given(instance=sADL_SelectExpression_strategy)
def test_sadl_selectexpression_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=sADL_AskExpression_strategy)
@settings(max_examples=50)
def test_sadl_askexpression_instantiation(instance):
    assert isinstance(instance, sADL_AskExpression)

@given(instance=sADL_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_sadl_booleanliteral_instantiation(instance):
    assert isinstance(instance, sADL_BooleanLiteral)



@given(instance=sADL_BooleanLiteral_strategy)
def test_sadl_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SadlExplicitValueLiteral_strategy)
@settings(max_examples=50)
def test_sadlexplicitvalueliteral_instantiation(instance):
    assert isinstance(instance, SadlExplicitValueLiteral)

@given(instance=sADL_SadlBooleanLiteral_strategy)
@settings(max_examples=50)
def test_sadl_sadlbooleanliteral_instantiation(instance):
    assert isinstance(instance, sADL_SadlBooleanLiteral)



@given(instance=sADL_SadlBooleanLiteral_strategy)
def test_sadl_sadlbooleanliteral_truethy_setter(instance):
    original = instance.truethy
    instance.truethy = original
    assert instance.truethy == original

@given(instance=sADL_SadlConstantLiteral_strategy)
@settings(max_examples=50)
def test_sadl_sadlconstantliteral_instantiation(instance):
    assert isinstance(instance, sADL_SadlConstantLiteral)



@given(instance=sADL_SadlConstantLiteral_strategy)
def test_sadl_sadlconstantliteral_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original

@given(instance=sADL_SadlNumberLiteral_strategy)
@settings(max_examples=50)
def test_sadl_sadlnumberliteral_instantiation(instance):
    assert isinstance(instance, sADL_SadlNumberLiteral)



@given(instance=sADL_SadlNumberLiteral_strategy)
def test_sadl_sadlnumberliteral_literalNumber_setter(instance):
    original = instance.literalNumber
    instance.literalNumber = original
    assert instance.literalNumber == original



@given(instance=sADL_SadlNumberLiteral_strategy)
def test_sadl_sadlnumberliteral_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=sADL_SadlStringLiteral_strategy)
@settings(max_examples=50)
def test_sadl_sadlstringliteral_instantiation(instance):
    assert isinstance(instance, sADL_SadlStringLiteral)



@given(instance=sADL_SadlStringLiteral_strategy)
def test_sadl_sadlstringliteral_literalString_setter(instance):
    original = instance.literalString
    instance.literalString = original
    assert instance.literalString == original

@given(instance=sADL_SadlValueList_strategy)
@settings(max_examples=50)
def test_sadl_sadlvaluelist_instantiation(instance):
    assert isinstance(instance, sADL_SadlValueList)

@given(instance=SadlStatement_strategy)
@settings(max_examples=50)
def test_sadlstatement_instantiation(instance):
    assert isinstance(instance, SadlStatement)

@given(instance=sADL_SadlNecessaryAndSufficient_strategy)
@settings(max_examples=50)
def test_sadl_sadlnecessaryandsufficient_instantiation(instance):
    assert isinstance(instance, sADL_SadlNecessaryAndSufficient)

@given(instance=sADL_SadlTypeReference_strategy)
@settings(max_examples=50)
def test_sadl_sadltypereference_instantiation(instance):
    assert isinstance(instance, sADL_SadlTypeReference)

@given(instance=sADL_SadlSameAs_strategy)
@settings(max_examples=50)
def test_sadl_sadlsameas_instantiation(instance):
    assert isinstance(instance, sADL_SadlSameAs)



@given(instance=sADL_SadlSameAs_strategy)
def test_sadl_sadlsameas_complement_setter(instance):
    original = instance.complement
    instance.complement = original
    assert instance.complement == original

@given(instance=sADL_SadlProperty_strategy)
@settings(max_examples=50)
def test_sadl_sadlproperty_instantiation(instance):
    assert isinstance(instance, sADL_SadlProperty)



@given(instance=sADL_SadlProperty_strategy)
def test_sadl_sadlproperty_primaryDeclaration_setter(instance):
    original = instance.primaryDeclaration
    instance.primaryDeclaration = original
    assert instance.primaryDeclaration == original

@given(instance=sADL_SadlClassOrPropertyDeclaration_strategy)
@settings(max_examples=50)
def test_sadl_sadlclassorpropertydeclaration_instantiation(instance):
    assert isinstance(instance, sADL_SadlClassOrPropertyDeclaration)

@given(instance=sADL_SadlDisjointClasses_strategy)
@settings(max_examples=50)
def test_sadl_sadldisjointclasses_instantiation(instance):
    assert isinstance(instance, sADL_SadlDisjointClasses)

@given(instance=sADL_SadlDifferentFrom_strategy)
@settings(max_examples=50)
def test_sadl_sadldifferentfrom_instantiation(instance):
    assert isinstance(instance, sADL_SadlDifferentFrom)



@given(instance=sADL_SadlDifferentFrom_strategy)
def test_sadl_sadldifferentfrom_complement_setter(instance):
    original = instance.complement
    instance.complement = original
    assert instance.complement == original

@given(instance=sADL_SadlResource_strategy)
@settings(max_examples=50)
def test_sadl_sadlresource_instantiation(instance):
    assert isinstance(instance, sADL_SadlResource)

@given(instance=sADL_SadlInstance_strategy)
@settings(max_examples=50)
def test_sadl_sadlinstance_instantiation(instance):
    assert isinstance(instance, sADL_SadlInstance)

@given(instance=sADL_EObject_strategy)
@settings(max_examples=50)
def test_sadl_eobject_instantiation(instance):
    assert isinstance(instance, sADL_EObject)

@given(instance=sADL_SadlModel_strategy)
@settings(max_examples=50)
def test_sadl_sadlmodel_instantiation(instance):
    assert isinstance(instance, sADL_SadlModel)



@given(instance=sADL_SadlModel_strategy)
def test_sadl_sadlmodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=sADL_SadlModel_strategy)
def test_sadl_sadlmodel_baseUri_setter(instance):
    original = instance.baseUri
    instance.baseUri = original
    assert instance.baseUri == original



@given(instance=sADL_SadlModel_strategy)
def test_sadl_sadlmodel_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=sADL_Expression_strategy)
@settings(max_examples=50)
def test_sadl_expression_instantiation(instance):
    assert isinstance(instance, sADL_Expression)

@given(instance=AbstractSadlEquation_strategy)
@settings(max_examples=50)
def test_abstractsadlequation_instantiation(instance):
    assert isinstance(instance, AbstractSadlEquation)

@given(instance=SadlModelElement_strategy)
@settings(max_examples=50)
def test_sadlmodelelement_instantiation(instance):
    assert isinstance(instance, SadlModelElement)

@given(instance=sADL_ExternalEquationStatement_strategy)
@settings(max_examples=50)
def test_sadl_externalequationstatement_instantiation(instance):
    assert isinstance(instance, sADL_ExternalEquationStatement)



@given(instance=sADL_ExternalEquationStatement_strategy)
def test_sadl_externalequationstatement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=sADL_ExternalEquationStatement_strategy)
def test_sadl_externalequationstatement_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=sADL_StartWriteStatement_strategy)
@settings(max_examples=50)
def test_sadl_startwritestatement_instantiation(instance):
    assert isinstance(instance, sADL_StartWriteStatement)



@given(instance=sADL_StartWriteStatement_strategy)
def test_sadl_startwritestatement_write_setter(instance):
    original = instance.write
    instance.write = original
    assert instance.write == original



@given(instance=sADL_StartWriteStatement_strategy)
def test_sadl_startwritestatement_dataOnly_setter(instance):
    original = instance.dataOnly
    instance.dataOnly = original
    assert instance.dataOnly == original

@given(instance=sADL_ExpressionScope_strategy)
@settings(max_examples=50)
def test_sadl_expressionscope_instantiation(instance):
    assert isinstance(instance, sADL_ExpressionScope)

@given(instance=sADL_PrintStatement_strategy)
@settings(max_examples=50)
def test_sadl_printstatement_instantiation(instance):
    assert isinstance(instance, sADL_PrintStatement)



@given(instance=sADL_PrintStatement_strategy)
def test_sadl_printstatement_displayString_setter(instance):
    original = instance.displayString
    instance.displayString = original
    assert instance.displayString == original



@given(instance=sADL_PrintStatement_strategy)
def test_sadl_printstatement_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original

@given(instance=sADL_SadlStatement_strategy)
@settings(max_examples=50)
def test_sadl_sadlstatement_instantiation(instance):
    assert isinstance(instance, sADL_SadlStatement)

@given(instance=sADL_EndWriteStatement_strategy)
@settings(max_examples=50)
def test_sadl_endwritestatement_instantiation(instance):
    assert isinstance(instance, sADL_EndWriteStatement)



@given(instance=sADL_EndWriteStatement_strategy)
def test_sadl_endwritestatement_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=sADL_ReadStatement_strategy)
@settings(max_examples=50)
def test_sadl_readstatement_instantiation(instance):
    assert isinstance(instance, sADL_ReadStatement)



@given(instance=sADL_ReadStatement_strategy)
def test_sadl_readstatement_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original



@given(instance=sADL_ReadStatement_strategy)
def test_sadl_readstatement_templateFilename_setter(instance):
    original = instance.templateFilename
    instance.templateFilename = original
    assert instance.templateFilename == original

@given(instance=sADL_ExplainStatement_strategy)
@settings(max_examples=50)
def test_sadl_explainstatement_instantiation(instance):
    assert isinstance(instance, sADL_ExplainStatement)

@given(instance=sADL_EquationStatement_strategy)
@settings(max_examples=50)
def test_sadl_equationstatement_instantiation(instance):
    assert isinstance(instance, sADL_EquationStatement)

@given(instance=sADL_SadlModelElement_strategy)
@settings(max_examples=50)
def test_sadl_sadlmodelelement_instantiation(instance):
    assert isinstance(instance, sADL_SadlModelElement)

@given(instance=sADL_SadlImport_strategy)
@settings(max_examples=50)
def test_sadl_sadlimport_instantiation(instance):
    assert isinstance(instance, sADL_SadlImport)



@given(instance=sADL_SadlImport_strategy)
def test_sadl_sadlimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=sADL_SadlAnnotation_strategy)
@settings(max_examples=50)
def test_sadl_sadlannotation_instantiation(instance):
    assert isinstance(instance, sADL_SadlAnnotation)



@given(instance=sADL_SadlAnnotation_strategy)
def test_sadl_sadlannotation_contents_setter(instance):
    original = instance.contents
    instance.contents = original
    assert instance.contents == original



@given(instance=sADL_SadlAnnotation_strategy)
def test_sadl_sadlannotation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
