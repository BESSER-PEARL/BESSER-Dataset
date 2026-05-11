import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    B,
    oo::remove::empty::C,
    oo::remove::empty::B,
    oo::remove::empty::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_oo::remove::empty::c_is_not_abstract():
    assert not inspect.isabstract(oo::remove::empty::C)


def test_oo::remove::empty::c_constructor_exists():
    assert callable(oo::remove::empty::C.__init__)


def test_oo::remove::empty::c_constructor_args():
    sig = inspect.signature(oo::remove::empty::C.__init__)
    params = list(sig.parameters.keys())



def test_oo::remove::empty::b_is_not_abstract():
    assert not inspect.isabstract(oo::remove::empty::B)


def test_oo::remove::empty::b_constructor_exists():
    assert callable(oo::remove::empty::B.__init__)


def test_oo::remove::empty::b_constructor_args():
    sig = inspect.signature(oo::remove::empty::B.__init__)
    params = list(sig.parameters.keys())



def test_oo::remove::empty::a_is_not_abstract():
    assert not inspect.isabstract(oo::remove::empty::A)


def test_oo::remove::empty::a_constructor_exists():
    assert callable(oo::remove::empty::A.__init__)


def test_oo::remove::empty::a_constructor_args():
    sig = inspect.signature(oo::remove::empty::A.__init__)
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
B_strategy = st.builds(
    B,
)
oo::remove::empty::C_strategy = st.builds(
    oo::remove::empty::C,
)
oo::remove::empty::B_strategy = st.builds(
    oo::remove::empty::B,
)
oo::remove::empty::A_strategy = st.builds(
    oo::remove::empty::A,
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=oo::remove::empty::C_strategy)
@settings(max_examples=50)
def test_oo::remove::empty::c_instantiation(instance):
    assert isinstance(instance, oo::remove::empty::C)

@given(instance=oo::remove::empty::B_strategy)
@settings(max_examples=50)
def test_oo::remove::empty::b_instantiation(instance):
    assert isinstance(instance, oo::remove::empty::B)

@given(instance=oo::remove::empty::A_strategy)
@settings(max_examples=50)
def test_oo::remove::empty::a_instantiation(instance):
    assert isinstance(instance, oo::remove::empty::A)
