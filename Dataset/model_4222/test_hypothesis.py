import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    _101companies_Company,
    _101companies_Employee,
    _101companies_Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test__101companies_company_is_not_abstract():
    assert not inspect.isabstract(_101companies_Company)


def test__101companies_company_constructor_exists():
    assert callable(_101companies_Company.__init__)


def test__101companies_company_constructor_args():
    sig = inspect.signature(_101companies_Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "totalSalary" in params, "Missing parameter 'totalSalary'"

def test__101companies_company_has_name():
    assert hasattr(_101companies_Company, "name")
    descriptor = None
    for klass in _101companies_Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test__101companies_company_has_totalSalary():
    assert hasattr(_101companies_Company, "totalSalary")
    descriptor = None
    for klass in _101companies_Company.__mro__:
        if "totalSalary" in klass.__dict__:
            descriptor = klass.__dict__["totalSalary"]
            break
    assert isinstance(descriptor, property)



def test__101companies_employee_is_not_abstract():
    assert not inspect.isabstract(_101companies_Employee)


def test__101companies_employee_constructor_exists():
    assert callable(_101companies_Employee.__init__)


def test__101companies_employee_constructor_args():
    sig = inspect.signature(_101companies_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"
    assert "salary" in params, "Missing parameter 'salary'"

def test__101companies_employee_has_name():
    assert hasattr(_101companies_Employee, "name")
    descriptor = None
    for klass in _101companies_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test__101companies_employee_has_address():
    assert hasattr(_101companies_Employee, "address")
    descriptor = None
    for klass in _101companies_Employee.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test__101companies_employee_has_salary():
    assert hasattr(_101companies_Employee, "salary")
    descriptor = None
    for klass in _101companies_Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)



def test__101companies_department_is_not_abstract():
    assert not inspect.isabstract(_101companies_Department)


def test__101companies_department_constructor_exists():
    assert callable(_101companies_Department.__init__)


def test__101companies_department_constructor_args():
    sig = inspect.signature(_101companies_Department.__init__)
    params = list(sig.parameters.keys())
    assert "totalSalary" in params, "Missing parameter 'totalSalary'"
    assert "name" in params, "Missing parameter 'name'"

def test__101companies_department_has_totalSalary():
    assert hasattr(_101companies_Department, "totalSalary")
    descriptor = None
    for klass in _101companies_Department.__mro__:
        if "totalSalary" in klass.__dict__:
            descriptor = klass.__dict__["totalSalary"]
            break
    assert isinstance(descriptor, property)

def test__101companies_department_has_name():
    assert hasattr(_101companies_Department, "name")
    descriptor = None
    for klass in _101companies_Department.__mro__:
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
_101companies_Company_strategy = st.builds(
    _101companies_Company,
    name=
        safe_text,
    totalSalary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
_101companies_Employee_strategy = st.builds(
    _101companies_Employee,
    name=
        safe_text,
    address=
        safe_text,
    salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
_101companies_Department_strategy = st.builds(
    _101companies_Department,
    totalSalary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)

@given(instance=_101companies_Company_strategy)
@settings(max_examples=50)
def test__101companies_company_instantiation(instance):
    assert isinstance(instance, _101companies_Company)



@given(instance=_101companies_Company_strategy)
def test__101companies_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=_101companies_Company_strategy)
def test__101companies_company_totalSalary_setter(instance):
    original = instance.totalSalary
    instance.totalSalary = original
    assert instance.totalSalary == original

@given(instance=_101companies_Employee_strategy)
@settings(max_examples=50)
def test__101companies_employee_instantiation(instance):
    assert isinstance(instance, _101companies_Employee)



@given(instance=_101companies_Employee_strategy)
def test__101companies_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=_101companies_Employee_strategy)
def test__101companies_employee_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=_101companies_Employee_strategy)
def test__101companies_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=_101companies_Department_strategy)
@settings(max_examples=50)
def test__101companies_department_instantiation(instance):
    assert isinstance(instance, _101companies_Department)



@given(instance=_101companies_Department_strategy)
def test__101companies_department_totalSalary_setter(instance):
    original = instance.totalSalary
    instance.totalSalary = original
    assert instance.totalSalary == original



@given(instance=_101companies_Department_strategy)
def test__101companies_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
