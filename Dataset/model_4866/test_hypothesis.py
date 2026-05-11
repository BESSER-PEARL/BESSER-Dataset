import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    simpleExpressions::Comparison,
    simpleExpressions::MethodCall,
    simpleExpressions::OrExpression,
    simpleExpressions::NotExpression,
    simpleExpressions::AndExpression,
    simpleExpressions::NumberLiteral,
    simpleExpressions::Expression,
    simpleExpressions::IfCondition,
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



def test_simpleexpressions::comparison_is_not_abstract():
    assert not inspect.isabstract(simpleExpressions::Comparison)


def test_simpleexpressions::comparison_constructor_exists():
    assert callable(simpleExpressions::Comparison.__init__)


def test_simpleexpressions::comparison_constructor_args():
    sig = inspect.signature(simpleExpressions::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_simpleexpressions::comparison_has_operator():
    assert hasattr(simpleExpressions::Comparison, "operator")
    descriptor = None
    for klass in simpleExpressions::Comparison.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_simpleexpressions::methodcall_is_not_abstract():
    assert not inspect.isabstract(simpleExpressions::MethodCall)


def test_simpleexpressions::methodcall_constructor_exists():
    assert callable(simpleExpressions::MethodCall.__init__)


def test_simpleexpressions::methodcall_constructor_args():
    sig = inspect.signature(simpleExpressions::MethodCall.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simpleexpressions::methodcall_has_value():
    assert hasattr(simpleExpressions::MethodCall, "value")
    descriptor = None
    for klass in simpleExpressions::MethodCall.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simpleexpressions::orexpression_is_not_abstract():
    assert not inspect.isabstract(simpleExpressions::OrExpression)


def test_simpleexpressions::orexpression_constructor_exists():
    assert callable(simpleExpressions::OrExpression.__init__)


def test_simpleexpressions::orexpression_constructor_args():
    sig = inspect.signature(simpleExpressions::OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_simpleexpressions::notexpression_is_not_abstract():
    assert not inspect.isabstract(simpleExpressions::NotExpression)


def test_simpleexpressions::notexpression_constructor_exists():
    assert callable(simpleExpressions::NotExpression.__init__)


def test_simpleexpressions::notexpression_constructor_args():
    sig = inspect.signature(simpleExpressions::NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_simpleexpressions::andexpression_is_not_abstract():
    assert not inspect.isabstract(simpleExpressions::AndExpression)


def test_simpleexpressions::andexpression_constructor_exists():
    assert callable(simpleExpressions::AndExpression.__init__)


def test_simpleexpressions::andexpression_constructor_args():
    sig = inspect.signature(simpleExpressions::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_simpleexpressions::numberliteral_is_not_abstract():
    assert not inspect.isabstract(simpleExpressions::NumberLiteral)


def test_simpleexpressions::numberliteral_constructor_exists():
    assert callable(simpleExpressions::NumberLiteral.__init__)


def test_simpleexpressions::numberliteral_constructor_args():
    sig = inspect.signature(simpleExpressions::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simpleexpressions::numberliteral_has_value():
    assert hasattr(simpleExpressions::NumberLiteral, "value")
    descriptor = None
    for klass in simpleExpressions::NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simpleexpressions::expression_is_not_abstract():
    assert not inspect.isabstract(simpleExpressions::Expression)


def test_simpleexpressions::expression_constructor_exists():
    assert callable(simpleExpressions::Expression.__init__)


def test_simpleexpressions::expression_constructor_args():
    sig = inspect.signature(simpleExpressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_simpleexpressions::ifcondition_is_not_abstract():
    assert not inspect.isabstract(simpleExpressions::IfCondition)


def test_simpleexpressions::ifcondition_constructor_exists():
    assert callable(simpleExpressions::IfCondition.__init__)


def test_simpleexpressions::ifcondition_constructor_args():
    sig = inspect.signature(simpleExpressions::IfCondition.__init__)
    params = list(sig.parameters.keys())
    assert "elseif" in params, "Missing parameter 'elseif'"

def test_simpleexpressions::ifcondition_has_elseif():
    assert hasattr(simpleExpressions::IfCondition, "elseif")
    descriptor = None
    for klass in simpleExpressions::IfCondition.__mro__:
        if "elseif" in klass.__dict__:
            descriptor = klass.__dict__["elseif"]
            break
    assert isinstance(descriptor, property)


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
simpleExpressions::Comparison_strategy = st.builds(
    simpleExpressions::Comparison,
    operator=
        safe_text
)
simpleExpressions::MethodCall_strategy = st.builds(
    simpleExpressions::MethodCall,
    value=
        safe_text
)
simpleExpressions::OrExpression_strategy = st.builds(
    simpleExpressions::OrExpression,
)
simpleExpressions::NotExpression_strategy = st.builds(
    simpleExpressions::NotExpression,
)
simpleExpressions::AndExpression_strategy = st.builds(
    simpleExpressions::AndExpression,
)
simpleExpressions::NumberLiteral_strategy = st.builds(
    simpleExpressions::NumberLiteral,
    value=
        st.integers()
)
simpleExpressions::Expression_strategy = st.builds(
    simpleExpressions::Expression,
)
simpleExpressions::IfCondition_strategy = st.builds(
    simpleExpressions::IfCondition,
    elseif=
        st.booleans()
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=simpleExpressions::Comparison_strategy)
@settings(max_examples=50)
def test_simpleexpressions::comparison_instantiation(instance):
    assert isinstance(instance, simpleExpressions::Comparison)

@given(instance=simpleExpressions::Comparison_strategy)
def test_simpleexpressions::comparison_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=simpleExpressions::Comparison_strategy)
def test_simpleexpressions::comparison_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=simpleExpressions::MethodCall_strategy)
@settings(max_examples=50)
def test_simpleexpressions::methodcall_instantiation(instance):
    assert isinstance(instance, simpleExpressions::MethodCall)

@given(instance=simpleExpressions::MethodCall_strategy)
def test_simpleexpressions::methodcall_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=simpleExpressions::MethodCall_strategy)
def test_simpleexpressions::methodcall_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simpleExpressions::OrExpression_strategy)
@settings(max_examples=50)
def test_simpleexpressions::orexpression_instantiation(instance):
    assert isinstance(instance, simpleExpressions::OrExpression)

@given(instance=simpleExpressions::NotExpression_strategy)
@settings(max_examples=50)
def test_simpleexpressions::notexpression_instantiation(instance):
    assert isinstance(instance, simpleExpressions::NotExpression)

@given(instance=simpleExpressions::AndExpression_strategy)
@settings(max_examples=50)
def test_simpleexpressions::andexpression_instantiation(instance):
    assert isinstance(instance, simpleExpressions::AndExpression)

@given(instance=simpleExpressions::NumberLiteral_strategy)
@settings(max_examples=50)
def test_simpleexpressions::numberliteral_instantiation(instance):
    assert isinstance(instance, simpleExpressions::NumberLiteral)

@given(instance=simpleExpressions::NumberLiteral_strategy)
def test_simpleexpressions::numberliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=simpleExpressions::NumberLiteral_strategy)
def test_simpleexpressions::numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simpleExpressions::Expression_strategy)
@settings(max_examples=50)
def test_simpleexpressions::expression_instantiation(instance):
    assert isinstance(instance, simpleExpressions::Expression)

@given(instance=simpleExpressions::IfCondition_strategy)
@settings(max_examples=50)
def test_simpleexpressions::ifcondition_instantiation(instance):
    assert isinstance(instance, simpleExpressions::IfCondition)

@given(instance=simpleExpressions::IfCondition_strategy)
def test_simpleexpressions::ifcondition_elseif_type(instance):
    assert isinstance(instance.elseif, bool)


@given(instance=simpleExpressions::IfCondition_strategy)
def test_simpleexpressions::ifcondition_elseif_setter(instance):
    original = instance.elseif
    instance.elseif = original
    assert instance.elseif == original
