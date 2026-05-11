import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    A,
    diamon::B,
    diamon::A,
    C,
    B,
    diamon::D,
    diamon::C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_diamon::b_is_not_abstract():
    assert not inspect.isabstract(diamon::B)


def test_diamon::b_constructor_exists():
    assert callable(diamon::B.__init__)


def test_diamon::b_constructor_args():
    sig = inspect.signature(diamon::B.__init__)
    params = list(sig.parameters.keys())



def test_diamon::a_is_not_abstract():
    assert not inspect.isabstract(diamon::A)


def test_diamon::a_constructor_exists():
    assert callable(diamon::A.__init__)


def test_diamon::a_constructor_args():
    sig = inspect.signature(diamon::A.__init__)
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



def test_diamon::d_is_not_abstract():
    assert not inspect.isabstract(diamon::D)


def test_diamon::d_constructor_exists():
    assert callable(diamon::D.__init__)


def test_diamon::d_constructor_args():
    sig = inspect.signature(diamon::D.__init__)
    params = list(sig.parameters.keys())



def test_diamon::c_is_not_abstract():
    assert not inspect.isabstract(diamon::C)


def test_diamon::c_constructor_exists():
    assert callable(diamon::C.__init__)


def test_diamon::c_constructor_args():
    sig = inspect.signature(diamon::C.__init__)
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
A_strategy = st.builds(
    A,
)
diamon::B_strategy = st.builds(
    diamon::B,
)
diamon::A_strategy = st.builds(
    diamon::A,
)
C_strategy = st.builds(
    C,
)
B_strategy = st.builds(
    B,
)
diamon::D_strategy = st.builds(
    diamon::D,
)
diamon::C_strategy = st.builds(
    diamon::C,
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=diamon::B_strategy)
@settings(max_examples=50)
def test_diamon::b_instantiation(instance):
    assert isinstance(instance, diamon::B)

@given(instance=diamon::A_strategy)
@settings(max_examples=50)
def test_diamon::a_instantiation(instance):
    assert isinstance(instance, diamon::A)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=diamon::D_strategy)
@settings(max_examples=50)
def test_diamon::d_instantiation(instance):
    assert isinstance(instance, diamon::D)

@given(instance=diamon::C_strategy)
@settings(max_examples=50)
def test_diamon::c_instantiation(instance):
    assert isinstance(instance, diamon::C)
