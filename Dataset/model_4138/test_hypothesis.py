import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    mathInterpreter_Plus,
    mathInterpreter_Minus,
    mathInterpreter_Divide,
    mathInterpreter_Multiply,
    mathInterpreter_Exp,
    mathInterpreter_Expression,
    mathInterpreter_MathExp,
    mathInterpreter_Num,
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



def test_mathinterpreter_plus_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter_Plus)


def test_mathinterpreter_plus_constructor_exists():
    assert callable(mathInterpreter_Plus.__init__)


def test_mathinterpreter_plus_constructor_args():
    sig = inspect.signature(mathInterpreter_Plus.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter_minus_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter_Minus)


def test_mathinterpreter_minus_constructor_exists():
    assert callable(mathInterpreter_Minus.__init__)


def test_mathinterpreter_minus_constructor_args():
    sig = inspect.signature(mathInterpreter_Minus.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter_divide_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter_Divide)


def test_mathinterpreter_divide_constructor_exists():
    assert callable(mathInterpreter_Divide.__init__)


def test_mathinterpreter_divide_constructor_args():
    sig = inspect.signature(mathInterpreter_Divide.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter_multiply_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter_Multiply)


def test_mathinterpreter_multiply_constructor_exists():
    assert callable(mathInterpreter_Multiply.__init__)


def test_mathinterpreter_multiply_constructor_args():
    sig = inspect.signature(mathInterpreter_Multiply.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter_exp_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter_Exp)


def test_mathinterpreter_exp_constructor_exists():
    assert callable(mathInterpreter_Exp.__init__)


def test_mathinterpreter_exp_constructor_args():
    sig = inspect.signature(mathInterpreter_Exp.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter_expression_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter_Expression)


def test_mathinterpreter_expression_constructor_exists():
    assert callable(mathInterpreter_Expression.__init__)


def test_mathinterpreter_expression_constructor_args():
    sig = inspect.signature(mathInterpreter_Expression.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter_mathexp_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter_MathExp)


def test_mathinterpreter_mathexp_constructor_exists():
    assert callable(mathInterpreter_MathExp.__init__)


def test_mathinterpreter_mathexp_constructor_args():
    sig = inspect.signature(mathInterpreter_MathExp.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter_num_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter_Num)


def test_mathinterpreter_num_constructor_exists():
    assert callable(mathInterpreter_Num.__init__)


def test_mathinterpreter_num_constructor_args():
    sig = inspect.signature(mathInterpreter_Num.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mathinterpreter_num_has_value():
    assert hasattr(mathInterpreter_Num, "value")
    descriptor = None
    for klass in mathInterpreter_Num.__mro__:
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
mathInterpreter_Plus_strategy = st.builds(
    mathInterpreter_Plus,
)
mathInterpreter_Minus_strategy = st.builds(
    mathInterpreter_Minus,
)
mathInterpreter_Divide_strategy = st.builds(
    mathInterpreter_Divide,
)
mathInterpreter_Multiply_strategy = st.builds(
    mathInterpreter_Multiply,
)
mathInterpreter_Exp_strategy = st.builds(
    mathInterpreter_Exp,
)
mathInterpreter_Expression_strategy = st.builds(
    mathInterpreter_Expression,
)
mathInterpreter_MathExp_strategy = st.builds(
    mathInterpreter_MathExp,
)
mathInterpreter_Num_strategy = st.builds(
    mathInterpreter_Num,
    value=
        st.integers()
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=mathInterpreter_Plus_strategy)
@settings(max_examples=50)
def test_mathinterpreter_plus_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Plus)

@given(instance=mathInterpreter_Minus_strategy)
@settings(max_examples=50)
def test_mathinterpreter_minus_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Minus)

@given(instance=mathInterpreter_Divide_strategy)
@settings(max_examples=50)
def test_mathinterpreter_divide_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Divide)

@given(instance=mathInterpreter_Multiply_strategy)
@settings(max_examples=50)
def test_mathinterpreter_multiply_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Multiply)

@given(instance=mathInterpreter_Exp_strategy)
@settings(max_examples=50)
def test_mathinterpreter_exp_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Exp)

@given(instance=mathInterpreter_Expression_strategy)
@settings(max_examples=50)
def test_mathinterpreter_expression_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Expression)

@given(instance=mathInterpreter_MathExp_strategy)
@settings(max_examples=50)
def test_mathinterpreter_mathexp_instantiation(instance):
    assert isinstance(instance, mathInterpreter_MathExp)

@given(instance=mathInterpreter_Num_strategy)
@settings(max_examples=50)
def test_mathinterpreter_num_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Num)



@given(instance=mathInterpreter_Num_strategy)
def test_mathinterpreter_num_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
