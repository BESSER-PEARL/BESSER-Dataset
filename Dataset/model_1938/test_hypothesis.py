import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    addressbook::FederalState,
    addressbook::Address,
    addressbook::Country,
    addressbook::Person,
    addressbook::AddressBook,
    AddressType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_addressbook::federalstate_is_not_abstract():
    assert not inspect.isabstract(addressbook::FederalState)


def test_addressbook::federalstate_constructor_exists():
    assert callable(addressbook::FederalState.__init__)


def test_addressbook::federalstate_constructor_args():
    sig = inspect.signature(addressbook::FederalState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_addressbook::federalstate_has_name():
    assert hasattr(addressbook::FederalState, "name")
    descriptor = None
    for klass in addressbook::FederalState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_addressbook::address_is_not_abstract():
    assert not inspect.isabstract(addressbook::Address)


def test_addressbook::address_constructor_exists():
    assert callable(addressbook::Address.__init__)


def test_addressbook::address_constructor_args():
    sig = inspect.signature(addressbook::Address.__init__)
    params = list(sig.parameters.keys())
    assert "street" in params, "Missing parameter 'street'"
    assert "city" in params, "Missing parameter 'city'"
    assert "zip" in params, "Missing parameter 'zip'"
    assert "type" in params, "Missing parameter 'type'"

def test_addressbook::address_has_street():
    assert hasattr(addressbook::Address, "street")
    descriptor = None
    for klass in addressbook::Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_addressbook::address_has_city():
    assert hasattr(addressbook::Address, "city")
    descriptor = None
    for klass in addressbook::Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_addressbook::address_has_zip():
    assert hasattr(addressbook::Address, "zip")
    descriptor = None
    for klass in addressbook::Address.__mro__:
        if "zip" in klass.__dict__:
            descriptor = klass.__dict__["zip"]
            break
    assert isinstance(descriptor, property)

def test_addressbook::address_has_type():
    assert hasattr(addressbook::Address, "type")
    descriptor = None
    for klass in addressbook::Address.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_addressbook::country_is_not_abstract():
    assert not inspect.isabstract(addressbook::Country)


def test_addressbook::country_constructor_exists():
    assert callable(addressbook::Country.__init__)


def test_addressbook::country_constructor_args():
    sig = inspect.signature(addressbook::Country.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_addressbook::country_has_name():
    assert hasattr(addressbook::Country, "name")
    descriptor = None
    for klass in addressbook::Country.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_addressbook::person_is_not_abstract():
    assert not inspect.isabstract(addressbook::Person)


def test_addressbook::person_constructor_exists():
    assert callable(addressbook::Person.__init__)


def test_addressbook::person_constructor_args():
    sig = inspect.signature(addressbook::Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_addressbook::person_has_lastname():
    assert hasattr(addressbook::Person, "lastname")
    descriptor = None
    for klass in addressbook::Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_addressbook::person_has_firstname():
    assert hasattr(addressbook::Person, "firstname")
    descriptor = None
    for klass in addressbook::Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)



def test_addressbook::addressbook_is_not_abstract():
    assert not inspect.isabstract(addressbook::AddressBook)


def test_addressbook::addressbook_constructor_exists():
    assert callable(addressbook::AddressBook.__init__)


def test_addressbook::addressbook_constructor_args():
    sig = inspect.signature(addressbook::AddressBook.__init__)
    params = list(sig.parameters.keys())

def test_addresstype_exists():
    # Check that the Enumeration exists
    assert AddressType is not None

def test_addresstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AddressType]
    expected_literals = [
        "PRIVATE",
        "BUSINESS",
        "DELIVERY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AddressType"


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
addressbook::FederalState_strategy = st.builds(
    addressbook::FederalState,
    name=
        safe_text
)
addressbook::Address_strategy = st.builds(
    addressbook::Address,
    street=
        safe_text,
    city=
        safe_text,
    zip=
        safe_text,
    type=
        safe_text
)
addressbook::Country_strategy = st.builds(
    addressbook::Country,
    name=
        safe_text
)
addressbook::Person_strategy = st.builds(
    addressbook::Person,
    lastname=
        safe_text,
    firstname=
        safe_text
)
addressbook::AddressBook_strategy = st.builds(
    addressbook::AddressBook,
)

@given(instance=addressbook::FederalState_strategy)
@settings(max_examples=50)
def test_addressbook::federalstate_instantiation(instance):
    assert isinstance(instance, addressbook::FederalState)

@given(instance=addressbook::FederalState_strategy)
def test_addressbook::federalstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=addressbook::FederalState_strategy)
def test_addressbook::federalstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=addressbook::Address_strategy)
@settings(max_examples=50)
def test_addressbook::address_instantiation(instance):
    assert isinstance(instance, addressbook::Address)

@given(instance=addressbook::Address_strategy)
def test_addressbook::address_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=addressbook::Address_strategy)
def test_addressbook::address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=addressbook::Address_strategy)
def test_addressbook::address_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=addressbook::Address_strategy)
def test_addressbook::address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=addressbook::Address_strategy)
def test_addressbook::address_zip_type(instance):
    assert isinstance(instance.zip, str)


@given(instance=addressbook::Address_strategy)
def test_addressbook::address_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original

@given(instance=addressbook::Address_strategy)
def test_addressbook::address_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=addressbook::Address_strategy)
def test_addressbook::address_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=addressbook::Country_strategy)
@settings(max_examples=50)
def test_addressbook::country_instantiation(instance):
    assert isinstance(instance, addressbook::Country)

@given(instance=addressbook::Country_strategy)
def test_addressbook::country_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=addressbook::Country_strategy)
def test_addressbook::country_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=addressbook::Person_strategy)
@settings(max_examples=50)
def test_addressbook::person_instantiation(instance):
    assert isinstance(instance, addressbook::Person)

@given(instance=addressbook::Person_strategy)
def test_addressbook::person_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=addressbook::Person_strategy)
def test_addressbook::person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=addressbook::Person_strategy)
def test_addressbook::person_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=addressbook::Person_strategy)
def test_addressbook::person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=addressbook::AddressBook_strategy)
@settings(max_examples=50)
def test_addressbook::addressbook_instantiation(instance):
    assert isinstance(instance, addressbook::AddressBook)
