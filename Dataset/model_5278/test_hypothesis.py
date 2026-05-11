import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    a::B,
    a::EObject,
    a::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a::b_is_not_abstract():
    assert not inspect.isabstract(a::B)


def test_a::b_constructor_exists():
    assert callable(a::B.__init__)


def test_a::b_constructor_args():
    sig = inspect.signature(a::B.__init__)
    params = list(sig.parameters.keys())



def test_a::eobject_is_not_abstract():
    assert not inspect.isabstract(a::EObject)


def test_a::eobject_constructor_exists():
    assert callable(a::EObject.__init__)


def test_a::eobject_constructor_args():
    sig = inspect.signature(a::EObject.__init__)
    params = list(sig.parameters.keys())



def test_a::a_is_not_abstract():
    assert not inspect.isabstract(a::A)


def test_a::a_constructor_exists():
    assert callable(a::A.__init__)


def test_a::a_constructor_args():
    sig = inspect.signature(a::A.__init__)
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
a::B_strategy = st.builds(
    a::B,
)
a::EObject_strategy = st.builds(
    a::EObject,
)
a::A_strategy = st.builds(
    a::A,
)

@given(instance=a::B_strategy)
@settings(max_examples=50)
def test_a::b_instantiation(instance):
    assert isinstance(instance, a::B)

@given(instance=a::EObject_strategy)
@settings(max_examples=50)
def test_a::eobject_instantiation(instance):
    assert isinstance(instance, a::EObject)

@given(instance=a::A_strategy)
@settings(max_examples=50)
def test_a::a_instantiation(instance):
    assert isinstance(instance, a::A)
