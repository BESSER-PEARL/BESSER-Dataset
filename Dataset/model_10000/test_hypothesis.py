import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    bank_Manager,
    bank_Bank,
    bank_Card,
    bank_Client,
    bank_Account,
    CardType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bank_manager_is_not_abstract():
    assert not inspect.isabstract(bank_Manager)


def test_bank_manager_constructor_exists():
    assert callable(bank_Manager.__init__)


def test_bank_manager_constructor_args():
    sig = inspect.signature(bank_Manager.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bank_manager_has_name():
    assert hasattr(bank_Manager, "name")
    descriptor = None
    for klass in bank_Manager.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bank_bank_is_not_abstract():
    assert not inspect.isabstract(bank_Bank)


def test_bank_bank_constructor_exists():
    assert callable(bank_Bank.__init__)


def test_bank_bank_constructor_args():
    sig = inspect.signature(bank_Bank.__init__)
    params = list(sig.parameters.keys())



def test_bank_card_is_not_abstract():
    assert not inspect.isabstract(bank_Card)


def test_bank_card_constructor_exists():
    assert callable(bank_Card.__init__)


def test_bank_card_constructor_args():
    sig = inspect.signature(bank_Card.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "number" in params, "Missing parameter 'number'"

def test_bank_card_has_type():
    assert hasattr(bank_Card, "type")
    descriptor = None
    for klass in bank_Card.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bank_card_has_number():
    assert hasattr(bank_Card, "number")
    descriptor = None
    for klass in bank_Card.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_bank_client_is_not_abstract():
    assert not inspect.isabstract(bank_Client)


def test_bank_client_constructor_exists():
    assert callable(bank_Client.__init__)


def test_bank_client_constructor_args():
    sig = inspect.signature(bank_Client.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "name" in params, "Missing parameter 'name'"

def test_bank_client_has_capacity():
    assert hasattr(bank_Client, "capacity")
    descriptor = None
    for klass in bank_Client.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_bank_client_has_name():
    assert hasattr(bank_Client, "name")
    descriptor = None
    for klass in bank_Client.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bank_account_is_not_abstract():
    assert not inspect.isabstract(bank_Account)


def test_bank_account_constructor_exists():
    assert callable(bank_Account.__init__)


def test_bank_account_constructor_args():
    sig = inspect.signature(bank_Account.__init__)
    params = list(sig.parameters.keys())
    assert "overdraft" in params, "Missing parameter 'overdraft'"
    assert "credit" in params, "Missing parameter 'credit'"

def test_bank_account_has_overdraft():
    assert hasattr(bank_Account, "overdraft")
    descriptor = None
    for klass in bank_Account.__mro__:
        if "overdraft" in klass.__dict__:
            descriptor = klass.__dict__["overdraft"]
            break
    assert isinstance(descriptor, property)

def test_bank_account_has_credit():
    assert hasattr(bank_Account, "credit")
    descriptor = None
    for klass in bank_Account.__mro__:
        if "credit" in klass.__dict__:
            descriptor = klass.__dict__["credit"]
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
bank_Manager_strategy = st.builds(
    bank_Manager,
    name=
        safe_text
)
bank_Bank_strategy = st.builds(
    bank_Bank,
)
bank_Card_strategy = st.builds(
    bank_Card,
    type=
        safe_text,
    number=
        safe_text
)
bank_Client_strategy = st.builds(
    bank_Client,
    capacity=
        st.integers(),
    name=
        safe_text
)
bank_Account_strategy = st.builds(
    bank_Account,
    overdraft=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=bank_Manager_strategy)
@settings(max_examples=50)
def test_bank_manager_instantiation(instance):
    assert isinstance(instance, bank_Manager)



@given(instance=bank_Manager_strategy)
def test_bank_manager_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bank_Bank_strategy)
@settings(max_examples=50)
def test_bank_bank_instantiation(instance):
    assert isinstance(instance, bank_Bank)

@given(instance=bank_Card_strategy)
@settings(max_examples=50)
def test_bank_card_instantiation(instance):
    assert isinstance(instance, bank_Card)



@given(instance=bank_Card_strategy)
def test_bank_card_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=bank_Card_strategy)
def test_bank_card_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=bank_Client_strategy)
@settings(max_examples=50)
def test_bank_client_instantiation(instance):
    assert isinstance(instance, bank_Client)



@given(instance=bank_Client_strategy)
def test_bank_client_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=bank_Client_strategy)
def test_bank_client_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bank_Account_strategy)
@settings(max_examples=50)
def test_bank_account_instantiation(instance):
    assert isinstance(instance, bank_Account)



@given(instance=bank_Account_strategy)
def test_bank_account_overdraft_setter(instance):
    original = instance.overdraft
    instance.overdraft = original
    assert instance.overdraft == original



@given(instance=bank_Account_strategy)
def test_bank_account_credit_setter(instance):
    original = instance.credit
    instance.credit = original
    assert instance.credit == original
