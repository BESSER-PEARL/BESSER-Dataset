import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Original_Metamodel_D,
    Original_Metamodel_C,
    Original_Metamodel_B,
    Original_Metamodel_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_original_metamodel_d_is_not_abstract():
    assert not inspect.isabstract(Original_Metamodel_D)


def test_original_metamodel_d_constructor_exists():
    assert callable(Original_Metamodel_D.__init__)


def test_original_metamodel_d_constructor_args():
    sig = inspect.signature(Original_Metamodel_D.__init__)
    params = list(sig.parameters.keys())



def test_original_metamodel_c_is_not_abstract():
    assert not inspect.isabstract(Original_Metamodel_C)


def test_original_metamodel_c_constructor_exists():
    assert callable(Original_Metamodel_C.__init__)


def test_original_metamodel_c_constructor_args():
    sig = inspect.signature(Original_Metamodel_C.__init__)
    params = list(sig.parameters.keys())
    assert "propertyC" in params, "Missing parameter 'propertyC'"

def test_original_metamodel_c_has_propertyC():
    assert hasattr(Original_Metamodel_C, "propertyC")
    descriptor = None
    for klass in Original_Metamodel_C.__mro__:
        if "propertyC" in klass.__dict__:
            descriptor = klass.__dict__["propertyC"]
            break
    assert isinstance(descriptor, property)



def test_original_metamodel_b_is_not_abstract():
    assert not inspect.isabstract(Original_Metamodel_B)


def test_original_metamodel_b_constructor_exists():
    assert callable(Original_Metamodel_B.__init__)


def test_original_metamodel_b_constructor_args():
    sig = inspect.signature(Original_Metamodel_B.__init__)
    params = list(sig.parameters.keys())
    assert "propertyB" in params, "Missing parameter 'propertyB'"

def test_original_metamodel_b_has_propertyB():
    assert hasattr(Original_Metamodel_B, "propertyB")
    descriptor = None
    for klass in Original_Metamodel_B.__mro__:
        if "propertyB" in klass.__dict__:
            descriptor = klass.__dict__["propertyB"]
            break
    assert isinstance(descriptor, property)



def test_original_metamodel_a_is_not_abstract():
    assert not inspect.isabstract(Original_Metamodel_A)


def test_original_metamodel_a_constructor_exists():
    assert callable(Original_Metamodel_A.__init__)


def test_original_metamodel_a_constructor_args():
    sig = inspect.signature(Original_Metamodel_A.__init__)
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
Original_Metamodel_D_strategy = st.builds(
    Original_Metamodel_D,
)
Original_Metamodel_C_strategy = st.builds(
    Original_Metamodel_C,
    propertyC=
        safe_text
)
Original_Metamodel_B_strategy = st.builds(
    Original_Metamodel_B,
    propertyB=
        safe_text
)
Original_Metamodel_A_strategy = st.builds(
    Original_Metamodel_A,
)

@given(instance=Original_Metamodel_D_strategy)
@settings(max_examples=50)
def test_original_metamodel_d_instantiation(instance):
    assert isinstance(instance, Original_Metamodel_D)

@given(instance=Original_Metamodel_C_strategy)
@settings(max_examples=50)
def test_original_metamodel_c_instantiation(instance):
    assert isinstance(instance, Original_Metamodel_C)



@given(instance=Original_Metamodel_C_strategy)
def test_original_metamodel_c_propertyC_setter(instance):
    original = instance.propertyC
    instance.propertyC = original
    assert instance.propertyC == original

@given(instance=Original_Metamodel_B_strategy)
@settings(max_examples=50)
def test_original_metamodel_b_instantiation(instance):
    assert isinstance(instance, Original_Metamodel_B)



@given(instance=Original_Metamodel_B_strategy)
def test_original_metamodel_b_propertyB_setter(instance):
    original = instance.propertyB
    instance.propertyB = original
    assert instance.propertyB == original

@given(instance=Original_Metamodel_A_strategy)
@settings(max_examples=50)
def test_original_metamodel_a_instantiation(instance):
    assert isinstance(instance, Original_Metamodel_A)
