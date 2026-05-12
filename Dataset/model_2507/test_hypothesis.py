import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dummy_E,
    dummy_D,
    dummy_B,
    dummy_A,
    E,
    dummy_G,
    dummy_F,
    dummy_C,
    EnumExample,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dummy_e_is_not_abstract():
    assert not inspect.isabstract(dummy_E)


def test_dummy_e_constructor_exists():
    assert callable(dummy_E.__init__)


def test_dummy_e_constructor_args():
    sig = inspect.signature(dummy_E.__init__)
    params = list(sig.parameters.keys())
    assert "eName" in params, "Missing parameter 'eName'"

def test_dummy_e_has_eName():
    assert hasattr(dummy_E, "eName")
    descriptor = None
    for klass in dummy_E.__mro__:
        if "eName" in klass.__dict__:
            descriptor = klass.__dict__["eName"]
            break
    assert isinstance(descriptor, property)



def test_dummy_d_is_not_abstract():
    assert not inspect.isabstract(dummy_D)


def test_dummy_d_constructor_exists():
    assert callable(dummy_D.__init__)


def test_dummy_d_constructor_args():
    sig = inspect.signature(dummy_D.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "m" in params, "Missing parameter 'm'"
    assert "l" in params, "Missing parameter 'l'"

def test_dummy_d_has_name():
    assert hasattr(dummy_D, "name")
    descriptor = None
    for klass in dummy_D.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dummy_d_has_m():
    assert hasattr(dummy_D, "m")
    descriptor = None
    for klass in dummy_D.__mro__:
        if "m" in klass.__dict__:
            descriptor = klass.__dict__["m"]
            break
    assert isinstance(descriptor, property)

def test_dummy_d_has_l():
    assert hasattr(dummy_D, "l")
    descriptor = None
    for klass in dummy_D.__mro__:
        if "l" in klass.__dict__:
            descriptor = klass.__dict__["l"]
            break
    assert isinstance(descriptor, property)



def test_dummy_b_is_not_abstract():
    assert not inspect.isabstract(dummy_B)


def test_dummy_b_constructor_exists():
    assert callable(dummy_B.__init__)


def test_dummy_b_constructor_args():
    sig = inspect.signature(dummy_B.__init__)
    params = list(sig.parameters.keys())
    assert "z" in params, "Missing parameter 'z'"
    assert "y" in params, "Missing parameter 'y'"

def test_dummy_b_has_z():
    assert hasattr(dummy_B, "z")
    descriptor = None
    for klass in dummy_B.__mro__:
        if "z" in klass.__dict__:
            descriptor = klass.__dict__["z"]
            break
    assert isinstance(descriptor, property)

def test_dummy_b_has_y():
    assert hasattr(dummy_B, "y")
    descriptor = None
    for klass in dummy_B.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_dummy_a_is_not_abstract():
    assert not inspect.isabstract(dummy_A)


def test_dummy_a_constructor_exists():
    assert callable(dummy_A.__init__)


def test_dummy_a_constructor_args():
    sig = inspect.signature(dummy_A.__init__)
    params = list(sig.parameters.keys())
    assert "en" in params, "Missing parameter 'en'"
    assert "x" in params, "Missing parameter 'x'"

def test_dummy_a_has_en():
    assert hasattr(dummy_A, "en")
    descriptor = None
    for klass in dummy_A.__mro__:
        if "en" in klass.__dict__:
            descriptor = klass.__dict__["en"]
            break
    assert isinstance(descriptor, property)

def test_dummy_a_has_x():
    assert hasattr(dummy_A, "x")
    descriptor = None
    for klass in dummy_A.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_e_is_not_abstract():
    assert not inspect.isabstract(E)


def test_e_constructor_exists():
    assert callable(E.__init__)


def test_e_constructor_args():
    sig = inspect.signature(E.__init__)
    params = list(sig.parameters.keys())



def test_dummy_g_is_not_abstract():
    assert not inspect.isabstract(dummy_G)


def test_dummy_g_constructor_exists():
    assert callable(dummy_G.__init__)


def test_dummy_g_constructor_args():
    sig = inspect.signature(dummy_G.__init__)
    params = list(sig.parameters.keys())
    assert "gString" in params, "Missing parameter 'gString'"

def test_dummy_g_has_gString():
    assert hasattr(dummy_G, "gString")
    descriptor = None
    for klass in dummy_G.__mro__:
        if "gString" in klass.__dict__:
            descriptor = klass.__dict__["gString"]
            break
    assert isinstance(descriptor, property)



def test_dummy_f_is_not_abstract():
    assert not inspect.isabstract(dummy_F)


def test_dummy_f_constructor_exists():
    assert callable(dummy_F.__init__)


def test_dummy_f_constructor_args():
    sig = inspect.signature(dummy_F.__init__)
    params = list(sig.parameters.keys())
    assert "fString" in params, "Missing parameter 'fString'"
    assert "fDouble" in params, "Missing parameter 'fDouble'"

def test_dummy_f_has_fString():
    assert hasattr(dummy_F, "fString")
    descriptor = None
    for klass in dummy_F.__mro__:
        if "fString" in klass.__dict__:
            descriptor = klass.__dict__["fString"]
            break
    assert isinstance(descriptor, property)

def test_dummy_f_has_fDouble():
    assert hasattr(dummy_F, "fDouble")
    descriptor = None
    for klass in dummy_F.__mro__:
        if "fDouble" in klass.__dict__:
            descriptor = klass.__dict__["fDouble"]
            break
    assert isinstance(descriptor, property)



def test_dummy_c_is_not_abstract():
    assert not inspect.isabstract(dummy_C)


def test_dummy_c_constructor_exists():
    assert callable(dummy_C.__init__)


def test_dummy_c_constructor_args():
    sig = inspect.signature(dummy_C.__init__)
    params = list(sig.parameters.keys())
    assert "k" in params, "Missing parameter 'k'"

def test_dummy_c_has_k():
    assert hasattr(dummy_C, "k")
    descriptor = None
    for klass in dummy_C.__mro__:
        if "k" in klass.__dict__:
            descriptor = klass.__dict__["k"]
            break
    assert isinstance(descriptor, property)

def test_enumexample_exists():
    # Check that the Enumeration exists
    assert EnumExample is not None

def test_enumexample_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnumExample]
    expected_literals = [
        "value2",
        "value3",
        "value1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnumExample"


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
dummy_E_strategy = st.builds(
    dummy_E,
    eName=
        safe_text
)
dummy_D_strategy = st.builds(
    dummy_D,
    name=
        safe_text,
    m=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    l=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dummy_B_strategy = st.builds(
    dummy_B,
    z=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dummy_A_strategy = st.builds(
    dummy_A,
    en=
        safe_text,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
E_strategy = st.builds(
    E,
)
dummy_G_strategy = st.builds(
    dummy_G,
    gString=
        safe_text
)
dummy_F_strategy = st.builds(
    dummy_F,
    fString=
        safe_text,
    fDouble=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dummy_C_strategy = st.builds(
    dummy_C,
    k=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=dummy_E_strategy)
@settings(max_examples=50)
def test_dummy_e_instantiation(instance):
    assert isinstance(instance, dummy_E)



@given(instance=dummy_E_strategy)
def test_dummy_e_eName_setter(instance):
    original = instance.eName
    instance.eName = original
    assert instance.eName == original

@given(instance=dummy_D_strategy)
@settings(max_examples=50)
def test_dummy_d_instantiation(instance):
    assert isinstance(instance, dummy_D)



@given(instance=dummy_D_strategy)
def test_dummy_d_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dummy_D_strategy)
def test_dummy_d_m_setter(instance):
    original = instance.m
    instance.m = original
    assert instance.m == original



@given(instance=dummy_D_strategy)
def test_dummy_d_l_setter(instance):
    original = instance.l
    instance.l = original
    assert instance.l == original

@given(instance=dummy_B_strategy)
@settings(max_examples=50)
def test_dummy_b_instantiation(instance):
    assert isinstance(instance, dummy_B)



@given(instance=dummy_B_strategy)
def test_dummy_b_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original



@given(instance=dummy_B_strategy)
def test_dummy_b_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=dummy_A_strategy)
@settings(max_examples=50)
def test_dummy_a_instantiation(instance):
    assert isinstance(instance, dummy_A)



@given(instance=dummy_A_strategy)
def test_dummy_a_en_setter(instance):
    original = instance.en
    instance.en = original
    assert instance.en == original



@given(instance=dummy_A_strategy)
def test_dummy_a_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=E_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, E)

@given(instance=dummy_G_strategy)
@settings(max_examples=50)
def test_dummy_g_instantiation(instance):
    assert isinstance(instance, dummy_G)



@given(instance=dummy_G_strategy)
def test_dummy_g_gString_setter(instance):
    original = instance.gString
    instance.gString = original
    assert instance.gString == original

@given(instance=dummy_F_strategy)
@settings(max_examples=50)
def test_dummy_f_instantiation(instance):
    assert isinstance(instance, dummy_F)



@given(instance=dummy_F_strategy)
def test_dummy_f_fString_setter(instance):
    original = instance.fString
    instance.fString = original
    assert instance.fString == original



@given(instance=dummy_F_strategy)
def test_dummy_f_fDouble_setter(instance):
    original = instance.fDouble
    instance.fDouble = original
    assert instance.fDouble == original

@given(instance=dummy_C_strategy)
@settings(max_examples=50)
def test_dummy_c_instantiation(instance):
    assert isinstance(instance, dummy_C)



@given(instance=dummy_C_strategy)
def test_dummy_c_k_setter(instance):
    original = instance.k
    instance.k = original
    assert instance.k == original
