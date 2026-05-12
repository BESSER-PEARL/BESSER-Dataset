import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_Program,
    test_C,
    A,
    test_B,
    test_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_program_is_not_abstract():
    assert not inspect.isabstract(test_Program)


def test_test_program_constructor_exists():
    assert callable(test_Program.__init__)


def test_test_program_constructor_args():
    sig = inspect.signature(test_Program.__init__)
    params = list(sig.parameters.keys())



def test_test_c_is_not_abstract():
    assert not inspect.isabstract(test_C)


def test_test_c_constructor_exists():
    assert callable(test_C.__init__)


def test_test_c_constructor_args():
    sig = inspect.signature(test_C.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_test_b_is_not_abstract():
    assert not inspect.isabstract(test_B)


def test_test_b_constructor_exists():
    assert callable(test_B.__init__)


def test_test_b_constructor_args():
    sig = inspect.signature(test_B.__init__)
    params = list(sig.parameters.keys())



def test_test_a_is_not_abstract():
    assert not inspect.isabstract(test_A)


def test_test_a_constructor_exists():
    assert callable(test_A.__init__)


def test_test_a_constructor_args():
    sig = inspect.signature(test_A.__init__)
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
test_Program_strategy = st.builds(
    test_Program,
)
test_C_strategy = st.builds(
    test_C,
)
A_strategy = st.builds(
    A,
)
test_B_strategy = st.builds(
    test_B,
)
test_A_strategy = st.builds(
    test_A,
)

@given(instance=test_Program_strategy)
@settings(max_examples=50)
def test_test_program_instantiation(instance):
    assert isinstance(instance, test_Program)

@given(instance=test_C_strategy)
@settings(max_examples=50)
def test_test_c_instantiation(instance):
    assert isinstance(instance, test_C)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=test_B_strategy)
@settings(max_examples=50)
def test_test_b_instantiation(instance):
    assert isinstance(instance, test_B)

@given(instance=test_A_strategy)
@settings(max_examples=50)
def test_test_a_instantiation(instance):
    assert isinstance(instance, test_A)
