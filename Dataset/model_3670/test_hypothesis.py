import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Company_Project,
    Company_Department,
    Company_Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_company_project_is_not_abstract():
    assert not inspect.isabstract(Company_Project)


def test_company_project_constructor_exists():
    assert callable(Company_Project.__init__)


def test_company_project_constructor_args():
    sig = inspect.signature(Company_Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "budget" in params, "Missing parameter 'budget'"

def test_company_project_has_name():
    assert hasattr(Company_Project, "name")
    descriptor = None
    for klass in Company_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company_project_has_budget():
    assert hasattr(Company_Project, "budget")
    descriptor = None
    for klass in Company_Project.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)



def test_company_department_is_not_abstract():
    assert not inspect.isabstract(Company_Department)


def test_company_department_constructor_exists():
    assert callable(Company_Department.__init__)


def test_company_department_constructor_args():
    sig = inspect.signature(Company_Department.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"
    assert "name" in params, "Missing parameter 'name'"
    assert "location" in params, "Missing parameter 'location'"

def test_company_department_has_budget():
    assert hasattr(Company_Department, "budget")
    descriptor = None
    for klass in Company_Department.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)

def test_company_department_has_name():
    assert hasattr(Company_Department, "name")
    descriptor = None
    for klass in Company_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company_department_has_location():
    assert hasattr(Company_Department, "location")
    descriptor = None
    for klass in Company_Department.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_company_employee_is_not_abstract():
    assert not inspect.isabstract(Company_Employee)


def test_company_employee_constructor_exists():
    assert callable(Company_Employee.__init__)


def test_company_employee_constructor_args():
    sig = inspect.signature(Company_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"

def test_company_employee_has_salary():
    assert hasattr(Company_Employee, "salary")
    descriptor = None
    for klass in Company_Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_company_employee_has_name():
    assert hasattr(Company_Employee, "name")
    descriptor = None
    for klass in Company_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
Company_Project_strategy = st.builds(
    Company_Project,
    name=
        safe_text,
    budget=
        st.integers()
)
Company_Department_strategy = st.builds(
    Company_Department,
    budget=
        st.integers(),
    name=
        safe_text,
    location=
        safe_text
)
Company_Employee_strategy = st.builds(
    Company_Employee,
    salary=
        st.integers(),
    name=
        safe_text
)

@given(instance=Company_Project_strategy)
@settings(max_examples=50)
def test_company_project_instantiation(instance):
    assert isinstance(instance, Company_Project)



@given(instance=Company_Project_strategy)
def test_company_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Company_Project_strategy)
def test_company_project_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=Company_Department_strategy)
@settings(max_examples=50)
def test_company_department_instantiation(instance):
    assert isinstance(instance, Company_Department)



@given(instance=Company_Department_strategy)
def test_company_department_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original



@given(instance=Company_Department_strategy)
def test_company_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Company_Department_strategy)
def test_company_department_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Company_Employee_strategy)
@settings(max_examples=50)
def test_company_employee_instantiation(instance):
    assert isinstance(instance, Company_Employee)



@given(instance=Company_Employee_strategy)
def test_company_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original



@given(instance=Company_Employee_strategy)
def test_company_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
