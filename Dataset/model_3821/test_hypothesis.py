import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    expression_ExpressionStatement,
    expression_Expression,
    Expression,
    expression_UnaryExpression,
    expression_IntegerExpression,
    expression_BinaryExpression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(expression_ExpressionStatement)


def test_expression_expressionstatement_constructor_exists():
    assert callable(expression_ExpressionStatement.__init__)


def test_expression_expressionstatement_constructor_args():
    sig = inspect.signature(expression_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression_expression_is_not_abstract():
    assert not inspect.isabstract(expression_Expression)


def test_expression_expression_constructor_exists():
    assert callable(expression_Expression.__init__)


def test_expression_expression_constructor_args():
    sig = inspect.signature(expression_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "calculatedValue" in params, "Missing parameter 'calculatedValue'"

def test_expression_expression_has_calculatedValue():
    assert hasattr(expression_Expression, "calculatedValue")
    descriptor = None
    for klass in expression_Expression.__mro__:
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



def test_expression_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(expression_UnaryExpression)


def test_expression_unaryexpression_constructor_exists():
    assert callable(expression_UnaryExpression.__init__)


def test_expression_unaryexpression_constructor_args():
    sig = inspect.signature(expression_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_integerexpression_is_not_abstract():
    assert not inspect.isabstract(expression_IntegerExpression)


def test_expression_integerexpression_constructor_exists():
    assert callable(expression_IntegerExpression.__init__)


def test_expression_integerexpression_constructor_args():
    sig = inspect.signature(expression_IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression_integerexpression_has_value():
    assert hasattr(expression_IntegerExpression, "value")
    descriptor = None
    for klass in expression_IntegerExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(expression_BinaryExpression)


def test_expression_binaryexpression_constructor_exists():
    assert callable(expression_BinaryExpression.__init__)


def test_expression_binaryexpression_constructor_args():
    sig = inspect.signature(expression_BinaryExpression.__init__)
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
expression_ExpressionStatement_strategy = st.builds(
    expression_ExpressionStatement,
)
expression_Expression_strategy = st.builds(
    expression_Expression,
    calculatedValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Expression_strategy = st.builds(
    Expression,
)
expression_UnaryExpression_strategy = st.builds(
    expression_UnaryExpression,
)
expression_IntegerExpression_strategy = st.builds(
    expression_IntegerExpression,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
expression_BinaryExpression_strategy = st.builds(
    expression_BinaryExpression,
)

@given(instance=expression_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_expression_expressionstatement_instantiation(instance):
    assert isinstance(instance, expression_ExpressionStatement)

@given(instance=expression_Expression_strategy)
@settings(max_examples=50)
def test_expression_expression_instantiation(instance):
    assert isinstance(instance, expression_Expression)



@given(instance=expression_Expression_strategy)
def test_expression_expression_calculatedValue_setter(instance):
    original = instance.calculatedValue
    instance.calculatedValue = original
    assert instance.calculatedValue == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=expression_UnaryExpression_strategy)
@settings(max_examples=50)
def test_expression_unaryexpression_instantiation(instance):
    assert isinstance(instance, expression_UnaryExpression)

@given(instance=expression_IntegerExpression_strategy)
@settings(max_examples=50)
def test_expression_integerexpression_instantiation(instance):
    assert isinstance(instance, expression_IntegerExpression)



@given(instance=expression_IntegerExpression_strategy)
def test_expression_integerexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression_BinaryExpression_strategy)
@settings(max_examples=50)
def test_expression_binaryexpression_instantiation(instance):
    assert isinstance(instance, expression_BinaryExpression)
