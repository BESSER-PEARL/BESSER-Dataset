import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    reference_C,
    reference_Y,
    reference_X,
    reference_B,
    reference_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_reference_c_is_not_abstract():
    assert not inspect.isabstract(reference_C)


def test_reference_c_constructor_exists():
    assert callable(reference_C.__init__)


def test_reference_c_constructor_args():
    sig = inspect.signature(reference_C.__init__)
    params = list(sig.parameters.keys())



def test_reference_y_is_not_abstract():
    assert not inspect.isabstract(reference_Y)


def test_reference_y_constructor_exists():
    assert callable(reference_Y.__init__)


def test_reference_y_constructor_args():
    sig = inspect.signature(reference_Y.__init__)
    params = list(sig.parameters.keys())



def test_reference_x_is_not_abstract():
    assert not inspect.isabstract(reference_X)


def test_reference_x_constructor_exists():
    assert callable(reference_X.__init__)


def test_reference_x_constructor_args():
    sig = inspect.signature(reference_X.__init__)
    params = list(sig.parameters.keys())



def test_reference_b_is_not_abstract():
    assert not inspect.isabstract(reference_B)


def test_reference_b_constructor_exists():
    assert callable(reference_B.__init__)


def test_reference_b_constructor_args():
    sig = inspect.signature(reference_B.__init__)
    params = list(sig.parameters.keys())



def test_reference_a_is_not_abstract():
    assert not inspect.isabstract(reference_A)


def test_reference_a_constructor_exists():
    assert callable(reference_A.__init__)


def test_reference_a_constructor_args():
    sig = inspect.signature(reference_A.__init__)
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
reference_C_strategy = st.builds(
    reference_C,
)
reference_Y_strategy = st.builds(
    reference_Y,
)
reference_X_strategy = st.builds(
    reference_X,
)
reference_B_strategy = st.builds(
    reference_B,
)
reference_A_strategy = st.builds(
    reference_A,
)

@given(instance=reference_C_strategy)
@settings(max_examples=50)
def test_reference_c_instantiation(instance):
    assert isinstance(instance, reference_C)

@given(instance=reference_Y_strategy)
@settings(max_examples=50)
def test_reference_y_instantiation(instance):
    assert isinstance(instance, reference_Y)

@given(instance=reference_X_strategy)
@settings(max_examples=50)
def test_reference_x_instantiation(instance):
    assert isinstance(instance, reference_X)

@given(instance=reference_B_strategy)
@settings(max_examples=50)
def test_reference_b_instantiation(instance):
    assert isinstance(instance, reference_B)

@given(instance=reference_A_strategy)
@settings(max_examples=50)
def test_reference_a_instantiation(instance):
    assert isinstance(instance, reference_A)
