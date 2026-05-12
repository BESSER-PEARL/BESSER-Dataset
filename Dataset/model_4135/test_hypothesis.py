import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Exp,
    mathInterpreter_Minus,
    mathInterpreter_Div,
    mathInterpreter_Mult,
    mathInterpreter_Plus,
    mathInterpreter_Exp,
    mathInterpreter_MathExp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter_minus_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter_Minus)


def test_mathinterpreter_minus_constructor_exists():
    assert callable(mathInterpreter_Minus.__init__)


def test_mathinterpreter_minus_constructor_args():
    sig = inspect.signature(mathInterpreter_Minus.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter_div_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter_Div)


def test_mathinterpreter_div_constructor_exists():
    assert callable(mathInterpreter_Div.__init__)


def test_mathinterpreter_div_constructor_args():
    sig = inspect.signature(mathInterpreter_Div.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mathinterpreter_div_has_op():
    assert hasattr(mathInterpreter_Div, "op")
    descriptor = None
    for klass in mathInterpreter_Div.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mathinterpreter_mult_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter_Mult)


def test_mathinterpreter_mult_constructor_exists():
    assert callable(mathInterpreter_Mult.__init__)


def test_mathinterpreter_mult_constructor_args():
    sig = inspect.signature(mathInterpreter_Mult.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mathinterpreter_mult_has_op():
    assert hasattr(mathInterpreter_Mult, "op")
    descriptor = None
    for klass in mathInterpreter_Mult.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mathinterpreter_plus_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter_Plus)


def test_mathinterpreter_plus_constructor_exists():
    assert callable(mathInterpreter_Plus.__init__)


def test_mathinterpreter_plus_constructor_args():
    sig = inspect.signature(mathInterpreter_Plus.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter_exp_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter_Exp)


def test_mathinterpreter_exp_constructor_exists():
    assert callable(mathInterpreter_Exp.__init__)


def test_mathinterpreter_exp_constructor_args():
    sig = inspect.signature(mathInterpreter_Exp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mathinterpreter_exp_has_value():
    assert hasattr(mathInterpreter_Exp, "value")
    descriptor = None
    for klass in mathInterpreter_Exp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mathinterpreter_mathexp_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter_MathExp)


def test_mathinterpreter_mathexp_constructor_exists():
    assert callable(mathInterpreter_MathExp.__init__)


def test_mathinterpreter_mathexp_constructor_args():
    sig = inspect.signature(mathInterpreter_MathExp.__init__)
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
Exp_strategy = st.builds(
    Exp,
)
mathInterpreter_Minus_strategy = st.builds(
    mathInterpreter_Minus,
)
mathInterpreter_Div_strategy = st.builds(
    mathInterpreter_Div,
    op=
        safe_text
)
mathInterpreter_Mult_strategy = st.builds(
    mathInterpreter_Mult,
    op=
        safe_text
)
mathInterpreter_Plus_strategy = st.builds(
    mathInterpreter_Plus,
)
mathInterpreter_Exp_strategy = st.builds(
    mathInterpreter_Exp,
    value=
        st.integers()
)
mathInterpreter_MathExp_strategy = st.builds(
    mathInterpreter_MathExp,
)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=mathInterpreter_Minus_strategy)
@settings(max_examples=50)
def test_mathinterpreter_minus_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Minus)

@given(instance=mathInterpreter_Div_strategy)
@settings(max_examples=50)
def test_mathinterpreter_div_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Div)



@given(instance=mathInterpreter_Div_strategy)
def test_mathinterpreter_div_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=mathInterpreter_Mult_strategy)
@settings(max_examples=50)
def test_mathinterpreter_mult_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Mult)



@given(instance=mathInterpreter_Mult_strategy)
def test_mathinterpreter_mult_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=mathInterpreter_Plus_strategy)
@settings(max_examples=50)
def test_mathinterpreter_plus_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Plus)

@given(instance=mathInterpreter_Exp_strategy)
@settings(max_examples=50)
def test_mathinterpreter_exp_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Exp)



@given(instance=mathInterpreter_Exp_strategy)
def test_mathinterpreter_exp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mathInterpreter_MathExp_strategy)
@settings(max_examples=50)
def test_mathinterpreter_mathexp_instantiation(instance):
    assert isinstance(instance, mathInterpreter_MathExp)
