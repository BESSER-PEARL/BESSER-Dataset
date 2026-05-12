import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FaultyUMLmodel_D,
    FaultyUMLmodel_C,
    FaultyUMLmodel_B,
    FaultyUMLmodel_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_faultyumlmodel_d_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel_D)


def test_faultyumlmodel_d_constructor_exists():
    assert callable(FaultyUMLmodel_D.__init__)


def test_faultyumlmodel_d_constructor_args():
    sig = inspect.signature(FaultyUMLmodel_D.__init__)
    params = list(sig.parameters.keys())
    assert "z" in params, "Missing parameter 'z'"

def test_faultyumlmodel_d_has_z():
    assert hasattr(FaultyUMLmodel_D, "z")
    descriptor = None
    for klass in FaultyUMLmodel_D.__mro__:
        if "z" in klass.__dict__:
            descriptor = klass.__dict__["z"]
            break
    assert isinstance(descriptor, property)



def test_faultyumlmodel_c_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel_C)


def test_faultyumlmodel_c_constructor_exists():
    assert callable(FaultyUMLmodel_C.__init__)


def test_faultyumlmodel_c_constructor_args():
    sig = inspect.signature(FaultyUMLmodel_C.__init__)
    params = list(sig.parameters.keys())
    assert "u" in params, "Missing parameter 'u'"

def test_faultyumlmodel_c_has_u():
    assert hasattr(FaultyUMLmodel_C, "u")
    descriptor = None
    for klass in FaultyUMLmodel_C.__mro__:
        if "u" in klass.__dict__:
            descriptor = klass.__dict__["u"]
            break
    assert isinstance(descriptor, property)



def test_faultyumlmodel_b_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel_B)


def test_faultyumlmodel_b_constructor_exists():
    assert callable(FaultyUMLmodel_B.__init__)


def test_faultyumlmodel_b_constructor_args():
    sig = inspect.signature(FaultyUMLmodel_B.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_faultyumlmodel_b_has_y():
    assert hasattr(FaultyUMLmodel_B, "y")
    descriptor = None
    for klass in FaultyUMLmodel_B.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_faultyumlmodel_b_has_x():
    assert hasattr(FaultyUMLmodel_B, "x")
    descriptor = None
    for klass in FaultyUMLmodel_B.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_faultyumlmodel_a_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel_A)


def test_faultyumlmodel_a_constructor_exists():
    assert callable(FaultyUMLmodel_A.__init__)


def test_faultyumlmodel_a_constructor_args():
    sig = inspect.signature(FaultyUMLmodel_A.__init__)
    params = list(sig.parameters.keys())
    assert "v" in params, "Missing parameter 'v'"
    assert "w" in params, "Missing parameter 'w'"

def test_faultyumlmodel_a_has_v():
    assert hasattr(FaultyUMLmodel_A, "v")
    descriptor = None
    for klass in FaultyUMLmodel_A.__mro__:
        if "v" in klass.__dict__:
            descriptor = klass.__dict__["v"]
            break
    assert isinstance(descriptor, property)

def test_faultyumlmodel_a_has_w():
    assert hasattr(FaultyUMLmodel_A, "w")
    descriptor = None
    for klass in FaultyUMLmodel_A.__mro__:
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
FaultyUMLmodel_D_strategy = st.builds(
    FaultyUMLmodel_D,
    z=
        st.booleans()
)
FaultyUMLmodel_C_strategy = st.builds(
    FaultyUMLmodel_C,
    u=
        st.integers()
)
FaultyUMLmodel_B_strategy = st.builds(
    FaultyUMLmodel_B,
    y=
        st.integers(),
    x=
        st.integers()
)
FaultyUMLmodel_A_strategy = st.builds(
    FaultyUMLmodel_A,
    v=
        st.integers(),
    w=
        st.booleans()
)

@given(instance=FaultyUMLmodel_D_strategy)
@settings(max_examples=50)
def test_faultyumlmodel_d_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel_D)



@given(instance=FaultyUMLmodel_D_strategy)
def test_faultyumlmodel_d_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original

@given(instance=FaultyUMLmodel_C_strategy)
@settings(max_examples=50)
def test_faultyumlmodel_c_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel_C)



@given(instance=FaultyUMLmodel_C_strategy)
def test_faultyumlmodel_c_u_setter(instance):
    original = instance.u
    instance.u = original
    assert instance.u == original

@given(instance=FaultyUMLmodel_B_strategy)
@settings(max_examples=50)
def test_faultyumlmodel_b_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel_B)



@given(instance=FaultyUMLmodel_B_strategy)
def test_faultyumlmodel_b_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=FaultyUMLmodel_B_strategy)
def test_faultyumlmodel_b_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=FaultyUMLmodel_A_strategy)
@settings(max_examples=50)
def test_faultyumlmodel_a_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel_A)



@given(instance=FaultyUMLmodel_A_strategy)
def test_faultyumlmodel_a_v_setter(instance):
    original = instance.v
    instance.v = original
    assert instance.v == original



@given(instance=FaultyUMLmodel_A_strategy)
def test_faultyumlmodel_a_w_setter(instance):
    original = instance.w
    instance.w = original
    assert instance.w == original
