import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ::101companies::Company,
    ::101companies::Employee,
    ::101companies::Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_::101companies::company_is_not_abstract():
    assert not inspect.isabstract(::101companies::Company)


def test_::101companies::company_constructor_exists():
    assert callable(::101companies::Company.__init__)


def test_::101companies::company_constructor_args():
    sig = inspect.signature(::101companies::Company.__init__)
    params = list(sig.parameters.keys())
    assert "totalSalary" in params, "Missing parameter 'totalSalary'"
    assert "name" in params, "Missing parameter 'name'"

def test_::101companies::company_has_totalSalary():
    assert hasattr(::101companies::Company, "totalSalary")
    descriptor = None
    for klass in ::101companies::Company.__mro__:
        if "totalSalary" in klass.__dict__:
            descriptor = klass.__dict__["totalSalary"]
            break
    assert isinstance(descriptor, property)

def test_::101companies::company_has_name():
    assert hasattr(::101companies::Company, "name")
    descriptor = None
    for klass in ::101companies::Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_::101companies::employee_is_not_abstract():
    assert not inspect.isabstract(::101companies::Employee)


def test_::101companies::employee_constructor_exists():
    assert callable(::101companies::Employee.__init__)


def test_::101companies::employee_constructor_args():
    sig = inspect.signature(::101companies::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"

def test_::101companies::employee_has_salary():
    assert hasattr(::101companies::Employee, "salary")
    descriptor = None
    for klass in ::101companies::Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_::101companies::employee_has_name():
    assert hasattr(::101companies::Employee, "name")
    descriptor = None
    for klass in ::101companies::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_::101companies::employee_has_address():
    assert hasattr(::101companies::Employee, "address")
    descriptor = None
    for klass in ::101companies::Employee.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_::101companies::department_is_not_abstract():
    assert not inspect.isabstract(::101companies::Department)


def test_::101companies::department_constructor_exists():
    assert callable(::101companies::Department.__init__)


def test_::101companies::department_constructor_args():
    sig = inspect.signature(::101companies::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "totalSalary" in params, "Missing parameter 'totalSalary'"

def test_::101companies::department_has_name():
    assert hasattr(::101companies::Department, "name")
    descriptor = None
    for klass in ::101companies::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_::101companies::department_has_totalSalary():
    assert hasattr(::101companies::Department, "totalSalary")
    descriptor = None
    for klass in ::101companies::Department.__mro__:
        if "totalSalary" in klass.__dict__:
            descriptor = klass.__dict__["totalSalary"]
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
::101companies::Company_strategy = st.builds(
    ::101companies::Company,
    totalSalary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
::101companies::Employee_strategy = st.builds(
    ::101companies::Employee,
    salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    address=
        safe_text
)
::101companies::Department_strategy = st.builds(
    ::101companies::Department,
    name=
        safe_text,
    totalSalary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=::101companies::Company_strategy)
@settings(max_examples=50)
def test_::101companies::company_instantiation(instance):
    assert isinstance(instance, ::101companies::Company)

@given(instance=::101companies::Company_strategy)
def test_::101companies::company_totalSalary_type(instance):
    assert isinstance(instance.totalSalary, float)


@given(instance=::101companies::Company_strategy)
def test_::101companies::company_totalSalary_setter(instance):
    original = instance.totalSalary
    instance.totalSalary = original
    assert instance.totalSalary == original

@given(instance=::101companies::Company_strategy)
def test_::101companies::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=::101companies::Company_strategy)
def test_::101companies::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=::101companies::Employee_strategy)
@settings(max_examples=50)
def test_::101companies::employee_instantiation(instance):
    assert isinstance(instance, ::101companies::Employee)

@given(instance=::101companies::Employee_strategy)
def test_::101companies::employee_salary_type(instance):
    assert isinstance(instance.salary, float)


@given(instance=::101companies::Employee_strategy)
def test_::101companies::employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=::101companies::Employee_strategy)
def test_::101companies::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=::101companies::Employee_strategy)
def test_::101companies::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=::101companies::Employee_strategy)
def test_::101companies::employee_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=::101companies::Employee_strategy)
def test_::101companies::employee_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=::101companies::Department_strategy)
@settings(max_examples=50)
def test_::101companies::department_instantiation(instance):
    assert isinstance(instance, ::101companies::Department)

@given(instance=::101companies::Department_strategy)
def test_::101companies::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=::101companies::Department_strategy)
def test_::101companies::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=::101companies::Department_strategy)
def test_::101companies::department_totalSalary_type(instance):
    assert isinstance(instance.totalSalary, float)


@given(instance=::101companies::Department_strategy)
def test_::101companies::department_totalSalary_setter(instance):
    original = instance.totalSalary
    instance.totalSalary = original
    assert instance.totalSalary == original
