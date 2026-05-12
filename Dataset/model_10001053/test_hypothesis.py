import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Premium_class,
    Business_class,
    Normal_class,
    System,
    Room,
    Hotel,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_premium_class_is_not_abstract():
    assert not inspect.isabstract(Premium_class)


def test_premium_class_constructor_exists():
    assert callable(Premium_class.__init__)


def test_premium_class_constructor_args():
    sig = inspect.signature(Premium_class.__init__)
    params = list(sig.parameters.keys())



def test_business_class_is_not_abstract():
    assert not inspect.isabstract(Business_class)


def test_business_class_constructor_exists():
    assert callable(Business_class.__init__)


def test_business_class_constructor_args():
    sig = inspect.signature(Business_class.__init__)
    params = list(sig.parameters.keys())



def test_normal_class_is_not_abstract():
    assert not inspect.isabstract(Normal_class)


def test_normal_class_constructor_exists():
    assert callable(Normal_class.__init__)


def test_normal_class_constructor_args():
    sig = inspect.signature(Normal_class.__init__)
    params = list(sig.parameters.keys())



def test_system_is_not_abstract():
    assert not inspect.isabstract(System)


def test_system_constructor_exists():
    assert callable(System.__init__)


def test_system_constructor_args():
    sig = inspect.signature(System.__init__)
    params = list(sig.parameters.keys())



def test_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_room_constructor_exists():
    assert callable(Room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())



def test_hotel_is_not_abstract():
    assert not inspect.isabstract(Hotel)


def test_hotel_constructor_exists():
    assert callable(Hotel.__init__)


def test_hotel_constructor_args():
    sig = inspect.signature(Hotel.__init__)
    params = list(sig.parameters.keys())



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
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
Premium_class_strategy = st.builds(
    Premium_class,
)
Business_class_strategy = st.builds(
    Business_class,
)
Normal_class_strategy = st.builds(
    Normal_class,
)
System_strategy = st.builds(
    System,
)
Room_strategy = st.builds(
    Room,
)
Hotel_strategy = st.builds(
    Hotel,
)
Customer_strategy = st.builds(
    Customer,
)

@given(instance=Premium_class_strategy)
@settings(max_examples=50)
def test_premium_class_instantiation(instance):
    assert isinstance(instance, Premium_class)

@given(instance=Business_class_strategy)
@settings(max_examples=50)
def test_business_class_instantiation(instance):
    assert isinstance(instance, Business_class)

@given(instance=Normal_class_strategy)
@settings(max_examples=50)
def test_normal_class_instantiation(instance):
    assert isinstance(instance, Normal_class)

@given(instance=System_strategy)
@settings(max_examples=50)
def test_system_instantiation(instance):
    assert isinstance(instance, System)

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)

@given(instance=Hotel_strategy)
@settings(max_examples=50)
def test_hotel_instantiation(instance):
    assert isinstance(instance, Hotel)

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)
