import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    pdb1_Person,
    pdb1_Database,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pdb1_person_is_not_abstract():
    assert not inspect.isabstract(pdb1_Person)


def test_pdb1_person_constructor_exists():
    assert callable(pdb1_Person.__init__)


def test_pdb1_person_constructor_args():
    sig = inspect.signature(pdb1_Person.__init__)
    params = list(sig.parameters.keys())
    assert "placeOfBirth" in params, "Missing parameter 'placeOfBirth'"
    assert "id" in params, "Missing parameter 'id'"
    assert "incrementalID" in params, "Missing parameter 'incrementalID'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "birthday" in params, "Missing parameter 'birthday'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_pdb1_person_has_placeOfBirth():
    assert hasattr(pdb1_Person, "placeOfBirth")
    descriptor = None
    for klass in pdb1_Person.__mro__:
        if "placeOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["placeOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_pdb1_person_has_id():
    assert hasattr(pdb1_Person, "id")
    descriptor = None
    for klass in pdb1_Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_pdb1_person_has_incrementalID():
    assert hasattr(pdb1_Person, "incrementalID")
    descriptor = None
    for klass in pdb1_Person.__mro__:
        if "incrementalID" in klass.__dict__:
            descriptor = klass.__dict__["incrementalID"]
            break
    assert isinstance(descriptor, property)

def test_pdb1_person_has_lastName():
    assert hasattr(pdb1_Person, "lastName")
    descriptor = None
    for klass in pdb1_Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_pdb1_person_has_birthday():
    assert hasattr(pdb1_Person, "birthday")
    descriptor = None
    for klass in pdb1_Person.__mro__:
        if "birthday" in klass.__dict__:
            descriptor = klass.__dict__["birthday"]
            break
    assert isinstance(descriptor, property)

def test_pdb1_person_has_firstName():
    assert hasattr(pdb1_Person, "firstName")
    descriptor = None
    for klass in pdb1_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_pdb1_database_is_not_abstract():
    assert not inspect.isabstract(pdb1_Database)


def test_pdb1_database_constructor_exists():
    assert callable(pdb1_Database.__init__)


def test_pdb1_database_constructor_args():
    sig = inspect.signature(pdb1_Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pdb1_database_has_name():
    assert hasattr(pdb1_Database, "name")
    descriptor = None
    for klass in pdb1_Database.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
pdb1_Person_strategy = st.builds(
    pdb1_Person,
    placeOfBirth=
        safe_text,
    id=
        safe_text,
    incrementalID=
        safe_text,
    lastName=
        safe_text,
    birthday=
        safe_text,
    firstName=
        safe_text
)
pdb1_Database_strategy = st.builds(
    pdb1_Database,
    name=
        safe_text
)

@given(instance=pdb1_Person_strategy)
@settings(max_examples=50)
def test_pdb1_person_instantiation(instance):
    assert isinstance(instance, pdb1_Person)



@given(instance=pdb1_Person_strategy)
def test_pdb1_person_placeOfBirth_setter(instance):
    original = instance.placeOfBirth
    instance.placeOfBirth = original
    assert instance.placeOfBirth == original



@given(instance=pdb1_Person_strategy)
def test_pdb1_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=pdb1_Person_strategy)
def test_pdb1_person_incrementalID_setter(instance):
    original = instance.incrementalID
    instance.incrementalID = original
    assert instance.incrementalID == original



@given(instance=pdb1_Person_strategy)
def test_pdb1_person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=pdb1_Person_strategy)
def test_pdb1_person_birthday_setter(instance):
    original = instance.birthday
    instance.birthday = original
    assert instance.birthday == original



@given(instance=pdb1_Person_strategy)
def test_pdb1_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=pdb1_Database_strategy)
@settings(max_examples=50)
def test_pdb1_database_instantiation(instance):
    assert isinstance(instance, pdb1_Database)



@given(instance=pdb1_Database_strategy)
def test_pdb1_database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
