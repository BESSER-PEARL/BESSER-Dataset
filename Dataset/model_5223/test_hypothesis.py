import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FaultyRelations_A,
    FaultyRelations_C,
    FaultyRelations_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_faultyrelations_a_is_not_abstract():
    assert not inspect.isabstract(FaultyRelations_A)


def test_faultyrelations_a_constructor_exists():
    assert callable(FaultyRelations_A.__init__)


def test_faultyrelations_a_constructor_args():
    sig = inspect.signature(FaultyRelations_A.__init__)
    params = list(sig.parameters.keys())
    assert "v" in params, "Missing parameter 'v'"
    assert "w" in params, "Missing parameter 'w'"

def test_faultyrelations_a_has_v():
    assert hasattr(FaultyRelations_A, "v")
    descriptor = None
    for klass in FaultyRelations_A.__mro__:
        if "v" in klass.__dict__:
            descriptor = klass.__dict__["v"]
            break
    assert isinstance(descriptor, property)

def test_faultyrelations_a_has_w():
    assert hasattr(FaultyRelations_A, "w")
    descriptor = None
    for klass in FaultyRelations_A.__mro__:
        if "w" in klass.__dict__:
            descriptor = klass.__dict__["w"]
            break
    assert isinstance(descriptor, property)



def test_faultyrelations_c_is_not_abstract():
    assert not inspect.isabstract(FaultyRelations_C)


def test_faultyrelations_c_constructor_exists():
    assert callable(FaultyRelations_C.__init__)


def test_faultyrelations_c_constructor_args():
    sig = inspect.signature(FaultyRelations_C.__init__)
    params = list(sig.parameters.keys())
    assert "u" in params, "Missing parameter 'u'"

def test_faultyrelations_c_has_u():
    assert hasattr(FaultyRelations_C, "u")
    descriptor = None
    for klass in FaultyRelations_C.__mro__:
        if "u" in klass.__dict__:
            descriptor = klass.__dict__["u"]
            break
    assert isinstance(descriptor, property)



def test_faultyrelations_b_is_not_abstract():
    assert not inspect.isabstract(FaultyRelations_B)


def test_faultyrelations_b_constructor_exists():
    assert callable(FaultyRelations_B.__init__)


def test_faultyrelations_b_constructor_args():
    sig = inspect.signature(FaultyRelations_B.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_faultyrelations_b_has_y():
    assert hasattr(FaultyRelations_B, "y")
    descriptor = None
    for klass in FaultyRelations_B.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_faultyrelations_b_has_x():
    assert hasattr(FaultyRelations_B, "x")
    descriptor = None
    for klass in FaultyRelations_B.__mro__:
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
FaultyRelations_A_strategy = st.builds(
    FaultyRelations_A,
    v=
        st.integers(),
    w=
        st.booleans()
)
FaultyRelations_C_strategy = st.builds(
    FaultyRelations_C,
    u=
        st.integers()
)
FaultyRelations_B_strategy = st.builds(
    FaultyRelations_B,
    y=
        st.integers(),
    x=
        st.integers()
)

@given(instance=FaultyRelations_A_strategy)
@settings(max_examples=50)
def test_faultyrelations_a_instantiation(instance):
    assert isinstance(instance, FaultyRelations_A)



@given(instance=FaultyRelations_A_strategy)
def test_faultyrelations_a_v_setter(instance):
    original = instance.v
    instance.v = original
    assert instance.v == original



@given(instance=FaultyRelations_A_strategy)
def test_faultyrelations_a_w_setter(instance):
    original = instance.w
    instance.w = original
    assert instance.w == original

@given(instance=FaultyRelations_C_strategy)
@settings(max_examples=50)
def test_faultyrelations_c_instantiation(instance):
    assert isinstance(instance, FaultyRelations_C)



@given(instance=FaultyRelations_C_strategy)
def test_faultyrelations_c_u_setter(instance):
    original = instance.u
    instance.u = original
    assert instance.u == original

@given(instance=FaultyRelations_B_strategy)
@settings(max_examples=50)
def test_faultyrelations_b_instantiation(instance):
    assert isinstance(instance, FaultyRelations_B)



@given(instance=FaultyRelations_B_strategy)
def test_faultyrelations_b_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=FaultyRelations_B_strategy)
def test_faultyrelations_b_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original
