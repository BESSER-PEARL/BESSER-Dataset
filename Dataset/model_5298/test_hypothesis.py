import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    B,
    tderived::B2,
    tderived::D,
    A,
    tderived::A2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_tderived::b2_is_not_abstract():
    assert not inspect.isabstract(tderived::B2)


def test_tderived::b2_constructor_exists():
    assert callable(tderived::B2.__init__)


def test_tderived::b2_constructor_args():
    sig = inspect.signature(tderived::B2.__init__)
    params = list(sig.parameters.keys())
    assert "anotherName" in params, "Missing parameter 'anotherName'"

def test_tderived::b2_has_anotherName():
    assert hasattr(tderived::B2, "anotherName")
    descriptor = None
    for klass in tderived::B2.__mro__:
        if "anotherName" in klass.__dict__:
            descriptor = klass.__dict__["anotherName"]
            break
    assert isinstance(descriptor, property)



def test_tderived::d_is_not_abstract():
    assert not inspect.isabstract(tderived::D)


def test_tderived::d_constructor_exists():
    assert callable(tderived::D.__init__)


def test_tderived::d_constructor_args():
    sig = inspect.signature(tderived::D.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_tderived::a2_is_not_abstract():
    assert not inspect.isabstract(tderived::A2)


def test_tderived::a2_constructor_exists():
    assert callable(tderived::A2.__init__)


def test_tderived::a2_constructor_args():
    sig = inspect.signature(tderived::A2.__init__)
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
B_strategy = st.builds(
    B,
)
tderived::B2_strategy = st.builds(
    tderived::B2,
    anotherName=
        safe_text
)
tderived::D_strategy = st.builds(
    tderived::D,
)
A_strategy = st.builds(
    A,
)
tderived::A2_strategy = st.builds(
    tderived::A2,
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=tderived::B2_strategy)
@settings(max_examples=50)
def test_tderived::b2_instantiation(instance):
    assert isinstance(instance, tderived::B2)

@given(instance=tderived::B2_strategy)
def test_tderived::b2_anotherName_type(instance):
    assert isinstance(instance.anotherName, str)


@given(instance=tderived::B2_strategy)
def test_tderived::b2_anotherName_setter(instance):
    original = instance.anotherName
    instance.anotherName = original
    assert instance.anotherName == original

@given(instance=tderived::D_strategy)
@settings(max_examples=50)
def test_tderived::d_instantiation(instance):
    assert isinstance(instance, tderived::D)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=tderived::A2_strategy)
@settings(max_examples=50)
def test_tderived::a2_instantiation(instance):
    assert isinstance(instance, tderived::A2)
