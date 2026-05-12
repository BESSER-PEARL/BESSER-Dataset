import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    demo_model_Employee,
    demo_model_Company,
    demo_model_Address,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_demo_model_employee_is_not_abstract():
    assert not inspect.isabstract(demo_model_Employee)


def test_demo_model_employee_constructor_exists():
    assert callable(demo_model_Employee.__init__)


def test_demo_model_employee_constructor_args():
    sig = inspect.signature(demo_model_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "position" in params, "Missing parameter 'position'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "birthday" in params, "Missing parameter 'birthday'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_demo_model_employee_has_email():
    assert hasattr(demo_model_Employee, "email")
    descriptor = None
    for klass in demo_model_Employee.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_demo_model_employee_has_phone():
    assert hasattr(demo_model_Employee, "phone")
    descriptor = None
    for klass in demo_model_Employee.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_demo_model_employee_has_position():
    assert hasattr(demo_model_Employee, "position")
    descriptor = None
    for klass in demo_model_Employee.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_demo_model_employee_has_lastname():
    assert hasattr(demo_model_Employee, "lastname")
    descriptor = None
    for klass in demo_model_Employee.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_demo_model_employee_has_birthday():
    assert hasattr(demo_model_Employee, "birthday")
    descriptor = None
    for klass in demo_model_Employee.__mro__:
        if "birthday" in klass.__dict__:
            descriptor = klass.__dict__["birthday"]
            break
    assert isinstance(descriptor, property)

def test_demo_model_employee_has_firstname():
    assert hasattr(demo_model_Employee, "firstname")
    descriptor = None
    for klass in demo_model_Employee.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)



def test_demo_model_company_is_not_abstract():
    assert not inspect.isabstract(demo_model_Company)


def test_demo_model_company_constructor_exists():
    assert callable(demo_model_Company.__init__)


def test_demo_model_company_constructor_args():
    sig = inspect.signature(demo_model_Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_demo_model_company_has_name():
    assert hasattr(demo_model_Company, "name")
    descriptor = None
    for klass in demo_model_Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_demo_model_address_is_not_abstract():
    assert not inspect.isabstract(demo_model_Address)


def test_demo_model_address_constructor_exists():
    assert callable(demo_model_Address.__init__)


def test_demo_model_address_constructor_args():
    sig = inspect.signature(demo_model_Address.__init__)
    params = list(sig.parameters.keys())
    assert "street" in params, "Missing parameter 'street'"
    assert "city" in params, "Missing parameter 'city'"
    assert "zipcode" in params, "Missing parameter 'zipcode'"
    assert "country" in params, "Missing parameter 'country'"
    assert "state" in params, "Missing parameter 'state'"

def test_demo_model_address_has_street():
    assert hasattr(demo_model_Address, "street")
    descriptor = None
    for klass in demo_model_Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_demo_model_address_has_city():
    assert hasattr(demo_model_Address, "city")
    descriptor = None
    for klass in demo_model_Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_demo_model_address_has_zipcode():
    assert hasattr(demo_model_Address, "zipcode")
    descriptor = None
    for klass in demo_model_Address.__mro__:
        if "zipcode" in klass.__dict__:
            descriptor = klass.__dict__["zipcode"]
            break
    assert isinstance(descriptor, property)

def test_demo_model_address_has_country():
    assert hasattr(demo_model_Address, "country")
    descriptor = None
    for klass in demo_model_Address.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_demo_model_address_has_state():
    assert hasattr(demo_model_Address, "state")
    descriptor = None
    for klass in demo_model_Address.__mro__:
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
demo_model_Employee_strategy = st.builds(
    demo_model_Employee,
    email=
        safe_text,
    phone=
        safe_text,
    position=
        safe_text,
    lastname=
        safe_text,
    birthday=
        st.dates(),
    firstname=
        safe_text
)
demo_model_Company_strategy = st.builds(
    demo_model_Company,
    name=
        safe_text
)
demo_model_Address_strategy = st.builds(
    demo_model_Address,
    street=
        safe_text,
    city=
        safe_text,
    zipcode=
        st.integers(),
    country=
        safe_text,
    state=
        safe_text
)

@given(instance=demo_model_Employee_strategy)
@settings(max_examples=50)
def test_demo_model_employee_instantiation(instance):
    assert isinstance(instance, demo_model_Employee)



@given(instance=demo_model_Employee_strategy)
def test_demo_model_employee_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=demo_model_Employee_strategy)
def test_demo_model_employee_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=demo_model_Employee_strategy)
def test_demo_model_employee_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=demo_model_Employee_strategy)
def test_demo_model_employee_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=demo_model_Employee_strategy)
def test_demo_model_employee_birthday_setter(instance):
    original = instance.birthday
    instance.birthday = original
    assert instance.birthday == original



@given(instance=demo_model_Employee_strategy)
def test_demo_model_employee_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=demo_model_Company_strategy)
@settings(max_examples=50)
def test_demo_model_company_instantiation(instance):
    assert isinstance(instance, demo_model_Company)



@given(instance=demo_model_Company_strategy)
def test_demo_model_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=demo_model_Address_strategy)
@settings(max_examples=50)
def test_demo_model_address_instantiation(instance):
    assert isinstance(instance, demo_model_Address)



@given(instance=demo_model_Address_strategy)
def test_demo_model_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=demo_model_Address_strategy)
def test_demo_model_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=demo_model_Address_strategy)
def test_demo_model_address_zipcode_setter(instance):
    original = instance.zipcode
    instance.zipcode = original
    assert instance.zipcode == original



@given(instance=demo_model_Address_strategy)
def test_demo_model_address_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=demo_model_Address_strategy)
def test_demo_model_address_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original
