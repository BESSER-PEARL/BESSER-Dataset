import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    addressbook_FederalState,
    addressbook_Person,
    addressbook_AddressBook,
    addressbook_Address,
    addressbook_Country,
    AddressType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_addressbook_federalstate_is_not_abstract():
    assert not inspect.isabstract(addressbook_FederalState)


def test_addressbook_federalstate_constructor_exists():
    assert callable(addressbook_FederalState.__init__)


def test_addressbook_federalstate_constructor_args():
    sig = inspect.signature(addressbook_FederalState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_addressbook_federalstate_has_name():
    assert hasattr(addressbook_FederalState, "name")
    descriptor = None
    for klass in addressbook_FederalState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_addressbook_person_is_not_abstract():
    assert not inspect.isabstract(addressbook_Person)


def test_addressbook_person_constructor_exists():
    assert callable(addressbook_Person.__init__)


def test_addressbook_person_constructor_args():
    sig = inspect.signature(addressbook_Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_addressbook_person_has_lastname():
    assert hasattr(addressbook_Person, "lastname")
    descriptor = None
    for klass in addressbook_Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_addressbook_person_has_firstname():
    assert hasattr(addressbook_Person, "firstname")
    descriptor = None
    for klass in addressbook_Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)



def test_addressbook_addressbook_is_not_abstract():
    assert not inspect.isabstract(addressbook_AddressBook)


def test_addressbook_addressbook_constructor_exists():
    assert callable(addressbook_AddressBook.__init__)


def test_addressbook_addressbook_constructor_args():
    sig = inspect.signature(addressbook_AddressBook.__init__)
    params = list(sig.parameters.keys())



def test_addressbook_address_is_not_abstract():
    assert not inspect.isabstract(addressbook_Address)


def test_addressbook_address_constructor_exists():
    assert callable(addressbook_Address.__init__)


def test_addressbook_address_constructor_args():
    sig = inspect.signature(addressbook_Address.__init__)
    params = list(sig.parameters.keys())
    assert "zip" in params, "Missing parameter 'zip'"
    assert "type" in params, "Missing parameter 'type'"
    assert "street" in params, "Missing parameter 'street'"
    assert "city" in params, "Missing parameter 'city'"

def test_addressbook_address_has_zip():
    assert hasattr(addressbook_Address, "zip")
    descriptor = None
    for klass in addressbook_Address.__mro__:
        if "zip" in klass.__dict__:
            descriptor = klass.__dict__["zip"]
            break
    assert isinstance(descriptor, property)

def test_addressbook_address_has_type():
    assert hasattr(addressbook_Address, "type")
    descriptor = None
    for klass in addressbook_Address.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_addressbook_address_has_street():
    assert hasattr(addressbook_Address, "street")
    descriptor = None
    for klass in addressbook_Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_addressbook_address_has_city():
    assert hasattr(addressbook_Address, "city")
    descriptor = None
    for klass in addressbook_Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)



def test_addressbook_country_is_not_abstract():
    assert not inspect.isabstract(addressbook_Country)


def test_addressbook_country_constructor_exists():
    assert callable(addressbook_Country.__init__)


def test_addressbook_country_constructor_args():
    sig = inspect.signature(addressbook_Country.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_addressbook_country_has_name():
    assert hasattr(addressbook_Country, "name")
    descriptor = None
    for klass in addressbook_Country.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_addresstype_exists():
    # Check that the Enumeration exists
    assert AddressType is not None

def test_addresstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AddressType]
    expected_literals = [
        "DELIVERY",
        "BUSINESS",
        "PRIVATE",
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
addressbook_FederalState_strategy = st.builds(
    addressbook_FederalState,
    name=
        safe_text
)
addressbook_Person_strategy = st.builds(
    addressbook_Person,
    lastname=
        safe_text,
    firstname=
        safe_text
)
addressbook_AddressBook_strategy = st.builds(
    addressbook_AddressBook,
)
addressbook_Address_strategy = st.builds(
    addressbook_Address,
    zip=
        safe_text,
    type=
        safe_text,
    street=
        safe_text,
    city=
        safe_text
)
addressbook_Country_strategy = st.builds(
    addressbook_Country,
    name=
        safe_text
)

@given(instance=addressbook_FederalState_strategy)
@settings(max_examples=50)
def test_addressbook_federalstate_instantiation(instance):
    assert isinstance(instance, addressbook_FederalState)



@given(instance=addressbook_FederalState_strategy)
def test_addressbook_federalstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=addressbook_Person_strategy)
@settings(max_examples=50)
def test_addressbook_person_instantiation(instance):
    assert isinstance(instance, addressbook_Person)



@given(instance=addressbook_Person_strategy)
def test_addressbook_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=addressbook_Person_strategy)
def test_addressbook_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=addressbook_AddressBook_strategy)
@settings(max_examples=50)
def test_addressbook_addressbook_instantiation(instance):
    assert isinstance(instance, addressbook_AddressBook)

@given(instance=addressbook_Address_strategy)
@settings(max_examples=50)
def test_addressbook_address_instantiation(instance):
    assert isinstance(instance, addressbook_Address)



@given(instance=addressbook_Address_strategy)
def test_addressbook_address_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original



@given(instance=addressbook_Address_strategy)
def test_addressbook_address_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=addressbook_Address_strategy)
def test_addressbook_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=addressbook_Address_strategy)
def test_addressbook_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=addressbook_Country_strategy)
@settings(max_examples=50)
def test_addressbook_country_instantiation(instance):
    assert isinstance(instance, addressbook_Country)



@given(instance=addressbook_Country_strategy)
def test_addressbook_country_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
