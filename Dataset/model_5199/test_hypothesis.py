import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    abc_C,
    A,
    abc_B,
    abc_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abc_c_is_not_abstract():
    assert not inspect.isabstract(abc_C)


def test_abc_c_constructor_exists():
    assert callable(abc_C.__init__)


def test_abc_c_constructor_args():
    sig = inspect.signature(abc_C.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_abc_b_is_not_abstract():
    assert not inspect.isabstract(abc_B)


def test_abc_b_constructor_exists():
    assert callable(abc_B.__init__)


def test_abc_b_constructor_args():
    sig = inspect.signature(abc_B.__init__)
    params = list(sig.parameters.keys())



def test_abc_a_is_not_abstract():
    assert not inspect.isabstract(abc_A)


def test_abc_a_constructor_exists():
    assert callable(abc_A.__init__)


def test_abc_a_constructor_args():
    sig = inspect.signature(abc_A.__init__)
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
abc_C_strategy = st.builds(
    abc_C,
)
A_strategy = st.builds(
    A,
)
abc_B_strategy = st.builds(
    abc_B,
)
abc_A_strategy = st.builds(
    abc_A,
)

@given(instance=abc_C_strategy)
@settings(max_examples=50)
def test_abc_c_instantiation(instance):
    assert isinstance(instance, abc_C)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=abc_B_strategy)
@settings(max_examples=50)
def test_abc_b_instantiation(instance):
    assert isinstance(instance, abc_B)

@given(instance=abc_A_strategy)
@settings(max_examples=50)
def test_abc_a_instantiation(instance):
    assert isinstance(instance, abc_A)
