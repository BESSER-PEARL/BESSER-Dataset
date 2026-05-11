import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    p::B,
    p::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_p::b_is_not_abstract():
    assert not inspect.isabstract(p::B)


def test_p::b_constructor_exists():
    assert callable(p::B.__init__)


def test_p::b_constructor_args():
    sig = inspect.signature(p::B.__init__)
    params = list(sig.parameters.keys())



def test_p::a_is_not_abstract():
    assert not inspect.isabstract(p::A)


def test_p::a_constructor_exists():
    assert callable(p::A.__init__)


def test_p::a_constructor_args():
    sig = inspect.signature(p::A.__init__)
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
p::B_strategy = st.builds(
    p::B,
)
p::A_strategy = st.builds(
    p::A,
)

@given(instance=p::B_strategy)
@settings(max_examples=50)
def test_p::b_instantiation(instance):
    assert isinstance(instance, p::B)

@given(instance=p::A_strategy)
@settings(max_examples=50)
def test_p::a_instantiation(instance):
    assert isinstance(instance, p::A)
