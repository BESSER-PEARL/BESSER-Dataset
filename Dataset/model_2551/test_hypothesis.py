import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test2::E,
    D,
    test2::D2,
    test2::D,
    B,
    test2::C,
    test2::B,
    test2::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test2::e_is_not_abstract():
    assert not inspect.isabstract(test2::E)


def test_test2::e_constructor_exists():
    assert callable(test2::E.__init__)


def test_test2::e_constructor_args():
    sig = inspect.signature(test2::E.__init__)
    params = list(sig.parameters.keys())



def test_d_is_not_abstract():
    assert not inspect.isabstract(D)


def test_d_constructor_exists():
    assert callable(D.__init__)


def test_d_constructor_args():
    sig = inspect.signature(D.__init__)
    params = list(sig.parameters.keys())



def test_test2::d2_is_not_abstract():
    assert not inspect.isabstract(test2::D2)


def test_test2::d2_constructor_exists():
    assert callable(test2::D2.__init__)


def test_test2::d2_constructor_args():
    sig = inspect.signature(test2::D2.__init__)
    params = list(sig.parameters.keys())



def test_test2::d_is_not_abstract():
    assert not inspect.isabstract(test2::D)


def test_test2::d_constructor_exists():
    assert callable(test2::D.__init__)


def test_test2::d_constructor_args():
    sig = inspect.signature(test2::D.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_test2::c_is_not_abstract():
    assert not inspect.isabstract(test2::C)


def test_test2::c_constructor_exists():
    assert callable(test2::C.__init__)


def test_test2::c_constructor_args():
    sig = inspect.signature(test2::C.__init__)
    params = list(sig.parameters.keys())



def test_test2::b_is_not_abstract():
    assert not inspect.isabstract(test2::B)


def test_test2::b_constructor_exists():
    assert callable(test2::B.__init__)


def test_test2::b_constructor_args():
    sig = inspect.signature(test2::B.__init__)
    params = list(sig.parameters.keys())



def test_test2::a_is_not_abstract():
    assert not inspect.isabstract(test2::A)


def test_test2::a_constructor_exists():
    assert callable(test2::A.__init__)


def test_test2::a_constructor_args():
    sig = inspect.signature(test2::A.__init__)
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
test2::E_strategy = st.builds(
    test2::E,
)
D_strategy = st.builds(
    D,
)
test2::D2_strategy = st.builds(
    test2::D2,
)
test2::D_strategy = st.builds(
    test2::D,
)
B_strategy = st.builds(
    B,
)
test2::C_strategy = st.builds(
    test2::C,
)
test2::B_strategy = st.builds(
    test2::B,
)
test2::A_strategy = st.builds(
    test2::A,
)

@given(instance=test2::E_strategy)
@settings(max_examples=50)
def test_test2::e_instantiation(instance):
    assert isinstance(instance, test2::E)

@given(instance=D_strategy)
@settings(max_examples=50)
def test_d_instantiation(instance):
    assert isinstance(instance, D)

@given(instance=test2::D2_strategy)
@settings(max_examples=50)
def test_test2::d2_instantiation(instance):
    assert isinstance(instance, test2::D2)

@given(instance=test2::D_strategy)
@settings(max_examples=50)
def test_test2::d_instantiation(instance):
    assert isinstance(instance, test2::D)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=test2::C_strategy)
@settings(max_examples=50)
def test_test2::c_instantiation(instance):
    assert isinstance(instance, test2::C)

@given(instance=test2::B_strategy)
@settings(max_examples=50)
def test_test2::b_instantiation(instance):
    assert isinstance(instance, test2::B)

@given(instance=test2::A_strategy)
@settings(max_examples=50)
def test_test2::a_instantiation(instance):
    assert isinstance(instance, test2::A)
