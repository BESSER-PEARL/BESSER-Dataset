import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person_Model,
    Person_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_person_model_is_not_abstract():
    assert not inspect.isabstract(Person_Model)


def test_person_model_constructor_exists():
    assert callable(Person_Model.__init__)


def test_person_model_constructor_args():
    sig = inspect.signature(Person_Model.__init__)
    params = list(sig.parameters.keys())



def test_person_person_is_not_abstract():
    assert not inspect.isabstract(Person_Person)


def test_person_person_constructor_exists():
    assert callable(Person_Person.__init__)


def test_person_person_constructor_args():
    sig = inspect.signature(Person_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_person_person_has_firstName():
    assert hasattr(Person_Person, "firstName")
    descriptor = None
    for klass in Person_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_person_person_has_lastName():
    assert hasattr(Person_Person, "lastName")
    descriptor = None
    for klass in Person_Person.__mro__:
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
Person_Model_strategy = st.builds(
    Person_Model,
)
Person_Person_strategy = st.builds(
    Person_Person,
    firstName=
        safe_text,
    lastName=
        safe_text
)

@given(instance=Person_Model_strategy)
@settings(max_examples=50)
def test_person_model_instantiation(instance):
    assert isinstance(instance, Person_Model)

@given(instance=Person_Person_strategy)
@settings(max_examples=50)
def test_person_person_instantiation(instance):
    assert isinstance(instance, Person_Person)



@given(instance=Person_Person_strategy)
def test_person_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=Person_Person_strategy)
def test_person_person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original
