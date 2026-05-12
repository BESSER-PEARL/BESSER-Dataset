import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    C,
    B,
    diamond_D,
    A,
    diamond_C,
    diamond_B,
    diamond_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_diamond_d_is_not_abstract():
    assert not inspect.isabstract(diamond_D)


def test_diamond_d_constructor_exists():
    assert callable(diamond_D.__init__)


def test_diamond_d_constructor_args():
    sig = inspect.signature(diamond_D.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_diamond_c_is_not_abstract():
    assert not inspect.isabstract(diamond_C)


def test_diamond_c_constructor_exists():
    assert callable(diamond_C.__init__)


def test_diamond_c_constructor_args():
    sig = inspect.signature(diamond_C.__init__)
    params = list(sig.parameters.keys())



def test_diamond_b_is_not_abstract():
    assert not inspect.isabstract(diamond_B)


def test_diamond_b_constructor_exists():
    assert callable(diamond_B.__init__)


def test_diamond_b_constructor_args():
    sig = inspect.signature(diamond_B.__init__)
    params = list(sig.parameters.keys())



def test_diamond_a_is_not_abstract():
    assert not inspect.isabstract(diamond_A)


def test_diamond_a_constructor_exists():
    assert callable(diamond_A.__init__)


def test_diamond_a_constructor_args():
    sig = inspect.signature(diamond_A.__init__)
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
C_strategy = st.builds(
    C,
)
B_strategy = st.builds(
    B,
)
diamond_D_strategy = st.builds(
    diamond_D,
)
A_strategy = st.builds(
    A,
)
diamond_C_strategy = st.builds(
    diamond_C,
)
diamond_B_strategy = st.builds(
    diamond_B,
)
diamond_A_strategy = st.builds(
    diamond_A,
)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=diamond_D_strategy)
@settings(max_examples=50)
def test_diamond_d_instantiation(instance):
    assert isinstance(instance, diamond_D)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=diamond_C_strategy)
@settings(max_examples=50)
def test_diamond_c_instantiation(instance):
    assert isinstance(instance, diamond_C)

@given(instance=diamond_B_strategy)
@settings(max_examples=50)
def test_diamond_b_instantiation(instance):
    assert isinstance(instance, diamond_B)

@given(instance=diamond_A_strategy)
@settings(max_examples=50)
def test_diamond_a_instantiation(instance):
    assert isinstance(instance, diamond_A)
