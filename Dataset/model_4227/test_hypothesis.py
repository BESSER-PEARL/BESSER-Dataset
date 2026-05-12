import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    company_NamedElement,
    NamedElement,
    company_Person,
    company_Department,
    company_Company,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_company_namedelement_is_not_abstract():
    assert not inspect.isabstract(company_NamedElement)


def test_company_namedelement_constructor_exists():
    assert callable(company_NamedElement.__init__)


def test_company_namedelement_constructor_args():
    sig = inspect.signature(company_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company_namedelement_has_name():
    assert hasattr(company_NamedElement, "name")
    descriptor = None
    for klass in company_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_company_person_is_not_abstract():
    assert not inspect.isabstract(company_Person)


def test_company_person_constructor_exists():
    assert callable(company_Person.__init__)


def test_company_person_constructor_args():
    sig = inspect.signature(company_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "fullName" in params, "Missing parameter 'fullName'"
    assert "age" in params, "Missing parameter 'age'"

def test_company_person_has_firstName():
    assert hasattr(company_Person, "firstName")
    descriptor = None
    for klass in company_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_company_person_has_fullName():
    assert hasattr(company_Person, "fullName")
    descriptor = None
    for klass in company_Person.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
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



def test_company_department_is_not_abstract():
    assert not inspect.isabstract(company_Department)


def test_company_department_constructor_exists():
    assert callable(company_Department.__init__)


def test_company_department_constructor_args():
    sig = inspect.signature(company_Department.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfEmployees" in params, "Missing parameter 'numberOfEmployees'"
    assert "ageSumOfEmployees" in params, "Missing parameter 'ageSumOfEmployees'"

def test_company_department_has_numberOfEmployees():
    assert hasattr(company_Department, "numberOfEmployees")
    descriptor = None
    for klass in company_Department.__mro__:
        if "numberOfEmployees" in klass.__dict__:
            descriptor = klass.__dict__["numberOfEmployees"]
            break
    assert isinstance(descriptor, property)

def test_company_department_has_ageSumOfEmployees():
    assert hasattr(company_Department, "ageSumOfEmployees")
    descriptor = None
    for klass in company_Department.__mro__:
        if "ageSumOfEmployees" in klass.__dict__:
            descriptor = klass.__dict__["ageSumOfEmployees"]
            break
    assert isinstance(descriptor, property)



def test_company_company_is_not_abstract():
    assert not inspect.isabstract(company_Company)


def test_company_company_constructor_exists():
    assert callable(company_Company.__init__)


def test_company_company_constructor_args():
    sig = inspect.signature(company_Company.__init__)
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
company_NamedElement_strategy = st.builds(
    company_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
company_Person_strategy = st.builds(
    company_Person,
    firstName=
        safe_text,
    fullName=
        safe_text,
    age=
        st.integers()
)
company_Department_strategy = st.builds(
    company_Department,
    numberOfEmployees=
        st.integers(),
    ageSumOfEmployees=
        st.integers()
)
company_Company_strategy = st.builds(
    company_Company,
)

@given(instance=company_NamedElement_strategy)
@settings(max_examples=50)
def test_company_namedelement_instantiation(instance):
    assert isinstance(instance, company_NamedElement)



@given(instance=company_NamedElement_strategy)
def test_company_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=company_Person_strategy)
@settings(max_examples=50)
def test_company_person_instantiation(instance):
    assert isinstance(instance, company_Person)



@given(instance=company_Person_strategy)
def test_company_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=company_Person_strategy)
def test_company_person_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original



@given(instance=company_Person_strategy)
def test_company_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=company_Department_strategy)
@settings(max_examples=50)
def test_company_department_instantiation(instance):
    assert isinstance(instance, company_Department)



@given(instance=company_Department_strategy)
def test_company_department_numberOfEmployees_setter(instance):
    original = instance.numberOfEmployees
    instance.numberOfEmployees = original
    assert instance.numberOfEmployees == original



@given(instance=company_Department_strategy)
def test_company_department_ageSumOfEmployees_setter(instance):
    original = instance.ageSumOfEmployees
    instance.ageSumOfEmployees = original
    assert instance.ageSumOfEmployees == original

@given(instance=company_Company_strategy)
@settings(max_examples=50)
def test_company_company_instantiation(instance):
    assert isinstance(instance, company_Company)
