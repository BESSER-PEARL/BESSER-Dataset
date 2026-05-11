import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BKeys::Y,
    BKeys::RootB,
    BKeys::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bkeys::y_is_not_abstract():
    assert not inspect.isabstract(BKeys::Y)


def test_bkeys::y_constructor_exists():
    assert callable(BKeys::Y.__init__)


def test_bkeys::y_constructor_args():
    sig = inspect.signature(BKeys::Y.__init__)
    params = list(sig.parameters.keys())



def test_bkeys::rootb_is_not_abstract():
    assert not inspect.isabstract(BKeys::RootB)


def test_bkeys::rootb_constructor_exists():
    assert callable(BKeys::RootB.__init__)


def test_bkeys::rootb_constructor_args():
    sig = inspect.signature(BKeys::RootB.__init__)
    params = list(sig.parameters.keys())



def test_bkeys::b_is_not_abstract():
    assert not inspect.isabstract(BKeys::B)


def test_bkeys::b_constructor_exists():
    assert callable(BKeys::B.__init__)


def test_bkeys::b_constructor_args():
    sig = inspect.signature(BKeys::B.__init__)
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
BKeys::Y_strategy = st.builds(
    BKeys::Y,
)
BKeys::RootB_strategy = st.builds(
    BKeys::RootB,
)
BKeys::B_strategy = st.builds(
    BKeys::B,
)

@given(instance=BKeys::Y_strategy)
@settings(max_examples=50)
def test_bkeys::y_instantiation(instance):
    assert isinstance(instance, BKeys::Y)

@given(instance=BKeys::RootB_strategy)
@settings(max_examples=50)
def test_bkeys::rootb_instantiation(instance):
    assert isinstance(instance, BKeys::RootB)

@given(instance=BKeys::B_strategy)
@settings(max_examples=50)
def test_bkeys::b_instantiation(instance):
    assert isinstance(instance, BKeys::B)
