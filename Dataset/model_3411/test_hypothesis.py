import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    people_Universe,
    people_Person,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_people_universe_is_not_abstract():
    assert not inspect.isabstract(people_Universe)


def test_people_universe_constructor_exists():
    assert callable(people_Universe.__init__)


def test_people_universe_constructor_args():
    sig = inspect.signature(people_Universe.__init__)
    params = list(sig.parameters.keys())



def test_people_person_is_not_abstract():
    assert not inspect.isabstract(people_Person)


def test_people_person_constructor_exists():
    assert callable(people_Person.__init__)


def test_people_person_constructor_args():
    sig = inspect.signature(people_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "gender" in params, "Missing parameter 'gender'"

def test_people_person_has_name():
    assert hasattr(people_Person, "name")
    descriptor = None
    for klass in people_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_people_person_has_gender():
    assert hasattr(people_Person, "gender")
    descriptor = None
    for klass in people_Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

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
people_Universe_strategy = st.builds(
    people_Universe,
)
people_Person_strategy = st.builds(
    people_Person,
    name=
        safe_text,
    gender=
        safe_text
)

@given(instance=people_Universe_strategy)
@settings(max_examples=50)
def test_people_universe_instantiation(instance):
    assert isinstance(instance, people_Universe)

@given(instance=people_Person_strategy)
@settings(max_examples=50)
def test_people_person_instantiation(instance):
    assert isinstance(instance, people_Person)



@given(instance=people_Person_strategy)
def test_people_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=people_Person_strategy)
def test_people_person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original
