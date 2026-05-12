import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ale2_RB,
    ale2_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ale2_rb_is_not_abstract():
    assert not inspect.isabstract(ale2_RB)


def test_ale2_rb_constructor_exists():
    assert callable(ale2_RB.__init__)


def test_ale2_rb_constructor_args():
    sig = inspect.signature(ale2_RB.__init__)
    params = list(sig.parameters.keys())



def test_ale2_b_is_not_abstract():
    assert not inspect.isabstract(ale2_B)


def test_ale2_b_constructor_exists():
    assert callable(ale2_B.__init__)


def test_ale2_b_constructor_args():
    sig = inspect.signature(ale2_B.__init__)
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
ale2_RB_strategy = st.builds(
    ale2_RB,
)
ale2_B_strategy = st.builds(
    ale2_B,
)

@given(instance=ale2_RB_strategy)
@settings(max_examples=50)
def test_ale2_rb_instantiation(instance):
    assert isinstance(instance, ale2_RB)

@given(instance=ale2_B_strategy)
@settings(max_examples=50)
def test_ale2_b_instantiation(instance):
    assert isinstance(instance, ale2_B)
