import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    diamon_A,
    C,
    B,
    diamon_D,
    A,
    diamon_C,
    diamon_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_diamon_a_is_not_abstract():
    assert not inspect.isabstract(diamon_A)


def test_diamon_a_constructor_exists():
    assert callable(diamon_A.__init__)


def test_diamon_a_constructor_args():
    sig = inspect.signature(diamon_A.__init__)
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



def test_diamon_d_is_not_abstract():
    assert not inspect.isabstract(diamon_D)


def test_diamon_d_constructor_exists():
    assert callable(diamon_D.__init__)


def test_diamon_d_constructor_args():
    sig = inspect.signature(diamon_D.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_diamon_c_is_not_abstract():
    assert not inspect.isabstract(diamon_C)


def test_diamon_c_constructor_exists():
    assert callable(diamon_C.__init__)


def test_diamon_c_constructor_args():
    sig = inspect.signature(diamon_C.__init__)
    params = list(sig.parameters.keys())



def test_diamon_b_is_not_abstract():
    assert not inspect.isabstract(diamon_B)


def test_diamon_b_constructor_exists():
    assert callable(diamon_B.__init__)


def test_diamon_b_constructor_args():
    sig = inspect.signature(diamon_B.__init__)
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
diamon_A_strategy = st.builds(
    diamon_A,
)
C_strategy = st.builds(
    C,
)
B_strategy = st.builds(
    B,
)
diamon_D_strategy = st.builds(
    diamon_D,
)
A_strategy = st.builds(
    A,
)
diamon_C_strategy = st.builds(
    diamon_C,
)
diamon_B_strategy = st.builds(
    diamon_B,
)

@given(instance=diamon_A_strategy)
@settings(max_examples=50)
def test_diamon_a_instantiation(instance):
    assert isinstance(instance, diamon_A)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=diamon_D_strategy)
@settings(max_examples=50)
def test_diamon_d_instantiation(instance):
    assert isinstance(instance, diamon_D)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=diamon_C_strategy)
@settings(max_examples=50)
def test_diamon_c_instantiation(instance):
    assert isinstance(instance, diamon_C)

@given(instance=diamon_B_strategy)
@settings(max_examples=50)
def test_diamon_b_instantiation(instance):
    assert isinstance(instance, diamon_B)
