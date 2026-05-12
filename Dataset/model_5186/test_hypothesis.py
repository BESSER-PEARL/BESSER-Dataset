import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    B,
    A,
    multi_C,
    multi_B,
    multi_A,
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



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_multi_c_is_not_abstract():
    assert not inspect.isabstract(multi_C)


def test_multi_c_constructor_exists():
    assert callable(multi_C.__init__)


def test_multi_c_constructor_args():
    sig = inspect.signature(multi_C.__init__)
    params = list(sig.parameters.keys())



def test_multi_b_is_not_abstract():
    assert not inspect.isabstract(multi_B)


def test_multi_b_constructor_exists():
    assert callable(multi_B.__init__)


def test_multi_b_constructor_args():
    sig = inspect.signature(multi_B.__init__)
    params = list(sig.parameters.keys())



def test_multi_a_is_not_abstract():
    assert not inspect.isabstract(multi_A)


def test_multi_a_constructor_exists():
    assert callable(multi_A.__init__)


def test_multi_a_constructor_args():
    sig = inspect.signature(multi_A.__init__)
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
A_strategy = st.builds(
    A,
)
multi_C_strategy = st.builds(
    multi_C,
)
multi_B_strategy = st.builds(
    multi_B,
)
multi_A_strategy = st.builds(
    multi_A,
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=multi_C_strategy)
@settings(max_examples=50)
def test_multi_c_instantiation(instance):
    assert isinstance(instance, multi_C)

@given(instance=multi_B_strategy)
@settings(max_examples=50)
def test_multi_b_instantiation(instance):
    assert isinstance(instance, multi_B)

@given(instance=multi_A_strategy)
@settings(max_examples=50)
def test_multi_a_instantiation(instance):
    assert isinstance(instance, multi_A)
