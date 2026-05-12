import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Cashier,
    SYSTEM,
    ADMIN,
    VOTER,
    People,
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



def test_system_is_not_abstract():
    assert not inspect.isabstract(SYSTEM)


def test_system_constructor_exists():
    assert callable(SYSTEM.__init__)


def test_system_constructor_args():
    sig = inspect.signature(SYSTEM.__init__)
    params = list(sig.parameters.keys())



def test_admin_is_not_abstract():
    assert not inspect.isabstract(ADMIN)


def test_admin_constructor_exists():
    assert callable(ADMIN.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(ADMIN.__init__)
    params = list(sig.parameters.keys())



def test_voter_is_not_abstract():
    assert not inspect.isabstract(VOTER)


def test_voter_constructor_exists():
    assert callable(VOTER.__init__)


def test_voter_constructor_args():
    sig = inspect.signature(VOTER.__init__)
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
Cashier_strategy = st.builds(
    Cashier,
)
SYSTEM_strategy = st.builds(
    SYSTEM,
)
ADMIN_strategy = st.builds(
    ADMIN,
)
VOTER_strategy = st.builds(
    VOTER,
)
People_strategy = st.builds(
    People,
    name=
        safe_text
)
Worker_strategy = st.builds(
    Worker,
)

@given(instance=Cashier_strategy)
@settings(max_examples=50)
def test_cashier_instantiation(instance):
    assert isinstance(instance, Cashier)

@given(instance=SYSTEM_strategy)
@settings(max_examples=50)
def test_system_instantiation(instance):
    assert isinstance(instance, SYSTEM)

@given(instance=ADMIN_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, ADMIN)

@given(instance=VOTER_strategy)
@settings(max_examples=50)
def test_voter_instantiation(instance):
    assert isinstance(instance, VOTER)

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
