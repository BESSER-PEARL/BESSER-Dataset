import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Primary,
    mathInterpeter_Number,
    mathInterpeter_Parenthesis,
    Exp,
    mathInterpeter_Plus,
    mathInterpeter_Div,
    mathInterpeter_Minus,
    mathInterpeter_Mult,
    mathInterpeter_Primary,
    mathInterpeter_Exp,
    mathInterpeter_MathExp,
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



def test_mathinterpeter_number_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter_Number)


def test_mathinterpeter_number_constructor_exists():
    assert callable(mathInterpeter_Number.__init__)


def test_mathinterpeter_number_constructor_args():
    sig = inspect.signature(mathInterpeter_Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mathinterpeter_number_has_value():
    assert hasattr(mathInterpeter_Number, "value")
    descriptor = None
    for klass in mathInterpeter_Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mathinterpeter_parenthesis_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter_Parenthesis)


def test_mathinterpeter_parenthesis_constructor_exists():
    assert callable(mathInterpeter_Parenthesis.__init__)


def test_mathinterpeter_parenthesis_constructor_args():
    sig = inspect.signature(mathInterpeter_Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpeter_plus_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter_Plus)


def test_mathinterpeter_plus_constructor_exists():
    assert callable(mathInterpeter_Plus.__init__)


def test_mathinterpeter_plus_constructor_args():
    sig = inspect.signature(mathInterpeter_Plus.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpeter_div_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter_Div)


def test_mathinterpeter_div_constructor_exists():
    assert callable(mathInterpeter_Div.__init__)


def test_mathinterpeter_div_constructor_args():
    sig = inspect.signature(mathInterpeter_Div.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpeter_minus_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter_Minus)


def test_mathinterpeter_minus_constructor_exists():
    assert callable(mathInterpeter_Minus.__init__)


def test_mathinterpeter_minus_constructor_args():
    sig = inspect.signature(mathInterpeter_Minus.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpeter_mult_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter_Mult)


def test_mathinterpeter_mult_constructor_exists():
    assert callable(mathInterpeter_Mult.__init__)


def test_mathinterpeter_mult_constructor_args():
    sig = inspect.signature(mathInterpeter_Mult.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpeter_primary_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter_Primary)


def test_mathinterpeter_primary_constructor_exists():
    assert callable(mathInterpeter_Primary.__init__)


def test_mathinterpeter_primary_constructor_args():
    sig = inspect.signature(mathInterpeter_Primary.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpeter_exp_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter_Exp)


def test_mathinterpeter_exp_constructor_exists():
    assert callable(mathInterpeter_Exp.__init__)


def test_mathinterpeter_exp_constructor_args():
    sig = inspect.signature(mathInterpeter_Exp.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpeter_mathexp_is_not_abstract():
    assert not inspect.isabstract(mathInterpeter_MathExp)


def test_mathinterpeter_mathexp_constructor_exists():
    assert callable(mathInterpeter_MathExp.__init__)


def test_mathinterpeter_mathexp_constructor_args():
    sig = inspect.signature(mathInterpeter_MathExp.__init__)
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
mathInterpeter_Number_strategy = st.builds(
    mathInterpeter_Number,
    value=
        st.integers()
)
mathInterpeter_Parenthesis_strategy = st.builds(
    mathInterpeter_Parenthesis,
)
Exp_strategy = st.builds(
    Exp,
)
mathInterpeter_Plus_strategy = st.builds(
    mathInterpeter_Plus,
)
mathInterpeter_Div_strategy = st.builds(
    mathInterpeter_Div,
)
mathInterpeter_Minus_strategy = st.builds(
    mathInterpeter_Minus,
)
mathInterpeter_Mult_strategy = st.builds(
    mathInterpeter_Mult,
)
mathInterpeter_Primary_strategy = st.builds(
    mathInterpeter_Primary,
)
mathInterpeter_Exp_strategy = st.builds(
    mathInterpeter_Exp,
)
mathInterpeter_MathExp_strategy = st.builds(
    mathInterpeter_MathExp,
)

@given(instance=Primary_strategy)
@settings(max_examples=50)
def test_primary_instantiation(instance):
    assert isinstance(instance, Primary)

@given(instance=mathInterpeter_Number_strategy)
@settings(max_examples=50)
def test_mathinterpeter_number_instantiation(instance):
    assert isinstance(instance, mathInterpeter_Number)



@given(instance=mathInterpeter_Number_strategy)
def test_mathinterpeter_number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mathInterpeter_Parenthesis_strategy)
@settings(max_examples=50)
def test_mathinterpeter_parenthesis_instantiation(instance):
    assert isinstance(instance, mathInterpeter_Parenthesis)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=mathInterpeter_Plus_strategy)
@settings(max_examples=50)
def test_mathinterpeter_plus_instantiation(instance):
    assert isinstance(instance, mathInterpeter_Plus)

@given(instance=mathInterpeter_Div_strategy)
@settings(max_examples=50)
def test_mathinterpeter_div_instantiation(instance):
    assert isinstance(instance, mathInterpeter_Div)

@given(instance=mathInterpeter_Minus_strategy)
@settings(max_examples=50)
def test_mathinterpeter_minus_instantiation(instance):
    assert isinstance(instance, mathInterpeter_Minus)

@given(instance=mathInterpeter_Mult_strategy)
@settings(max_examples=50)
def test_mathinterpeter_mult_instantiation(instance):
    assert isinstance(instance, mathInterpeter_Mult)

@given(instance=mathInterpeter_Primary_strategy)
@settings(max_examples=50)
def test_mathinterpeter_primary_instantiation(instance):
    assert isinstance(instance, mathInterpeter_Primary)

@given(instance=mathInterpeter_Exp_strategy)
@settings(max_examples=50)
def test_mathinterpeter_exp_instantiation(instance):
    assert isinstance(instance, mathInterpeter_Exp)

@given(instance=mathInterpeter_MathExp_strategy)
@settings(max_examples=50)
def test_mathinterpeter_mathexp_instantiation(instance):
    assert isinstance(instance, mathInterpeter_MathExp)
