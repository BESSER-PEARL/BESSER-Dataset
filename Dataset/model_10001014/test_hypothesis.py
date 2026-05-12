import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Cashier,
    Waiter,
    Cook,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cashier_is_not_abstract():
    assert not inspect.isabstract(Cashier)


def test_cashier_constructor_exists():
    assert callable(Cashier.__init__)


def test_cashier_constructor_args():
    sig = inspect.signature(Cashier.__init__)
    params = list(sig.parameters.keys())



def test_waiter_is_not_abstract():
    assert not inspect.isabstract(Waiter)


def test_waiter_constructor_exists():
    assert callable(Waiter.__init__)


def test_waiter_constructor_args():
    sig = inspect.signature(Waiter.__init__)
    params = list(sig.parameters.keys())



def test_cook_is_not_abstract():
    assert not inspect.isabstract(Cook)


def test_cook_constructor_exists():
    assert callable(Cook.__init__)


def test_cook_constructor_args():
    sig = inspect.signature(Cook.__init__)
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
Cashier_strategy = st.builds(
    Cashier,
)
Waiter_strategy = st.builds(
    Waiter,
)
Cook_strategy = st.builds(
    Cook,
)

@given(instance=Cashier_strategy)
@settings(max_examples=50)
def test_cashier_instantiation(instance):
    assert isinstance(instance, Cashier)

@given(instance=Waiter_strategy)
@settings(max_examples=50)
def test_waiter_instantiation(instance):
    assert isinstance(instance, Waiter)

@given(instance=Cook_strategy)
@settings(max_examples=50)
def test_cook_instantiation(instance):
    assert isinstance(instance, Cook)
