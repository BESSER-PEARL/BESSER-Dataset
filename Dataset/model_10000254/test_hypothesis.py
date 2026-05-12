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
    Customer,
    Event,
    Worker,
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



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())
    assert "entity" in params, "Missing parameter 'entity'"
    assert "created_at" in params, "Missing parameter 'created_at'"

def test_event_has_entity():
    assert hasattr(Event, "entity")
    descriptor = None
    for klass in Event.__mro__:
        if "entity" in klass.__dict__:
            descriptor = klass.__dict__["entity"]
            break
    assert isinstance(descriptor, property)

def test_event_has_created_at():
    assert hasattr(Event, "created_at")
    descriptor = None
    for klass in Event.__mro__:
        if "created_at" in klass.__dict__:
            descriptor = klass.__dict__["created_at"]
            break
    assert isinstance(descriptor, property)



def test_worker_is_not_abstract():
    assert not inspect.isabstract(Worker)


def test_worker_constructor_exists():
    assert callable(Worker.__init__)


def test_worker_constructor_args():
    sig = inspect.signature(Worker.__init__)
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
Customer_strategy = st.builds(
    Customer,
)
Event_strategy = st.builds(
    Event,
    entity=
        safe_text,
    created_at=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Worker_strategy = st.builds(
    Worker,
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

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)



@given(instance=Event_strategy)
def test_event_entity_setter(instance):
    original = instance.entity
    instance.entity = original
    assert instance.entity == original



@given(instance=Event_strategy)
def test_event_created_at_setter(instance):
    original = instance.created_at
    instance.created_at = original
    assert instance.created_at == original

@given(instance=Worker_strategy)
@settings(max_examples=50)
def test_worker_instantiation(instance):
    assert isinstance(instance, Worker)
