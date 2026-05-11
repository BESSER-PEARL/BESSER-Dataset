import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    pdb2::Person,
    pdb2::Database,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pdb2::person_is_not_abstract():
    assert not inspect.isabstract(pdb2::Person)


def test_pdb2::person_constructor_exists():
    assert callable(pdb2::Person.__init__)


def test_pdb2::person_constructor_args():
    sig = inspect.signature(pdb2::Person.__init__)
    params = list(sig.parameters.keys())
    assert "birthday" in params, "Missing parameter 'birthday'"
    assert "incrementalID" in params, "Missing parameter 'incrementalID'"
    assert "placeOfBirth" in params, "Missing parameter 'placeOfBirth'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_pdb2::person_has_birthday():
    assert hasattr(pdb2::Person, "birthday")
    descriptor = None
    for klass in pdb2::Person.__mro__:
        if "birthday" in klass.__dict__:
            descriptor = klass.__dict__["birthday"]
            break
    assert isinstance(descriptor, property)

def test_pdb2::person_has_incrementalID():
    assert hasattr(pdb2::Person, "incrementalID")
    descriptor = None
    for klass in pdb2::Person.__mro__:
        if "incrementalID" in klass.__dict__:
            descriptor = klass.__dict__["incrementalID"]
            break
    assert isinstance(descriptor, property)

def test_pdb2::person_has_placeOfBirth():
    assert hasattr(pdb2::Person, "placeOfBirth")
    descriptor = None
    for klass in pdb2::Person.__mro__:
        if "placeOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["placeOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_pdb2::person_has_name():
    assert hasattr(pdb2::Person, "name")
    descriptor = None
    for klass in pdb2::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pdb2::person_has_id():
    assert hasattr(pdb2::Person, "id")
    descriptor = None
    for klass in pdb2::Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_pdb2::database_is_not_abstract():
    assert not inspect.isabstract(pdb2::Database)


def test_pdb2::database_constructor_exists():
    assert callable(pdb2::Database.__init__)


def test_pdb2::database_constructor_args():
    sig = inspect.signature(pdb2::Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pdb2::database_has_name():
    assert hasattr(pdb2::Database, "name")
    descriptor = None
    for klass in pdb2::Database.__mro__:
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
pdb2::Person_strategy = st.builds(
    pdb2::Person,
    birthday=
        safe_text,
    incrementalID=
        safe_text,
    placeOfBirth=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
pdb2::Database_strategy = st.builds(
    pdb2::Database,
    name=
        safe_text
)

@given(instance=pdb2::Person_strategy)
@settings(max_examples=50)
def test_pdb2::person_instantiation(instance):
    assert isinstance(instance, pdb2::Person)

@given(instance=pdb2::Person_strategy)
def test_pdb2::person_birthday_type(instance):
    assert isinstance(instance.birthday, str)


@given(instance=pdb2::Person_strategy)
def test_pdb2::person_birthday_setter(instance):
    original = instance.birthday
    instance.birthday = original
    assert instance.birthday == original

@given(instance=pdb2::Person_strategy)
def test_pdb2::person_incrementalID_type(instance):
    assert isinstance(instance.incrementalID, str)


@given(instance=pdb2::Person_strategy)
def test_pdb2::person_incrementalID_setter(instance):
    original = instance.incrementalID
    instance.incrementalID = original
    assert instance.incrementalID == original

@given(instance=pdb2::Person_strategy)
def test_pdb2::person_placeOfBirth_type(instance):
    assert isinstance(instance.placeOfBirth, str)


@given(instance=pdb2::Person_strategy)
def test_pdb2::person_placeOfBirth_setter(instance):
    original = instance.placeOfBirth
    instance.placeOfBirth = original
    assert instance.placeOfBirth == original

@given(instance=pdb2::Person_strategy)
def test_pdb2::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pdb2::Person_strategy)
def test_pdb2::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pdb2::Person_strategy)
def test_pdb2::person_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=pdb2::Person_strategy)
def test_pdb2::person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=pdb2::Database_strategy)
@settings(max_examples=50)
def test_pdb2::database_instantiation(instance):
    assert isinstance(instance, pdb2::Database)

@given(instance=pdb2::Database_strategy)
def test_pdb2::database_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pdb2::Database_strategy)
def test_pdb2::database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
