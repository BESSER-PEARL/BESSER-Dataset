import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    C,
    B,
    A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())
    assert "attrC1" in params, "Missing parameter 'attrC1'"
    assert "attrC2" in params, "Missing parameter 'attrC2'"

def test_c_has_attrC1():
    assert hasattr(C, "attrC1")
    descriptor = None
    for klass in C.__mro__:
        if "attrC1" in klass.__dict__:
            descriptor = klass.__dict__["attrC1"]
            break
    assert isinstance(descriptor, property)

def test_c_has_attrC2():
    assert hasattr(C, "attrC2")
    descriptor = None
    for klass in C.__mro__:
        if "attrC2" in klass.__dict__:
            descriptor = klass.__dict__["attrC2"]
            break
    assert isinstance(descriptor, property)



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())
    assert "attrB1" in params, "Missing parameter 'attrB1'"
    assert "attrB2" in params, "Missing parameter 'attrB2'"

def test_b_has_attrB1():
    assert hasattr(B, "attrB1")
    descriptor = None
    for klass in B.__mro__:
        if "attrB1" in klass.__dict__:
            descriptor = klass.__dict__["attrB1"]
            break
    assert isinstance(descriptor, property)

def test_b_has_attrB2():
    assert hasattr(B, "attrB2")
    descriptor = None
    for klass in B.__mro__:
        if "attrB2" in klass.__dict__:
            descriptor = klass.__dict__["attrB2"]
            break
    assert isinstance(descriptor, property)



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())
    assert "attrA2" in params, "Missing parameter 'attrA2'"
    assert "attrA1" in params, "Missing parameter 'attrA1'"

def test_a_has_attrA2():
    assert hasattr(A, "attrA2")
    descriptor = None
    for klass in A.__mro__:
        if "attrA2" in klass.__dict__:
            descriptor = klass.__dict__["attrA2"]
            break
    assert isinstance(descriptor, property)

def test_a_has_attrA1():
    assert hasattr(A, "attrA1")
    descriptor = None
    for klass in A.__mro__:
        if "attrA1" in klass.__dict__:
            descriptor = klass.__dict__["attrA1"]
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
C_strategy = st.builds(
    C,
    attrC1=
        st.integers(),
    attrC2=
        safe_text
)
B_strategy = st.builds(
    B,
    attrB1=
        st.integers(),
    attrB2=
        safe_text
)
A_strategy = st.builds(
    A,
    attrA2=
        safe_text,
    attrA1=
        st.integers()
)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)



@given(instance=C_strategy)
def test_c_attrC1_setter(instance):
    original = instance.attrC1
    instance.attrC1 = original
    assert instance.attrC1 == original



@given(instance=C_strategy)
def test_c_attrC2_setter(instance):
    original = instance.attrC2
    instance.attrC2 = original
    assert instance.attrC2 == original

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)



@given(instance=B_strategy)
def test_b_attrB1_setter(instance):
    original = instance.attrB1
    instance.attrB1 = original
    assert instance.attrB1 == original



@given(instance=B_strategy)
def test_b_attrB2_setter(instance):
    original = instance.attrB2
    instance.attrB2 = original
    assert instance.attrB2 == original

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)



@given(instance=A_strategy)
def test_a_attrA2_setter(instance):
    original = instance.attrA2
    instance.attrA2 = original
    assert instance.attrA2 == original



@given(instance=A_strategy)
def test_a_attrA1_setter(instance):
    original = instance.attrA1
    instance.attrA1 = original
    assert instance.attrA1 == original
