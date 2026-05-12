import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BBase_RootB,
    BBase_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bbase_rootb_is_not_abstract():
    assert not inspect.isabstract(BBase_RootB)


def test_bbase_rootb_constructor_exists():
    assert callable(BBase_RootB.__init__)


def test_bbase_rootb_constructor_args():
    sig = inspect.signature(BBase_RootB.__init__)
    params = list(sig.parameters.keys())



def test_bbase_b_is_not_abstract():
    assert not inspect.isabstract(BBase_B)


def test_bbase_b_constructor_exists():
    assert callable(BBase_B.__init__)


def test_bbase_b_constructor_args():
    sig = inspect.signature(BBase_B.__init__)
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
BBase_RootB_strategy = st.builds(
    BBase_RootB,
)
BBase_B_strategy = st.builds(
    BBase_B,
)

@given(instance=BBase_RootB_strategy)
@settings(max_examples=50)
def test_bbase_rootb_instantiation(instance):
    assert isinstance(instance, BBase_RootB)

@given(instance=BBase_B_strategy)
@settings(max_examples=50)
def test_bbase_b_instantiation(instance):
    assert isinstance(instance, BBase_B)
