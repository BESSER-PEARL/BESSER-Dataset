import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    abc_A,
    abc_B,
    abc_C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abc_a_is_not_abstract():
    assert not inspect.isabstract(abc_A)


def test_abc_a_constructor_exists():
    assert callable(abc_A.__init__)


def test_abc_a_constructor_args():
    sig = inspect.signature(abc_A.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_abc_a_has_x():
    assert hasattr(abc_A, "x")
    descriptor = None
    for klass in abc_A.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_abc_b_is_not_abstract():
    assert not inspect.isabstract(abc_B)


def test_abc_b_constructor_exists():
    assert callable(abc_B.__init__)


def test_abc_b_constructor_args():
    sig = inspect.signature(abc_B.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_abc_b_has_x():
    assert hasattr(abc_B, "x")
    descriptor = None
    for klass in abc_B.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_abc_c_is_not_abstract():
    assert not inspect.isabstract(abc_C)


def test_abc_c_constructor_exists():
    assert callable(abc_C.__init__)


def test_abc_c_constructor_args():
    sig = inspect.signature(abc_C.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_abc_c_has_x():
    assert hasattr(abc_C, "x")
    descriptor = None
    for klass in abc_C.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
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
abc_A_strategy = st.builds(
    abc_A,
    x=
        st.integers()
)
abc_B_strategy = st.builds(
    abc_B,
    x=
        st.integers()
)
abc_C_strategy = st.builds(
    abc_C,
    x=
        st.integers()
)

@given(instance=abc_A_strategy)
@settings(max_examples=50)
def test_abc_a_instantiation(instance):
    assert isinstance(instance, abc_A)



@given(instance=abc_A_strategy)
def test_abc_a_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=abc_B_strategy)
@settings(max_examples=50)
def test_abc_b_instantiation(instance):
    assert isinstance(instance, abc_B)



@given(instance=abc_B_strategy)
def test_abc_b_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=abc_C_strategy)
@settings(max_examples=50)
def test_abc_c_instantiation(instance):
    assert isinstance(instance, abc_C)



@given(instance=abc_C_strategy)
def test_abc_c_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original
