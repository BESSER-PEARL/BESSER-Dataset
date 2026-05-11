import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FaultyRelations::A,
    FaultyRelations::C,
    FaultyRelations::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_faultyrelations::a_is_not_abstract():
    assert not inspect.isabstract(FaultyRelations::A)


def test_faultyrelations::a_constructor_exists():
    assert callable(FaultyRelations::A.__init__)


def test_faultyrelations::a_constructor_args():
    sig = inspect.signature(FaultyRelations::A.__init__)
    params = list(sig.parameters.keys())
    assert "w" in params, "Missing parameter 'w'"
    assert "v" in params, "Missing parameter 'v'"

def test_faultyrelations::a_has_w():
    assert hasattr(FaultyRelations::A, "w")
    descriptor = None
    for klass in FaultyRelations::A.__mro__:
        if "w" in klass.__dict__:
            descriptor = klass.__dict__["w"]
            break
    assert isinstance(descriptor, property)

def test_faultyrelations::a_has_v():
    assert hasattr(FaultyRelations::A, "v")
    descriptor = None
    for klass in FaultyRelations::A.__mro__:
        if "v" in klass.__dict__:
            descriptor = klass.__dict__["v"]
            break
    assert isinstance(descriptor, property)



def test_faultyrelations::c_is_not_abstract():
    assert not inspect.isabstract(FaultyRelations::C)


def test_faultyrelations::c_constructor_exists():
    assert callable(FaultyRelations::C.__init__)


def test_faultyrelations::c_constructor_args():
    sig = inspect.signature(FaultyRelations::C.__init__)
    params = list(sig.parameters.keys())
    assert "u" in params, "Missing parameter 'u'"

def test_faultyrelations::c_has_u():
    assert hasattr(FaultyRelations::C, "u")
    descriptor = None
    for klass in FaultyRelations::C.__mro__:
        if "u" in klass.__dict__:
            descriptor = klass.__dict__["u"]
            break
    assert isinstance(descriptor, property)



def test_faultyrelations::b_is_not_abstract():
    assert not inspect.isabstract(FaultyRelations::B)


def test_faultyrelations::b_constructor_exists():
    assert callable(FaultyRelations::B.__init__)


def test_faultyrelations::b_constructor_args():
    sig = inspect.signature(FaultyRelations::B.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_faultyrelations::b_has_x():
    assert hasattr(FaultyRelations::B, "x")
    descriptor = None
    for klass in FaultyRelations::B.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_faultyrelations::b_has_y():
    assert hasattr(FaultyRelations::B, "y")
    descriptor = None
    for klass in FaultyRelations::B.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
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
FaultyRelations::A_strategy = st.builds(
    FaultyRelations::A,
    w=
        st.booleans(),
    v=
        st.integers()
)
FaultyRelations::C_strategy = st.builds(
    FaultyRelations::C,
    u=
        st.integers()
)
FaultyRelations::B_strategy = st.builds(
    FaultyRelations::B,
    x=
        st.integers(),
    y=
        st.integers()
)

@given(instance=FaultyRelations::A_strategy)
@settings(max_examples=50)
def test_faultyrelations::a_instantiation(instance):
    assert isinstance(instance, FaultyRelations::A)

@given(instance=FaultyRelations::A_strategy)
def test_faultyrelations::a_w_type(instance):
    assert isinstance(instance.w, bool)


@given(instance=FaultyRelations::A_strategy)
def test_faultyrelations::a_w_setter(instance):
    original = instance.w
    instance.w = original
    assert instance.w == original

@given(instance=FaultyRelations::A_strategy)
def test_faultyrelations::a_v_type(instance):
    assert isinstance(instance.v, int)


@given(instance=FaultyRelations::A_strategy)
def test_faultyrelations::a_v_setter(instance):
    original = instance.v
    instance.v = original
    assert instance.v == original

@given(instance=FaultyRelations::C_strategy)
@settings(max_examples=50)
def test_faultyrelations::c_instantiation(instance):
    assert isinstance(instance, FaultyRelations::C)

@given(instance=FaultyRelations::C_strategy)
def test_faultyrelations::c_u_type(instance):
    assert isinstance(instance.u, int)


@given(instance=FaultyRelations::C_strategy)
def test_faultyrelations::c_u_setter(instance):
    original = instance.u
    instance.u = original
    assert instance.u == original

@given(instance=FaultyRelations::B_strategy)
@settings(max_examples=50)
def test_faultyrelations::b_instantiation(instance):
    assert isinstance(instance, FaultyRelations::B)

@given(instance=FaultyRelations::B_strategy)
def test_faultyrelations::b_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=FaultyRelations::B_strategy)
def test_faultyrelations::b_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=FaultyRelations::B_strategy)
def test_faultyrelations::b_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=FaultyRelations::B_strategy)
def test_faultyrelations::b_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original
