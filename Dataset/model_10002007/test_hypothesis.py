import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Customer,
    Account,
    ATM,
    Bank,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "pin" in params, "Missing parameter 'pin'"
    assert "address" in params, "Missing parameter 'address'"
    assert "cardnumber" in params, "Missing parameter 'cardnumber'"
    assert "name" in params, "Missing parameter 'name'"
    assert "dob" in params, "Missing parameter 'dob'"

def test_customer_has_pin():
    assert hasattr(Customer, "pin")
    descriptor = None
    for klass in Customer.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_address():
    assert hasattr(Customer, "address")
    descriptor = None
    for klass in Customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_cardnumber():
    assert hasattr(Customer, "cardnumber")
    descriptor = None
    for klass in Customer.__mro__:
        if "cardnumber" in klass.__dict__:
            descriptor = klass.__dict__["cardnumber"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_name():
    assert hasattr(Customer, "name")
    descriptor = None
    for klass in Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_dob():
    assert hasattr(Customer, "dob")
    descriptor = None
    for klass in Customer.__mro__:
        if "dob" in klass.__dict__:
            descriptor = klass.__dict__["dob"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "balance" in params, "Missing parameter 'balance'"

def test_account_has_number():
    assert hasattr(Account, "number")
    descriptor = None
    for klass in Account.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_account_has_balance():
    assert hasattr(Account, "balance")
    descriptor = None
    for klass in Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)



def test_atm_is_not_abstract():
    assert not inspect.isabstract(ATM)


def test_atm_constructor_exists():
    assert callable(ATM.__init__)


def test_atm_constructor_args():
    sig = inspect.signature(ATM.__init__)
    params = list(sig.parameters.keys())
    assert "managedby" in params, "Missing parameter 'managedby'"
    assert "location" in params, "Missing parameter 'location'"

def test_atm_has_managedby():
    assert hasattr(ATM, "managedby")
    descriptor = None
    for klass in ATM.__mro__:
        if "managedby" in klass.__dict__:
            descriptor = klass.__dict__["managedby"]
            break
    assert isinstance(descriptor, property)

def test_atm_has_location():
    assert hasattr(ATM, "location")
    descriptor = None
    for klass in ATM.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_bank_is_not_abstract():
    assert not inspect.isabstract(Bank)


def test_bank_constructor_exists():
    assert callable(Bank.__init__)


def test_bank_constructor_args():
    sig = inspect.signature(Bank.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "address" in params, "Missing parameter 'address'"

def test_bank_has_code():
    assert hasattr(Bank, "code")
    descriptor = None
    for klass in Bank.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_bank_has_address():
    assert hasattr(Bank, "address")
    descriptor = None
    for klass in Bank.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
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
Customer_strategy = st.builds(
    Customer,
    pin=
        st.integers(),
    address=
        safe_text,
    cardnumber=
        st.integers(),
    name=
        safe_text,
    dob=
        safe_text
)
Account_strategy = st.builds(
    Account,
    number=
        st.integers(),
    balance=
        st.integers()
)
ATM_strategy = st.builds(
    ATM,
    managedby=
        safe_text,
    location=
        safe_text
)
Bank_strategy = st.builds(
    Bank,
    code=
        st.integers(),
    address=
        safe_text
)

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original



@given(instance=Customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_customer_cardnumber_setter(instance):
    original = instance.cardnumber
    instance.cardnumber = original
    assert instance.cardnumber == original



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Customer_strategy)
def test_customer_dob_setter(instance):
    original = instance.dob
    instance.dob = original
    assert instance.dob == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=Account_strategy)
def test_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original

@given(instance=ATM_strategy)
@settings(max_examples=50)
def test_atm_instantiation(instance):
    assert isinstance(instance, ATM)



@given(instance=ATM_strategy)
def test_atm_managedby_setter(instance):
    original = instance.managedby
    instance.managedby = original
    assert instance.managedby == original



@given(instance=ATM_strategy)
def test_atm_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Bank_strategy)
@settings(max_examples=50)
def test_bank_instantiation(instance):
    assert isinstance(instance, Bank)



@given(instance=Bank_strategy)
def test_bank_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=Bank_strategy)
def test_bank_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original
