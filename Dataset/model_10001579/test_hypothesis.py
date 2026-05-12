import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    C1,
    B1,
    A1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_c1_is_not_abstract():
    assert not inspect.isabstract(C1)


def test_c1_constructor_exists():
    assert callable(C1.__init__)


def test_c1_constructor_args():
    sig = inspect.signature(C1.__init__)
    params = list(sig.parameters.keys())
    assert "attc1" in params, "Missing parameter 'attc1'"
    assert "attc2" in params, "Missing parameter 'attc2'"

def test_c1_has_attc1():
    assert hasattr(C1, "attc1")
    descriptor = None
    for klass in C1.__mro__:
        if "attc1" in klass.__dict__:
            descriptor = klass.__dict__["attc1"]
            break
    assert isinstance(descriptor, property)

def test_c1_has_attc2():
    assert hasattr(C1, "attc2")
    descriptor = None
    for klass in C1.__mro__:
        if "attc2" in klass.__dict__:
            descriptor = klass.__dict__["attc2"]
            break
    assert isinstance(descriptor, property)



def test_b1_is_not_abstract():
    assert not inspect.isabstract(B1)


def test_b1_constructor_exists():
    assert callable(B1.__init__)


def test_b1_constructor_args():
    sig = inspect.signature(B1.__init__)
    params = list(sig.parameters.keys())
    assert "attb" in params, "Missing parameter 'attb'"

def test_b1_has_attb():
    assert hasattr(B1, "attb")
    descriptor = None
    for klass in B1.__mro__:
        if "attb" in klass.__dict__:
            descriptor = klass.__dict__["attb"]
            break
    assert isinstance(descriptor, property)



def test_a1_is_not_abstract():
    assert not inspect.isabstract(A1)


def test_a1_constructor_exists():
    assert callable(A1.__init__)


def test_a1_constructor_args():
    sig = inspect.signature(A1.__init__)
    params = list(sig.parameters.keys())
    assert "atta" in params, "Missing parameter 'atta'"

def test_a1_has_atta():
    assert hasattr(A1, "atta")
    descriptor = None
    for klass in A1.__mro__:
        if "atta" in klass.__dict__:
            descriptor = klass.__dict__["atta"]
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
C1_strategy = st.builds(
    C1,
    attc1=
        st.integers(),
    attc2=
        st.booleans()
)
B1_strategy = st.builds(
    B1,
    attb=
        st.integers()
)
A1_strategy = st.builds(
    A1,
    atta=
        safe_text
)

@given(instance=C1_strategy)
@settings(max_examples=50)
def test_c1_instantiation(instance):
    assert isinstance(instance, C1)



@given(instance=C1_strategy)
def test_c1_attc1_setter(instance):
    original = instance.attc1
    instance.attc1 = original
    assert instance.attc1 == original



@given(instance=C1_strategy)
def test_c1_attc2_setter(instance):
    original = instance.attc2
    instance.attc2 = original
    assert instance.attc2 == original

@given(instance=B1_strategy)
@settings(max_examples=50)
def test_b1_instantiation(instance):
    assert isinstance(instance, B1)



@given(instance=B1_strategy)
def test_b1_attb_setter(instance):
    original = instance.attb
    instance.attb = original
    assert instance.attb == original

@given(instance=A1_strategy)
@settings(max_examples=50)
def test_a1_instantiation(instance):
    assert isinstance(instance, A1)



@given(instance=A1_strategy)
def test_a1_atta_setter(instance):
    original = instance.atta
    instance.atta = original
    assert instance.atta == original
