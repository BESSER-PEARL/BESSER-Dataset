import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    arithmetics::Minus,
    arithmetics::Plus,
    arithmetics::Expression,
    arithmetics::Evaluation,
    arithmetics::NumberLiteral,
    arithmetics::Div,
    arithmetics::Multi,
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



def test_arithmetics::minus_is_not_abstract():
    assert not inspect.isabstract(arithmetics::Minus)


def test_arithmetics::minus_constructor_exists():
    assert callable(arithmetics::Minus.__init__)


def test_arithmetics::minus_constructor_args():
    sig = inspect.signature(arithmetics::Minus.__init__)
    params = list(sig.parameters.keys())



def test_arithmetics::plus_is_not_abstract():
    assert not inspect.isabstract(arithmetics::Plus)


def test_arithmetics::plus_constructor_exists():
    assert callable(arithmetics::Plus.__init__)


def test_arithmetics::plus_constructor_args():
    sig = inspect.signature(arithmetics::Plus.__init__)
    params = list(sig.parameters.keys())



def test_arithmetics::expression_is_not_abstract():
    assert not inspect.isabstract(arithmetics::Expression)


def test_arithmetics::expression_constructor_exists():
    assert callable(arithmetics::Expression.__init__)


def test_arithmetics::expression_constructor_args():
    sig = inspect.signature(arithmetics::Expression.__init__)
    params = list(sig.parameters.keys())



def test_arithmetics::evaluation_is_not_abstract():
    assert not inspect.isabstract(arithmetics::Evaluation)


def test_arithmetics::evaluation_constructor_exists():
    assert callable(arithmetics::Evaluation.__init__)


def test_arithmetics::evaluation_constructor_args():
    sig = inspect.signature(arithmetics::Evaluation.__init__)
    params = list(sig.parameters.keys())



def test_arithmetics::numberliteral_is_not_abstract():
    assert not inspect.isabstract(arithmetics::NumberLiteral)


def test_arithmetics::numberliteral_constructor_exists():
    assert callable(arithmetics::NumberLiteral.__init__)


def test_arithmetics::numberliteral_constructor_args():
    sig = inspect.signature(arithmetics::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arithmetics::numberliteral_has_value():
    assert hasattr(arithmetics::NumberLiteral, "value")
    descriptor = None
    for klass in arithmetics::NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arithmetics::div_is_not_abstract():
    assert not inspect.isabstract(arithmetics::Div)


def test_arithmetics::div_constructor_exists():
    assert callable(arithmetics::Div.__init__)


def test_arithmetics::div_constructor_args():
    sig = inspect.signature(arithmetics::Div.__init__)
    params = list(sig.parameters.keys())



def test_arithmetics::multi_is_not_abstract():
    assert not inspect.isabstract(arithmetics::Multi)


def test_arithmetics::multi_constructor_exists():
    assert callable(arithmetics::Multi.__init__)


def test_arithmetics::multi_constructor_args():
    sig = inspect.signature(arithmetics::Multi.__init__)
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
Expression_strategy = st.builds(
    Expression,
)
arithmetics::Minus_strategy = st.builds(
    arithmetics::Minus,
)
arithmetics::Plus_strategy = st.builds(
    arithmetics::Plus,
)
arithmetics::Expression_strategy = st.builds(
    arithmetics::Expression,
)
arithmetics::Evaluation_strategy = st.builds(
    arithmetics::Evaluation,
)
arithmetics::NumberLiteral_strategy = st.builds(
    arithmetics::NumberLiteral,
    value=
        safe_text
)
arithmetics::Div_strategy = st.builds(
    arithmetics::Div,
)
arithmetics::Multi_strategy = st.builds(
    arithmetics::Multi,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=arithmetics::Minus_strategy)
@settings(max_examples=50)
def test_arithmetics::minus_instantiation(instance):
    assert isinstance(instance, arithmetics::Minus)

@given(instance=arithmetics::Plus_strategy)
@settings(max_examples=50)
def test_arithmetics::plus_instantiation(instance):
    assert isinstance(instance, arithmetics::Plus)

@given(instance=arithmetics::Expression_strategy)
@settings(max_examples=50)
def test_arithmetics::expression_instantiation(instance):
    assert isinstance(instance, arithmetics::Expression)

@given(instance=arithmetics::Evaluation_strategy)
@settings(max_examples=50)
def test_arithmetics::evaluation_instantiation(instance):
    assert isinstance(instance, arithmetics::Evaluation)

@given(instance=arithmetics::NumberLiteral_strategy)
@settings(max_examples=50)
def test_arithmetics::numberliteral_instantiation(instance):
    assert isinstance(instance, arithmetics::NumberLiteral)

@given(instance=arithmetics::NumberLiteral_strategy)
def test_arithmetics::numberliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=arithmetics::NumberLiteral_strategy)
def test_arithmetics::numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arithmetics::Div_strategy)
@settings(max_examples=50)
def test_arithmetics::div_instantiation(instance):
    assert isinstance(instance, arithmetics::Div)

@given(instance=arithmetics::Multi_strategy)
@settings(max_examples=50)
def test_arithmetics::multi_instantiation(instance):
    assert isinstance(instance, arithmetics::Multi)
