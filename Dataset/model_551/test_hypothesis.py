import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    familyTree_Person,
    familyTree_FamilyTree,
    Person,
    familyTree_Female,
    familyTree_Male,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_familytree_person_is_not_abstract():
    assert not inspect.isabstract(familyTree_Person)


def test_familytree_person_constructor_exists():
    assert callable(familyTree_Person.__init__)


def test_familytree_person_constructor_args():
    sig = inspect.signature(familyTree_Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "name" in params, "Missing parameter 'name'"

def test_familytree_person_has_lastName():
    assert hasattr(familyTree_Person, "lastName")
    descriptor = None
    for klass in familyTree_Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_familytree_person_has_name():
    assert hasattr(familyTree_Person, "name")
    descriptor = None
    for klass in familyTree_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_familytree_familytree_is_not_abstract():
    assert not inspect.isabstract(familyTree_FamilyTree)


def test_familytree_familytree_constructor_exists():
    assert callable(familyTree_FamilyTree.__init__)


def test_familytree_familytree_constructor_args():
    sig = inspect.signature(familyTree_FamilyTree.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_familytree_female_is_not_abstract():
    assert not inspect.isabstract(familyTree_Female)


def test_familytree_female_constructor_exists():
    assert callable(familyTree_Female.__init__)


def test_familytree_female_constructor_args():
    sig = inspect.signature(familyTree_Female.__init__)
    params = list(sig.parameters.keys())



def test_familytree_male_is_not_abstract():
    assert not inspect.isabstract(familyTree_Male)


def test_familytree_male_constructor_exists():
    assert callable(familyTree_Male.__init__)


def test_familytree_male_constructor_args():
    sig = inspect.signature(familyTree_Male.__init__)
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
familyTree_Person_strategy = st.builds(
    familyTree_Person,
    lastName=
        safe_text,
    name=
        safe_text
)
familyTree_FamilyTree_strategy = st.builds(
    familyTree_FamilyTree,
)
Person_strategy = st.builds(
    Person,
)
familyTree_Female_strategy = st.builds(
    familyTree_Female,
)
familyTree_Male_strategy = st.builds(
    familyTree_Male,
)

@given(instance=familyTree_Person_strategy)
@settings(max_examples=50)
def test_familytree_person_instantiation(instance):
    assert isinstance(instance, familyTree_Person)



@given(instance=familyTree_Person_strategy)
def test_familytree_person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=familyTree_Person_strategy)
def test_familytree_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=familyTree_FamilyTree_strategy)
@settings(max_examples=50)
def test_familytree_familytree_instantiation(instance):
    assert isinstance(instance, familyTree_FamilyTree)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=familyTree_Female_strategy)
@settings(max_examples=50)
def test_familytree_female_instantiation(instance):
    assert isinstance(instance, familyTree_Female)

@given(instance=familyTree_Male_strategy)
@settings(max_examples=50)
def test_familytree_male_instantiation(instance):
    assert isinstance(instance, familyTree_Male)
