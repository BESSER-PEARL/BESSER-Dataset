import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    A::E,
    A::D,
    A::C,
    A::B,
    A::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a::e_is_not_abstract():
    assert not inspect.isabstract(A::E)


def test_a::e_constructor_exists():
    assert callable(A::E.__init__)


def test_a::e_constructor_args():
    sig = inspect.signature(A::E.__init__)
    params = list(sig.parameters.keys())



def test_a::d_is_not_abstract():
    assert not inspect.isabstract(A::D)


def test_a::d_constructor_exists():
    assert callable(A::D.__init__)


def test_a::d_constructor_args():
    sig = inspect.signature(A::D.__init__)
    params = list(sig.parameters.keys())



def test_a::c_is_not_abstract():
    assert not inspect.isabstract(A::C)


def test_a::c_constructor_exists():
    assert callable(A::C.__init__)


def test_a::c_constructor_args():
    sig = inspect.signature(A::C.__init__)
    params = list(sig.parameters.keys())



def test_a::b_is_not_abstract():
    assert not inspect.isabstract(A::B)


def test_a::b_constructor_exists():
    assert callable(A::B.__init__)


def test_a::b_constructor_args():
    sig = inspect.signature(A::B.__init__)
    params = list(sig.parameters.keys())



def test_a::a_is_not_abstract():
    assert not inspect.isabstract(A::A)


def test_a::a_constructor_exists():
    assert callable(A::A.__init__)


def test_a::a_constructor_args():
    sig = inspect.signature(A::A.__init__)
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
A::E_strategy = st.builds(
    A::E,
)
A::D_strategy = st.builds(
    A::D,
)
A::C_strategy = st.builds(
    A::C,
)
A::B_strategy = st.builds(
    A::B,
)
A::A_strategy = st.builds(
    A::A,
)

@given(instance=A::E_strategy)
@settings(max_examples=50)
def test_a::e_instantiation(instance):
    assert isinstance(instance, A::E)

@given(instance=A::D_strategy)
@settings(max_examples=50)
def test_a::d_instantiation(instance):
    assert isinstance(instance, A::D)

@given(instance=A::C_strategy)
@settings(max_examples=50)
def test_a::c_instantiation(instance):
    assert isinstance(instance, A::C)

@given(instance=A::B_strategy)
@settings(max_examples=50)
def test_a::b_instantiation(instance):
    assert isinstance(instance, A::B)

@given(instance=A::A_strategy)
@settings(max_examples=50)
def test_a::a_instantiation(instance):
    assert isinstance(instance, A::A)
