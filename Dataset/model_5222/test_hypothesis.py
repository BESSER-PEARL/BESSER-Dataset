import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model2_D,
    model2_C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model2_d_is_not_abstract():
    assert not inspect.isabstract(model2_D)


def test_model2_d_constructor_exists():
    assert callable(model2_D.__init__)


def test_model2_d_constructor_args():
    sig = inspect.signature(model2_D.__init__)
    params = list(sig.parameters.keys())



def test_model2_c_is_not_abstract():
    assert not inspect.isabstract(model2_C)


def test_model2_c_constructor_exists():
    assert callable(model2_C.__init__)


def test_model2_c_constructor_args():
    sig = inspect.signature(model2_C.__init__)
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
model2_D_strategy = st.builds(
    model2_D,
)
model2_C_strategy = st.builds(
    model2_C,
)

@given(instance=model2_D_strategy)
@settings(max_examples=50)
def test_model2_d_instantiation(instance):
    assert isinstance(instance, model2_D)

@given(instance=model2_C_strategy)
@settings(max_examples=50)
def test_model2_c_instantiation(instance):
    assert isinstance(instance, model2_C)
