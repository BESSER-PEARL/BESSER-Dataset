import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    company::Person,
    company::Company,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_company::person_is_not_abstract():
    assert not inspect.isabstract(company::Person)


def test_company::person_constructor_exists():
    assert callable(company::Person.__init__)


def test_company::person_constructor_args():
    sig = inspect.signature(company::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"
    assert "isUnemployed" in params, "Missing parameter 'isUnemployed'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "salary" in params, "Missing parameter 'salary'"
    assert "lastname" in params, "Missing parameter 'lastname'"

def test_company::person_has_name():
    assert hasattr(company::Person, "name")
    descriptor = None
    for klass in company::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company::person_has_age():
    assert hasattr(company::Person, "age")
    descriptor = None
    for klass in company::Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_company::person_has_isUnemployed():
    assert hasattr(company::Person, "isUnemployed")
    descriptor = None
    for klass in company::Person.__mro__:
        if "isUnemployed" in klass.__dict__:
            descriptor = klass.__dict__["isUnemployed"]
            break
    assert isinstance(descriptor, property)

def test_company::person_has_gender():
    assert hasattr(company::Person, "gender")
    descriptor = None
    for klass in company::Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_company::person_has_salary():
    assert hasattr(company::Person, "salary")
    descriptor = None
    for klass in company::Person.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_company::person_has_lastname():
    assert hasattr(company::Person, "lastname")
    descriptor = None
    for klass in company::Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)



def test_company::company_is_not_abstract():
    assert not inspect.isabstract(company::Company)


def test_company::company_constructor_exists():
    assert callable(company::Company.__init__)


def test_company::company_constructor_args():
    sig = inspect.signature(company::Company.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfManager" in params, "Missing parameter 'numberOfManager'"
    assert "name" in params, "Missing parameter 'name'"

def test_company::company_has_numberOfManager():
    assert hasattr(company::Company, "numberOfManager")
    descriptor = None
    for klass in company::Company.__mro__:
        if "numberOfManager" in klass.__dict__:
            descriptor = klass.__dict__["numberOfManager"]
            break
    assert isinstance(descriptor, property)

def test_company::company_has_name():
    assert hasattr(company::Company, "name")
    descriptor = None
    for klass in company::Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "male",
        "female",
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
company::Person_strategy = st.builds(
    company::Person,
    name=
        safe_text,
    age=
        st.integers(),
    isUnemployed=
        st.booleans(),
    gender=
        safe_text,
    salary=
        st.integers(),
    lastname=
        safe_text
)
company::Company_strategy = st.builds(
    company::Company,
    numberOfManager=
        st.integers(),
    name=
        safe_text
)

@given(instance=company::Person_strategy)
@settings(max_examples=50)
def test_company::person_instantiation(instance):
    assert isinstance(instance, company::Person)

@given(instance=company::Person_strategy)
def test_company::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=company::Person_strategy)
def test_company::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=company::Person_strategy)
def test_company::person_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=company::Person_strategy)
def test_company::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=company::Person_strategy)
def test_company::person_isUnemployed_type(instance):
    assert isinstance(instance.isUnemployed, bool)


@given(instance=company::Person_strategy)
def test_company::person_isUnemployed_setter(instance):
    original = instance.isUnemployed
    instance.isUnemployed = original
    assert instance.isUnemployed == original

@given(instance=company::Person_strategy)
def test_company::person_gender_type(instance):
    assert isinstance(instance.gender, str)


@given(instance=company::Person_strategy)
def test_company::person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original

@given(instance=company::Person_strategy)
def test_company::person_salary_type(instance):
    assert isinstance(instance.salary, int)


@given(instance=company::Person_strategy)
def test_company::person_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=company::Person_strategy)
def test_company::person_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=company::Person_strategy)
def test_company::person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=company::Company_strategy)
@settings(max_examples=50)
def test_company::company_instantiation(instance):
    assert isinstance(instance, company::Company)

@given(instance=company::Company_strategy)
def test_company::company_numberOfManager_type(instance):
    assert isinstance(instance.numberOfManager, int)


@given(instance=company::Company_strategy)
def test_company::company_numberOfManager_setter(instance):
    original = instance.numberOfManager
    instance.numberOfManager = original
    assert instance.numberOfManager == original

@given(instance=company::Company_strategy)
def test_company::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=company::Company_strategy)
def test_company::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
