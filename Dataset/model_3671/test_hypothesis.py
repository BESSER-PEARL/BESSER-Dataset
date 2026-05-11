import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Project::Project,
    Project::Department,
    Project::Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_project::project_is_not_abstract():
    assert not inspect.isabstract(Project::Project)


def test_project::project_constructor_exists():
    assert callable(Project::Project.__init__)


def test_project::project_constructor_args():
    sig = inspect.signature(Project::Project.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"
    assert "name" in params, "Missing parameter 'name'"

def test_project::project_has_budget():
    assert hasattr(Project::Project, "budget")
    descriptor = None
    for klass in Project::Project.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)

def test_project::project_has_name():
    assert hasattr(Project::Project, "name")
    descriptor = None
    for klass in Project::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_project::department_is_not_abstract():
    assert not inspect.isabstract(Project::Department)


def test_project::department_constructor_exists():
    assert callable(Project::Department.__init__)


def test_project::department_constructor_args():
    sig = inspect.signature(Project::Department.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"
    assert "name" in params, "Missing parameter 'name'"
    assert "location" in params, "Missing parameter 'location'"

def test_project::department_has_budget():
    assert hasattr(Project::Department, "budget")
    descriptor = None
    for klass in Project::Department.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)

def test_project::department_has_name():
    assert hasattr(Project::Department, "name")
    descriptor = None
    for klass in Project::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_project::department_has_location():
    assert hasattr(Project::Department, "location")
    descriptor = None
    for klass in Project::Department.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_project::employee_is_not_abstract():
    assert not inspect.isabstract(Project::Employee)


def test_project::employee_constructor_exists():
    assert callable(Project::Employee.__init__)


def test_project::employee_constructor_args():
    sig = inspect.signature(Project::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"

def test_project::employee_has_salary():
    assert hasattr(Project::Employee, "salary")
    descriptor = None
    for klass in Project::Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_project::employee_has_name():
    assert hasattr(Project::Employee, "name")
    descriptor = None
    for klass in Project::Employee.__mro__:
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
Project::Project_strategy = st.builds(
    Project::Project,
    budget=
        st.integers(),
    name=
        safe_text
)
Project::Department_strategy = st.builds(
    Project::Department,
    budget=
        st.integers(),
    name=
        safe_text,
    location=
        safe_text
)
Project::Employee_strategy = st.builds(
    Project::Employee,
    salary=
        st.integers(),
    name=
        safe_text
)

@given(instance=Project::Project_strategy)
@settings(max_examples=50)
def test_project::project_instantiation(instance):
    assert isinstance(instance, Project::Project)

@given(instance=Project::Project_strategy)
def test_project::project_budget_type(instance):
    assert isinstance(instance.budget, int)


@given(instance=Project::Project_strategy)
def test_project::project_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=Project::Project_strategy)
def test_project::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Project::Project_strategy)
def test_project::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Project::Department_strategy)
@settings(max_examples=50)
def test_project::department_instantiation(instance):
    assert isinstance(instance, Project::Department)

@given(instance=Project::Department_strategy)
def test_project::department_budget_type(instance):
    assert isinstance(instance.budget, int)


@given(instance=Project::Department_strategy)
def test_project::department_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=Project::Department_strategy)
def test_project::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Project::Department_strategy)
def test_project::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Project::Department_strategy)
def test_project::department_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=Project::Department_strategy)
def test_project::department_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Project::Employee_strategy)
@settings(max_examples=50)
def test_project::employee_instantiation(instance):
    assert isinstance(instance, Project::Employee)

@given(instance=Project::Employee_strategy)
def test_project::employee_salary_type(instance):
    assert isinstance(instance.salary, int)


@given(instance=Project::Employee_strategy)
def test_project::employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=Project::Employee_strategy)
def test_project::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Project::Employee_strategy)
def test_project::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
