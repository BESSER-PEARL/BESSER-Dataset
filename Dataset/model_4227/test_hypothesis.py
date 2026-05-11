import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    company::NamedElement,
    NamedElement,
    company::Person,
    company::Department,
    company::Company,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_company::namedelement_is_not_abstract():
    assert not inspect.isabstract(company::NamedElement)


def test_company::namedelement_constructor_exists():
    assert callable(company::NamedElement.__init__)


def test_company::namedelement_constructor_args():
    sig = inspect.signature(company::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company::namedelement_has_name():
    assert hasattr(company::NamedElement, "name")
    descriptor = None
    for klass in company::NamedElement.__mro__:
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



def test_company::person_is_not_abstract():
    assert not inspect.isabstract(company::Person)


def test_company::person_constructor_exists():
    assert callable(company::Person.__init__)


def test_company::person_constructor_args():
    sig = inspect.signature(company::Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "fullName" in params, "Missing parameter 'fullName'"
    assert "age" in params, "Missing parameter 'age'"

def test_company::person_has_firstName():
    assert hasattr(company::Person, "firstName")
    descriptor = None
    for klass in company::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_company::person_has_fullName():
    assert hasattr(company::Person, "fullName")
    descriptor = None
    for klass in company::Person.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
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



def test_company::department_is_not_abstract():
    assert not inspect.isabstract(company::Department)


def test_company::department_constructor_exists():
    assert callable(company::Department.__init__)


def test_company::department_constructor_args():
    sig = inspect.signature(company::Department.__init__)
    params = list(sig.parameters.keys())
    assert "ageSumOfEmployees" in params, "Missing parameter 'ageSumOfEmployees'"
    assert "numberOfEmployees" in params, "Missing parameter 'numberOfEmployees'"

def test_company::department_has_ageSumOfEmployees():
    assert hasattr(company::Department, "ageSumOfEmployees")
    descriptor = None
    for klass in company::Department.__mro__:
        if "ageSumOfEmployees" in klass.__dict__:
            descriptor = klass.__dict__["ageSumOfEmployees"]
            break
    assert isinstance(descriptor, property)

def test_company::department_has_numberOfEmployees():
    assert hasattr(company::Department, "numberOfEmployees")
    descriptor = None
    for klass in company::Department.__mro__:
        if "numberOfEmployees" in klass.__dict__:
            descriptor = klass.__dict__["numberOfEmployees"]
            break
    assert isinstance(descriptor, property)



def test_company::company_is_not_abstract():
    assert not inspect.isabstract(company::Company)


def test_company::company_constructor_exists():
    assert callable(company::Company.__init__)


def test_company::company_constructor_args():
    sig = inspect.signature(company::Company.__init__)
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
company::NamedElement_strategy = st.builds(
    company::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
company::Person_strategy = st.builds(
    company::Person,
    firstName=
        safe_text,
    fullName=
        safe_text,
    age=
        st.integers()
)
company::Department_strategy = st.builds(
    company::Department,
    ageSumOfEmployees=
        st.integers(),
    numberOfEmployees=
        st.integers()
)
company::Company_strategy = st.builds(
    company::Company,
)

@given(instance=company::NamedElement_strategy)
@settings(max_examples=50)
def test_company::namedelement_instantiation(instance):
    assert isinstance(instance, company::NamedElement)

@given(instance=company::NamedElement_strategy)
def test_company::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=company::NamedElement_strategy)
def test_company::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=company::Person_strategy)
@settings(max_examples=50)
def test_company::person_instantiation(instance):
    assert isinstance(instance, company::Person)

@given(instance=company::Person_strategy)
def test_company::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=company::Person_strategy)
def test_company::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=company::Person_strategy)
def test_company::person_fullName_type(instance):
    assert isinstance(instance.fullName, str)


@given(instance=company::Person_strategy)
def test_company::person_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=company::Person_strategy)
def test_company::person_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=company::Person_strategy)
def test_company::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=company::Department_strategy)
@settings(max_examples=50)
def test_company::department_instantiation(instance):
    assert isinstance(instance, company::Department)

@given(instance=company::Department_strategy)
def test_company::department_ageSumOfEmployees_type(instance):
    assert isinstance(instance.ageSumOfEmployees, int)


@given(instance=company::Department_strategy)
def test_company::department_ageSumOfEmployees_setter(instance):
    original = instance.ageSumOfEmployees
    instance.ageSumOfEmployees = original
    assert instance.ageSumOfEmployees == original

@given(instance=company::Department_strategy)
def test_company::department_numberOfEmployees_type(instance):
    assert isinstance(instance.numberOfEmployees, int)


@given(instance=company::Department_strategy)
def test_company::department_numberOfEmployees_setter(instance):
    original = instance.numberOfEmployees
    instance.numberOfEmployees = original
    assert instance.numberOfEmployees == original

@given(instance=company::Company_strategy)
@settings(max_examples=50)
def test_company::company_instantiation(instance):
    assert isinstance(instance, company::Company)
