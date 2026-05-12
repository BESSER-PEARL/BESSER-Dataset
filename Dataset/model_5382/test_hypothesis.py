import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    p_B,
    B,
    p_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_p_b_is_not_abstract():
    assert not inspect.isabstract(p_B)


def test_p_b_constructor_exists():
    assert callable(p_B.__init__)


def test_p_b_constructor_args():
    sig = inspect.signature(p_B.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_p_a_is_not_abstract():
    assert not inspect.isabstract(p_A)


def test_p_a_constructor_exists():
    assert callable(p_A.__init__)


def test_p_a_constructor_args():
    sig = inspect.signature(p_A.__init__)
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
p_B_strategy = st.builds(
    p_B,
)
B_strategy = st.builds(
    B,
)
p_A_strategy = st.builds(
    p_A,
)

@given(instance=p_B_strategy)
@settings(max_examples=50)
def test_p_b_instantiation(instance):
    assert isinstance(instance, p_B)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=p_A_strategy)
@settings(max_examples=50)
def test_p_a_instantiation(instance):
    assert isinstance(instance, p_A)
