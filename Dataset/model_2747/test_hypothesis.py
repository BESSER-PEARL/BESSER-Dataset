import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testcontainment_B,
    testcontainment_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testcontainment_b_is_not_abstract():
    assert not inspect.isabstract(testcontainment_B)


def test_testcontainment_b_constructor_exists():
    assert callable(testcontainment_B.__init__)


def test_testcontainment_b_constructor_args():
    sig = inspect.signature(testcontainment_B.__init__)
    params = list(sig.parameters.keys())



def test_testcontainment_a_is_not_abstract():
    assert not inspect.isabstract(testcontainment_A)


def test_testcontainment_a_constructor_exists():
    assert callable(testcontainment_A.__init__)


def test_testcontainment_a_constructor_args():
    sig = inspect.signature(testcontainment_A.__init__)
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
testcontainment_B_strategy = st.builds(
    testcontainment_B,
)
testcontainment_A_strategy = st.builds(
    testcontainment_A,
)

@given(instance=testcontainment_B_strategy)
@settings(max_examples=50)
def test_testcontainment_b_instantiation(instance):
    assert isinstance(instance, testcontainment_B)

@given(instance=testcontainment_A_strategy)
@settings(max_examples=50)
def test_testcontainment_a_instantiation(instance):
    assert isinstance(instance, testcontainment_A)
