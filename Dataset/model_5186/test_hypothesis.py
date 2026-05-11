import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    B,
    A,
    multi::C,
    multi::B,
    multi::A,
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



def test_multi::c_is_not_abstract():
    assert not inspect.isabstract(multi::C)


def test_multi::c_constructor_exists():
    assert callable(multi::C.__init__)


def test_multi::c_constructor_args():
    sig = inspect.signature(multi::C.__init__)
    params = list(sig.parameters.keys())



def test_multi::b_is_not_abstract():
    assert not inspect.isabstract(multi::B)


def test_multi::b_constructor_exists():
    assert callable(multi::B.__init__)


def test_multi::b_constructor_args():
    sig = inspect.signature(multi::B.__init__)
    params = list(sig.parameters.keys())



def test_multi::a_is_not_abstract():
    assert not inspect.isabstract(multi::A)


def test_multi::a_constructor_exists():
    assert callable(multi::A.__init__)


def test_multi::a_constructor_args():
    sig = inspect.signature(multi::A.__init__)
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
multi::C_strategy = st.builds(
    multi::C,
)
multi::B_strategy = st.builds(
    multi::B,
)
multi::A_strategy = st.builds(
    multi::A,
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=multi::C_strategy)
@settings(max_examples=50)
def test_multi::c_instantiation(instance):
    assert isinstance(instance, multi::C)

@given(instance=multi::B_strategy)
@settings(max_examples=50)
def test_multi::b_instantiation(instance):
    assert isinstance(instance, multi::B)

@given(instance=multi::A_strategy)
@settings(max_examples=50)
def test_multi::a_instantiation(instance):
    assert isinstance(instance, multi::A)
