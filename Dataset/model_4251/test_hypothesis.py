import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Employees::Employee,
    Employees::EmployeeContainer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_employees::employee_is_not_abstract():
    assert not inspect.isabstract(Employees::Employee)


def test_employees::employee_constructor_exists():
    assert callable(Employees::Employee.__init__)


def test_employees::employee_constructor_args():
    sig = inspect.signature(Employees::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "salary" in params, "Missing parameter 'salary'"

def test_employees::employee_has_name():
    assert hasattr(Employees::Employee, "name")
    descriptor = None
    for klass in Employees::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_employees::employee_has_ID():
    assert hasattr(Employees::Employee, "ID")
    descriptor = None
    for klass in Employees::Employee.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_employees::employee_has_salary():
    assert hasattr(Employees::Employee, "salary")
    descriptor = None
    for klass in Employees::Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)



def test_employees::employeecontainer_is_not_abstract():
    assert not inspect.isabstract(Employees::EmployeeContainer)


def test_employees::employeecontainer_constructor_exists():
    assert callable(Employees::EmployeeContainer.__init__)


def test_employees::employeecontainer_constructor_args():
    sig = inspect.signature(Employees::EmployeeContainer.__init__)
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
Employees::Employee_strategy = st.builds(
    Employees::Employee,
    name=
        safe_text,
    ID=
        st.integers(),
    salary=
        st.integers()
)
Employees::EmployeeContainer_strategy = st.builds(
    Employees::EmployeeContainer,
)

@given(instance=Employees::Employee_strategy)
@settings(max_examples=50)
def test_employees::employee_instantiation(instance):
    assert isinstance(instance, Employees::Employee)

@given(instance=Employees::Employee_strategy)
def test_employees::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Employees::Employee_strategy)
def test_employees::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Employees::Employee_strategy)
def test_employees::employee_ID_type(instance):
    assert isinstance(instance.ID, int)


@given(instance=Employees::Employee_strategy)
def test_employees::employee_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Employees::Employee_strategy)
def test_employees::employee_salary_type(instance):
    assert isinstance(instance.salary, int)


@given(instance=Employees::Employee_strategy)
def test_employees::employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=Employees::EmployeeContainer_strategy)
@settings(max_examples=50)
def test_employees::employeecontainer_instantiation(instance):
    assert isinstance(instance, Employees::EmployeeContainer)
