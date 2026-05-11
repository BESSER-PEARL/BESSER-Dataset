import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Primary,
    mathInterpeter::Number,
    mathInterpeter::Parenthesis,
    Exp,
    mathInterpeter::Plus,
    mathInterpeter::Div,
    mathInterpeter::Minus,
    mathInterpeter::Mult,
    mathInterpeter::Primary,
    mathInterpeter::Exp,
    mathInterpeter::MathExp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_primary_is_not_abstract():
    assert not inspect.isabstract(Primary)


def test_primary_constructor_exists():
    assert callable(Primary.__init__)


def test_primary_constructor_args():
    sig = inspect.signature(Primary.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpeter::number_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter::Number)


def test_mathinterpeter::number_constructor_exists():
    assert callable(mathInterpeter::Number.__init__)


def test_mathinterpeter::number_constructor_args():
    sig = inspect.signature(mathInterpeter::Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mathinterpeter::number_has_value():
    assert hasattr(mathInterpeter::Number, "value")
    descriptor = None
    for klass in mathInterpeter::Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mathinterpeter::parenthesis_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter::Parenthesis)


def test_mathinterpeter::parenthesis_constructor_exists():
    assert callable(mathInterpeter::Parenthesis.__init__)


def test_mathinterpeter::parenthesis_constructor_args():
    sig = inspect.signature(mathInterpeter::Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpeter::plus_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter::Plus)


def test_mathinterpeter::plus_constructor_exists():
    assert callable(mathInterpeter::Plus.__init__)


def test_mathinterpeter::plus_constructor_args():
    sig = inspect.signature(mathInterpeter::Plus.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpeter::div_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter::Div)


def test_mathinterpeter::div_constructor_exists():
    assert callable(mathInterpeter::Div.__init__)


def test_mathinterpeter::div_constructor_args():
    sig = inspect.signature(mathInterpeter::Div.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpeter::minus_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter::Minus)


def test_mathinterpeter::minus_constructor_exists():
    assert callable(mathInterpeter::Minus.__init__)


def test_mathinterpeter::minus_constructor_args():
    sig = inspect.signature(mathInterpeter::Minus.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpeter::mult_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter::Mult)


def test_mathinterpeter::mult_constructor_exists():
    assert callable(mathInterpeter::Mult.__init__)


def test_mathinterpeter::mult_constructor_args():
    sig = inspect.signature(mathInterpeter::Mult.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpeter::primary_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter::Primary)


def test_mathinterpeter::primary_constructor_exists():
    assert callable(mathInterpeter::Primary.__init__)


def test_mathinterpeter::primary_constructor_args():
    sig = inspect.signature(mathInterpeter::Primary.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpeter::exp_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter::Exp)


def test_mathinterpeter::exp_constructor_exists():
    assert callable(mathInterpeter::Exp.__init__)


def test_mathinterpeter::exp_constructor_args():
    sig = inspect.signature(mathInterpeter::Exp.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpeter::mathexp_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter::MathExp)


def test_mathinterpeter::mathexp_constructor_exists():
    assert callable(mathInterpeter::MathExp.__init__)


def test_mathinterpeter::mathexp_constructor_args():
    sig = inspect.signature(mathInterpeter::MathExp.__init__)
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
Primary_strategy = st.builds(
    Primary,
)
mathInterpeter::Number_strategy = st.builds(
    mathInterpeter::Number,
    value=
        st.integers()
)
mathInterpeter::Parenthesis_strategy = st.builds(
    mathInterpeter::Parenthesis,
)
Exp_strategy = st.builds(
    Exp,
)
mathInterpeter::Plus_strategy = st.builds(
    mathInterpeter::Plus,
)
mathInterpeter::Div_strategy = st.builds(
    mathInterpeter::Div,
)
mathInterpeter::Minus_strategy = st.builds(
    mathInterpeter::Minus,
)
mathInterpeter::Mult_strategy = st.builds(
    mathInterpeter::Mult,
)
mathInterpeter::Primary_strategy = st.builds(
    mathInterpeter::Primary,
)
mathInterpeter::Exp_strategy = st.builds(
    mathInterpeter::Exp,
)
mathInterpeter::MathExp_strategy = st.builds(
    mathInterpeter::MathExp,
)

@given(instance=Primary_strategy)
@settings(max_examples=50)
def test_primary_instantiation(instance):
    assert isinstance(instance, Primary)

@given(instance=mathInterpeter::Number_strategy)
@settings(max_examples=50)
def test_mathinterpeter::number_instantiation(instance):
    assert isinstance(instance, mathInterpeter::Number)

@given(instance=mathInterpeter::Number_strategy)
def test_mathinterpeter::number_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=mathInterpeter::Number_strategy)
def test_mathinterpeter::number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mathInterpeter::Parenthesis_strategy)
@settings(max_examples=50)
def test_mathinterpeter::parenthesis_instantiation(instance):
    assert isinstance(instance, mathInterpeter::Parenthesis)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=mathInterpeter::Plus_strategy)
@settings(max_examples=50)
def test_mathinterpeter::plus_instantiation(instance):
    assert isinstance(instance, mathInterpeter::Plus)

@given(instance=mathInterpeter::Div_strategy)
@settings(max_examples=50)
def test_mathinterpeter::div_instantiation(instance):
    assert isinstance(instance, mathInterpeter::Div)

@given(instance=mathInterpeter::Minus_strategy)
@settings(max_examples=50)
def test_mathinterpeter::minus_instantiation(instance):
    assert isinstance(instance, mathInterpeter::Minus)

@given(instance=mathInterpeter::Mult_strategy)
@settings(max_examples=50)
def test_mathinterpeter::mult_instantiation(instance):
    assert isinstance(instance, mathInterpeter::Mult)

@given(instance=mathInterpeter::Primary_strategy)
@settings(max_examples=50)
def test_mathinterpeter::primary_instantiation(instance):
    assert isinstance(instance, mathInterpeter::Primary)

@given(instance=mathInterpeter::Exp_strategy)
@settings(max_examples=50)
def test_mathinterpeter::exp_instantiation(instance):
    assert isinstance(instance, mathInterpeter::Exp)

@given(instance=mathInterpeter::MathExp_strategy)
@settings(max_examples=50)
def test_mathinterpeter::mathexp_instantiation(instance):
    assert isinstance(instance, mathInterpeter::MathExp)
