import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Demo::Project,
    Demo::Department,
    Demo::Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_demo::project_is_not_abstract():
    assert not inspect.isabstract(Demo::Project)


def test_demo::project_constructor_exists():
    assert callable(Demo::Project.__init__)


def test_demo::project_constructor_args():
    sig = inspect.signature(Demo::Project.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"
    assert "name" in params, "Missing parameter 'name'"

def test_demo::project_has_budget():
    assert hasattr(Demo::Project, "budget")
    descriptor = None
    for klass in Demo::Project.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)

def test_demo::project_has_name():
    assert hasattr(Demo::Project, "name")
    descriptor = None
    for klass in Demo::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_demo::department_is_not_abstract():
    assert not inspect.isabstract(Demo::Department)


def test_demo::department_constructor_exists():
    assert callable(Demo::Department.__init__)


def test_demo::department_constructor_args():
    sig = inspect.signature(Demo::Department.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "name" in params, "Missing parameter 'name'"
    assert "budget" in params, "Missing parameter 'budget'"

def test_demo::department_has_location():
    assert hasattr(Demo::Department, "location")
    descriptor = None
    for klass in Demo::Department.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_demo::department_has_name():
    assert hasattr(Demo::Department, "name")
    descriptor = None
    for klass in Demo::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_demo::department_has_budget():
    assert hasattr(Demo::Department, "budget")
    descriptor = None
    for klass in Demo::Department.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)



def test_demo::employee_is_not_abstract():
    assert not inspect.isabstract(Demo::Employee)


def test_demo::employee_constructor_exists():
    assert callable(Demo::Employee.__init__)


def test_demo::employee_constructor_args():
    sig = inspect.signature(Demo::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "salary" in params, "Missing parameter 'salary'"

def test_demo::employee_has_name():
    assert hasattr(Demo::Employee, "name")
    descriptor = None
    for klass in Demo::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_demo::employee_has_salary():
    assert hasattr(Demo::Employee, "salary")
    descriptor = None
    for klass in Demo::Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
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
Demo::Project_strategy = st.builds(
    Demo::Project,
    budget=
        st.integers(),
    name=
        st.booleans()
)
Demo::Department_strategy = st.builds(
    Demo::Department,
    location=
        st.booleans(),
    name=
        st.booleans(),
    budget=
        st.integers()
)
Demo::Employee_strategy = st.builds(
    Demo::Employee,
    name=
        st.booleans(),
    salary=
        st.integers()
)

@given(instance=Demo::Project_strategy)
@settings(max_examples=50)
def test_demo::project_instantiation(instance):
    assert isinstance(instance, Demo::Project)

@given(instance=Demo::Project_strategy)
def test_demo::project_budget_type(instance):
    assert isinstance(instance.budget, int)


@given(instance=Demo::Project_strategy)
def test_demo::project_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=Demo::Project_strategy)
def test_demo::project_name_type(instance):
    assert isinstance(instance.name, bool)


@given(instance=Demo::Project_strategy)
def test_demo::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Demo::Department_strategy)
@settings(max_examples=50)
def test_demo::department_instantiation(instance):
    assert isinstance(instance, Demo::Department)

@given(instance=Demo::Department_strategy)
def test_demo::department_location_type(instance):
    assert isinstance(instance.location, bool)


@given(instance=Demo::Department_strategy)
def test_demo::department_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Demo::Department_strategy)
def test_demo::department_name_type(instance):
    assert isinstance(instance.name, bool)


@given(instance=Demo::Department_strategy)
def test_demo::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Demo::Department_strategy)
def test_demo::department_budget_type(instance):
    assert isinstance(instance.budget, int)


@given(instance=Demo::Department_strategy)
def test_demo::department_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=Demo::Employee_strategy)
@settings(max_examples=50)
def test_demo::employee_instantiation(instance):
    assert isinstance(instance, Demo::Employee)

@given(instance=Demo::Employee_strategy)
def test_demo::employee_name_type(instance):
    assert isinstance(instance.name, bool)


@given(instance=Demo::Employee_strategy)
def test_demo::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Demo::Employee_strategy)
def test_demo::employee_salary_type(instance):
    assert isinstance(instance.salary, int)


@given(instance=Demo::Employee_strategy)
def test_demo::employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original
