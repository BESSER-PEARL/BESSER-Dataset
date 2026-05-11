import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    mathDSL::Minus,
    mathDSL::Plus,
    mathDSL::NumberLiteral,
    mathDSL::Div,
    mathDSL::Multi,
    mathDSL::Expression,
    mathDSL::Math,
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



def test_mathdsl::minus_is_not_abstract():
    assert not inspect.isabstract(mathDSL::Minus)


def test_mathdsl::minus_constructor_exists():
    assert callable(mathDSL::Minus.__init__)


def test_mathdsl::minus_constructor_args():
    sig = inspect.signature(mathDSL::Minus.__init__)
    params = list(sig.parameters.keys())



def test_mathdsl::plus_is_not_abstract():
    assert not inspect.isabstract(mathDSL::Plus)


def test_mathdsl::plus_constructor_exists():
    assert callable(mathDSL::Plus.__init__)


def test_mathdsl::plus_constructor_args():
    sig = inspect.signature(mathDSL::Plus.__init__)
    params = list(sig.parameters.keys())



def test_mathdsl::numberliteral_is_not_abstract():
    assert not inspect.isabstract(mathDSL::NumberLiteral)


def test_mathdsl::numberliteral_constructor_exists():
    assert callable(mathDSL::NumberLiteral.__init__)


def test_mathdsl::numberliteral_constructor_args():
    sig = inspect.signature(mathDSL::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mathdsl::numberliteral_has_value():
    assert hasattr(mathDSL::NumberLiteral, "value")
    descriptor = None
    for klass in mathDSL::NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mathdsl::div_is_not_abstract():
    assert not inspect.isabstract(mathDSL::Div)


def test_mathdsl::div_constructor_exists():
    assert callable(mathDSL::Div.__init__)


def test_mathdsl::div_constructor_args():
    sig = inspect.signature(mathDSL::Div.__init__)
    params = list(sig.parameters.keys())



def test_mathdsl::multi_is_not_abstract():
    assert not inspect.isabstract(mathDSL::Multi)


def test_mathdsl::multi_constructor_exists():
    assert callable(mathDSL::Multi.__init__)


def test_mathdsl::multi_constructor_args():
    sig = inspect.signature(mathDSL::Multi.__init__)
    params = list(sig.parameters.keys())



def test_mathdsl::expression_is_not_abstract():
    assert not inspect.isabstract(mathDSL::Expression)


def test_mathdsl::expression_constructor_exists():
    assert callable(mathDSL::Expression.__init__)


def test_mathdsl::expression_constructor_args():
    sig = inspect.signature(mathDSL::Expression.__init__)
    params = list(sig.parameters.keys())



def test_mathdsl::math_is_not_abstract():
    assert not inspect.isabstract(mathDSL::Math)


def test_mathdsl::math_constructor_exists():
    assert callable(mathDSL::Math.__init__)


def test_mathdsl::math_constructor_args():
    sig = inspect.signature(mathDSL::Math.__init__)
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
mathDSL::Minus_strategy = st.builds(
    mathDSL::Minus,
)
mathDSL::Plus_strategy = st.builds(
    mathDSL::Plus,
)
mathDSL::NumberLiteral_strategy = st.builds(
    mathDSL::NumberLiteral,
    value=
        safe_text
)
mathDSL::Div_strategy = st.builds(
    mathDSL::Div,
)
mathDSL::Multi_strategy = st.builds(
    mathDSL::Multi,
)
mathDSL::Expression_strategy = st.builds(
    mathDSL::Expression,
)
mathDSL::Math_strategy = st.builds(
    mathDSL::Math,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=mathDSL::Minus_strategy)
@settings(max_examples=50)
def test_mathdsl::minus_instantiation(instance):
    assert isinstance(instance, mathDSL::Minus)

@given(instance=mathDSL::Plus_strategy)
@settings(max_examples=50)
def test_mathdsl::plus_instantiation(instance):
    assert isinstance(instance, mathDSL::Plus)

@given(instance=mathDSL::NumberLiteral_strategy)
@settings(max_examples=50)
def test_mathdsl::numberliteral_instantiation(instance):
    assert isinstance(instance, mathDSL::NumberLiteral)

@given(instance=mathDSL::NumberLiteral_strategy)
def test_mathdsl::numberliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=mathDSL::NumberLiteral_strategy)
def test_mathdsl::numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mathDSL::Div_strategy)
@settings(max_examples=50)
def test_mathdsl::div_instantiation(instance):
    assert isinstance(instance, mathDSL::Div)

@given(instance=mathDSL::Multi_strategy)
@settings(max_examples=50)
def test_mathdsl::multi_instantiation(instance):
    assert isinstance(instance, mathDSL::Multi)

@given(instance=mathDSL::Expression_strategy)
@settings(max_examples=50)
def test_mathdsl::expression_instantiation(instance):
    assert isinstance(instance, mathDSL::Expression)

@given(instance=mathDSL::Math_strategy)
@settings(max_examples=50)
def test_mathdsl::math_instantiation(instance):
    assert isinstance(instance, mathDSL::Math)
