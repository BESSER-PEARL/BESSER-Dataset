import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_A,
    model_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_a_is_not_abstract():
    assert not inspect.isabstract(model_A)


def test_model_a_constructor_exists():
    assert callable(model_A.__init__)


def test_model_a_constructor_args():
    sig = inspect.signature(model_A.__init__)
    params = list(sig.parameters.keys())



def test_model_b_is_not_abstract():
    assert not inspect.isabstract(model_B)


def test_model_b_constructor_exists():
    assert callable(model_B.__init__)


def test_model_b_constructor_args():
    sig = inspect.signature(model_B.__init__)
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
model_A_strategy = st.builds(
    model_A,
)
model_B_strategy = st.builds(
    model_B,
)

@given(instance=model_A_strategy)
@settings(max_examples=50)
def test_model_a_instantiation(instance):
    assert isinstance(instance, model_A)

@given(instance=model_B_strategy)
@settings(max_examples=50)
def test_model_b_instantiation(instance):
    assert isinstance(instance, model_B)
