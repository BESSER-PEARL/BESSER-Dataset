import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    minimalref::B,
    minimalref::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_minimalref::b_is_not_abstract():
    assert not inspect.isabstract(minimalref::B)


def test_minimalref::b_constructor_exists():
    assert callable(minimalref::B.__init__)


def test_minimalref::b_constructor_args():
    sig = inspect.signature(minimalref::B.__init__)
    params = list(sig.parameters.keys())



def test_minimalref::a_is_not_abstract():
    assert not inspect.isabstract(minimalref::A)


def test_minimalref::a_constructor_exists():
    assert callable(minimalref::A.__init__)


def test_minimalref::a_constructor_args():
    sig = inspect.signature(minimalref::A.__init__)
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
minimalref::B_strategy = st.builds(
    minimalref::B,
)
minimalref::A_strategy = st.builds(
    minimalref::A,
)

@given(instance=minimalref::B_strategy)
@settings(max_examples=50)
def test_minimalref::b_instantiation(instance):
    assert isinstance(instance, minimalref::B)

@given(instance=minimalref::A_strategy)
@settings(max_examples=50)
def test_minimalref::a_instantiation(instance):
    assert isinstance(instance, minimalref::A)
