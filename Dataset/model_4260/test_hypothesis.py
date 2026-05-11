import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    bz321765::EmployeePK,
    bz321765::Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bz321765::employeepk_is_not_abstract():
    assert not inspect.isabstract(bz321765::EmployeePK)


def test_bz321765::employeepk_constructor_exists():
    assert callable(bz321765::EmployeePK.__init__)


def test_bz321765::employeepk_constructor_args():
    sig = inspect.signature(bz321765::EmployeePK.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "id" in params, "Missing parameter 'id'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_bz321765::employeepk_has_lastName():
    assert hasattr(bz321765::EmployeePK, "lastName")
    descriptor = None
    for klass in bz321765::EmployeePK.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_bz321765::employeepk_has_id():
    assert hasattr(bz321765::EmployeePK, "id")
    descriptor = None
    for klass in bz321765::EmployeePK.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_bz321765::employeepk_has_firstName():
    assert hasattr(bz321765::EmployeePK, "firstName")
    descriptor = None
    for klass in bz321765::EmployeePK.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_bz321765::employee_is_not_abstract():
    assert not inspect.isabstract(bz321765::Employee)


def test_bz321765::employee_constructor_exists():
    assert callable(bz321765::Employee.__init__)


def test_bz321765::employee_constructor_args():
    sig = inspect.signature(bz321765::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "salary" in params, "Missing parameter 'salary'"

def test_bz321765::employee_has_title():
    assert hasattr(bz321765::Employee, "title")
    descriptor = None
    for klass in bz321765::Employee.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bz321765::employee_has_salary():
    assert hasattr(bz321765::Employee, "salary")
    descriptor = None
    for klass in bz321765::Employee.__mro__:
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
bz321765::EmployeePK_strategy = st.builds(
    bz321765::EmployeePK,
    lastName=
        safe_text,
    id=
        safe_text,
    firstName=
        safe_text
)
bz321765::Employee_strategy = st.builds(
    bz321765::Employee,
    title=
        safe_text,
    salary=
        safe_text
)

@given(instance=bz321765::EmployeePK_strategy)
@settings(max_examples=50)
def test_bz321765::employeepk_instantiation(instance):
    assert isinstance(instance, bz321765::EmployeePK)

@given(instance=bz321765::EmployeePK_strategy)
def test_bz321765::employeepk_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=bz321765::EmployeePK_strategy)
def test_bz321765::employeepk_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=bz321765::EmployeePK_strategy)
def test_bz321765::employeepk_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=bz321765::EmployeePK_strategy)
def test_bz321765::employeepk_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=bz321765::EmployeePK_strategy)
def test_bz321765::employeepk_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=bz321765::EmployeePK_strategy)
def test_bz321765::employeepk_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=bz321765::Employee_strategy)
@settings(max_examples=50)
def test_bz321765::employee_instantiation(instance):
    assert isinstance(instance, bz321765::Employee)

@given(instance=bz321765::Employee_strategy)
def test_bz321765::employee_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bz321765::Employee_strategy)
def test_bz321765::employee_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bz321765::Employee_strategy)
def test_bz321765::employee_salary_type(instance):
    assert isinstance(instance.salary, str)


@given(instance=bz321765::Employee_strategy)
def test_bz321765::employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original
