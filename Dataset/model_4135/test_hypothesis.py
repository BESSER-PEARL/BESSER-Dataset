import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Exp,
    mathInterpreter::Mult,
    mathInterpreter::Minus,
    mathInterpreter::Div,
    mathInterpreter::Plus,
    mathInterpreter::Exp,
    mathInterpreter::MathExp,
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



def test_mathinterpreter::mult_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Mult)


def test_mathinterpreter::mult_constructor_exists():
    assert callable(mathInterpreter::Mult.__init__)


def test_mathinterpreter::mult_constructor_args():
    sig = inspect.signature(mathInterpreter::Mult.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mathinterpreter::mult_has_op():
    assert hasattr(mathInterpreter::Mult, "op")
    descriptor = None
    for klass in mathInterpreter::Mult.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mathinterpreter::minus_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Minus)


def test_mathinterpreter::minus_constructor_exists():
    assert callable(mathInterpreter::Minus.__init__)


def test_mathinterpreter::minus_constructor_args():
    sig = inspect.signature(mathInterpreter::Minus.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::div_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Div)


def test_mathinterpreter::div_constructor_exists():
    assert callable(mathInterpreter::Div.__init__)


def test_mathinterpreter::div_constructor_args():
    sig = inspect.signature(mathInterpreter::Div.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mathinterpreter::div_has_op():
    assert hasattr(mathInterpreter::Div, "op")
    descriptor = None
    for klass in mathInterpreter::Div.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mathinterpreter::plus_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Plus)


def test_mathinterpreter::plus_constructor_exists():
    assert callable(mathInterpreter::Plus.__init__)


def test_mathinterpreter::plus_constructor_args():
    sig = inspect.signature(mathInterpreter::Plus.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::exp_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Exp)


def test_mathinterpreter::exp_constructor_exists():
    assert callable(mathInterpreter::Exp.__init__)


def test_mathinterpreter::exp_constructor_args():
    sig = inspect.signature(mathInterpreter::Exp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mathinterpreter::exp_has_value():
    assert hasattr(mathInterpreter::Exp, "value")
    descriptor = None
    for klass in mathInterpreter::Exp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mathinterpreter::mathexp_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::MathExp)


def test_mathinterpreter::mathexp_constructor_exists():
    assert callable(mathInterpreter::MathExp.__init__)


def test_mathinterpreter::mathexp_constructor_args():
    sig = inspect.signature(mathInterpreter::MathExp.__init__)
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
mathInterpreter::Mult_strategy = st.builds(
    mathInterpreter::Mult,
    op=
        safe_text
)
mathInterpreter::Minus_strategy = st.builds(
    mathInterpreter::Minus,
)
mathInterpreter::Div_strategy = st.builds(
    mathInterpreter::Div,
    op=
        safe_text
)
mathInterpreter::Plus_strategy = st.builds(
    mathInterpreter::Plus,
)
mathInterpreter::Exp_strategy = st.builds(
    mathInterpreter::Exp,
    value=
        st.integers()
)
mathInterpreter::MathExp_strategy = st.builds(
    mathInterpreter::MathExp,
)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=mathInterpreter::Mult_strategy)
@settings(max_examples=50)
def test_mathinterpreter::mult_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Mult)

@given(instance=mathInterpreter::Mult_strategy)
def test_mathinterpreter::mult_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=mathInterpreter::Mult_strategy)
def test_mathinterpreter::mult_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=mathInterpreter::Minus_strategy)
@settings(max_examples=50)
def test_mathinterpreter::minus_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Minus)

@given(instance=mathInterpreter::Div_strategy)
@settings(max_examples=50)
def test_mathinterpreter::div_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Div)

@given(instance=mathInterpreter::Div_strategy)
def test_mathinterpreter::div_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=mathInterpreter::Div_strategy)
def test_mathinterpreter::div_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=mathInterpreter::Plus_strategy)
@settings(max_examples=50)
def test_mathinterpreter::plus_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Plus)

@given(instance=mathInterpreter::Exp_strategy)
@settings(max_examples=50)
def test_mathinterpreter::exp_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Exp)

@given(instance=mathInterpreter::Exp_strategy)
def test_mathinterpreter::exp_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=mathInterpreter::Exp_strategy)
def test_mathinterpreter::exp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mathInterpreter::MathExp_strategy)
@settings(max_examples=50)
def test_mathinterpreter::mathexp_instantiation(instance):
    assert isinstance(instance, mathInterpreter::MathExp)
