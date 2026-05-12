import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    mathDSL_Minus,
    mathDSL_Plus,
    mathDSL_NumberLiteral,
    mathDSL_Div,
    mathDSL_Multi,
    mathDSL_Expression,
    mathDSL_Math,
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



def test_mathdsl_minus_is_not_abstract():
    assert not inspect.isabstract(mathDSL_Minus)


def test_mathdsl_minus_constructor_exists():
    assert callable(mathDSL_Minus.__init__)


def test_mathdsl_minus_constructor_args():
    sig = inspect.signature(mathDSL_Minus.__init__)
    params = list(sig.parameters.keys())



def test_mathdsl_plus_is_not_abstract():
    assert not inspect.isabstract(mathDSL_Plus)


def test_mathdsl_plus_constructor_exists():
    assert callable(mathDSL_Plus.__init__)


def test_mathdsl_plus_constructor_args():
    sig = inspect.signature(mathDSL_Plus.__init__)
    params = list(sig.parameters.keys())



def test_mathdsl_numberliteral_is_not_abstract():
    assert not inspect.isabstract(mathDSL_NumberLiteral)


def test_mathdsl_numberliteral_constructor_exists():
    assert callable(mathDSL_NumberLiteral.__init__)


def test_mathdsl_numberliteral_constructor_args():
    sig = inspect.signature(mathDSL_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mathdsl_numberliteral_has_value():
    assert hasattr(mathDSL_NumberLiteral, "value")
    descriptor = None
    for klass in mathDSL_NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mathdsl_div_is_not_abstract():
    assert not inspect.isabstract(mathDSL_Div)


def test_mathdsl_div_constructor_exists():
    assert callable(mathDSL_Div.__init__)


def test_mathdsl_div_constructor_args():
    sig = inspect.signature(mathDSL_Div.__init__)
    params = list(sig.parameters.keys())



def test_mathdsl_multi_is_not_abstract():
    assert not inspect.isabstract(mathDSL_Multi)


def test_mathdsl_multi_constructor_exists():
    assert callable(mathDSL_Multi.__init__)


def test_mathdsl_multi_constructor_args():
    sig = inspect.signature(mathDSL_Multi.__init__)
    params = list(sig.parameters.keys())



def test_mathdsl_expression_is_not_abstract():
    assert not inspect.isabstract(mathDSL_Expression)


def test_mathdsl_expression_constructor_exists():
    assert callable(mathDSL_Expression.__init__)


def test_mathdsl_expression_constructor_args():
    sig = inspect.signature(mathDSL_Expression.__init__)
    params = list(sig.parameters.keys())



def test_mathdsl_math_is_not_abstract():
    assert not inspect.isabstract(mathDSL_Math)


def test_mathdsl_math_constructor_exists():
    assert callable(mathDSL_Math.__init__)


def test_mathdsl_math_constructor_args():
    sig = inspect.signature(mathDSL_Math.__init__)
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
mathDSL_Minus_strategy = st.builds(
    mathDSL_Minus,
)
mathDSL_Plus_strategy = st.builds(
    mathDSL_Plus,
)
mathDSL_NumberLiteral_strategy = st.builds(
    mathDSL_NumberLiteral,
    value=
        safe_text
)
mathDSL_Div_strategy = st.builds(
    mathDSL_Div,
)
mathDSL_Multi_strategy = st.builds(
    mathDSL_Multi,
)
mathDSL_Expression_strategy = st.builds(
    mathDSL_Expression,
)
mathDSL_Math_strategy = st.builds(
    mathDSL_Math,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=mathDSL_Minus_strategy)
@settings(max_examples=50)
def test_mathdsl_minus_instantiation(instance):
    assert isinstance(instance, mathDSL_Minus)

@given(instance=mathDSL_Plus_strategy)
@settings(max_examples=50)
def test_mathdsl_plus_instantiation(instance):
    assert isinstance(instance, mathDSL_Plus)

@given(instance=mathDSL_NumberLiteral_strategy)
@settings(max_examples=50)
def test_mathdsl_numberliteral_instantiation(instance):
    assert isinstance(instance, mathDSL_NumberLiteral)



@given(instance=mathDSL_NumberLiteral_strategy)
def test_mathdsl_numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mathDSL_Div_strategy)
@settings(max_examples=50)
def test_mathdsl_div_instantiation(instance):
    assert isinstance(instance, mathDSL_Div)

@given(instance=mathDSL_Multi_strategy)
@settings(max_examples=50)
def test_mathdsl_multi_instantiation(instance):
    assert isinstance(instance, mathDSL_Multi)

@given(instance=mathDSL_Expression_strategy)
@settings(max_examples=50)
def test_mathdsl_expression_instantiation(instance):
    assert isinstance(instance, mathDSL_Expression)

@given(instance=mathDSL_Math_strategy)
@settings(max_examples=50)
def test_mathdsl_math_instantiation(instance):
    assert isinstance(instance, mathDSL_Math)
