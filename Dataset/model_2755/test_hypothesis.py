import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BAttributes_Y,
    BAttributes_RootB,
    BAttributes_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_battributes_y_is_not_abstract():
    assert not inspect.isabstract(BAttributes_Y)


def test_battributes_y_constructor_exists():
    assert callable(BAttributes_Y.__init__)


def test_battributes_y_constructor_args():
    sig = inspect.signature(BAttributes_Y.__init__)
    params = list(sig.parameters.keys())



def test_battributes_rootb_is_not_abstract():
    assert not inspect.isabstract(BAttributes_RootB)


def test_battributes_rootb_constructor_exists():
    assert callable(BAttributes_RootB.__init__)


def test_battributes_rootb_constructor_args():
    sig = inspect.signature(BAttributes_RootB.__init__)
    params = list(sig.parameters.keys())



def test_battributes_b_is_not_abstract():
    assert not inspect.isabstract(BAttributes_B)


def test_battributes_b_constructor_exists():
    assert callable(BAttributes_B.__init__)


def test_battributes_b_constructor_args():
    sig = inspect.signature(BAttributes_B.__init__)
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
BAttributes_Y_strategy = st.builds(
    BAttributes_Y,
)
BAttributes_RootB_strategy = st.builds(
    BAttributes_RootB,
)
BAttributes_B_strategy = st.builds(
    BAttributes_B,
)

@given(instance=BAttributes_Y_strategy)
@settings(max_examples=50)
def test_battributes_y_instantiation(instance):
    assert isinstance(instance, BAttributes_Y)

@given(instance=BAttributes_RootB_strategy)
@settings(max_examples=50)
def test_battributes_rootb_instantiation(instance):
    assert isinstance(instance, BAttributes_RootB)

@given(instance=BAttributes_B_strategy)
@settings(max_examples=50)
def test_battributes_b_instantiation(instance):
    assert isinstance(instance, BAttributes_B)
