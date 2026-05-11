import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    employeeDsl::Employee,
    employeeDsl::EmployeeContainer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_employeedsl::employee_is_not_abstract():
    assert not inspect.isabstract(employeeDsl::Employee)


def test_employeedsl::employee_constructor_exists():
    assert callable(employeeDsl::Employee.__init__)


def test_employeedsl::employee_constructor_args():
    sig = inspect.signature(employeeDsl::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_employeedsl::employee_has_salary():
    assert hasattr(employeeDsl::Employee, "salary")
    descriptor = None
    for klass in employeeDsl::Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_employeedsl::employee_has_name():
    assert hasattr(employeeDsl::Employee, "name")
    descriptor = None
    for klass in employeeDsl::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_employeedsl::employee_has_ID():
    assert hasattr(employeeDsl::Employee, "ID")
    descriptor = None
    for klass in employeeDsl::Employee.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_employeedsl::employeecontainer_is_not_abstract():
    assert not inspect.isabstract(employeeDsl::EmployeeContainer)


def test_employeedsl::employeecontainer_constructor_exists():
    assert callable(employeeDsl::EmployeeContainer.__init__)


def test_employeedsl::employeecontainer_constructor_args():
    sig = inspect.signature(employeeDsl::EmployeeContainer.__init__)
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
employeeDsl::Employee_strategy = st.builds(
    employeeDsl::Employee,
    salary=
        st.integers(),
    name=
        safe_text,
    ID=
        st.integers()
)
employeeDsl::EmployeeContainer_strategy = st.builds(
    employeeDsl::EmployeeContainer,
)

@given(instance=employeeDsl::Employee_strategy)
@settings(max_examples=50)
def test_employeedsl::employee_instantiation(instance):
    assert isinstance(instance, employeeDsl::Employee)

@given(instance=employeeDsl::Employee_strategy)
def test_employeedsl::employee_salary_type(instance):
    assert isinstance(instance.salary, int)


@given(instance=employeeDsl::Employee_strategy)
def test_employeedsl::employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=employeeDsl::Employee_strategy)
def test_employeedsl::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=employeeDsl::Employee_strategy)
def test_employeedsl::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=employeeDsl::Employee_strategy)
def test_employeedsl::employee_ID_type(instance):
    assert isinstance(instance.ID, int)


@given(instance=employeeDsl::Employee_strategy)
def test_employeedsl::employee_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=employeeDsl::EmployeeContainer_strategy)
@settings(max_examples=50)
def test_employeedsl::employeecontainer_instantiation(instance):
    assert isinstance(instance, employeeDsl::EmployeeContainer)
