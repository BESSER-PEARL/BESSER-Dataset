import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    persons_Female,
    persons_Male,
    persons_Person,
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
    assert not inspect.isabstract(persons_Female)


def test_persons_female_constructor_exists():
    assert callable(persons_Female.__init__)


def test_persons_female_constructor_args():
    sig = inspect.signature(persons_Female.__init__)
    params = list(sig.parameters.keys())



def test_persons_male_is_not_abstract():
    assert not inspect.isabstract(persons_Male)


def test_persons_male_constructor_exists():
    assert callable(persons_Male.__init__)


def test_persons_male_constructor_args():
    sig = inspect.signature(persons_Male.__init__)
    params = list(sig.parameters.keys())



def test_persons_person_is_not_abstract():
    assert not inspect.isabstract(persons_Person)


def test_persons_person_constructor_exists():
    assert callable(persons_Person.__init__)


def test_persons_person_constructor_args():
    sig = inspect.signature(persons_Person.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_persons_person_has_fullName():
    assert hasattr(persons_Person, "fullName")
    descriptor = None
    for klass in persons_Person.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
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
persons_Female_strategy = st.builds(
    persons_Female,
)
persons_Male_strategy = st.builds(
    persons_Male,
)
persons_Person_strategy = st.builds(
    persons_Person,
    fullName=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=persons_Female_strategy)
@settings(max_examples=50)
def test_persons_female_instantiation(instance):
    assert isinstance(instance, persons_Female)

@given(instance=persons_Male_strategy)
@settings(max_examples=50)
def test_persons_male_instantiation(instance):
    assert isinstance(instance, persons_Male)

@given(instance=persons_Person_strategy)
@settings(max_examples=50)
def test_persons_person_instantiation(instance):
    assert isinstance(instance, persons_Person)



@given(instance=persons_Person_strategy)
def test_persons_person_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original
