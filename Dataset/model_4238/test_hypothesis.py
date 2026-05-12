import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    company_Person,
    company_Company,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_company_person_is_not_abstract():
    assert not inspect.isabstract(company_Person)


def test_company_person_constructor_exists():
    assert callable(company_Person.__init__)


def test_company_person_constructor_args():
    sig = inspect.signature(company_Person.__init__)
    params = list(sig.parameters.keys())
    assert "gender" in params, "Missing parameter 'gender'"
    assert "salary" in params, "Missing parameter 'salary'"
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isUnemployed" in params, "Missing parameter 'isUnemployed'"
    assert "lastname" in params, "Missing parameter 'lastname'"

def test_company_person_has_gender():
    assert hasattr(company_Person, "gender")
    descriptor = None
    for klass in company_Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_company_person_has_salary():
    assert hasattr(company_Person, "salary")
    descriptor = None
    for klass in company_Person.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_company_person_has_age():
    assert hasattr(company_Person, "age")
    descriptor = None
    for klass in company_Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_company_person_has_name():
    assert hasattr(company_Person, "name")
    descriptor = None
    for klass in company_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company_person_has_isUnemployed():
    assert hasattr(company_Person, "isUnemployed")
    descriptor = None
    for klass in company_Person.__mro__:
        if "isUnemployed" in klass.__dict__:
            descriptor = klass.__dict__["isUnemployed"]
            break
    assert isinstance(descriptor, property)

def test_company_person_has_lastname():
    assert hasattr(company_Person, "lastname")
    descriptor = None
    for klass in company_Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)



def test_company_company_is_not_abstract():
    assert not inspect.isabstract(company_Company)


def test_company_company_constructor_exists():
    assert callable(company_Company.__init__)


def test_company_company_constructor_args():
    sig = inspect.signature(company_Company.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfManager" in params, "Missing parameter 'numberOfManager'"
    assert "name" in params, "Missing parameter 'name'"

def test_company_company_has_numberOfManager():
    assert hasattr(company_Company, "numberOfManager")
    descriptor = None
    for klass in company_Company.__mro__:
        if "numberOfManager" in klass.__dict__:
            descriptor = klass.__dict__["numberOfManager"]
            break
    assert isinstance(descriptor, property)

def test_company_company_has_name():
    assert hasattr(company_Company, "name")
    descriptor = None
    for klass in company_Company.__mro__:
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
company_Person_strategy = st.builds(
    company_Person,
    gender=
        safe_text,
    salary=
        st.integers(),
    age=
        st.integers(),
    name=
        safe_text,
    isUnemployed=
        st.booleans(),
    lastname=
        safe_text
)
company_Company_strategy = st.builds(
    company_Company,
    numberOfManager=
        st.integers(),
    name=
        safe_text
)

@given(instance=company_Person_strategy)
@settings(max_examples=50)
def test_company_person_instantiation(instance):
    assert isinstance(instance, company_Person)



@given(instance=company_Person_strategy)
def test_company_person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=company_Person_strategy)
def test_company_person_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original



@given(instance=company_Person_strategy)
def test_company_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=company_Person_strategy)
def test_company_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=company_Person_strategy)
def test_company_person_isUnemployed_setter(instance):
    original = instance.isUnemployed
    instance.isUnemployed = original
    assert instance.isUnemployed == original



@given(instance=company_Person_strategy)
def test_company_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=company_Company_strategy)
@settings(max_examples=50)
def test_company_company_instantiation(instance):
    assert isinstance(instance, company_Company)



@given(instance=company_Company_strategy)
def test_company_company_numberOfManager_setter(instance):
    original = instance.numberOfManager
    instance.numberOfManager = original
    assert instance.numberOfManager == original



@given(instance=company_Company_strategy)
def test_company_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
