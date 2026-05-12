import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Worker,
    Cashier,
    Waiter,
    Cook,
    Customer,
    People,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_worker_is_not_abstract():
    assert not inspect.isabstract(Worker)


def test_worker_constructor_exists():
    assert callable(Worker.__init__)


def test_worker_constructor_args():
    sig = inspect.signature(Worker.__init__)
    params = list(sig.parameters.keys())
    assert "Cook" in params, "Missing parameter 'Cook'"
    assert "Waitor" in params, "Missing parameter 'Waitor'"
    assert "Cashier" in params, "Missing parameter 'Cashier'"

def test_worker_has_Cook():
    assert hasattr(Worker, "Cook")
    descriptor = None
    for klass in Worker.__mro__:
        if "Cook" in klass.__dict__:
            descriptor = klass.__dict__["Cook"]
            break
    assert isinstance(descriptor, property)

def test_worker_has_Waitor():
    assert hasattr(Worker, "Waitor")
    descriptor = None
    for klass in Worker.__mro__:
        if "Waitor" in klass.__dict__:
            descriptor = klass.__dict__["Waitor"]
            break
    assert isinstance(descriptor, property)

def test_worker_has_Cashier():
    assert hasattr(Worker, "Cashier")
    descriptor = None
    for klass in Worker.__mro__:
        if "Cashier" in klass.__dict__:
            descriptor = klass.__dict__["Cashier"]
            break
    assert isinstance(descriptor, property)



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



def test_people_is_not_abstract():
    assert not inspect.isabstract(People)


def test_people_constructor_exists():
    assert callable(People.__init__)


def test_people_constructor_args():
    sig = inspect.signature(People.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "Worker" in params, "Missing parameter 'Worker'"
    assert "Custumer_" in params, "Missing parameter 'Custumer_'"

def test_people_has_name():
    assert hasattr(People, "name")
    descriptor = None
    for klass in People.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_people_has_Worker():
    assert hasattr(People, "Worker")
    descriptor = None
    for klass in People.__mro__:
        if "Worker" in klass.__dict__:
            descriptor = klass.__dict__["Worker"]
            break
    assert isinstance(descriptor, property)

def test_people_has_Custumer_():
    assert hasattr(People, "Custumer_")
    descriptor = None
    for klass in People.__mro__:
        if "Custumer_" in klass.__dict__:
            descriptor = klass.__dict__["Custumer_"]
            break
    assert isinstance(descriptor, property)


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
Worker_strategy = st.builds(
    Worker,
    Cook=
        safe_text,
    Waitor=
        safe_text,
    Cashier=
        safe_text
)
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
People_strategy = st.builds(
    People,
    name=
        safe_text,
    Worker=
        safe_text,
    Custumer_=
        safe_text
)

@given(instance=Worker_strategy)
@settings(max_examples=50)
def test_worker_instantiation(instance):
    assert isinstance(instance, Worker)



@given(instance=Worker_strategy)
def test_worker_Cook_setter(instance):
    original = instance.Cook
    instance.Cook = original
    assert instance.Cook == original



@given(instance=Worker_strategy)
def test_worker_Waitor_setter(instance):
    original = instance.Waitor
    instance.Waitor = original
    assert instance.Waitor == original



@given(instance=Worker_strategy)
def test_worker_Cashier_setter(instance):
    original = instance.Cashier
    instance.Cashier = original
    assert instance.Cashier == original

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

@given(instance=People_strategy)
@settings(max_examples=50)
def test_people_instantiation(instance):
    assert isinstance(instance, People)



@given(instance=People_strategy)
def test_people_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=People_strategy)
def test_people_Worker_setter(instance):
    original = instance.Worker
    instance.Worker = original
    assert instance.Worker == original



@given(instance=People_strategy)
def test_people_Custumer__setter(instance):
    original = instance.Custumer_
    instance.Custumer_ = original
    assert instance.Custumer_ == original
