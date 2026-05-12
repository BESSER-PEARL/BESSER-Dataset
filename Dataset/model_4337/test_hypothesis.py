import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    Expression_Operation,
    Expression_Expression,
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



def test_expression_operation_is_not_abstract():
    assert not inspect.isabstract(Expression_Operation)


def test_expression_operation_constructor_exists():
    assert callable(Expression_Operation.__init__)


def test_expression_operation_constructor_args():
    sig = inspect.signature(Expression_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expression_operation_has_op():
    assert hasattr(Expression_Operation, "op")
    descriptor = None
    for klass in Expression_Operation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression_expression_is_not_abstract():
    assert not inspect.isabstract(Expression_Expression)


def test_expression_expression_constructor_exists():
    assert callable(Expression_Expression.__init__)


def test_expression_expression_constructor_args():
    sig = inspect.signature(Expression_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression_expression_has_value():
    assert hasattr(Expression_Expression, "value")
    descriptor = None
    for klass in Expression_Expression.__mro__:
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
Expression_Operation_strategy = st.builds(
    Expression_Operation,
    op=
        safe_text
)
Expression_Expression_strategy = st.builds(
    Expression_Expression,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=Expression_Operation_strategy)
@settings(max_examples=50)
def test_expression_operation_instantiation(instance):
    assert isinstance(instance, Expression_Operation)



@given(instance=Expression_Operation_strategy)
def test_expression_operation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=Expression_Expression_strategy)
@settings(max_examples=50)
def test_expression_expression_instantiation(instance):
    assert isinstance(instance, Expression_Expression)



@given(instance=Expression_Expression_strategy)
def test_expression_expression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
