import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    familyTree::Person,
    familyTree::FamilyTree,
    Person,
    familyTree::Female,
    familyTree::Male,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_familytree::person_is_not_abstract():
    assert not inspect.isabstract(familyTree::Person)


def test_familytree::person_constructor_exists():
    assert callable(familyTree::Person.__init__)


def test_familytree::person_constructor_args():
    sig = inspect.signature(familyTree::Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "name" in params, "Missing parameter 'name'"

def test_familytree::person_has_lastName():
    assert hasattr(familyTree::Person, "lastName")
    descriptor = None
    for klass in familyTree::Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_familytree::person_has_name():
    assert hasattr(familyTree::Person, "name")
    descriptor = None
    for klass in familyTree::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_familytree::familytree_is_not_abstract():
    assert not inspect.isabstract(familyTree::FamilyTree)


def test_familytree::familytree_constructor_exists():
    assert callable(familyTree::FamilyTree.__init__)


def test_familytree::familytree_constructor_args():
    sig = inspect.signature(familyTree::FamilyTree.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_familytree::female_is_not_abstract():
    assert not inspect.isabstract(familyTree::Female)


def test_familytree::female_constructor_exists():
    assert callable(familyTree::Female.__init__)


def test_familytree::female_constructor_args():
    sig = inspect.signature(familyTree::Female.__init__)
    params = list(sig.parameters.keys())



def test_familytree::male_is_not_abstract():
    assert not inspect.isabstract(familyTree::Male)


def test_familytree::male_constructor_exists():
    assert callable(familyTree::Male.__init__)


def test_familytree::male_constructor_args():
    sig = inspect.signature(familyTree::Male.__init__)
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
familyTree::Person_strategy = st.builds(
    familyTree::Person,
    lastName=
        safe_text,
    name=
        safe_text
)
familyTree::FamilyTree_strategy = st.builds(
    familyTree::FamilyTree,
)
Person_strategy = st.builds(
    Person,
)
familyTree::Female_strategy = st.builds(
    familyTree::Female,
)
familyTree::Male_strategy = st.builds(
    familyTree::Male,
)

@given(instance=familyTree::Person_strategy)
@settings(max_examples=50)
def test_familytree::person_instantiation(instance):
    assert isinstance(instance, familyTree::Person)

@given(instance=familyTree::Person_strategy)
def test_familytree::person_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=familyTree::Person_strategy)
def test_familytree::person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=familyTree::Person_strategy)
def test_familytree::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=familyTree::Person_strategy)
def test_familytree::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=familyTree::FamilyTree_strategy)
@settings(max_examples=50)
def test_familytree::familytree_instantiation(instance):
    assert isinstance(instance, familyTree::FamilyTree)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=familyTree::Female_strategy)
@settings(max_examples=50)
def test_familytree::female_instantiation(instance):
    assert isinstance(instance, familyTree::Female)

@given(instance=familyTree::Male_strategy)
@settings(max_examples=50)
def test_familytree::male_instantiation(instance):
    assert isinstance(instance, familyTree::Male)
