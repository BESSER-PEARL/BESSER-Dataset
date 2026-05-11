import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sample::C,
    A,
    sample::B,
    sample::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sample::c_is_not_abstract():
    assert not inspect.isabstract(sample::C)


def test_sample::c_constructor_exists():
    assert callable(sample::C.__init__)


def test_sample::c_constructor_args():
    sig = inspect.signature(sample::C.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_sample::b_is_not_abstract():
    assert not inspect.isabstract(sample::B)


def test_sample::b_constructor_exists():
    assert callable(sample::B.__init__)


def test_sample::b_constructor_args():
    sig = inspect.signature(sample::B.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_sample::b_has_label():
    assert hasattr(sample::B, "label")
    descriptor = None
    for klass in sample::B.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_sample::a_is_not_abstract():
    assert not inspect.isabstract(sample::A)


def test_sample::a_constructor_exists():
    assert callable(sample::A.__init__)


def test_sample::a_constructor_args():
    sig = inspect.signature(sample::A.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "valid" in params, "Missing parameter 'valid'"
    assert "name" in params, "Missing parameter 'name'"

def test_sample::a_has_quantity():
    assert hasattr(sample::A, "quantity")
    descriptor = None
    for klass in sample::A.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_sample::a_has_valid():
    assert hasattr(sample::A, "valid")
    descriptor = None
    for klass in sample::A.__mro__:
        if "valid" in klass.__dict__:
            descriptor = klass.__dict__["valid"]
            break
    assert isinstance(descriptor, property)

def test_sample::a_has_name():
    assert hasattr(sample::A, "name")
    descriptor = None
    for klass in sample::A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
sample::C_strategy = st.builds(
    sample::C,
)
A_strategy = st.builds(
    A,
)
sample::B_strategy = st.builds(
    sample::B,
    label=
        safe_text
)
sample::A_strategy = st.builds(
    sample::A,
    quantity=
        st.integers(),
    valid=
        st.booleans(),
    name=
        safe_text
)

@given(instance=sample::C_strategy)
@settings(max_examples=50)
def test_sample::c_instantiation(instance):
    assert isinstance(instance, sample::C)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=sample::B_strategy)
@settings(max_examples=50)
def test_sample::b_instantiation(instance):
    assert isinstance(instance, sample::B)

@given(instance=sample::B_strategy)
def test_sample::b_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=sample::B_strategy)
def test_sample::b_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=sample::A_strategy)
@settings(max_examples=50)
def test_sample::a_instantiation(instance):
    assert isinstance(instance, sample::A)

@given(instance=sample::A_strategy)
def test_sample::a_quantity_type(instance):
    assert isinstance(instance.quantity, int)


@given(instance=sample::A_strategy)
def test_sample::a_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=sample::A_strategy)
def test_sample::a_valid_type(instance):
    assert isinstance(instance.valid, bool)


@given(instance=sample::A_strategy)
def test_sample::a_valid_setter(instance):
    original = instance.valid
    instance.valid = original
    assert instance.valid == original

@given(instance=sample::A_strategy)
def test_sample::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sample::A_strategy)
def test_sample::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
