import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    a_B,
    a_EObject,
    a_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_b_is_not_abstract():
    assert not inspect.isabstract(a_B)


def test_a_b_constructor_exists():
    assert callable(a_B.__init__)


def test_a_b_constructor_args():
    sig = inspect.signature(a_B.__init__)
    params = list(sig.parameters.keys())



def test_a_eobject_is_not_abstract():
    assert not inspect.isabstract(a_EObject)


def test_a_eobject_constructor_exists():
    assert callable(a_EObject.__init__)


def test_a_eobject_constructor_args():
    sig = inspect.signature(a_EObject.__init__)
    params = list(sig.parameters.keys())



def test_a_a_is_not_abstract():
    assert not inspect.isabstract(a_A)


def test_a_a_constructor_exists():
    assert callable(a_A.__init__)


def test_a_a_constructor_args():
    sig = inspect.signature(a_A.__init__)
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
a_B_strategy = st.builds(
    a_B,
)
a_EObject_strategy = st.builds(
    a_EObject,
)
a_A_strategy = st.builds(
    a_A,
)

@given(instance=a_B_strategy)
@settings(max_examples=50)
def test_a_b_instantiation(instance):
    assert isinstance(instance, a_B)

@given(instance=a_EObject_strategy)
@settings(max_examples=50)
def test_a_eobject_instantiation(instance):
    assert isinstance(instance, a_EObject)

@given(instance=a_A_strategy)
@settings(max_examples=50)
def test_a_a_instantiation(instance):
    assert isinstance(instance, a_A)
