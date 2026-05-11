import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    companies::Visitable,
    companies::CSTrace,
    CSTrace,
    companies::department::manager,
    companies::department,
    companies::company,
    companies::employee,
    companies::department::employees,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_companies::visitable_is_not_abstract():
    assert not inspect.isabstract(companies::Visitable)


def test_companies::visitable_constructor_exists():
    assert callable(companies::Visitable.__init__)


def test_companies::visitable_constructor_args():
    sig = inspect.signature(companies::Visitable.__init__)
    params = list(sig.parameters.keys())



def test_companies::cstrace_is_not_abstract():
    assert not inspect.isabstract(companies::CSTrace)


def test_companies::cstrace_constructor_exists():
    assert callable(companies::CSTrace.__init__)


def test_companies::cstrace_constructor_args():
    sig = inspect.signature(companies::CSTrace.__init__)
    params = list(sig.parameters.keys())



def test_cstrace_is_not_abstract():
    assert not inspect.isabstract(CSTrace)


def test_cstrace_constructor_exists():
    assert callable(CSTrace.__init__)


def test_cstrace_constructor_args():
    sig = inspect.signature(CSTrace.__init__)
    params = list(sig.parameters.keys())



def test_companies::department::manager_is_not_abstract():
    assert not inspect.isabstract(companies::department::manager)


def test_companies::department::manager_constructor_exists():
    assert callable(companies::department::manager.__init__)


def test_companies::department::manager_constructor_args():
    sig = inspect.signature(companies::department::manager.__init__)
    params = list(sig.parameters.keys())



def test_companies::department_is_not_abstract():
    assert not inspect.isabstract(companies::department)


def test_companies::department_constructor_exists():
    assert callable(companies::department.__init__)


def test_companies::department_constructor_args():
    sig = inspect.signature(companies::department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_companies::department_has_name():
    assert hasattr(companies::department, "name")
    descriptor = None
    for klass in companies::department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_companies::company_is_not_abstract():
    assert not inspect.isabstract(companies::company)


def test_companies::company_constructor_exists():
    assert callable(companies::company.__init__)


def test_companies::company_constructor_args():
    sig = inspect.signature(companies::company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_companies::company_has_name():
    assert hasattr(companies::company, "name")
    descriptor = None
    for klass in companies::company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_companies::employee_is_not_abstract():
    assert not inspect.isabstract(companies::employee)


def test_companies::employee_constructor_exists():
    assert callable(companies::employee.__init__)


def test_companies::employee_constructor_args():
    sig = inspect.signature(companies::employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"
    assert "mentor" in params, "Missing parameter 'mentor'"

def test_companies::employee_has_salary():
    assert hasattr(companies::employee, "salary")
    descriptor = None
    for klass in companies::employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_companies::employee_has_name():
    assert hasattr(companies::employee, "name")
    descriptor = None
    for klass in companies::employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_companies::employee_has_address():
    assert hasattr(companies::employee, "address")
    descriptor = None
    for klass in companies::employee.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_companies::employee_has_mentor():
    assert hasattr(companies::employee, "mentor")
    descriptor = None
    for klass in companies::employee.__mro__:
        if "mentor" in klass.__dict__:
            descriptor = klass.__dict__["mentor"]
            break
    assert isinstance(descriptor, property)



def test_companies::department::employees_is_not_abstract():
    assert not inspect.isabstract(companies::department::employees)


def test_companies::department::employees_constructor_exists():
    assert callable(companies::department::employees.__init__)


def test_companies::department::employees_constructor_args():
    sig = inspect.signature(companies::department::employees.__init__)
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
companies::Visitable_strategy = st.builds(
    companies::Visitable,
)
companies::CSTrace_strategy = st.builds(
    companies::CSTrace,
)
CSTrace_strategy = st.builds(
    CSTrace,
)
companies::department::manager_strategy = st.builds(
    companies::department::manager,
)
companies::department_strategy = st.builds(
    companies::department,
    name=
        safe_text
)
companies::company_strategy = st.builds(
    companies::company,
    name=
        safe_text
)
companies::employee_strategy = st.builds(
    companies::employee,
    salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    address=
        safe_text,
    mentor=
        safe_text
)
companies::department::employees_strategy = st.builds(
    companies::department::employees,
)

@given(instance=companies::Visitable_strategy)
@settings(max_examples=50)
def test_companies::visitable_instantiation(instance):
    assert isinstance(instance, companies::Visitable)

@given(instance=companies::CSTrace_strategy)
@settings(max_examples=50)
def test_companies::cstrace_instantiation(instance):
    assert isinstance(instance, companies::CSTrace)

@given(instance=CSTrace_strategy)
@settings(max_examples=50)
def test_cstrace_instantiation(instance):
    assert isinstance(instance, CSTrace)

@given(instance=companies::department::manager_strategy)
@settings(max_examples=50)
def test_companies::department::manager_instantiation(instance):
    assert isinstance(instance, companies::department::manager)

@given(instance=companies::department_strategy)
@settings(max_examples=50)
def test_companies::department_instantiation(instance):
    assert isinstance(instance, companies::department)

@given(instance=companies::department_strategy)
def test_companies::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=companies::department_strategy)
def test_companies::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=companies::company_strategy)
@settings(max_examples=50)
def test_companies::company_instantiation(instance):
    assert isinstance(instance, companies::company)

@given(instance=companies::company_strategy)
def test_companies::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=companies::company_strategy)
def test_companies::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=companies::employee_strategy)
@settings(max_examples=50)
def test_companies::employee_instantiation(instance):
    assert isinstance(instance, companies::employee)

@given(instance=companies::employee_strategy)
def test_companies::employee_salary_type(instance):
    assert isinstance(instance.salary, float)


@given(instance=companies::employee_strategy)
def test_companies::employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=companies::employee_strategy)
def test_companies::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=companies::employee_strategy)
def test_companies::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=companies::employee_strategy)
def test_companies::employee_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=companies::employee_strategy)
def test_companies::employee_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=companies::employee_strategy)
def test_companies::employee_mentor_type(instance):
    assert isinstance(instance.mentor, str)


@given(instance=companies::employee_strategy)
def test_companies::employee_mentor_setter(instance):
    original = instance.mentor
    instance.mentor = original
    assert instance.mentor == original

@given(instance=companies::department::employees_strategy)
@settings(max_examples=50)
def test_companies::department::employees_instantiation(instance):
    assert isinstance(instance, companies::department::employees)
