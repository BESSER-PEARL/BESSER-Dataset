import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    x::B,
    x::C,
    x::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_x::b_is_not_abstract():
    assert not inspect.isabstract(x::B)


def test_x::b_constructor_exists():
    assert callable(x::B.__init__)


def test_x::b_constructor_args():
    sig = inspect.signature(x::B.__init__)
    params = list(sig.parameters.keys())



def test_x::c_is_not_abstract():
    assert not inspect.isabstract(x::C)


def test_x::c_constructor_exists():
    assert callable(x::C.__init__)


def test_x::c_constructor_args():
    sig = inspect.signature(x::C.__init__)
    params = list(sig.parameters.keys())



def test_x::a_is_not_abstract():
    assert not inspect.isabstract(x::A)


def test_x::a_constructor_exists():
    assert callable(x::A.__init__)


def test_x::a_constructor_args():
    sig = inspect.signature(x::A.__init__)
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
x::B_strategy = st.builds(
    x::B,
)
x::C_strategy = st.builds(
    x::C,
)
x::A_strategy = st.builds(
    x::A,
)

@given(instance=x::B_strategy)
@settings(max_examples=50)
def test_x::b_instantiation(instance):
    assert isinstance(instance, x::B)

@given(instance=x::C_strategy)
@settings(max_examples=50)
def test_x::c_instantiation(instance):
    assert isinstance(instance, x::C)

@given(instance=x::A_strategy)
@settings(max_examples=50)
def test_x::a_instantiation(instance):
    assert isinstance(instance, x::A)
