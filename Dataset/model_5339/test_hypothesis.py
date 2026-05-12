import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    b_B1,
    b_B2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b_b1_is_not_abstract():
    assert not inspect.isabstract(b_B1)


def test_b_b1_constructor_exists():
    assert callable(b_B1.__init__)


def test_b_b1_constructor_args():
    sig = inspect.signature(b_B1.__init__)
    params = list(sig.parameters.keys())



def test_b_b2_is_not_abstract():
    assert not inspect.isabstract(b_B2)


def test_b_b2_constructor_exists():
    assert callable(b_B2.__init__)


def test_b_b2_constructor_args():
    sig = inspect.signature(b_B2.__init__)
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
b_B1_strategy = st.builds(
    b_B1,
)
b_B2_strategy = st.builds(
    b_B2,
)

@given(instance=b_B1_strategy)
@settings(max_examples=50)
def test_b_b1_instantiation(instance):
    assert isinstance(instance, b_B1)

@given(instance=b_B2_strategy)
@settings(max_examples=50)
def test_b_b2_instantiation(instance):
    assert isinstance(instance, b_B2)
