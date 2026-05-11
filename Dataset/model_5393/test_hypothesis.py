import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    A,
    b::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_b::b_is_not_abstract():
    assert not inspect.isabstract(b::B)


def test_b::b_constructor_exists():
    assert callable(b::B.__init__)


def test_b::b_constructor_args():
    sig = inspect.signature(b::B.__init__)
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
A_strategy = st.builds(
    A,
)
b::B_strategy = st.builds(
    b::B,
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=b::B_strategy)
@settings(max_examples=50)
def test_b::b_instantiation(instance):
    assert isinstance(instance, b::B)
