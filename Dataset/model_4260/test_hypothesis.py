import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    bz321765_EmployeePK,
    bz321765_Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bz321765_employeepk_is_not_abstract():
    assert not inspect.isabstract(bz321765_EmployeePK)


def test_bz321765_employeepk_constructor_exists():
    assert callable(bz321765_EmployeePK.__init__)


def test_bz321765_employeepk_constructor_args():
    sig = inspect.signature(bz321765_EmployeePK.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "id" in params, "Missing parameter 'id'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_bz321765_employeepk_has_lastName():
    assert hasattr(bz321765_EmployeePK, "lastName")
    descriptor = None
    for klass in bz321765_EmployeePK.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_bz321765_employeepk_has_id():
    assert hasattr(bz321765_EmployeePK, "id")
    descriptor = None
    for klass in bz321765_EmployeePK.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_bz321765_employeepk_has_firstName():
    assert hasattr(bz321765_EmployeePK, "firstName")
    descriptor = None
    for klass in bz321765_EmployeePK.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_bz321765_employee_is_not_abstract():
    assert not inspect.isabstract(bz321765_Employee)


def test_bz321765_employee_constructor_exists():
    assert callable(bz321765_Employee.__init__)


def test_bz321765_employee_constructor_args():
    sig = inspect.signature(bz321765_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "salary" in params, "Missing parameter 'salary'"

def test_bz321765_employee_has_title():
    assert hasattr(bz321765_Employee, "title")
    descriptor = None
    for klass in bz321765_Employee.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bz321765_employee_has_salary():
    assert hasattr(bz321765_Employee, "salary")
    descriptor = None
    for klass in bz321765_Employee.__mro__:
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
bz321765_EmployeePK_strategy = st.builds(
    bz321765_EmployeePK,
    lastName=
        safe_text,
    id=
        safe_text,
    firstName=
        safe_text
)
bz321765_Employee_strategy = st.builds(
    bz321765_Employee,
    title=
        safe_text,
    salary=
        safe_text
)

@given(instance=bz321765_EmployeePK_strategy)
@settings(max_examples=50)
def test_bz321765_employeepk_instantiation(instance):
    assert isinstance(instance, bz321765_EmployeePK)



@given(instance=bz321765_EmployeePK_strategy)
def test_bz321765_employeepk_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=bz321765_EmployeePK_strategy)
def test_bz321765_employeepk_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=bz321765_EmployeePK_strategy)
def test_bz321765_employeepk_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=bz321765_Employee_strategy)
@settings(max_examples=50)
def test_bz321765_employee_instantiation(instance):
    assert isinstance(instance, bz321765_Employee)



@given(instance=bz321765_Employee_strategy)
def test_bz321765_employee_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=bz321765_Employee_strategy)
def test_bz321765_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original
