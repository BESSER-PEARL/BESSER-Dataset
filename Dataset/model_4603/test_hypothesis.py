import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    henshin::text::BoolValue,
    henshin::text::JavaAttributeValue,
    henshin::text::NumberValue,
    henshin::text::ParameterValue,
    henshin::text::BracketExpression,
    henshin::text::JavaClassValue,
    henshin::text::StringValue,
    henshin::text::IntegerValue,
    henshin::text::MulOrDivExpression,
    henshin::text::NotExpression,
    henshin::text::NaturalValue,
    henshin::text::OrExpression,
    henshin::text::MinusExpression,
    henshin::text::PlusExpression,
    henshin::text::ComparisonExpression,
    henshin::text::EqualityExpression,
    henshin::text::AndExpression,
    Logic,
    henshin::text::Not,
    henshin::text::AND,
    henshin::text::ConditionGraphRef,
    henshin::text::ORorXOR,
    ModelElement,
    henshin::text::Unit,
    henshin::text::Rule,
    henshin::text::ParameterType,
    henshin::text::UnitElement,
    henshin::text::List,
    SequentialProperties,
    henshin::text::Rollback,
    henshin::text::Strict,
    UnitElement,
    henshin::text::Call,
    henshin::text::IndependentUnit,
    henshin::text::ConditionalUnit,
    henshin::text::IteratedUnit,
    henshin::text::LoopUnit,
    henshin::text::PriorityUnit,
    henshin::text::SequentialProperties,
    henshin::text::Logic,
    ConditionGraphElements,
    henshin::text::ConditionReuseNode,
    henshin::text::Match,
    henshin::text::ConditionNodeTypes,
    henshin::text::ConditionEdge,
    henshin::text::ConditionEdges,
    henshin::text::ConditionGraphElements,
    henshin::text::ConditionGraph,
    henshin::text::RuleNodeTypes,
    henshin::text::Edge,
    GraphElements,
    henshin::text::MultiRule,
    henshin::text::Formula,
    henshin::text::Edges,
    henshin::text::GraphElements,
    henshin::text::Expression,
    henshin::text::EAttribute,
    henshin::text::Attribute,
    henshin::text::EClass,
    ConditionNodeTypes,
    henshin::text::ConditionNode,
    RuleNodeTypes,
    henshin::text::MultiRuleReuseNode,
    henshin::text::Node,
    henshin::text::EReference,
    henshin::text::EPackageImport,
    henshin::text::Model,
    RuleElement,
    henshin::text::CheckDangling,
    henshin::text::InjectiveMatching,
    henshin::text::Conditions,
    henshin::text::Graph,
    henshin::text::JavaImport,
    henshin::text::RuleElement,
    henshin::text::Parameter,
    henshin::text::EPackage,
    henshin::text::ModelElement,
    ParameterKind,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::boolvalue_is_not_abstract():
    assert not inspect.isabstract(henshin::text::BoolValue)


def test_henshin::text::boolvalue_constructor_exists():
    assert callable(henshin::text::BoolValue.__init__)


def test_henshin::text::boolvalue_constructor_args():
    sig = inspect.signature(henshin::text::BoolValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_henshin::text::boolvalue_has_value():
    assert hasattr(henshin::text::BoolValue, "value")
    descriptor = None
    for klass in henshin::text::BoolValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::javaattributevalue_is_not_abstract():
    assert not inspect.isabstract(henshin::text::JavaAttributeValue)


def test_henshin::text::javaattributevalue_constructor_exists():
    assert callable(henshin::text::JavaAttributeValue.__init__)


def test_henshin::text::javaattributevalue_constructor_args():
    sig = inspect.signature(henshin::text::JavaAttributeValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_henshin::text::javaattributevalue_has_value():
    assert hasattr(henshin::text::JavaAttributeValue, "value")
    descriptor = None
    for klass in henshin::text::JavaAttributeValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::numbervalue_is_not_abstract():
    assert not inspect.isabstract(henshin::text::NumberValue)


def test_henshin::text::numbervalue_constructor_exists():
    assert callable(henshin::text::NumberValue.__init__)


def test_henshin::text::numbervalue_constructor_args():
    sig = inspect.signature(henshin::text::NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_henshin::text::numbervalue_has_value():
    assert hasattr(henshin::text::NumberValue, "value")
    descriptor = None
    for klass in henshin::text::NumberValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::parametervalue_is_not_abstract():
    assert not inspect.isabstract(henshin::text::ParameterValue)


def test_henshin::text::parametervalue_constructor_exists():
    assert callable(henshin::text::ParameterValue.__init__)


def test_henshin::text::parametervalue_constructor_args():
    sig = inspect.signature(henshin::text::ParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::bracketexpression_is_not_abstract():
    assert not inspect.isabstract(henshin::text::BracketExpression)


def test_henshin::text::bracketexpression_constructor_exists():
    assert callable(henshin::text::BracketExpression.__init__)


def test_henshin::text::bracketexpression_constructor_args():
    sig = inspect.signature(henshin::text::BracketExpression.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::javaclassvalue_is_not_abstract():
    assert not inspect.isabstract(henshin::text::JavaClassValue)


def test_henshin::text::javaclassvalue_constructor_exists():
    assert callable(henshin::text::JavaClassValue.__init__)


def test_henshin::text::javaclassvalue_constructor_args():
    sig = inspect.signature(henshin::text::JavaClassValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_henshin::text::javaclassvalue_has_value():
    assert hasattr(henshin::text::JavaClassValue, "value")
    descriptor = None
    for klass in henshin::text::JavaClassValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::stringvalue_is_not_abstract():
    assert not inspect.isabstract(henshin::text::StringValue)


def test_henshin::text::stringvalue_constructor_exists():
    assert callable(henshin::text::StringValue.__init__)


def test_henshin::text::stringvalue_constructor_args():
    sig = inspect.signature(henshin::text::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_henshin::text::stringvalue_has_value():
    assert hasattr(henshin::text::StringValue, "value")
    descriptor = None
    for klass in henshin::text::StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::integervalue_is_not_abstract():
    assert not inspect.isabstract(henshin::text::IntegerValue)


def test_henshin::text::integervalue_constructor_exists():
    assert callable(henshin::text::IntegerValue.__init__)


def test_henshin::text::integervalue_constructor_args():
    sig = inspect.signature(henshin::text::IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_henshin::text::integervalue_has_value():
    assert hasattr(henshin::text::IntegerValue, "value")
    descriptor = None
    for klass in henshin::text::IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::mulordivexpression_is_not_abstract():
    assert not inspect.isabstract(henshin::text::MulOrDivExpression)


def test_henshin::text::mulordivexpression_constructor_exists():
    assert callable(henshin::text::MulOrDivExpression.__init__)


def test_henshin::text::mulordivexpression_constructor_args():
    sig = inspect.signature(henshin::text::MulOrDivExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_henshin::text::mulordivexpression_has_op():
    assert hasattr(henshin::text::MulOrDivExpression, "op")
    descriptor = None
    for klass in henshin::text::MulOrDivExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::notexpression_is_not_abstract():
    assert not inspect.isabstract(henshin::text::NotExpression)


def test_henshin::text::notexpression_constructor_exists():
    assert callable(henshin::text::NotExpression.__init__)


def test_henshin::text::notexpression_constructor_args():
    sig = inspect.signature(henshin::text::NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::naturalvalue_is_not_abstract():
    assert not inspect.isabstract(henshin::text::NaturalValue)


def test_henshin::text::naturalvalue_constructor_exists():
    assert callable(henshin::text::NaturalValue.__init__)


def test_henshin::text::naturalvalue_constructor_args():
    sig = inspect.signature(henshin::text::NaturalValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_henshin::text::naturalvalue_has_value():
    assert hasattr(henshin::text::NaturalValue, "value")
    descriptor = None
    for klass in henshin::text::NaturalValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::orexpression_is_not_abstract():
    assert not inspect.isabstract(henshin::text::OrExpression)


def test_henshin::text::orexpression_constructor_exists():
    assert callable(henshin::text::OrExpression.__init__)


def test_henshin::text::orexpression_constructor_args():
    sig = inspect.signature(henshin::text::OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::minusexpression_is_not_abstract():
    assert not inspect.isabstract(henshin::text::MinusExpression)


def test_henshin::text::minusexpression_constructor_exists():
    assert callable(henshin::text::MinusExpression.__init__)


def test_henshin::text::minusexpression_constructor_args():
    sig = inspect.signature(henshin::text::MinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::plusexpression_is_not_abstract():
    assert not inspect.isabstract(henshin::text::PlusExpression)


def test_henshin::text::plusexpression_constructor_exists():
    assert callable(henshin::text::PlusExpression.__init__)


def test_henshin::text::plusexpression_constructor_args():
    sig = inspect.signature(henshin::text::PlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(henshin::text::ComparisonExpression)


def test_henshin::text::comparisonexpression_constructor_exists():
    assert callable(henshin::text::ComparisonExpression.__init__)


def test_henshin::text::comparisonexpression_constructor_args():
    sig = inspect.signature(henshin::text::ComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_henshin::text::comparisonexpression_has_op():
    assert hasattr(henshin::text::ComparisonExpression, "op")
    descriptor = None
    for klass in henshin::text::ComparisonExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(henshin::text::EqualityExpression)


def test_henshin::text::equalityexpression_constructor_exists():
    assert callable(henshin::text::EqualityExpression.__init__)


def test_henshin::text::equalityexpression_constructor_args():
    sig = inspect.signature(henshin::text::EqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_henshin::text::equalityexpression_has_op():
    assert hasattr(henshin::text::EqualityExpression, "op")
    descriptor = None
    for klass in henshin::text::EqualityExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::andexpression_is_not_abstract():
    assert not inspect.isabstract(henshin::text::AndExpression)


def test_henshin::text::andexpression_constructor_exists():
    assert callable(henshin::text::AndExpression.__init__)


def test_henshin::text::andexpression_constructor_args():
    sig = inspect.signature(henshin::text::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_logic_is_not_abstract():
    assert not inspect.isabstract(Logic)


def test_logic_constructor_exists():
    assert callable(Logic.__init__)


def test_logic_constructor_args():
    sig = inspect.signature(Logic.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::not_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Not)


def test_henshin::text::not_constructor_exists():
    assert callable(henshin::text::Not.__init__)


def test_henshin::text::not_constructor_args():
    sig = inspect.signature(henshin::text::Not.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::and_is_not_abstract():
    assert not inspect.isabstract(henshin::text::AND)


def test_henshin::text::and_constructor_exists():
    assert callable(henshin::text::AND.__init__)


def test_henshin::text::and_constructor_args():
    sig = inspect.signature(henshin::text::AND.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::conditiongraphref_is_not_abstract():
    assert not inspect.isabstract(henshin::text::ConditionGraphRef)


def test_henshin::text::conditiongraphref_constructor_exists():
    assert callable(henshin::text::ConditionGraphRef.__init__)


def test_henshin::text::conditiongraphref_constructor_args():
    sig = inspect.signature(henshin::text::ConditionGraphRef.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::ororxor_is_not_abstract():
    assert not inspect.isabstract(henshin::text::ORorXOR)


def test_henshin::text::ororxor_constructor_exists():
    assert callable(henshin::text::ORorXOR.__init__)


def test_henshin::text::ororxor_constructor_args():
    sig = inspect.signature(henshin::text::ORorXOR.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_henshin::text::ororxor_has_op():
    assert hasattr(henshin::text::ORorXOR, "op")
    descriptor = None
    for klass in henshin::text::ORorXOR.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::unit_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Unit)


def test_henshin::text::unit_constructor_exists():
    assert callable(henshin::text::Unit.__init__)


def test_henshin::text::unit_constructor_args():
    sig = inspect.signature(henshin::text::Unit.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::rule_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Rule)


def test_henshin::text::rule_constructor_exists():
    assert callable(henshin::text::Rule.__init__)


def test_henshin::text::rule_constructor_args():
    sig = inspect.signature(henshin::text::Rule.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::parametertype_is_not_abstract():
    assert not inspect.isabstract(henshin::text::ParameterType)


def test_henshin::text::parametertype_constructor_exists():
    assert callable(henshin::text::ParameterType.__init__)


def test_henshin::text::parametertype_constructor_args():
    sig = inspect.signature(henshin::text::ParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "enumType" in params, "Missing parameter 'enumType'"

def test_henshin::text::parametertype_has_enumType():
    assert hasattr(henshin::text::ParameterType, "enumType")
    descriptor = None
    for klass in henshin::text::ParameterType.__mro__:
        if "enumType" in klass.__dict__:
            descriptor = klass.__dict__["enumType"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::unitelement_is_not_abstract():
    assert not inspect.isabstract(henshin::text::UnitElement)


def test_henshin::text::unitelement_constructor_exists():
    assert callable(henshin::text::UnitElement.__init__)


def test_henshin::text::unitelement_constructor_args():
    sig = inspect.signature(henshin::text::UnitElement.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::list_is_not_abstract():
    assert not inspect.isabstract(henshin::text::List)


def test_henshin::text::list_constructor_exists():
    assert callable(henshin::text::List.__init__)


def test_henshin::text::list_constructor_args():
    sig = inspect.signature(henshin::text::List.__init__)
    params = list(sig.parameters.keys())



def test_sequentialproperties_is_not_abstract():
    assert not inspect.isabstract(SequentialProperties)


def test_sequentialproperties_constructor_exists():
    assert callable(SequentialProperties.__init__)


def test_sequentialproperties_constructor_args():
    sig = inspect.signature(SequentialProperties.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::rollback_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Rollback)


def test_henshin::text::rollback_constructor_exists():
    assert callable(henshin::text::Rollback.__init__)


def test_henshin::text::rollback_constructor_args():
    sig = inspect.signature(henshin::text::Rollback.__init__)
    params = list(sig.parameters.keys())
    assert "rollback" in params, "Missing parameter 'rollback'"

def test_henshin::text::rollback_has_rollback():
    assert hasattr(henshin::text::Rollback, "rollback")
    descriptor = None
    for klass in henshin::text::Rollback.__mro__:
        if "rollback" in klass.__dict__:
            descriptor = klass.__dict__["rollback"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::strict_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Strict)


def test_henshin::text::strict_constructor_exists():
    assert callable(henshin::text::Strict.__init__)


def test_henshin::text::strict_constructor_args():
    sig = inspect.signature(henshin::text::Strict.__init__)
    params = list(sig.parameters.keys())
    assert "strict" in params, "Missing parameter 'strict'"

def test_henshin::text::strict_has_strict():
    assert hasattr(henshin::text::Strict, "strict")
    descriptor = None
    for klass in henshin::text::Strict.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)



def test_unitelement_is_not_abstract():
    assert not inspect.isabstract(UnitElement)


def test_unitelement_constructor_exists():
    assert callable(UnitElement.__init__)


def test_unitelement_constructor_args():
    sig = inspect.signature(UnitElement.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::call_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Call)


def test_henshin::text::call_constructor_exists():
    assert callable(henshin::text::Call.__init__)


def test_henshin::text::call_constructor_args():
    sig = inspect.signature(henshin::text::Call.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::independentunit_is_not_abstract():
    assert not inspect.isabstract(henshin::text::IndependentUnit)


def test_henshin::text::independentunit_constructor_exists():
    assert callable(henshin::text::IndependentUnit.__init__)


def test_henshin::text::independentunit_constructor_args():
    sig = inspect.signature(henshin::text::IndependentUnit.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::conditionalunit_is_not_abstract():
    assert not inspect.isabstract(henshin::text::ConditionalUnit)


def test_henshin::text::conditionalunit_constructor_exists():
    assert callable(henshin::text::ConditionalUnit.__init__)


def test_henshin::text::conditionalunit_constructor_args():
    sig = inspect.signature(henshin::text::ConditionalUnit.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::iteratedunit_is_not_abstract():
    assert not inspect.isabstract(henshin::text::IteratedUnit)


def test_henshin::text::iteratedunit_constructor_exists():
    assert callable(henshin::text::IteratedUnit.__init__)


def test_henshin::text::iteratedunit_constructor_args():
    sig = inspect.signature(henshin::text::IteratedUnit.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::loopunit_is_not_abstract():
    assert not inspect.isabstract(henshin::text::LoopUnit)


def test_henshin::text::loopunit_constructor_exists():
    assert callable(henshin::text::LoopUnit.__init__)


def test_henshin::text::loopunit_constructor_args():
    sig = inspect.signature(henshin::text::LoopUnit.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::priorityunit_is_not_abstract():
    assert not inspect.isabstract(henshin::text::PriorityUnit)


def test_henshin::text::priorityunit_constructor_exists():
    assert callable(henshin::text::PriorityUnit.__init__)


def test_henshin::text::priorityunit_constructor_args():
    sig = inspect.signature(henshin::text::PriorityUnit.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::sequentialproperties_is_not_abstract():
    assert not inspect.isabstract(henshin::text::SequentialProperties)


def test_henshin::text::sequentialproperties_constructor_exists():
    assert callable(henshin::text::SequentialProperties.__init__)


def test_henshin::text::sequentialproperties_constructor_args():
    sig = inspect.signature(henshin::text::SequentialProperties.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::logic_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Logic)


def test_henshin::text::logic_constructor_exists():
    assert callable(henshin::text::Logic.__init__)


def test_henshin::text::logic_constructor_args():
    sig = inspect.signature(henshin::text::Logic.__init__)
    params = list(sig.parameters.keys())



def test_conditiongraphelements_is_not_abstract():
    assert not inspect.isabstract(ConditionGraphElements)


def test_conditiongraphelements_constructor_exists():
    assert callable(ConditionGraphElements.__init__)


def test_conditiongraphelements_constructor_args():
    sig = inspect.signature(ConditionGraphElements.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::conditionreusenode_is_not_abstract():
    assert not inspect.isabstract(henshin::text::ConditionReuseNode)


def test_henshin::text::conditionreusenode_constructor_exists():
    assert callable(henshin::text::ConditionReuseNode.__init__)


def test_henshin::text::conditionreusenode_constructor_args():
    sig = inspect.signature(henshin::text::ConditionReuseNode.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::match_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Match)


def test_henshin::text::match_constructor_exists():
    assert callable(henshin::text::Match.__init__)


def test_henshin::text::match_constructor_args():
    sig = inspect.signature(henshin::text::Match.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::conditionnodetypes_is_not_abstract():
    assert not inspect.isabstract(henshin::text::ConditionNodeTypes)


def test_henshin::text::conditionnodetypes_constructor_exists():
    assert callable(henshin::text::ConditionNodeTypes.__init__)


def test_henshin::text::conditionnodetypes_constructor_args():
    sig = inspect.signature(henshin::text::ConditionNodeTypes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_henshin::text::conditionnodetypes_has_name():
    assert hasattr(henshin::text::ConditionNodeTypes, "name")
    descriptor = None
    for klass in henshin::text::ConditionNodeTypes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::conditionedge_is_not_abstract():
    assert not inspect.isabstract(henshin::text::ConditionEdge)


def test_henshin::text::conditionedge_constructor_exists():
    assert callable(henshin::text::ConditionEdge.__init__)


def test_henshin::text::conditionedge_constructor_args():
    sig = inspect.signature(henshin::text::ConditionEdge.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::conditionedges_is_not_abstract():
    assert not inspect.isabstract(henshin::text::ConditionEdges)


def test_henshin::text::conditionedges_constructor_exists():
    assert callable(henshin::text::ConditionEdges.__init__)


def test_henshin::text::conditionedges_constructor_args():
    sig = inspect.signature(henshin::text::ConditionEdges.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::conditiongraphelements_is_not_abstract():
    assert not inspect.isabstract(henshin::text::ConditionGraphElements)


def test_henshin::text::conditiongraphelements_constructor_exists():
    assert callable(henshin::text::ConditionGraphElements.__init__)


def test_henshin::text::conditiongraphelements_constructor_args():
    sig = inspect.signature(henshin::text::ConditionGraphElements.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::conditiongraph_is_not_abstract():
    assert not inspect.isabstract(henshin::text::ConditionGraph)


def test_henshin::text::conditiongraph_constructor_exists():
    assert callable(henshin::text::ConditionGraph.__init__)


def test_henshin::text::conditiongraph_constructor_args():
    sig = inspect.signature(henshin::text::ConditionGraph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_henshin::text::conditiongraph_has_name():
    assert hasattr(henshin::text::ConditionGraph, "name")
    descriptor = None
    for klass in henshin::text::ConditionGraph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::rulenodetypes_is_not_abstract():
    assert not inspect.isabstract(henshin::text::RuleNodeTypes)


def test_henshin::text::rulenodetypes_constructor_exists():
    assert callable(henshin::text::RuleNodeTypes.__init__)


def test_henshin::text::rulenodetypes_constructor_args():
    sig = inspect.signature(henshin::text::RuleNodeTypes.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::edge_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Edge)


def test_henshin::text::edge_constructor_exists():
    assert callable(henshin::text::Edge.__init__)


def test_henshin::text::edge_constructor_args():
    sig = inspect.signature(henshin::text::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "actiontype" in params, "Missing parameter 'actiontype'"

def test_henshin::text::edge_has_actiontype():
    assert hasattr(henshin::text::Edge, "actiontype")
    descriptor = None
    for klass in henshin::text::Edge.__mro__:
        if "actiontype" in klass.__dict__:
            descriptor = klass.__dict__["actiontype"]
            break
    assert isinstance(descriptor, property)



def test_graphelements_is_not_abstract():
    assert not inspect.isabstract(GraphElements)


def test_graphelements_constructor_exists():
    assert callable(GraphElements.__init__)


def test_graphelements_constructor_args():
    sig = inspect.signature(GraphElements.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::multirule_is_not_abstract():
    assert not inspect.isabstract(henshin::text::MultiRule)


def test_henshin::text::multirule_constructor_exists():
    assert callable(henshin::text::MultiRule.__init__)


def test_henshin::text::multirule_constructor_args():
    sig = inspect.signature(henshin::text::MultiRule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_henshin::text::multirule_has_name():
    assert hasattr(henshin::text::MultiRule, "name")
    descriptor = None
    for klass in henshin::text::MultiRule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::formula_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Formula)


def test_henshin::text::formula_constructor_exists():
    assert callable(henshin::text::Formula.__init__)


def test_henshin::text::formula_constructor_args():
    sig = inspect.signature(henshin::text::Formula.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::edges_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Edges)


def test_henshin::text::edges_constructor_exists():
    assert callable(henshin::text::Edges.__init__)


def test_henshin::text::edges_constructor_args():
    sig = inspect.signature(henshin::text::Edges.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::graphelements_is_not_abstract():
    assert not inspect.isabstract(henshin::text::GraphElements)


def test_henshin::text::graphelements_constructor_exists():
    assert callable(henshin::text::GraphElements.__init__)


def test_henshin::text::graphelements_constructor_args():
    sig = inspect.signature(henshin::text::GraphElements.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::expression_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Expression)


def test_henshin::text::expression_constructor_exists():
    assert callable(henshin::text::Expression.__init__)


def test_henshin::text::expression_constructor_args():
    sig = inspect.signature(henshin::text::Expression.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::eattribute_is_not_abstract():
    assert not inspect.isabstract(henshin::text::EAttribute)


def test_henshin::text::eattribute_constructor_exists():
    assert callable(henshin::text::EAttribute.__init__)


def test_henshin::text::eattribute_constructor_args():
    sig = inspect.signature(henshin::text::EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::attribute_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Attribute)


def test_henshin::text::attribute_constructor_exists():
    assert callable(henshin::text::Attribute.__init__)


def test_henshin::text::attribute_constructor_args():
    sig = inspect.signature(henshin::text::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "update" in params, "Missing parameter 'update'"
    assert "actiontype" in params, "Missing parameter 'actiontype'"

def test_henshin::text::attribute_has_update():
    assert hasattr(henshin::text::Attribute, "update")
    descriptor = None
    for klass in henshin::text::Attribute.__mro__:
        if "update" in klass.__dict__:
            descriptor = klass.__dict__["update"]
            break
    assert isinstance(descriptor, property)

def test_henshin::text::attribute_has_actiontype():
    assert hasattr(henshin::text::Attribute, "actiontype")
    descriptor = None
    for klass in henshin::text::Attribute.__mro__:
        if "actiontype" in klass.__dict__:
            descriptor = klass.__dict__["actiontype"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::eclass_is_not_abstract():
    assert not inspect.isabstract(henshin::text::EClass)


def test_henshin::text::eclass_constructor_exists():
    assert callable(henshin::text::EClass.__init__)


def test_henshin::text::eclass_constructor_args():
    sig = inspect.signature(henshin::text::EClass.__init__)
    params = list(sig.parameters.keys())



def test_conditionnodetypes_is_not_abstract():
    assert not inspect.isabstract(ConditionNodeTypes)


def test_conditionnodetypes_constructor_exists():
    assert callable(ConditionNodeTypes.__init__)


def test_conditionnodetypes_constructor_args():
    sig = inspect.signature(ConditionNodeTypes.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::conditionnode_is_not_abstract():
    assert not inspect.isabstract(henshin::text::ConditionNode)


def test_henshin::text::conditionnode_constructor_exists():
    assert callable(henshin::text::ConditionNode.__init__)


def test_henshin::text::conditionnode_constructor_args():
    sig = inspect.signature(henshin::text::ConditionNode.__init__)
    params = list(sig.parameters.keys())



def test_rulenodetypes_is_not_abstract():
    assert not inspect.isabstract(RuleNodeTypes)


def test_rulenodetypes_constructor_exists():
    assert callable(RuleNodeTypes.__init__)


def test_rulenodetypes_constructor_args():
    sig = inspect.signature(RuleNodeTypes.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::multirulereusenode_is_not_abstract():
    assert not inspect.isabstract(henshin::text::MultiRuleReuseNode)


def test_henshin::text::multirulereusenode_constructor_exists():
    assert callable(henshin::text::MultiRuleReuseNode.__init__)


def test_henshin::text::multirulereusenode_constructor_args():
    sig = inspect.signature(henshin::text::MultiRuleReuseNode.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::node_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Node)


def test_henshin::text::node_constructor_exists():
    assert callable(henshin::text::Node.__init__)


def test_henshin::text::node_constructor_args():
    sig = inspect.signature(henshin::text::Node.__init__)
    params = list(sig.parameters.keys())
    assert "actiontype" in params, "Missing parameter 'actiontype'"

def test_henshin::text::node_has_actiontype():
    assert hasattr(henshin::text::Node, "actiontype")
    descriptor = None
    for klass in henshin::text::Node.__mro__:
        if "actiontype" in klass.__dict__:
            descriptor = klass.__dict__["actiontype"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::ereference_is_not_abstract():
    assert not inspect.isabstract(henshin::text::EReference)


def test_henshin::text::ereference_constructor_exists():
    assert callable(henshin::text::EReference.__init__)


def test_henshin::text::ereference_constructor_args():
    sig = inspect.signature(henshin::text::EReference.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::epackageimport_is_not_abstract():
    assert not inspect.isabstract(henshin::text::EPackageImport)


def test_henshin::text::epackageimport_constructor_exists():
    assert callable(henshin::text::EPackageImport.__init__)


def test_henshin::text::epackageimport_constructor_args():
    sig = inspect.signature(henshin::text::EPackageImport.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::model_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Model)


def test_henshin::text::model_constructor_exists():
    assert callable(henshin::text::Model.__init__)


def test_henshin::text::model_constructor_args():
    sig = inspect.signature(henshin::text::Model.__init__)
    params = list(sig.parameters.keys())



def test_ruleelement_is_not_abstract():
    assert not inspect.isabstract(RuleElement)


def test_ruleelement_constructor_exists():
    assert callable(RuleElement.__init__)


def test_ruleelement_constructor_args():
    sig = inspect.signature(RuleElement.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::checkdangling_is_not_abstract():
    assert not inspect.isabstract(henshin::text::CheckDangling)


def test_henshin::text::checkdangling_constructor_exists():
    assert callable(henshin::text::CheckDangling.__init__)


def test_henshin::text::checkdangling_constructor_args():
    sig = inspect.signature(henshin::text::CheckDangling.__init__)
    params = list(sig.parameters.keys())
    assert "checkDangling" in params, "Missing parameter 'checkDangling'"

def test_henshin::text::checkdangling_has_checkDangling():
    assert hasattr(henshin::text::CheckDangling, "checkDangling")
    descriptor = None
    for klass in henshin::text::CheckDangling.__mro__:
        if "checkDangling" in klass.__dict__:
            descriptor = klass.__dict__["checkDangling"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::injectivematching_is_not_abstract():
    assert not inspect.isabstract(henshin::text::InjectiveMatching)


def test_henshin::text::injectivematching_constructor_exists():
    assert callable(henshin::text::InjectiveMatching.__init__)


def test_henshin::text::injectivematching_constructor_args():
    sig = inspect.signature(henshin::text::InjectiveMatching.__init__)
    params = list(sig.parameters.keys())
    assert "injectiveMatching" in params, "Missing parameter 'injectiveMatching'"

def test_henshin::text::injectivematching_has_injectiveMatching():
    assert hasattr(henshin::text::InjectiveMatching, "injectiveMatching")
    descriptor = None
    for klass in henshin::text::InjectiveMatching.__mro__:
        if "injectiveMatching" in klass.__dict__:
            descriptor = klass.__dict__["injectiveMatching"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::conditions_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Conditions)


def test_henshin::text::conditions_constructor_exists():
    assert callable(henshin::text::Conditions.__init__)


def test_henshin::text::conditions_constructor_args():
    sig = inspect.signature(henshin::text::Conditions.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::graph_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Graph)


def test_henshin::text::graph_constructor_exists():
    assert callable(henshin::text::Graph.__init__)


def test_henshin::text::graph_constructor_args():
    sig = inspect.signature(henshin::text::Graph.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::javaimport_is_not_abstract():
    assert not inspect.isabstract(henshin::text::JavaImport)


def test_henshin::text::javaimport_constructor_exists():
    assert callable(henshin::text::JavaImport.__init__)


def test_henshin::text::javaimport_constructor_args():
    sig = inspect.signature(henshin::text::JavaImport.__init__)
    params = list(sig.parameters.keys())
    assert "packagename" in params, "Missing parameter 'packagename'"

def test_henshin::text::javaimport_has_packagename():
    assert hasattr(henshin::text::JavaImport, "packagename")
    descriptor = None
    for klass in henshin::text::JavaImport.__mro__:
        if "packagename" in klass.__dict__:
            descriptor = klass.__dict__["packagename"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::ruleelement_is_not_abstract():
    assert not inspect.isabstract(henshin::text::RuleElement)


def test_henshin::text::ruleelement_constructor_exists():
    assert callable(henshin::text::RuleElement.__init__)


def test_henshin::text::ruleelement_constructor_args():
    sig = inspect.signature(henshin::text::RuleElement.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::parameter_is_not_abstract():
    assert not inspect.isabstract(henshin::text::Parameter)


def test_henshin::text::parameter_constructor_exists():
    assert callable(henshin::text::Parameter.__init__)


def test_henshin::text::parameter_constructor_args():
    sig = inspect.signature(henshin::text::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_henshin::text::parameter_has_kind():
    assert hasattr(henshin::text::Parameter, "kind")
    descriptor = None
    for klass in henshin::text::Parameter.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_henshin::text::parameter_has_name():
    assert hasattr(henshin::text::Parameter, "name")
    descriptor = None
    for klass in henshin::text::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_henshin::text::epackage_is_not_abstract():
    assert not inspect.isabstract(henshin::text::EPackage)


def test_henshin::text::epackage_constructor_exists():
    assert callable(henshin::text::EPackage.__init__)


def test_henshin::text::epackage_constructor_args():
    sig = inspect.signature(henshin::text::EPackage.__init__)
    params = list(sig.parameters.keys())



def test_henshin::text::modelelement_is_not_abstract():
    assert not inspect.isabstract(henshin::text::ModelElement)


def test_henshin::text::modelelement_constructor_exists():
    assert callable(henshin::text::ModelElement.__init__)


def test_henshin::text::modelelement_constructor_args():
    sig = inspect.signature(henshin::text::ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_henshin::text::modelelement_has_name():
    assert hasattr(henshin::text::ModelElement, "name")
    descriptor = None
    for klass in henshin::text::ModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_parameterkind_exists():
    # Check that the Enumeration exists
    assert ParameterKind is not None

def test_parameterkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterKind]
    expected_literals = [
        "UNKNOWN",
        "INOUT",
        "IN",
        "OUT",
        "VAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterKind"

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "eJavaClass",
        "eCharacterObject",
        "eResource",
        "eShortObject",
        "eEList",
        "eJavaObject",
        "eLong",
        "eBooleanObject",
        "eByte",
        "eShort",
        "eResourceSet",
        "eByteObject",
        "eInvocationTargetException",
        "eBigDecimal",
        "eFloatObject",
        "eBigInteger",
        "eDouble",
        "eByteArray",
        "eFeatureMap",
        "eDoubleObject",
        "eIntegerObject",
        "eString",
        "eFeatureMapEntry",
        "eTreeIterator",
        "eDate",
        "eInt",
        "eBoolean",
        "eLongObject",
        "eChar",
        "eMap",
        "eEnumerator",
        "eFloat",
        "eDiagnosticChain",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
Expression_strategy = st.builds(
    Expression,
)
henshin::text::BoolValue_strategy = st.builds(
    henshin::text::BoolValue,
    value=
        st.booleans()
)
henshin::text::JavaAttributeValue_strategy = st.builds(
    henshin::text::JavaAttributeValue,
    value=
        safe_text
)
henshin::text::NumberValue_strategy = st.builds(
    henshin::text::NumberValue,
    value=
        safe_text
)
henshin::text::ParameterValue_strategy = st.builds(
    henshin::text::ParameterValue,
)
henshin::text::BracketExpression_strategy = st.builds(
    henshin::text::BracketExpression,
)
henshin::text::JavaClassValue_strategy = st.builds(
    henshin::text::JavaClassValue,
    value=
        safe_text
)
henshin::text::StringValue_strategy = st.builds(
    henshin::text::StringValue,
    value=
        safe_text
)
henshin::text::IntegerValue_strategy = st.builds(
    henshin::text::IntegerValue,
    value=
        safe_text
)
henshin::text::MulOrDivExpression_strategy = st.builds(
    henshin::text::MulOrDivExpression,
    op=
        safe_text
)
henshin::text::NotExpression_strategy = st.builds(
    henshin::text::NotExpression,
)
henshin::text::NaturalValue_strategy = st.builds(
    henshin::text::NaturalValue,
    value=
        st.integers()
)
henshin::text::OrExpression_strategy = st.builds(
    henshin::text::OrExpression,
)
henshin::text::MinusExpression_strategy = st.builds(
    henshin::text::MinusExpression,
)
henshin::text::PlusExpression_strategy = st.builds(
    henshin::text::PlusExpression,
)
henshin::text::ComparisonExpression_strategy = st.builds(
    henshin::text::ComparisonExpression,
    op=
        safe_text
)
henshin::text::EqualityExpression_strategy = st.builds(
    henshin::text::EqualityExpression,
    op=
        safe_text
)
henshin::text::AndExpression_strategy = st.builds(
    henshin::text::AndExpression,
)
Logic_strategy = st.builds(
    Logic,
)
henshin::text::Not_strategy = st.builds(
    henshin::text::Not,
)
henshin::text::AND_strategy = st.builds(
    henshin::text::AND,
)
henshin::text::ConditionGraphRef_strategy = st.builds(
    henshin::text::ConditionGraphRef,
)
henshin::text::ORorXOR_strategy = st.builds(
    henshin::text::ORorXOR,
    op=
        safe_text
)
ModelElement_strategy = st.builds(
    ModelElement,
)
henshin::text::Unit_strategy = st.builds(
    henshin::text::Unit,
)
henshin::text::Rule_strategy = st.builds(
    henshin::text::Rule,
)
henshin::text::ParameterType_strategy = st.builds(
    henshin::text::ParameterType,
    enumType=
        safe_text
)
henshin::text::UnitElement_strategy = st.builds(
    henshin::text::UnitElement,
)
henshin::text::List_strategy = st.builds(
    henshin::text::List,
)
SequentialProperties_strategy = st.builds(
    SequentialProperties,
)
henshin::text::Rollback_strategy = st.builds(
    henshin::text::Rollback,
    rollback=
        st.booleans()
)
henshin::text::Strict_strategy = st.builds(
    henshin::text::Strict,
    strict=
        st.booleans()
)
UnitElement_strategy = st.builds(
    UnitElement,
)
henshin::text::Call_strategy = st.builds(
    henshin::text::Call,
)
henshin::text::IndependentUnit_strategy = st.builds(
    henshin::text::IndependentUnit,
)
henshin::text::ConditionalUnit_strategy = st.builds(
    henshin::text::ConditionalUnit,
)
henshin::text::IteratedUnit_strategy = st.builds(
    henshin::text::IteratedUnit,
)
henshin::text::LoopUnit_strategy = st.builds(
    henshin::text::LoopUnit,
)
henshin::text::PriorityUnit_strategy = st.builds(
    henshin::text::PriorityUnit,
)
henshin::text::SequentialProperties_strategy = st.builds(
    henshin::text::SequentialProperties,
)
henshin::text::Logic_strategy = st.builds(
    henshin::text::Logic,
)
ConditionGraphElements_strategy = st.builds(
    ConditionGraphElements,
)
henshin::text::ConditionReuseNode_strategy = st.builds(
    henshin::text::ConditionReuseNode,
)
henshin::text::Match_strategy = st.builds(
    henshin::text::Match,
)
henshin::text::ConditionNodeTypes_strategy = st.builds(
    henshin::text::ConditionNodeTypes,
    name=
        safe_text
)
henshin::text::ConditionEdge_strategy = st.builds(
    henshin::text::ConditionEdge,
)
henshin::text::ConditionEdges_strategy = st.builds(
    henshin::text::ConditionEdges,
)
henshin::text::ConditionGraphElements_strategy = st.builds(
    henshin::text::ConditionGraphElements,
)
henshin::text::ConditionGraph_strategy = st.builds(
    henshin::text::ConditionGraph,
    name=
        safe_text
)
henshin::text::RuleNodeTypes_strategy = st.builds(
    henshin::text::RuleNodeTypes,
)
henshin::text::Edge_strategy = st.builds(
    henshin::text::Edge,
    actiontype=
        safe_text
)
GraphElements_strategy = st.builds(
    GraphElements,
)
henshin::text::MultiRule_strategy = st.builds(
    henshin::text::MultiRule,
    name=
        safe_text
)
henshin::text::Formula_strategy = st.builds(
    henshin::text::Formula,
)
henshin::text::Edges_strategy = st.builds(
    henshin::text::Edges,
)
henshin::text::GraphElements_strategy = st.builds(
    henshin::text::GraphElements,
)
henshin::text::Expression_strategy = st.builds(
    henshin::text::Expression,
)
henshin::text::EAttribute_strategy = st.builds(
    henshin::text::EAttribute,
)
henshin::text::Attribute_strategy = st.builds(
    henshin::text::Attribute,
    update=
        safe_text,
    actiontype=
        safe_text
)
henshin::text::EClass_strategy = st.builds(
    henshin::text::EClass,
)
ConditionNodeTypes_strategy = st.builds(
    ConditionNodeTypes,
)
henshin::text::ConditionNode_strategy = st.builds(
    henshin::text::ConditionNode,
)
RuleNodeTypes_strategy = st.builds(
    RuleNodeTypes,
)
henshin::text::MultiRuleReuseNode_strategy = st.builds(
    henshin::text::MultiRuleReuseNode,
)
henshin::text::Node_strategy = st.builds(
    henshin::text::Node,
    actiontype=
        safe_text
)
henshin::text::EReference_strategy = st.builds(
    henshin::text::EReference,
)
henshin::text::EPackageImport_strategy = st.builds(
    henshin::text::EPackageImport,
)
henshin::text::Model_strategy = st.builds(
    henshin::text::Model,
)
RuleElement_strategy = st.builds(
    RuleElement,
)
henshin::text::CheckDangling_strategy = st.builds(
    henshin::text::CheckDangling,
    checkDangling=
        st.booleans()
)
henshin::text::InjectiveMatching_strategy = st.builds(
    henshin::text::InjectiveMatching,
    injectiveMatching=
        st.booleans()
)
henshin::text::Conditions_strategy = st.builds(
    henshin::text::Conditions,
)
henshin::text::Graph_strategy = st.builds(
    henshin::text::Graph,
)
henshin::text::JavaImport_strategy = st.builds(
    henshin::text::JavaImport,
    packagename=
        safe_text
)
henshin::text::RuleElement_strategy = st.builds(
    henshin::text::RuleElement,
)
henshin::text::Parameter_strategy = st.builds(
    henshin::text::Parameter,
    kind=
        safe_text,
    name=
        safe_text
)
henshin::text::EPackage_strategy = st.builds(
    henshin::text::EPackage,
)
henshin::text::ModelElement_strategy = st.builds(
    henshin::text::ModelElement,
    name=
        safe_text
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=henshin::text::BoolValue_strategy)
@settings(max_examples=50)
def test_henshin::text::boolvalue_instantiation(instance):
    assert isinstance(instance, henshin::text::BoolValue)

@given(instance=henshin::text::BoolValue_strategy)
def test_henshin::text::boolvalue_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=henshin::text::BoolValue_strategy)
def test_henshin::text::boolvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=henshin::text::JavaAttributeValue_strategy)
@settings(max_examples=50)
def test_henshin::text::javaattributevalue_instantiation(instance):
    assert isinstance(instance, henshin::text::JavaAttributeValue)

@given(instance=henshin::text::JavaAttributeValue_strategy)
def test_henshin::text::javaattributevalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=henshin::text::JavaAttributeValue_strategy)
def test_henshin::text::javaattributevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=henshin::text::NumberValue_strategy)
@settings(max_examples=50)
def test_henshin::text::numbervalue_instantiation(instance):
    assert isinstance(instance, henshin::text::NumberValue)

@given(instance=henshin::text::NumberValue_strategy)
def test_henshin::text::numbervalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=henshin::text::NumberValue_strategy)
def test_henshin::text::numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=henshin::text::ParameterValue_strategy)
@settings(max_examples=50)
def test_henshin::text::parametervalue_instantiation(instance):
    assert isinstance(instance, henshin::text::ParameterValue)

@given(instance=henshin::text::BracketExpression_strategy)
@settings(max_examples=50)
def test_henshin::text::bracketexpression_instantiation(instance):
    assert isinstance(instance, henshin::text::BracketExpression)

@given(instance=henshin::text::JavaClassValue_strategy)
@settings(max_examples=50)
def test_henshin::text::javaclassvalue_instantiation(instance):
    assert isinstance(instance, henshin::text::JavaClassValue)

@given(instance=henshin::text::JavaClassValue_strategy)
def test_henshin::text::javaclassvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=henshin::text::JavaClassValue_strategy)
def test_henshin::text::javaclassvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=henshin::text::StringValue_strategy)
@settings(max_examples=50)
def test_henshin::text::stringvalue_instantiation(instance):
    assert isinstance(instance, henshin::text::StringValue)

@given(instance=henshin::text::StringValue_strategy)
def test_henshin::text::stringvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=henshin::text::StringValue_strategy)
def test_henshin::text::stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=henshin::text::IntegerValue_strategy)
@settings(max_examples=50)
def test_henshin::text::integervalue_instantiation(instance):
    assert isinstance(instance, henshin::text::IntegerValue)

@given(instance=henshin::text::IntegerValue_strategy)
def test_henshin::text::integervalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=henshin::text::IntegerValue_strategy)
def test_henshin::text::integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=henshin::text::MulOrDivExpression_strategy)
@settings(max_examples=50)
def test_henshin::text::mulordivexpression_instantiation(instance):
    assert isinstance(instance, henshin::text::MulOrDivExpression)

@given(instance=henshin::text::MulOrDivExpression_strategy)
def test_henshin::text::mulordivexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=henshin::text::MulOrDivExpression_strategy)
def test_henshin::text::mulordivexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=henshin::text::NotExpression_strategy)
@settings(max_examples=50)
def test_henshin::text::notexpression_instantiation(instance):
    assert isinstance(instance, henshin::text::NotExpression)

@given(instance=henshin::text::NaturalValue_strategy)
@settings(max_examples=50)
def test_henshin::text::naturalvalue_instantiation(instance):
    assert isinstance(instance, henshin::text::NaturalValue)

@given(instance=henshin::text::NaturalValue_strategy)
def test_henshin::text::naturalvalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=henshin::text::NaturalValue_strategy)
def test_henshin::text::naturalvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=henshin::text::OrExpression_strategy)
@settings(max_examples=50)
def test_henshin::text::orexpression_instantiation(instance):
    assert isinstance(instance, henshin::text::OrExpression)

@given(instance=henshin::text::MinusExpression_strategy)
@settings(max_examples=50)
def test_henshin::text::minusexpression_instantiation(instance):
    assert isinstance(instance, henshin::text::MinusExpression)

@given(instance=henshin::text::PlusExpression_strategy)
@settings(max_examples=50)
def test_henshin::text::plusexpression_instantiation(instance):
    assert isinstance(instance, henshin::text::PlusExpression)

@given(instance=henshin::text::ComparisonExpression_strategy)
@settings(max_examples=50)
def test_henshin::text::comparisonexpression_instantiation(instance):
    assert isinstance(instance, henshin::text::ComparisonExpression)

@given(instance=henshin::text::ComparisonExpression_strategy)
def test_henshin::text::comparisonexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=henshin::text::ComparisonExpression_strategy)
def test_henshin::text::comparisonexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=henshin::text::EqualityExpression_strategy)
@settings(max_examples=50)
def test_henshin::text::equalityexpression_instantiation(instance):
    assert isinstance(instance, henshin::text::EqualityExpression)

@given(instance=henshin::text::EqualityExpression_strategy)
def test_henshin::text::equalityexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=henshin::text::EqualityExpression_strategy)
def test_henshin::text::equalityexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=henshin::text::AndExpression_strategy)
@settings(max_examples=50)
def test_henshin::text::andexpression_instantiation(instance):
    assert isinstance(instance, henshin::text::AndExpression)

@given(instance=Logic_strategy)
@settings(max_examples=50)
def test_logic_instantiation(instance):
    assert isinstance(instance, Logic)

@given(instance=henshin::text::Not_strategy)
@settings(max_examples=50)
def test_henshin::text::not_instantiation(instance):
    assert isinstance(instance, henshin::text::Not)

@given(instance=henshin::text::AND_strategy)
@settings(max_examples=50)
def test_henshin::text::and_instantiation(instance):
    assert isinstance(instance, henshin::text::AND)

@given(instance=henshin::text::ConditionGraphRef_strategy)
@settings(max_examples=50)
def test_henshin::text::conditiongraphref_instantiation(instance):
    assert isinstance(instance, henshin::text::ConditionGraphRef)

@given(instance=henshin::text::ORorXOR_strategy)
@settings(max_examples=50)
def test_henshin::text::ororxor_instantiation(instance):
    assert isinstance(instance, henshin::text::ORorXOR)

@given(instance=henshin::text::ORorXOR_strategy)
def test_henshin::text::ororxor_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=henshin::text::ORorXOR_strategy)
def test_henshin::text::ororxor_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=henshin::text::Unit_strategy)
@settings(max_examples=50)
def test_henshin::text::unit_instantiation(instance):
    assert isinstance(instance, henshin::text::Unit)

@given(instance=henshin::text::Rule_strategy)
@settings(max_examples=50)
def test_henshin::text::rule_instantiation(instance):
    assert isinstance(instance, henshin::text::Rule)

@given(instance=henshin::text::ParameterType_strategy)
@settings(max_examples=50)
def test_henshin::text::parametertype_instantiation(instance):
    assert isinstance(instance, henshin::text::ParameterType)

@given(instance=henshin::text::ParameterType_strategy)
def test_henshin::text::parametertype_enumType_type(instance):
    assert isinstance(instance.enumType, str)


@given(instance=henshin::text::ParameterType_strategy)
def test_henshin::text::parametertype_enumType_setter(instance):
    original = instance.enumType
    instance.enumType = original
    assert instance.enumType == original

@given(instance=henshin::text::UnitElement_strategy)
@settings(max_examples=50)
def test_henshin::text::unitelement_instantiation(instance):
    assert isinstance(instance, henshin::text::UnitElement)

@given(instance=henshin::text::List_strategy)
@settings(max_examples=50)
def test_henshin::text::list_instantiation(instance):
    assert isinstance(instance, henshin::text::List)

@given(instance=SequentialProperties_strategy)
@settings(max_examples=50)
def test_sequentialproperties_instantiation(instance):
    assert isinstance(instance, SequentialProperties)

@given(instance=henshin::text::Rollback_strategy)
@settings(max_examples=50)
def test_henshin::text::rollback_instantiation(instance):
    assert isinstance(instance, henshin::text::Rollback)

@given(instance=henshin::text::Rollback_strategy)
def test_henshin::text::rollback_rollback_type(instance):
    assert isinstance(instance.rollback, bool)


@given(instance=henshin::text::Rollback_strategy)
def test_henshin::text::rollback_rollback_setter(instance):
    original = instance.rollback
    instance.rollback = original
    assert instance.rollback == original

@given(instance=henshin::text::Strict_strategy)
@settings(max_examples=50)
def test_henshin::text::strict_instantiation(instance):
    assert isinstance(instance, henshin::text::Strict)

@given(instance=henshin::text::Strict_strategy)
def test_henshin::text::strict_strict_type(instance):
    assert isinstance(instance.strict, bool)


@given(instance=henshin::text::Strict_strategy)
def test_henshin::text::strict_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original

@given(instance=UnitElement_strategy)
@settings(max_examples=50)
def test_unitelement_instantiation(instance):
    assert isinstance(instance, UnitElement)

@given(instance=henshin::text::Call_strategy)
@settings(max_examples=50)
def test_henshin::text::call_instantiation(instance):
    assert isinstance(instance, henshin::text::Call)

@given(instance=henshin::text::IndependentUnit_strategy)
@settings(max_examples=50)
def test_henshin::text::independentunit_instantiation(instance):
    assert isinstance(instance, henshin::text::IndependentUnit)

@given(instance=henshin::text::ConditionalUnit_strategy)
@settings(max_examples=50)
def test_henshin::text::conditionalunit_instantiation(instance):
    assert isinstance(instance, henshin::text::ConditionalUnit)

@given(instance=henshin::text::IteratedUnit_strategy)
@settings(max_examples=50)
def test_henshin::text::iteratedunit_instantiation(instance):
    assert isinstance(instance, henshin::text::IteratedUnit)

@given(instance=henshin::text::LoopUnit_strategy)
@settings(max_examples=50)
def test_henshin::text::loopunit_instantiation(instance):
    assert isinstance(instance, henshin::text::LoopUnit)

@given(instance=henshin::text::PriorityUnit_strategy)
@settings(max_examples=50)
def test_henshin::text::priorityunit_instantiation(instance):
    assert isinstance(instance, henshin::text::PriorityUnit)

@given(instance=henshin::text::SequentialProperties_strategy)
@settings(max_examples=50)
def test_henshin::text::sequentialproperties_instantiation(instance):
    assert isinstance(instance, henshin::text::SequentialProperties)

@given(instance=henshin::text::Logic_strategy)
@settings(max_examples=50)
def test_henshin::text::logic_instantiation(instance):
    assert isinstance(instance, henshin::text::Logic)

@given(instance=ConditionGraphElements_strategy)
@settings(max_examples=50)
def test_conditiongraphelements_instantiation(instance):
    assert isinstance(instance, ConditionGraphElements)

@given(instance=henshin::text::ConditionReuseNode_strategy)
@settings(max_examples=50)
def test_henshin::text::conditionreusenode_instantiation(instance):
    assert isinstance(instance, henshin::text::ConditionReuseNode)

@given(instance=henshin::text::Match_strategy)
@settings(max_examples=50)
def test_henshin::text::match_instantiation(instance):
    assert isinstance(instance, henshin::text::Match)

@given(instance=henshin::text::ConditionNodeTypes_strategy)
@settings(max_examples=50)
def test_henshin::text::conditionnodetypes_instantiation(instance):
    assert isinstance(instance, henshin::text::ConditionNodeTypes)

@given(instance=henshin::text::ConditionNodeTypes_strategy)
def test_henshin::text::conditionnodetypes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=henshin::text::ConditionNodeTypes_strategy)
def test_henshin::text::conditionnodetypes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=henshin::text::ConditionEdge_strategy)
@settings(max_examples=50)
def test_henshin::text::conditionedge_instantiation(instance):
    assert isinstance(instance, henshin::text::ConditionEdge)

@given(instance=henshin::text::ConditionEdges_strategy)
@settings(max_examples=50)
def test_henshin::text::conditionedges_instantiation(instance):
    assert isinstance(instance, henshin::text::ConditionEdges)

@given(instance=henshin::text::ConditionGraphElements_strategy)
@settings(max_examples=50)
def test_henshin::text::conditiongraphelements_instantiation(instance):
    assert isinstance(instance, henshin::text::ConditionGraphElements)

@given(instance=henshin::text::ConditionGraph_strategy)
@settings(max_examples=50)
def test_henshin::text::conditiongraph_instantiation(instance):
    assert isinstance(instance, henshin::text::ConditionGraph)

@given(instance=henshin::text::ConditionGraph_strategy)
def test_henshin::text::conditiongraph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=henshin::text::ConditionGraph_strategy)
def test_henshin::text::conditiongraph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=henshin::text::RuleNodeTypes_strategy)
@settings(max_examples=50)
def test_henshin::text::rulenodetypes_instantiation(instance):
    assert isinstance(instance, henshin::text::RuleNodeTypes)

@given(instance=henshin::text::Edge_strategy)
@settings(max_examples=50)
def test_henshin::text::edge_instantiation(instance):
    assert isinstance(instance, henshin::text::Edge)

@given(instance=henshin::text::Edge_strategy)
def test_henshin::text::edge_actiontype_type(instance):
    assert isinstance(instance.actiontype, str)


@given(instance=henshin::text::Edge_strategy)
def test_henshin::text::edge_actiontype_setter(instance):
    original = instance.actiontype
    instance.actiontype = original
    assert instance.actiontype == original

@given(instance=GraphElements_strategy)
@settings(max_examples=50)
def test_graphelements_instantiation(instance):
    assert isinstance(instance, GraphElements)

@given(instance=henshin::text::MultiRule_strategy)
@settings(max_examples=50)
def test_henshin::text::multirule_instantiation(instance):
    assert isinstance(instance, henshin::text::MultiRule)

@given(instance=henshin::text::MultiRule_strategy)
def test_henshin::text::multirule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=henshin::text::MultiRule_strategy)
def test_henshin::text::multirule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=henshin::text::Formula_strategy)
@settings(max_examples=50)
def test_henshin::text::formula_instantiation(instance):
    assert isinstance(instance, henshin::text::Formula)

@given(instance=henshin::text::Edges_strategy)
@settings(max_examples=50)
def test_henshin::text::edges_instantiation(instance):
    assert isinstance(instance, henshin::text::Edges)

@given(instance=henshin::text::GraphElements_strategy)
@settings(max_examples=50)
def test_henshin::text::graphelements_instantiation(instance):
    assert isinstance(instance, henshin::text::GraphElements)

@given(instance=henshin::text::Expression_strategy)
@settings(max_examples=50)
def test_henshin::text::expression_instantiation(instance):
    assert isinstance(instance, henshin::text::Expression)

@given(instance=henshin::text::EAttribute_strategy)
@settings(max_examples=50)
def test_henshin::text::eattribute_instantiation(instance):
    assert isinstance(instance, henshin::text::EAttribute)

@given(instance=henshin::text::Attribute_strategy)
@settings(max_examples=50)
def test_henshin::text::attribute_instantiation(instance):
    assert isinstance(instance, henshin::text::Attribute)

@given(instance=henshin::text::Attribute_strategy)
def test_henshin::text::attribute_update_type(instance):
    assert isinstance(instance.update, str)


@given(instance=henshin::text::Attribute_strategy)
def test_henshin::text::attribute_update_setter(instance):
    original = instance.update
    instance.update = original
    assert instance.update == original

@given(instance=henshin::text::Attribute_strategy)
def test_henshin::text::attribute_actiontype_type(instance):
    assert isinstance(instance.actiontype, str)


@given(instance=henshin::text::Attribute_strategy)
def test_henshin::text::attribute_actiontype_setter(instance):
    original = instance.actiontype
    instance.actiontype = original
    assert instance.actiontype == original

@given(instance=henshin::text::EClass_strategy)
@settings(max_examples=50)
def test_henshin::text::eclass_instantiation(instance):
    assert isinstance(instance, henshin::text::EClass)

@given(instance=ConditionNodeTypes_strategy)
@settings(max_examples=50)
def test_conditionnodetypes_instantiation(instance):
    assert isinstance(instance, ConditionNodeTypes)

@given(instance=henshin::text::ConditionNode_strategy)
@settings(max_examples=50)
def test_henshin::text::conditionnode_instantiation(instance):
    assert isinstance(instance, henshin::text::ConditionNode)

@given(instance=RuleNodeTypes_strategy)
@settings(max_examples=50)
def test_rulenodetypes_instantiation(instance):
    assert isinstance(instance, RuleNodeTypes)

@given(instance=henshin::text::MultiRuleReuseNode_strategy)
@settings(max_examples=50)
def test_henshin::text::multirulereusenode_instantiation(instance):
    assert isinstance(instance, henshin::text::MultiRuleReuseNode)

@given(instance=henshin::text::Node_strategy)
@settings(max_examples=50)
def test_henshin::text::node_instantiation(instance):
    assert isinstance(instance, henshin::text::Node)

@given(instance=henshin::text::Node_strategy)
def test_henshin::text::node_actiontype_type(instance):
    assert isinstance(instance.actiontype, str)


@given(instance=henshin::text::Node_strategy)
def test_henshin::text::node_actiontype_setter(instance):
    original = instance.actiontype
    instance.actiontype = original
    assert instance.actiontype == original

@given(instance=henshin::text::EReference_strategy)
@settings(max_examples=50)
def test_henshin::text::ereference_instantiation(instance):
    assert isinstance(instance, henshin::text::EReference)

@given(instance=henshin::text::EPackageImport_strategy)
@settings(max_examples=50)
def test_henshin::text::epackageimport_instantiation(instance):
    assert isinstance(instance, henshin::text::EPackageImport)

@given(instance=henshin::text::Model_strategy)
@settings(max_examples=50)
def test_henshin::text::model_instantiation(instance):
    assert isinstance(instance, henshin::text::Model)

@given(instance=RuleElement_strategy)
@settings(max_examples=50)
def test_ruleelement_instantiation(instance):
    assert isinstance(instance, RuleElement)

@given(instance=henshin::text::CheckDangling_strategy)
@settings(max_examples=50)
def test_henshin::text::checkdangling_instantiation(instance):
    assert isinstance(instance, henshin::text::CheckDangling)

@given(instance=henshin::text::CheckDangling_strategy)
def test_henshin::text::checkdangling_checkDangling_type(instance):
    assert isinstance(instance.checkDangling, bool)


@given(instance=henshin::text::CheckDangling_strategy)
def test_henshin::text::checkdangling_checkDangling_setter(instance):
    original = instance.checkDangling
    instance.checkDangling = original
    assert instance.checkDangling == original

@given(instance=henshin::text::InjectiveMatching_strategy)
@settings(max_examples=50)
def test_henshin::text::injectivematching_instantiation(instance):
    assert isinstance(instance, henshin::text::InjectiveMatching)

@given(instance=henshin::text::InjectiveMatching_strategy)
def test_henshin::text::injectivematching_injectiveMatching_type(instance):
    assert isinstance(instance.injectiveMatching, bool)


@given(instance=henshin::text::InjectiveMatching_strategy)
def test_henshin::text::injectivematching_injectiveMatching_setter(instance):
    original = instance.injectiveMatching
    instance.injectiveMatching = original
    assert instance.injectiveMatching == original

@given(instance=henshin::text::Conditions_strategy)
@settings(max_examples=50)
def test_henshin::text::conditions_instantiation(instance):
    assert isinstance(instance, henshin::text::Conditions)

@given(instance=henshin::text::Graph_strategy)
@settings(max_examples=50)
def test_henshin::text::graph_instantiation(instance):
    assert isinstance(instance, henshin::text::Graph)

@given(instance=henshin::text::JavaImport_strategy)
@settings(max_examples=50)
def test_henshin::text::javaimport_instantiation(instance):
    assert isinstance(instance, henshin::text::JavaImport)

@given(instance=henshin::text::JavaImport_strategy)
def test_henshin::text::javaimport_packagename_type(instance):
    assert isinstance(instance.packagename, str)


@given(instance=henshin::text::JavaImport_strategy)
def test_henshin::text::javaimport_packagename_setter(instance):
    original = instance.packagename
    instance.packagename = original
    assert instance.packagename == original

@given(instance=henshin::text::RuleElement_strategy)
@settings(max_examples=50)
def test_henshin::text::ruleelement_instantiation(instance):
    assert isinstance(instance, henshin::text::RuleElement)

@given(instance=henshin::text::Parameter_strategy)
@settings(max_examples=50)
def test_henshin::text::parameter_instantiation(instance):
    assert isinstance(instance, henshin::text::Parameter)

@given(instance=henshin::text::Parameter_strategy)
def test_henshin::text::parameter_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=henshin::text::Parameter_strategy)
def test_henshin::text::parameter_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=henshin::text::Parameter_strategy)
def test_henshin::text::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=henshin::text::Parameter_strategy)
def test_henshin::text::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=henshin::text::EPackage_strategy)
@settings(max_examples=50)
def test_henshin::text::epackage_instantiation(instance):
    assert isinstance(instance, henshin::text::EPackage)

@given(instance=henshin::text::ModelElement_strategy)
@settings(max_examples=50)
def test_henshin::text::modelelement_instantiation(instance):
    assert isinstance(instance, henshin::text::ModelElement)

@given(instance=henshin::text::ModelElement_strategy)
def test_henshin::text::modelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=henshin::text::ModelElement_strategy)
def test_henshin::text::modelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
