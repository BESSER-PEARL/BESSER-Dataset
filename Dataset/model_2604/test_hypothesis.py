import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PersonList_LivingPlace,
    PersonList_WorkPlace,
    PersonList_Person,
    PersonList_List,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_personlist_livingplace_is_not_abstract():
    assert not inspect.isabstract(PersonList_LivingPlace)


def test_personlist_livingplace_constructor_exists():
    assert callable(PersonList_LivingPlace.__init__)


def test_personlist_livingplace_constructor_args():
    sig = inspect.signature(PersonList_LivingPlace.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_personlist_livingplace_has_address():
    assert hasattr(PersonList_LivingPlace, "address")
    descriptor = None
    for klass in PersonList_LivingPlace.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_personlist_workplace_is_not_abstract():
    assert not inspect.isabstract(PersonList_WorkPlace)


def test_personlist_workplace_constructor_exists():
    assert callable(PersonList_WorkPlace.__init__)


def test_personlist_workplace_constructor_args():
    sig = inspect.signature(PersonList_WorkPlace.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_personlist_workplace_has_address():
    assert hasattr(PersonList_WorkPlace, "address")
    descriptor = None
    for klass in PersonList_WorkPlace.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_personlist_person_is_not_abstract():
    assert not inspect.isabstract(PersonList_Person)


def test_personlist_person_constructor_exists():
    assert callable(PersonList_Person.__init__)


def test_personlist_person_constructor_args():
    sig = inspect.signature(PersonList_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "gender" in params, "Missing parameter 'gender'"

def test_personlist_person_has_firstname():
    assert hasattr(PersonList_Person, "firstname")
    descriptor = None
    for klass in PersonList_Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_personlist_person_has_lastname():
    assert hasattr(PersonList_Person, "lastname")
    descriptor = None
    for klass in PersonList_Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_personlist_person_has_gender():
    assert hasattr(PersonList_Person, "gender")
    descriptor = None
    for klass in PersonList_Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)



def test_personlist_list_is_not_abstract():
    assert not inspect.isabstract(PersonList_List)


def test_personlist_list_constructor_exists():
    assert callable(PersonList_List.__init__)


def test_personlist_list_constructor_args():
    sig = inspect.signature(PersonList_List.__init__)
    params = list(sig.parameters.keys())

def test_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "Male",
        "Female",
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
PersonList_LivingPlace_strategy = st.builds(
    PersonList_LivingPlace,
    address=
        safe_text
)
PersonList_WorkPlace_strategy = st.builds(
    PersonList_WorkPlace,
    address=
        safe_text
)
PersonList_Person_strategy = st.builds(
    PersonList_Person,
    firstname=
        safe_text,
    lastname=
        safe_text,
    gender=
        safe_text
)
PersonList_List_strategy = st.builds(
    PersonList_List,
)

@given(instance=PersonList_LivingPlace_strategy)
@settings(max_examples=50)
def test_personlist_livingplace_instantiation(instance):
    assert isinstance(instance, PersonList_LivingPlace)



@given(instance=PersonList_LivingPlace_strategy)
def test_personlist_livingplace_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=PersonList_WorkPlace_strategy)
@settings(max_examples=50)
def test_personlist_workplace_instantiation(instance):
    assert isinstance(instance, PersonList_WorkPlace)



@given(instance=PersonList_WorkPlace_strategy)
def test_personlist_workplace_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=PersonList_Person_strategy)
@settings(max_examples=50)
def test_personlist_person_instantiation(instance):
    assert isinstance(instance, PersonList_Person)



@given(instance=PersonList_Person_strategy)
def test_personlist_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=PersonList_Person_strategy)
def test_personlist_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=PersonList_Person_strategy)
def test_personlist_person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original

@given(instance=PersonList_List_strategy)
@settings(max_examples=50)
def test_personlist_list_instantiation(instance):
    assert isinstance(instance, PersonList_List)
