import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    d::D,
    d::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_d::d_is_not_abstract():
    assert not inspect.isabstract(d::D)


def test_d::d_constructor_exists():
    assert callable(d::D.__init__)


def test_d::d_constructor_args():
    sig = inspect.signature(d::D.__init__)
    params = list(sig.parameters.keys())



def test_d::b_is_not_abstract():
    assert not inspect.isabstract(d::B)


def test_d::b_constructor_exists():
    assert callable(d::B.__init__)


def test_d::b_constructor_args():
    sig = inspect.signature(d::B.__init__)
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
d::D_strategy = st.builds(
    d::D,
)
d::B_strategy = st.builds(
    d::B,
)

@given(instance=d::D_strategy)
@settings(max_examples=50)
def test_d::d_instantiation(instance):
    assert isinstance(instance, d::D)

@given(instance=d::B_strategy)
@settings(max_examples=50)
def test_d::b_instantiation(instance):
    assert isinstance(instance, d::B)
