import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Entry,
    addressbook::Contact,
    addressbook::Entry,
    addressbook::NamedElement,
    NamedElement,
    addressbook::Category,
    addressbook::Organization,
    addressbook::AddressBook,
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



def test_addressbook::contact_is_not_abstract():
    assert not inspect.isabstract(addressbook::Contact)


def test_addressbook::contact_constructor_exists():
    assert callable(addressbook::Contact.__init__)


def test_addressbook::contact_constructor_args():
    sig = inspect.signature(addressbook::Contact.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_addressbook::contact_has_email():
    assert hasattr(addressbook::Contact, "email")
    descriptor = None
    for klass in addressbook::Contact.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_addressbook::contact_has_lastName():
    assert hasattr(addressbook::Contact, "lastName")
    descriptor = None
    for klass in addressbook::Contact.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_addressbook::contact_has_firstName():
    assert hasattr(addressbook::Contact, "firstName")
    descriptor = None
    for klass in addressbook::Contact.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_addressbook::entry_is_not_abstract():
    assert not inspect.isabstract(addressbook::Entry)


def test_addressbook::entry_constructor_exists():
    assert callable(addressbook::Entry.__init__)


def test_addressbook::entry_constructor_args():
    sig = inspect.signature(addressbook::Entry.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_addressbook::entry_has_id():
    assert hasattr(addressbook::Entry, "id")
    descriptor = None
    for klass in addressbook::Entry.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_addressbook::namedelement_is_not_abstract():
    assert not inspect.isabstract(addressbook::NamedElement)


def test_addressbook::namedelement_constructor_exists():
    assert callable(addressbook::NamedElement.__init__)


def test_addressbook::namedelement_constructor_args():
    sig = inspect.signature(addressbook::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_addressbook::namedelement_has_name():
    assert hasattr(addressbook::NamedElement, "name")
    descriptor = None
    for klass in addressbook::NamedElement.__mro__:
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



def test_addressbook::category_is_not_abstract():
    assert not inspect.isabstract(addressbook::Category)


def test_addressbook::category_constructor_exists():
    assert callable(addressbook::Category.__init__)


def test_addressbook::category_constructor_args():
    sig = inspect.signature(addressbook::Category.__init__)
    params = list(sig.parameters.keys())



def test_addressbook::organization_is_not_abstract():
    assert not inspect.isabstract(addressbook::Organization)


def test_addressbook::organization_constructor_exists():
    assert callable(addressbook::Organization.__init__)


def test_addressbook::organization_constructor_args():
    sig = inspect.signature(addressbook::Organization.__init__)
    params = list(sig.parameters.keys())
    assert "homepage" in params, "Missing parameter 'homepage'"

def test_addressbook::organization_has_homepage():
    assert hasattr(addressbook::Organization, "homepage")
    descriptor = None
    for klass in addressbook::Organization.__mro__:
        if "homepage" in klass.__dict__:
            descriptor = klass.__dict__["homepage"]
            break
    assert isinstance(descriptor, property)



def test_addressbook::addressbook_is_not_abstract():
    assert not inspect.isabstract(addressbook::AddressBook)


def test_addressbook::addressbook_constructor_exists():
    assert callable(addressbook::AddressBook.__init__)


def test_addressbook::addressbook_constructor_args():
    sig = inspect.signature(addressbook::AddressBook.__init__)
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
addressbook::Contact_strategy = st.builds(
    addressbook::Contact,
    email=
        safe_text,
    lastName=
        safe_text,
    firstName=
        safe_text
)
addressbook::Entry_strategy = st.builds(
    addressbook::Entry,
    id=
        st.integers()
)
addressbook::NamedElement_strategy = st.builds(
    addressbook::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
addressbook::Category_strategy = st.builds(
    addressbook::Category,
)
addressbook::Organization_strategy = st.builds(
    addressbook::Organization,
    homepage=
        safe_text
)
addressbook::AddressBook_strategy = st.builds(
    addressbook::AddressBook,
)

@given(instance=Entry_strategy)
@settings(max_examples=50)
def test_entry_instantiation(instance):
    assert isinstance(instance, Entry)

@given(instance=addressbook::Contact_strategy)
@settings(max_examples=50)
def test_addressbook::contact_instantiation(instance):
    assert isinstance(instance, addressbook::Contact)

@given(instance=addressbook::Contact_strategy)
def test_addressbook::contact_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=addressbook::Contact_strategy)
def test_addressbook::contact_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=addressbook::Contact_strategy)
def test_addressbook::contact_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=addressbook::Contact_strategy)
def test_addressbook::contact_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=addressbook::Contact_strategy)
def test_addressbook::contact_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=addressbook::Contact_strategy)
def test_addressbook::contact_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=addressbook::Entry_strategy)
@settings(max_examples=50)
def test_addressbook::entry_instantiation(instance):
    assert isinstance(instance, addressbook::Entry)

@given(instance=addressbook::Entry_strategy)
def test_addressbook::entry_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=addressbook::Entry_strategy)
def test_addressbook::entry_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=addressbook::NamedElement_strategy)
@settings(max_examples=50)
def test_addressbook::namedelement_instantiation(instance):
    assert isinstance(instance, addressbook::NamedElement)

@given(instance=addressbook::NamedElement_strategy)
def test_addressbook::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=addressbook::NamedElement_strategy)
def test_addressbook::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=addressbook::Category_strategy)
@settings(max_examples=50)
def test_addressbook::category_instantiation(instance):
    assert isinstance(instance, addressbook::Category)

@given(instance=addressbook::Organization_strategy)
@settings(max_examples=50)
def test_addressbook::organization_instantiation(instance):
    assert isinstance(instance, addressbook::Organization)

@given(instance=addressbook::Organization_strategy)
def test_addressbook::organization_homepage_type(instance):
    assert isinstance(instance.homepage, str)


@given(instance=addressbook::Organization_strategy)
def test_addressbook::organization_homepage_setter(instance):
    original = instance.homepage
    instance.homepage = original
    assert instance.homepage == original

@given(instance=addressbook::AddressBook_strategy)
@settings(max_examples=50)
def test_addressbook::addressbook_instantiation(instance):
    assert isinstance(instance, addressbook::AddressBook)
