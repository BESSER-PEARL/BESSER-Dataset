import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Exp,
    exp_Add,
    exp_Lit,
    exp_Exp,
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



def test_exp_add_is_not_abstract():
    assert not inspect.isabstract(exp_Add)


def test_exp_add_constructor_exists():
    assert callable(exp_Add.__init__)


def test_exp_add_constructor_args():
    sig = inspect.signature(exp_Add.__init__)
    params = list(sig.parameters.keys())



def test_exp_lit_is_not_abstract():
    assert not inspect.isabstract(exp_Lit)


def test_exp_lit_constructor_exists():
    assert callable(exp_Lit.__init__)


def test_exp_lit_constructor_args():
    sig = inspect.signature(exp_Lit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_exp_lit_has_value():
    assert hasattr(exp_Lit, "value")
    descriptor = None
    for klass in exp_Lit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_exp_exp_is_not_abstract():
    assert not inspect.isabstract(exp_Exp)


def test_exp_exp_constructor_exists():
    assert callable(exp_Exp.__init__)


def test_exp_exp_constructor_args():
    sig = inspect.signature(exp_Exp.__init__)
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
exp_Add_strategy = st.builds(
    exp_Add,
)
exp_Lit_strategy = st.builds(
    exp_Lit,
    value=
        st.integers()
)
exp_Exp_strategy = st.builds(
    exp_Exp,
)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=exp_Add_strategy)
@settings(max_examples=50)
def test_exp_add_instantiation(instance):
    assert isinstance(instance, exp_Add)

@given(instance=exp_Lit_strategy)
@settings(max_examples=50)
def test_exp_lit_instantiation(instance):
    assert isinstance(instance, exp_Lit)



@given(instance=exp_Lit_strategy)
def test_exp_lit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=exp_Exp_strategy)
@settings(max_examples=50)
def test_exp_exp_instantiation(instance):
    assert isinstance(instance, exp_Exp)
