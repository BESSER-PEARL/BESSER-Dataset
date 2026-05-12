import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    persons_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_persons_person_is_not_abstract():
    assert not inspect.isabstract(persons_Person)


def test_persons_person_constructor_exists():
    assert callable(persons_Person.__init__)


def test_persons_person_constructor_args():
    sig = inspect.signature(persons_Person.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_persons_person_has_id():
    assert hasattr(persons_Person, "id")
    descriptor = None
    for klass in persons_Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_persons_person_has_lastName():
    assert hasattr(persons_Person, "lastName")
    descriptor = None
    for klass in persons_Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_persons_person_has_firstName():
    assert hasattr(persons_Person, "firstName")
    descriptor = None
    for klass in persons_Person.__mro__:
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
persons_Person_strategy = st.builds(
    persons_Person,
    id=
        safe_text,
    lastName=
        safe_text,
    firstName=
        safe_text
)

@given(instance=persons_Person_strategy)
@settings(max_examples=50)
def test_persons_person_instantiation(instance):
    assert isinstance(instance, persons_Person)



@given(instance=persons_Person_strategy)
def test_persons_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=persons_Person_strategy)
def test_persons_person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=persons_Person_strategy)
def test_persons_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original
