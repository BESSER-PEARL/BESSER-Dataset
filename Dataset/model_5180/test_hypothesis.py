import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    A,
    MM1_B,
    MM1_D,
    MM1_C,
    MM1_A,
    MM1_ContainerMM1,
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



def test_mm1_b_is_not_abstract():
    assert not inspect.isabstract(MM1_B)


def test_mm1_b_constructor_exists():
    assert callable(MM1_B.__init__)


def test_mm1_b_constructor_args():
    sig = inspect.signature(MM1_B.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mm1_b_has_value():
    assert hasattr(MM1_B, "value")
    descriptor = None
    for klass in MM1_B.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mm1_d_is_not_abstract():
    assert not inspect.isabstract(MM1_D)


def test_mm1_d_constructor_exists():
    assert callable(MM1_D.__init__)


def test_mm1_d_constructor_args():
    sig = inspect.signature(MM1_D.__init__)
    params = list(sig.parameters.keys())



def test_mm1_c_is_not_abstract():
    assert not inspect.isabstract(MM1_C)


def test_mm1_c_constructor_exists():
    assert callable(MM1_C.__init__)


def test_mm1_c_constructor_args():
    sig = inspect.signature(MM1_C.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mm1_c_has_value():
    assert hasattr(MM1_C, "value")
    descriptor = None
    for klass in MM1_C.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mm1_a_is_not_abstract():
    assert not inspect.isabstract(MM1_A)


def test_mm1_a_constructor_exists():
    assert callable(MM1_A.__init__)


def test_mm1_a_constructor_args():
    sig = inspect.signature(MM1_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm1_a_has_name():
    assert hasattr(MM1_A, "name")
    descriptor = None
    for klass in MM1_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm1_containermm1_is_not_abstract():
    assert not inspect.isabstract(MM1_ContainerMM1)


def test_mm1_containermm1_constructor_exists():
    assert callable(MM1_ContainerMM1.__init__)


def test_mm1_containermm1_constructor_args():
    sig = inspect.signature(MM1_ContainerMM1.__init__)
    params = list(sig.parameters.keys())
    assert "aname" in params, "Missing parameter 'aname'"

def test_mm1_containermm1_has_aname():
    assert hasattr(MM1_ContainerMM1, "aname")
    descriptor = None
    for klass in MM1_ContainerMM1.__mro__:
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
MM1_B_strategy = st.builds(
    MM1_B,
    value=
        st.integers()
)
MM1_D_strategy = st.builds(
    MM1_D,
)
MM1_C_strategy = st.builds(
    MM1_C,
    value=
        st.booleans()
)
MM1_A_strategy = st.builds(
    MM1_A,
    name=
        safe_text
)
MM1_ContainerMM1_strategy = st.builds(
    MM1_ContainerMM1,
    aname=
        st.integers()
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=MM1_B_strategy)
@settings(max_examples=50)
def test_mm1_b_instantiation(instance):
    assert isinstance(instance, MM1_B)



@given(instance=MM1_B_strategy)
def test_mm1_b_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MM1_D_strategy)
@settings(max_examples=50)
def test_mm1_d_instantiation(instance):
    assert isinstance(instance, MM1_D)

@given(instance=MM1_C_strategy)
@settings(max_examples=50)
def test_mm1_c_instantiation(instance):
    assert isinstance(instance, MM1_C)



@given(instance=MM1_C_strategy)
def test_mm1_c_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MM1_A_strategy)
@settings(max_examples=50)
def test_mm1_a_instantiation(instance):
    assert isinstance(instance, MM1_A)



@given(instance=MM1_A_strategy)
def test_mm1_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MM1_ContainerMM1_strategy)
@settings(max_examples=50)
def test_mm1_containermm1_instantiation(instance):
    assert isinstance(instance, MM1_ContainerMM1)



@given(instance=MM1_ContainerMM1_strategy)
def test_mm1_containermm1_aname_setter(instance):
    original = instance.aname
    instance.aname = original
    assert instance.aname == original
