import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    A,
    MM1::B,
    MM1::D,
    MM1::C,
    MM1::A,
    MM1::ContainerMM1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_mm1::b_is_not_abstract():
    assert not inspect.isabstract(MM1::B)


def test_mm1::b_constructor_exists():
    assert callable(MM1::B.__init__)


def test_mm1::b_constructor_args():
    sig = inspect.signature(MM1::B.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mm1::b_has_value():
    assert hasattr(MM1::B, "value")
    descriptor = None
    for klass in MM1::B.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mm1::d_is_not_abstract():
    assert not inspect.isabstract(MM1::D)


def test_mm1::d_constructor_exists():
    assert callable(MM1::D.__init__)


def test_mm1::d_constructor_args():
    sig = inspect.signature(MM1::D.__init__)
    params = list(sig.parameters.keys())



def test_mm1::c_is_not_abstract():
    assert not inspect.isabstract(MM1::C)


def test_mm1::c_constructor_exists():
    assert callable(MM1::C.__init__)


def test_mm1::c_constructor_args():
    sig = inspect.signature(MM1::C.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mm1::c_has_value():
    assert hasattr(MM1::C, "value")
    descriptor = None
    for klass in MM1::C.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mm1::a_is_not_abstract():
    assert not inspect.isabstract(MM1::A)


def test_mm1::a_constructor_exists():
    assert callable(MM1::A.__init__)


def test_mm1::a_constructor_args():
    sig = inspect.signature(MM1::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm1::a_has_name():
    assert hasattr(MM1::A, "name")
    descriptor = None
    for klass in MM1::A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm1::containermm1_is_not_abstract():
    assert not inspect.isabstract(MM1::ContainerMM1)


def test_mm1::containermm1_constructor_exists():
    assert callable(MM1::ContainerMM1.__init__)


def test_mm1::containermm1_constructor_args():
    sig = inspect.signature(MM1::ContainerMM1.__init__)
    params = list(sig.parameters.keys())
    assert "aname" in params, "Missing parameter 'aname'"

def test_mm1::containermm1_has_aname():
    assert hasattr(MM1::ContainerMM1, "aname")
    descriptor = None
    for klass in MM1::ContainerMM1.__mro__:
        if "aname" in klass.__dict__:
            descriptor = klass.__dict__["aname"]
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
A_strategy = st.builds(
    A,
)
MM1::B_strategy = st.builds(
    MM1::B,
    value=
        st.integers()
)
MM1::D_strategy = st.builds(
    MM1::D,
)
MM1::C_strategy = st.builds(
    MM1::C,
    value=
        st.booleans()
)
MM1::A_strategy = st.builds(
    MM1::A,
    name=
        safe_text
)
MM1::ContainerMM1_strategy = st.builds(
    MM1::ContainerMM1,
    aname=
        st.integers()
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=MM1::B_strategy)
@settings(max_examples=50)
def test_mm1::b_instantiation(instance):
    assert isinstance(instance, MM1::B)

@given(instance=MM1::B_strategy)
def test_mm1::b_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=MM1::B_strategy)
def test_mm1::b_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MM1::D_strategy)
@settings(max_examples=50)
def test_mm1::d_instantiation(instance):
    assert isinstance(instance, MM1::D)

@given(instance=MM1::C_strategy)
@settings(max_examples=50)
def test_mm1::c_instantiation(instance):
    assert isinstance(instance, MM1::C)

@given(instance=MM1::C_strategy)
def test_mm1::c_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=MM1::C_strategy)
def test_mm1::c_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MM1::A_strategy)
@settings(max_examples=50)
def test_mm1::a_instantiation(instance):
    assert isinstance(instance, MM1::A)

@given(instance=MM1::A_strategy)
def test_mm1::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MM1::A_strategy)
def test_mm1::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MM1::ContainerMM1_strategy)
@settings(max_examples=50)
def test_mm1::containermm1_instantiation(instance):
    assert isinstance(instance, MM1::ContainerMM1)

@given(instance=MM1::ContainerMM1_strategy)
def test_mm1::containermm1_aname_type(instance):
    assert isinstance(instance.aname, int)


@given(instance=MM1::ContainerMM1_strategy)
def test_mm1::containermm1_aname_setter(instance):
    original = instance.aname
    instance.aname = original
    assert instance.aname == original
