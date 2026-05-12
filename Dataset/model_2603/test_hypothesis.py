import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Persons_Person,
    Persons_Persons,
    GenderType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_persons_person_is_not_abstract():
    assert not inspect.isabstract(Persons_Person)


def test_persons_person_constructor_exists():
    assert callable(Persons_Person.__init__)


def test_persons_person_constructor_args():
    sig = inspect.signature(Persons_Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_persons_person_has_lastname():
    assert hasattr(Persons_Person, "lastname")
    descriptor = None
    for klass in Persons_Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_persons_person_has_gender():
    assert hasattr(Persons_Person, "gender")
    descriptor = None
    for klass in Persons_Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_persons_person_has_firstname():
    assert hasattr(Persons_Person, "firstname")
    descriptor = None
    for klass in Persons_Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)



def test_persons_persons_is_not_abstract():
    assert not inspect.isabstract(Persons_Persons)


def test_persons_persons_constructor_exists():
    assert callable(Persons_Persons.__init__)


def test_persons_persons_constructor_args():
    sig = inspect.signature(Persons_Persons.__init__)
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
Persons_Person_strategy = st.builds(
    Persons_Person,
    lastname=
        safe_text,
    gender=
        safe_text,
    firstname=
        safe_text
)
Persons_Persons_strategy = st.builds(
    Persons_Persons,
)

@given(instance=Persons_Person_strategy)
@settings(max_examples=50)
def test_persons_person_instantiation(instance):
    assert isinstance(instance, Persons_Person)



@given(instance=Persons_Person_strategy)
def test_persons_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=Persons_Person_strategy)
def test_persons_person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Persons_Person_strategy)
def test_persons_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=Persons_Persons_strategy)
@settings(max_examples=50)
def test_persons_persons_instantiation(instance):
    assert isinstance(instance, Persons_Persons)
