import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    myMath::Sub,
    myMath::Num,
    myMath::Mult,
    myMath::Add,
    myMath::Expression,
    myMath::MathExp,
    myMath::Div,
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



def test_mymath::sub_is_not_abstract():
    assert not inspect.isabstract(myMath::Sub)


def test_mymath::sub_constructor_exists():
    assert callable(myMath::Sub.__init__)


def test_mymath::sub_constructor_args():
    sig = inspect.signature(myMath::Sub.__init__)
    params = list(sig.parameters.keys())



def test_mymath::num_is_not_abstract():
    assert not inspect.isabstract(myMath::Num)


def test_mymath::num_constructor_exists():
    assert callable(myMath::Num.__init__)


def test_mymath::num_constructor_args():
    sig = inspect.signature(myMath::Num.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mymath::num_has_value():
    assert hasattr(myMath::Num, "value")
    descriptor = None
    for klass in myMath::Num.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mymath::mult_is_not_abstract():
    assert not inspect.isabstract(myMath::Mult)


def test_mymath::mult_constructor_exists():
    assert callable(myMath::Mult.__init__)


def test_mymath::mult_constructor_args():
    sig = inspect.signature(myMath::Mult.__init__)
    params = list(sig.parameters.keys())



def test_mymath::add_is_not_abstract():
    assert not inspect.isabstract(myMath::Add)


def test_mymath::add_constructor_exists():
    assert callable(myMath::Add.__init__)


def test_mymath::add_constructor_args():
    sig = inspect.signature(myMath::Add.__init__)
    params = list(sig.parameters.keys())



def test_mymath::expression_is_not_abstract():
    assert not inspect.isabstract(myMath::Expression)


def test_mymath::expression_constructor_exists():
    assert callable(myMath::Expression.__init__)


def test_mymath::expression_constructor_args():
    sig = inspect.signature(myMath::Expression.__init__)
    params = list(sig.parameters.keys())



def test_mymath::mathexp_is_not_abstract():
    assert not inspect.isabstract(myMath::MathExp)


def test_mymath::mathexp_constructor_exists():
    assert callable(myMath::MathExp.__init__)


def test_mymath::mathexp_constructor_args():
    sig = inspect.signature(myMath::MathExp.__init__)
    params = list(sig.parameters.keys())



def test_mymath::div_is_not_abstract():
    assert not inspect.isabstract(myMath::Div)


def test_mymath::div_constructor_exists():
    assert callable(myMath::Div.__init__)


def test_mymath::div_constructor_args():
    sig = inspect.signature(myMath::Div.__init__)
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
myMath::Sub_strategy = st.builds(
    myMath::Sub,
)
myMath::Num_strategy = st.builds(
    myMath::Num,
    value=
        st.integers()
)
myMath::Mult_strategy = st.builds(
    myMath::Mult,
)
myMath::Add_strategy = st.builds(
    myMath::Add,
)
myMath::Expression_strategy = st.builds(
    myMath::Expression,
)
myMath::MathExp_strategy = st.builds(
    myMath::MathExp,
)
myMath::Div_strategy = st.builds(
    myMath::Div,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=myMath::Sub_strategy)
@settings(max_examples=50)
def test_mymath::sub_instantiation(instance):
    assert isinstance(instance, myMath::Sub)

@given(instance=myMath::Num_strategy)
@settings(max_examples=50)
def test_mymath::num_instantiation(instance):
    assert isinstance(instance, myMath::Num)

@given(instance=myMath::Num_strategy)
def test_mymath::num_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=myMath::Num_strategy)
def test_mymath::num_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myMath::Mult_strategy)
@settings(max_examples=50)
def test_mymath::mult_instantiation(instance):
    assert isinstance(instance, myMath::Mult)

@given(instance=myMath::Add_strategy)
@settings(max_examples=50)
def test_mymath::add_instantiation(instance):
    assert isinstance(instance, myMath::Add)

@given(instance=myMath::Expression_strategy)
@settings(max_examples=50)
def test_mymath::expression_instantiation(instance):
    assert isinstance(instance, myMath::Expression)

@given(instance=myMath::MathExp_strategy)
@settings(max_examples=50)
def test_mymath::mathexp_instantiation(instance):
    assert isinstance(instance, myMath::MathExp)

@given(instance=myMath::Div_strategy)
@settings(max_examples=50)
def test_mymath::div_instantiation(instance):
    assert isinstance(instance, myMath::Div)
