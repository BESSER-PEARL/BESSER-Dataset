import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    restaurant::Table,
    restaurant::Menu,
    restaurant::Restaurant,
    restaurant::Booking,
    restaurant::Waiter,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_restaurant::table_is_not_abstract():
    assert not inspect.isabstract(restaurant::Table)


def test_restaurant::table_constructor_exists():
    assert callable(restaurant::Table.__init__)


def test_restaurant::table_constructor_args():
    sig = inspect.signature(restaurant::Table.__init__)
    params = list(sig.parameters.keys())



def test_restaurant::menu_is_not_abstract():
    assert not inspect.isabstract(restaurant::Menu)


def test_restaurant::menu_constructor_exists():
    assert callable(restaurant::Menu.__init__)


def test_restaurant::menu_constructor_args():
    sig = inspect.signature(restaurant::Menu.__init__)
    params = list(sig.parameters.keys())



def test_restaurant::restaurant_is_not_abstract():
    assert not inspect.isabstract(restaurant::Restaurant)


def test_restaurant::restaurant_constructor_exists():
    assert callable(restaurant::Restaurant.__init__)


def test_restaurant::restaurant_constructor_args():
    sig = inspect.signature(restaurant::Restaurant.__init__)
    params = list(sig.parameters.keys())



def test_restaurant::booking_is_not_abstract():
    assert not inspect.isabstract(restaurant::Booking)


def test_restaurant::booking_constructor_exists():
    assert callable(restaurant::Booking.__init__)


def test_restaurant::booking_constructor_args():
    sig = inspect.signature(restaurant::Booking.__init__)
    params = list(sig.parameters.keys())



def test_restaurant::waiter_is_not_abstract():
    assert not inspect.isabstract(restaurant::Waiter)


def test_restaurant::waiter_constructor_exists():
    assert callable(restaurant::Waiter.__init__)


def test_restaurant::waiter_constructor_args():
    sig = inspect.signature(restaurant::Waiter.__init__)
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
restaurant::Table_strategy = st.builds(
    restaurant::Table,
)
restaurant::Menu_strategy = st.builds(
    restaurant::Menu,
)
restaurant::Restaurant_strategy = st.builds(
    restaurant::Restaurant,
)
restaurant::Booking_strategy = st.builds(
    restaurant::Booking,
)
restaurant::Waiter_strategy = st.builds(
    restaurant::Waiter,
)

@given(instance=restaurant::Table_strategy)
@settings(max_examples=50)
def test_restaurant::table_instantiation(instance):
    assert isinstance(instance, restaurant::Table)

@given(instance=restaurant::Menu_strategy)
@settings(max_examples=50)
def test_restaurant::menu_instantiation(instance):
    assert isinstance(instance, restaurant::Menu)

@given(instance=restaurant::Restaurant_strategy)
@settings(max_examples=50)
def test_restaurant::restaurant_instantiation(instance):
    assert isinstance(instance, restaurant::Restaurant)

@given(instance=restaurant::Booking_strategy)
@settings(max_examples=50)
def test_restaurant::booking_instantiation(instance):
    assert isinstance(instance, restaurant::Booking)

@given(instance=restaurant::Waiter_strategy)
@settings(max_examples=50)
def test_restaurant::waiter_instantiation(instance):
    assert isinstance(instance, restaurant::Waiter)
