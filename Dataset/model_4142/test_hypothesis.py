import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    arithmetics_Minus,
    arithmetics_Plus,
    arithmetics_Expression,
    arithmetics_Evaluation,
    arithmetics_NumberLiteral,
    arithmetics_Div,
    arithmetics_Multi,
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



def test_arithmetics_minus_is_not_abstract():
    assert not inspect.isabstract(arithmetics_Minus)


def test_arithmetics_minus_constructor_exists():
    assert callable(arithmetics_Minus.__init__)


def test_arithmetics_minus_constructor_args():
    sig = inspect.signature(arithmetics_Minus.__init__)
    params = list(sig.parameters.keys())



def test_arithmetics_plus_is_not_abstract():
    assert not inspect.isabstract(arithmetics_Plus)


def test_arithmetics_plus_constructor_exists():
    assert callable(arithmetics_Plus.__init__)


def test_arithmetics_plus_constructor_args():
    sig = inspect.signature(arithmetics_Plus.__init__)
    params = list(sig.parameters.keys())



def test_arithmetics_expression_is_not_abstract():
    assert not inspect.isabstract(arithmetics_Expression)


def test_arithmetics_expression_constructor_exists():
    assert callable(arithmetics_Expression.__init__)


def test_arithmetics_expression_constructor_args():
    sig = inspect.signature(arithmetics_Expression.__init__)
    params = list(sig.parameters.keys())



def test_arithmetics_evaluation_is_not_abstract():
    assert not inspect.isabstract(arithmetics_Evaluation)


def test_arithmetics_evaluation_constructor_exists():
    assert callable(arithmetics_Evaluation.__init__)


def test_arithmetics_evaluation_constructor_args():
    sig = inspect.signature(arithmetics_Evaluation.__init__)
    params = list(sig.parameters.keys())



def test_arithmetics_numberliteral_is_not_abstract():
    assert not inspect.isabstract(arithmetics_NumberLiteral)


def test_arithmetics_numberliteral_constructor_exists():
    assert callable(arithmetics_NumberLiteral.__init__)


def test_arithmetics_numberliteral_constructor_args():
    sig = inspect.signature(arithmetics_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arithmetics_numberliteral_has_value():
    assert hasattr(arithmetics_NumberLiteral, "value")
    descriptor = None
    for klass in arithmetics_NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arithmetics_div_is_not_abstract():
    assert not inspect.isabstract(arithmetics_Div)


def test_arithmetics_div_constructor_exists():
    assert callable(arithmetics_Div.__init__)


def test_arithmetics_div_constructor_args():
    sig = inspect.signature(arithmetics_Div.__init__)
    params = list(sig.parameters.keys())



def test_arithmetics_multi_is_not_abstract():
    assert not inspect.isabstract(arithmetics_Multi)


def test_arithmetics_multi_constructor_exists():
    assert callable(arithmetics_Multi.__init__)


def test_arithmetics_multi_constructor_args():
    sig = inspect.signature(arithmetics_Multi.__init__)
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
arithmetics_Minus_strategy = st.builds(
    arithmetics_Minus,
)
arithmetics_Plus_strategy = st.builds(
    arithmetics_Plus,
)
arithmetics_Expression_strategy = st.builds(
    arithmetics_Expression,
)
arithmetics_Evaluation_strategy = st.builds(
    arithmetics_Evaluation,
)
arithmetics_NumberLiteral_strategy = st.builds(
    arithmetics_NumberLiteral,
    value=
        safe_text
)
arithmetics_Div_strategy = st.builds(
    arithmetics_Div,
)
arithmetics_Multi_strategy = st.builds(
    arithmetics_Multi,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=arithmetics_Minus_strategy)
@settings(max_examples=50)
def test_arithmetics_minus_instantiation(instance):
    assert isinstance(instance, arithmetics_Minus)

@given(instance=arithmetics_Plus_strategy)
@settings(max_examples=50)
def test_arithmetics_plus_instantiation(instance):
    assert isinstance(instance, arithmetics_Plus)

@given(instance=arithmetics_Expression_strategy)
@settings(max_examples=50)
def test_arithmetics_expression_instantiation(instance):
    assert isinstance(instance, arithmetics_Expression)

@given(instance=arithmetics_Evaluation_strategy)
@settings(max_examples=50)
def test_arithmetics_evaluation_instantiation(instance):
    assert isinstance(instance, arithmetics_Evaluation)

@given(instance=arithmetics_NumberLiteral_strategy)
@settings(max_examples=50)
def test_arithmetics_numberliteral_instantiation(instance):
    assert isinstance(instance, arithmetics_NumberLiteral)



@given(instance=arithmetics_NumberLiteral_strategy)
def test_arithmetics_numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arithmetics_Div_strategy)
@settings(max_examples=50)
def test_arithmetics_div_instantiation(instance):
    assert isinstance(instance, arithmetics_Div)

@given(instance=arithmetics_Multi_strategy)
@settings(max_examples=50)
def test_arithmetics_multi_instantiation(instance):
    assert isinstance(instance, arithmetics_Multi)
