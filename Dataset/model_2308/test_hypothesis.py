import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Persons_LocatedElement,
    Persons_PersonsModel,
    Person,
    Persons_Female,
    Persons_Male,
    PersonsModel,
    Persons_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_persons_locatedelement_is_not_abstract():
    assert not inspect.isabstract(Persons_LocatedElement)


def test_persons_locatedelement_constructor_exists():
    assert callable(Persons_LocatedElement.__init__)


def test_persons_locatedelement_constructor_args():
    sig = inspect.signature(Persons_LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_persons_personsmodel_is_not_abstract():
    assert not inspect.isabstract(Persons_PersonsModel)


def test_persons_personsmodel_constructor_exists():
    assert callable(Persons_PersonsModel.__init__)


def test_persons_personsmodel_constructor_args():
    sig = inspect.signature(Persons_PersonsModel.__init__)
    params = list(sig.parameters.keys())



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



def test_personsmodel_is_not_abstract():
    assert not inspect.isabstract(PersonsModel)


def test_personsmodel_constructor_exists():
    assert callable(PersonsModel.__init__)


def test_personsmodel_constructor_args():
    sig = inspect.signature(PersonsModel.__init__)
    params = list(sig.parameters.keys())



def test_persons_person_is_not_abstract():
    assert not inspect.isabstract(Persons_Person)


def test_persons_person_constructor_exists():
    assert callable(Persons_Person.__init__)


def test_persons_person_constructor_args():
    sig = inspect.signature(Persons_Person.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_persons_person_has_fullName():
    assert hasattr(Persons_Person, "fullName")
    descriptor = None
    for klass in Persons_Person.__mro__:
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
Persons_LocatedElement_strategy = st.builds(
    Persons_LocatedElement,
)
Persons_PersonsModel_strategy = st.builds(
    Persons_PersonsModel,
)
Person_strategy = st.builds(
    Person,
)
Persons_Female_strategy = st.builds(
    Persons_Female,
)
Persons_Male_strategy = st.builds(
    Persons_Male,
)
PersonsModel_strategy = st.builds(
    PersonsModel,
)
Persons_Person_strategy = st.builds(
    Persons_Person,
    fullName=
        safe_text
)

@given(instance=Persons_LocatedElement_strategy)
@settings(max_examples=50)
def test_persons_locatedelement_instantiation(instance):
    assert isinstance(instance, Persons_LocatedElement)

@given(instance=Persons_PersonsModel_strategy)
@settings(max_examples=50)
def test_persons_personsmodel_instantiation(instance):
    assert isinstance(instance, Persons_PersonsModel)

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

@given(instance=PersonsModel_strategy)
@settings(max_examples=50)
def test_personsmodel_instantiation(instance):
    assert isinstance(instance, PersonsModel)

@given(instance=Persons_Person_strategy)
@settings(max_examples=50)
def test_persons_person_instantiation(instance):
    assert isinstance(instance, Persons_Person)



@given(instance=Persons_Person_strategy)
def test_persons_person_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original
