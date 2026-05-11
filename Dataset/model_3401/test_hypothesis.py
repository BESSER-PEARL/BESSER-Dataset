import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person::Model,
    Person::Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_person::model_is_not_abstract():
    assert not inspect.isabstract(Person::Model)


def test_person::model_constructor_exists():
    assert callable(Person::Model.__init__)


def test_person::model_constructor_args():
    sig = inspect.signature(Person::Model.__init__)
    params = list(sig.parameters.keys())



def test_person::person_is_not_abstract():
    assert not inspect.isabstract(Person::Person)


def test_person::person_constructor_exists():
    assert callable(Person::Person.__init__)


def test_person::person_constructor_args():
    sig = inspect.signature(Person::Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_person::person_has_lastName():
    assert hasattr(Person::Person, "lastName")
    descriptor = None
    for klass in Person::Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_person::person_has_firstName():
    assert hasattr(Person::Person, "firstName")
    descriptor = None
    for klass in Person::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
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
Person::Model_strategy = st.builds(
    Person::Model,
)
Person::Person_strategy = st.builds(
    Person::Person,
    lastName=
        safe_text,
    firstName=
        safe_text
)

@given(instance=Person::Model_strategy)
@settings(max_examples=50)
def test_person::model_instantiation(instance):
    assert isinstance(instance, Person::Model)

@given(instance=Person::Person_strategy)
@settings(max_examples=50)
def test_person::person_instantiation(instance):
    assert isinstance(instance, Person::Person)

@given(instance=Person::Person_strategy)
def test_person::person_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=Person::Person_strategy)
def test_person::person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=Person::Person_strategy)
def test_person::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=Person::Person_strategy)
def test_person::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original
