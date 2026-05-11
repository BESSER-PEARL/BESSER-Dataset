import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FaultyUMLmodel4::D,
    FaultyUMLmodel4::A,
    FaultyUMLmodel4::C,
    FaultyUMLmodel4::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_faultyumlmodel4::d_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel4::D)


def test_faultyumlmodel4::d_constructor_exists():
    assert callable(FaultyUMLmodel4::D.__init__)


def test_faultyumlmodel4::d_constructor_args():
    sig = inspect.signature(FaultyUMLmodel4::D.__init__)
    params = list(sig.parameters.keys())
    assert "z" in params, "Missing parameter 'z'"

def test_faultyumlmodel4::d_has_z():
    assert hasattr(FaultyUMLmodel4::D, "z")
    descriptor = None
    for klass in FaultyUMLmodel4::D.__mro__:
        if "z" in klass.__dict__:
            descriptor = klass.__dict__["z"]
            break
    assert isinstance(descriptor, property)



def test_faultyumlmodel4::a_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel4::A)


def test_faultyumlmodel4::a_constructor_exists():
    assert callable(FaultyUMLmodel4::A.__init__)


def test_faultyumlmodel4::a_constructor_args():
    sig = inspect.signature(FaultyUMLmodel4::A.__init__)
    params = list(sig.parameters.keys())
    assert "w" in params, "Missing parameter 'w'"
    assert "v" in params, "Missing parameter 'v'"

def test_faultyumlmodel4::a_has_w():
    assert hasattr(FaultyUMLmodel4::A, "w")
    descriptor = None
    for klass in FaultyUMLmodel4::A.__mro__:
        if "w" in klass.__dict__:
            descriptor = klass.__dict__["w"]
            break
    assert isinstance(descriptor, property)

def test_faultyumlmodel4::a_has_v():
    assert hasattr(FaultyUMLmodel4::A, "v")
    descriptor = None
    for klass in FaultyUMLmodel4::A.__mro__:
        if "v" in klass.__dict__:
            descriptor = klass.__dict__["v"]
            break
    assert isinstance(descriptor, property)



def test_faultyumlmodel4::c_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel4::C)


def test_faultyumlmodel4::c_constructor_exists():
    assert callable(FaultyUMLmodel4::C.__init__)


def test_faultyumlmodel4::c_constructor_args():
    sig = inspect.signature(FaultyUMLmodel4::C.__init__)
    params = list(sig.parameters.keys())
    assert "u" in params, "Missing parameter 'u'"

def test_faultyumlmodel4::c_has_u():
    assert hasattr(FaultyUMLmodel4::C, "u")
    descriptor = None
    for klass in FaultyUMLmodel4::C.__mro__:
        if "u" in klass.__dict__:
            descriptor = klass.__dict__["u"]
            break
    assert isinstance(descriptor, property)



def test_faultyumlmodel4::b_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel4::B)


def test_faultyumlmodel4::b_constructor_exists():
    assert callable(FaultyUMLmodel4::B.__init__)


def test_faultyumlmodel4::b_constructor_args():
    sig = inspect.signature(FaultyUMLmodel4::B.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_faultyumlmodel4::b_has_y():
    assert hasattr(FaultyUMLmodel4::B, "y")
    descriptor = None
    for klass in FaultyUMLmodel4::B.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_faultyumlmodel4::b_has_x():
    assert hasattr(FaultyUMLmodel4::B, "x")
    descriptor = None
    for klass in FaultyUMLmodel4::B.__mro__:
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
FaultyUMLmodel4::D_strategy = st.builds(
    FaultyUMLmodel4::D,
    z=
        st.booleans()
)
FaultyUMLmodel4::A_strategy = st.builds(
    FaultyUMLmodel4::A,
    w=
        st.booleans(),
    v=
        st.integers()
)
FaultyUMLmodel4::C_strategy = st.builds(
    FaultyUMLmodel4::C,
    u=
        st.integers()
)
FaultyUMLmodel4::B_strategy = st.builds(
    FaultyUMLmodel4::B,
    y=
        st.integers(),
    x=
        st.integers()
)

@given(instance=FaultyUMLmodel4::D_strategy)
@settings(max_examples=50)
def test_faultyumlmodel4::d_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel4::D)

@given(instance=FaultyUMLmodel4::D_strategy)
def test_faultyumlmodel4::d_z_type(instance):
    assert isinstance(instance.z, bool)


@given(instance=FaultyUMLmodel4::D_strategy)
def test_faultyumlmodel4::d_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original

@given(instance=FaultyUMLmodel4::A_strategy)
@settings(max_examples=50)
def test_faultyumlmodel4::a_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel4::A)

@given(instance=FaultyUMLmodel4::A_strategy)
def test_faultyumlmodel4::a_w_type(instance):
    assert isinstance(instance.w, bool)


@given(instance=FaultyUMLmodel4::A_strategy)
def test_faultyumlmodel4::a_w_setter(instance):
    original = instance.w
    instance.w = original
    assert instance.w == original

@given(instance=FaultyUMLmodel4::A_strategy)
def test_faultyumlmodel4::a_v_type(instance):
    assert isinstance(instance.v, int)


@given(instance=FaultyUMLmodel4::A_strategy)
def test_faultyumlmodel4::a_v_setter(instance):
    original = instance.v
    instance.v = original
    assert instance.v == original

@given(instance=FaultyUMLmodel4::C_strategy)
@settings(max_examples=50)
def test_faultyumlmodel4::c_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel4::C)

@given(instance=FaultyUMLmodel4::C_strategy)
def test_faultyumlmodel4::c_u_type(instance):
    assert isinstance(instance.u, int)


@given(instance=FaultyUMLmodel4::C_strategy)
def test_faultyumlmodel4::c_u_setter(instance):
    original = instance.u
    instance.u = original
    assert instance.u == original

@given(instance=FaultyUMLmodel4::B_strategy)
@settings(max_examples=50)
def test_faultyumlmodel4::b_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel4::B)

@given(instance=FaultyUMLmodel4::B_strategy)
def test_faultyumlmodel4::b_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=FaultyUMLmodel4::B_strategy)
def test_faultyumlmodel4::b_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=FaultyUMLmodel4::B_strategy)
def test_faultyumlmodel4::b_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=FaultyUMLmodel4::B_strategy)
def test_faultyumlmodel4::b_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original
