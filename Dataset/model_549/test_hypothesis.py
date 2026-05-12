import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    family_FamilyTree,
    Person,
    family_Female,
    family_Male,
    family_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family_familytree_is_not_abstract():
    assert not inspect.isabstract(family_FamilyTree)


def test_family_familytree_constructor_exists():
    assert callable(family_FamilyTree.__init__)


def test_family_familytree_constructor_args():
    sig = inspect.signature(family_FamilyTree.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_family_female_is_not_abstract():
    assert not inspect.isabstract(family_Female)


def test_family_female_constructor_exists():
    assert callable(family_Female.__init__)


def test_family_female_constructor_args():
    sig = inspect.signature(family_Female.__init__)
    params = list(sig.parameters.keys())



def test_family_male_is_not_abstract():
    assert not inspect.isabstract(family_Male)


def test_family_male_constructor_exists():
    assert callable(family_Male.__init__)


def test_family_male_constructor_args():
    sig = inspect.signature(family_Male.__init__)
    params = list(sig.parameters.keys())



def test_family_person_is_not_abstract():
    assert not inspect.isabstract(family_Person)


def test_family_person_constructor_exists():
    assert callable(family_Person.__init__)


def test_family_person_constructor_args():
    sig = inspect.signature(family_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "size" in params, "Missing parameter 'size'"
    assert "age" in params, "Missing parameter 'age'"

def test_family_person_has_name():
    assert hasattr(family_Person, "name")
    descriptor = None
    for klass in family_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_weight():
    assert hasattr(family_Person, "weight")
    descriptor = None
    for klass in family_Person.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_size():
    assert hasattr(family_Person, "size")
    descriptor = None
    for klass in family_Person.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_age():
    assert hasattr(family_Person, "age")
    descriptor = None
    for klass in family_Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
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
family_FamilyTree_strategy = st.builds(
    family_FamilyTree,
)
Person_strategy = st.builds(
    Person,
)
family_Female_strategy = st.builds(
    family_Female,
)
family_Male_strategy = st.builds(
    family_Male,
)
family_Person_strategy = st.builds(
    family_Person,
    name=
        safe_text,
    weight=
        st.integers(),
    size=
        st.integers(),
    age=
        st.integers()
)

@given(instance=family_FamilyTree_strategy)
@settings(max_examples=50)
def test_family_familytree_instantiation(instance):
    assert isinstance(instance, family_FamilyTree)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=family_Female_strategy)
@settings(max_examples=50)
def test_family_female_instantiation(instance):
    assert isinstance(instance, family_Female)

@given(instance=family_Male_strategy)
@settings(max_examples=50)
def test_family_male_instantiation(instance):
    assert isinstance(instance, family_Male)

@given(instance=family_Person_strategy)
@settings(max_examples=50)
def test_family_person_instantiation(instance):
    assert isinstance(instance, family_Person)



@given(instance=family_Person_strategy)
def test_family_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=family_Person_strategy)
def test_family_person_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=family_Person_strategy)
def test_family_person_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=family_Person_strategy)
def test_family_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original
