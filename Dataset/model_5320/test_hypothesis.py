import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    root::B,
    root::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root::b_is_not_abstract():
    assert not inspect.isabstract(root::B)


def test_root::b_constructor_exists():
    assert callable(root::B.__init__)


def test_root::b_constructor_args():
    sig = inspect.signature(root::B.__init__)
    params = list(sig.parameters.keys())



def test_root::a_is_not_abstract():
    assert not inspect.isabstract(root::A)


def test_root::a_constructor_exists():
    assert callable(root::A.__init__)


def test_root::a_constructor_args():
    sig = inspect.signature(root::A.__init__)
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
root::B_strategy = st.builds(
    root::B,
)
root::A_strategy = st.builds(
    root::A,
)

@given(instance=root::B_strategy)
@settings(max_examples=50)
def test_root::b_instantiation(instance):
    assert isinstance(instance, root::B)

@given(instance=root::A_strategy)
@settings(max_examples=50)
def test_root::a_instantiation(instance):
    assert isinstance(instance, root::A)
