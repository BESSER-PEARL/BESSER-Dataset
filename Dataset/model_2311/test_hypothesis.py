import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    Persons_Female,
    Persons_Male,
    Persons_Person,
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



def test_persons_female_is_not_abstract():
    assert not inspect.isabstract(Persons_Female)


def test_persons_female_constructor_exists():
    assert callable(Persons_Female.__init__)


def test_persons_female_constructor_args():
    sig = inspect.signature(Persons_Female.__init__)
    params = list(sig.parameters.keys())



def test_persons_male_is_not_abstract():
    assert not inspect.isabstract(Persons_Male)


def test_persons_male_constructor_exists():
    assert callable(Persons_Male.__init__)


def test_persons_male_constructor_args():
    sig = inspect.signature(Persons_Male.__init__)
    params = list(sig.parameters.keys())



def test_persons_person_is_not_abstract():
    assert not inspect.isabstract(Persons_Person)


def test_persons_person_constructor_exists():
    assert callable(Persons_Person.__init__)


def test_persons_person_constructor_args():
    sig = inspect.signature(Persons_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"

def test_persons_person_has_name():
    assert hasattr(Persons_Person, "name")
    descriptor = None
    for klass in Persons_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_persons_person_has_age():
    assert hasattr(Persons_Person, "age")
    descriptor = None
    for klass in Persons_Person.__mro__:
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
Person_strategy = st.builds(
    Person,
)
Persons_Female_strategy = st.builds(
    Persons_Female,
)
Persons_Male_strategy = st.builds(
    Persons_Male,
)
Persons_Person_strategy = st.builds(
    Persons_Person,
    name=
        safe_text,
    age=
        st.integers()
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=Persons_Female_strategy)
@settings(max_examples=50)
def test_persons_female_instantiation(instance):
    assert isinstance(instance, Persons_Female)

@given(instance=Persons_Male_strategy)
@settings(max_examples=50)
def test_persons_male_instantiation(instance):
    assert isinstance(instance, Persons_Male)

@given(instance=Persons_Person_strategy)
@settings(max_examples=50)
def test_persons_person_instantiation(instance):
    assert isinstance(instance, Persons_Person)



@given(instance=Persons_Person_strategy)
def test_persons_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Persons_Person_strategy)
def test_persons_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original
