import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testcontainment::B,
    testcontainment::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testcontainment::b_is_not_abstract():
    assert not inspect.isabstract(testcontainment::B)


def test_testcontainment::b_constructor_exists():
    assert callable(testcontainment::B.__init__)


def test_testcontainment::b_constructor_args():
    sig = inspect.signature(testcontainment::B.__init__)
    params = list(sig.parameters.keys())



def test_testcontainment::a_is_not_abstract():
    assert not inspect.isabstract(testcontainment::A)


def test_testcontainment::a_constructor_exists():
    assert callable(testcontainment::A.__init__)


def test_testcontainment::a_constructor_args():
    sig = inspect.signature(testcontainment::A.__init__)
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
testcontainment::B_strategy = st.builds(
    testcontainment::B,
)
testcontainment::A_strategy = st.builds(
    testcontainment::A,
)

@given(instance=testcontainment::B_strategy)
@settings(max_examples=50)
def test_testcontainment::b_instantiation(instance):
    assert isinstance(instance, testcontainment::B)

@given(instance=testcontainment::A_strategy)
@settings(max_examples=50)
def test_testcontainment::a_instantiation(instance):
    assert isinstance(instance, testcontainment::A)
