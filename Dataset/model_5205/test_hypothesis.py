import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Original::Metamodel::D,
    Original::Metamodel::C,
    Original::Metamodel::B,
    Original::Metamodel::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_original::metamodel::d_is_not_abstract():
    assert not inspect.isabstract(Original::Metamodel::D)


def test_original::metamodel::d_constructor_exists():
    assert callable(Original::Metamodel::D.__init__)


def test_original::metamodel::d_constructor_args():
    sig = inspect.signature(Original::Metamodel::D.__init__)
    params = list(sig.parameters.keys())



def test_original::metamodel::c_is_not_abstract():
    assert not inspect.isabstract(Original::Metamodel::C)


def test_original::metamodel::c_constructor_exists():
    assert callable(Original::Metamodel::C.__init__)


def test_original::metamodel::c_constructor_args():
    sig = inspect.signature(Original::Metamodel::C.__init__)
    params = list(sig.parameters.keys())
    assert "propertyC" in params, "Missing parameter 'propertyC'"

def test_original::metamodel::c_has_propertyC():
    assert hasattr(Original::Metamodel::C, "propertyC")
    descriptor = None
    for klass in Original::Metamodel::C.__mro__:
        if "propertyC" in klass.__dict__:
            descriptor = klass.__dict__["propertyC"]
            break
    assert isinstance(descriptor, property)



def test_original::metamodel::b_is_not_abstract():
    assert not inspect.isabstract(Original::Metamodel::B)


def test_original::metamodel::b_constructor_exists():
    assert callable(Original::Metamodel::B.__init__)


def test_original::metamodel::b_constructor_args():
    sig = inspect.signature(Original::Metamodel::B.__init__)
    params = list(sig.parameters.keys())
    assert "propertyB" in params, "Missing parameter 'propertyB'"

def test_original::metamodel::b_has_propertyB():
    assert hasattr(Original::Metamodel::B, "propertyB")
    descriptor = None
    for klass in Original::Metamodel::B.__mro__:
        if "propertyB" in klass.__dict__:
            descriptor = klass.__dict__["propertyB"]
            break
    assert isinstance(descriptor, property)



def test_original::metamodel::a_is_not_abstract():
    assert not inspect.isabstract(Original::Metamodel::A)


def test_original::metamodel::a_constructor_exists():
    assert callable(Original::Metamodel::A.__init__)


def test_original::metamodel::a_constructor_args():
    sig = inspect.signature(Original::Metamodel::A.__init__)
    params = list(sig.parameters.keys())


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
Original::Metamodel::D_strategy = st.builds(
    Original::Metamodel::D,
)
Original::Metamodel::C_strategy = st.builds(
    Original::Metamodel::C,
    propertyC=
        safe_text
)
Original::Metamodel::B_strategy = st.builds(
    Original::Metamodel::B,
    propertyB=
        safe_text
)
Original::Metamodel::A_strategy = st.builds(
    Original::Metamodel::A,
)

@given(instance=Original::Metamodel::D_strategy)
@settings(max_examples=50)
def test_original::metamodel::d_instantiation(instance):
    assert isinstance(instance, Original::Metamodel::D)

@given(instance=Original::Metamodel::C_strategy)
@settings(max_examples=50)
def test_original::metamodel::c_instantiation(instance):
    assert isinstance(instance, Original::Metamodel::C)

@given(instance=Original::Metamodel::C_strategy)
def test_original::metamodel::c_propertyC_type(instance):
    assert isinstance(instance.propertyC, str)


@given(instance=Original::Metamodel::C_strategy)
def test_original::metamodel::c_propertyC_setter(instance):
    original = instance.propertyC
    instance.propertyC = original
    assert instance.propertyC == original

@given(instance=Original::Metamodel::B_strategy)
@settings(max_examples=50)
def test_original::metamodel::b_instantiation(instance):
    assert isinstance(instance, Original::Metamodel::B)

@given(instance=Original::Metamodel::B_strategy)
def test_original::metamodel::b_propertyB_type(instance):
    assert isinstance(instance.propertyB, str)


@given(instance=Original::Metamodel::B_strategy)
def test_original::metamodel::b_propertyB_setter(instance):
    original = instance.propertyB
    instance.propertyB = original
    assert instance.propertyB == original

@given(instance=Original::Metamodel::A_strategy)
@settings(max_examples=50)
def test_original::metamodel::a_instantiation(instance):
    assert isinstance(instance, Original::Metamodel::A)
