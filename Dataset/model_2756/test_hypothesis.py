import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BAttributes::Y,
    BAttributes::RootB,
    BAttributes::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_battributes::y_is_not_abstract():
    assert not inspect.isabstract(BAttributes::Y)


def test_battributes::y_constructor_exists():
    assert callable(BAttributes::Y.__init__)


def test_battributes::y_constructor_args():
    sig = inspect.signature(BAttributes::Y.__init__)
    params = list(sig.parameters.keys())



def test_battributes::rootb_is_not_abstract():
    assert not inspect.isabstract(BAttributes::RootB)


def test_battributes::rootb_constructor_exists():
    assert callable(BAttributes::RootB.__init__)


def test_battributes::rootb_constructor_args():
    sig = inspect.signature(BAttributes::RootB.__init__)
    params = list(sig.parameters.keys())



def test_battributes::b_is_not_abstract():
    assert not inspect.isabstract(BAttributes::B)


def test_battributes::b_constructor_exists():
    assert callable(BAttributes::B.__init__)


def test_battributes::b_constructor_args():
    sig = inspect.signature(BAttributes::B.__init__)
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
BAttributes::Y_strategy = st.builds(
    BAttributes::Y,
)
BAttributes::RootB_strategy = st.builds(
    BAttributes::RootB,
)
BAttributes::B_strategy = st.builds(
    BAttributes::B,
)

@given(instance=BAttributes::Y_strategy)
@settings(max_examples=50)
def test_battributes::y_instantiation(instance):
    assert isinstance(instance, BAttributes::Y)

@given(instance=BAttributes::RootB_strategy)
@settings(max_examples=50)
def test_battributes::rootb_instantiation(instance):
    assert isinstance(instance, BAttributes::RootB)

@given(instance=BAttributes::B_strategy)
@settings(max_examples=50)
def test_battributes::b_instantiation(instance):
    assert isinstance(instance, BAttributes::B)
