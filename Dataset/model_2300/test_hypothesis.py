import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    persons::Female,
    persons::Male,
    persons::Person,
    persons::PersonRegister,
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



def test_persons::female_is_not_abstract():
    assert not inspect.isabstract(persons::Female)


def test_persons::female_constructor_exists():
    assert callable(persons::Female.__init__)


def test_persons::female_constructor_args():
    sig = inspect.signature(persons::Female.__init__)
    params = list(sig.parameters.keys())



def test_persons::male_is_not_abstract():
    assert not inspect.isabstract(persons::Male)


def test_persons::male_constructor_exists():
    assert callable(persons::Male.__init__)


def test_persons::male_constructor_args():
    sig = inspect.signature(persons::Male.__init__)
    params = list(sig.parameters.keys())



def test_persons::person_is_not_abstract():
    assert not inspect.isabstract(persons::Person)


def test_persons::person_constructor_exists():
    assert callable(persons::Person.__init__)


def test_persons::person_constructor_args():
    sig = inspect.signature(persons::Person.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"
    assert "birthday" in params, "Missing parameter 'birthday'"

def test_persons::person_has_fullName():
    assert hasattr(persons::Person, "fullName")
    descriptor = None
    for klass in persons::Person.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)

def test_persons::person_has_birthday():
    assert hasattr(persons::Person, "birthday")
    descriptor = None
    for klass in persons::Person.__mro__:
        if "birthday" in klass.__dict__:
            descriptor = klass.__dict__["birthday"]
            break
    assert isinstance(descriptor, property)



def test_persons::personregister_is_not_abstract():
    assert not inspect.isabstract(persons::PersonRegister)


def test_persons::personregister_constructor_exists():
    assert callable(persons::PersonRegister.__init__)


def test_persons::personregister_constructor_args():
    sig = inspect.signature(persons::PersonRegister.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_persons::personregister_has_id():
    assert hasattr(persons::PersonRegister, "id")
    descriptor = None
    for klass in persons::PersonRegister.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
persons::Female_strategy = st.builds(
    persons::Female,
)
persons::Male_strategy = st.builds(
    persons::Male,
)
persons::Person_strategy = st.builds(
    persons::Person,
    fullName=
        safe_text,
    birthday=
        st.dates()
)
persons::PersonRegister_strategy = st.builds(
    persons::PersonRegister,
    id=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=persons::Female_strategy)
@settings(max_examples=50)
def test_persons::female_instantiation(instance):
    assert isinstance(instance, persons::Female)

@given(instance=persons::Male_strategy)
@settings(max_examples=50)
def test_persons::male_instantiation(instance):
    assert isinstance(instance, persons::Male)

@given(instance=persons::Person_strategy)
@settings(max_examples=50)
def test_persons::person_instantiation(instance):
    assert isinstance(instance, persons::Person)

@given(instance=persons::Person_strategy)
def test_persons::person_fullName_type(instance):
    assert isinstance(instance.fullName, str)


@given(instance=persons::Person_strategy)
def test_persons::person_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=persons::Person_strategy)
def test_persons::person_birthday_type(instance):
    assert isinstance(instance.birthday, date)


@given(instance=persons::Person_strategy)
def test_persons::person_birthday_setter(instance):
    original = instance.birthday
    instance.birthday = original
    assert instance.birthday == original

@given(instance=persons::PersonRegister_strategy)
@settings(max_examples=50)
def test_persons::personregister_instantiation(instance):
    assert isinstance(instance, persons::PersonRegister)

@given(instance=persons::PersonRegister_strategy)
def test_persons::personregister_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=persons::PersonRegister_strategy)
def test_persons::personregister_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
