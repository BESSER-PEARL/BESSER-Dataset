import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_Contact,
    test_Address,
    test_Person,
    ContactType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_contact_is_not_abstract():
    assert not inspect.isabstract(test_Contact)


def test_test_contact_constructor_exists():
    assert callable(test_Contact.__init__)


def test_test_contact_constructor_args():
    sig = inspect.signature(test_Contact.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_test_contact_has_value():
    assert hasattr(test_Contact, "value")
    descriptor = None
    for klass in test_Contact.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_test_contact_has_type():
    assert hasattr(test_Contact, "type")
    descriptor = None
    for klass in test_Contact.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_test_address_is_not_abstract():
    assert not inspect.isabstract(test_Address)


def test_test_address_constructor_exists():
    assert callable(test_Address.__init__)


def test_test_address_constructor_args():
    sig = inspect.signature(test_Address.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "street" in params, "Missing parameter 'street'"

def test_test_address_has_city():
    assert hasattr(test_Address, "city")
    descriptor = None
    for klass in test_Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_test_address_has_street():
    assert hasattr(test_Address, "street")
    descriptor = None
    for klass in test_Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)



def test_test_person_is_not_abstract():
    assert not inspect.isabstract(test_Person)


def test_test_person_constructor_exists():
    assert callable(test_Person.__init__)


def test_test_person_constructor_args():
    sig = inspect.signature(test_Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_test_person_has_lastname():
    assert hasattr(test_Person, "lastname")
    descriptor = None
    for klass in test_Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_test_person_has_firstname():
    assert hasattr(test_Person, "firstname")
    descriptor = None
    for klass in test_Person.__mro__:
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
test_Contact_strategy = st.builds(
    test_Contact,
    value=
        safe_text,
    type=
        safe_text
)
test_Address_strategy = st.builds(
    test_Address,
    city=
        safe_text,
    street=
        safe_text
)
test_Person_strategy = st.builds(
    test_Person,
    lastname=
        safe_text,
    firstname=
        safe_text
)

@given(instance=test_Contact_strategy)
@settings(max_examples=50)
def test_test_contact_instantiation(instance):
    assert isinstance(instance, test_Contact)



@given(instance=test_Contact_strategy)
def test_test_contact_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=test_Contact_strategy)
def test_test_contact_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=test_Address_strategy)
@settings(max_examples=50)
def test_test_address_instantiation(instance):
    assert isinstance(instance, test_Address)



@given(instance=test_Address_strategy)
def test_test_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=test_Address_strategy)
def test_test_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=test_Person_strategy)
@settings(max_examples=50)
def test_test_person_instantiation(instance):
    assert isinstance(instance, test_Person)



@given(instance=test_Person_strategy)
def test_test_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=test_Person_strategy)
def test_test_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original
