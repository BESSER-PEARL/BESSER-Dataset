import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ExtendedFamilies::Person,
    ExtendedFamilies::Family,
    Person,
    ExtendedFamilies::Female,
    ExtendedFamilies::Male,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_extendedfamilies::person_is_not_abstract():
    assert not inspect.isabstract(ExtendedFamilies::Person)


def test_extendedfamilies::person_constructor_exists():
    assert callable(ExtendedFamilies::Person.__init__)


def test_extendedfamilies::person_constructor_args():
    sig = inspect.signature(ExtendedFamilies::Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_extendedfamilies::person_has_firstName():
    assert hasattr(ExtendedFamilies::Person, "firstName")
    descriptor = None
    for klass in ExtendedFamilies::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_extendedfamilies::family_is_not_abstract():
    assert not inspect.isabstract(ExtendedFamilies::Family)


def test_extendedfamilies::family_constructor_exists():
    assert callable(ExtendedFamilies::Family.__init__)


def test_extendedfamilies::family_constructor_args():
    sig = inspect.signature(ExtendedFamilies::Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_extendedfamilies::family_has_lastName():
    assert hasattr(ExtendedFamilies::Family, "lastName")
    descriptor = None
    for klass in ExtendedFamilies::Family.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_extendedfamilies::female_is_not_abstract():
    assert not inspect.isabstract(ExtendedFamilies::Female)


def test_extendedfamilies::female_constructor_exists():
    assert callable(ExtendedFamilies::Female.__init__)


def test_extendedfamilies::female_constructor_args():
    sig = inspect.signature(ExtendedFamilies::Female.__init__)
    params = list(sig.parameters.keys())



def test_extendedfamilies::male_is_not_abstract():
    assert not inspect.isabstract(ExtendedFamilies::Male)


def test_extendedfamilies::male_constructor_exists():
    assert callable(ExtendedFamilies::Male.__init__)


def test_extendedfamilies::male_constructor_args():
    sig = inspect.signature(ExtendedFamilies::Male.__init__)
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
ExtendedFamilies::Person_strategy = st.builds(
    ExtendedFamilies::Person,
    firstName=
        safe_text
)
ExtendedFamilies::Family_strategy = st.builds(
    ExtendedFamilies::Family,
    lastName=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
ExtendedFamilies::Female_strategy = st.builds(
    ExtendedFamilies::Female,
)
ExtendedFamilies::Male_strategy = st.builds(
    ExtendedFamilies::Male,
)

@given(instance=ExtendedFamilies::Person_strategy)
@settings(max_examples=50)
def test_extendedfamilies::person_instantiation(instance):
    assert isinstance(instance, ExtendedFamilies::Person)

@given(instance=ExtendedFamilies::Person_strategy)
def test_extendedfamilies::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=ExtendedFamilies::Person_strategy)
def test_extendedfamilies::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=ExtendedFamilies::Family_strategy)
@settings(max_examples=50)
def test_extendedfamilies::family_instantiation(instance):
    assert isinstance(instance, ExtendedFamilies::Family)

@given(instance=ExtendedFamilies::Family_strategy)
def test_extendedfamilies::family_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=ExtendedFamilies::Family_strategy)
def test_extendedfamilies::family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=ExtendedFamilies::Female_strategy)
@settings(max_examples=50)
def test_extendedfamilies::female_instantiation(instance):
    assert isinstance(instance, ExtendedFamilies::Female)

@given(instance=ExtendedFamilies::Male_strategy)
@settings(max_examples=50)
def test_extendedfamilies::male_instantiation(instance):
    assert isinstance(instance, ExtendedFamilies::Male)
