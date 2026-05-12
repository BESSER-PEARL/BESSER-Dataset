import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BKeys_Y,
    BKeys_RootB,
    BKeys_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bkeys_y_is_not_abstract():
    assert not inspect.isabstract(BKeys_Y)


def test_bkeys_y_constructor_exists():
    assert callable(BKeys_Y.__init__)


def test_bkeys_y_constructor_args():
    sig = inspect.signature(BKeys_Y.__init__)
    params = list(sig.parameters.keys())



def test_bkeys_rootb_is_not_abstract():
    assert not inspect.isabstract(BKeys_RootB)


def test_bkeys_rootb_constructor_exists():
    assert callable(BKeys_RootB.__init__)


def test_bkeys_rootb_constructor_args():
    sig = inspect.signature(BKeys_RootB.__init__)
    params = list(sig.parameters.keys())



def test_bkeys_b_is_not_abstract():
    assert not inspect.isabstract(BKeys_B)


def test_bkeys_b_constructor_exists():
    assert callable(BKeys_B.__init__)


def test_bkeys_b_constructor_args():
    sig = inspect.signature(BKeys_B.__init__)
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
BKeys_Y_strategy = st.builds(
    BKeys_Y,
)
BKeys_RootB_strategy = st.builds(
    BKeys_RootB,
)
BKeys_B_strategy = st.builds(
    BKeys_B,
)

@given(instance=BKeys_Y_strategy)
@settings(max_examples=50)
def test_bkeys_y_instantiation(instance):
    assert isinstance(instance, BKeys_Y)

@given(instance=BKeys_RootB_strategy)
@settings(max_examples=50)
def test_bkeys_rootb_instantiation(instance):
    assert isinstance(instance, BKeys_RootB)

@given(instance=BKeys_B_strategy)
@settings(max_examples=50)
def test_bkeys_b_instantiation(instance):
    assert isinstance(instance, BKeys_B)
