import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    SimplePersons_Female,
    SimplePersons_Male,
    SimplePersons_Person,
    SimplePersons_PersonRegister,
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



def test_simplepersons_female_is_not_abstract():
    assert not inspect.isabstract(SimplePersons_Female)


def test_simplepersons_female_constructor_exists():
    assert callable(SimplePersons_Female.__init__)


def test_simplepersons_female_constructor_args():
    sig = inspect.signature(SimplePersons_Female.__init__)
    params = list(sig.parameters.keys())



def test_simplepersons_male_is_not_abstract():
    assert not inspect.isabstract(SimplePersons_Male)


def test_simplepersons_male_constructor_exists():
    assert callable(SimplePersons_Male.__init__)


def test_simplepersons_male_constructor_args():
    sig = inspect.signature(SimplePersons_Male.__init__)
    params = list(sig.parameters.keys())



def test_simplepersons_person_is_not_abstract():
    assert not inspect.isabstract(SimplePersons_Person)


def test_simplepersons_person_constructor_exists():
    assert callable(SimplePersons_Person.__init__)


def test_simplepersons_person_constructor_args():
    sig = inspect.signature(SimplePersons_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplepersons_person_has_name():
    assert hasattr(SimplePersons_Person, "name")
    descriptor = None
    for klass in SimplePersons_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplepersons_personregister_is_not_abstract():
    assert not inspect.isabstract(SimplePersons_PersonRegister)


def test_simplepersons_personregister_constructor_exists():
    assert callable(SimplePersons_PersonRegister.__init__)


def test_simplepersons_personregister_constructor_args():
    sig = inspect.signature(SimplePersons_PersonRegister.__init__)
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
SimplePersons_Female_strategy = st.builds(
    SimplePersons_Female,
)
SimplePersons_Male_strategy = st.builds(
    SimplePersons_Male,
)
SimplePersons_Person_strategy = st.builds(
    SimplePersons_Person,
    name=
        safe_text
)
SimplePersons_PersonRegister_strategy = st.builds(
    SimplePersons_PersonRegister,
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=SimplePersons_Female_strategy)
@settings(max_examples=50)
def test_simplepersons_female_instantiation(instance):
    assert isinstance(instance, SimplePersons_Female)

@given(instance=SimplePersons_Male_strategy)
@settings(max_examples=50)
def test_simplepersons_male_instantiation(instance):
    assert isinstance(instance, SimplePersons_Male)

@given(instance=SimplePersons_Person_strategy)
@settings(max_examples=50)
def test_simplepersons_person_instantiation(instance):
    assert isinstance(instance, SimplePersons_Person)



@given(instance=SimplePersons_Person_strategy)
def test_simplepersons_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimplePersons_PersonRegister_strategy)
@settings(max_examples=50)
def test_simplepersons_personregister_instantiation(instance):
    assert isinstance(instance, SimplePersons_PersonRegister)
