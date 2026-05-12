import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FaultyUMLmodel4_D,
    FaultyUMLmodel4_A,
    FaultyUMLmodel4_C,
    FaultyUMLmodel4_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_faultyumlmodel4_d_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel4_D)


def test_faultyumlmodel4_d_constructor_exists():
    assert callable(FaultyUMLmodel4_D.__init__)


def test_faultyumlmodel4_d_constructor_args():
    sig = inspect.signature(FaultyUMLmodel4_D.__init__)
    params = list(sig.parameters.keys())
    assert "z" in params, "Missing parameter 'z'"

def test_faultyumlmodel4_d_has_z():
    assert hasattr(FaultyUMLmodel4_D, "z")
    descriptor = None
    for klass in FaultyUMLmodel4_D.__mro__:
        if "z" in klass.__dict__:
            descriptor = klass.__dict__["z"]
            break
    assert isinstance(descriptor, property)



def test_faultyumlmodel4_a_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel4_A)


def test_faultyumlmodel4_a_constructor_exists():
    assert callable(FaultyUMLmodel4_A.__init__)


def test_faultyumlmodel4_a_constructor_args():
    sig = inspect.signature(FaultyUMLmodel4_A.__init__)
    params = list(sig.parameters.keys())
    assert "v" in params, "Missing parameter 'v'"
    assert "w" in params, "Missing parameter 'w'"

def test_faultyumlmodel4_a_has_v():
    assert hasattr(FaultyUMLmodel4_A, "v")
    descriptor = None
    for klass in FaultyUMLmodel4_A.__mro__:
        if "v" in klass.__dict__:
            descriptor = klass.__dict__["v"]
            break
    assert isinstance(descriptor, property)

def test_faultyumlmodel4_a_has_w():
    assert hasattr(FaultyUMLmodel4_A, "w")
    descriptor = None
    for klass in FaultyUMLmodel4_A.__mro__:
        if "w" in klass.__dict__:
            descriptor = klass.__dict__["w"]
            break
    assert isinstance(descriptor, property)



def test_faultyumlmodel4_c_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel4_C)


def test_faultyumlmodel4_c_constructor_exists():
    assert callable(FaultyUMLmodel4_C.__init__)


def test_faultyumlmodel4_c_constructor_args():
    sig = inspect.signature(FaultyUMLmodel4_C.__init__)
    params = list(sig.parameters.keys())
    assert "u" in params, "Missing parameter 'u'"

def test_faultyumlmodel4_c_has_u():
    assert hasattr(FaultyUMLmodel4_C, "u")
    descriptor = None
    for klass in FaultyUMLmodel4_C.__mro__:
        if "u" in klass.__dict__:
            descriptor = klass.__dict__["u"]
            break
    assert isinstance(descriptor, property)



def test_faultyumlmodel4_b_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel4_B)


def test_faultyumlmodel4_b_constructor_exists():
    assert callable(FaultyUMLmodel4_B.__init__)


def test_faultyumlmodel4_b_constructor_args():
    sig = inspect.signature(FaultyUMLmodel4_B.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_faultyumlmodel4_b_has_y():
    assert hasattr(FaultyUMLmodel4_B, "y")
    descriptor = None
    for klass in FaultyUMLmodel4_B.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_faultyumlmodel4_b_has_x():
    assert hasattr(FaultyUMLmodel4_B, "x")
    descriptor = None
    for klass in FaultyUMLmodel4_B.__mro__:
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
FaultyUMLmodel4_D_strategy = st.builds(
    FaultyUMLmodel4_D,
    z=
        st.booleans()
)
FaultyUMLmodel4_A_strategy = st.builds(
    FaultyUMLmodel4_A,
    v=
        st.integers(),
    w=
        st.booleans()
)
FaultyUMLmodel4_C_strategy = st.builds(
    FaultyUMLmodel4_C,
    u=
        st.integers()
)
FaultyUMLmodel4_B_strategy = st.builds(
    FaultyUMLmodel4_B,
    y=
        st.integers(),
    x=
        st.integers()
)

@given(instance=FaultyUMLmodel4_D_strategy)
@settings(max_examples=50)
def test_faultyumlmodel4_d_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel4_D)



@given(instance=FaultyUMLmodel4_D_strategy)
def test_faultyumlmodel4_d_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original

@given(instance=FaultyUMLmodel4_A_strategy)
@settings(max_examples=50)
def test_faultyumlmodel4_a_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel4_A)



@given(instance=FaultyUMLmodel4_A_strategy)
def test_faultyumlmodel4_a_v_setter(instance):
    original = instance.v
    instance.v = original
    assert instance.v == original



@given(instance=FaultyUMLmodel4_A_strategy)
def test_faultyumlmodel4_a_w_setter(instance):
    original = instance.w
    instance.w = original
    assert instance.w == original

@given(instance=FaultyUMLmodel4_C_strategy)
@settings(max_examples=50)
def test_faultyumlmodel4_c_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel4_C)



@given(instance=FaultyUMLmodel4_C_strategy)
def test_faultyumlmodel4_c_u_setter(instance):
    original = instance.u
    instance.u = original
    assert instance.u == original

@given(instance=FaultyUMLmodel4_B_strategy)
@settings(max_examples=50)
def test_faultyumlmodel4_b_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel4_B)



@given(instance=FaultyUMLmodel4_B_strategy)
def test_faultyumlmodel4_b_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=FaultyUMLmodel4_B_strategy)
def test_faultyumlmodel4_b_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original
