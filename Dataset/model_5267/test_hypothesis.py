import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    l1::B,
    l1::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_l1::b_is_not_abstract():
    assert not inspect.isabstract(l1::B)


def test_l1::b_constructor_exists():
    assert callable(l1::B.__init__)


def test_l1::b_constructor_args():
    sig = inspect.signature(l1::B.__init__)
    params = list(sig.parameters.keys())



def test_l1::a_is_not_abstract():
    assert not inspect.isabstract(l1::A)


def test_l1::a_constructor_exists():
    assert callable(l1::A.__init__)


def test_l1::a_constructor_args():
    sig = inspect.signature(l1::A.__init__)
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
l1::B_strategy = st.builds(
    l1::B,
)
l1::A_strategy = st.builds(
    l1::A,
)

@given(instance=l1::B_strategy)
@settings(max_examples=50)
def test_l1::b_instantiation(instance):
    assert isinstance(instance, l1::B)

@given(instance=l1::A_strategy)
@settings(max_examples=50)
def test_l1::a_instantiation(instance):
    assert isinstance(instance, l1::A)
