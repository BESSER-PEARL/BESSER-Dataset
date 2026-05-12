import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    contacts_UoD,
    contacts_AddressBook,
    contacts_PhoneNumber,
    contacts_Address,
    contacts_Contact,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_contacts_uod_is_not_abstract():
    assert not inspect.isabstract(contacts_UoD)


def test_contacts_uod_constructor_exists():
    assert callable(contacts_UoD.__init__)


def test_contacts_uod_constructor_args():
    sig = inspect.signature(contacts_UoD.__init__)
    params = list(sig.parameters.keys())



def test_contacts_addressbook_is_not_abstract():
    assert not inspect.isabstract(contacts_AddressBook)


def test_contacts_addressbook_constructor_exists():
    assert callable(contacts_AddressBook.__init__)


def test_contacts_addressbook_constructor_args():
    sig = inspect.signature(contacts_AddressBook.__init__)
    params = list(sig.parameters.keys())



def test_contacts_phonenumber_is_not_abstract():
    assert not inspect.isabstract(contacts_PhoneNumber)


def test_contacts_phonenumber_constructor_exists():
    assert callable(contacts_PhoneNumber.__init__)


def test_contacts_phonenumber_constructor_args():
    sig = inspect.signature(contacts_PhoneNumber.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "country" in params, "Missing parameter 'country'"

def test_contacts_phonenumber_has_number():
    assert hasattr(contacts_PhoneNumber, "number")
    descriptor = None
    for klass in contacts_PhoneNumber.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_contacts_phonenumber_has_country():
    assert hasattr(contacts_PhoneNumber, "country")
    descriptor = None
    for klass in contacts_PhoneNumber.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)



def test_contacts_address_is_not_abstract():
    assert not inspect.isabstract(contacts_Address)


def test_contacts_address_constructor_exists():
    assert callable(contacts_Address.__init__)


def test_contacts_address_constructor_args():
    sig = inspect.signature(contacts_Address.__init__)
    params = list(sig.parameters.keys())
    assert "zipCode" in params, "Missing parameter 'zipCode'"
    assert "city" in params, "Missing parameter 'city'"
    assert "street" in params, "Missing parameter 'street'"
    assert "country" in params, "Missing parameter 'country'"
    assert "state" in params, "Missing parameter 'state'"

def test_contacts_address_has_zipCode():
    assert hasattr(contacts_Address, "zipCode")
    descriptor = None
    for klass in contacts_Address.__mro__:
        if "zipCode" in klass.__dict__:
            descriptor = klass.__dict__["zipCode"]
            break
    assert isinstance(descriptor, property)

def test_contacts_address_has_city():
    assert hasattr(contacts_Address, "city")
    descriptor = None
    for klass in contacts_Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_contacts_address_has_street():
    assert hasattr(contacts_Address, "street")
    descriptor = None
    for klass in contacts_Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_contacts_address_has_country():
    assert hasattr(contacts_Address, "country")
    descriptor = None
    for klass in contacts_Address.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_contacts_address_has_state():
    assert hasattr(contacts_Address, "state")
    descriptor = None
    for klass in contacts_Address.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_contacts_contact_is_not_abstract():
    assert not inspect.isabstract(contacts_Contact)


def test_contacts_contact_constructor_exists():
    assert callable(contacts_Contact.__init__)


def test_contacts_contact_constructor_args():
    sig = inspect.signature(contacts_Contact.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"
    assert "company" in params, "Missing parameter 'company'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "jobTitle" in params, "Missing parameter 'jobTitle'"
    assert "email" in params, "Missing parameter 'email'"
    assert "middleName" in params, "Missing parameter 'middleName'"
    assert "webPage" in params, "Missing parameter 'webPage'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "note" in params, "Missing parameter 'note'"
    assert "title" in params, "Missing parameter 'title'"

def test_contacts_contact_has_image():
    assert hasattr(contacts_Contact, "image")
    descriptor = None
    for klass in contacts_Contact.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_contacts_contact_has_company():
    assert hasattr(contacts_Contact, "company")
    descriptor = None
    for klass in contacts_Contact.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_contacts_contact_has_firstName():
    assert hasattr(contacts_Contact, "firstName")
    descriptor = None
    for klass in contacts_Contact.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_contacts_contact_has_jobTitle():
    assert hasattr(contacts_Contact, "jobTitle")
    descriptor = None
    for klass in contacts_Contact.__mro__:
        if "jobTitle" in klass.__dict__:
            descriptor = klass.__dict__["jobTitle"]
            break
    assert isinstance(descriptor, property)

def test_contacts_contact_has_email():
    assert hasattr(contacts_Contact, "email")
    descriptor = None
    for klass in contacts_Contact.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_contacts_contact_has_middleName():
    assert hasattr(contacts_Contact, "middleName")
    descriptor = None
    for klass in contacts_Contact.__mro__:
        if "middleName" in klass.__dict__:
            descriptor = klass.__dict__["middleName"]
            break
    assert isinstance(descriptor, property)

def test_contacts_contact_has_webPage():
    assert hasattr(contacts_Contact, "webPage")
    descriptor = None
    for klass in contacts_Contact.__mro__:
        if "webPage" in klass.__dict__:
            descriptor = klass.__dict__["webPage"]
            break
    assert isinstance(descriptor, property)

def test_contacts_contact_has_lastName():
    assert hasattr(contacts_Contact, "lastName")
    descriptor = None
    for klass in contacts_Contact.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_contacts_contact_has_note():
    assert hasattr(contacts_Contact, "note")
    descriptor = None
    for klass in contacts_Contact.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_contacts_contact_has_title():
    assert hasattr(contacts_Contact, "title")
    descriptor = None
    for klass in contacts_Contact.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
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
contacts_UoD_strategy = st.builds(
    contacts_UoD,
)
contacts_AddressBook_strategy = st.builds(
    contacts_AddressBook,
)
contacts_PhoneNumber_strategy = st.builds(
    contacts_PhoneNumber,
    number=
        safe_text,
    country=
        safe_text
)
contacts_Address_strategy = st.builds(
    contacts_Address,
    zipCode=
        safe_text,
    city=
        safe_text,
    street=
        safe_text,
    country=
        safe_text,
    state=
        safe_text
)
contacts_Contact_strategy = st.builds(
    contacts_Contact,
    image=
        safe_text,
    company=
        safe_text,
    firstName=
        safe_text,
    jobTitle=
        safe_text,
    email=
        safe_text,
    middleName=
        safe_text,
    webPage=
        safe_text,
    lastName=
        safe_text,
    note=
        safe_text,
    title=
        safe_text
)

@given(instance=contacts_UoD_strategy)
@settings(max_examples=50)
def test_contacts_uod_instantiation(instance):
    assert isinstance(instance, contacts_UoD)

@given(instance=contacts_AddressBook_strategy)
@settings(max_examples=50)
def test_contacts_addressbook_instantiation(instance):
    assert isinstance(instance, contacts_AddressBook)

@given(instance=contacts_PhoneNumber_strategy)
@settings(max_examples=50)
def test_contacts_phonenumber_instantiation(instance):
    assert isinstance(instance, contacts_PhoneNumber)



@given(instance=contacts_PhoneNumber_strategy)
def test_contacts_phonenumber_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=contacts_PhoneNumber_strategy)
def test_contacts_phonenumber_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original

@given(instance=contacts_Address_strategy)
@settings(max_examples=50)
def test_contacts_address_instantiation(instance):
    assert isinstance(instance, contacts_Address)



@given(instance=contacts_Address_strategy)
def test_contacts_address_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original



@given(instance=contacts_Address_strategy)
def test_contacts_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=contacts_Address_strategy)
def test_contacts_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=contacts_Address_strategy)
def test_contacts_address_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=contacts_Address_strategy)
def test_contacts_address_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=contacts_Contact_strategy)
@settings(max_examples=50)
def test_contacts_contact_instantiation(instance):
    assert isinstance(instance, contacts_Contact)



@given(instance=contacts_Contact_strategy)
def test_contacts_contact_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=contacts_Contact_strategy)
def test_contacts_contact_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original



@given(instance=contacts_Contact_strategy)
def test_contacts_contact_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=contacts_Contact_strategy)
def test_contacts_contact_jobTitle_setter(instance):
    original = instance.jobTitle
    instance.jobTitle = original
    assert instance.jobTitle == original



@given(instance=contacts_Contact_strategy)
def test_contacts_contact_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=contacts_Contact_strategy)
def test_contacts_contact_middleName_setter(instance):
    original = instance.middleName
    instance.middleName = original
    assert instance.middleName == original



@given(instance=contacts_Contact_strategy)
def test_contacts_contact_webPage_setter(instance):
    original = instance.webPage
    instance.webPage = original
    assert instance.webPage == original



@given(instance=contacts_Contact_strategy)
def test_contacts_contact_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=contacts_Contact_strategy)
def test_contacts_contact_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original



@given(instance=contacts_Contact_strategy)
def test_contacts_contact_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
