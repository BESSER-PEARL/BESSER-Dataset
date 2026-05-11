import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    demo::model::Employee,
    demo::model::Company,
    demo::model::Address,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_demo::model::employee_is_not_abstract():
    assert not inspect.isabstract(demo::model::Employee)


def test_demo::model::employee_constructor_exists():
    assert callable(demo::model::Employee.__init__)


def test_demo::model::employee_constructor_args():
    sig = inspect.signature(demo::model::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "birthday" in params, "Missing parameter 'birthday'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "position" in params, "Missing parameter 'position'"
    assert "email" in params, "Missing parameter 'email'"

def test_demo::model::employee_has_firstname():
    assert hasattr(demo::model::Employee, "firstname")
    descriptor = None
    for klass in demo::model::Employee.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_demo::model::employee_has_birthday():
    assert hasattr(demo::model::Employee, "birthday")
    descriptor = None
    for klass in demo::model::Employee.__mro__:
        if "birthday" in klass.__dict__:
            descriptor = klass.__dict__["birthday"]
            break
    assert isinstance(descriptor, property)

def test_demo::model::employee_has_lastname():
    assert hasattr(demo::model::Employee, "lastname")
    descriptor = None
    for klass in demo::model::Employee.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_demo::model::employee_has_phone():
    assert hasattr(demo::model::Employee, "phone")
    descriptor = None
    for klass in demo::model::Employee.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_demo::model::employee_has_position():
    assert hasattr(demo::model::Employee, "position")
    descriptor = None
    for klass in demo::model::Employee.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_demo::model::employee_has_email():
    assert hasattr(demo::model::Employee, "email")
    descriptor = None
    for klass in demo::model::Employee.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_demo::model::company_is_not_abstract():
    assert not inspect.isabstract(demo::model::Company)


def test_demo::model::company_constructor_exists():
    assert callable(demo::model::Company.__init__)


def test_demo::model::company_constructor_args():
    sig = inspect.signature(demo::model::Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_demo::model::company_has_name():
    assert hasattr(demo::model::Company, "name")
    descriptor = None
    for klass in demo::model::Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_demo::model::address_is_not_abstract():
    assert not inspect.isabstract(demo::model::Address)


def test_demo::model::address_constructor_exists():
    assert callable(demo::model::Address.__init__)


def test_demo::model::address_constructor_args():
    sig = inspect.signature(demo::model::Address.__init__)
    params = list(sig.parameters.keys())
    assert "country" in params, "Missing parameter 'country'"
    assert "zipcode" in params, "Missing parameter 'zipcode'"
    assert "street" in params, "Missing parameter 'street'"
    assert "city" in params, "Missing parameter 'city'"
    assert "state" in params, "Missing parameter 'state'"

def test_demo::model::address_has_country():
    assert hasattr(demo::model::Address, "country")
    descriptor = None
    for klass in demo::model::Address.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_demo::model::address_has_zipcode():
    assert hasattr(demo::model::Address, "zipcode")
    descriptor = None
    for klass in demo::model::Address.__mro__:
        if "zipcode" in klass.__dict__:
            descriptor = klass.__dict__["zipcode"]
            break
    assert isinstance(descriptor, property)

def test_demo::model::address_has_street():
    assert hasattr(demo::model::Address, "street")
    descriptor = None
    for klass in demo::model::Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_demo::model::address_has_city():
    assert hasattr(demo::model::Address, "city")
    descriptor = None
    for klass in demo::model::Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_demo::model::address_has_state():
    assert hasattr(demo::model::Address, "state")
    descriptor = None
    for klass in demo::model::Address.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
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
demo::model::Employee_strategy = st.builds(
    demo::model::Employee,
    firstname=
        safe_text,
    birthday=
        st.dates(),
    lastname=
        safe_text,
    phone=
        safe_text,
    position=
        safe_text,
    email=
        safe_text
)
demo::model::Company_strategy = st.builds(
    demo::model::Company,
    name=
        safe_text
)
demo::model::Address_strategy = st.builds(
    demo::model::Address,
    country=
        safe_text,
    zipcode=
        st.integers(),
    street=
        safe_text,
    city=
        safe_text,
    state=
        safe_text
)

@given(instance=demo::model::Employee_strategy)
@settings(max_examples=50)
def test_demo::model::employee_instantiation(instance):
    assert isinstance(instance, demo::model::Employee)

@given(instance=demo::model::Employee_strategy)
def test_demo::model::employee_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=demo::model::Employee_strategy)
def test_demo::model::employee_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=demo::model::Employee_strategy)
def test_demo::model::employee_birthday_type(instance):
    assert isinstance(instance.birthday, date)


@given(instance=demo::model::Employee_strategy)
def test_demo::model::employee_birthday_setter(instance):
    original = instance.birthday
    instance.birthday = original
    assert instance.birthday == original

@given(instance=demo::model::Employee_strategy)
def test_demo::model::employee_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=demo::model::Employee_strategy)
def test_demo::model::employee_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=demo::model::Employee_strategy)
def test_demo::model::employee_phone_type(instance):
    assert isinstance(instance.phone, str)


@given(instance=demo::model::Employee_strategy)
def test_demo::model::employee_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original

@given(instance=demo::model::Employee_strategy)
def test_demo::model::employee_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=demo::model::Employee_strategy)
def test_demo::model::employee_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=demo::model::Employee_strategy)
def test_demo::model::employee_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=demo::model::Employee_strategy)
def test_demo::model::employee_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=demo::model::Company_strategy)
@settings(max_examples=50)
def test_demo::model::company_instantiation(instance):
    assert isinstance(instance, demo::model::Company)

@given(instance=demo::model::Company_strategy)
def test_demo::model::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=demo::model::Company_strategy)
def test_demo::model::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=demo::model::Address_strategy)
@settings(max_examples=50)
def test_demo::model::address_instantiation(instance):
    assert isinstance(instance, demo::model::Address)

@given(instance=demo::model::Address_strategy)
def test_demo::model::address_country_type(instance):
    assert isinstance(instance.country, str)


@given(instance=demo::model::Address_strategy)
def test_demo::model::address_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original

@given(instance=demo::model::Address_strategy)
def test_demo::model::address_zipcode_type(instance):
    assert isinstance(instance.zipcode, int)


@given(instance=demo::model::Address_strategy)
def test_demo::model::address_zipcode_setter(instance):
    original = instance.zipcode
    instance.zipcode = original
    assert instance.zipcode == original

@given(instance=demo::model::Address_strategy)
def test_demo::model::address_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=demo::model::Address_strategy)
def test_demo::model::address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=demo::model::Address_strategy)
def test_demo::model::address_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=demo::model::Address_strategy)
def test_demo::model::address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=demo::model::Address_strategy)
def test_demo::model::address_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=demo::model::Address_strategy)
def test_demo::model::address_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original
