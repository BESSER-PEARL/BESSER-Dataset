import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    bank::Manager,
    bank::Bank,
    bank::Card,
    bank::Client,
    bank::Account,
    CardType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bank::manager_is_not_abstract():
    assert not inspect.isabstract(bank::Manager)


def test_bank::manager_constructor_exists():
    assert callable(bank::Manager.__init__)


def test_bank::manager_constructor_args():
    sig = inspect.signature(bank::Manager.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bank::manager_has_name():
    assert hasattr(bank::Manager, "name")
    descriptor = None
    for klass in bank::Manager.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bank::bank_is_not_abstract():
    assert not inspect.isabstract(bank::Bank)


def test_bank::bank_constructor_exists():
    assert callable(bank::Bank.__init__)


def test_bank::bank_constructor_args():
    sig = inspect.signature(bank::Bank.__init__)
    params = list(sig.parameters.keys())



def test_bank::card_is_not_abstract():
    assert not inspect.isabstract(bank::Card)


def test_bank::card_constructor_exists():
    assert callable(bank::Card.__init__)


def test_bank::card_constructor_args():
    sig = inspect.signature(bank::Card.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "type" in params, "Missing parameter 'type'"

def test_bank::card_has_number():
    assert hasattr(bank::Card, "number")
    descriptor = None
    for klass in bank::Card.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_bank::card_has_type():
    assert hasattr(bank::Card, "type")
    descriptor = None
    for klass in bank::Card.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_bank::client_is_not_abstract():
    assert not inspect.isabstract(bank::Client)


def test_bank::client_constructor_exists():
    assert callable(bank::Client.__init__)


def test_bank::client_constructor_args():
    sig = inspect.signature(bank::Client.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "name" in params, "Missing parameter 'name'"

def test_bank::client_has_capacity():
    assert hasattr(bank::Client, "capacity")
    descriptor = None
    for klass in bank::Client.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_bank::client_has_name():
    assert hasattr(bank::Client, "name")
    descriptor = None
    for klass in bank::Client.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bank::account_is_not_abstract():
    assert not inspect.isabstract(bank::Account)


def test_bank::account_constructor_exists():
    assert callable(bank::Account.__init__)


def test_bank::account_constructor_args():
    sig = inspect.signature(bank::Account.__init__)
    params = list(sig.parameters.keys())
    assert "credit" in params, "Missing parameter 'credit'"
    assert "overdraft" in params, "Missing parameter 'overdraft'"

def test_bank::account_has_credit():
    assert hasattr(bank::Account, "credit")
    descriptor = None
    for klass in bank::Account.__mro__:
        if "credit" in klass.__dict__:
            descriptor = klass.__dict__["credit"]
            break
    assert isinstance(descriptor, property)

def test_bank::account_has_overdraft():
    assert hasattr(bank::Account, "overdraft")
    descriptor = None
    for klass in bank::Account.__mro__:
        if "overdraft" in klass.__dict__:
            descriptor = klass.__dict__["overdraft"]
            break
    assert isinstance(descriptor, property)

def test_cardtype_exists():
    # Check that the Enumeration exists
    assert CardType is not None

def test_cardtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CardType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CardType"


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
bank::Manager_strategy = st.builds(
    bank::Manager,
    name=
        safe_text
)
bank::Bank_strategy = st.builds(
    bank::Bank,
)
bank::Card_strategy = st.builds(
    bank::Card,
    number=
        safe_text,
    type=
        safe_text
)
bank::Client_strategy = st.builds(
    bank::Client,
    capacity=
        st.integers(),
    name=
        safe_text
)
bank::Account_strategy = st.builds(
    bank::Account,
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    overdraft=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=bank::Manager_strategy)
@settings(max_examples=50)
def test_bank::manager_instantiation(instance):
    assert isinstance(instance, bank::Manager)

@given(instance=bank::Manager_strategy)
def test_bank::manager_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bank::Manager_strategy)
def test_bank::manager_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bank::Bank_strategy)
@settings(max_examples=50)
def test_bank::bank_instantiation(instance):
    assert isinstance(instance, bank::Bank)

@given(instance=bank::Card_strategy)
@settings(max_examples=50)
def test_bank::card_instantiation(instance):
    assert isinstance(instance, bank::Card)

@given(instance=bank::Card_strategy)
def test_bank::card_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=bank::Card_strategy)
def test_bank::card_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=bank::Card_strategy)
def test_bank::card_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=bank::Card_strategy)
def test_bank::card_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=bank::Client_strategy)
@settings(max_examples=50)
def test_bank::client_instantiation(instance):
    assert isinstance(instance, bank::Client)

@given(instance=bank::Client_strategy)
def test_bank::client_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=bank::Client_strategy)
def test_bank::client_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=bank::Client_strategy)
def test_bank::client_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bank::Client_strategy)
def test_bank::client_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bank::Account_strategy)
@settings(max_examples=50)
def test_bank::account_instantiation(instance):
    assert isinstance(instance, bank::Account)

@given(instance=bank::Account_strategy)
def test_bank::account_credit_type(instance):
    assert isinstance(instance.credit, float)


@given(instance=bank::Account_strategy)
def test_bank::account_credit_setter(instance):
    original = instance.credit
    instance.credit = original
    assert instance.credit == original

@given(instance=bank::Account_strategy)
def test_bank::account_overdraft_type(instance):
    assert isinstance(instance.overdraft, float)


@given(instance=bank::Account_strategy)
def test_bank::account_overdraft_setter(instance):
    original = instance.overdraft
    instance.overdraft = original
    assert instance.overdraft == original
