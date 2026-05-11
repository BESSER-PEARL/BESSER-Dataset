import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    Expression::Operation,
    Expression::Expression,
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



def test_expression::operation_is_not_abstract():
    assert not inspect.isabstract(Expression::Operation)


def test_expression::operation_constructor_exists():
    assert callable(Expression::Operation.__init__)


def test_expression::operation_constructor_args():
    sig = inspect.signature(Expression::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expression::operation_has_op():
    assert hasattr(Expression::Operation, "op")
    descriptor = None
    for klass in Expression::Operation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression::expression_is_not_abstract():
    assert not inspect.isabstract(Expression::Expression)


def test_expression::expression_constructor_exists():
    assert callable(Expression::Expression.__init__)


def test_expression::expression_constructor_args():
    sig = inspect.signature(Expression::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression::expression_has_value():
    assert hasattr(Expression::Expression, "value")
    descriptor = None
    for klass in Expression::Expression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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
Expression::Operation_strategy = st.builds(
    Expression::Operation,
    op=
        safe_text
)
Expression::Expression_strategy = st.builds(
    Expression::Expression,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=Expression::Operation_strategy)
@settings(max_examples=50)
def test_expression::operation_instantiation(instance):
    assert isinstance(instance, Expression::Operation)

@given(instance=Expression::Operation_strategy)
def test_expression::operation_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=Expression::Operation_strategy)
def test_expression::operation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=Expression::Expression_strategy)
@settings(max_examples=50)
def test_expression::expression_instantiation(instance):
    assert isinstance(instance, Expression::Expression)

@given(instance=Expression::Expression_strategy)
def test_expression::expression_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=Expression::Expression_strategy)
def test_expression::expression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
