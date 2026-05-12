import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    bug404318_B,
    bug404318_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bug404318_b_is_not_abstract():
    assert not inspect.isabstract(bug404318_B)


def test_bug404318_b_constructor_exists():
    assert callable(bug404318_B.__init__)


def test_bug404318_b_constructor_args():
    sig = inspect.signature(bug404318_B.__init__)
    params = list(sig.parameters.keys())



def test_bug404318_a_is_not_abstract():
    assert not inspect.isabstract(bug404318_A)


def test_bug404318_a_constructor_exists():
    assert callable(bug404318_A.__init__)


def test_bug404318_a_constructor_args():
    sig = inspect.signature(bug404318_A.__init__)
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
bug404318_B_strategy = st.builds(
    bug404318_B,
)
bug404318_A_strategy = st.builds(
    bug404318_A,
)

@given(instance=bug404318_B_strategy)
@settings(max_examples=50)
def test_bug404318_b_instantiation(instance):
    assert isinstance(instance, bug404318_B)

@given(instance=bug404318_A_strategy)
@settings(max_examples=50)
def test_bug404318_a_instantiation(instance):
    assert isinstance(instance, bug404318_A)
