import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Demo_Project,
    Demo_Department,
    Demo_Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_demo_project_is_not_abstract():
    assert not inspect.isabstract(Demo_Project)


def test_demo_project_constructor_exists():
    assert callable(Demo_Project.__init__)


def test_demo_project_constructor_args():
    sig = inspect.signature(Demo_Project.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"
    assert "name" in params, "Missing parameter 'name'"

def test_demo_project_has_budget():
    assert hasattr(Demo_Project, "budget")
    descriptor = None
    for klass in Demo_Project.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)

def test_demo_project_has_name():
    assert hasattr(Demo_Project, "name")
    descriptor = None
    for klass in Demo_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_demo_department_is_not_abstract():
    assert not inspect.isabstract(Demo_Department)


def test_demo_department_constructor_exists():
    assert callable(Demo_Department.__init__)


def test_demo_department_constructor_args():
    sig = inspect.signature(Demo_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "location" in params, "Missing parameter 'location'"
    assert "budget" in params, "Missing parameter 'budget'"

def test_demo_department_has_name():
    assert hasattr(Demo_Department, "name")
    descriptor = None
    for klass in Demo_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_demo_department_has_location():
    assert hasattr(Demo_Department, "location")
    descriptor = None
    for klass in Demo_Department.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_demo_department_has_budget():
    assert hasattr(Demo_Department, "budget")
    descriptor = None
    for klass in Demo_Department.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)



def test_demo_employee_is_not_abstract():
    assert not inspect.isabstract(Demo_Employee)


def test_demo_employee_constructor_exists():
    assert callable(Demo_Employee.__init__)


def test_demo_employee_constructor_args():
    sig = inspect.signature(Demo_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"

def test_demo_employee_has_salary():
    assert hasattr(Demo_Employee, "salary")
    descriptor = None
    for klass in Demo_Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_demo_employee_has_name():
    assert hasattr(Demo_Employee, "name")
    descriptor = None
    for klass in Demo_Employee.__mro__:
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
Demo_Project_strategy = st.builds(
    Demo_Project,
    budget=
        st.integers(),
    name=
        st.booleans()
)
Demo_Department_strategy = st.builds(
    Demo_Department,
    name=
        st.booleans(),
    location=
        st.booleans(),
    budget=
        st.integers()
)
Demo_Employee_strategy = st.builds(
    Demo_Employee,
    salary=
        st.integers(),
    name=
        st.booleans()
)

@given(instance=Demo_Project_strategy)
@settings(max_examples=50)
def test_demo_project_instantiation(instance):
    assert isinstance(instance, Demo_Project)



@given(instance=Demo_Project_strategy)
def test_demo_project_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original



@given(instance=Demo_Project_strategy)
def test_demo_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Demo_Department_strategy)
@settings(max_examples=50)
def test_demo_department_instantiation(instance):
    assert isinstance(instance, Demo_Department)



@given(instance=Demo_Department_strategy)
def test_demo_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Demo_Department_strategy)
def test_demo_department_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Demo_Department_strategy)
def test_demo_department_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=Demo_Employee_strategy)
@settings(max_examples=50)
def test_demo_employee_instantiation(instance):
    assert isinstance(instance, Demo_Employee)



@given(instance=Demo_Employee_strategy)
def test_demo_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original



@given(instance=Demo_Employee_strategy)
def test_demo_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
