import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    C3,
    C2,
    C1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_c3_is_not_abstract():
    assert not inspect.isabstract(C3)


def test_c3_constructor_exists():
    assert callable(C3.__init__)


def test_c3_constructor_args():
    sig = inspect.signature(C3.__init__)
    params = list(sig.parameters.keys())



def test_c2_is_not_abstract():
    assert not inspect.isabstract(C2)


def test_c2_constructor_exists():
    assert callable(C2.__init__)


def test_c2_constructor_args():
    sig = inspect.signature(C2.__init__)
    params = list(sig.parameters.keys())
    assert "C2ID" in params, "Missing parameter 'C2ID'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "C1ID" in params, "Missing parameter 'C1ID'"

def test_c2_has_C2ID():
    assert hasattr(C2, "C2ID")
    descriptor = None
    for klass in C2.__mro__:
        if "C2ID" in klass.__dict__:
            descriptor = klass.__dict__["C2ID"]
            break
    assert isinstance(descriptor, property)

def test_c2_has_attribute():
    assert hasattr(C2, "attribute")
    descriptor = None
    for klass in C2.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_c2_has_C1ID():
    assert hasattr(C2, "C1ID")
    descriptor = None
    for klass in C2.__mro__:
        if "C1ID" in klass.__dict__:
            descriptor = klass.__dict__["C1ID"]
            break
    assert isinstance(descriptor, property)



def test_c1_is_not_abstract():
    assert not inspect.isabstract(C1)


def test_c1_constructor_exists():
    assert callable(C1.__init__)


def test_c1_constructor_args():
    sig = inspect.signature(C1.__init__)
    params = list(sig.parameters.keys())
    assert "C1ID" in params, "Missing parameter 'C1ID'"

def test_c1_has_C1ID():
    assert hasattr(C1, "C1ID")
    descriptor = None
    for klass in C1.__mro__:
        if "C1ID" in klass.__dict__:
            descriptor = klass.__dict__["C1ID"]
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
C3_strategy = st.builds(
    C3,
)
C2_strategy = st.builds(
    C2,
    C2ID=
        st.integers(),
    attribute=
        safe_text,
    C1ID=
        st.integers()
)
C1_strategy = st.builds(
    C1,
    C1ID=
        st.integers()
)

@given(instance=C3_strategy)
@settings(max_examples=50)
def test_c3_instantiation(instance):
    assert isinstance(instance, C3)

@given(instance=C2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, C2)



@given(instance=C2_strategy)
def test_c2_C2ID_setter(instance):
    original = instance.C2ID
    instance.C2ID = original
    assert instance.C2ID == original



@given(instance=C2_strategy)
def test_c2_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=C2_strategy)
def test_c2_C1ID_setter(instance):
    original = instance.C1ID
    instance.C1ID = original
    assert instance.C1ID == original

@given(instance=C1_strategy)
@settings(max_examples=50)
def test_c1_instantiation(instance):
    assert isinstance(instance, C1)



@given(instance=C1_strategy)
def test_c1_C1ID_setter(instance):
    original = instance.C1ID
    instance.C1ID = original
    assert instance.C1ID == original
