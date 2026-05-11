import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    in::B,
    C,
    B,
    in::A,
    in::x::X,
    in::C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_in::b_is_not_abstract():
    assert not inspect.isabstract(in::B)


def test_in::b_constructor_exists():
    assert callable(in::B.__init__)


def test_in::b_constructor_args():
    sig = inspect.signature(in::B.__init__)
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



def test_in::a_is_not_abstract():
    assert not inspect.isabstract(in::A)


def test_in::a_constructor_exists():
    assert callable(in::A.__init__)


def test_in::a_constructor_args():
    sig = inspect.signature(in::A.__init__)
    params = list(sig.parameters.keys())



def test_in::x::x_is_not_abstract():
    assert not inspect.isabstract(in::x::X)


def test_in::x::x_constructor_exists():
    assert callable(in::x::X.__init__)


def test_in::x::x_constructor_args():
    sig = inspect.signature(in::x::X.__init__)
    params = list(sig.parameters.keys())



def test_in::c_is_not_abstract():
    assert not inspect.isabstract(in::C)


def test_in::c_constructor_exists():
    assert callable(in::C.__init__)


def test_in::c_constructor_args():
    sig = inspect.signature(in::C.__init__)
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
in::B_strategy = st.builds(
    in::B,
)
C_strategy = st.builds(
    C,
)
B_strategy = st.builds(
    B,
)
in::A_strategy = st.builds(
    in::A,
)
in::x::X_strategy = st.builds(
    in::x::X,
)
in::C_strategy = st.builds(
    in::C,
)

@given(instance=in::B_strategy)
@settings(max_examples=50)
def test_in::b_instantiation(instance):
    assert isinstance(instance, in::B)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=in::A_strategy)
@settings(max_examples=50)
def test_in::a_instantiation(instance):
    assert isinstance(instance, in::A)

@given(instance=in::x::X_strategy)
@settings(max_examples=50)
def test_in::x::x_instantiation(instance):
    assert isinstance(instance, in::x::X)

@given(instance=in::C_strategy)
@settings(max_examples=50)
def test_in::c_instantiation(instance):
    assert isinstance(instance, in::C)
