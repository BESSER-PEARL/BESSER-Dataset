import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    cycle_C,
    cycle_B,
    cycle_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cycle_c_is_not_abstract():
    assert not inspect.isabstract(cycle_C)


def test_cycle_c_constructor_exists():
    assert callable(cycle_C.__init__)


def test_cycle_c_constructor_args():
    sig = inspect.signature(cycle_C.__init__)
    params = list(sig.parameters.keys())



def test_cycle_b_is_not_abstract():
    assert not inspect.isabstract(cycle_B)


def test_cycle_b_constructor_exists():
    assert callable(cycle_B.__init__)


def test_cycle_b_constructor_args():
    sig = inspect.signature(cycle_B.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_cycle_b_has_x():
    assert hasattr(cycle_B, "x")
    descriptor = None
    for klass in cycle_B.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_cycle_b_has_y():
    assert hasattr(cycle_B, "y")
    descriptor = None
    for klass in cycle_B.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_cycle_a_is_not_abstract():
    assert not inspect.isabstract(cycle_A)


def test_cycle_a_constructor_exists():
    assert callable(cycle_A.__init__)


def test_cycle_a_constructor_args():
    sig = inspect.signature(cycle_A.__init__)
    params = list(sig.parameters.keys())
    assert "j" in params, "Missing parameter 'j'"
    assert "i" in params, "Missing parameter 'i'"

def test_cycle_a_has_j():
    assert hasattr(cycle_A, "j")
    descriptor = None
    for klass in cycle_A.__mro__:
        if "j" in klass.__dict__:
            descriptor = klass.__dict__["j"]
            break
    assert isinstance(descriptor, property)

def test_cycle_a_has_i():
    assert hasattr(cycle_A, "i")
    descriptor = None
    for klass in cycle_A.__mro__:
        if "i" in klass.__dict__:
            descriptor = klass.__dict__["i"]
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
cycle_C_strategy = st.builds(
    cycle_C,
)
cycle_B_strategy = st.builds(
    cycle_B,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cycle_A_strategy = st.builds(
    cycle_A,
    j=
        st.integers(),
    i=
        st.integers()
)

@given(instance=cycle_C_strategy)
@settings(max_examples=50)
def test_cycle_c_instantiation(instance):
    assert isinstance(instance, cycle_C)

@given(instance=cycle_B_strategy)
@settings(max_examples=50)
def test_cycle_b_instantiation(instance):
    assert isinstance(instance, cycle_B)



@given(instance=cycle_B_strategy)
def test_cycle_b_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=cycle_B_strategy)
def test_cycle_b_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=cycle_A_strategy)
@settings(max_examples=50)
def test_cycle_a_instantiation(instance):
    assert isinstance(instance, cycle_A)



@given(instance=cycle_A_strategy)
def test_cycle_a_j_setter(instance):
    original = instance.j
    instance.j = original
    assert instance.j == original



@given(instance=cycle_A_strategy)
def test_cycle_a_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original
