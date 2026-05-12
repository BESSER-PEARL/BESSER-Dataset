import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    companies_Visitable,
    companies_CSTrace,
    CSTrace,
    companies_department,
    companies_company,
    companies_employee,
    companies_department_employees,
    companies_department_manager,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_companies_visitable_is_not_abstract():
    assert not inspect.isabstract(companies_Visitable)


def test_companies_visitable_constructor_exists():
    assert callable(companies_Visitable.__init__)


def test_companies_visitable_constructor_args():
    sig = inspect.signature(companies_Visitable.__init__)
    params = list(sig.parameters.keys())



def test_companies_cstrace_is_not_abstract():
    assert not inspect.isabstract(companies_CSTrace)


def test_companies_cstrace_constructor_exists():
    assert callable(companies_CSTrace.__init__)


def test_companies_cstrace_constructor_args():
    sig = inspect.signature(companies_CSTrace.__init__)
    params = list(sig.parameters.keys())



def test_cstrace_is_not_abstract():
    assert not inspect.isabstract(CSTrace)


def test_cstrace_constructor_exists():
    assert callable(CSTrace.__init__)


def test_cstrace_constructor_args():
    sig = inspect.signature(CSTrace.__init__)
    params = list(sig.parameters.keys())



def test_companies_department_is_not_abstract():
    assert not inspect.isabstract(companies_department)


def test_companies_department_constructor_exists():
    assert callable(companies_department.__init__)


def test_companies_department_constructor_args():
    sig = inspect.signature(companies_department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_companies_department_has_name():
    assert hasattr(companies_department, "name")
    descriptor = None
    for klass in companies_department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_companies_company_is_not_abstract():
    assert not inspect.isabstract(companies_company)


def test_companies_company_constructor_exists():
    assert callable(companies_company.__init__)


def test_companies_company_constructor_args():
    sig = inspect.signature(companies_company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_companies_company_has_name():
    assert hasattr(companies_company, "name")
    descriptor = None
    for klass in companies_company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_companies_employee_is_not_abstract():
    assert not inspect.isabstract(companies_employee)


def test_companies_employee_constructor_exists():
    assert callable(companies_employee.__init__)


def test_companies_employee_constructor_args():
    sig = inspect.signature(companies_employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "mentor" in params, "Missing parameter 'mentor'"
    assert "salary" in params, "Missing parameter 'salary'"
    assert "address" in params, "Missing parameter 'address'"

def test_companies_employee_has_name():
    assert hasattr(companies_employee, "name")
    descriptor = None
    for klass in companies_employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_companies_employee_has_mentor():
    assert hasattr(companies_employee, "mentor")
    descriptor = None
    for klass in companies_employee.__mro__:
        if "mentor" in klass.__dict__:
            descriptor = klass.__dict__["mentor"]
            break
    assert isinstance(descriptor, property)

def test_companies_employee_has_salary():
    assert hasattr(companies_employee, "salary")
    descriptor = None
    for klass in companies_employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_companies_employee_has_address():
    assert hasattr(companies_employee, "address")
    descriptor = None
    for klass in companies_employee.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_companies_department_employees_is_not_abstract():
    assert not inspect.isabstract(companies_department_employees)


def test_companies_department_employees_constructor_exists():
    assert callable(companies_department_employees.__init__)


def test_companies_department_employees_constructor_args():
    sig = inspect.signature(companies_department_employees.__init__)
    params = list(sig.parameters.keys())



def test_companies_department_manager_is_not_abstract():
    assert not inspect.isabstract(companies_department_manager)


def test_companies_department_manager_constructor_exists():
    assert callable(companies_department_manager.__init__)


def test_companies_department_manager_constructor_args():
    sig = inspect.signature(companies_department_manager.__init__)
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
companies_Visitable_strategy = st.builds(
    companies_Visitable,
)
companies_CSTrace_strategy = st.builds(
    companies_CSTrace,
)
CSTrace_strategy = st.builds(
    CSTrace,
)
companies_department_strategy = st.builds(
    companies_department,
    name=
        safe_text
)
companies_company_strategy = st.builds(
    companies_company,
    name=
        safe_text
)
companies_employee_strategy = st.builds(
    companies_employee,
    name=
        safe_text,
    mentor=
        safe_text,
    salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    address=
        safe_text
)
companies_department_employees_strategy = st.builds(
    companies_department_employees,
)
companies_department_manager_strategy = st.builds(
    companies_department_manager,
)

@given(instance=companies_Visitable_strategy)
@settings(max_examples=50)
def test_companies_visitable_instantiation(instance):
    assert isinstance(instance, companies_Visitable)

@given(instance=companies_CSTrace_strategy)
@settings(max_examples=50)
def test_companies_cstrace_instantiation(instance):
    assert isinstance(instance, companies_CSTrace)

@given(instance=CSTrace_strategy)
@settings(max_examples=50)
def test_cstrace_instantiation(instance):
    assert isinstance(instance, CSTrace)

@given(instance=companies_department_strategy)
@settings(max_examples=50)
def test_companies_department_instantiation(instance):
    assert isinstance(instance, companies_department)



@given(instance=companies_department_strategy)
def test_companies_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=companies_company_strategy)
@settings(max_examples=50)
def test_companies_company_instantiation(instance):
    assert isinstance(instance, companies_company)



@given(instance=companies_company_strategy)
def test_companies_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=companies_employee_strategy)
@settings(max_examples=50)
def test_companies_employee_instantiation(instance):
    assert isinstance(instance, companies_employee)



@given(instance=companies_employee_strategy)
def test_companies_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=companies_employee_strategy)
def test_companies_employee_mentor_setter(instance):
    original = instance.mentor
    instance.mentor = original
    assert instance.mentor == original



@given(instance=companies_employee_strategy)
def test_companies_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original



@given(instance=companies_employee_strategy)
def test_companies_employee_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=companies_department_employees_strategy)
@settings(max_examples=50)
def test_companies_department_employees_instantiation(instance):
    assert isinstance(instance, companies_department_employees)

@given(instance=companies_department_manager_strategy)
@settings(max_examples=50)
def test_companies_department_manager_instantiation(instance):
    assert isinstance(instance, companies_department_manager)
