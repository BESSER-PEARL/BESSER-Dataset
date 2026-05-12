import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    x_B,
    x_C,
    x_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_x_b_is_not_abstract():
    assert not inspect.isabstract(x_B)


def test_x_b_constructor_exists():
    assert callable(x_B.__init__)


def test_x_b_constructor_args():
    sig = inspect.signature(x_B.__init__)
    params = list(sig.parameters.keys())



def test_x_c_is_not_abstract():
    assert not inspect.isabstract(x_C)


def test_x_c_constructor_exists():
    assert callable(x_C.__init__)


def test_x_c_constructor_args():
    sig = inspect.signature(x_C.__init__)
    params = list(sig.parameters.keys())



def test_x_a_is_not_abstract():
    assert not inspect.isabstract(x_A)


def test_x_a_constructor_exists():
    assert callable(x_A.__init__)


def test_x_a_constructor_args():
    sig = inspect.signature(x_A.__init__)
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
x_B_strategy = st.builds(
    x_B,
)
x_C_strategy = st.builds(
    x_C,
)
x_A_strategy = st.builds(
    x_A,
)

@given(instance=x_B_strategy)
@settings(max_examples=50)
def test_x_b_instantiation(instance):
    assert isinstance(instance, x_B)

@given(instance=x_C_strategy)
@settings(max_examples=50)
def test_x_c_instantiation(instance):
    assert isinstance(instance, x_C)

@given(instance=x_A_strategy)
@settings(max_examples=50)
def test_x_a_instantiation(instance):
    assert isinstance(instance, x_A)
