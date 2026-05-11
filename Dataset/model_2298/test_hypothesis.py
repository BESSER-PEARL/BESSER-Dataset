import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    Persons::Female,
    Persons::Male,
    Persons::Person,
    Persons::PersonRegister,
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



def test_persons::person_is_not_abstract():
    assert not inspect.isabstract(Persons::Person)


def test_persons::person_constructor_exists():
    assert callable(Persons::Person.__init__)


def test_persons::person_constructor_args():
    sig = inspect.signature(Persons::Person.__init__)
    params = list(sig.parameters.keys())
    assert "birthday" in params, "Missing parameter 'birthday'"
    assert "name" in params, "Missing parameter 'name'"

def test_persons::person_has_birthday():
    assert hasattr(Persons::Person, "birthday")
    descriptor = None
    for klass in Persons::Person.__mro__:
        if "birthday" in klass.__dict__:
            descriptor = klass.__dict__["birthday"]
            break
    assert isinstance(descriptor, property)

def test_persons::person_has_name():
    assert hasattr(Persons::Person, "name")
    descriptor = None
    for klass in Persons::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_persons::personregister_is_not_abstract():
    assert not inspect.isabstract(Persons::PersonRegister)


def test_persons::personregister_constructor_exists():
    assert callable(Persons::PersonRegister.__init__)


def test_persons::personregister_constructor_args():
    sig = inspect.signature(Persons::PersonRegister.__init__)
    params = list(sig.parameters.keys())


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
Persons::Female_strategy = st.builds(
    Persons::Female,
)
Persons::Male_strategy = st.builds(
    Persons::Male,
)
Persons::Person_strategy = st.builds(
    Persons::Person,
    birthday=
        st.dates(),
    name=
        safe_text
)
Persons::PersonRegister_strategy = st.builds(
    Persons::PersonRegister,
)

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

@given(instance=Persons::Person_strategy)
@settings(max_examples=50)
def test_persons::person_instantiation(instance):
    assert isinstance(instance, Persons::Person)

@given(instance=Persons::Person_strategy)
def test_persons::person_birthday_type(instance):
    assert isinstance(instance.birthday, date)


@given(instance=Persons::Person_strategy)
def test_persons::person_birthday_setter(instance):
    original = instance.birthday
    instance.birthday = original
    assert instance.birthday == original

@given(instance=Persons::Person_strategy)
def test_persons::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Persons::Person_strategy)
def test_persons::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Persons::PersonRegister_strategy)
@settings(max_examples=50)
def test_persons::personregister_instantiation(instance):
    assert isinstance(instance, Persons::PersonRegister)
