import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sample_C,
    A,
    sample_B,
    sample_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sample_c_is_not_abstract():
    assert not inspect.isabstract(sample_C)


def test_sample_c_constructor_exists():
    assert callable(sample_C.__init__)


def test_sample_c_constructor_args():
    sig = inspect.signature(sample_C.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_sample_b_is_not_abstract():
    assert not inspect.isabstract(sample_B)


def test_sample_b_constructor_exists():
    assert callable(sample_B.__init__)


def test_sample_b_constructor_args():
    sig = inspect.signature(sample_B.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_sample_b_has_label():
    assert hasattr(sample_B, "label")
    descriptor = None
    for klass in sample_B.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_sample_a_is_not_abstract():
    assert not inspect.isabstract(sample_A)


def test_sample_a_constructor_exists():
    assert callable(sample_A.__init__)


def test_sample_a_constructor_args():
    sig = inspect.signature(sample_A.__init__)
    params = list(sig.parameters.keys())
    assert "valid" in params, "Missing parameter 'valid'"
    assert "name" in params, "Missing parameter 'name'"
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_sample_a_has_valid():
    assert hasattr(sample_A, "valid")
    descriptor = None
    for klass in sample_A.__mro__:
        if "valid" in klass.__dict__:
            descriptor = klass.__dict__["valid"]
            break
    assert isinstance(descriptor, property)

def test_sample_a_has_name():
    assert hasattr(sample_A, "name")
    descriptor = None
    for klass in sample_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sample_a_has_quantity():
    assert hasattr(sample_A, "quantity")
    descriptor = None
    for klass in sample_A.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
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
sample_C_strategy = st.builds(
    sample_C,
)
A_strategy = st.builds(
    A,
)
sample_B_strategy = st.builds(
    sample_B,
    label=
        safe_text
)
sample_A_strategy = st.builds(
    sample_A,
    valid=
        st.booleans(),
    name=
        safe_text,
    quantity=
        st.integers()
)

@given(instance=sample_C_strategy)
@settings(max_examples=50)
def test_sample_c_instantiation(instance):
    assert isinstance(instance, sample_C)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=sample_B_strategy)
@settings(max_examples=50)
def test_sample_b_instantiation(instance):
    assert isinstance(instance, sample_B)



@given(instance=sample_B_strategy)
def test_sample_b_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=sample_A_strategy)
@settings(max_examples=50)
def test_sample_a_instantiation(instance):
    assert isinstance(instance, sample_A)



@given(instance=sample_A_strategy)
def test_sample_a_valid_setter(instance):
    original = instance.valid
    instance.valid = original
    assert instance.valid == original



@given(instance=sample_A_strategy)
def test_sample_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sample_A_strategy)
def test_sample_a_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original
