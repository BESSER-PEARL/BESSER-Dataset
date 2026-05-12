import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    B,
    oo_remove_empty_C,
    oo_remove_empty_B,
    oo_remove_empty_A,
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



def test_oo_remove_empty_c_is_not_abstract():
    assert not inspect.isabstract(oo_remove_empty_C)


def test_oo_remove_empty_c_constructor_exists():
    assert callable(oo_remove_empty_C.__init__)


def test_oo_remove_empty_c_constructor_args():
    sig = inspect.signature(oo_remove_empty_C.__init__)
    params = list(sig.parameters.keys())



def test_oo_remove_empty_b_is_not_abstract():
    assert not inspect.isabstract(oo_remove_empty_B)


def test_oo_remove_empty_b_constructor_exists():
    assert callable(oo_remove_empty_B.__init__)


def test_oo_remove_empty_b_constructor_args():
    sig = inspect.signature(oo_remove_empty_B.__init__)
    params = list(sig.parameters.keys())



def test_oo_remove_empty_a_is_not_abstract():
    assert not inspect.isabstract(oo_remove_empty_A)


def test_oo_remove_empty_a_constructor_exists():
    assert callable(oo_remove_empty_A.__init__)


def test_oo_remove_empty_a_constructor_args():
    sig = inspect.signature(oo_remove_empty_A.__init__)
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
oo_remove_empty_C_strategy = st.builds(
    oo_remove_empty_C,
)
oo_remove_empty_B_strategy = st.builds(
    oo_remove_empty_B,
)
oo_remove_empty_A_strategy = st.builds(
    oo_remove_empty_A,
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=oo_remove_empty_C_strategy)
@settings(max_examples=50)
def test_oo_remove_empty_c_instantiation(instance):
    assert isinstance(instance, oo_remove_empty_C)

@given(instance=oo_remove_empty_B_strategy)
@settings(max_examples=50)
def test_oo_remove_empty_b_instantiation(instance):
    assert isinstance(instance, oo_remove_empty_B)

@given(instance=oo_remove_empty_A_strategy)
@settings(max_examples=50)
def test_oo_remove_empty_a_instantiation(instance):
    assert isinstance(instance, oo_remove_empty_A)
