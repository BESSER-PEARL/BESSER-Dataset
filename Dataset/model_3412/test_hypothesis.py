import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    people::Person,
    people::Universe,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_people::person_is_not_abstract():
    assert not inspect.isabstract(people::Person)


def test_people::person_constructor_exists():
    assert callable(people::Person.__init__)


def test_people::person_constructor_args():
    sig = inspect.signature(people::Person.__init__)
    params = list(sig.parameters.keys())
    assert "gender" in params, "Missing parameter 'gender'"
    assert "name" in params, "Missing parameter 'name'"

def test_people::person_has_gender():
    assert hasattr(people::Person, "gender")
    descriptor = None
    for klass in people::Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_people::person_has_name():
    assert hasattr(people::Person, "name")
    descriptor = None
    for klass in people::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_people::universe_is_not_abstract():
    assert not inspect.isabstract(people::Universe)


def test_people::universe_constructor_exists():
    assert callable(people::Universe.__init__)


def test_people::universe_constructor_args():
    sig = inspect.signature(people::Universe.__init__)
    params = list(sig.parameters.keys())

def test_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "MALE",
        "FEMALE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gender"


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
people::Person_strategy = st.builds(
    people::Person,
    gender=
        safe_text,
    name=
        safe_text
)
people::Universe_strategy = st.builds(
    people::Universe,
)

@given(instance=people::Person_strategy)
@settings(max_examples=50)
def test_people::person_instantiation(instance):
    assert isinstance(instance, people::Person)

@given(instance=people::Person_strategy)
def test_people::person_gender_type(instance):
    assert isinstance(instance.gender, str)


@given(instance=people::Person_strategy)
def test_people::person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original

@given(instance=people::Person_strategy)
def test_people::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=people::Person_strategy)
def test_people::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=people::Universe_strategy)
@settings(max_examples=50)
def test_people::universe_instantiation(instance):
    assert isinstance(instance, people::Universe)
