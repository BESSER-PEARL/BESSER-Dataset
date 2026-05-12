import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_D,
    model_C,
    model_B,
    model_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_d_is_not_abstract():
    assert not inspect.isabstract(model_D)


def test_model_d_constructor_exists():
    assert callable(model_D.__init__)


def test_model_d_constructor_args():
    sig = inspect.signature(model_D.__init__)
    params = list(sig.parameters.keys())



def test_model_c_is_not_abstract():
    assert not inspect.isabstract(model_C)


def test_model_c_constructor_exists():
    assert callable(model_C.__init__)


def test_model_c_constructor_args():
    sig = inspect.signature(model_C.__init__)
    params = list(sig.parameters.keys())



def test_model_b_is_not_abstract():
    assert not inspect.isabstract(model_B)


def test_model_b_constructor_exists():
    assert callable(model_B.__init__)


def test_model_b_constructor_args():
    sig = inspect.signature(model_B.__init__)
    params = list(sig.parameters.keys())



def test_model_a_is_not_abstract():
    assert not inspect.isabstract(model_A)


def test_model_a_constructor_exists():
    assert callable(model_A.__init__)


def test_model_a_constructor_args():
    sig = inspect.signature(model_A.__init__)
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
model_D_strategy = st.builds(
    model_D,
)
model_C_strategy = st.builds(
    model_C,
)
model_B_strategy = st.builds(
    model_B,
)
model_A_strategy = st.builds(
    model_A,
)

@given(instance=model_D_strategy)
@settings(max_examples=50)
def test_model_d_instantiation(instance):
    assert isinstance(instance, model_D)

@given(instance=model_C_strategy)
@settings(max_examples=50)
def test_model_c_instantiation(instance):
    assert isinstance(instance, model_C)

@given(instance=model_B_strategy)
@settings(max_examples=50)
def test_model_b_instantiation(instance):
    assert isinstance(instance, model_B)

@given(instance=model_A_strategy)
@settings(max_examples=50)
def test_model_a_instantiation(instance):
    assert isinstance(instance, model_A)
