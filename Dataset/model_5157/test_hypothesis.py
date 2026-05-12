import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    minimalref_B,
    minimalref_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_minimalref_b_is_not_abstract():
    assert not inspect.isabstract(minimalref_B)


def test_minimalref_b_constructor_exists():
    assert callable(minimalref_B.__init__)


def test_minimalref_b_constructor_args():
    sig = inspect.signature(minimalref_B.__init__)
    params = list(sig.parameters.keys())



def test_minimalref_a_is_not_abstract():
    assert not inspect.isabstract(minimalref_A)


def test_minimalref_a_constructor_exists():
    assert callable(minimalref_A.__init__)


def test_minimalref_a_constructor_args():
    sig = inspect.signature(minimalref_A.__init__)
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
minimalref_B_strategy = st.builds(
    minimalref_B,
)
minimalref_A_strategy = st.builds(
    minimalref_A,
)

@given(instance=minimalref_B_strategy)
@settings(max_examples=50)
def test_minimalref_b_instantiation(instance):
    assert isinstance(instance, minimalref_B)

@given(instance=minimalref_A_strategy)
@settings(max_examples=50)
def test_minimalref_a_instantiation(instance):
    assert isinstance(instance, minimalref_A)
