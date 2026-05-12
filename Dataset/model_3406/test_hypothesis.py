import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    menus_PersonDirectory,
    menus_Person,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_menus_persondirectory_is_not_abstract():
    assert not inspect.isabstract(menus_PersonDirectory)


def test_menus_persondirectory_constructor_exists():
    assert callable(menus_PersonDirectory.__init__)


def test_menus_persondirectory_constructor_args():
    sig = inspect.signature(menus_PersonDirectory.__init__)
    params = list(sig.parameters.keys())



def test_menus_person_is_not_abstract():
    assert not inspect.isabstract(menus_Person)


def test_menus_person_constructor_exists():
    assert callable(menus_Person.__init__)


def test_menus_person_constructor_args():
    sig = inspect.signature(menus_Person.__init__)
    params = list(sig.parameters.keys())
    assert "pregnant" in params, "Missing parameter 'pregnant'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_menus_person_has_pregnant():
    assert hasattr(menus_Person, "pregnant")
    descriptor = None
    for klass in menus_Person.__mro__:
        if "pregnant" in klass.__dict__:
            descriptor = klass.__dict__["pregnant"]
            break
    assert isinstance(descriptor, property)

def test_menus_person_has_lastname():
    assert hasattr(menus_Person, "lastname")
    descriptor = None
    for klass in menus_Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_menus_person_has_dateOfBirth():
    assert hasattr(menus_Person, "dateOfBirth")
    descriptor = None
    for klass in menus_Person.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_menus_person_has_sex():
    assert hasattr(menus_Person, "sex")
    descriptor = None
    for klass in menus_Person.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)

def test_menus_person_has_firstname():
    assert hasattr(menus_Person, "firstname")
    descriptor = None
    for klass in menus_Person.__mro__:
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
        "FEMALE",
        "UNSPECIFIED",
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
menus_PersonDirectory_strategy = st.builds(
    menus_PersonDirectory,
)
menus_Person_strategy = st.builds(
    menus_Person,
    pregnant=
        st.booleans(),
    lastname=
        safe_text,
    dateOfBirth=
        st.dates(),
    sex=
        safe_text,
    firstname=
        safe_text
)

@given(instance=menus_PersonDirectory_strategy)
@settings(max_examples=50)
def test_menus_persondirectory_instantiation(instance):
    assert isinstance(instance, menus_PersonDirectory)

@given(instance=menus_Person_strategy)
@settings(max_examples=50)
def test_menus_person_instantiation(instance):
    assert isinstance(instance, menus_Person)



@given(instance=menus_Person_strategy)
def test_menus_person_pregnant_setter(instance):
    original = instance.pregnant
    instance.pregnant = original
    assert instance.pregnant == original



@given(instance=menus_Person_strategy)
def test_menus_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=menus_Person_strategy)
def test_menus_person_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=menus_Person_strategy)
def test_menus_person_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=menus_Person_strategy)
def test_menus_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original
