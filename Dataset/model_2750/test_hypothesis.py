import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BBase::RootB,
    BBase::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bbase::rootb_is_not_abstract():
    assert not inspect.isabstract(BBase::RootB)


def test_bbase::rootb_constructor_exists():
    assert callable(BBase::RootB.__init__)


def test_bbase::rootb_constructor_args():
    sig = inspect.signature(BBase::RootB.__init__)
    params = list(sig.parameters.keys())



def test_bbase::b_is_not_abstract():
    assert not inspect.isabstract(BBase::B)


def test_bbase::b_constructor_exists():
    assert callable(BBase::B.__init__)


def test_bbase::b_constructor_args():
    sig = inspect.signature(BBase::B.__init__)
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
BBase::RootB_strategy = st.builds(
    BBase::RootB,
)
BBase::B_strategy = st.builds(
    BBase::B,
)

@given(instance=BBase::RootB_strategy)
@settings(max_examples=50)
def test_bbase::rootb_instantiation(instance):
    assert isinstance(instance, BBase::RootB)

@given(instance=BBase::B_strategy)
@settings(max_examples=50)
def test_bbase::b_instantiation(instance):
    assert isinstance(instance, BBase::B)
