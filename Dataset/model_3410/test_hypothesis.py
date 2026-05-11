import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::Contact,
    test::Address,
    test::Person,
    ContactType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::contact_is_not_abstract():
    assert not inspect.isabstract(test::Contact)


def test_test::contact_constructor_exists():
    assert callable(test::Contact.__init__)


def test_test::contact_constructor_args():
    sig = inspect.signature(test::Contact.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_test::contact_has_value():
    assert hasattr(test::Contact, "value")
    descriptor = None
    for klass in test::Contact.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_test::contact_has_type():
    assert hasattr(test::Contact, "type")
    descriptor = None
    for klass in test::Contact.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_test::address_is_not_abstract():
    assert not inspect.isabstract(test::Address)


def test_test::address_constructor_exists():
    assert callable(test::Address.__init__)


def test_test::address_constructor_args():
    sig = inspect.signature(test::Address.__init__)
    params = list(sig.parameters.keys())
    assert "street" in params, "Missing parameter 'street'"
    assert "city" in params, "Missing parameter 'city'"

def test_test::address_has_street():
    assert hasattr(test::Address, "street")
    descriptor = None
    for klass in test::Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_test::address_has_city():
    assert hasattr(test::Address, "city")
    descriptor = None
    for klass in test::Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)



def test_test::person_is_not_abstract():
    assert not inspect.isabstract(test::Person)


def test_test::person_constructor_exists():
    assert callable(test::Person.__init__)


def test_test::person_constructor_args():
    sig = inspect.signature(test::Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_test::person_has_lastname():
    assert hasattr(test::Person, "lastname")
    descriptor = None
    for klass in test::Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_test::person_has_firstname():
    assert hasattr(test::Person, "firstname")
    descriptor = None
    for klass in test::Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_contacttype_exists():
    # Check that the Enumeration exists
    assert ContactType is not None

def test_contacttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContactType]
    expected_literals = [
        "EMAIL",
        "PHONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContactType"


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
test::Contact_strategy = st.builds(
    test::Contact,
    value=
        safe_text,
    type=
        safe_text
)
test::Address_strategy = st.builds(
    test::Address,
    street=
        safe_text,
    city=
        safe_text
)
test::Person_strategy = st.builds(
    test::Person,
    lastname=
        safe_text,
    firstname=
        safe_text
)

@given(instance=test::Contact_strategy)
@settings(max_examples=50)
def test_test::contact_instantiation(instance):
    assert isinstance(instance, test::Contact)

@given(instance=test::Contact_strategy)
def test_test::contact_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=test::Contact_strategy)
def test_test::contact_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=test::Contact_strategy)
def test_test::contact_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=test::Contact_strategy)
def test_test::contact_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=test::Address_strategy)
@settings(max_examples=50)
def test_test::address_instantiation(instance):
    assert isinstance(instance, test::Address)

@given(instance=test::Address_strategy)
def test_test::address_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=test::Address_strategy)
def test_test::address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=test::Address_strategy)
def test_test::address_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=test::Address_strategy)
def test_test::address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=test::Person_strategy)
@settings(max_examples=50)
def test_test::person_instantiation(instance):
    assert isinstance(instance, test::Person)

@given(instance=test::Person_strategy)
def test_test::person_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=test::Person_strategy)
def test_test::person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=test::Person_strategy)
def test_test::person_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=test::Person_strategy)
def test_test::person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original
