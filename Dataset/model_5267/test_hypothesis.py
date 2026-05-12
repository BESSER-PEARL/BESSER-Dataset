import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    l1_B,
    l1_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_l1_b_is_not_abstract():
    assert not inspect.isabstract(l1_B)


def test_l1_b_constructor_exists():
    assert callable(l1_B.__init__)


def test_l1_b_constructor_args():
    sig = inspect.signature(l1_B.__init__)
    params = list(sig.parameters.keys())



def test_l1_a_is_not_abstract():
    assert not inspect.isabstract(l1_A)


def test_l1_a_constructor_exists():
    assert callable(l1_A.__init__)


def test_l1_a_constructor_args():
    sig = inspect.signature(l1_A.__init__)
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
l1_B_strategy = st.builds(
    l1_B,
)
l1_A_strategy = st.builds(
    l1_A,
)

@given(instance=l1_B_strategy)
@settings(max_examples=50)
def test_l1_b_instantiation(instance):
    assert isinstance(instance, l1_B)

@given(instance=l1_A_strategy)
@settings(max_examples=50)
def test_l1_a_instantiation(instance):
    assert isinstance(instance, l1_A)
