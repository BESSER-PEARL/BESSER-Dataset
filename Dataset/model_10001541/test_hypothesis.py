import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    casier,
    Waiter,
    Cook,
    Customer,
    People,
    Worker,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_casier_is_not_abstract():
    assert not inspect.isabstract(casier)


def test_casier_constructor_exists():
    assert callable(casier.__init__)


def test_casier_constructor_args():
    sig = inspect.signature(casier.__init__)
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



def test_people_is_not_abstract():
    assert not inspect.isabstract(People)


def test_people_constructor_exists():
    assert callable(People.__init__)


def test_people_constructor_args():
    sig = inspect.signature(People.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_people_has_name():
    assert hasattr(People, "name")
    descriptor = None
    for klass in People.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
casier_strategy = st.builds(
    casier,
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
People_strategy = st.builds(
    People,
    name=
        safe_text
)
Worker_strategy = st.builds(
    Worker,
)

@given(instance=casier_strategy)
@settings(max_examples=50)
def test_casier_instantiation(instance):
    assert isinstance(instance, casier)

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

@given(instance=People_strategy)
@settings(max_examples=50)
def test_people_instantiation(instance):
    assert isinstance(instance, People)



@given(instance=People_strategy)
def test_people_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Worker_strategy)
@settings(max_examples=50)
def test_worker_instantiation(instance):
    assert isinstance(instance, Worker)
