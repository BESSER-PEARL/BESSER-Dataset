import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    employee::Employee,
    employee::Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_employee::employee_is_not_abstract():
    assert not inspect.isabstract(employee::Employee)


def test_employee::employee_constructor_exists():
    assert callable(employee::Employee.__init__)


def test_employee::employee_constructor_args():
    sig = inspect.signature(employee::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "hireDate" in params, "Missing parameter 'hireDate'"
    assert "age" in params, "Missing parameter 'age'"
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"

def test_employee::employee_has_hireDate():
    assert hasattr(employee::Employee, "hireDate")
    descriptor = None
    for klass in employee::Employee.__mro__:
        if "hireDate" in klass.__dict__:
            descriptor = klass.__dict__["hireDate"]
            break
    assert isinstance(descriptor, property)

def test_employee::employee_has_age():
    assert hasattr(employee::Employee, "age")
    descriptor = None
    for klass in employee::Employee.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_employee::employee_has_salary():
    assert hasattr(employee::Employee, "salary")
    descriptor = None
    for klass in employee::Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_employee::employee_has_name():
    assert hasattr(employee::Employee, "name")
    descriptor = None
    for klass in employee::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_employee::department_is_not_abstract():
    assert not inspect.isabstract(employee::Department)


def test_employee::department_constructor_exists():
    assert callable(employee::Department.__init__)


def test_employee::department_constructor_args():
    sig = inspect.signature(employee::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_employee::department_has_name():
    assert hasattr(employee::Department, "name")
    descriptor = None
    for klass in employee::Department.__mro__:
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
employee::Employee_strategy = st.builds(
    employee::Employee,
    hireDate=
        safe_text,
    age=
        safe_text,
    salary=
        safe_text,
    name=
        safe_text
)
employee::Department_strategy = st.builds(
    employee::Department,
    name=
        safe_text
)

@given(instance=employee::Employee_strategy)
@settings(max_examples=50)
def test_employee::employee_instantiation(instance):
    assert isinstance(instance, employee::Employee)

@given(instance=employee::Employee_strategy)
def test_employee::employee_hireDate_type(instance):
    assert isinstance(instance.hireDate, str)


@given(instance=employee::Employee_strategy)
def test_employee::employee_hireDate_setter(instance):
    original = instance.hireDate
    instance.hireDate = original
    assert instance.hireDate == original

@given(instance=employee::Employee_strategy)
def test_employee::employee_age_type(instance):
    assert isinstance(instance.age, str)


@given(instance=employee::Employee_strategy)
def test_employee::employee_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=employee::Employee_strategy)
def test_employee::employee_salary_type(instance):
    assert isinstance(instance.salary, str)


@given(instance=employee::Employee_strategy)
def test_employee::employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=employee::Employee_strategy)
def test_employee::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=employee::Employee_strategy)
def test_employee::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=employee::Department_strategy)
@settings(max_examples=50)
def test_employee::department_instantiation(instance):
    assert isinstance(instance, employee::Department)

@given(instance=employee::Department_strategy)
def test_employee::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=employee::Department_strategy)
def test_employee::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
