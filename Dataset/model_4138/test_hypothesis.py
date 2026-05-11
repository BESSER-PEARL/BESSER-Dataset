import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    mathInterpreter::Divide,
    mathInterpreter::Multiply,
    mathInterpreter::Plus,
    mathInterpreter::Minus,
    mathInterpreter::Exp,
    mathInterpreter::Expression,
    mathInterpreter::MathExp,
    mathInterpreter::Num,
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



def test_mathinterpreter::divide_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Divide)


def test_mathinterpreter::divide_constructor_exists():
    assert callable(mathInterpreter::Divide.__init__)


def test_mathinterpreter::divide_constructor_args():
    sig = inspect.signature(mathInterpreter::Divide.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::multiply_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Multiply)


def test_mathinterpreter::multiply_constructor_exists():
    assert callable(mathInterpreter::Multiply.__init__)


def test_mathinterpreter::multiply_constructor_args():
    sig = inspect.signature(mathInterpreter::Multiply.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::plus_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Plus)


def test_mathinterpreter::plus_constructor_exists():
    assert callable(mathInterpreter::Plus.__init__)


def test_mathinterpreter::plus_constructor_args():
    sig = inspect.signature(mathInterpreter::Plus.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::minus_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Minus)


def test_mathinterpreter::minus_constructor_exists():
    assert callable(mathInterpreter::Minus.__init__)


def test_mathinterpreter::minus_constructor_args():
    sig = inspect.signature(mathInterpreter::Minus.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::exp_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Exp)


def test_mathinterpreter::exp_constructor_exists():
    assert callable(mathInterpreter::Exp.__init__)


def test_mathinterpreter::exp_constructor_args():
    sig = inspect.signature(mathInterpreter::Exp.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::expression_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Expression)


def test_mathinterpreter::expression_constructor_exists():
    assert callable(mathInterpreter::Expression.__init__)


def test_mathinterpreter::expression_constructor_args():
    sig = inspect.signature(mathInterpreter::Expression.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::mathexp_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::MathExp)


def test_mathinterpreter::mathexp_constructor_exists():
    assert callable(mathInterpreter::MathExp.__init__)


def test_mathinterpreter::mathexp_constructor_args():
    sig = inspect.signature(mathInterpreter::MathExp.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::num_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Num)


def test_mathinterpreter::num_constructor_exists():
    assert callable(mathInterpreter::Num.__init__)


def test_mathinterpreter::num_constructor_args():
    sig = inspect.signature(mathInterpreter::Num.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mathinterpreter::num_has_value():
    assert hasattr(mathInterpreter::Num, "value")
    descriptor = None
    for klass in mathInterpreter::Num.__mro__:
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
mathInterpreter::Divide_strategy = st.builds(
    mathInterpreter::Divide,
)
mathInterpreter::Multiply_strategy = st.builds(
    mathInterpreter::Multiply,
)
mathInterpreter::Plus_strategy = st.builds(
    mathInterpreter::Plus,
)
mathInterpreter::Minus_strategy = st.builds(
    mathInterpreter::Minus,
)
mathInterpreter::Exp_strategy = st.builds(
    mathInterpreter::Exp,
)
mathInterpreter::Expression_strategy = st.builds(
    mathInterpreter::Expression,
)
mathInterpreter::MathExp_strategy = st.builds(
    mathInterpreter::MathExp,
)
mathInterpreter::Num_strategy = st.builds(
    mathInterpreter::Num,
    value=
        st.integers()
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=mathInterpreter::Divide_strategy)
@settings(max_examples=50)
def test_mathinterpreter::divide_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Divide)

@given(instance=mathInterpreter::Multiply_strategy)
@settings(max_examples=50)
def test_mathinterpreter::multiply_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Multiply)

@given(instance=mathInterpreter::Plus_strategy)
@settings(max_examples=50)
def test_mathinterpreter::plus_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Plus)

@given(instance=mathInterpreter::Minus_strategy)
@settings(max_examples=50)
def test_mathinterpreter::minus_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Minus)

@given(instance=mathInterpreter::Exp_strategy)
@settings(max_examples=50)
def test_mathinterpreter::exp_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Exp)

@given(instance=mathInterpreter::Expression_strategy)
@settings(max_examples=50)
def test_mathinterpreter::expression_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Expression)

@given(instance=mathInterpreter::MathExp_strategy)
@settings(max_examples=50)
def test_mathinterpreter::mathexp_instantiation(instance):
    assert isinstance(instance, mathInterpreter::MathExp)

@given(instance=mathInterpreter::Num_strategy)
@settings(max_examples=50)
def test_mathinterpreter::num_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Num)

@given(instance=mathInterpreter::Num_strategy)
def test_mathinterpreter::num_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=mathInterpreter::Num_strategy)
def test_mathinterpreter::num_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
