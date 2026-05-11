import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ExpOp,
    mathAssignmentLanguage::Mult,
    mathAssignmentLanguage::ExpOp,
    Exp,
    mathAssignmentLanguage::Parenthesis,
    mathAssignmentLanguage::Number,
    mathAssignmentLanguage::Minus,
    mathAssignmentLanguage::Plus,
    mathAssignmentLanguage::Div,
    mathAssignmentLanguage::Exp,
    mathAssignmentLanguage::MathExp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expop_is_not_abstract():
    assert not inspect.isabstract(ExpOp)


def test_expop_constructor_exists():
    assert callable(ExpOp.__init__)


def test_expop_constructor_args():
    sig = inspect.signature(ExpOp.__init__)
    params = list(sig.parameters.keys())



def test_mathassignmentlanguage::mult_is_not_abstract():
    assert not inspect.isabstract(mathAssignmentLanguage::Mult)


def test_mathassignmentlanguage::mult_constructor_exists():
    assert callable(mathAssignmentLanguage::Mult.__init__)


def test_mathassignmentlanguage::mult_constructor_args():
    sig = inspect.signature(mathAssignmentLanguage::Mult.__init__)
    params = list(sig.parameters.keys())



def test_mathassignmentlanguage::expop_is_not_abstract():
    assert not inspect.isabstract(mathAssignmentLanguage::ExpOp)


def test_mathassignmentlanguage::expop_constructor_exists():
    assert callable(mathAssignmentLanguage::ExpOp.__init__)


def test_mathassignmentlanguage::expop_constructor_args():
    sig = inspect.signature(mathAssignmentLanguage::ExpOp.__init__)
    params = list(sig.parameters.keys())



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_mathassignmentlanguage::parenthesis_is_not_abstract():
    assert not inspect.isabstract(mathAssignmentLanguage::Parenthesis)


def test_mathassignmentlanguage::parenthesis_constructor_exists():
    assert callable(mathAssignmentLanguage::Parenthesis.__init__)


def test_mathassignmentlanguage::parenthesis_constructor_args():
    sig = inspect.signature(mathAssignmentLanguage::Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_mathassignmentlanguage::number_is_not_abstract():
    assert not inspect.isabstract(mathAssignmentLanguage::Number)


def test_mathassignmentlanguage::number_constructor_exists():
    assert callable(mathAssignmentLanguage::Number.__init__)


def test_mathassignmentlanguage::number_constructor_args():
    sig = inspect.signature(mathAssignmentLanguage::Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mathassignmentlanguage::number_has_value():
    assert hasattr(mathAssignmentLanguage::Number, "value")
    descriptor = None
    for klass in mathAssignmentLanguage::Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mathassignmentlanguage::minus_is_not_abstract():
    assert not inspect.isabstract(mathAssignmentLanguage::Minus)


def test_mathassignmentlanguage::minus_constructor_exists():
    assert callable(mathAssignmentLanguage::Minus.__init__)


def test_mathassignmentlanguage::minus_constructor_args():
    sig = inspect.signature(mathAssignmentLanguage::Minus.__init__)
    params = list(sig.parameters.keys())



def test_mathassignmentlanguage::plus_is_not_abstract():
    assert not inspect.isabstract(mathAssignmentLanguage::Plus)


def test_mathassignmentlanguage::plus_constructor_exists():
    assert callable(mathAssignmentLanguage::Plus.__init__)


def test_mathassignmentlanguage::plus_constructor_args():
    sig = inspect.signature(mathAssignmentLanguage::Plus.__init__)
    params = list(sig.parameters.keys())



def test_mathassignmentlanguage::div_is_not_abstract():
    assert not inspect.isabstract(mathAssignmentLanguage::Div)


def test_mathassignmentlanguage::div_constructor_exists():
    assert callable(mathAssignmentLanguage::Div.__init__)


def test_mathassignmentlanguage::div_constructor_args():
    sig = inspect.signature(mathAssignmentLanguage::Div.__init__)
    params = list(sig.parameters.keys())



def test_mathassignmentlanguage::exp_is_not_abstract():
    assert not inspect.isabstract(mathAssignmentLanguage::Exp)


def test_mathassignmentlanguage::exp_constructor_exists():
    assert callable(mathAssignmentLanguage::Exp.__init__)


def test_mathassignmentlanguage::exp_constructor_args():
    sig = inspect.signature(mathAssignmentLanguage::Exp.__init__)
    params = list(sig.parameters.keys())



def test_mathassignmentlanguage::mathexp_is_not_abstract():
    assert not inspect.isabstract(mathAssignmentLanguage::MathExp)


def test_mathassignmentlanguage::mathexp_constructor_exists():
    assert callable(mathAssignmentLanguage::MathExp.__init__)


def test_mathassignmentlanguage::mathexp_constructor_args():
    sig = inspect.signature(mathAssignmentLanguage::MathExp.__init__)
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
ExpOp_strategy = st.builds(
    ExpOp,
)
mathAssignmentLanguage::Mult_strategy = st.builds(
    mathAssignmentLanguage::Mult,
)
mathAssignmentLanguage::ExpOp_strategy = st.builds(
    mathAssignmentLanguage::ExpOp,
)
Exp_strategy = st.builds(
    Exp,
)
mathAssignmentLanguage::Parenthesis_strategy = st.builds(
    mathAssignmentLanguage::Parenthesis,
)
mathAssignmentLanguage::Number_strategy = st.builds(
    mathAssignmentLanguage::Number,
    value=
        st.integers()
)
mathAssignmentLanguage::Minus_strategy = st.builds(
    mathAssignmentLanguage::Minus,
)
mathAssignmentLanguage::Plus_strategy = st.builds(
    mathAssignmentLanguage::Plus,
)
mathAssignmentLanguage::Div_strategy = st.builds(
    mathAssignmentLanguage::Div,
)
mathAssignmentLanguage::Exp_strategy = st.builds(
    mathAssignmentLanguage::Exp,
)
mathAssignmentLanguage::MathExp_strategy = st.builds(
    mathAssignmentLanguage::MathExp,
)

@given(instance=ExpOp_strategy)
@settings(max_examples=50)
def test_expop_instantiation(instance):
    assert isinstance(instance, ExpOp)

@given(instance=mathAssignmentLanguage::Mult_strategy)
@settings(max_examples=50)
def test_mathassignmentlanguage::mult_instantiation(instance):
    assert isinstance(instance, mathAssignmentLanguage::Mult)

@given(instance=mathAssignmentLanguage::ExpOp_strategy)
@settings(max_examples=50)
def test_mathassignmentlanguage::expop_instantiation(instance):
    assert isinstance(instance, mathAssignmentLanguage::ExpOp)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=mathAssignmentLanguage::Parenthesis_strategy)
@settings(max_examples=50)
def test_mathassignmentlanguage::parenthesis_instantiation(instance):
    assert isinstance(instance, mathAssignmentLanguage::Parenthesis)

@given(instance=mathAssignmentLanguage::Number_strategy)
@settings(max_examples=50)
def test_mathassignmentlanguage::number_instantiation(instance):
    assert isinstance(instance, mathAssignmentLanguage::Number)

@given(instance=mathAssignmentLanguage::Number_strategy)
def test_mathassignmentlanguage::number_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=mathAssignmentLanguage::Number_strategy)
def test_mathassignmentlanguage::number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mathAssignmentLanguage::Minus_strategy)
@settings(max_examples=50)
def test_mathassignmentlanguage::minus_instantiation(instance):
    assert isinstance(instance, mathAssignmentLanguage::Minus)

@given(instance=mathAssignmentLanguage::Plus_strategy)
@settings(max_examples=50)
def test_mathassignmentlanguage::plus_instantiation(instance):
    assert isinstance(instance, mathAssignmentLanguage::Plus)

@given(instance=mathAssignmentLanguage::Div_strategy)
@settings(max_examples=50)
def test_mathassignmentlanguage::div_instantiation(instance):
    assert isinstance(instance, mathAssignmentLanguage::Div)

@given(instance=mathAssignmentLanguage::Exp_strategy)
@settings(max_examples=50)
def test_mathassignmentlanguage::exp_instantiation(instance):
    assert isinstance(instance, mathAssignmentLanguage::Exp)

@given(instance=mathAssignmentLanguage::MathExp_strategy)
@settings(max_examples=50)
def test_mathassignmentlanguage::mathexp_instantiation(instance):
    assert isinstance(instance, mathAssignmentLanguage::MathExp)
