import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    SimplePersons::Female,
    SimplePersons::Male,
    SimplePersons::Person,
    SimplePersons::PersonRegister,
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



def test_simplepersons::female_is_not_abstract():
    assert not inspect.isabstract(SimplePersons::Female)


def test_simplepersons::female_constructor_exists():
    assert callable(SimplePersons::Female.__init__)


def test_simplepersons::female_constructor_args():
    sig = inspect.signature(SimplePersons::Female.__init__)
    params = list(sig.parameters.keys())



def test_simplepersons::male_is_not_abstract():
    assert not inspect.isabstract(SimplePersons::Male)


def test_simplepersons::male_constructor_exists():
    assert callable(SimplePersons::Male.__init__)


def test_simplepersons::male_constructor_args():
    sig = inspect.signature(SimplePersons::Male.__init__)
    params = list(sig.parameters.keys())



def test_simplepersons::person_is_not_abstract():
    assert not inspect.isabstract(SimplePersons::Person)


def test_simplepersons::person_constructor_exists():
    assert callable(SimplePersons::Person.__init__)


def test_simplepersons::person_constructor_args():
    sig = inspect.signature(SimplePersons::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplepersons::person_has_name():
    assert hasattr(SimplePersons::Person, "name")
    descriptor = None
    for klass in SimplePersons::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplepersons::personregister_is_not_abstract():
    assert not inspect.isabstract(SimplePersons::PersonRegister)


def test_simplepersons::personregister_constructor_exists():
    assert callable(SimplePersons::PersonRegister.__init__)


def test_simplepersons::personregister_constructor_args():
    sig = inspect.signature(SimplePersons::PersonRegister.__init__)
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
SimplePersons::Female_strategy = st.builds(
    SimplePersons::Female,
)
SimplePersons::Male_strategy = st.builds(
    SimplePersons::Male,
)
SimplePersons::Person_strategy = st.builds(
    SimplePersons::Person,
    name=
        safe_text
)
SimplePersons::PersonRegister_strategy = st.builds(
    SimplePersons::PersonRegister,
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=SimplePersons::Female_strategy)
@settings(max_examples=50)
def test_simplepersons::female_instantiation(instance):
    assert isinstance(instance, SimplePersons::Female)

@given(instance=SimplePersons::Male_strategy)
@settings(max_examples=50)
def test_simplepersons::male_instantiation(instance):
    assert isinstance(instance, SimplePersons::Male)

@given(instance=SimplePersons::Person_strategy)
@settings(max_examples=50)
def test_simplepersons::person_instantiation(instance):
    assert isinstance(instance, SimplePersons::Person)

@given(instance=SimplePersons::Person_strategy)
def test_simplepersons::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimplePersons::Person_strategy)
def test_simplepersons::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimplePersons::PersonRegister_strategy)
@settings(max_examples=50)
def test_simplepersons::personregister_instantiation(instance):
    assert isinstance(instance, SimplePersons::PersonRegister)
