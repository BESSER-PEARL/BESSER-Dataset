import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    pdb2_Person,
    pdb2_Database,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pdb2_person_is_not_abstract():
    assert not inspect.isabstract(pdb2_Person)


def test_pdb2_person_constructor_exists():
    assert callable(pdb2_Person.__init__)


def test_pdb2_person_constructor_args():
    sig = inspect.signature(pdb2_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "placeOfBirth" in params, "Missing parameter 'placeOfBirth'"
    assert "birthday" in params, "Missing parameter 'birthday'"
    assert "incrementalID" in params, "Missing parameter 'incrementalID'"
    assert "id" in params, "Missing parameter 'id'"

def test_pdb2_person_has_name():
    assert hasattr(pdb2_Person, "name")
    descriptor = None
    for klass in pdb2_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pdb2_person_has_placeOfBirth():
    assert hasattr(pdb2_Person, "placeOfBirth")
    descriptor = None
    for klass in pdb2_Person.__mro__:
        if "placeOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["placeOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_pdb2_person_has_birthday():
    assert hasattr(pdb2_Person, "birthday")
    descriptor = None
    for klass in pdb2_Person.__mro__:
        if "birthday" in klass.__dict__:
            descriptor = klass.__dict__["birthday"]
            break
    assert isinstance(descriptor, property)

def test_pdb2_person_has_incrementalID():
    assert hasattr(pdb2_Person, "incrementalID")
    descriptor = None
    for klass in pdb2_Person.__mro__:
        if "incrementalID" in klass.__dict__:
            descriptor = klass.__dict__["incrementalID"]
            break
    assert isinstance(descriptor, property)

def test_pdb2_person_has_id():
    assert hasattr(pdb2_Person, "id")
    descriptor = None
    for klass in pdb2_Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_pdb2_database_is_not_abstract():
    assert not inspect.isabstract(pdb2_Database)


def test_pdb2_database_constructor_exists():
    assert callable(pdb2_Database.__init__)


def test_pdb2_database_constructor_args():
    sig = inspect.signature(pdb2_Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pdb2_database_has_name():
    assert hasattr(pdb2_Database, "name")
    descriptor = None
    for klass in pdb2_Database.__mro__:
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
pdb2_Person_strategy = st.builds(
    pdb2_Person,
    name=
        safe_text,
    placeOfBirth=
        safe_text,
    birthday=
        safe_text,
    incrementalID=
        safe_text,
    id=
        safe_text
)
pdb2_Database_strategy = st.builds(
    pdb2_Database,
    name=
        safe_text
)

@given(instance=pdb2_Person_strategy)
@settings(max_examples=50)
def test_pdb2_person_instantiation(instance):
    assert isinstance(instance, pdb2_Person)



@given(instance=pdb2_Person_strategy)
def test_pdb2_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pdb2_Person_strategy)
def test_pdb2_person_placeOfBirth_setter(instance):
    original = instance.placeOfBirth
    instance.placeOfBirth = original
    assert instance.placeOfBirth == original



@given(instance=pdb2_Person_strategy)
def test_pdb2_person_birthday_setter(instance):
    original = instance.birthday
    instance.birthday = original
    assert instance.birthday == original



@given(instance=pdb2_Person_strategy)
def test_pdb2_person_incrementalID_setter(instance):
    original = instance.incrementalID
    instance.incrementalID = original
    assert instance.incrementalID == original



@given(instance=pdb2_Person_strategy)
def test_pdb2_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=pdb2_Database_strategy)
@settings(max_examples=50)
def test_pdb2_database_instantiation(instance):
    assert isinstance(instance, pdb2_Database)



@given(instance=pdb2_Database_strategy)
def test_pdb2_database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
