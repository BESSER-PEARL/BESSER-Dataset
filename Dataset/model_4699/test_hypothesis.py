import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    familytree::Woman,
    familytree::Man,
    familytree::FamilyTree,
    familytree::Wedding,
    familytree::Person,
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



def test_familytree::woman_is_not_abstract():
    assert not inspect.isabstract(familytree::Woman)


def test_familytree::woman_constructor_exists():
    assert callable(familytree::Woman.__init__)


def test_familytree::woman_constructor_args():
    sig = inspect.signature(familytree::Woman.__init__)
    params = list(sig.parameters.keys())



def test_familytree::man_is_not_abstract():
    assert not inspect.isabstract(familytree::Man)


def test_familytree::man_constructor_exists():
    assert callable(familytree::Man.__init__)


def test_familytree::man_constructor_args():
    sig = inspect.signature(familytree::Man.__init__)
    params = list(sig.parameters.keys())



def test_familytree::familytree_is_not_abstract():
    assert not inspect.isabstract(familytree::FamilyTree)


def test_familytree::familytree_constructor_exists():
    assert callable(familytree::FamilyTree.__init__)


def test_familytree::familytree_constructor_args():
    sig = inspect.signature(familytree::FamilyTree.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_familytree::familytree_has_name():
    assert hasattr(familytree::FamilyTree, "name")
    descriptor = None
    for klass in familytree::FamilyTree.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_familytree::wedding_is_not_abstract():
    assert not inspect.isabstract(familytree::Wedding)


def test_familytree::wedding_constructor_exists():
    assert callable(familytree::Wedding.__init__)


def test_familytree::wedding_constructor_args():
    sig = inspect.signature(familytree::Wedding.__init__)
    params = list(sig.parameters.keys())



def test_familytree::person_is_not_abstract():
    assert not inspect.isabstract(familytree::Person)


def test_familytree::person_constructor_exists():
    assert callable(familytree::Person.__init__)


def test_familytree::person_constructor_args():
    sig = inspect.signature(familytree::Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "deathYear" in params, "Missing parameter 'deathYear'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "birthYear" in params, "Missing parameter 'birthYear'"

def test_familytree::person_has_firstName():
    assert hasattr(familytree::Person, "firstName")
    descriptor = None
    for klass in familytree::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_familytree::person_has_deathYear():
    assert hasattr(familytree::Person, "deathYear")
    descriptor = None
    for klass in familytree::Person.__mro__:
        if "deathYear" in klass.__dict__:
            descriptor = klass.__dict__["deathYear"]
            break
    assert isinstance(descriptor, property)

def test_familytree::person_has_lastName():
    assert hasattr(familytree::Person, "lastName")
    descriptor = None
    for klass in familytree::Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_familytree::person_has_birthYear():
    assert hasattr(familytree::Person, "birthYear")
    descriptor = None
    for klass in familytree::Person.__mro__:
        if "birthYear" in klass.__dict__:
            descriptor = klass.__dict__["birthYear"]
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
familytree::Woman_strategy = st.builds(
    familytree::Woman,
)
familytree::Man_strategy = st.builds(
    familytree::Man,
)
familytree::FamilyTree_strategy = st.builds(
    familytree::FamilyTree,
    name=
        safe_text
)
familytree::Wedding_strategy = st.builds(
    familytree::Wedding,
)
familytree::Person_strategy = st.builds(
    familytree::Person,
    firstName=
        safe_text,
    deathYear=
        st.integers(),
    lastName=
        safe_text,
    birthYear=
        st.integers()
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=familytree::Woman_strategy)
@settings(max_examples=50)
def test_familytree::woman_instantiation(instance):
    assert isinstance(instance, familytree::Woman)

@given(instance=familytree::Man_strategy)
@settings(max_examples=50)
def test_familytree::man_instantiation(instance):
    assert isinstance(instance, familytree::Man)

@given(instance=familytree::FamilyTree_strategy)
@settings(max_examples=50)
def test_familytree::familytree_instantiation(instance):
    assert isinstance(instance, familytree::FamilyTree)

@given(instance=familytree::FamilyTree_strategy)
def test_familytree::familytree_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=familytree::FamilyTree_strategy)
def test_familytree::familytree_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=familytree::Wedding_strategy)
@settings(max_examples=50)
def test_familytree::wedding_instantiation(instance):
    assert isinstance(instance, familytree::Wedding)

@given(instance=familytree::Person_strategy)
@settings(max_examples=50)
def test_familytree::person_instantiation(instance):
    assert isinstance(instance, familytree::Person)

@given(instance=familytree::Person_strategy)
def test_familytree::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=familytree::Person_strategy)
def test_familytree::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=familytree::Person_strategy)
def test_familytree::person_deathYear_type(instance):
    assert isinstance(instance.deathYear, int)


@given(instance=familytree::Person_strategy)
def test_familytree::person_deathYear_setter(instance):
    original = instance.deathYear
    instance.deathYear = original
    assert instance.deathYear == original

@given(instance=familytree::Person_strategy)
def test_familytree::person_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=familytree::Person_strategy)
def test_familytree::person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=familytree::Person_strategy)
def test_familytree::person_birthYear_type(instance):
    assert isinstance(instance.birthYear, int)


@given(instance=familytree::Person_strategy)
def test_familytree::person_birthYear_setter(instance):
    original = instance.birthYear
    instance.birthYear = original
    assert instance.birthYear == original
