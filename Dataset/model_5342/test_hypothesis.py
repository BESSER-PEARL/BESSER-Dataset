import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    a_A2,
    B2,
    B1,
    a_A1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_a2_is_not_abstract():
    assert not inspect.isabstract(a_A2)


def test_a_a2_constructor_exists():
    assert callable(a_A2.__init__)


def test_a_a2_constructor_args():
    sig = inspect.signature(a_A2.__init__)
    params = list(sig.parameters.keys())



def test_b2_is_not_abstract():
    assert not inspect.isabstract(B2)


def test_b2_constructor_exists():
    assert callable(B2.__init__)


def test_b2_constructor_args():
    sig = inspect.signature(B2.__init__)
    params = list(sig.parameters.keys())



def test_b1_is_not_abstract():
    assert not inspect.isabstract(B1)


def test_b1_constructor_exists():
    assert callable(B1.__init__)


def test_b1_constructor_args():
    sig = inspect.signature(B1.__init__)
    params = list(sig.parameters.keys())



def test_a_a1_is_not_abstract():
    assert not inspect.isabstract(a_A1)


def test_a_a1_constructor_exists():
    assert callable(a_A1.__init__)


def test_a_a1_constructor_args():
    sig = inspect.signature(a_A1.__init__)
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
a_A2_strategy = st.builds(
    a_A2,
)
B2_strategy = st.builds(
    B2,
)
B1_strategy = st.builds(
    B1,
)
a_A1_strategy = st.builds(
    a_A1,
)

@given(instance=a_A2_strategy)
@settings(max_examples=50)
def test_a_a2_instantiation(instance):
    assert isinstance(instance, a_A2)

@given(instance=B2_strategy)
@settings(max_examples=50)
def test_b2_instantiation(instance):
    assert isinstance(instance, B2)

@given(instance=B1_strategy)
@settings(max_examples=50)
def test_b1_instantiation(instance):
    assert isinstance(instance, B1)

@given(instance=a_A1_strategy)
@settings(max_examples=50)
def test_a_a1_instantiation(instance):
    assert isinstance(instance, a_A1)
