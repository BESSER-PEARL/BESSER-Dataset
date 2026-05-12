import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    employeeDsl_Employee,
    employeeDsl_EmployeeContainer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_employeedsl_employee_is_not_abstract():
    assert not inspect.isabstract(employeeDsl_Employee)


def test_employeedsl_employee_constructor_exists():
    assert callable(employeeDsl_Employee.__init__)


def test_employeedsl_employee_constructor_args():
    sig = inspect.signature(employeeDsl_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "name" in params, "Missing parameter 'name'"

def test_employeedsl_employee_has_salary():
    assert hasattr(employeeDsl_Employee, "salary")
    descriptor = None
    for klass in employeeDsl_Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_employeedsl_employee_has_ID():
    assert hasattr(employeeDsl_Employee, "ID")
    descriptor = None
    for klass in employeeDsl_Employee.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_employeedsl_employee_has_name():
    assert hasattr(employeeDsl_Employee, "name")
    descriptor = None
    for klass in employeeDsl_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_employeedsl_employeecontainer_is_not_abstract():
    assert not inspect.isabstract(employeeDsl_EmployeeContainer)


def test_employeedsl_employeecontainer_constructor_exists():
    assert callable(employeeDsl_EmployeeContainer.__init__)


def test_employeedsl_employeecontainer_constructor_args():
    sig = inspect.signature(employeeDsl_EmployeeContainer.__init__)
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
employeeDsl_Employee_strategy = st.builds(
    employeeDsl_Employee,
    salary=
        st.integers(),
    ID=
        st.integers(),
    name=
        safe_text
)
employeeDsl_EmployeeContainer_strategy = st.builds(
    employeeDsl_EmployeeContainer,
)

@given(instance=employeeDsl_Employee_strategy)
@settings(max_examples=50)
def test_employeedsl_employee_instantiation(instance):
    assert isinstance(instance, employeeDsl_Employee)



@given(instance=employeeDsl_Employee_strategy)
def test_employeedsl_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original



@given(instance=employeeDsl_Employee_strategy)
def test_employeedsl_employee_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=employeeDsl_Employee_strategy)
def test_employeedsl_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=employeeDsl_EmployeeContainer_strategy)
@settings(max_examples=50)
def test_employeedsl_employeecontainer_instantiation(instance):
    assert isinstance(instance, employeeDsl_EmployeeContainer)
