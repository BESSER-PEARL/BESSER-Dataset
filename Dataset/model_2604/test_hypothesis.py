import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PersonList::LivingPlace,
    PersonList::WorkPlace,
    PersonList::Person,
    PersonList::List,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_personlist::livingplace_is_not_abstract():
    assert not inspect.isabstract(PersonList::LivingPlace)


def test_personlist::livingplace_constructor_exists():
    assert callable(PersonList::LivingPlace.__init__)


def test_personlist::livingplace_constructor_args():
    sig = inspect.signature(PersonList::LivingPlace.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_personlist::livingplace_has_address():
    assert hasattr(PersonList::LivingPlace, "address")
    descriptor = None
    for klass in PersonList::LivingPlace.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_personlist::workplace_is_not_abstract():
    assert not inspect.isabstract(PersonList::WorkPlace)


def test_personlist::workplace_constructor_exists():
    assert callable(PersonList::WorkPlace.__init__)


def test_personlist::workplace_constructor_args():
    sig = inspect.signature(PersonList::WorkPlace.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_personlist::workplace_has_address():
    assert hasattr(PersonList::WorkPlace, "address")
    descriptor = None
    for klass in PersonList::WorkPlace.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_personlist::person_is_not_abstract():
    assert not inspect.isabstract(PersonList::Person)


def test_personlist::person_constructor_exists():
    assert callable(PersonList::Person.__init__)


def test_personlist::person_constructor_args():
    sig = inspect.signature(PersonList::Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "gender" in params, "Missing parameter 'gender'"

def test_personlist::person_has_firstname():
    assert hasattr(PersonList::Person, "firstname")
    descriptor = None
    for klass in PersonList::Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_personlist::person_has_lastname():
    assert hasattr(PersonList::Person, "lastname")
    descriptor = None
    for klass in PersonList::Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_personlist::person_has_gender():
    assert hasattr(PersonList::Person, "gender")
    descriptor = None
    for klass in PersonList::Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)



def test_personlist::list_is_not_abstract():
    assert not inspect.isabstract(PersonList::List)


def test_personlist::list_constructor_exists():
    assert callable(PersonList::List.__init__)


def test_personlist::list_constructor_args():
    sig = inspect.signature(PersonList::List.__init__)
    params = list(sig.parameters.keys())

def test_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "Female",
        "Male",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gender"


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
PersonList::LivingPlace_strategy = st.builds(
    PersonList::LivingPlace,
    address=
        safe_text
)
PersonList::WorkPlace_strategy = st.builds(
    PersonList::WorkPlace,
    address=
        safe_text
)
PersonList::Person_strategy = st.builds(
    PersonList::Person,
    firstname=
        safe_text,
    lastname=
        safe_text,
    gender=
        safe_text
)
PersonList::List_strategy = st.builds(
    PersonList::List,
)

@given(instance=PersonList::LivingPlace_strategy)
@settings(max_examples=50)
def test_personlist::livingplace_instantiation(instance):
    assert isinstance(instance, PersonList::LivingPlace)

@given(instance=PersonList::LivingPlace_strategy)
def test_personlist::livingplace_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=PersonList::LivingPlace_strategy)
def test_personlist::livingplace_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=PersonList::WorkPlace_strategy)
@settings(max_examples=50)
def test_personlist::workplace_instantiation(instance):
    assert isinstance(instance, PersonList::WorkPlace)

@given(instance=PersonList::WorkPlace_strategy)
def test_personlist::workplace_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=PersonList::WorkPlace_strategy)
def test_personlist::workplace_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=PersonList::Person_strategy)
@settings(max_examples=50)
def test_personlist::person_instantiation(instance):
    assert isinstance(instance, PersonList::Person)

@given(instance=PersonList::Person_strategy)
def test_personlist::person_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=PersonList::Person_strategy)
def test_personlist::person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=PersonList::Person_strategy)
def test_personlist::person_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=PersonList::Person_strategy)
def test_personlist::person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=PersonList::Person_strategy)
def test_personlist::person_gender_type(instance):
    assert isinstance(instance.gender, str)


@given(instance=PersonList::Person_strategy)
def test_personlist::person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original

@given(instance=PersonList::List_strategy)
@settings(max_examples=50)
def test_personlist::list_instantiation(instance):
    assert isinstance(instance, PersonList::List)
