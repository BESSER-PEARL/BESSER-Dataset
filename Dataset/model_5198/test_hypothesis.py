import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dispatchroot_C,
    A,
    dispatchroot_B,
    dispatchroot_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dispatchroot_c_is_not_abstract():
    assert not inspect.isabstract(dispatchroot_C)


def test_dispatchroot_c_constructor_exists():
    assert callable(dispatchroot_C.__init__)


def test_dispatchroot_c_constructor_args():
    sig = inspect.signature(dispatchroot_C.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_dispatchroot_b_is_not_abstract():
    assert not inspect.isabstract(dispatchroot_B)


def test_dispatchroot_b_constructor_exists():
    assert callable(dispatchroot_B.__init__)


def test_dispatchroot_b_constructor_args():
    sig = inspect.signature(dispatchroot_B.__init__)
    params = list(sig.parameters.keys())



def test_dispatchroot_a_is_not_abstract():
    assert not inspect.isabstract(dispatchroot_A)


def test_dispatchroot_a_constructor_exists():
    assert callable(dispatchroot_A.__init__)


def test_dispatchroot_a_constructor_args():
    sig = inspect.signature(dispatchroot_A.__init__)
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
dispatchroot_C_strategy = st.builds(
    dispatchroot_C,
)
A_strategy = st.builds(
    A,
)
dispatchroot_B_strategy = st.builds(
    dispatchroot_B,
)
dispatchroot_A_strategy = st.builds(
    dispatchroot_A,
)

@given(instance=dispatchroot_C_strategy)
@settings(max_examples=50)
def test_dispatchroot_c_instantiation(instance):
    assert isinstance(instance, dispatchroot_C)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=dispatchroot_B_strategy)
@settings(max_examples=50)
def test_dispatchroot_b_instantiation(instance):
    assert isinstance(instance, dispatchroot_B)

@given(instance=dispatchroot_A_strategy)
@settings(max_examples=50)
def test_dispatchroot_a_instantiation(instance):
    assert isinstance(instance, dispatchroot_A)
