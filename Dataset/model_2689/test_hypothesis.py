import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    cycle::A,
    cycle::C,
    cycle::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cycle::a_is_not_abstract():
    assert not inspect.isabstract(cycle::A)


def test_cycle::a_constructor_exists():
    assert callable(cycle::A.__init__)


def test_cycle::a_constructor_args():
    sig = inspect.signature(cycle::A.__init__)
    params = list(sig.parameters.keys())
    assert "i" in params, "Missing parameter 'i'"

def test_cycle::a_has_i():
    assert hasattr(cycle::A, "i")
    descriptor = None
    for klass in cycle::A.__mro__:
        if "i" in klass.__dict__:
            descriptor = klass.__dict__["i"]
            break
    assert isinstance(descriptor, property)



def test_cycle::c_is_not_abstract():
    assert not inspect.isabstract(cycle::C)


def test_cycle::c_constructor_exists():
    assert callable(cycle::C.__init__)


def test_cycle::c_constructor_args():
    sig = inspect.signature(cycle::C.__init__)
    params = list(sig.parameters.keys())



def test_cycle::b_is_not_abstract():
    assert not inspect.isabstract(cycle::B)


def test_cycle::b_constructor_exists():
    assert callable(cycle::B.__init__)


def test_cycle::b_constructor_args():
    sig = inspect.signature(cycle::B.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_cycle::b_has_x():
    assert hasattr(cycle::B, "x")
    descriptor = None
    for klass in cycle::B.__mro__:
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
cycle::A_strategy = st.builds(
    cycle::A,
    i=
        st.integers()
)
cycle::C_strategy = st.builds(
    cycle::C,
)
cycle::B_strategy = st.builds(
    cycle::B,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=cycle::A_strategy)
@settings(max_examples=50)
def test_cycle::a_instantiation(instance):
    assert isinstance(instance, cycle::A)

@given(instance=cycle::A_strategy)
def test_cycle::a_i_type(instance):
    assert isinstance(instance.i, int)


@given(instance=cycle::A_strategy)
def test_cycle::a_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original

@given(instance=cycle::C_strategy)
@settings(max_examples=50)
def test_cycle::c_instantiation(instance):
    assert isinstance(instance, cycle::C)

@given(instance=cycle::B_strategy)
@settings(max_examples=50)
def test_cycle::b_instantiation(instance):
    assert isinstance(instance, cycle::B)

@given(instance=cycle::B_strategy)
def test_cycle::b_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=cycle::B_strategy)
def test_cycle::b_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original
