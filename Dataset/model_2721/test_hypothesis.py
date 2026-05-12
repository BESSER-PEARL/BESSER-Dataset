import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    b_C,
    b_A,
    b_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b_c_is_not_abstract():
    assert not inspect.isabstract(b_C)


def test_b_c_constructor_exists():
    assert callable(b_C.__init__)


def test_b_c_constructor_args():
    sig = inspect.signature(b_C.__init__)
    params = list(sig.parameters.keys())



def test_b_a_is_not_abstract():
    assert not inspect.isabstract(b_A)


def test_b_a_constructor_exists():
    assert callable(b_A.__init__)


def test_b_a_constructor_args():
    sig = inspect.signature(b_A.__init__)
    params = list(sig.parameters.keys())



def test_b_b_is_not_abstract():
    assert not inspect.isabstract(b_B)


def test_b_b_constructor_exists():
    assert callable(b_B.__init__)


def test_b_b_constructor_args():
    sig = inspect.signature(b_B.__init__)
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
b_C_strategy = st.builds(
    b_C,
)
b_A_strategy = st.builds(
    b_A,
)
b_B_strategy = st.builds(
    b_B,
)

@given(instance=b_C_strategy)
@settings(max_examples=50)
def test_b_c_instantiation(instance):
    assert isinstance(instance, b_C)

@given(instance=b_A_strategy)
@settings(max_examples=50)
def test_b_a_instantiation(instance):
    assert isinstance(instance, b_A)

@given(instance=b_B_strategy)
@settings(max_examples=50)
def test_b_b_instantiation(instance):
    assert isinstance(instance, b_B)
