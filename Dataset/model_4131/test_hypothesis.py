import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ExpOp,
    mdsdassignment2::Mult,
    mdsdassignment2::Sub,
    mdsdassignment2::Div,
    mdsdassignment2::Parenthesis,
    mdsdassignment2::ExpOp,
    mdsdassignment2::Exp,
    mdsdassignment2::MathExp,
    mdsdassignment2::Add,
    mdsdassignment2::Num,
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



def test_mdsdassignment2::mult_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2::Mult)


def test_mdsdassignment2::mult_constructor_exists():
    assert callable(mdsdassignment2::Mult.__init__)


def test_mdsdassignment2::mult_constructor_args():
    sig = inspect.signature(mdsdassignment2::Mult.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2::sub_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2::Sub)


def test_mdsdassignment2::sub_constructor_exists():
    assert callable(mdsdassignment2::Sub.__init__)


def test_mdsdassignment2::sub_constructor_args():
    sig = inspect.signature(mdsdassignment2::Sub.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2::div_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2::Div)


def test_mdsdassignment2::div_constructor_exists():
    assert callable(mdsdassignment2::Div.__init__)


def test_mdsdassignment2::div_constructor_args():
    sig = inspect.signature(mdsdassignment2::Div.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2::parenthesis_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2::Parenthesis)


def test_mdsdassignment2::parenthesis_constructor_exists():
    assert callable(mdsdassignment2::Parenthesis.__init__)


def test_mdsdassignment2::parenthesis_constructor_args():
    sig = inspect.signature(mdsdassignment2::Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2::expop_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2::ExpOp)


def test_mdsdassignment2::expop_constructor_exists():
    assert callable(mdsdassignment2::ExpOp.__init__)


def test_mdsdassignment2::expop_constructor_args():
    sig = inspect.signature(mdsdassignment2::ExpOp.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2::exp_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2::Exp)


def test_mdsdassignment2::exp_constructor_exists():
    assert callable(mdsdassignment2::Exp.__init__)


def test_mdsdassignment2::exp_constructor_args():
    sig = inspect.signature(mdsdassignment2::Exp.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2::mathexp_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2::MathExp)


def test_mdsdassignment2::mathexp_constructor_exists():
    assert callable(mdsdassignment2::MathExp.__init__)


def test_mdsdassignment2::mathexp_constructor_args():
    sig = inspect.signature(mdsdassignment2::MathExp.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2::add_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2::Add)


def test_mdsdassignment2::add_constructor_exists():
    assert callable(mdsdassignment2::Add.__init__)


def test_mdsdassignment2::add_constructor_args():
    sig = inspect.signature(mdsdassignment2::Add.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2::num_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2::Num)


def test_mdsdassignment2::num_constructor_exists():
    assert callable(mdsdassignment2::Num.__init__)


def test_mdsdassignment2::num_constructor_args():
    sig = inspect.signature(mdsdassignment2::Num.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mdsdassignment2::num_has_value():
    assert hasattr(mdsdassignment2::Num, "value")
    descriptor = None
    for klass in mdsdassignment2::Num.__mro__:
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
ExpOp_strategy = st.builds(
    ExpOp,
)
mdsdassignment2::Mult_strategy = st.builds(
    mdsdassignment2::Mult,
)
mdsdassignment2::Sub_strategy = st.builds(
    mdsdassignment2::Sub,
)
mdsdassignment2::Div_strategy = st.builds(
    mdsdassignment2::Div,
)
mdsdassignment2::Parenthesis_strategy = st.builds(
    mdsdassignment2::Parenthesis,
)
mdsdassignment2::ExpOp_strategy = st.builds(
    mdsdassignment2::ExpOp,
)
mdsdassignment2::Exp_strategy = st.builds(
    mdsdassignment2::Exp,
)
mdsdassignment2::MathExp_strategy = st.builds(
    mdsdassignment2::MathExp,
)
mdsdassignment2::Add_strategy = st.builds(
    mdsdassignment2::Add,
)
mdsdassignment2::Num_strategy = st.builds(
    mdsdassignment2::Num,
    value=
        st.integers()
)

@given(instance=ExpOp_strategy)
@settings(max_examples=50)
def test_expop_instantiation(instance):
    assert isinstance(instance, ExpOp)

@given(instance=mdsdassignment2::Mult_strategy)
@settings(max_examples=50)
def test_mdsdassignment2::mult_instantiation(instance):
    assert isinstance(instance, mdsdassignment2::Mult)

@given(instance=mdsdassignment2::Sub_strategy)
@settings(max_examples=50)
def test_mdsdassignment2::sub_instantiation(instance):
    assert isinstance(instance, mdsdassignment2::Sub)

@given(instance=mdsdassignment2::Div_strategy)
@settings(max_examples=50)
def test_mdsdassignment2::div_instantiation(instance):
    assert isinstance(instance, mdsdassignment2::Div)

@given(instance=mdsdassignment2::Parenthesis_strategy)
@settings(max_examples=50)
def test_mdsdassignment2::parenthesis_instantiation(instance):
    assert isinstance(instance, mdsdassignment2::Parenthesis)

@given(instance=mdsdassignment2::ExpOp_strategy)
@settings(max_examples=50)
def test_mdsdassignment2::expop_instantiation(instance):
    assert isinstance(instance, mdsdassignment2::ExpOp)

@given(instance=mdsdassignment2::Exp_strategy)
@settings(max_examples=50)
def test_mdsdassignment2::exp_instantiation(instance):
    assert isinstance(instance, mdsdassignment2::Exp)

@given(instance=mdsdassignment2::MathExp_strategy)
@settings(max_examples=50)
def test_mdsdassignment2::mathexp_instantiation(instance):
    assert isinstance(instance, mdsdassignment2::MathExp)

@given(instance=mdsdassignment2::Add_strategy)
@settings(max_examples=50)
def test_mdsdassignment2::add_instantiation(instance):
    assert isinstance(instance, mdsdassignment2::Add)

@given(instance=mdsdassignment2::Num_strategy)
@settings(max_examples=50)
def test_mdsdassignment2::num_instantiation(instance):
    assert isinstance(instance, mdsdassignment2::Num)

@given(instance=mdsdassignment2::Num_strategy)
def test_mdsdassignment2::num_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=mdsdassignment2::Num_strategy)
def test_mdsdassignment2::num_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
