import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    b::A,
    b::B,
    b::C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b::a_is_not_abstract():
    assert not inspect.isabstract(b::A)


def test_b::a_constructor_exists():
    assert callable(b::A.__init__)


def test_b::a_constructor_args():
    sig = inspect.signature(b::A.__init__)
    params = list(sig.parameters.keys())



def test_b::b_is_not_abstract():
    assert not inspect.isabstract(b::B)


def test_b::b_constructor_exists():
    assert callable(b::B.__init__)


def test_b::b_constructor_args():
    sig = inspect.signature(b::B.__init__)
    params = list(sig.parameters.keys())



def test_b::c_is_not_abstract():
    assert not inspect.isabstract(b::C)


def test_b::c_constructor_exists():
    assert callable(b::C.__init__)


def test_b::c_constructor_args():
    sig = inspect.signature(b::C.__init__)
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
b::A_strategy = st.builds(
    b::A,
)
b::B_strategy = st.builds(
    b::B,
)
b::C_strategy = st.builds(
    b::C,
)

@given(instance=b::A_strategy)
@settings(max_examples=50)
def test_b::a_instantiation(instance):
    assert isinstance(instance, b::A)

@given(instance=b::B_strategy)
@settings(max_examples=50)
def test_b::b_instantiation(instance):
    assert isinstance(instance, b::B)

@given(instance=b::C_strategy)
@settings(max_examples=50)
def test_b::c_instantiation(instance):
    assert isinstance(instance, b::C)
