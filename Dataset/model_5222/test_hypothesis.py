import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model2::D,
    model2::C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model2::d_is_not_abstract():
    assert not inspect.isabstract(model2::D)


def test_model2::d_constructor_exists():
    assert callable(model2::D.__init__)


def test_model2::d_constructor_args():
    sig = inspect.signature(model2::D.__init__)
    params = list(sig.parameters.keys())



def test_model2::c_is_not_abstract():
    assert not inspect.isabstract(model2::C)


def test_model2::c_constructor_exists():
    assert callable(model2::C.__init__)


def test_model2::c_constructor_args():
    sig = inspect.signature(model2::C.__init__)
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
model2::D_strategy = st.builds(
    model2::D,
)
model2::C_strategy = st.builds(
    model2::C,
)

@given(instance=model2::D_strategy)
@settings(max_examples=50)
def test_model2::d_instantiation(instance):
    assert isinstance(instance, model2::D)

@given(instance=model2::C_strategy)
@settings(max_examples=50)
def test_model2::c_instantiation(instance):
    assert isinstance(instance, model2::C)
