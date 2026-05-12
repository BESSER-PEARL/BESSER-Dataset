import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Entry,
    addressbook_Contact,
    addressbook_Entry,
    addressbook_NamedElement,
    NamedElement,
    addressbook_Category,
    addressbook_Organization,
    addressbook_AddressBook,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entry_is_not_abstract():
    assert not inspect.isabstract(Entry)


def test_entry_constructor_exists():
    assert callable(Entry.__init__)


def test_entry_constructor_args():
    sig = inspect.signature(Entry.__init__)
    params = list(sig.parameters.keys())



def test_addressbook_contact_is_not_abstract():
    assert not inspect.isabstract(addressbook_Contact)


def test_addressbook_contact_constructor_exists():
    assert callable(addressbook_Contact.__init__)


def test_addressbook_contact_constructor_args():
    sig = inspect.signature(addressbook_Contact.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "email" in params, "Missing parameter 'email'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_addressbook_contact_has_lastName():
    assert hasattr(addressbook_Contact, "lastName")
    descriptor = None
    for klass in addressbook_Contact.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_addressbook_contact_has_email():
    assert hasattr(addressbook_Contact, "email")
    descriptor = None
    for klass in addressbook_Contact.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_addressbook_contact_has_firstName():
    assert hasattr(addressbook_Contact, "firstName")
    descriptor = None
    for klass in addressbook_Contact.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_addressbook_entry_is_not_abstract():
    assert not inspect.isabstract(addressbook_Entry)


def test_addressbook_entry_constructor_exists():
    assert callable(addressbook_Entry.__init__)


def test_addressbook_entry_constructor_args():
    sig = inspect.signature(addressbook_Entry.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_addressbook_entry_has_id():
    assert hasattr(addressbook_Entry, "id")
    descriptor = None
    for klass in addressbook_Entry.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_addressbook_namedelement_is_not_abstract():
    assert not inspect.isabstract(addressbook_NamedElement)


def test_addressbook_namedelement_constructor_exists():
    assert callable(addressbook_NamedElement.__init__)


def test_addressbook_namedelement_constructor_args():
    sig = inspect.signature(addressbook_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_addressbook_namedelement_has_name():
    assert hasattr(addressbook_NamedElement, "name")
    descriptor = None
    for klass in addressbook_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_addressbook_category_is_not_abstract():
    assert not inspect.isabstract(addressbook_Category)


def test_addressbook_category_constructor_exists():
    assert callable(addressbook_Category.__init__)


def test_addressbook_category_constructor_args():
    sig = inspect.signature(addressbook_Category.__init__)
    params = list(sig.parameters.keys())



def test_addressbook_organization_is_not_abstract():
    assert not inspect.isabstract(addressbook_Organization)


def test_addressbook_organization_constructor_exists():
    assert callable(addressbook_Organization.__init__)


def test_addressbook_organization_constructor_args():
    sig = inspect.signature(addressbook_Organization.__init__)
    params = list(sig.parameters.keys())
    assert "homepage" in params, "Missing parameter 'homepage'"

def test_addressbook_organization_has_homepage():
    assert hasattr(addressbook_Organization, "homepage")
    descriptor = None
    for klass in addressbook_Organization.__mro__:
        if "homepage" in klass.__dict__:
            descriptor = klass.__dict__["homepage"]
            break
    assert isinstance(descriptor, property)



def test_addressbook_addressbook_is_not_abstract():
    assert not inspect.isabstract(addressbook_AddressBook)


def test_addressbook_addressbook_constructor_exists():
    assert callable(addressbook_AddressBook.__init__)


def test_addressbook_addressbook_constructor_args():
    sig = inspect.signature(addressbook_AddressBook.__init__)
    params = list(sig.parameters.keys())


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
Entry_strategy = st.builds(
    Entry,
)
addressbook_Contact_strategy = st.builds(
    addressbook_Contact,
    lastName=
        safe_text,
    email=
        safe_text,
    firstName=
        safe_text
)
addressbook_Entry_strategy = st.builds(
    addressbook_Entry,
    id=
        st.integers()
)
addressbook_NamedElement_strategy = st.builds(
    addressbook_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
addressbook_Category_strategy = st.builds(
    addressbook_Category,
)
addressbook_Organization_strategy = st.builds(
    addressbook_Organization,
    homepage=
        safe_text
)
addressbook_AddressBook_strategy = st.builds(
    addressbook_AddressBook,
)

@given(instance=Entry_strategy)
@settings(max_examples=50)
def test_entry_instantiation(instance):
    assert isinstance(instance, Entry)

@given(instance=addressbook_Contact_strategy)
@settings(max_examples=50)
def test_addressbook_contact_instantiation(instance):
    assert isinstance(instance, addressbook_Contact)



@given(instance=addressbook_Contact_strategy)
def test_addressbook_contact_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=addressbook_Contact_strategy)
def test_addressbook_contact_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=addressbook_Contact_strategy)
def test_addressbook_contact_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=addressbook_Entry_strategy)
@settings(max_examples=50)
def test_addressbook_entry_instantiation(instance):
    assert isinstance(instance, addressbook_Entry)



@given(instance=addressbook_Entry_strategy)
def test_addressbook_entry_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=addressbook_NamedElement_strategy)
@settings(max_examples=50)
def test_addressbook_namedelement_instantiation(instance):
    assert isinstance(instance, addressbook_NamedElement)



@given(instance=addressbook_NamedElement_strategy)
def test_addressbook_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=addressbook_Category_strategy)
@settings(max_examples=50)
def test_addressbook_category_instantiation(instance):
    assert isinstance(instance, addressbook_Category)

@given(instance=addressbook_Organization_strategy)
@settings(max_examples=50)
def test_addressbook_organization_instantiation(instance):
    assert isinstance(instance, addressbook_Organization)



@given(instance=addressbook_Organization_strategy)
def test_addressbook_organization_homepage_setter(instance):
    original = instance.homepage
    instance.homepage = original
    assert instance.homepage == original

@given(instance=addressbook_AddressBook_strategy)
@settings(max_examples=50)
def test_addressbook_addressbook_instantiation(instance):
    assert isinstance(instance, addressbook_AddressBook)
