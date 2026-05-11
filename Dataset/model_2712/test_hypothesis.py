import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::Program,
    test::C,
    A,
    test::B,
    test::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::program_is_not_abstract():
    assert not inspect.isabstract(test::Program)


def test_test::program_constructor_exists():
    assert callable(test::Program.__init__)


def test_test::program_constructor_args():
    sig = inspect.signature(test::Program.__init__)
    params = list(sig.parameters.keys())



def test_test::c_is_not_abstract():
    assert not inspect.isabstract(test::C)


def test_test::c_constructor_exists():
    assert callable(test::C.__init__)


def test_test::c_constructor_args():
    sig = inspect.signature(test::C.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_test::b_is_not_abstract():
    assert not inspect.isabstract(test::B)


def test_test::b_constructor_exists():
    assert callable(test::B.__init__)


def test_test::b_constructor_args():
    sig = inspect.signature(test::B.__init__)
    params = list(sig.parameters.keys())



def test_test::a_is_not_abstract():
    assert not inspect.isabstract(test::A)


def test_test::a_constructor_exists():
    assert callable(test::A.__init__)


def test_test::a_constructor_args():
    sig = inspect.signature(test::A.__init__)
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
test::Program_strategy = st.builds(
    test::Program,
)
test::C_strategy = st.builds(
    test::C,
)
A_strategy = st.builds(
    A,
)
test::B_strategy = st.builds(
    test::B,
)
test::A_strategy = st.builds(
    test::A,
)

@given(instance=test::Program_strategy)
@settings(max_examples=50)
def test_test::program_instantiation(instance):
    assert isinstance(instance, test::Program)

@given(instance=test::C_strategy)
@settings(max_examples=50)
def test_test::c_instantiation(instance):
    assert isinstance(instance, test::C)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=test::B_strategy)
@settings(max_examples=50)
def test_test::b_instantiation(instance):
    assert isinstance(instance, test::B)

@given(instance=test::A_strategy)
@settings(max_examples=50)
def test_test::a_instantiation(instance):
    assert isinstance(instance, test::A)
