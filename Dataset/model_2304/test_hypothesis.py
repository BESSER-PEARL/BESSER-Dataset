import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Persons::PersonsModel,
    Person,
    Persons::Female,
    Persons::Male,
    PersonsModel,
    Persons::Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_persons::personsmodel_is_not_abstract():
    assert not inspect.isabstract(Persons::PersonsModel)


def test_persons::personsmodel_constructor_exists():
    assert callable(Persons::PersonsModel.__init__)


def test_persons::personsmodel_constructor_args():
    sig = inspect.signature(Persons::PersonsModel.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_persons::female_is_not_abstract():
    assert not inspect.isabstract(Persons::Female)


def test_persons::female_constructor_exists():
    assert callable(Persons::Female.__init__)


def test_persons::female_constructor_args():
    sig = inspect.signature(Persons::Female.__init__)
    params = list(sig.parameters.keys())



def test_persons::male_is_not_abstract():
    assert not inspect.isabstract(Persons::Male)


def test_persons::male_constructor_exists():
    assert callable(Persons::Male.__init__)


def test_persons::male_constructor_args():
    sig = inspect.signature(Persons::Male.__init__)
    params = list(sig.parameters.keys())



def test_personsmodel_is_not_abstract():
    assert not inspect.isabstract(PersonsModel)


def test_personsmodel_constructor_exists():
    assert callable(PersonsModel.__init__)


def test_personsmodel_constructor_args():
    sig = inspect.signature(PersonsModel.__init__)
    params = list(sig.parameters.keys())



def test_persons::person_is_not_abstract():
    assert not inspect.isabstract(Persons::Person)


def test_persons::person_constructor_exists():
    assert callable(Persons::Person.__init__)


def test_persons::person_constructor_args():
    sig = inspect.signature(Persons::Person.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_persons::person_has_fullName():
    assert hasattr(Persons::Person, "fullName")
    descriptor = None
    for klass in Persons::Person.__mro__:
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
Persons::PersonsModel_strategy = st.builds(
    Persons::PersonsModel,
)
Person_strategy = st.builds(
    Person,
)
Persons::Female_strategy = st.builds(
    Persons::Female,
)
Persons::Male_strategy = st.builds(
    Persons::Male,
)
PersonsModel_strategy = st.builds(
    PersonsModel,
)
Persons::Person_strategy = st.builds(
    Persons::Person,
    fullName=
        safe_text
)

@given(instance=Persons::PersonsModel_strategy)
@settings(max_examples=50)
def test_persons::personsmodel_instantiation(instance):
    assert isinstance(instance, Persons::PersonsModel)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=Persons::Female_strategy)
@settings(max_examples=50)
def test_persons::female_instantiation(instance):
    assert isinstance(instance, Persons::Female)

@given(instance=Persons::Male_strategy)
@settings(max_examples=50)
def test_persons::male_instantiation(instance):
    assert isinstance(instance, Persons::Male)

@given(instance=PersonsModel_strategy)
@settings(max_examples=50)
def test_personsmodel_instantiation(instance):
    assert isinstance(instance, PersonsModel)

@given(instance=Persons::Person_strategy)
@settings(max_examples=50)
def test_persons::person_instantiation(instance):
    assert isinstance(instance, Persons::Person)

@given(instance=Persons::Person_strategy)
def test_persons::person_fullName_type(instance):
    assert isinstance(instance.fullName, str)


@given(instance=Persons::Person_strategy)
def test_persons::person_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original
