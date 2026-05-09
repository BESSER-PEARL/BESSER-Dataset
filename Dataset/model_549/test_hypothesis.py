import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    family::FamilyTree,
    Person,
    family::Female,
    family::Male,
    family::Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family::familytree_is_not_abstract():
    assert not inspect.isabstract(family::FamilyTree)


def test_family::familytree_constructor_exists():
    assert callable(family::FamilyTree.__init__)


def test_family::familytree_constructor_args():
    sig = inspect.signature(family::FamilyTree.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_family::female_is_not_abstract():
    assert not inspect.isabstract(family::Female)


def test_family::female_constructor_exists():
    assert callable(family::Female.__init__)


def test_family::female_constructor_args():
    sig = inspect.signature(family::Female.__init__)
    params = list(sig.parameters.keys())



def test_family::male_is_not_abstract():
    assert not inspect.isabstract(family::Male)


def test_family::male_constructor_exists():
    assert callable(family::Male.__init__)


def test_family::male_constructor_args():
    sig = inspect.signature(family::Male.__init__)
    params = list(sig.parameters.keys())



def test_family::person_is_not_abstract():
    assert not inspect.isabstract(family::Person)


def test_family::person_constructor_exists():
    assert callable(family::Person.__init__)


def test_family::person_constructor_args():
    sig = inspect.signature(family::Person.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "age" in params, "Missing parameter 'age'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "name" in params, "Missing parameter 'name'"

def test_family::person_has_size():
    assert hasattr(family::Person, "size")
    descriptor = None
    for klass in family::Person.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_age():
    assert hasattr(family::Person, "age")
    descriptor = None
    for klass in family::Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_weight():
    assert hasattr(family::Person, "weight")
    descriptor = None
    for klass in family::Person.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_name():
    assert hasattr(family::Person, "name")
    descriptor = None
    for klass in family::Person.__mro__:
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
family::FamilyTree_strategy = st.builds(
    family::FamilyTree,
)
Person_strategy = st.builds(
    Person,
)
family::Female_strategy = st.builds(
    family::Female,
)
family::Male_strategy = st.builds(
    family::Male,
)
family::Person_strategy = st.builds(
    family::Person,
    size=
        st.integers(),
    age=
        st.integers(),
    weight=
        st.integers(),
    name=
        safe_text
)

@given(instance=family::FamilyTree_strategy)
@settings(max_examples=50)
def test_family::familytree_instantiation(instance):
    assert isinstance(instance, family::FamilyTree)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=family::Female_strategy)
@settings(max_examples=50)
def test_family::female_instantiation(instance):
    assert isinstance(instance, family::Female)

@given(instance=family::Male_strategy)
@settings(max_examples=50)
def test_family::male_instantiation(instance):
    assert isinstance(instance, family::Male)

@given(instance=family::Person_strategy)
@settings(max_examples=50)
def test_family::person_instantiation(instance):
    assert isinstance(instance, family::Person)

@given(instance=family::Person_strategy)
def test_family::person_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=family::Person_strategy)
def test_family::person_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=family::Person_strategy)
def test_family::person_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=family::Person_strategy)
def test_family::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=family::Person_strategy)
def test_family::person_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=family::Person_strategy)
def test_family::person_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=family::Person_strategy)
def test_family::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::Person_strategy)
def test_family::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
