import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    in_B,
    C,
    B,
    in_A,
    in_x_X,
    in_C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_in_b_is_not_abstract():
    assert not inspect.isabstract(in_B)


def test_in_b_constructor_exists():
    assert callable(in_B.__init__)


def test_in_b_constructor_args():
    sig = inspect.signature(in_B.__init__)
    params = list(sig.parameters.keys())



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



def test_in_a_is_not_abstract():
    assert not inspect.isabstract(in_A)


def test_in_a_constructor_exists():
    assert callable(in_A.__init__)


def test_in_a_constructor_args():
    sig = inspect.signature(in_A.__init__)
    params = list(sig.parameters.keys())



def test_in_x_x_is_not_abstract():
    assert not inspect.isabstract(in_x_X)


def test_in_x_x_constructor_exists():
    assert callable(in_x_X.__init__)


def test_in_x_x_constructor_args():
    sig = inspect.signature(in_x_X.__init__)
    params = list(sig.parameters.keys())



def test_in_c_is_not_abstract():
    assert not inspect.isabstract(in_C)


def test_in_c_constructor_exists():
    assert callable(in_C.__init__)


def test_in_c_constructor_args():
    sig = inspect.signature(in_C.__init__)
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
in_B_strategy = st.builds(
    in_B,
)
C_strategy = st.builds(
    C,
)
B_strategy = st.builds(
    B,
)
in_A_strategy = st.builds(
    in_A,
)
in_x_X_strategy = st.builds(
    in_x_X,
)
in_C_strategy = st.builds(
    in_C,
)

@given(instance=in_B_strategy)
@settings(max_examples=50)
def test_in_b_instantiation(instance):
    assert isinstance(instance, in_B)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=in_A_strategy)
@settings(max_examples=50)
def test_in_a_instantiation(instance):
    assert isinstance(instance, in_A)

@given(instance=in_x_X_strategy)
@settings(max_examples=50)
def test_in_x_x_instantiation(instance):
    assert isinstance(instance, in_x_X)

@given(instance=in_C_strategy)
@settings(max_examples=50)
def test_in_c_instantiation(instance):
    assert isinstance(instance, in_C)
