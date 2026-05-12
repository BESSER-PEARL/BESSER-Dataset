import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    restaurant_Table,
    restaurant_Menu,
    restaurant_Restaurant,
    restaurant_Booking,
    restaurant_Waiter,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_restaurant_table_is_not_abstract():
    assert not inspect.isabstract(restaurant_Table)


def test_restaurant_table_constructor_exists():
    assert callable(restaurant_Table.__init__)


def test_restaurant_table_constructor_args():
    sig = inspect.signature(restaurant_Table.__init__)
    params = list(sig.parameters.keys())



def test_restaurant_menu_is_not_abstract():
    assert not inspect.isabstract(restaurant_Menu)


def test_restaurant_menu_constructor_exists():
    assert callable(restaurant_Menu.__init__)


def test_restaurant_menu_constructor_args():
    sig = inspect.signature(restaurant_Menu.__init__)
    params = list(sig.parameters.keys())



def test_restaurant_restaurant_is_not_abstract():
    assert not inspect.isabstract(restaurant_Restaurant)


def test_restaurant_restaurant_constructor_exists():
    assert callable(restaurant_Restaurant.__init__)


def test_restaurant_restaurant_constructor_args():
    sig = inspect.signature(restaurant_Restaurant.__init__)
    params = list(sig.parameters.keys())



def test_restaurant_booking_is_not_abstract():
    assert not inspect.isabstract(restaurant_Booking)


def test_restaurant_booking_constructor_exists():
    assert callable(restaurant_Booking.__init__)


def test_restaurant_booking_constructor_args():
    sig = inspect.signature(restaurant_Booking.__init__)
    params = list(sig.parameters.keys())



def test_restaurant_waiter_is_not_abstract():
    assert not inspect.isabstract(restaurant_Waiter)


def test_restaurant_waiter_constructor_exists():
    assert callable(restaurant_Waiter.__init__)


def test_restaurant_waiter_constructor_args():
    sig = inspect.signature(restaurant_Waiter.__init__)
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
restaurant_Table_strategy = st.builds(
    restaurant_Table,
)
restaurant_Menu_strategy = st.builds(
    restaurant_Menu,
)
restaurant_Restaurant_strategy = st.builds(
    restaurant_Restaurant,
)
restaurant_Booking_strategy = st.builds(
    restaurant_Booking,
)
restaurant_Waiter_strategy = st.builds(
    restaurant_Waiter,
)

@given(instance=restaurant_Table_strategy)
@settings(max_examples=50)
def test_restaurant_table_instantiation(instance):
    assert isinstance(instance, restaurant_Table)

@given(instance=restaurant_Menu_strategy)
@settings(max_examples=50)
def test_restaurant_menu_instantiation(instance):
    assert isinstance(instance, restaurant_Menu)

@given(instance=restaurant_Restaurant_strategy)
@settings(max_examples=50)
def test_restaurant_restaurant_instantiation(instance):
    assert isinstance(instance, restaurant_Restaurant)

@given(instance=restaurant_Booking_strategy)
@settings(max_examples=50)
def test_restaurant_booking_instantiation(instance):
    assert isinstance(instance, restaurant_Booking)

@given(instance=restaurant_Waiter_strategy)
@settings(max_examples=50)
def test_restaurant_waiter_instantiation(instance):
    assert isinstance(instance, restaurant_Waiter)
