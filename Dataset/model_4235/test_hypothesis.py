import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    employee_Employee,
    employee_Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_employee_employee_is_not_abstract():
    assert not inspect.isabstract(employee_Employee)


def test_employee_employee_constructor_exists():
    assert callable(employee_Employee.__init__)


def test_employee_employee_constructor_args():
    sig = inspect.signature(employee_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"
    assert "hireDate" in params, "Missing parameter 'hireDate'"

def test_employee_employee_has_age():
    assert hasattr(employee_Employee, "age")
    descriptor = None
    for klass in employee_Employee.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_employee_employee_has_salary():
    assert hasattr(employee_Employee, "salary")
    descriptor = None
    for klass in employee_Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_employee_employee_has_name():
    assert hasattr(employee_Employee, "name")
    descriptor = None
    for klass in employee_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_employee_employee_has_hireDate():
    assert hasattr(employee_Employee, "hireDate")
    descriptor = None
    for klass in employee_Employee.__mro__:
        if "hireDate" in klass.__dict__:
            descriptor = klass.__dict__["hireDate"]
            break
    assert isinstance(descriptor, property)



def test_employee_department_is_not_abstract():
    assert not inspect.isabstract(employee_Department)


def test_employee_department_constructor_exists():
    assert callable(employee_Department.__init__)


def test_employee_department_constructor_args():
    sig = inspect.signature(employee_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_employee_department_has_name():
    assert hasattr(employee_Department, "name")
    descriptor = None
    for klass in employee_Department.__mro__:
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
employee_Employee_strategy = st.builds(
    employee_Employee,
    age=
        safe_text,
    salary=
        safe_text,
    name=
        safe_text,
    hireDate=
        safe_text
)
employee_Department_strategy = st.builds(
    employee_Department,
    name=
        safe_text
)

@given(instance=employee_Employee_strategy)
@settings(max_examples=50)
def test_employee_employee_instantiation(instance):
    assert isinstance(instance, employee_Employee)



@given(instance=employee_Employee_strategy)
def test_employee_employee_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=employee_Employee_strategy)
def test_employee_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original



@given(instance=employee_Employee_strategy)
def test_employee_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=employee_Employee_strategy)
def test_employee_employee_hireDate_setter(instance):
    original = instance.hireDate
    instance.hireDate = original
    assert instance.hireDate == original

@given(instance=employee_Department_strategy)
@settings(max_examples=50)
def test_employee_department_instantiation(instance):
    assert isinstance(instance, employee_Department)



@given(instance=employee_Department_strategy)
def test_employee_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
