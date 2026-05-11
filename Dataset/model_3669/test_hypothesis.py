import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Company::Employee,
    Company::Project,
    Company::Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_company::employee_is_not_abstract():
    assert not inspect.isabstract(Company::Employee)


def test_company::employee_constructor_exists():
    assert callable(Company::Employee.__init__)


def test_company::employee_constructor_args():
    sig = inspect.signature(Company::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "salary" in params, "Missing parameter 'salary'"

def test_company::employee_has_name():
    assert hasattr(Company::Employee, "name")
    descriptor = None
    for klass in Company::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company::employee_has_salary():
    assert hasattr(Company::Employee, "salary")
    descriptor = None
    for klass in Company::Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)



def test_company::project_is_not_abstract():
    assert not inspect.isabstract(Company::Project)


def test_company::project_constructor_exists():
    assert callable(Company::Project.__init__)


def test_company::project_constructor_args():
    sig = inspect.signature(Company::Project.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"
    assert "name" in params, "Missing parameter 'name'"

def test_company::project_has_budget():
    assert hasattr(Company::Project, "budget")
    descriptor = None
    for klass in Company::Project.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)

def test_company::project_has_name():
    assert hasattr(Company::Project, "name")
    descriptor = None
    for klass in Company::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_company::department_is_not_abstract():
    assert not inspect.isabstract(Company::Department)


def test_company::department_constructor_exists():
    assert callable(Company::Department.__init__)


def test_company::department_constructor_args():
    sig = inspect.signature(Company::Department.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"
    assert "name" in params, "Missing parameter 'name'"
    assert "location" in params, "Missing parameter 'location'"

def test_company::department_has_budget():
    assert hasattr(Company::Department, "budget")
    descriptor = None
    for klass in Company::Department.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)

def test_company::department_has_name():
    assert hasattr(Company::Department, "name")
    descriptor = None
    for klass in Company::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company::department_has_location():
    assert hasattr(Company::Department, "location")
    descriptor = None
    for klass in Company::Department.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)


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
Company::Employee_strategy = st.builds(
    Company::Employee,
    name=
        safe_text,
    salary=
        st.integers()
)
Company::Project_strategy = st.builds(
    Company::Project,
    budget=
        st.integers(),
    name=
        safe_text
)
Company::Department_strategy = st.builds(
    Company::Department,
    budget=
        st.integers(),
    name=
        safe_text,
    location=
        safe_text
)

@given(instance=Company::Employee_strategy)
@settings(max_examples=50)
def test_company::employee_instantiation(instance):
    assert isinstance(instance, Company::Employee)

@given(instance=Company::Employee_strategy)
def test_company::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Company::Employee_strategy)
def test_company::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Company::Employee_strategy)
def test_company::employee_salary_type(instance):
    assert isinstance(instance.salary, int)


@given(instance=Company::Employee_strategy)
def test_company::employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=Company::Project_strategy)
@settings(max_examples=50)
def test_company::project_instantiation(instance):
    assert isinstance(instance, Company::Project)

@given(instance=Company::Project_strategy)
def test_company::project_budget_type(instance):
    assert isinstance(instance.budget, int)


@given(instance=Company::Project_strategy)
def test_company::project_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=Company::Project_strategy)
def test_company::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Company::Project_strategy)
def test_company::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Company::Department_strategy)
@settings(max_examples=50)
def test_company::department_instantiation(instance):
    assert isinstance(instance, Company::Department)

@given(instance=Company::Department_strategy)
def test_company::department_budget_type(instance):
    assert isinstance(instance.budget, int)


@given(instance=Company::Department_strategy)
def test_company::department_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=Company::Department_strategy)
def test_company::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Company::Department_strategy)
def test_company::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Company::Department_strategy)
def test_company::department_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=Company::Department_strategy)
def test_company::department_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original
