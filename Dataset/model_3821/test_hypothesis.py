import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    expression::ExpressionStatement,
    expression::Expression,
    Expression,
    expression::UnaryExpression,
    expression::IntegerExpression,
    expression::BinaryExpression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(expression::ExpressionStatement)


def test_expression::expressionstatement_constructor_exists():
    assert callable(expression::ExpressionStatement.__init__)


def test_expression::expressionstatement_constructor_args():
    sig = inspect.signature(expression::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression::expression_is_not_abstract():
    assert not inspect.isabstract(expression::Expression)


def test_expression::expression_constructor_exists():
    assert callable(expression::Expression.__init__)


def test_expression::expression_constructor_args():
    sig = inspect.signature(expression::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "calculatedValue" in params, "Missing parameter 'calculatedValue'"

def test_expression::expression_has_calculatedValue():
    assert hasattr(expression::Expression, "calculatedValue")
    descriptor = None
    for klass in expression::Expression.__mro__:
        if "calculatedValue" in klass.__dict__:
            descriptor = klass.__dict__["calculatedValue"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_expression::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(expression::UnaryExpression)


def test_expression::unaryexpression_constructor_exists():
    assert callable(expression::UnaryExpression.__init__)


def test_expression::unaryexpression_constructor_args():
    sig = inspect.signature(expression::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression::integerexpression_is_not_abstract():
    assert not inspect.isabstract(expression::IntegerExpression)


def test_expression::integerexpression_constructor_exists():
    assert callable(expression::IntegerExpression.__init__)


def test_expression::integerexpression_constructor_args():
    sig = inspect.signature(expression::IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression::integerexpression_has_value():
    assert hasattr(expression::IntegerExpression, "value")
    descriptor = None
    for klass in expression::IntegerExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(expression::BinaryExpression)


def test_expression::binaryexpression_constructor_exists():
    assert callable(expression::BinaryExpression.__init__)


def test_expression::binaryexpression_constructor_args():
    sig = inspect.signature(expression::BinaryExpression.__init__)
    params = list(sig.parameters.keys())


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
expression::ExpressionStatement_strategy = st.builds(
    expression::ExpressionStatement,
)
expression::Expression_strategy = st.builds(
    expression::Expression,
    calculatedValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Expression_strategy = st.builds(
    Expression,
)
expression::UnaryExpression_strategy = st.builds(
    expression::UnaryExpression,
)
expression::IntegerExpression_strategy = st.builds(
    expression::IntegerExpression,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
expression::BinaryExpression_strategy = st.builds(
    expression::BinaryExpression,
)

@given(instance=expression::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_expression::expressionstatement_instantiation(instance):
    assert isinstance(instance, expression::ExpressionStatement)

@given(instance=expression::Expression_strategy)
@settings(max_examples=50)
def test_expression::expression_instantiation(instance):
    assert isinstance(instance, expression::Expression)

@given(instance=expression::Expression_strategy)
def test_expression::expression_calculatedValue_type(instance):
    assert isinstance(instance.calculatedValue, float)


@given(instance=expression::Expression_strategy)
def test_expression::expression_calculatedValue_setter(instance):
    original = instance.calculatedValue
    instance.calculatedValue = original
    assert instance.calculatedValue == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=expression::UnaryExpression_strategy)
@settings(max_examples=50)
def test_expression::unaryexpression_instantiation(instance):
    assert isinstance(instance, expression::UnaryExpression)

@given(instance=expression::IntegerExpression_strategy)
@settings(max_examples=50)
def test_expression::integerexpression_instantiation(instance):
    assert isinstance(instance, expression::IntegerExpression)

@given(instance=expression::IntegerExpression_strategy)
def test_expression::integerexpression_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=expression::IntegerExpression_strategy)
def test_expression::integerexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression::BinaryExpression_strategy)
@settings(max_examples=50)
def test_expression::binaryexpression_instantiation(instance):
    assert isinstance(instance, expression::BinaryExpression)
