import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Persons::Person,
    Persons::Persons,
    GenderType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_persons::person_is_not_abstract():
    assert not inspect.isabstract(Persons::Person)


def test_persons::person_constructor_exists():
    assert callable(Persons::Person.__init__)


def test_persons::person_constructor_args():
    sig = inspect.signature(Persons::Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "lastname" in params, "Missing parameter 'lastname'"

def test_persons::person_has_firstname():
    assert hasattr(Persons::Person, "firstname")
    descriptor = None
    for klass in Persons::Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_persons::person_has_gender():
    assert hasattr(Persons::Person, "gender")
    descriptor = None
    for klass in Persons::Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_persons::person_has_lastname():
    assert hasattr(Persons::Person, "lastname")
    descriptor = None
    for klass in Persons::Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)



def test_persons::persons_is_not_abstract():
    assert not inspect.isabstract(Persons::Persons)


def test_persons::persons_constructor_exists():
    assert callable(Persons::Persons.__init__)


def test_persons::persons_constructor_args():
    sig = inspect.signature(Persons::Persons.__init__)
    params = list(sig.parameters.keys())

def test_gendertype_exists():
    # Check that the Enumeration exists
    assert GenderType is not None

def test_gendertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GenderType]
    expected_literals = [
        "female",
        "male",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GenderType"


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
Persons::Person_strategy = st.builds(
    Persons::Person,
    firstname=
        safe_text,
    gender=
        safe_text,
    lastname=
        safe_text
)
Persons::Persons_strategy = st.builds(
    Persons::Persons,
)

@given(instance=Persons::Person_strategy)
@settings(max_examples=50)
def test_persons::person_instantiation(instance):
    assert isinstance(instance, Persons::Person)

@given(instance=Persons::Person_strategy)
def test_persons::person_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=Persons::Person_strategy)
def test_persons::person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=Persons::Person_strategy)
def test_persons::person_gender_type(instance):
    assert isinstance(instance.gender, str)


@given(instance=Persons::Person_strategy)
def test_persons::person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original

@given(instance=Persons::Person_strategy)
def test_persons::person_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=Persons::Person_strategy)
def test_persons::person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=Persons::Persons_strategy)
@settings(max_examples=50)
def test_persons::persons_instantiation(instance):
    assert isinstance(instance, Persons::Persons)
