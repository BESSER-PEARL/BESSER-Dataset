import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    A,
    model::B,
    model::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_model::b_is_not_abstract():
    assert not inspect.isabstract(model::B)


def test_model::b_constructor_exists():
    assert callable(model::B.__init__)


def test_model::b_constructor_args():
    sig = inspect.signature(model::B.__init__)
    params = list(sig.parameters.keys())



def test_model::a_is_not_abstract():
    assert not inspect.isabstract(model::A)


def test_model::a_constructor_exists():
    assert callable(model::A.__init__)


def test_model::a_constructor_args():
    sig = inspect.signature(model::A.__init__)
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
A_strategy = st.builds(
    A,
)
model::B_strategy = st.builds(
    model::B,
)
model::A_strategy = st.builds(
    model::A,
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=model::B_strategy)
@settings(max_examples=50)
def test_model::b_instantiation(instance):
    assert isinstance(instance, model::B)

@given(instance=model::A_strategy)
@settings(max_examples=50)
def test_model::a_instantiation(instance):
    assert isinstance(instance, model::A)
