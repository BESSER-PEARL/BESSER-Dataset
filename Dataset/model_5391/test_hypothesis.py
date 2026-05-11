import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ale2::RB,
    ale2::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ale2::rb_is_not_abstract():
    assert not inspect.isabstract(ale2::RB)


def test_ale2::rb_constructor_exists():
    assert callable(ale2::RB.__init__)


def test_ale2::rb_constructor_args():
    sig = inspect.signature(ale2::RB.__init__)
    params = list(sig.parameters.keys())



def test_ale2::b_is_not_abstract():
    assert not inspect.isabstract(ale2::B)


def test_ale2::b_constructor_exists():
    assert callable(ale2::B.__init__)


def test_ale2::b_constructor_args():
    sig = inspect.signature(ale2::B.__init__)
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
ale2::RB_strategy = st.builds(
    ale2::RB,
)
ale2::B_strategy = st.builds(
    ale2::B,
)

@given(instance=ale2::RB_strategy)
@settings(max_examples=50)
def test_ale2::rb_instantiation(instance):
    assert isinstance(instance, ale2::RB)

@given(instance=ale2::B_strategy)
@settings(max_examples=50)
def test_ale2::b_instantiation(instance):
    assert isinstance(instance, ale2::B)
