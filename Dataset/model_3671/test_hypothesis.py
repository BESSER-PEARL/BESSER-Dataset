import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Project_Project,
    Project_Department,
    Project_Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_project_project_is_not_abstract():
    assert not inspect.isabstract(Project_Project)


def test_project_project_constructor_exists():
    assert callable(Project_Project.__init__)


def test_project_project_constructor_args():
    sig = inspect.signature(Project_Project.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"
    assert "name" in params, "Missing parameter 'name'"

def test_project_project_has_budget():
    assert hasattr(Project_Project, "budget")
    descriptor = None
    for klass in Project_Project.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)

def test_project_project_has_name():
    assert hasattr(Project_Project, "name")
    descriptor = None
    for klass in Project_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_project_department_is_not_abstract():
    assert not inspect.isabstract(Project_Department)


def test_project_department_constructor_exists():
    assert callable(Project_Department.__init__)


def test_project_department_constructor_args():
    sig = inspect.signature(Project_Department.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"
    assert "name" in params, "Missing parameter 'name'"
    assert "location" in params, "Missing parameter 'location'"

def test_project_department_has_budget():
    assert hasattr(Project_Department, "budget")
    descriptor = None
    for klass in Project_Department.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)

def test_project_department_has_name():
    assert hasattr(Project_Department, "name")
    descriptor = None
    for klass in Project_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_project_department_has_location():
    assert hasattr(Project_Department, "location")
    descriptor = None
    for klass in Project_Department.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_project_employee_is_not_abstract():
    assert not inspect.isabstract(Project_Employee)


def test_project_employee_constructor_exists():
    assert callable(Project_Employee.__init__)


def test_project_employee_constructor_args():
    sig = inspect.signature(Project_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"

def test_project_employee_has_salary():
    assert hasattr(Project_Employee, "salary")
    descriptor = None
    for klass in Project_Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_project_employee_has_name():
    assert hasattr(Project_Employee, "name")
    descriptor = None
    for klass in Project_Employee.__mro__:
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
Project_Project_strategy = st.builds(
    Project_Project,
    budget=
        st.integers(),
    name=
        safe_text
)
Project_Department_strategy = st.builds(
    Project_Department,
    budget=
        st.integers(),
    name=
        safe_text,
    location=
        safe_text
)
Project_Employee_strategy = st.builds(
    Project_Employee,
    salary=
        st.integers(),
    name=
        safe_text
)

@given(instance=Project_Project_strategy)
@settings(max_examples=50)
def test_project_project_instantiation(instance):
    assert isinstance(instance, Project_Project)



@given(instance=Project_Project_strategy)
def test_project_project_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original



@given(instance=Project_Project_strategy)
def test_project_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Project_Department_strategy)
@settings(max_examples=50)
def test_project_department_instantiation(instance):
    assert isinstance(instance, Project_Department)



@given(instance=Project_Department_strategy)
def test_project_department_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original



@given(instance=Project_Department_strategy)
def test_project_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Project_Department_strategy)
def test_project_department_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Project_Employee_strategy)
@settings(max_examples=50)
def test_project_employee_instantiation(instance):
    assert isinstance(instance, Project_Employee)



@given(instance=Project_Employee_strategy)
def test_project_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original



@given(instance=Project_Employee_strategy)
def test_project_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
