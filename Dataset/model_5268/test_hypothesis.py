import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    bug404318::B,
    bug404318::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bug404318::b_is_not_abstract():
    assert not inspect.isabstract(bug404318::B)


def test_bug404318::b_constructor_exists():
    assert callable(bug404318::B.__init__)


def test_bug404318::b_constructor_args():
    sig = inspect.signature(bug404318::B.__init__)
    params = list(sig.parameters.keys())



def test_bug404318::a_is_not_abstract():
    assert not inspect.isabstract(bug404318::A)


def test_bug404318::a_constructor_exists():
    assert callable(bug404318::A.__init__)


def test_bug404318::a_constructor_args():
    sig = inspect.signature(bug404318::A.__init__)
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
bug404318::B_strategy = st.builds(
    bug404318::B,
)
bug404318::A_strategy = st.builds(
    bug404318::A,
)

@given(instance=bug404318::B_strategy)
@settings(max_examples=50)
def test_bug404318::b_instantiation(instance):
    assert isinstance(instance, bug404318::B)

@given(instance=bug404318::A_strategy)
@settings(max_examples=50)
def test_bug404318::a_instantiation(instance):
    assert isinstance(instance, bug404318::A)
