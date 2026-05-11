import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    b::B2,
    b::B1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b::b2_is_not_abstract():
    assert not inspect.isabstract(b::B2)


def test_b::b2_constructor_exists():
    assert callable(b::B2.__init__)


def test_b::b2_constructor_args():
    sig = inspect.signature(b::B2.__init__)
    params = list(sig.parameters.keys())



def test_b::b1_is_not_abstract():
    assert not inspect.isabstract(b::B1)


def test_b::b1_constructor_exists():
    assert callable(b::B1.__init__)


def test_b::b1_constructor_args():
    sig = inspect.signature(b::B1.__init__)
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
b::B2_strategy = st.builds(
    b::B2,
)
b::B1_strategy = st.builds(
    b::B1,
)

@given(instance=b::B2_strategy)
@settings(max_examples=50)
def test_b::b2_instantiation(instance):
    assert isinstance(instance, b::B2)

@given(instance=b::B1_strategy)
@settings(max_examples=50)
def test_b::b1_instantiation(instance):
    assert isinstance(instance, b::B1)
