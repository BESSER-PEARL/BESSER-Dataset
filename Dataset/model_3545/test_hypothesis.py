import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    C,
    B,
    diamond::D,
    A,
    diamond::C,
    diamond::B,
    diamond::A,
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



def test_diamond::d_is_not_abstract():
    assert not inspect.isabstract(diamond::D)


def test_diamond::d_constructor_exists():
    assert callable(diamond::D.__init__)


def test_diamond::d_constructor_args():
    sig = inspect.signature(diamond::D.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_diamond::c_is_not_abstract():
    assert not inspect.isabstract(diamond::C)


def test_diamond::c_constructor_exists():
    assert callable(diamond::C.__init__)


def test_diamond::c_constructor_args():
    sig = inspect.signature(diamond::C.__init__)
    params = list(sig.parameters.keys())



def test_diamond::b_is_not_abstract():
    assert not inspect.isabstract(diamond::B)


def test_diamond::b_constructor_exists():
    assert callable(diamond::B.__init__)


def test_diamond::b_constructor_args():
    sig = inspect.signature(diamond::B.__init__)
    params = list(sig.parameters.keys())



def test_diamond::a_is_not_abstract():
    assert not inspect.isabstract(diamond::A)


def test_diamond::a_constructor_exists():
    assert callable(diamond::A.__init__)


def test_diamond::a_constructor_args():
    sig = inspect.signature(diamond::A.__init__)
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
diamond::D_strategy = st.builds(
    diamond::D,
)
A_strategy = st.builds(
    A,
)
diamond::C_strategy = st.builds(
    diamond::C,
)
diamond::B_strategy = st.builds(
    diamond::B,
)
diamond::A_strategy = st.builds(
    diamond::A,
)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=diamond::D_strategy)
@settings(max_examples=50)
def test_diamond::d_instantiation(instance):
    assert isinstance(instance, diamond::D)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=diamond::C_strategy)
@settings(max_examples=50)
def test_diamond::c_instantiation(instance):
    assert isinstance(instance, diamond::C)

@given(instance=diamond::B_strategy)
@settings(max_examples=50)
def test_diamond::b_instantiation(instance):
    assert isinstance(instance, diamond::B)

@given(instance=diamond::A_strategy)
@settings(max_examples=50)
def test_diamond::a_instantiation(instance):
    assert isinstance(instance, diamond::A)
