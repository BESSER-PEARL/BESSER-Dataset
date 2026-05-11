import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dummy::E,
    dummy::D,
    dummy::B,
    dummy::A,
    E,
    dummy::G,
    dummy::F,
    dummy::C,
    EnumExample,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dummy::e_is_not_abstract():
    assert not inspect.isabstract(dummy::E)


def test_dummy::e_constructor_exists():
    assert callable(dummy::E.__init__)


def test_dummy::e_constructor_args():
    sig = inspect.signature(dummy::E.__init__)
    params = list(sig.parameters.keys())
    assert "eName" in params, "Missing parameter 'eName'"

def test_dummy::e_has_eName():
    assert hasattr(dummy::E, "eName")
    descriptor = None
    for klass in dummy::E.__mro__:
        if "eName" in klass.__dict__:
            descriptor = klass.__dict__["eName"]
            break
    assert isinstance(descriptor, property)



def test_dummy::d_is_not_abstract():
    assert not inspect.isabstract(dummy::D)


def test_dummy::d_constructor_exists():
    assert callable(dummy::D.__init__)


def test_dummy::d_constructor_args():
    sig = inspect.signature(dummy::D.__init__)
    params = list(sig.parameters.keys())
    assert "m" in params, "Missing parameter 'm'"
    assert "name" in params, "Missing parameter 'name'"
    assert "l" in params, "Missing parameter 'l'"

def test_dummy::d_has_m():
    assert hasattr(dummy::D, "m")
    descriptor = None
    for klass in dummy::D.__mro__:
        if "m" in klass.__dict__:
            descriptor = klass.__dict__["m"]
            break
    assert isinstance(descriptor, property)

def test_dummy::d_has_name():
    assert hasattr(dummy::D, "name")
    descriptor = None
    for klass in dummy::D.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dummy::d_has_l():
    assert hasattr(dummy::D, "l")
    descriptor = None
    for klass in dummy::D.__mro__:
        if "l" in klass.__dict__:
            descriptor = klass.__dict__["l"]
            break
    assert isinstance(descriptor, property)



def test_dummy::b_is_not_abstract():
    assert not inspect.isabstract(dummy::B)


def test_dummy::b_constructor_exists():
    assert callable(dummy::B.__init__)


def test_dummy::b_constructor_args():
    sig = inspect.signature(dummy::B.__init__)
    params = list(sig.parameters.keys())
    assert "z" in params, "Missing parameter 'z'"
    assert "y" in params, "Missing parameter 'y'"

def test_dummy::b_has_z():
    assert hasattr(dummy::B, "z")
    descriptor = None
    for klass in dummy::B.__mro__:
        if "z" in klass.__dict__:
            descriptor = klass.__dict__["z"]
            break
    assert isinstance(descriptor, property)

def test_dummy::b_has_y():
    assert hasattr(dummy::B, "y")
    descriptor = None
    for klass in dummy::B.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_dummy::a_is_not_abstract():
    assert not inspect.isabstract(dummy::A)


def test_dummy::a_constructor_exists():
    assert callable(dummy::A.__init__)


def test_dummy::a_constructor_args():
    sig = inspect.signature(dummy::A.__init__)
    params = list(sig.parameters.keys())
    assert "en" in params, "Missing parameter 'en'"
    assert "x" in params, "Missing parameter 'x'"

def test_dummy::a_has_en():
    assert hasattr(dummy::A, "en")
    descriptor = None
    for klass in dummy::A.__mro__:
        if "en" in klass.__dict__:
            descriptor = klass.__dict__["en"]
            break
    assert isinstance(descriptor, property)

def test_dummy::a_has_x():
    assert hasattr(dummy::A, "x")
    descriptor = None
    for klass in dummy::A.__mro__:
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



def test_dummy::g_is_not_abstract():
    assert not inspect.isabstract(dummy::G)


def test_dummy::g_constructor_exists():
    assert callable(dummy::G.__init__)


def test_dummy::g_constructor_args():
    sig = inspect.signature(dummy::G.__init__)
    params = list(sig.parameters.keys())
    assert "gString" in params, "Missing parameter 'gString'"

def test_dummy::g_has_gString():
    assert hasattr(dummy::G, "gString")
    descriptor = None
    for klass in dummy::G.__mro__:
        if "gString" in klass.__dict__:
            descriptor = klass.__dict__["gString"]
            break
    assert isinstance(descriptor, property)



def test_dummy::f_is_not_abstract():
    assert not inspect.isabstract(dummy::F)


def test_dummy::f_constructor_exists():
    assert callable(dummy::F.__init__)


def test_dummy::f_constructor_args():
    sig = inspect.signature(dummy::F.__init__)
    params = list(sig.parameters.keys())
    assert "fDouble" in params, "Missing parameter 'fDouble'"
    assert "fString" in params, "Missing parameter 'fString'"

def test_dummy::f_has_fDouble():
    assert hasattr(dummy::F, "fDouble")
    descriptor = None
    for klass in dummy::F.__mro__:
        if "fDouble" in klass.__dict__:
            descriptor = klass.__dict__["fDouble"]
            break
    assert isinstance(descriptor, property)

def test_dummy::f_has_fString():
    assert hasattr(dummy::F, "fString")
    descriptor = None
    for klass in dummy::F.__mro__:
        if "fString" in klass.__dict__:
            descriptor = klass.__dict__["fString"]
            break
    assert isinstance(descriptor, property)



def test_dummy::c_is_not_abstract():
    assert not inspect.isabstract(dummy::C)


def test_dummy::c_constructor_exists():
    assert callable(dummy::C.__init__)


def test_dummy::c_constructor_args():
    sig = inspect.signature(dummy::C.__init__)
    params = list(sig.parameters.keys())
    assert "k" in params, "Missing parameter 'k'"

def test_dummy::c_has_k():
    assert hasattr(dummy::C, "k")
    descriptor = None
    for klass in dummy::C.__mro__:
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
        "value3",
        "value1",
        "value2",
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
dummy::E_strategy = st.builds(
    dummy::E,
    eName=
        safe_text
)
dummy::D_strategy = st.builds(
    dummy::D,
    m=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    l=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dummy::B_strategy = st.builds(
    dummy::B,
    z=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dummy::A_strategy = st.builds(
    dummy::A,
    en=
        safe_text,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
E_strategy = st.builds(
    E,
)
dummy::G_strategy = st.builds(
    dummy::G,
    gString=
        safe_text
)
dummy::F_strategy = st.builds(
    dummy::F,
    fDouble=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    fString=
        safe_text
)
dummy::C_strategy = st.builds(
    dummy::C,
    k=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=dummy::E_strategy)
@settings(max_examples=50)
def test_dummy::e_instantiation(instance):
    assert isinstance(instance, dummy::E)

@given(instance=dummy::E_strategy)
def test_dummy::e_eName_type(instance):
    assert isinstance(instance.eName, str)


@given(instance=dummy::E_strategy)
def test_dummy::e_eName_setter(instance):
    original = instance.eName
    instance.eName = original
    assert instance.eName == original

@given(instance=dummy::D_strategy)
@settings(max_examples=50)
def test_dummy::d_instantiation(instance):
    assert isinstance(instance, dummy::D)

@given(instance=dummy::D_strategy)
def test_dummy::d_m_type(instance):
    assert isinstance(instance.m, float)


@given(instance=dummy::D_strategy)
def test_dummy::d_m_setter(instance):
    original = instance.m
    instance.m = original
    assert instance.m == original

@given(instance=dummy::D_strategy)
def test_dummy::d_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dummy::D_strategy)
def test_dummy::d_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dummy::D_strategy)
def test_dummy::d_l_type(instance):
    assert isinstance(instance.l, float)


@given(instance=dummy::D_strategy)
def test_dummy::d_l_setter(instance):
    original = instance.l
    instance.l = original
    assert instance.l == original

@given(instance=dummy::B_strategy)
@settings(max_examples=50)
def test_dummy::b_instantiation(instance):
    assert isinstance(instance, dummy::B)

@given(instance=dummy::B_strategy)
def test_dummy::b_z_type(instance):
    assert isinstance(instance.z, float)


@given(instance=dummy::B_strategy)
def test_dummy::b_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original

@given(instance=dummy::B_strategy)
def test_dummy::b_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=dummy::B_strategy)
def test_dummy::b_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=dummy::A_strategy)
@settings(max_examples=50)
def test_dummy::a_instantiation(instance):
    assert isinstance(instance, dummy::A)

@given(instance=dummy::A_strategy)
def test_dummy::a_en_type(instance):
    assert isinstance(instance.en, str)


@given(instance=dummy::A_strategy)
def test_dummy::a_en_setter(instance):
    original = instance.en
    instance.en = original
    assert instance.en == original

@given(instance=dummy::A_strategy)
def test_dummy::a_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=dummy::A_strategy)
def test_dummy::a_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=E_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, E)

@given(instance=dummy::G_strategy)
@settings(max_examples=50)
def test_dummy::g_instantiation(instance):
    assert isinstance(instance, dummy::G)

@given(instance=dummy::G_strategy)
def test_dummy::g_gString_type(instance):
    assert isinstance(instance.gString, str)


@given(instance=dummy::G_strategy)
def test_dummy::g_gString_setter(instance):
    original = instance.gString
    instance.gString = original
    assert instance.gString == original

@given(instance=dummy::F_strategy)
@settings(max_examples=50)
def test_dummy::f_instantiation(instance):
    assert isinstance(instance, dummy::F)

@given(instance=dummy::F_strategy)
def test_dummy::f_fDouble_type(instance):
    assert isinstance(instance.fDouble, float)


@given(instance=dummy::F_strategy)
def test_dummy::f_fDouble_setter(instance):
    original = instance.fDouble
    instance.fDouble = original
    assert instance.fDouble == original

@given(instance=dummy::F_strategy)
def test_dummy::f_fString_type(instance):
    assert isinstance(instance.fString, str)


@given(instance=dummy::F_strategy)
def test_dummy::f_fString_setter(instance):
    original = instance.fString
    instance.fString = original
    assert instance.fString == original

@given(instance=dummy::C_strategy)
@settings(max_examples=50)
def test_dummy::c_instantiation(instance):
    assert isinstance(instance, dummy::C)

@given(instance=dummy::C_strategy)
def test_dummy::c_k_type(instance):
    assert isinstance(instance.k, float)


@given(instance=dummy::C_strategy)
def test_dummy::c_k_setter(instance):
    original = instance.k
    instance.k = original
    assert instance.k == original
