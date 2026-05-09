import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    contacts::UoD,
    contacts::AddressBook,
    contacts::PhoneNumber,
    contacts::Address,
    contacts::Contact,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_contacts::uod_is_not_abstract():
    assert not inspect.isabstract(contacts::UoD)


def test_contacts::uod_constructor_exists():
    assert callable(contacts::UoD.__init__)


def test_contacts::uod_constructor_args():
    sig = inspect.signature(contacts::UoD.__init__)
    params = list(sig.parameters.keys())



def test_contacts::addressbook_is_not_abstract():
    assert not inspect.isabstract(contacts::AddressBook)


def test_contacts::addressbook_constructor_exists():
    assert callable(contacts::AddressBook.__init__)


def test_contacts::addressbook_constructor_args():
    sig = inspect.signature(contacts::AddressBook.__init__)
    params = list(sig.parameters.keys())



def test_contacts::phonenumber_is_not_abstract():
    assert not inspect.isabstract(contacts::PhoneNumber)


def test_contacts::phonenumber_constructor_exists():
    assert callable(contacts::PhoneNumber.__init__)


def test_contacts::phonenumber_constructor_args():
    sig = inspect.signature(contacts::PhoneNumber.__init__)
    params = list(sig.parameters.keys())
    assert "country" in params, "Missing parameter 'country'"
    assert "number" in params, "Missing parameter 'number'"

def test_contacts::phonenumber_has_country():
    assert hasattr(contacts::PhoneNumber, "country")
    descriptor = None
    for klass in contacts::PhoneNumber.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_contacts::phonenumber_has_number():
    assert hasattr(contacts::PhoneNumber, "number")
    descriptor = None
    for klass in contacts::PhoneNumber.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_contacts::address_is_not_abstract():
    assert not inspect.isabstract(contacts::Address)


def test_contacts::address_constructor_exists():
    assert callable(contacts::Address.__init__)


def test_contacts::address_constructor_args():
    sig = inspect.signature(contacts::Address.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "state" in params, "Missing parameter 'state'"
    assert "country" in params, "Missing parameter 'country'"
    assert "street" in params, "Missing parameter 'street'"
    assert "zipCode" in params, "Missing parameter 'zipCode'"

def test_contacts::address_has_city():
    assert hasattr(contacts::Address, "city")
    descriptor = None
    for klass in contacts::Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_contacts::address_has_state():
    assert hasattr(contacts::Address, "state")
    descriptor = None
    for klass in contacts::Address.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_contacts::address_has_country():
    assert hasattr(contacts::Address, "country")
    descriptor = None
    for klass in contacts::Address.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_contacts::address_has_street():
    assert hasattr(contacts::Address, "street")
    descriptor = None
    for klass in contacts::Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_contacts::address_has_zipCode():
    assert hasattr(contacts::Address, "zipCode")
    descriptor = None
    for klass in contacts::Address.__mro__:
        if "zipCode" in klass.__dict__:
            descriptor = klass.__dict__["zipCode"]
            break
    assert isinstance(descriptor, property)



def test_contacts::contact_is_not_abstract():
    assert not inspect.isabstract(contacts::Contact)


def test_contacts::contact_constructor_exists():
    assert callable(contacts::Contact.__init__)


def test_contacts::contact_constructor_args():
    sig = inspect.signature(contacts::Contact.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "jobTitle" in params, "Missing parameter 'jobTitle'"
    assert "image" in params, "Missing parameter 'image'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "title" in params, "Missing parameter 'title'"
    assert "company" in params, "Missing parameter 'company'"
    assert "middleName" in params, "Missing parameter 'middleName'"
    assert "email" in params, "Missing parameter 'email'"
    assert "note" in params, "Missing parameter 'note'"
    assert "webPage" in params, "Missing parameter 'webPage'"

def test_contacts::contact_has_lastName():
    assert hasattr(contacts::Contact, "lastName")
    descriptor = None
    for klass in contacts::Contact.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_contacts::contact_has_jobTitle():
    assert hasattr(contacts::Contact, "jobTitle")
    descriptor = None
    for klass in contacts::Contact.__mro__:
        if "jobTitle" in klass.__dict__:
            descriptor = klass.__dict__["jobTitle"]
            break
    assert isinstance(descriptor, property)

def test_contacts::contact_has_image():
    assert hasattr(contacts::Contact, "image")
    descriptor = None
    for klass in contacts::Contact.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_contacts::contact_has_firstName():
    assert hasattr(contacts::Contact, "firstName")
    descriptor = None
    for klass in contacts::Contact.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_contacts::contact_has_title():
    assert hasattr(contacts::Contact, "title")
    descriptor = None
    for klass in contacts::Contact.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_contacts::contact_has_company():
    assert hasattr(contacts::Contact, "company")
    descriptor = None
    for klass in contacts::Contact.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_contacts::contact_has_middleName():
    assert hasattr(contacts::Contact, "middleName")
    descriptor = None
    for klass in contacts::Contact.__mro__:
        if "middleName" in klass.__dict__:
            descriptor = klass.__dict__["middleName"]
            break
    assert isinstance(descriptor, property)

def test_contacts::contact_has_email():
    assert hasattr(contacts::Contact, "email")
    descriptor = None
    for klass in contacts::Contact.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_contacts::contact_has_note():
    assert hasattr(contacts::Contact, "note")
    descriptor = None
    for klass in contacts::Contact.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_contacts::contact_has_webPage():
    assert hasattr(contacts::Contact, "webPage")
    descriptor = None
    for klass in contacts::Contact.__mro__:
        if "webPage" in klass.__dict__:
            descriptor = klass.__dict__["webPage"]
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
contacts::UoD_strategy = st.builds(
    contacts::UoD,
)
contacts::AddressBook_strategy = st.builds(
    contacts::AddressBook,
)
contacts::PhoneNumber_strategy = st.builds(
    contacts::PhoneNumber,
    country=
        safe_text,
    number=
        safe_text
)
contacts::Address_strategy = st.builds(
    contacts::Address,
    city=
        safe_text,
    state=
        safe_text,
    country=
        safe_text,
    street=
        safe_text,
    zipCode=
        safe_text
)
contacts::Contact_strategy = st.builds(
    contacts::Contact,
    lastName=
        safe_text,
    jobTitle=
        safe_text,
    image=
        safe_text,
    firstName=
        safe_text,
    title=
        safe_text,
    company=
        safe_text,
    middleName=
        safe_text,
    email=
        safe_text,
    note=
        safe_text,
    webPage=
        safe_text
)

@given(instance=contacts::UoD_strategy)
@settings(max_examples=50)
def test_contacts::uod_instantiation(instance):
    assert isinstance(instance, contacts::UoD)

@given(instance=contacts::AddressBook_strategy)
@settings(max_examples=50)
def test_contacts::addressbook_instantiation(instance):
    assert isinstance(instance, contacts::AddressBook)

@given(instance=contacts::PhoneNumber_strategy)
@settings(max_examples=50)
def test_contacts::phonenumber_instantiation(instance):
    assert isinstance(instance, contacts::PhoneNumber)

@given(instance=contacts::PhoneNumber_strategy)
def test_contacts::phonenumber_country_type(instance):
    assert isinstance(instance.country, str)


@given(instance=contacts::PhoneNumber_strategy)
def test_contacts::phonenumber_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original

@given(instance=contacts::PhoneNumber_strategy)
def test_contacts::phonenumber_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=contacts::PhoneNumber_strategy)
def test_contacts::phonenumber_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=contacts::Address_strategy)
@settings(max_examples=50)
def test_contacts::address_instantiation(instance):
    assert isinstance(instance, contacts::Address)

@given(instance=contacts::Address_strategy)
def test_contacts::address_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=contacts::Address_strategy)
def test_contacts::address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=contacts::Address_strategy)
def test_contacts::address_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=contacts::Address_strategy)
def test_contacts::address_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=contacts::Address_strategy)
def test_contacts::address_country_type(instance):
    assert isinstance(instance.country, str)


@given(instance=contacts::Address_strategy)
def test_contacts::address_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original

@given(instance=contacts::Address_strategy)
def test_contacts::address_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=contacts::Address_strategy)
def test_contacts::address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=contacts::Address_strategy)
def test_contacts::address_zipCode_type(instance):
    assert isinstance(instance.zipCode, str)


@given(instance=contacts::Address_strategy)
def test_contacts::address_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original

@given(instance=contacts::Contact_strategy)
@settings(max_examples=50)
def test_contacts::contact_instantiation(instance):
    assert isinstance(instance, contacts::Contact)

@given(instance=contacts::Contact_strategy)
def test_contacts::contact_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=contacts::Contact_strategy)
def test_contacts::contact_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=contacts::Contact_strategy)
def test_contacts::contact_jobTitle_type(instance):
    assert isinstance(instance.jobTitle, str)


@given(instance=contacts::Contact_strategy)
def test_contacts::contact_jobTitle_setter(instance):
    original = instance.jobTitle
    instance.jobTitle = original
    assert instance.jobTitle == original

@given(instance=contacts::Contact_strategy)
def test_contacts::contact_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=contacts::Contact_strategy)
def test_contacts::contact_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=contacts::Contact_strategy)
def test_contacts::contact_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=contacts::Contact_strategy)
def test_contacts::contact_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=contacts::Contact_strategy)
def test_contacts::contact_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=contacts::Contact_strategy)
def test_contacts::contact_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=contacts::Contact_strategy)
def test_contacts::contact_company_type(instance):
    assert isinstance(instance.company, str)


@given(instance=contacts::Contact_strategy)
def test_contacts::contact_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original

@given(instance=contacts::Contact_strategy)
def test_contacts::contact_middleName_type(instance):
    assert isinstance(instance.middleName, str)


@given(instance=contacts::Contact_strategy)
def test_contacts::contact_middleName_setter(instance):
    original = instance.middleName
    instance.middleName = original
    assert instance.middleName == original

@given(instance=contacts::Contact_strategy)
def test_contacts::contact_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=contacts::Contact_strategy)
def test_contacts::contact_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=contacts::Contact_strategy)
def test_contacts::contact_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=contacts::Contact_strategy)
def test_contacts::contact_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=contacts::Contact_strategy)
def test_contacts::contact_webPage_type(instance):
    assert isinstance(instance.webPage, str)


@given(instance=contacts::Contact_strategy)
def test_contacts::contact_webPage_setter(instance):
    original = instance.webPage
    instance.webPage = original
    assert instance.webPage == original
