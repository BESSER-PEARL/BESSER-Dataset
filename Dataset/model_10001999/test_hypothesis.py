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
    assert "attrCA" in params, "Missing parameter 'attrCA'"
    assert "attrC2" in params, "Missing parameter 'attrC2'"

def test_c_has_attrCA():
    assert hasattr(C, "attrCA")
    descriptor = None
    for klass in C.__mro__:
        if "attrCA" in klass.__dict__:
            descriptor = klass.__dict__["attrCA"]
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
    assert "attrB" in params, "Missing parameter 'attrB'"

def test_b_has_attrB():
    assert hasattr(B, "attrB")
    descriptor = None
    for klass in B.__mro__:
        if "attrB" in klass.__dict__:
            descriptor = klass.__dict__["attrB"]
            break
    assert isinstance(descriptor, property)



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())
    assert "attrA" in params, "Missing parameter 'attrA'"

def test_a_has_attrA():
    assert hasattr(A, "attrA")
    descriptor = None
    for klass in A.__mro__:
        if "attrA" in klass.__dict__:
            descriptor = klass.__dict__["attrA"]
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
    attrCA=
        st.integers(),
    attrC2=
        st.booleans()
)
B_strategy = st.builds(
    B,
    attrB=
        safe_text
)
A_strategy = st.builds(
    A,
    attrA=
        safe_text
)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)



@given(instance=C_strategy)
def test_c_attrCA_setter(instance):
    original = instance.attrCA
    instance.attrCA = original
    assert instance.attrCA == original



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
def test_b_attrB_setter(instance):
    original = instance.attrB
    instance.attrB = original
    assert instance.attrB == original

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)



@given(instance=A_strategy)
def test_a_attrA_setter(instance):
    original = instance.attrA
    instance.attrA = original
    assert instance.attrA == original
