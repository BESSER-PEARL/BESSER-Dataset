import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Exp,
    exp::Add,
    exp::Lit,
    exp::Exp,
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



def test_exp::add_is_not_abstract():
    assert not inspect.isabstract(exp::Add)


def test_exp::add_constructor_exists():
    assert callable(exp::Add.__init__)


def test_exp::add_constructor_args():
    sig = inspect.signature(exp::Add.__init__)
    params = list(sig.parameters.keys())



def test_exp::lit_is_not_abstract():
    assert not inspect.isabstract(exp::Lit)


def test_exp::lit_constructor_exists():
    assert callable(exp::Lit.__init__)


def test_exp::lit_constructor_args():
    sig = inspect.signature(exp::Lit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_exp::lit_has_value():
    assert hasattr(exp::Lit, "value")
    descriptor = None
    for klass in exp::Lit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_exp::exp_is_not_abstract():
    assert not inspect.isabstract(exp::Exp)


def test_exp::exp_constructor_exists():
    assert callable(exp::Exp.__init__)


def test_exp::exp_constructor_args():
    sig = inspect.signature(exp::Exp.__init__)
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
exp::Add_strategy = st.builds(
    exp::Add,
)
exp::Lit_strategy = st.builds(
    exp::Lit,
    value=
        st.integers()
)
exp::Exp_strategy = st.builds(
    exp::Exp,
)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=exp::Add_strategy)
@settings(max_examples=50)
def test_exp::add_instantiation(instance):
    assert isinstance(instance, exp::Add)

@given(instance=exp::Lit_strategy)
@settings(max_examples=50)
def test_exp::lit_instantiation(instance):
    assert isinstance(instance, exp::Lit)

@given(instance=exp::Lit_strategy)
def test_exp::lit_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=exp::Lit_strategy)
def test_exp::lit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=exp::Exp_strategy)
@settings(max_examples=50)
def test_exp::exp_instantiation(instance):
    assert isinstance(instance, exp::Exp)
