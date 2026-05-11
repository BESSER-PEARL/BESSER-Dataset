import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FaultyUMLmodel::D,
    FaultyUMLmodel::C,
    FaultyUMLmodel::B,
    FaultyUMLmodel::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_faultyumlmodel::d_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel::D)


def test_faultyumlmodel::d_constructor_exists():
    assert callable(FaultyUMLmodel::D.__init__)


def test_faultyumlmodel::d_constructor_args():
    sig = inspect.signature(FaultyUMLmodel::D.__init__)
    params = list(sig.parameters.keys())
    assert "z" in params, "Missing parameter 'z'"

def test_faultyumlmodel::d_has_z():
    assert hasattr(FaultyUMLmodel::D, "z")
    descriptor = None
    for klass in FaultyUMLmodel::D.__mro__:
        if "z" in klass.__dict__:
            descriptor = klass.__dict__["z"]
            break
    assert isinstance(descriptor, property)



def test_faultyumlmodel::c_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel::C)


def test_faultyumlmodel::c_constructor_exists():
    assert callable(FaultyUMLmodel::C.__init__)


def test_faultyumlmodel::c_constructor_args():
    sig = inspect.signature(FaultyUMLmodel::C.__init__)
    params = list(sig.parameters.keys())
    assert "u" in params, "Missing parameter 'u'"

def test_faultyumlmodel::c_has_u():
    assert hasattr(FaultyUMLmodel::C, "u")
    descriptor = None
    for klass in FaultyUMLmodel::C.__mro__:
        if "u" in klass.__dict__:
            descriptor = klass.__dict__["u"]
            break
    assert isinstance(descriptor, property)



def test_faultyumlmodel::b_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel::B)


def test_faultyumlmodel::b_constructor_exists():
    assert callable(FaultyUMLmodel::B.__init__)


def test_faultyumlmodel::b_constructor_args():
    sig = inspect.signature(FaultyUMLmodel::B.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_faultyumlmodel::b_has_x():
    assert hasattr(FaultyUMLmodel::B, "x")
    descriptor = None
    for klass in FaultyUMLmodel::B.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_faultyumlmodel::b_has_y():
    assert hasattr(FaultyUMLmodel::B, "y")
    descriptor = None
    for klass in FaultyUMLmodel::B.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_faultyumlmodel::a_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel::A)


def test_faultyumlmodel::a_constructor_exists():
    assert callable(FaultyUMLmodel::A.__init__)


def test_faultyumlmodel::a_constructor_args():
    sig = inspect.signature(FaultyUMLmodel::A.__init__)
    params = list(sig.parameters.keys())
    assert "v" in params, "Missing parameter 'v'"
    assert "w" in params, "Missing parameter 'w'"

def test_faultyumlmodel::a_has_v():
    assert hasattr(FaultyUMLmodel::A, "v")
    descriptor = None
    for klass in FaultyUMLmodel::A.__mro__:
        if "v" in klass.__dict__:
            descriptor = klass.__dict__["v"]
            break
    assert isinstance(descriptor, property)

def test_faultyumlmodel::a_has_w():
    assert hasattr(FaultyUMLmodel::A, "w")
    descriptor = None
    for klass in FaultyUMLmodel::A.__mro__:
        if "w" in klass.__dict__:
            descriptor = klass.__dict__["w"]
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
FaultyUMLmodel::D_strategy = st.builds(
    FaultyUMLmodel::D,
    z=
        st.booleans()
)
FaultyUMLmodel::C_strategy = st.builds(
    FaultyUMLmodel::C,
    u=
        st.integers()
)
FaultyUMLmodel::B_strategy = st.builds(
    FaultyUMLmodel::B,
    x=
        st.integers(),
    y=
        st.integers()
)
FaultyUMLmodel::A_strategy = st.builds(
    FaultyUMLmodel::A,
    v=
        st.integers(),
    w=
        st.booleans()
)

@given(instance=FaultyUMLmodel::D_strategy)
@settings(max_examples=50)
def test_faultyumlmodel::d_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel::D)

@given(instance=FaultyUMLmodel::D_strategy)
def test_faultyumlmodel::d_z_type(instance):
    assert isinstance(instance.z, bool)


@given(instance=FaultyUMLmodel::D_strategy)
def test_faultyumlmodel::d_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original

@given(instance=FaultyUMLmodel::C_strategy)
@settings(max_examples=50)
def test_faultyumlmodel::c_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel::C)

@given(instance=FaultyUMLmodel::C_strategy)
def test_faultyumlmodel::c_u_type(instance):
    assert isinstance(instance.u, int)


@given(instance=FaultyUMLmodel::C_strategy)
def test_faultyumlmodel::c_u_setter(instance):
    original = instance.u
    instance.u = original
    assert instance.u == original

@given(instance=FaultyUMLmodel::B_strategy)
@settings(max_examples=50)
def test_faultyumlmodel::b_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel::B)

@given(instance=FaultyUMLmodel::B_strategy)
def test_faultyumlmodel::b_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=FaultyUMLmodel::B_strategy)
def test_faultyumlmodel::b_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=FaultyUMLmodel::B_strategy)
def test_faultyumlmodel::b_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=FaultyUMLmodel::B_strategy)
def test_faultyumlmodel::b_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=FaultyUMLmodel::A_strategy)
@settings(max_examples=50)
def test_faultyumlmodel::a_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel::A)

@given(instance=FaultyUMLmodel::A_strategy)
def test_faultyumlmodel::a_v_type(instance):
    assert isinstance(instance.v, int)


@given(instance=FaultyUMLmodel::A_strategy)
def test_faultyumlmodel::a_v_setter(instance):
    original = instance.v
    instance.v = original
    assert instance.v == original

@given(instance=FaultyUMLmodel::A_strategy)
def test_faultyumlmodel::a_w_type(instance):
    assert isinstance(instance.w, bool)


@given(instance=FaultyUMLmodel::A_strategy)
def test_faultyumlmodel::a_w_setter(instance):
    original = instance.w
    instance.w = original
    assert instance.w == original
