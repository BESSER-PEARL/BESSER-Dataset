import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SadlResource,
    sADL::Name,
    ExpressionScope,
    sADL::QueryStatement,
    sADL::RuleStatement,
    sADL::TestStatement,
    sADL::ExpressionStatement,
    SadlInstance,
    sADL::SadlNestedInstance,
    sADL::ValueRow,
    sADL::OrderElement,
    sADL::NamedStructureAnnotation,
    SadlExplicitValue,
    sADL::SadlUnaryExpression,
    sADL::SadlExplicitValueLiteral,
    sADL::SadlExplicitValue,
    SadlCondition,
    sADL::SadlCardinalityCondition,
    sADL::SadlHasValueCondition,
    sADL::SadlAllValuesCondition,
    SadlPropertyRestriction,
    sADL::SadlIsTransitive,
    sADL::SadlIsAnnotation,
    sADL::SadlIsFunctional,
    sADL::SadlIsSymmetrical,
    sADL::SadlIsInverseOf,
    sADL::SadlTypeAssociation,
    sADL::SadlDefaultValue,
    sADL::SadlMustBeOneOf,
    sADL::SadlCanOnlyBeOneOf,
    sADL::SadlRangeRestriction,
    sADL::SadlDataTypeFacet,
    sADL::SadlPropertyRestriction,
    sADL::SadlPropertyInitializer,
    sADL::SadlCondition,
    SadlTypeReference,
    sADL::SadlIntersectionType,
    sADL::SadlPrimitiveDataType,
    sADL::SadlSimpleTypeReference,
    sADL::SadlUnionType,
    sADL::SadlPropertyCondition,
    sADL::SadlParameterDeclaration,
    sADL::AbstractSadlEquation,
    Expression,
    sADL::BinaryOperation,
    sADL::Declaration,
    sADL::ConstructExpression,
    sADL::ValueTable,
    sADL::SubjHasProp,
    sADL::UnitExpression,
    sADL::NumberLiteral,
    sADL::StringLiteral,
    sADL::SelectExpression,
    sADL::UnaryExpression,
    sADL::Constant,
    sADL::PropOfSubject,
    sADL::Sublist,
    sADL::BooleanLiteral,
    sADL::ElementInList,
    sADL::AskExpression,
    SadlExplicitValueLiteral,
    sADL::SadlStringLiteral,
    sADL::SadlConstantLiteral,
    sADL::SadlNumberLiteral,
    sADL::SadlBooleanLiteral,
    sADL::SadlValueList,
    SadlStatement,
    sADL::SadlSameAs,
    sADL::SadlDisjointClasses,
    sADL::SadlTypeReference,
    sADL::SadlDifferentFrom,
    sADL::SadlClassOrPropertyDeclaration,
    sADL::SadlNecessaryAndSufficient,
    sADL::SadlResource,
    sADL::SadlProperty,
    sADL::SadlInstance,
    sADL::EObject,
    sADL::SadlModel,
    sADL::Expression,
    AbstractSadlEquation,
    SadlModelElement,
    sADL::ReadStatement,
    sADL::ExternalEquationStatement,
    sADL::StartWriteStatement,
    sADL::SadlStatement,
    sADL::EndWriteStatement,
    sADL::ExplainStatement,
    sADL::PrintStatement,
    sADL::ExpressionScope,
    sADL::EquationStatement,
    sADL::SadlModelElement,
    sADL::SadlImport,
    sADL::SadlAnnotation,
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



def test_sadl::name_is_not_abstract():
    assert not inspect.isabstract(sADL::Name)


def test_sadl::name_constructor_exists():
    assert callable(sADL::Name.__init__)


def test_sadl::name_constructor_args():
    sig = inspect.signature(sADL::Name.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_sadl::name_has_function():
    assert hasattr(sADL::Name, "function")
    descriptor = None
    for klass in sADL::Name.__mro__:
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



def test_sadl::querystatement_is_not_abstract():
    assert not inspect.isabstract(sADL::QueryStatement)


def test_sadl::querystatement_constructor_exists():
    assert callable(sADL::QueryStatement.__init__)


def test_sadl::querystatement_constructor_args():
    sig = inspect.signature(sADL::QueryStatement.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"

def test_sadl::querystatement_has_start():
    assert hasattr(sADL::QueryStatement, "start")
    descriptor = None
    for klass in sADL::QueryStatement.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_sadl::rulestatement_is_not_abstract():
    assert not inspect.isabstract(sADL::RuleStatement)


def test_sadl::rulestatement_constructor_exists():
    assert callable(sADL::RuleStatement.__init__)


def test_sadl::rulestatement_constructor_args():
    sig = inspect.signature(sADL::RuleStatement.__init__)
    params = list(sig.parameters.keys())



def test_sadl::teststatement_is_not_abstract():
    assert not inspect.isabstract(sADL::TestStatement)


def test_sadl::teststatement_constructor_exists():
    assert callable(sADL::TestStatement.__init__)


def test_sadl::teststatement_constructor_args():
    sig = inspect.signature(sADL::TestStatement.__init__)
    params = list(sig.parameters.keys())



def test_sadl::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(sADL::ExpressionStatement)


def test_sadl::expressionstatement_constructor_exists():
    assert callable(sADL::ExpressionStatement.__init__)


def test_sadl::expressionstatement_constructor_args():
    sig = inspect.signature(sADL::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())
    assert "evaluatesTo" in params, "Missing parameter 'evaluatesTo'"

def test_sadl::expressionstatement_has_evaluatesTo():
    assert hasattr(sADL::ExpressionStatement, "evaluatesTo")
    descriptor = None
    for klass in sADL::ExpressionStatement.__mro__:
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



def test_sadl::sadlnestedinstance_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlNestedInstance)


def test_sadl::sadlnestedinstance_constructor_exists():
    assert callable(sADL::SadlNestedInstance.__init__)


def test_sadl::sadlnestedinstance_constructor_args():
    sig = inspect.signature(sADL::SadlNestedInstance.__init__)
    params = list(sig.parameters.keys())
    assert "article" in params, "Missing parameter 'article'"

def test_sadl::sadlnestedinstance_has_article():
    assert hasattr(sADL::SadlNestedInstance, "article")
    descriptor = None
    for klass in sADL::SadlNestedInstance.__mro__:
        if "article" in klass.__dict__:
            descriptor = klass.__dict__["article"]
            break
    assert isinstance(descriptor, property)



def test_sadl::valuerow_is_not_abstract():
    assert not inspect.isabstract(sADL::ValueRow)


def test_sadl::valuerow_constructor_exists():
    assert callable(sADL::ValueRow.__init__)


def test_sadl::valuerow_constructor_args():
    sig = inspect.signature(sADL::ValueRow.__init__)
    params = list(sig.parameters.keys())



def test_sadl::orderelement_is_not_abstract():
    assert not inspect.isabstract(sADL::OrderElement)


def test_sadl::orderelement_constructor_exists():
    assert callable(sADL::OrderElement.__init__)


def test_sadl::orderelement_constructor_args():
    sig = inspect.signature(sADL::OrderElement.__init__)
    params = list(sig.parameters.keys())
    assert "desc" in params, "Missing parameter 'desc'"

def test_sadl::orderelement_has_desc():
    assert hasattr(sADL::OrderElement, "desc")
    descriptor = None
    for klass in sADL::OrderElement.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)



def test_sadl::namedstructureannotation_is_not_abstract():
    assert not inspect.isabstract(sADL::NamedStructureAnnotation)


def test_sadl::namedstructureannotation_constructor_exists():
    assert callable(sADL::NamedStructureAnnotation.__init__)


def test_sadl::namedstructureannotation_constructor_args():
    sig = inspect.signature(sADL::NamedStructureAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_sadlexplicitvalue_is_not_abstract():
    assert not inspect.isabstract(SadlExplicitValue)


def test_sadlexplicitvalue_constructor_exists():
    assert callable(SadlExplicitValue.__init__)


def test_sadlexplicitvalue_constructor_args():
    sig = inspect.signature(SadlExplicitValue.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlunaryexpression_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlUnaryExpression)


def test_sadl::sadlunaryexpression_constructor_exists():
    assert callable(sADL::SadlUnaryExpression.__init__)


def test_sadl::sadlunaryexpression_constructor_args():
    sig = inspect.signature(sADL::SadlUnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_sadl::sadlunaryexpression_has_operator():
    assert hasattr(sADL::SadlUnaryExpression, "operator")
    descriptor = None
    for klass in sADL::SadlUnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadlexplicitvalueliteral_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlExplicitValueLiteral)


def test_sadl::sadlexplicitvalueliteral_constructor_exists():
    assert callable(sADL::SadlExplicitValueLiteral.__init__)


def test_sadl::sadlexplicitvalueliteral_constructor_args():
    sig = inspect.signature(sADL::SadlExplicitValueLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlexplicitvalue_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlExplicitValue)


def test_sadl::sadlexplicitvalue_constructor_exists():
    assert callable(sADL::SadlExplicitValue.__init__)


def test_sadl::sadlexplicitvalue_constructor_args():
    sig = inspect.signature(sADL::SadlExplicitValue.__init__)
    params = list(sig.parameters.keys())



def test_sadlcondition_is_not_abstract():
    assert not inspect.isabstract(SadlCondition)


def test_sadlcondition_constructor_exists():
    assert callable(SadlCondition.__init__)


def test_sadlcondition_constructor_args():
    sig = inspect.signature(SadlCondition.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlcardinalitycondition_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlCardinalityCondition)


def test_sadl::sadlcardinalitycondition_constructor_exists():
    assert callable(sADL::SadlCardinalityCondition.__init__)


def test_sadl::sadlcardinalitycondition_constructor_args():
    sig = inspect.signature(sADL::SadlCardinalityCondition.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_sadl::sadlcardinalitycondition_has_cardinality():
    assert hasattr(sADL::SadlCardinalityCondition, "cardinality")
    descriptor = None
    for klass in sADL::SadlCardinalityCondition.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)

def test_sadl::sadlcardinalitycondition_has_operator():
    assert hasattr(sADL::SadlCardinalityCondition, "operator")
    descriptor = None
    for klass in sADL::SadlCardinalityCondition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadlhasvaluecondition_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlHasValueCondition)


def test_sadl::sadlhasvaluecondition_constructor_exists():
    assert callable(sADL::SadlHasValueCondition.__init__)


def test_sadl::sadlhasvaluecondition_constructor_args():
    sig = inspect.signature(sADL::SadlHasValueCondition.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlallvaluescondition_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlAllValuesCondition)


def test_sadl::sadlallvaluescondition_constructor_exists():
    assert callable(sADL::SadlAllValuesCondition.__init__)


def test_sadl::sadlallvaluescondition_constructor_args():
    sig = inspect.signature(sADL::SadlAllValuesCondition.__init__)
    params = list(sig.parameters.keys())



def test_sadlpropertyrestriction_is_not_abstract():
    assert not inspect.isabstract(SadlPropertyRestriction)


def test_sadlpropertyrestriction_constructor_exists():
    assert callable(SadlPropertyRestriction.__init__)


def test_sadlpropertyrestriction_constructor_args():
    sig = inspect.signature(SadlPropertyRestriction.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlistransitive_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlIsTransitive)


def test_sadl::sadlistransitive_constructor_exists():
    assert callable(sADL::SadlIsTransitive.__init__)


def test_sadl::sadlistransitive_constructor_args():
    sig = inspect.signature(sADL::SadlIsTransitive.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlisannotation_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlIsAnnotation)


def test_sadl::sadlisannotation_constructor_exists():
    assert callable(sADL::SadlIsAnnotation.__init__)


def test_sadl::sadlisannotation_constructor_args():
    sig = inspect.signature(sADL::SadlIsAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlisfunctional_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlIsFunctional)


def test_sadl::sadlisfunctional_constructor_exists():
    assert callable(sADL::SadlIsFunctional.__init__)


def test_sadl::sadlisfunctional_constructor_args():
    sig = inspect.signature(sADL::SadlIsFunctional.__init__)
    params = list(sig.parameters.keys())
    assert "inverse" in params, "Missing parameter 'inverse'"

def test_sadl::sadlisfunctional_has_inverse():
    assert hasattr(sADL::SadlIsFunctional, "inverse")
    descriptor = None
    for klass in sADL::SadlIsFunctional.__mro__:
        if "inverse" in klass.__dict__:
            descriptor = klass.__dict__["inverse"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadlissymmetrical_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlIsSymmetrical)


def test_sadl::sadlissymmetrical_constructor_exists():
    assert callable(sADL::SadlIsSymmetrical.__init__)


def test_sadl::sadlissymmetrical_constructor_args():
    sig = inspect.signature(sADL::SadlIsSymmetrical.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlisinverseof_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlIsInverseOf)


def test_sadl::sadlisinverseof_constructor_exists():
    assert callable(sADL::SadlIsInverseOf.__init__)


def test_sadl::sadlisinverseof_constructor_args():
    sig = inspect.signature(sADL::SadlIsInverseOf.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadltypeassociation_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlTypeAssociation)


def test_sadl::sadltypeassociation_constructor_exists():
    assert callable(sADL::SadlTypeAssociation.__init__)


def test_sadl::sadltypeassociation_constructor_args():
    sig = inspect.signature(sADL::SadlTypeAssociation.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadldefaultvalue_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlDefaultValue)


def test_sadl::sadldefaultvalue_constructor_exists():
    assert callable(sADL::SadlDefaultValue.__init__)


def test_sadl::sadldefaultvalue_constructor_args():
    sig = inspect.signature(sADL::SadlDefaultValue.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_sadl::sadldefaultvalue_has_level():
    assert hasattr(sADL::SadlDefaultValue, "level")
    descriptor = None
    for klass in sADL::SadlDefaultValue.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadlmustbeoneof_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlMustBeOneOf)


def test_sadl::sadlmustbeoneof_constructor_exists():
    assert callable(sADL::SadlMustBeOneOf.__init__)


def test_sadl::sadlmustbeoneof_constructor_args():
    sig = inspect.signature(sADL::SadlMustBeOneOf.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlcanonlybeoneof_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlCanOnlyBeOneOf)


def test_sadl::sadlcanonlybeoneof_constructor_exists():
    assert callable(sADL::SadlCanOnlyBeOneOf.__init__)


def test_sadl::sadlcanonlybeoneof_constructor_args():
    sig = inspect.signature(sADL::SadlCanOnlyBeOneOf.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlrangerestriction_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlRangeRestriction)


def test_sadl::sadlrangerestriction_constructor_exists():
    assert callable(sADL::SadlRangeRestriction.__init__)


def test_sadl::sadlrangerestriction_constructor_args():
    sig = inspect.signature(sADL::SadlRangeRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "singleValued" in params, "Missing parameter 'singleValued'"
    assert "typeonly" in params, "Missing parameter 'typeonly'"

def test_sadl::sadlrangerestriction_has_singleValued():
    assert hasattr(sADL::SadlRangeRestriction, "singleValued")
    descriptor = None
    for klass in sADL::SadlRangeRestriction.__mro__:
        if "singleValued" in klass.__dict__:
            descriptor = klass.__dict__["singleValued"]
            break
    assert isinstance(descriptor, property)

def test_sadl::sadlrangerestriction_has_typeonly():
    assert hasattr(sADL::SadlRangeRestriction, "typeonly")
    descriptor = None
    for klass in sADL::SadlRangeRestriction.__mro__:
        if "typeonly" in klass.__dict__:
            descriptor = klass.__dict__["typeonly"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadldatatypefacet_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlDataTypeFacet)


def test_sadl::sadldatatypefacet_constructor_exists():
    assert callable(sADL::SadlDataTypeFacet.__init__)


def test_sadl::sadldatatypefacet_constructor_args():
    sig = inspect.signature(sADL::SadlDataTypeFacet.__init__)
    params = list(sig.parameters.keys())
    assert "minlen" in params, "Missing parameter 'minlen'"
    assert "min" in params, "Missing parameter 'min'"
    assert "maxInclusive" in params, "Missing parameter 'maxInclusive'"
    assert "len" in params, "Missing parameter 'len'"
    assert "minInclusive" in params, "Missing parameter 'minInclusive'"
    assert "regex" in params, "Missing parameter 'regex'"
    assert "values" in params, "Missing parameter 'values'"
    assert "maxlen" in params, "Missing parameter 'maxlen'"
    assert "max" in params, "Missing parameter 'max'"

def test_sadl::sadldatatypefacet_has_minlen():
    assert hasattr(sADL::SadlDataTypeFacet, "minlen")
    descriptor = None
    for klass in sADL::SadlDataTypeFacet.__mro__:
        if "minlen" in klass.__dict__:
            descriptor = klass.__dict__["minlen"]
            break
    assert isinstance(descriptor, property)

def test_sadl::sadldatatypefacet_has_min():
    assert hasattr(sADL::SadlDataTypeFacet, "min")
    descriptor = None
    for klass in sADL::SadlDataTypeFacet.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_sadl::sadldatatypefacet_has_maxInclusive():
    assert hasattr(sADL::SadlDataTypeFacet, "maxInclusive")
    descriptor = None
    for klass in sADL::SadlDataTypeFacet.__mro__:
        if "maxInclusive" in klass.__dict__:
            descriptor = klass.__dict__["maxInclusive"]
            break
    assert isinstance(descriptor, property)

def test_sadl::sadldatatypefacet_has_len():
    assert hasattr(sADL::SadlDataTypeFacet, "len")
    descriptor = None
    for klass in sADL::SadlDataTypeFacet.__mro__:
        if "len" in klass.__dict__:
            descriptor = klass.__dict__["len"]
            break
    assert isinstance(descriptor, property)

def test_sadl::sadldatatypefacet_has_minInclusive():
    assert hasattr(sADL::SadlDataTypeFacet, "minInclusive")
    descriptor = None
    for klass in sADL::SadlDataTypeFacet.__mro__:
        if "minInclusive" in klass.__dict__:
            descriptor = klass.__dict__["minInclusive"]
            break
    assert isinstance(descriptor, property)

def test_sadl::sadldatatypefacet_has_regex():
    assert hasattr(sADL::SadlDataTypeFacet, "regex")
    descriptor = None
    for klass in sADL::SadlDataTypeFacet.__mro__:
        if "regex" in klass.__dict__:
            descriptor = klass.__dict__["regex"]
            break
    assert isinstance(descriptor, property)

def test_sadl::sadldatatypefacet_has_values():
    assert hasattr(sADL::SadlDataTypeFacet, "values")
    descriptor = None
    for klass in sADL::SadlDataTypeFacet.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)

def test_sadl::sadldatatypefacet_has_maxlen():
    assert hasattr(sADL::SadlDataTypeFacet, "maxlen")
    descriptor = None
    for klass in sADL::SadlDataTypeFacet.__mro__:
        if "maxlen" in klass.__dict__:
            descriptor = klass.__dict__["maxlen"]
            break
    assert isinstance(descriptor, property)

def test_sadl::sadldatatypefacet_has_max():
    assert hasattr(sADL::SadlDataTypeFacet, "max")
    descriptor = None
    for klass in sADL::SadlDataTypeFacet.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadlpropertyrestriction_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlPropertyRestriction)


def test_sadl::sadlpropertyrestriction_constructor_exists():
    assert callable(sADL::SadlPropertyRestriction.__init__)


def test_sadl::sadlpropertyrestriction_constructor_args():
    sig = inspect.signature(sADL::SadlPropertyRestriction.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlpropertyinitializer_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlPropertyInitializer)


def test_sadl::sadlpropertyinitializer_constructor_exists():
    assert callable(sADL::SadlPropertyInitializer.__init__)


def test_sadl::sadlpropertyinitializer_constructor_args():
    sig = inspect.signature(sADL::SadlPropertyInitializer.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlcondition_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlCondition)


def test_sadl::sadlcondition_constructor_exists():
    assert callable(sADL::SadlCondition.__init__)


def test_sadl::sadlcondition_constructor_args():
    sig = inspect.signature(sADL::SadlCondition.__init__)
    params = list(sig.parameters.keys())



def test_sadltypereference_is_not_abstract():
    assert not inspect.isabstract(SadlTypeReference)


def test_sadltypereference_constructor_exists():
    assert callable(SadlTypeReference.__init__)


def test_sadltypereference_constructor_args():
    sig = inspect.signature(SadlTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlintersectiontype_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlIntersectionType)


def test_sadl::sadlintersectiontype_constructor_exists():
    assert callable(sADL::SadlIntersectionType.__init__)


def test_sadl::sadlintersectiontype_constructor_args():
    sig = inspect.signature(sADL::SadlIntersectionType.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlprimitivedatatype_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlPrimitiveDataType)


def test_sadl::sadlprimitivedatatype_constructor_exists():
    assert callable(sADL::SadlPrimitiveDataType.__init__)


def test_sadl::sadlprimitivedatatype_constructor_args():
    sig = inspect.signature(sADL::SadlPrimitiveDataType.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"
    assert "list" in params, "Missing parameter 'list'"

def test_sadl::sadlprimitivedatatype_has_primitiveType():
    assert hasattr(sADL::SadlPrimitiveDataType, "primitiveType")
    descriptor = None
    for klass in sADL::SadlPrimitiveDataType.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)

def test_sadl::sadlprimitivedatatype_has_list():
    assert hasattr(sADL::SadlPrimitiveDataType, "list")
    descriptor = None
    for klass in sADL::SadlPrimitiveDataType.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadlsimpletypereference_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlSimpleTypeReference)


def test_sadl::sadlsimpletypereference_constructor_exists():
    assert callable(sADL::SadlSimpleTypeReference.__init__)


def test_sadl::sadlsimpletypereference_constructor_args():
    sig = inspect.signature(sADL::SadlSimpleTypeReference.__init__)
    params = list(sig.parameters.keys())
    assert "list" in params, "Missing parameter 'list'"

def test_sadl::sadlsimpletypereference_has_list():
    assert hasattr(sADL::SadlSimpleTypeReference, "list")
    descriptor = None
    for klass in sADL::SadlSimpleTypeReference.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadluniontype_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlUnionType)


def test_sadl::sadluniontype_constructor_exists():
    assert callable(sADL::SadlUnionType.__init__)


def test_sadl::sadluniontype_constructor_args():
    sig = inspect.signature(sADL::SadlUnionType.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlpropertycondition_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlPropertyCondition)


def test_sadl::sadlpropertycondition_constructor_exists():
    assert callable(sADL::SadlPropertyCondition.__init__)


def test_sadl::sadlpropertycondition_constructor_args():
    sig = inspect.signature(sADL::SadlPropertyCondition.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlParameterDeclaration)


def test_sadl::sadlparameterdeclaration_constructor_exists():
    assert callable(sADL::SadlParameterDeclaration.__init__)


def test_sadl::sadlparameterdeclaration_constructor_args():
    sig = inspect.signature(sADL::SadlParameterDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "ellipsis" in params, "Missing parameter 'ellipsis'"
    assert "unknown" in params, "Missing parameter 'unknown'"

def test_sadl::sadlparameterdeclaration_has_ellipsis():
    assert hasattr(sADL::SadlParameterDeclaration, "ellipsis")
    descriptor = None
    for klass in sADL::SadlParameterDeclaration.__mro__:
        if "ellipsis" in klass.__dict__:
            descriptor = klass.__dict__["ellipsis"]
            break
    assert isinstance(descriptor, property)

def test_sadl::sadlparameterdeclaration_has_unknown():
    assert hasattr(sADL::SadlParameterDeclaration, "unknown")
    descriptor = None
    for klass in sADL::SadlParameterDeclaration.__mro__:
        if "unknown" in klass.__dict__:
            descriptor = klass.__dict__["unknown"]
            break
    assert isinstance(descriptor, property)



def test_sadl::abstractsadlequation_is_not_abstract():
    assert not inspect.isabstract(sADL::AbstractSadlEquation)


def test_sadl::abstractsadlequation_constructor_exists():
    assert callable(sADL::AbstractSadlEquation.__init__)


def test_sadl::abstractsadlequation_constructor_args():
    sig = inspect.signature(sADL::AbstractSadlEquation.__init__)
    params = list(sig.parameters.keys())
    assert "unknown" in params, "Missing parameter 'unknown'"

def test_sadl::abstractsadlequation_has_unknown():
    assert hasattr(sADL::AbstractSadlEquation, "unknown")
    descriptor = None
    for klass in sADL::AbstractSadlEquation.__mro__:
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



def test_sadl::binaryoperation_is_not_abstract():
    assert not inspect.isabstract(sADL::BinaryOperation)


def test_sadl::binaryoperation_constructor_exists():
    assert callable(sADL::BinaryOperation.__init__)


def test_sadl::binaryoperation_constructor_args():
    sig = inspect.signature(sADL::BinaryOperation.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sadl::binaryoperation_has_op():
    assert hasattr(sADL::BinaryOperation, "op")
    descriptor = None
    for klass in sADL::BinaryOperation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sadl::declaration_is_not_abstract():
    assert not inspect.isabstract(sADL::Declaration)


def test_sadl::declaration_constructor_exists():
    assert callable(sADL::Declaration.__init__)


def test_sadl::declaration_constructor_args():
    sig = inspect.signature(sADL::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "maxlen" in params, "Missing parameter 'maxlen'"
    assert "len" in params, "Missing parameter 'len'"
    assert "article" in params, "Missing parameter 'article'"
    assert "ordinal" in params, "Missing parameter 'ordinal'"

def test_sadl::declaration_has_maxlen():
    assert hasattr(sADL::Declaration, "maxlen")
    descriptor = None
    for klass in sADL::Declaration.__mro__:
        if "maxlen" in klass.__dict__:
            descriptor = klass.__dict__["maxlen"]
            break
    assert isinstance(descriptor, property)

def test_sadl::declaration_has_len():
    assert hasattr(sADL::Declaration, "len")
    descriptor = None
    for klass in sADL::Declaration.__mro__:
        if "len" in klass.__dict__:
            descriptor = klass.__dict__["len"]
            break
    assert isinstance(descriptor, property)

def test_sadl::declaration_has_article():
    assert hasattr(sADL::Declaration, "article")
    descriptor = None
    for klass in sADL::Declaration.__mro__:
        if "article" in klass.__dict__:
            descriptor = klass.__dict__["article"]
            break
    assert isinstance(descriptor, property)

def test_sadl::declaration_has_ordinal():
    assert hasattr(sADL::Declaration, "ordinal")
    descriptor = None
    for klass in sADL::Declaration.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)



def test_sadl::constructexpression_is_not_abstract():
    assert not inspect.isabstract(sADL::ConstructExpression)


def test_sadl::constructexpression_constructor_exists():
    assert callable(sADL::ConstructExpression.__init__)


def test_sadl::constructexpression_constructor_args():
    sig = inspect.signature(sADL::ConstructExpression.__init__)
    params = list(sig.parameters.keys())



def test_sadl::valuetable_is_not_abstract():
    assert not inspect.isabstract(sADL::ValueTable)


def test_sadl::valuetable_constructor_exists():
    assert callable(sADL::ValueTable.__init__)


def test_sadl::valuetable_constructor_args():
    sig = inspect.signature(sADL::ValueTable.__init__)
    params = list(sig.parameters.keys())



def test_sadl::subjhasprop_is_not_abstract():
    assert not inspect.isabstract(sADL::SubjHasProp)


def test_sadl::subjhasprop_constructor_exists():
    assert callable(sADL::SubjHasProp.__init__)


def test_sadl::subjhasprop_constructor_args():
    sig = inspect.signature(sADL::SubjHasProp.__init__)
    params = list(sig.parameters.keys())
    assert "comma" in params, "Missing parameter 'comma'"

def test_sadl::subjhasprop_has_comma():
    assert hasattr(sADL::SubjHasProp, "comma")
    descriptor = None
    for klass in sADL::SubjHasProp.__mro__:
        if "comma" in klass.__dict__:
            descriptor = klass.__dict__["comma"]
            break
    assert isinstance(descriptor, property)



def test_sadl::unitexpression_is_not_abstract():
    assert not inspect.isabstract(sADL::UnitExpression)


def test_sadl::unitexpression_constructor_exists():
    assert callable(sADL::UnitExpression.__init__)


def test_sadl::unitexpression_constructor_args():
    sig = inspect.signature(sADL::UnitExpression.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_sadl::unitexpression_has_unit():
    assert hasattr(sADL::UnitExpression, "unit")
    descriptor = None
    for klass in sADL::UnitExpression.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_sadl::numberliteral_is_not_abstract():
    assert not inspect.isabstract(sADL::NumberLiteral)


def test_sadl::numberliteral_constructor_exists():
    assert callable(sADL::NumberLiteral.__init__)


def test_sadl::numberliteral_constructor_args():
    sig = inspect.signature(sADL::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sadl::numberliteral_has_value():
    assert hasattr(sADL::NumberLiteral, "value")
    descriptor = None
    for klass in sADL::NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sadl::stringliteral_is_not_abstract():
    assert not inspect.isabstract(sADL::StringLiteral)


def test_sadl::stringliteral_constructor_exists():
    assert callable(sADL::StringLiteral.__init__)


def test_sadl::stringliteral_constructor_args():
    sig = inspect.signature(sADL::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sadl::stringliteral_has_value():
    assert hasattr(sADL::StringLiteral, "value")
    descriptor = None
    for klass in sADL::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sadl::selectexpression_is_not_abstract():
    assert not inspect.isabstract(sADL::SelectExpression)


def test_sadl::selectexpression_constructor_exists():
    assert callable(sADL::SelectExpression.__init__)


def test_sadl::selectexpression_constructor_args():
    sig = inspect.signature(sADL::SelectExpression.__init__)
    params = list(sig.parameters.keys())
    assert "orderby" in params, "Missing parameter 'orderby'"
    assert "distinct" in params, "Missing parameter 'distinct'"

def test_sadl::selectexpression_has_orderby():
    assert hasattr(sADL::SelectExpression, "orderby")
    descriptor = None
    for klass in sADL::SelectExpression.__mro__:
        if "orderby" in klass.__dict__:
            descriptor = klass.__dict__["orderby"]
            break
    assert isinstance(descriptor, property)

def test_sadl::selectexpression_has_distinct():
    assert hasattr(sADL::SelectExpression, "distinct")
    descriptor = None
    for klass in sADL::SelectExpression.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)



def test_sadl::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(sADL::UnaryExpression)


def test_sadl::unaryexpression_constructor_exists():
    assert callable(sADL::UnaryExpression.__init__)


def test_sadl::unaryexpression_constructor_args():
    sig = inspect.signature(sADL::UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sadl::unaryexpression_has_op():
    assert hasattr(sADL::UnaryExpression, "op")
    descriptor = None
    for klass in sADL::UnaryExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sadl::constant_is_not_abstract():
    assert not inspect.isabstract(sADL::Constant)


def test_sadl::constant_constructor_exists():
    assert callable(sADL::Constant.__init__)


def test_sadl::constant_constructor_args():
    sig = inspect.signature(sADL::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"

def test_sadl::constant_has_constant():
    assert hasattr(sADL::Constant, "constant")
    descriptor = None
    for klass in sADL::Constant.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_sadl::propofsubject_is_not_abstract():
    assert not inspect.isabstract(sADL::PropOfSubject)


def test_sadl::propofsubject_constructor_exists():
    assert callable(sADL::PropOfSubject.__init__)


def test_sadl::propofsubject_constructor_args():
    sig = inspect.signature(sADL::PropOfSubject.__init__)
    params = list(sig.parameters.keys())
    assert "of" in params, "Missing parameter 'of'"

def test_sadl::propofsubject_has_of():
    assert hasattr(sADL::PropOfSubject, "of")
    descriptor = None
    for klass in sADL::PropOfSubject.__mro__:
        if "of" in klass.__dict__:
            descriptor = klass.__dict__["of"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sublist_is_not_abstract():
    assert not inspect.isabstract(sADL::Sublist)


def test_sadl::sublist_constructor_exists():
    assert callable(sADL::Sublist.__init__)


def test_sadl::sublist_constructor_args():
    sig = inspect.signature(sADL::Sublist.__init__)
    params = list(sig.parameters.keys())



def test_sadl::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(sADL::BooleanLiteral)


def test_sadl::booleanliteral_constructor_exists():
    assert callable(sADL::BooleanLiteral.__init__)


def test_sadl::booleanliteral_constructor_args():
    sig = inspect.signature(sADL::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sadl::booleanliteral_has_value():
    assert hasattr(sADL::BooleanLiteral, "value")
    descriptor = None
    for klass in sADL::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sadl::elementinlist_is_not_abstract():
    assert not inspect.isabstract(sADL::ElementInList)


def test_sadl::elementinlist_constructor_exists():
    assert callable(sADL::ElementInList.__init__)


def test_sadl::elementinlist_constructor_args():
    sig = inspect.signature(sADL::ElementInList.__init__)
    params = list(sig.parameters.keys())
    assert "after" in params, "Missing parameter 'after'"
    assert "before" in params, "Missing parameter 'before'"

def test_sadl::elementinlist_has_after():
    assert hasattr(sADL::ElementInList, "after")
    descriptor = None
    for klass in sADL::ElementInList.__mro__:
        if "after" in klass.__dict__:
            descriptor = klass.__dict__["after"]
            break
    assert isinstance(descriptor, property)

def test_sadl::elementinlist_has_before():
    assert hasattr(sADL::ElementInList, "before")
    descriptor = None
    for klass in sADL::ElementInList.__mro__:
        if "before" in klass.__dict__:
            descriptor = klass.__dict__["before"]
            break
    assert isinstance(descriptor, property)



def test_sadl::askexpression_is_not_abstract():
    assert not inspect.isabstract(sADL::AskExpression)


def test_sadl::askexpression_constructor_exists():
    assert callable(sADL::AskExpression.__init__)


def test_sadl::askexpression_constructor_args():
    sig = inspect.signature(sADL::AskExpression.__init__)
    params = list(sig.parameters.keys())



def test_sadlexplicitvalueliteral_is_not_abstract():
    assert not inspect.isabstract(SadlExplicitValueLiteral)


def test_sadlexplicitvalueliteral_constructor_exists():
    assert callable(SadlExplicitValueLiteral.__init__)


def test_sadlexplicitvalueliteral_constructor_args():
    sig = inspect.signature(SadlExplicitValueLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlstringliteral_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlStringLiteral)


def test_sadl::sadlstringliteral_constructor_exists():
    assert callable(sADL::SadlStringLiteral.__init__)


def test_sadl::sadlstringliteral_constructor_args():
    sig = inspect.signature(sADL::SadlStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literalString" in params, "Missing parameter 'literalString'"

def test_sadl::sadlstringliteral_has_literalString():
    assert hasattr(sADL::SadlStringLiteral, "literalString")
    descriptor = None
    for klass in sADL::SadlStringLiteral.__mro__:
        if "literalString" in klass.__dict__:
            descriptor = klass.__dict__["literalString"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadlconstantliteral_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlConstantLiteral)


def test_sadl::sadlconstantliteral_constructor_exists():
    assert callable(sADL::SadlConstantLiteral.__init__)


def test_sadl::sadlconstantliteral_constructor_args():
    sig = inspect.signature(sADL::SadlConstantLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "term" in params, "Missing parameter 'term'"

def test_sadl::sadlconstantliteral_has_term():
    assert hasattr(sADL::SadlConstantLiteral, "term")
    descriptor = None
    for klass in sADL::SadlConstantLiteral.__mro__:
        if "term" in klass.__dict__:
            descriptor = klass.__dict__["term"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadlnumberliteral_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlNumberLiteral)


def test_sadl::sadlnumberliteral_constructor_exists():
    assert callable(sADL::SadlNumberLiteral.__init__)


def test_sadl::sadlnumberliteral_constructor_args():
    sig = inspect.signature(sADL::SadlNumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literalNumber" in params, "Missing parameter 'literalNumber'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_sadl::sadlnumberliteral_has_literalNumber():
    assert hasattr(sADL::SadlNumberLiteral, "literalNumber")
    descriptor = None
    for klass in sADL::SadlNumberLiteral.__mro__:
        if "literalNumber" in klass.__dict__:
            descriptor = klass.__dict__["literalNumber"]
            break
    assert isinstance(descriptor, property)

def test_sadl::sadlnumberliteral_has_unit():
    assert hasattr(sADL::SadlNumberLiteral, "unit")
    descriptor = None
    for klass in sADL::SadlNumberLiteral.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadlbooleanliteral_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlBooleanLiteral)


def test_sadl::sadlbooleanliteral_constructor_exists():
    assert callable(sADL::SadlBooleanLiteral.__init__)


def test_sadl::sadlbooleanliteral_constructor_args():
    sig = inspect.signature(sADL::SadlBooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "truethy" in params, "Missing parameter 'truethy'"

def test_sadl::sadlbooleanliteral_has_truethy():
    assert hasattr(sADL::SadlBooleanLiteral, "truethy")
    descriptor = None
    for klass in sADL::SadlBooleanLiteral.__mro__:
        if "truethy" in klass.__dict__:
            descriptor = klass.__dict__["truethy"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadlvaluelist_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlValueList)


def test_sadl::sadlvaluelist_constructor_exists():
    assert callable(sADL::SadlValueList.__init__)


def test_sadl::sadlvaluelist_constructor_args():
    sig = inspect.signature(sADL::SadlValueList.__init__)
    params = list(sig.parameters.keys())



def test_sadlstatement_is_not_abstract():
    assert not inspect.isabstract(SadlStatement)


def test_sadlstatement_constructor_exists():
    assert callable(SadlStatement.__init__)


def test_sadlstatement_constructor_args():
    sig = inspect.signature(SadlStatement.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlsameas_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlSameAs)


def test_sadl::sadlsameas_constructor_exists():
    assert callable(sADL::SadlSameAs.__init__)


def test_sadl::sadlsameas_constructor_args():
    sig = inspect.signature(sADL::SadlSameAs.__init__)
    params = list(sig.parameters.keys())
    assert "complement" in params, "Missing parameter 'complement'"

def test_sadl::sadlsameas_has_complement():
    assert hasattr(sADL::SadlSameAs, "complement")
    descriptor = None
    for klass in sADL::SadlSameAs.__mro__:
        if "complement" in klass.__dict__:
            descriptor = klass.__dict__["complement"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadldisjointclasses_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlDisjointClasses)


def test_sadl::sadldisjointclasses_constructor_exists():
    assert callable(sADL::SadlDisjointClasses.__init__)


def test_sadl::sadldisjointclasses_constructor_args():
    sig = inspect.signature(sADL::SadlDisjointClasses.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadltypereference_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlTypeReference)


def test_sadl::sadltypereference_constructor_exists():
    assert callable(sADL::SadlTypeReference.__init__)


def test_sadl::sadltypereference_constructor_args():
    sig = inspect.signature(sADL::SadlTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadldifferentfrom_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlDifferentFrom)


def test_sadl::sadldifferentfrom_constructor_exists():
    assert callable(sADL::SadlDifferentFrom.__init__)


def test_sadl::sadldifferentfrom_constructor_args():
    sig = inspect.signature(sADL::SadlDifferentFrom.__init__)
    params = list(sig.parameters.keys())
    assert "complement" in params, "Missing parameter 'complement'"

def test_sadl::sadldifferentfrom_has_complement():
    assert hasattr(sADL::SadlDifferentFrom, "complement")
    descriptor = None
    for klass in sADL::SadlDifferentFrom.__mro__:
        if "complement" in klass.__dict__:
            descriptor = klass.__dict__["complement"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadlclassorpropertydeclaration_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlClassOrPropertyDeclaration)


def test_sadl::sadlclassorpropertydeclaration_constructor_exists():
    assert callable(sADL::SadlClassOrPropertyDeclaration.__init__)


def test_sadl::sadlclassorpropertydeclaration_constructor_args():
    sig = inspect.signature(sADL::SadlClassOrPropertyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlnecessaryandsufficient_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlNecessaryAndSufficient)


def test_sadl::sadlnecessaryandsufficient_constructor_exists():
    assert callable(sADL::SadlNecessaryAndSufficient.__init__)


def test_sadl::sadlnecessaryandsufficient_constructor_args():
    sig = inspect.signature(sADL::SadlNecessaryAndSufficient.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlresource_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlResource)


def test_sadl::sadlresource_constructor_exists():
    assert callable(sADL::SadlResource.__init__)


def test_sadl::sadlresource_constructor_args():
    sig = inspect.signature(sADL::SadlResource.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlproperty_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlProperty)


def test_sadl::sadlproperty_constructor_exists():
    assert callable(sADL::SadlProperty.__init__)


def test_sadl::sadlproperty_constructor_args():
    sig = inspect.signature(sADL::SadlProperty.__init__)
    params = list(sig.parameters.keys())
    assert "primaryDeclaration" in params, "Missing parameter 'primaryDeclaration'"

def test_sadl::sadlproperty_has_primaryDeclaration():
    assert hasattr(sADL::SadlProperty, "primaryDeclaration")
    descriptor = None
    for klass in sADL::SadlProperty.__mro__:
        if "primaryDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["primaryDeclaration"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadlinstance_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlInstance)


def test_sadl::sadlinstance_constructor_exists():
    assert callable(sADL::SadlInstance.__init__)


def test_sadl::sadlinstance_constructor_args():
    sig = inspect.signature(sADL::SadlInstance.__init__)
    params = list(sig.parameters.keys())



def test_sadl::eobject_is_not_abstract():
    assert not inspect.isabstract(sADL::EObject)


def test_sadl::eobject_constructor_exists():
    assert callable(sADL::EObject.__init__)


def test_sadl::eobject_constructor_args():
    sig = inspect.signature(sADL::EObject.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlmodel_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlModel)


def test_sadl::sadlmodel_constructor_exists():
    assert callable(sADL::SadlModel.__init__)


def test_sadl::sadlmodel_constructor_args():
    sig = inspect.signature(sADL::SadlModel.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "baseUri" in params, "Missing parameter 'baseUri'"
    assert "version" in params, "Missing parameter 'version'"

def test_sadl::sadlmodel_has_alias():
    assert hasattr(sADL::SadlModel, "alias")
    descriptor = None
    for klass in sADL::SadlModel.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_sadl::sadlmodel_has_baseUri():
    assert hasattr(sADL::SadlModel, "baseUri")
    descriptor = None
    for klass in sADL::SadlModel.__mro__:
        if "baseUri" in klass.__dict__:
            descriptor = klass.__dict__["baseUri"]
            break
    assert isinstance(descriptor, property)

def test_sadl::sadlmodel_has_version():
    assert hasattr(sADL::SadlModel, "version")
    descriptor = None
    for klass in sADL::SadlModel.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_sadl::expression_is_not_abstract():
    assert not inspect.isabstract(sADL::Expression)


def test_sadl::expression_constructor_exists():
    assert callable(sADL::Expression.__init__)


def test_sadl::expression_constructor_args():
    sig = inspect.signature(sADL::Expression.__init__)
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



def test_sadl::readstatement_is_not_abstract():
    assert not inspect.isabstract(sADL::ReadStatement)


def test_sadl::readstatement_constructor_exists():
    assert callable(sADL::ReadStatement.__init__)


def test_sadl::readstatement_constructor_args():
    sig = inspect.signature(sADL::ReadStatement.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"
    assert "templateFilename" in params, "Missing parameter 'templateFilename'"

def test_sadl::readstatement_has_filename():
    assert hasattr(sADL::ReadStatement, "filename")
    descriptor = None
    for klass in sADL::ReadStatement.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_sadl::readstatement_has_templateFilename():
    assert hasattr(sADL::ReadStatement, "templateFilename")
    descriptor = None
    for klass in sADL::ReadStatement.__mro__:
        if "templateFilename" in klass.__dict__:
            descriptor = klass.__dict__["templateFilename"]
            break
    assert isinstance(descriptor, property)



def test_sadl::externalequationstatement_is_not_abstract():
    assert not inspect.isabstract(sADL::ExternalEquationStatement)


def test_sadl::externalequationstatement_constructor_exists():
    assert callable(sADL::ExternalEquationStatement.__init__)


def test_sadl::externalequationstatement_constructor_args():
    sig = inspect.signature(sADL::ExternalEquationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "uri" in params, "Missing parameter 'uri'"

def test_sadl::externalequationstatement_has_location():
    assert hasattr(sADL::ExternalEquationStatement, "location")
    descriptor = None
    for klass in sADL::ExternalEquationStatement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_sadl::externalequationstatement_has_uri():
    assert hasattr(sADL::ExternalEquationStatement, "uri")
    descriptor = None
    for klass in sADL::ExternalEquationStatement.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_sadl::startwritestatement_is_not_abstract():
    assert not inspect.isabstract(sADL::StartWriteStatement)


def test_sadl::startwritestatement_constructor_exists():
    assert callable(sADL::StartWriteStatement.__init__)


def test_sadl::startwritestatement_constructor_args():
    sig = inspect.signature(sADL::StartWriteStatement.__init__)
    params = list(sig.parameters.keys())
    assert "dataOnly" in params, "Missing parameter 'dataOnly'"
    assert "write" in params, "Missing parameter 'write'"

def test_sadl::startwritestatement_has_dataOnly():
    assert hasattr(sADL::StartWriteStatement, "dataOnly")
    descriptor = None
    for klass in sADL::StartWriteStatement.__mro__:
        if "dataOnly" in klass.__dict__:
            descriptor = klass.__dict__["dataOnly"]
            break
    assert isinstance(descriptor, property)

def test_sadl::startwritestatement_has_write():
    assert hasattr(sADL::StartWriteStatement, "write")
    descriptor = None
    for klass in sADL::StartWriteStatement.__mro__:
        if "write" in klass.__dict__:
            descriptor = klass.__dict__["write"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadlstatement_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlStatement)


def test_sadl::sadlstatement_constructor_exists():
    assert callable(sADL::SadlStatement.__init__)


def test_sadl::sadlstatement_constructor_args():
    sig = inspect.signature(sADL::SadlStatement.__init__)
    params = list(sig.parameters.keys())



def test_sadl::endwritestatement_is_not_abstract():
    assert not inspect.isabstract(sADL::EndWriteStatement)


def test_sadl::endwritestatement_constructor_exists():
    assert callable(sADL::EndWriteStatement.__init__)


def test_sadl::endwritestatement_constructor_args():
    sig = inspect.signature(sADL::EndWriteStatement.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_sadl::endwritestatement_has_filename():
    assert hasattr(sADL::EndWriteStatement, "filename")
    descriptor = None
    for klass in sADL::EndWriteStatement.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_sadl::explainstatement_is_not_abstract():
    assert not inspect.isabstract(sADL::ExplainStatement)


def test_sadl::explainstatement_constructor_exists():
    assert callable(sADL::ExplainStatement.__init__)


def test_sadl::explainstatement_constructor_args():
    sig = inspect.signature(sADL::ExplainStatement.__init__)
    params = list(sig.parameters.keys())



def test_sadl::printstatement_is_not_abstract():
    assert not inspect.isabstract(sADL::PrintStatement)


def test_sadl::printstatement_constructor_exists():
    assert callable(sADL::PrintStatement.__init__)


def test_sadl::printstatement_constructor_args():
    sig = inspect.signature(sADL::PrintStatement.__init__)
    params = list(sig.parameters.keys())
    assert "model" in params, "Missing parameter 'model'"
    assert "displayString" in params, "Missing parameter 'displayString'"

def test_sadl::printstatement_has_model():
    assert hasattr(sADL::PrintStatement, "model")
    descriptor = None
    for klass in sADL::PrintStatement.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)

def test_sadl::printstatement_has_displayString():
    assert hasattr(sADL::PrintStatement, "displayString")
    descriptor = None
    for klass in sADL::PrintStatement.__mro__:
        if "displayString" in klass.__dict__:
            descriptor = klass.__dict__["displayString"]
            break
    assert isinstance(descriptor, property)



def test_sadl::expressionscope_is_not_abstract():
    assert not inspect.isabstract(sADL::ExpressionScope)


def test_sadl::expressionscope_constructor_exists():
    assert callable(sADL::ExpressionScope.__init__)


def test_sadl::expressionscope_constructor_args():
    sig = inspect.signature(sADL::ExpressionScope.__init__)
    params = list(sig.parameters.keys())



def test_sadl::equationstatement_is_not_abstract():
    assert not inspect.isabstract(sADL::EquationStatement)


def test_sadl::equationstatement_constructor_exists():
    assert callable(sADL::EquationStatement.__init__)


def test_sadl::equationstatement_constructor_args():
    sig = inspect.signature(sADL::EquationStatement.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlmodelelement_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlModelElement)


def test_sadl::sadlmodelelement_constructor_exists():
    assert callable(sADL::SadlModelElement.__init__)


def test_sadl::sadlmodelelement_constructor_args():
    sig = inspect.signature(sADL::SadlModelElement.__init__)
    params = list(sig.parameters.keys())



def test_sadl::sadlimport_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlImport)


def test_sadl::sadlimport_constructor_exists():
    assert callable(sADL::SadlImport.__init__)


def test_sadl::sadlimport_constructor_args():
    sig = inspect.signature(sADL::SadlImport.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_sadl::sadlimport_has_alias():
    assert hasattr(sADL::SadlImport, "alias")
    descriptor = None
    for klass in sADL::SadlImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_sadl::sadlannotation_is_not_abstract():
    assert not inspect.isabstract(sADL::SadlAnnotation)


def test_sadl::sadlannotation_constructor_exists():
    assert callable(sADL::SadlAnnotation.__init__)


def test_sadl::sadlannotation_constructor_args():
    sig = inspect.signature(sADL::SadlAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "contents" in params, "Missing parameter 'contents'"
    assert "type" in params, "Missing parameter 'type'"

def test_sadl::sadlannotation_has_contents():
    assert hasattr(sADL::SadlAnnotation, "contents")
    descriptor = None
    for klass in sADL::SadlAnnotation.__mro__:
        if "contents" in klass.__dict__:
            descriptor = klass.__dict__["contents"]
            break
    assert isinstance(descriptor, property)

def test_sadl::sadlannotation_has_type():
    assert hasattr(sADL::SadlAnnotation, "type")
    descriptor = None
    for klass in sADL::SadlAnnotation.__mro__:
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
        "double",
        "gYearMonth",
        "anySimpleType",
        "gMonthDay",
        "int",
        "anyURI",
        "negativeInteger",
        "unsignedByte",
        "hexBinary",
        "integer",
        "nonNegativeInteger",
        "decimal",
        "float",
        "base64Binary",
        "gYear",
        "unsignedInt",
        "dateTime",
        "gDay",
        "duration",
        "gMonth",
        "time",
        "string",
        "long",
        "boolean",
        "nonPositiveInteger",
        "positiveInteger",
        "byte",
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
sADL::Name_strategy = st.builds(
    sADL::Name,
    function=
        st.booleans()
)
ExpressionScope_strategy = st.builds(
    ExpressionScope,
)
sADL::QueryStatement_strategy = st.builds(
    sADL::QueryStatement,
    start=
        safe_text
)
sADL::RuleStatement_strategy = st.builds(
    sADL::RuleStatement,
)
sADL::TestStatement_strategy = st.builds(
    sADL::TestStatement,
)
sADL::ExpressionStatement_strategy = st.builds(
    sADL::ExpressionStatement,
    evaluatesTo=
        safe_text
)
SadlInstance_strategy = st.builds(
    SadlInstance,
)
sADL::SadlNestedInstance_strategy = st.builds(
    sADL::SadlNestedInstance,
    article=
        safe_text
)
sADL::ValueRow_strategy = st.builds(
    sADL::ValueRow,
)
sADL::OrderElement_strategy = st.builds(
    sADL::OrderElement,
    desc=
        st.booleans()
)
sADL::NamedStructureAnnotation_strategy = st.builds(
    sADL::NamedStructureAnnotation,
)
SadlExplicitValue_strategy = st.builds(
    SadlExplicitValue,
)
sADL::SadlUnaryExpression_strategy = st.builds(
    sADL::SadlUnaryExpression,
    operator=
        safe_text
)
sADL::SadlExplicitValueLiteral_strategy = st.builds(
    sADL::SadlExplicitValueLiteral,
)
sADL::SadlExplicitValue_strategy = st.builds(
    sADL::SadlExplicitValue,
)
SadlCondition_strategy = st.builds(
    SadlCondition,
)
sADL::SadlCardinalityCondition_strategy = st.builds(
    sADL::SadlCardinalityCondition,
    cardinality=
        safe_text,
    operator=
        safe_text
)
sADL::SadlHasValueCondition_strategy = st.builds(
    sADL::SadlHasValueCondition,
)
sADL::SadlAllValuesCondition_strategy = st.builds(
    sADL::SadlAllValuesCondition,
)
SadlPropertyRestriction_strategy = st.builds(
    SadlPropertyRestriction,
)
sADL::SadlIsTransitive_strategy = st.builds(
    sADL::SadlIsTransitive,
)
sADL::SadlIsAnnotation_strategy = st.builds(
    sADL::SadlIsAnnotation,
)
sADL::SadlIsFunctional_strategy = st.builds(
    sADL::SadlIsFunctional,
    inverse=
        st.booleans()
)
sADL::SadlIsSymmetrical_strategy = st.builds(
    sADL::SadlIsSymmetrical,
)
sADL::SadlIsInverseOf_strategy = st.builds(
    sADL::SadlIsInverseOf,
)
sADL::SadlTypeAssociation_strategy = st.builds(
    sADL::SadlTypeAssociation,
)
sADL::SadlDefaultValue_strategy = st.builds(
    sADL::SadlDefaultValue,
    level=
        st.integers()
)
sADL::SadlMustBeOneOf_strategy = st.builds(
    sADL::SadlMustBeOneOf,
)
sADL::SadlCanOnlyBeOneOf_strategy = st.builds(
    sADL::SadlCanOnlyBeOneOf,
)
sADL::SadlRangeRestriction_strategy = st.builds(
    sADL::SadlRangeRestriction,
    singleValued=
        st.booleans(),
    typeonly=
        safe_text
)
sADL::SadlDataTypeFacet_strategy = st.builds(
    sADL::SadlDataTypeFacet,
    minlen=
        safe_text,
    min=
        safe_text,
    maxInclusive=
        st.booleans(),
    len=
        safe_text,
    minInclusive=
        st.booleans(),
    regex=
        safe_text,
    values=
        safe_text,
    maxlen=
        safe_text,
    max=
        safe_text
)
sADL::SadlPropertyRestriction_strategy = st.builds(
    sADL::SadlPropertyRestriction,
)
sADL::SadlPropertyInitializer_strategy = st.builds(
    sADL::SadlPropertyInitializer,
)
sADL::SadlCondition_strategy = st.builds(
    sADL::SadlCondition,
)
SadlTypeReference_strategy = st.builds(
    SadlTypeReference,
)
sADL::SadlIntersectionType_strategy = st.builds(
    sADL::SadlIntersectionType,
)
sADL::SadlPrimitiveDataType_strategy = st.builds(
    sADL::SadlPrimitiveDataType,
    primitiveType=
        safe_text,
    list=
        st.booleans()
)
sADL::SadlSimpleTypeReference_strategy = st.builds(
    sADL::SadlSimpleTypeReference,
    list=
        st.booleans()
)
sADL::SadlUnionType_strategy = st.builds(
    sADL::SadlUnionType,
)
sADL::SadlPropertyCondition_strategy = st.builds(
    sADL::SadlPropertyCondition,
)
sADL::SadlParameterDeclaration_strategy = st.builds(
    sADL::SadlParameterDeclaration,
    ellipsis=
        safe_text,
    unknown=
        safe_text
)
sADL::AbstractSadlEquation_strategy = st.builds(
    sADL::AbstractSadlEquation,
    unknown=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
sADL::BinaryOperation_strategy = st.builds(
    sADL::BinaryOperation,
    op=
        safe_text
)
sADL::Declaration_strategy = st.builds(
    sADL::Declaration,
    maxlen=
        safe_text,
    len=
        safe_text,
    article=
        safe_text,
    ordinal=
        safe_text
)
sADL::ConstructExpression_strategy = st.builds(
    sADL::ConstructExpression,
)
sADL::ValueTable_strategy = st.builds(
    sADL::ValueTable,
)
sADL::SubjHasProp_strategy = st.builds(
    sADL::SubjHasProp,
    comma=
        st.booleans()
)
sADL::UnitExpression_strategy = st.builds(
    sADL::UnitExpression,
    unit=
        safe_text
)
sADL::NumberLiteral_strategy = st.builds(
    sADL::NumberLiteral,
    value=
        safe_text
)
sADL::StringLiteral_strategy = st.builds(
    sADL::StringLiteral,
    value=
        safe_text
)
sADL::SelectExpression_strategy = st.builds(
    sADL::SelectExpression,
    orderby=
        safe_text,
    distinct=
        st.booleans()
)
sADL::UnaryExpression_strategy = st.builds(
    sADL::UnaryExpression,
    op=
        safe_text
)
sADL::Constant_strategy = st.builds(
    sADL::Constant,
    constant=
        safe_text
)
sADL::PropOfSubject_strategy = st.builds(
    sADL::PropOfSubject,
    of=
        safe_text
)
sADL::Sublist_strategy = st.builds(
    sADL::Sublist,
)
sADL::BooleanLiteral_strategy = st.builds(
    sADL::BooleanLiteral,
    value=
        safe_text
)
sADL::ElementInList_strategy = st.builds(
    sADL::ElementInList,
    after=
        st.booleans(),
    before=
        st.booleans()
)
sADL::AskExpression_strategy = st.builds(
    sADL::AskExpression,
)
SadlExplicitValueLiteral_strategy = st.builds(
    SadlExplicitValueLiteral,
)
sADL::SadlStringLiteral_strategy = st.builds(
    sADL::SadlStringLiteral,
    literalString=
        safe_text
)
sADL::SadlConstantLiteral_strategy = st.builds(
    sADL::SadlConstantLiteral,
    term=
        safe_text
)
sADL::SadlNumberLiteral_strategy = st.builds(
    sADL::SadlNumberLiteral,
    literalNumber=
        safe_text,
    unit=
        safe_text
)
sADL::SadlBooleanLiteral_strategy = st.builds(
    sADL::SadlBooleanLiteral,
    truethy=
        st.booleans()
)
sADL::SadlValueList_strategy = st.builds(
    sADL::SadlValueList,
)
SadlStatement_strategy = st.builds(
    SadlStatement,
)
sADL::SadlSameAs_strategy = st.builds(
    sADL::SadlSameAs,
    complement=
        st.booleans()
)
sADL::SadlDisjointClasses_strategy = st.builds(
    sADL::SadlDisjointClasses,
)
sADL::SadlTypeReference_strategy = st.builds(
    sADL::SadlTypeReference,
)
sADL::SadlDifferentFrom_strategy = st.builds(
    sADL::SadlDifferentFrom,
    complement=
        st.booleans()
)
sADL::SadlClassOrPropertyDeclaration_strategy = st.builds(
    sADL::SadlClassOrPropertyDeclaration,
)
sADL::SadlNecessaryAndSufficient_strategy = st.builds(
    sADL::SadlNecessaryAndSufficient,
)
sADL::SadlResource_strategy = st.builds(
    sADL::SadlResource,
)
sADL::SadlProperty_strategy = st.builds(
    sADL::SadlProperty,
    primaryDeclaration=
        st.booleans()
)
sADL::SadlInstance_strategy = st.builds(
    sADL::SadlInstance,
)
sADL::EObject_strategy = st.builds(
    sADL::EObject,
)
sADL::SadlModel_strategy = st.builds(
    sADL::SadlModel,
    alias=
        safe_text,
    baseUri=
        safe_text,
    version=
        safe_text
)
sADL::Expression_strategy = st.builds(
    sADL::Expression,
)
AbstractSadlEquation_strategy = st.builds(
    AbstractSadlEquation,
)
SadlModelElement_strategy = st.builds(
    SadlModelElement,
)
sADL::ReadStatement_strategy = st.builds(
    sADL::ReadStatement,
    filename=
        safe_text,
    templateFilename=
        safe_text
)
sADL::ExternalEquationStatement_strategy = st.builds(
    sADL::ExternalEquationStatement,
    location=
        safe_text,
    uri=
        safe_text
)
sADL::StartWriteStatement_strategy = st.builds(
    sADL::StartWriteStatement,
    dataOnly=
        safe_text,
    write=
        safe_text
)
sADL::SadlStatement_strategy = st.builds(
    sADL::SadlStatement,
)
sADL::EndWriteStatement_strategy = st.builds(
    sADL::EndWriteStatement,
    filename=
        safe_text
)
sADL::ExplainStatement_strategy = st.builds(
    sADL::ExplainStatement,
)
sADL::PrintStatement_strategy = st.builds(
    sADL::PrintStatement,
    model=
        safe_text,
    displayString=
        safe_text
)
sADL::ExpressionScope_strategy = st.builds(
    sADL::ExpressionScope,
)
sADL::EquationStatement_strategy = st.builds(
    sADL::EquationStatement,
)
sADL::SadlModelElement_strategy = st.builds(
    sADL::SadlModelElement,
)
sADL::SadlImport_strategy = st.builds(
    sADL::SadlImport,
    alias=
        safe_text
)
sADL::SadlAnnotation_strategy = st.builds(
    sADL::SadlAnnotation,
    contents=
        safe_text,
    type=
        safe_text
)

@given(instance=SadlResource_strategy)
@settings(max_examples=50)
def test_sadlresource_instantiation(instance):
    assert isinstance(instance, SadlResource)

@given(instance=sADL::Name_strategy)
@settings(max_examples=50)
def test_sadl::name_instantiation(instance):
    assert isinstance(instance, sADL::Name)

@given(instance=sADL::Name_strategy)
def test_sadl::name_function_type(instance):
    assert isinstance(instance.function, bool)


@given(instance=sADL::Name_strategy)
def test_sadl::name_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=ExpressionScope_strategy)
@settings(max_examples=50)
def test_expressionscope_instantiation(instance):
    assert isinstance(instance, ExpressionScope)

@given(instance=sADL::QueryStatement_strategy)
@settings(max_examples=50)
def test_sadl::querystatement_instantiation(instance):
    assert isinstance(instance, sADL::QueryStatement)

@given(instance=sADL::QueryStatement_strategy)
def test_sadl::querystatement_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=sADL::QueryStatement_strategy)
def test_sadl::querystatement_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=sADL::RuleStatement_strategy)
@settings(max_examples=50)
def test_sadl::rulestatement_instantiation(instance):
    assert isinstance(instance, sADL::RuleStatement)

@given(instance=sADL::TestStatement_strategy)
@settings(max_examples=50)
def test_sadl::teststatement_instantiation(instance):
    assert isinstance(instance, sADL::TestStatement)

@given(instance=sADL::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_sadl::expressionstatement_instantiation(instance):
    assert isinstance(instance, sADL::ExpressionStatement)

@given(instance=sADL::ExpressionStatement_strategy)
def test_sadl::expressionstatement_evaluatesTo_type(instance):
    assert isinstance(instance.evaluatesTo, str)


@given(instance=sADL::ExpressionStatement_strategy)
def test_sadl::expressionstatement_evaluatesTo_setter(instance):
    original = instance.evaluatesTo
    instance.evaluatesTo = original
    assert instance.evaluatesTo == original

@given(instance=SadlInstance_strategy)
@settings(max_examples=50)
def test_sadlinstance_instantiation(instance):
    assert isinstance(instance, SadlInstance)

@given(instance=sADL::SadlNestedInstance_strategy)
@settings(max_examples=50)
def test_sadl::sadlnestedinstance_instantiation(instance):
    assert isinstance(instance, sADL::SadlNestedInstance)

@given(instance=sADL::SadlNestedInstance_strategy)
def test_sadl::sadlnestedinstance_article_type(instance):
    assert isinstance(instance.article, str)


@given(instance=sADL::SadlNestedInstance_strategy)
def test_sadl::sadlnestedinstance_article_setter(instance):
    original = instance.article
    instance.article = original
    assert instance.article == original

@given(instance=sADL::ValueRow_strategy)
@settings(max_examples=50)
def test_sadl::valuerow_instantiation(instance):
    assert isinstance(instance, sADL::ValueRow)

@given(instance=sADL::OrderElement_strategy)
@settings(max_examples=50)
def test_sadl::orderelement_instantiation(instance):
    assert isinstance(instance, sADL::OrderElement)

@given(instance=sADL::OrderElement_strategy)
def test_sadl::orderelement_desc_type(instance):
    assert isinstance(instance.desc, bool)


@given(instance=sADL::OrderElement_strategy)
def test_sadl::orderelement_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=sADL::NamedStructureAnnotation_strategy)
@settings(max_examples=50)
def test_sadl::namedstructureannotation_instantiation(instance):
    assert isinstance(instance, sADL::NamedStructureAnnotation)

@given(instance=SadlExplicitValue_strategy)
@settings(max_examples=50)
def test_sadlexplicitvalue_instantiation(instance):
    assert isinstance(instance, SadlExplicitValue)

@given(instance=sADL::SadlUnaryExpression_strategy)
@settings(max_examples=50)
def test_sadl::sadlunaryexpression_instantiation(instance):
    assert isinstance(instance, sADL::SadlUnaryExpression)

@given(instance=sADL::SadlUnaryExpression_strategy)
def test_sadl::sadlunaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=sADL::SadlUnaryExpression_strategy)
def test_sadl::sadlunaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=sADL::SadlExplicitValueLiteral_strategy)
@settings(max_examples=50)
def test_sadl::sadlexplicitvalueliteral_instantiation(instance):
    assert isinstance(instance, sADL::SadlExplicitValueLiteral)

@given(instance=sADL::SadlExplicitValue_strategy)
@settings(max_examples=50)
def test_sadl::sadlexplicitvalue_instantiation(instance):
    assert isinstance(instance, sADL::SadlExplicitValue)

@given(instance=SadlCondition_strategy)
@settings(max_examples=50)
def test_sadlcondition_instantiation(instance):
    assert isinstance(instance, SadlCondition)

@given(instance=sADL::SadlCardinalityCondition_strategy)
@settings(max_examples=50)
def test_sadl::sadlcardinalitycondition_instantiation(instance):
    assert isinstance(instance, sADL::SadlCardinalityCondition)

@given(instance=sADL::SadlCardinalityCondition_strategy)
def test_sadl::sadlcardinalitycondition_cardinality_type(instance):
    assert isinstance(instance.cardinality, str)


@given(instance=sADL::SadlCardinalityCondition_strategy)
def test_sadl::sadlcardinalitycondition_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=sADL::SadlCardinalityCondition_strategy)
def test_sadl::sadlcardinalitycondition_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=sADL::SadlCardinalityCondition_strategy)
def test_sadl::sadlcardinalitycondition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=sADL::SadlHasValueCondition_strategy)
@settings(max_examples=50)
def test_sadl::sadlhasvaluecondition_instantiation(instance):
    assert isinstance(instance, sADL::SadlHasValueCondition)

@given(instance=sADL::SadlAllValuesCondition_strategy)
@settings(max_examples=50)
def test_sadl::sadlallvaluescondition_instantiation(instance):
    assert isinstance(instance, sADL::SadlAllValuesCondition)

@given(instance=SadlPropertyRestriction_strategy)
@settings(max_examples=50)
def test_sadlpropertyrestriction_instantiation(instance):
    assert isinstance(instance, SadlPropertyRestriction)

@given(instance=sADL::SadlIsTransitive_strategy)
@settings(max_examples=50)
def test_sadl::sadlistransitive_instantiation(instance):
    assert isinstance(instance, sADL::SadlIsTransitive)

@given(instance=sADL::SadlIsAnnotation_strategy)
@settings(max_examples=50)
def test_sadl::sadlisannotation_instantiation(instance):
    assert isinstance(instance, sADL::SadlIsAnnotation)

@given(instance=sADL::SadlIsFunctional_strategy)
@settings(max_examples=50)
def test_sadl::sadlisfunctional_instantiation(instance):
    assert isinstance(instance, sADL::SadlIsFunctional)

@given(instance=sADL::SadlIsFunctional_strategy)
def test_sadl::sadlisfunctional_inverse_type(instance):
    assert isinstance(instance.inverse, bool)


@given(instance=sADL::SadlIsFunctional_strategy)
def test_sadl::sadlisfunctional_inverse_setter(instance):
    original = instance.inverse
    instance.inverse = original
    assert instance.inverse == original

@given(instance=sADL::SadlIsSymmetrical_strategy)
@settings(max_examples=50)
def test_sadl::sadlissymmetrical_instantiation(instance):
    assert isinstance(instance, sADL::SadlIsSymmetrical)

@given(instance=sADL::SadlIsInverseOf_strategy)
@settings(max_examples=50)
def test_sadl::sadlisinverseof_instantiation(instance):
    assert isinstance(instance, sADL::SadlIsInverseOf)

@given(instance=sADL::SadlTypeAssociation_strategy)
@settings(max_examples=50)
def test_sadl::sadltypeassociation_instantiation(instance):
    assert isinstance(instance, sADL::SadlTypeAssociation)

@given(instance=sADL::SadlDefaultValue_strategy)
@settings(max_examples=50)
def test_sadl::sadldefaultvalue_instantiation(instance):
    assert isinstance(instance, sADL::SadlDefaultValue)

@given(instance=sADL::SadlDefaultValue_strategy)
def test_sadl::sadldefaultvalue_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=sADL::SadlDefaultValue_strategy)
def test_sadl::sadldefaultvalue_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=sADL::SadlMustBeOneOf_strategy)
@settings(max_examples=50)
def test_sadl::sadlmustbeoneof_instantiation(instance):
    assert isinstance(instance, sADL::SadlMustBeOneOf)

@given(instance=sADL::SadlCanOnlyBeOneOf_strategy)
@settings(max_examples=50)
def test_sadl::sadlcanonlybeoneof_instantiation(instance):
    assert isinstance(instance, sADL::SadlCanOnlyBeOneOf)

@given(instance=sADL::SadlRangeRestriction_strategy)
@settings(max_examples=50)
def test_sadl::sadlrangerestriction_instantiation(instance):
    assert isinstance(instance, sADL::SadlRangeRestriction)

@given(instance=sADL::SadlRangeRestriction_strategy)
def test_sadl::sadlrangerestriction_singleValued_type(instance):
    assert isinstance(instance.singleValued, bool)


@given(instance=sADL::SadlRangeRestriction_strategy)
def test_sadl::sadlrangerestriction_singleValued_setter(instance):
    original = instance.singleValued
    instance.singleValued = original
    assert instance.singleValued == original

@given(instance=sADL::SadlRangeRestriction_strategy)
def test_sadl::sadlrangerestriction_typeonly_type(instance):
    assert isinstance(instance.typeonly, str)


@given(instance=sADL::SadlRangeRestriction_strategy)
def test_sadl::sadlrangerestriction_typeonly_setter(instance):
    original = instance.typeonly
    instance.typeonly = original
    assert instance.typeonly == original

@given(instance=sADL::SadlDataTypeFacet_strategy)
@settings(max_examples=50)
def test_sadl::sadldatatypefacet_instantiation(instance):
    assert isinstance(instance, sADL::SadlDataTypeFacet)

@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_minlen_type(instance):
    assert isinstance(instance.minlen, str)


@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_minlen_setter(instance):
    original = instance.minlen
    instance.minlen = original
    assert instance.minlen == original

@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_maxInclusive_type(instance):
    assert isinstance(instance.maxInclusive, bool)


@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_maxInclusive_setter(instance):
    original = instance.maxInclusive
    instance.maxInclusive = original
    assert instance.maxInclusive == original

@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_len_type(instance):
    assert isinstance(instance.len, str)


@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_len_setter(instance):
    original = instance.len
    instance.len = original
    assert instance.len == original

@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_minInclusive_type(instance):
    assert isinstance(instance.minInclusive, bool)


@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_minInclusive_setter(instance):
    original = instance.minInclusive
    instance.minInclusive = original
    assert instance.minInclusive == original

@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_regex_type(instance):
    assert isinstance(instance.regex, str)


@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_regex_setter(instance):
    original = instance.regex
    instance.regex = original
    assert instance.regex == original

@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_maxlen_type(instance):
    assert isinstance(instance.maxlen, str)


@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_maxlen_setter(instance):
    original = instance.maxlen
    instance.maxlen = original
    assert instance.maxlen == original

@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=sADL::SadlDataTypeFacet_strategy)
def test_sadl::sadldatatypefacet_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=sADL::SadlPropertyRestriction_strategy)
@settings(max_examples=50)
def test_sadl::sadlpropertyrestriction_instantiation(instance):
    assert isinstance(instance, sADL::SadlPropertyRestriction)

@given(instance=sADL::SadlPropertyInitializer_strategy)
@settings(max_examples=50)
def test_sadl::sadlpropertyinitializer_instantiation(instance):
    assert isinstance(instance, sADL::SadlPropertyInitializer)

@given(instance=sADL::SadlCondition_strategy)
@settings(max_examples=50)
def test_sadl::sadlcondition_instantiation(instance):
    assert isinstance(instance, sADL::SadlCondition)

@given(instance=SadlTypeReference_strategy)
@settings(max_examples=50)
def test_sadltypereference_instantiation(instance):
    assert isinstance(instance, SadlTypeReference)

@given(instance=sADL::SadlIntersectionType_strategy)
@settings(max_examples=50)
def test_sadl::sadlintersectiontype_instantiation(instance):
    assert isinstance(instance, sADL::SadlIntersectionType)

@given(instance=sADL::SadlPrimitiveDataType_strategy)
@settings(max_examples=50)
def test_sadl::sadlprimitivedatatype_instantiation(instance):
    assert isinstance(instance, sADL::SadlPrimitiveDataType)

@given(instance=sADL::SadlPrimitiveDataType_strategy)
def test_sadl::sadlprimitivedatatype_primitiveType_type(instance):
    assert isinstance(instance.primitiveType, str)


@given(instance=sADL::SadlPrimitiveDataType_strategy)
def test_sadl::sadlprimitivedatatype_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=sADL::SadlPrimitiveDataType_strategy)
def test_sadl::sadlprimitivedatatype_list_type(instance):
    assert isinstance(instance.list, bool)


@given(instance=sADL::SadlPrimitiveDataType_strategy)
def test_sadl::sadlprimitivedatatype_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=sADL::SadlSimpleTypeReference_strategy)
@settings(max_examples=50)
def test_sadl::sadlsimpletypereference_instantiation(instance):
    assert isinstance(instance, sADL::SadlSimpleTypeReference)

@given(instance=sADL::SadlSimpleTypeReference_strategy)
def test_sadl::sadlsimpletypereference_list_type(instance):
    assert isinstance(instance.list, bool)


@given(instance=sADL::SadlSimpleTypeReference_strategy)
def test_sadl::sadlsimpletypereference_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=sADL::SadlUnionType_strategy)
@settings(max_examples=50)
def test_sadl::sadluniontype_instantiation(instance):
    assert isinstance(instance, sADL::SadlUnionType)

@given(instance=sADL::SadlPropertyCondition_strategy)
@settings(max_examples=50)
def test_sadl::sadlpropertycondition_instantiation(instance):
    assert isinstance(instance, sADL::SadlPropertyCondition)

@given(instance=sADL::SadlParameterDeclaration_strategy)
@settings(max_examples=50)
def test_sadl::sadlparameterdeclaration_instantiation(instance):
    assert isinstance(instance, sADL::SadlParameterDeclaration)

@given(instance=sADL::SadlParameterDeclaration_strategy)
def test_sadl::sadlparameterdeclaration_ellipsis_type(instance):
    assert isinstance(instance.ellipsis, str)


@given(instance=sADL::SadlParameterDeclaration_strategy)
def test_sadl::sadlparameterdeclaration_ellipsis_setter(instance):
    original = instance.ellipsis
    instance.ellipsis = original
    assert instance.ellipsis == original

@given(instance=sADL::SadlParameterDeclaration_strategy)
def test_sadl::sadlparameterdeclaration_unknown_type(instance):
    assert isinstance(instance.unknown, str)


@given(instance=sADL::SadlParameterDeclaration_strategy)
def test_sadl::sadlparameterdeclaration_unknown_setter(instance):
    original = instance.unknown
    instance.unknown = original
    assert instance.unknown == original

@given(instance=sADL::AbstractSadlEquation_strategy)
@settings(max_examples=50)
def test_sadl::abstractsadlequation_instantiation(instance):
    assert isinstance(instance, sADL::AbstractSadlEquation)

@given(instance=sADL::AbstractSadlEquation_strategy)
def test_sadl::abstractsadlequation_unknown_type(instance):
    assert isinstance(instance.unknown, str)


@given(instance=sADL::AbstractSadlEquation_strategy)
def test_sadl::abstractsadlequation_unknown_setter(instance):
    original = instance.unknown
    instance.unknown = original
    assert instance.unknown == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=sADL::BinaryOperation_strategy)
@settings(max_examples=50)
def test_sadl::binaryoperation_instantiation(instance):
    assert isinstance(instance, sADL::BinaryOperation)

@given(instance=sADL::BinaryOperation_strategy)
def test_sadl::binaryoperation_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sADL::BinaryOperation_strategy)
def test_sadl::binaryoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sADL::Declaration_strategy)
@settings(max_examples=50)
def test_sadl::declaration_instantiation(instance):
    assert isinstance(instance, sADL::Declaration)

@given(instance=sADL::Declaration_strategy)
def test_sadl::declaration_maxlen_type(instance):
    assert isinstance(instance.maxlen, str)


@given(instance=sADL::Declaration_strategy)
def test_sadl::declaration_maxlen_setter(instance):
    original = instance.maxlen
    instance.maxlen = original
    assert instance.maxlen == original

@given(instance=sADL::Declaration_strategy)
def test_sadl::declaration_len_type(instance):
    assert isinstance(instance.len, str)


@given(instance=sADL::Declaration_strategy)
def test_sadl::declaration_len_setter(instance):
    original = instance.len
    instance.len = original
    assert instance.len == original

@given(instance=sADL::Declaration_strategy)
def test_sadl::declaration_article_type(instance):
    assert isinstance(instance.article, str)


@given(instance=sADL::Declaration_strategy)
def test_sadl::declaration_article_setter(instance):
    original = instance.article
    instance.article = original
    assert instance.article == original

@given(instance=sADL::Declaration_strategy)
def test_sadl::declaration_ordinal_type(instance):
    assert isinstance(instance.ordinal, str)


@given(instance=sADL::Declaration_strategy)
def test_sadl::declaration_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original

@given(instance=sADL::ConstructExpression_strategy)
@settings(max_examples=50)
def test_sadl::constructexpression_instantiation(instance):
    assert isinstance(instance, sADL::ConstructExpression)

@given(instance=sADL::ValueTable_strategy)
@settings(max_examples=50)
def test_sadl::valuetable_instantiation(instance):
    assert isinstance(instance, sADL::ValueTable)

@given(instance=sADL::SubjHasProp_strategy)
@settings(max_examples=50)
def test_sadl::subjhasprop_instantiation(instance):
    assert isinstance(instance, sADL::SubjHasProp)

@given(instance=sADL::SubjHasProp_strategy)
def test_sadl::subjhasprop_comma_type(instance):
    assert isinstance(instance.comma, bool)


@given(instance=sADL::SubjHasProp_strategy)
def test_sadl::subjhasprop_comma_setter(instance):
    original = instance.comma
    instance.comma = original
    assert instance.comma == original

@given(instance=sADL::UnitExpression_strategy)
@settings(max_examples=50)
def test_sadl::unitexpression_instantiation(instance):
    assert isinstance(instance, sADL::UnitExpression)

@given(instance=sADL::UnitExpression_strategy)
def test_sadl::unitexpression_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=sADL::UnitExpression_strategy)
def test_sadl::unitexpression_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=sADL::NumberLiteral_strategy)
@settings(max_examples=50)
def test_sadl::numberliteral_instantiation(instance):
    assert isinstance(instance, sADL::NumberLiteral)

@given(instance=sADL::NumberLiteral_strategy)
def test_sadl::numberliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sADL::NumberLiteral_strategy)
def test_sadl::numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sADL::StringLiteral_strategy)
@settings(max_examples=50)
def test_sadl::stringliteral_instantiation(instance):
    assert isinstance(instance, sADL::StringLiteral)

@given(instance=sADL::StringLiteral_strategy)
def test_sadl::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sADL::StringLiteral_strategy)
def test_sadl::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sADL::SelectExpression_strategy)
@settings(max_examples=50)
def test_sadl::selectexpression_instantiation(instance):
    assert isinstance(instance, sADL::SelectExpression)

@given(instance=sADL::SelectExpression_strategy)
def test_sadl::selectexpression_orderby_type(instance):
    assert isinstance(instance.orderby, str)


@given(instance=sADL::SelectExpression_strategy)
def test_sadl::selectexpression_orderby_setter(instance):
    original = instance.orderby
    instance.orderby = original
    assert instance.orderby == original

@given(instance=sADL::SelectExpression_strategy)
def test_sadl::selectexpression_distinct_type(instance):
    assert isinstance(instance.distinct, bool)


@given(instance=sADL::SelectExpression_strategy)
def test_sadl::selectexpression_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=sADL::UnaryExpression_strategy)
@settings(max_examples=50)
def test_sadl::unaryexpression_instantiation(instance):
    assert isinstance(instance, sADL::UnaryExpression)

@given(instance=sADL::UnaryExpression_strategy)
def test_sadl::unaryexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sADL::UnaryExpression_strategy)
def test_sadl::unaryexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sADL::Constant_strategy)
@settings(max_examples=50)
def test_sadl::constant_instantiation(instance):
    assert isinstance(instance, sADL::Constant)

@given(instance=sADL::Constant_strategy)
def test_sadl::constant_constant_type(instance):
    assert isinstance(instance.constant, str)


@given(instance=sADL::Constant_strategy)
def test_sadl::constant_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=sADL::PropOfSubject_strategy)
@settings(max_examples=50)
def test_sadl::propofsubject_instantiation(instance):
    assert isinstance(instance, sADL::PropOfSubject)

@given(instance=sADL::PropOfSubject_strategy)
def test_sadl::propofsubject_of_type(instance):
    assert isinstance(instance.of, str)


@given(instance=sADL::PropOfSubject_strategy)
def test_sadl::propofsubject_of_setter(instance):
    original = instance.of
    instance.of = original
    assert instance.of == original

@given(instance=sADL::Sublist_strategy)
@settings(max_examples=50)
def test_sadl::sublist_instantiation(instance):
    assert isinstance(instance, sADL::Sublist)

@given(instance=sADL::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_sadl::booleanliteral_instantiation(instance):
    assert isinstance(instance, sADL::BooleanLiteral)

@given(instance=sADL::BooleanLiteral_strategy)
def test_sadl::booleanliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sADL::BooleanLiteral_strategy)
def test_sadl::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sADL::ElementInList_strategy)
@settings(max_examples=50)
def test_sadl::elementinlist_instantiation(instance):
    assert isinstance(instance, sADL::ElementInList)

@given(instance=sADL::ElementInList_strategy)
def test_sadl::elementinlist_after_type(instance):
    assert isinstance(instance.after, bool)


@given(instance=sADL::ElementInList_strategy)
def test_sadl::elementinlist_after_setter(instance):
    original = instance.after
    instance.after = original
    assert instance.after == original

@given(instance=sADL::ElementInList_strategy)
def test_sadl::elementinlist_before_type(instance):
    assert isinstance(instance.before, bool)


@given(instance=sADL::ElementInList_strategy)
def test_sadl::elementinlist_before_setter(instance):
    original = instance.before
    instance.before = original
    assert instance.before == original

@given(instance=sADL::AskExpression_strategy)
@settings(max_examples=50)
def test_sadl::askexpression_instantiation(instance):
    assert isinstance(instance, sADL::AskExpression)

@given(instance=SadlExplicitValueLiteral_strategy)
@settings(max_examples=50)
def test_sadlexplicitvalueliteral_instantiation(instance):
    assert isinstance(instance, SadlExplicitValueLiteral)

@given(instance=sADL::SadlStringLiteral_strategy)
@settings(max_examples=50)
def test_sadl::sadlstringliteral_instantiation(instance):
    assert isinstance(instance, sADL::SadlStringLiteral)

@given(instance=sADL::SadlStringLiteral_strategy)
def test_sadl::sadlstringliteral_literalString_type(instance):
    assert isinstance(instance.literalString, str)


@given(instance=sADL::SadlStringLiteral_strategy)
def test_sadl::sadlstringliteral_literalString_setter(instance):
    original = instance.literalString
    instance.literalString = original
    assert instance.literalString == original

@given(instance=sADL::SadlConstantLiteral_strategy)
@settings(max_examples=50)
def test_sadl::sadlconstantliteral_instantiation(instance):
    assert isinstance(instance, sADL::SadlConstantLiteral)

@given(instance=sADL::SadlConstantLiteral_strategy)
def test_sadl::sadlconstantliteral_term_type(instance):
    assert isinstance(instance.term, str)


@given(instance=sADL::SadlConstantLiteral_strategy)
def test_sadl::sadlconstantliteral_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original

@given(instance=sADL::SadlNumberLiteral_strategy)
@settings(max_examples=50)
def test_sadl::sadlnumberliteral_instantiation(instance):
    assert isinstance(instance, sADL::SadlNumberLiteral)

@given(instance=sADL::SadlNumberLiteral_strategy)
def test_sadl::sadlnumberliteral_literalNumber_type(instance):
    assert isinstance(instance.literalNumber, str)


@given(instance=sADL::SadlNumberLiteral_strategy)
def test_sadl::sadlnumberliteral_literalNumber_setter(instance):
    original = instance.literalNumber
    instance.literalNumber = original
    assert instance.literalNumber == original

@given(instance=sADL::SadlNumberLiteral_strategy)
def test_sadl::sadlnumberliteral_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=sADL::SadlNumberLiteral_strategy)
def test_sadl::sadlnumberliteral_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=sADL::SadlBooleanLiteral_strategy)
@settings(max_examples=50)
def test_sadl::sadlbooleanliteral_instantiation(instance):
    assert isinstance(instance, sADL::SadlBooleanLiteral)

@given(instance=sADL::SadlBooleanLiteral_strategy)
def test_sadl::sadlbooleanliteral_truethy_type(instance):
    assert isinstance(instance.truethy, bool)


@given(instance=sADL::SadlBooleanLiteral_strategy)
def test_sadl::sadlbooleanliteral_truethy_setter(instance):
    original = instance.truethy
    instance.truethy = original
    assert instance.truethy == original

@given(instance=sADL::SadlValueList_strategy)
@settings(max_examples=50)
def test_sadl::sadlvaluelist_instantiation(instance):
    assert isinstance(instance, sADL::SadlValueList)

@given(instance=SadlStatement_strategy)
@settings(max_examples=50)
def test_sadlstatement_instantiation(instance):
    assert isinstance(instance, SadlStatement)

@given(instance=sADL::SadlSameAs_strategy)
@settings(max_examples=50)
def test_sadl::sadlsameas_instantiation(instance):
    assert isinstance(instance, sADL::SadlSameAs)

@given(instance=sADL::SadlSameAs_strategy)
def test_sadl::sadlsameas_complement_type(instance):
    assert isinstance(instance.complement, bool)


@given(instance=sADL::SadlSameAs_strategy)
def test_sadl::sadlsameas_complement_setter(instance):
    original = instance.complement
    instance.complement = original
    assert instance.complement == original

@given(instance=sADL::SadlDisjointClasses_strategy)
@settings(max_examples=50)
def test_sadl::sadldisjointclasses_instantiation(instance):
    assert isinstance(instance, sADL::SadlDisjointClasses)

@given(instance=sADL::SadlTypeReference_strategy)
@settings(max_examples=50)
def test_sadl::sadltypereference_instantiation(instance):
    assert isinstance(instance, sADL::SadlTypeReference)

@given(instance=sADL::SadlDifferentFrom_strategy)
@settings(max_examples=50)
def test_sadl::sadldifferentfrom_instantiation(instance):
    assert isinstance(instance, sADL::SadlDifferentFrom)

@given(instance=sADL::SadlDifferentFrom_strategy)
def test_sadl::sadldifferentfrom_complement_type(instance):
    assert isinstance(instance.complement, bool)


@given(instance=sADL::SadlDifferentFrom_strategy)
def test_sadl::sadldifferentfrom_complement_setter(instance):
    original = instance.complement
    instance.complement = original
    assert instance.complement == original

@given(instance=sADL::SadlClassOrPropertyDeclaration_strategy)
@settings(max_examples=50)
def test_sadl::sadlclassorpropertydeclaration_instantiation(instance):
    assert isinstance(instance, sADL::SadlClassOrPropertyDeclaration)

@given(instance=sADL::SadlNecessaryAndSufficient_strategy)
@settings(max_examples=50)
def test_sadl::sadlnecessaryandsufficient_instantiation(instance):
    assert isinstance(instance, sADL::SadlNecessaryAndSufficient)

@given(instance=sADL::SadlResource_strategy)
@settings(max_examples=50)
def test_sadl::sadlresource_instantiation(instance):
    assert isinstance(instance, sADL::SadlResource)

@given(instance=sADL::SadlProperty_strategy)
@settings(max_examples=50)
def test_sadl::sadlproperty_instantiation(instance):
    assert isinstance(instance, sADL::SadlProperty)

@given(instance=sADL::SadlProperty_strategy)
def test_sadl::sadlproperty_primaryDeclaration_type(instance):
    assert isinstance(instance.primaryDeclaration, bool)


@given(instance=sADL::SadlProperty_strategy)
def test_sadl::sadlproperty_primaryDeclaration_setter(instance):
    original = instance.primaryDeclaration
    instance.primaryDeclaration = original
    assert instance.primaryDeclaration == original

@given(instance=sADL::SadlInstance_strategy)
@settings(max_examples=50)
def test_sadl::sadlinstance_instantiation(instance):
    assert isinstance(instance, sADL::SadlInstance)

@given(instance=sADL::EObject_strategy)
@settings(max_examples=50)
def test_sadl::eobject_instantiation(instance):
    assert isinstance(instance, sADL::EObject)

@given(instance=sADL::SadlModel_strategy)
@settings(max_examples=50)
def test_sadl::sadlmodel_instantiation(instance):
    assert isinstance(instance, sADL::SadlModel)

@given(instance=sADL::SadlModel_strategy)
def test_sadl::sadlmodel_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=sADL::SadlModel_strategy)
def test_sadl::sadlmodel_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=sADL::SadlModel_strategy)
def test_sadl::sadlmodel_baseUri_type(instance):
    assert isinstance(instance.baseUri, str)


@given(instance=sADL::SadlModel_strategy)
def test_sadl::sadlmodel_baseUri_setter(instance):
    original = instance.baseUri
    instance.baseUri = original
    assert instance.baseUri == original

@given(instance=sADL::SadlModel_strategy)
def test_sadl::sadlmodel_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=sADL::SadlModel_strategy)
def test_sadl::sadlmodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=sADL::Expression_strategy)
@settings(max_examples=50)
def test_sadl::expression_instantiation(instance):
    assert isinstance(instance, sADL::Expression)

@given(instance=AbstractSadlEquation_strategy)
@settings(max_examples=50)
def test_abstractsadlequation_instantiation(instance):
    assert isinstance(instance, AbstractSadlEquation)

@given(instance=SadlModelElement_strategy)
@settings(max_examples=50)
def test_sadlmodelelement_instantiation(instance):
    assert isinstance(instance, SadlModelElement)

@given(instance=sADL::ReadStatement_strategy)
@settings(max_examples=50)
def test_sadl::readstatement_instantiation(instance):
    assert isinstance(instance, sADL::ReadStatement)

@given(instance=sADL::ReadStatement_strategy)
def test_sadl::readstatement_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=sADL::ReadStatement_strategy)
def test_sadl::readstatement_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=sADL::ReadStatement_strategy)
def test_sadl::readstatement_templateFilename_type(instance):
    assert isinstance(instance.templateFilename, str)


@given(instance=sADL::ReadStatement_strategy)
def test_sadl::readstatement_templateFilename_setter(instance):
    original = instance.templateFilename
    instance.templateFilename = original
    assert instance.templateFilename == original

@given(instance=sADL::ExternalEquationStatement_strategy)
@settings(max_examples=50)
def test_sadl::externalequationstatement_instantiation(instance):
    assert isinstance(instance, sADL::ExternalEquationStatement)

@given(instance=sADL::ExternalEquationStatement_strategy)
def test_sadl::externalequationstatement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=sADL::ExternalEquationStatement_strategy)
def test_sadl::externalequationstatement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=sADL::ExternalEquationStatement_strategy)
def test_sadl::externalequationstatement_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=sADL::ExternalEquationStatement_strategy)
def test_sadl::externalequationstatement_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=sADL::StartWriteStatement_strategy)
@settings(max_examples=50)
def test_sadl::startwritestatement_instantiation(instance):
    assert isinstance(instance, sADL::StartWriteStatement)

@given(instance=sADL::StartWriteStatement_strategy)
def test_sadl::startwritestatement_dataOnly_type(instance):
    assert isinstance(instance.dataOnly, str)


@given(instance=sADL::StartWriteStatement_strategy)
def test_sadl::startwritestatement_dataOnly_setter(instance):
    original = instance.dataOnly
    instance.dataOnly = original
    assert instance.dataOnly == original

@given(instance=sADL::StartWriteStatement_strategy)
def test_sadl::startwritestatement_write_type(instance):
    assert isinstance(instance.write, str)


@given(instance=sADL::StartWriteStatement_strategy)
def test_sadl::startwritestatement_write_setter(instance):
    original = instance.write
    instance.write = original
    assert instance.write == original

@given(instance=sADL::SadlStatement_strategy)
@settings(max_examples=50)
def test_sadl::sadlstatement_instantiation(instance):
    assert isinstance(instance, sADL::SadlStatement)

@given(instance=sADL::EndWriteStatement_strategy)
@settings(max_examples=50)
def test_sadl::endwritestatement_instantiation(instance):
    assert isinstance(instance, sADL::EndWriteStatement)

@given(instance=sADL::EndWriteStatement_strategy)
def test_sadl::endwritestatement_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=sADL::EndWriteStatement_strategy)
def test_sadl::endwritestatement_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=sADL::ExplainStatement_strategy)
@settings(max_examples=50)
def test_sadl::explainstatement_instantiation(instance):
    assert isinstance(instance, sADL::ExplainStatement)

@given(instance=sADL::PrintStatement_strategy)
@settings(max_examples=50)
def test_sadl::printstatement_instantiation(instance):
    assert isinstance(instance, sADL::PrintStatement)

@given(instance=sADL::PrintStatement_strategy)
def test_sadl::printstatement_model_type(instance):
    assert isinstance(instance.model, str)


@given(instance=sADL::PrintStatement_strategy)
def test_sadl::printstatement_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original

@given(instance=sADL::PrintStatement_strategy)
def test_sadl::printstatement_displayString_type(instance):
    assert isinstance(instance.displayString, str)


@given(instance=sADL::PrintStatement_strategy)
def test_sadl::printstatement_displayString_setter(instance):
    original = instance.displayString
    instance.displayString = original
    assert instance.displayString == original

@given(instance=sADL::ExpressionScope_strategy)
@settings(max_examples=50)
def test_sadl::expressionscope_instantiation(instance):
    assert isinstance(instance, sADL::ExpressionScope)

@given(instance=sADL::EquationStatement_strategy)
@settings(max_examples=50)
def test_sadl::equationstatement_instantiation(instance):
    assert isinstance(instance, sADL::EquationStatement)

@given(instance=sADL::SadlModelElement_strategy)
@settings(max_examples=50)
def test_sadl::sadlmodelelement_instantiation(instance):
    assert isinstance(instance, sADL::SadlModelElement)

@given(instance=sADL::SadlImport_strategy)
@settings(max_examples=50)
def test_sadl::sadlimport_instantiation(instance):
    assert isinstance(instance, sADL::SadlImport)

@given(instance=sADL::SadlImport_strategy)
def test_sadl::sadlimport_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=sADL::SadlImport_strategy)
def test_sadl::sadlimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=sADL::SadlAnnotation_strategy)
@settings(max_examples=50)
def test_sadl::sadlannotation_instantiation(instance):
    assert isinstance(instance, sADL::SadlAnnotation)

@given(instance=sADL::SadlAnnotation_strategy)
def test_sadl::sadlannotation_contents_type(instance):
    assert isinstance(instance.contents, str)


@given(instance=sADL::SadlAnnotation_strategy)
def test_sadl::sadlannotation_contents_setter(instance):
    original = instance.contents
    instance.contents = original
    assert instance.contents == original

@given(instance=sADL::SadlAnnotation_strategy)
def test_sadl::sadlannotation_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=sADL::SadlAnnotation_strategy)
def test_sadl::sadlannotation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
