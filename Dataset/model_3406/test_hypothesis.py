import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    menus::PersonDirectory,
    menus::Person,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_menus::persondirectory_is_not_abstract():
    assert not inspect.isabstract(menus::PersonDirectory)


def test_menus::persondirectory_constructor_exists():
    assert callable(menus::PersonDirectory.__init__)


def test_menus::persondirectory_constructor_args():
    sig = inspect.signature(menus::PersonDirectory.__init__)
    params = list(sig.parameters.keys())



def test_menus::person_is_not_abstract():
    assert not inspect.isabstract(menus::Person)


def test_menus::person_constructor_exists():
    assert callable(menus::Person.__init__)


def test_menus::person_constructor_args():
    sig = inspect.signature(menus::Person.__init__)
    params = list(sig.parameters.keys())
    assert "pregnant" in params, "Missing parameter 'pregnant'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_menus::person_has_pregnant():
    assert hasattr(menus::Person, "pregnant")
    descriptor = None
    for klass in menus::Person.__mro__:
        if "pregnant" in klass.__dict__:
            descriptor = klass.__dict__["pregnant"]
            break
    assert isinstance(descriptor, property)

def test_menus::person_has_dateOfBirth():
    assert hasattr(menus::Person, "dateOfBirth")
    descriptor = None
    for klass in menus::Person.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_menus::person_has_lastname():
    assert hasattr(menus::Person, "lastname")
    descriptor = None
    for klass in menus::Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_menus::person_has_sex():
    assert hasattr(menus::Person, "sex")
    descriptor = None
    for klass in menus::Person.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)

def test_menus::person_has_firstname():
    assert hasattr(menus::Person, "firstname")
    descriptor = None
    for klass in menus::Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "UNSPECIFIED",
        "FEMALE",
        "MALE",
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
menus::PersonDirectory_strategy = st.builds(
    menus::PersonDirectory,
)
menus::Person_strategy = st.builds(
    menus::Person,
    pregnant=
        st.booleans(),
    dateOfBirth=
        st.dates(),
    lastname=
        safe_text,
    sex=
        safe_text,
    firstname=
        safe_text
)

@given(instance=menus::PersonDirectory_strategy)
@settings(max_examples=50)
def test_menus::persondirectory_instantiation(instance):
    assert isinstance(instance, menus::PersonDirectory)

@given(instance=menus::Person_strategy)
@settings(max_examples=50)
def test_menus::person_instantiation(instance):
    assert isinstance(instance, menus::Person)

@given(instance=menus::Person_strategy)
def test_menus::person_pregnant_type(instance):
    assert isinstance(instance.pregnant, bool)


@given(instance=menus::Person_strategy)
def test_menus::person_pregnant_setter(instance):
    original = instance.pregnant
    instance.pregnant = original
    assert instance.pregnant == original

@given(instance=menus::Person_strategy)
def test_menus::person_dateOfBirth_type(instance):
    assert isinstance(instance.dateOfBirth, date)


@given(instance=menus::Person_strategy)
def test_menus::person_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original

@given(instance=menus::Person_strategy)
def test_menus::person_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=menus::Person_strategy)
def test_menus::person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=menus::Person_strategy)
def test_menus::person_sex_type(instance):
    assert isinstance(instance.sex, str)


@given(instance=menus::Person_strategy)
def test_menus::person_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original

@given(instance=menus::Person_strategy)
def test_menus::person_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=menus::Person_strategy)
def test_menus::person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original
