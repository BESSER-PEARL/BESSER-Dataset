import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    company_Employee,
    company_Department,
    company_Company,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_company_employee_is_not_abstract():
    assert not inspect.isabstract(company_Employee)


def test_company_employee_constructor_exists():
    assert callable(company_Employee.__init__)


def test_company_employee_constructor_args():
    sig = inspect.signature(company_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"
    assert "salary" in params, "Missing parameter 'salary'"

def test_company_employee_has_address():
    assert hasattr(company_Employee, "address")
    descriptor = None
    for klass in company_Employee.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_company_employee_has_name():
    assert hasattr(company_Employee, "name")
    descriptor = None
    for klass in company_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company_employee_has_salary():
    assert hasattr(company_Employee, "salary")
    descriptor = None
    for klass in company_Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)



def test_company_department_is_not_abstract():
    assert not inspect.isabstract(company_Department)


def test_company_department_constructor_exists():
    assert callable(company_Department.__init__)


def test_company_department_constructor_args():
    sig = inspect.signature(company_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company_department_has_name():
    assert hasattr(company_Department, "name")
    descriptor = None
    for klass in company_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_company_company_is_not_abstract():
    assert not inspect.isabstract(company_Company)


def test_company_company_constructor_exists():
    assert callable(company_Company.__init__)


def test_company_company_constructor_args():
    sig = inspect.signature(company_Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company_company_has_name():
    assert hasattr(company_Company, "name")
    descriptor = None
    for klass in company_Company.__mro__:
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
company_Employee_strategy = st.builds(
    company_Employee,
    address=
        safe_text,
    name=
        safe_text,
    salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
company_Department_strategy = st.builds(
    company_Department,
    name=
        safe_text
)
company_Company_strategy = st.builds(
    company_Company,
    name=
        safe_text
)

@given(instance=company_Employee_strategy)
@settings(max_examples=50)
def test_company_employee_instantiation(instance):
    assert isinstance(instance, company_Employee)



@given(instance=company_Employee_strategy)
def test_company_employee_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=company_Employee_strategy)
def test_company_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=company_Employee_strategy)
def test_company_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=company_Department_strategy)
@settings(max_examples=50)
def test_company_department_instantiation(instance):
    assert isinstance(instance, company_Department)



@given(instance=company_Department_strategy)
def test_company_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=company_Company_strategy)
@settings(max_examples=50)
def test_company_company_instantiation(instance):
    assert isinstance(instance, company_Company)



@given(instance=company_Company_strategy)
def test_company_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
