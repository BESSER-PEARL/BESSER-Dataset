import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    A_E,
    A_D,
    A_C,
    A_B,
    A_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_e_is_not_abstract():
    assert not inspect.isabstract(A_E)


def test_a_e_constructor_exists():
    assert callable(A_E.__init__)


def test_a_e_constructor_args():
    sig = inspect.signature(A_E.__init__)
    params = list(sig.parameters.keys())



def test_a_d_is_not_abstract():
    assert not inspect.isabstract(A_D)


def test_a_d_constructor_exists():
    assert callable(A_D.__init__)


def test_a_d_constructor_args():
    sig = inspect.signature(A_D.__init__)
    params = list(sig.parameters.keys())



def test_a_c_is_not_abstract():
    assert not inspect.isabstract(A_C)


def test_a_c_constructor_exists():
    assert callable(A_C.__init__)


def test_a_c_constructor_args():
    sig = inspect.signature(A_C.__init__)
    params = list(sig.parameters.keys())



def test_a_b_is_not_abstract():
    assert not inspect.isabstract(A_B)


def test_a_b_constructor_exists():
    assert callable(A_B.__init__)


def test_a_b_constructor_args():
    sig = inspect.signature(A_B.__init__)
    params = list(sig.parameters.keys())



def test_a_a_is_not_abstract():
    assert not inspect.isabstract(A_A)


def test_a_a_constructor_exists():
    assert callable(A_A.__init__)


def test_a_a_constructor_args():
    sig = inspect.signature(A_A.__init__)
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
A_E_strategy = st.builds(
    A_E,
)
A_D_strategy = st.builds(
    A_D,
)
A_C_strategy = st.builds(
    A_C,
)
A_B_strategy = st.builds(
    A_B,
)
A_A_strategy = st.builds(
    A_A,
)

@given(instance=A_E_strategy)
@settings(max_examples=50)
def test_a_e_instantiation(instance):
    assert isinstance(instance, A_E)

@given(instance=A_D_strategy)
@settings(max_examples=50)
def test_a_d_instantiation(instance):
    assert isinstance(instance, A_D)

@given(instance=A_C_strategy)
@settings(max_examples=50)
def test_a_c_instantiation(instance):
    assert isinstance(instance, A_C)

@given(instance=A_B_strategy)
@settings(max_examples=50)
def test_a_b_instantiation(instance):
    assert isinstance(instance, A_B)

@given(instance=A_A_strategy)
@settings(max_examples=50)
def test_a_a_instantiation(instance):
    assert isinstance(instance, A_A)
