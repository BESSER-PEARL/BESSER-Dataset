import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test2_test2sub2_E,
    D,
    test2_test2sub1_D2,
    test2_test2sub1_D,
    B,
    test2_C,
    test2_B,
    test2_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test2_test2sub2_e_is_not_abstract():
    assert not inspect.isabstract(test2_test2sub2_E)


def test_test2_test2sub2_e_constructor_exists():
    assert callable(test2_test2sub2_E.__init__)


def test_test2_test2sub2_e_constructor_args():
    sig = inspect.signature(test2_test2sub2_E.__init__)
    params = list(sig.parameters.keys())



def test_d_is_not_abstract():
    assert not inspect.isabstract(D)


def test_d_constructor_exists():
    assert callable(D.__init__)


def test_d_constructor_args():
    sig = inspect.signature(D.__init__)
    params = list(sig.parameters.keys())



def test_test2_test2sub1_d2_is_not_abstract():
    assert not inspect.isabstract(test2_test2sub1_D2)


def test_test2_test2sub1_d2_constructor_exists():
    assert callable(test2_test2sub1_D2.__init__)


def test_test2_test2sub1_d2_constructor_args():
    sig = inspect.signature(test2_test2sub1_D2.__init__)
    params = list(sig.parameters.keys())



def test_test2_test2sub1_d_is_not_abstract():
    assert not inspect.isabstract(test2_test2sub1_D)


def test_test2_test2sub1_d_constructor_exists():
    assert callable(test2_test2sub1_D.__init__)


def test_test2_test2sub1_d_constructor_args():
    sig = inspect.signature(test2_test2sub1_D.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_test2_c_is_not_abstract():
    assert not inspect.isabstract(test2_C)


def test_test2_c_constructor_exists():
    assert callable(test2_C.__init__)


def test_test2_c_constructor_args():
    sig = inspect.signature(test2_C.__init__)
    params = list(sig.parameters.keys())



def test_test2_b_is_not_abstract():
    assert not inspect.isabstract(test2_B)


def test_test2_b_constructor_exists():
    assert callable(test2_B.__init__)


def test_test2_b_constructor_args():
    sig = inspect.signature(test2_B.__init__)
    params = list(sig.parameters.keys())



def test_test2_a_is_not_abstract():
    assert not inspect.isabstract(test2_A)


def test_test2_a_constructor_exists():
    assert callable(test2_A.__init__)


def test_test2_a_constructor_args():
    sig = inspect.signature(test2_A.__init__)
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
test2_test2sub2_E_strategy = st.builds(
    test2_test2sub2_E,
)
D_strategy = st.builds(
    D,
)
test2_test2sub1_D2_strategy = st.builds(
    test2_test2sub1_D2,
)
test2_test2sub1_D_strategy = st.builds(
    test2_test2sub1_D,
)
B_strategy = st.builds(
    B,
)
test2_C_strategy = st.builds(
    test2_C,
)
test2_B_strategy = st.builds(
    test2_B,
)
test2_A_strategy = st.builds(
    test2_A,
)

@given(instance=test2_test2sub2_E_strategy)
@settings(max_examples=50)
def test_test2_test2sub2_e_instantiation(instance):
    assert isinstance(instance, test2_test2sub2_E)

@given(instance=D_strategy)
@settings(max_examples=50)
def test_d_instantiation(instance):
    assert isinstance(instance, D)

@given(instance=test2_test2sub1_D2_strategy)
@settings(max_examples=50)
def test_test2_test2sub1_d2_instantiation(instance):
    assert isinstance(instance, test2_test2sub1_D2)

@given(instance=test2_test2sub1_D_strategy)
@settings(max_examples=50)
def test_test2_test2sub1_d_instantiation(instance):
    assert isinstance(instance, test2_test2sub1_D)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=test2_C_strategy)
@settings(max_examples=50)
def test_test2_c_instantiation(instance):
    assert isinstance(instance, test2_C)

@given(instance=test2_B_strategy)
@settings(max_examples=50)
def test_test2_b_instantiation(instance):
    assert isinstance(instance, test2_B)

@given(instance=test2_A_strategy)
@settings(max_examples=50)
def test_test2_a_instantiation(instance):
    assert isinstance(instance, test2_A)
