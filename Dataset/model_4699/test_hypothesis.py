import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    familytree_Woman,
    familytree_Man,
    familytree_FamilyTree,
    familytree_Wedding,
    familytree_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_familytree_woman_is_not_abstract():
    assert not inspect.isabstract(familytree_Woman)


def test_familytree_woman_constructor_exists():
    assert callable(familytree_Woman.__init__)


def test_familytree_woman_constructor_args():
    sig = inspect.signature(familytree_Woman.__init__)
    params = list(sig.parameters.keys())



def test_familytree_man_is_not_abstract():
    assert not inspect.isabstract(familytree_Man)


def test_familytree_man_constructor_exists():
    assert callable(familytree_Man.__init__)


def test_familytree_man_constructor_args():
    sig = inspect.signature(familytree_Man.__init__)
    params = list(sig.parameters.keys())



def test_familytree_familytree_is_not_abstract():
    assert not inspect.isabstract(familytree_FamilyTree)


def test_familytree_familytree_constructor_exists():
    assert callable(familytree_FamilyTree.__init__)


def test_familytree_familytree_constructor_args():
    sig = inspect.signature(familytree_FamilyTree.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_familytree_familytree_has_name():
    assert hasattr(familytree_FamilyTree, "name")
    descriptor = None
    for klass in familytree_FamilyTree.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_familytree_wedding_is_not_abstract():
    assert not inspect.isabstract(familytree_Wedding)


def test_familytree_wedding_constructor_exists():
    assert callable(familytree_Wedding.__init__)


def test_familytree_wedding_constructor_args():
    sig = inspect.signature(familytree_Wedding.__init__)
    params = list(sig.parameters.keys())



def test_familytree_person_is_not_abstract():
    assert not inspect.isabstract(familytree_Person)


def test_familytree_person_constructor_exists():
    assert callable(familytree_Person.__init__)


def test_familytree_person_constructor_args():
    sig = inspect.signature(familytree_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "deathYear" in params, "Missing parameter 'deathYear'"
    assert "birthYear" in params, "Missing parameter 'birthYear'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_familytree_person_has_firstName():
    assert hasattr(familytree_Person, "firstName")
    descriptor = None
    for klass in familytree_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_familytree_person_has_deathYear():
    assert hasattr(familytree_Person, "deathYear")
    descriptor = None
    for klass in familytree_Person.__mro__:
        if "deathYear" in klass.__dict__:
            descriptor = klass.__dict__["deathYear"]
            break
    assert isinstance(descriptor, property)

def test_familytree_person_has_birthYear():
    assert hasattr(familytree_Person, "birthYear")
    descriptor = None
    for klass in familytree_Person.__mro__:
        if "birthYear" in klass.__dict__:
            descriptor = klass.__dict__["birthYear"]
            break
    assert isinstance(descriptor, property)

def test_familytree_person_has_lastName():
    assert hasattr(familytree_Person, "lastName")
    descriptor = None
    for klass in familytree_Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
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
Person_strategy = st.builds(
    Person,
)
familytree_Woman_strategy = st.builds(
    familytree_Woman,
)
familytree_Man_strategy = st.builds(
    familytree_Man,
)
familytree_FamilyTree_strategy = st.builds(
    familytree_FamilyTree,
    name=
        safe_text
)
familytree_Wedding_strategy = st.builds(
    familytree_Wedding,
)
familytree_Person_strategy = st.builds(
    familytree_Person,
    firstName=
        safe_text,
    deathYear=
        st.integers(),
    birthYear=
        st.integers(),
    lastName=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=familytree_Woman_strategy)
@settings(max_examples=50)
def test_familytree_woman_instantiation(instance):
    assert isinstance(instance, familytree_Woman)

@given(instance=familytree_Man_strategy)
@settings(max_examples=50)
def test_familytree_man_instantiation(instance):
    assert isinstance(instance, familytree_Man)

@given(instance=familytree_FamilyTree_strategy)
@settings(max_examples=50)
def test_familytree_familytree_instantiation(instance):
    assert isinstance(instance, familytree_FamilyTree)



@given(instance=familytree_FamilyTree_strategy)
def test_familytree_familytree_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=familytree_Wedding_strategy)
@settings(max_examples=50)
def test_familytree_wedding_instantiation(instance):
    assert isinstance(instance, familytree_Wedding)

@given(instance=familytree_Person_strategy)
@settings(max_examples=50)
def test_familytree_person_instantiation(instance):
    assert isinstance(instance, familytree_Person)



@given(instance=familytree_Person_strategy)
def test_familytree_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=familytree_Person_strategy)
def test_familytree_person_deathYear_setter(instance):
    original = instance.deathYear
    instance.deathYear = original
    assert instance.deathYear == original



@given(instance=familytree_Person_strategy)
def test_familytree_person_birthYear_setter(instance):
    original = instance.birthYear
    instance.birthYear = original
    assert instance.birthYear == original



@given(instance=familytree_Person_strategy)
def test_familytree_person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original
