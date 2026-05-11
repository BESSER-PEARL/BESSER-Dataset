import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dispatchroot::C,
    A,
    dispatchroot::B,
    dispatchroot::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dispatchroot::c_is_not_abstract():
    assert not inspect.isabstract(dispatchroot::C)


def test_dispatchroot::c_constructor_exists():
    assert callable(dispatchroot::C.__init__)


def test_dispatchroot::c_constructor_args():
    sig = inspect.signature(dispatchroot::C.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_dispatchroot::b_is_not_abstract():
    assert not inspect.isabstract(dispatchroot::B)


def test_dispatchroot::b_constructor_exists():
    assert callable(dispatchroot::B.__init__)


def test_dispatchroot::b_constructor_args():
    sig = inspect.signature(dispatchroot::B.__init__)
    params = list(sig.parameters.keys())



def test_dispatchroot::a_is_not_abstract():
    assert not inspect.isabstract(dispatchroot::A)


def test_dispatchroot::a_constructor_exists():
    assert callable(dispatchroot::A.__init__)


def test_dispatchroot::a_constructor_args():
    sig = inspect.signature(dispatchroot::A.__init__)
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
dispatchroot::C_strategy = st.builds(
    dispatchroot::C,
)
A_strategy = st.builds(
    A,
)
dispatchroot::B_strategy = st.builds(
    dispatchroot::B,
)
dispatchroot::A_strategy = st.builds(
    dispatchroot::A,
)

@given(instance=dispatchroot::C_strategy)
@settings(max_examples=50)
def test_dispatchroot::c_instantiation(instance):
    assert isinstance(instance, dispatchroot::C)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=dispatchroot::B_strategy)
@settings(max_examples=50)
def test_dispatchroot::b_instantiation(instance):
    assert isinstance(instance, dispatchroot::B)

@given(instance=dispatchroot::A_strategy)
@settings(max_examples=50)
def test_dispatchroot::a_instantiation(instance):
    assert isinstance(instance, dispatchroot::A)
