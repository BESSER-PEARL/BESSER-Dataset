import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    company::Visitable,
    Visitable,
    company::Employee,
    company::Department,
    company::Company,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_company::visitable_is_not_abstract():
    assert not inspect.isabstract(company::Visitable)


def test_company::visitable_constructor_exists():
    assert callable(company::Visitable.__init__)


def test_company::visitable_constructor_args():
    sig = inspect.signature(company::Visitable.__init__)
    params = list(sig.parameters.keys())



def test_visitable_is_not_abstract():
    assert not inspect.isabstract(Visitable)


def test_visitable_constructor_exists():
    assert callable(Visitable.__init__)


def test_visitable_constructor_args():
    sig = inspect.signature(Visitable.__init__)
    params = list(sig.parameters.keys())



def test_company::employee_is_not_abstract():
    assert not inspect.isabstract(company::Employee)


def test_company::employee_constructor_exists():
    assert callable(company::Employee.__init__)


def test_company::employee_constructor_args():
    sig = inspect.signature(company::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"

def test_company::employee_has_address():
    assert hasattr(company::Employee, "address")
    descriptor = None
    for klass in company::Employee.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_company::employee_has_salary():
    assert hasattr(company::Employee, "salary")
    descriptor = None
    for klass in company::Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_company::employee_has_name():
    assert hasattr(company::Employee, "name")
    descriptor = None
    for klass in company::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_company::department_is_not_abstract():
    assert not inspect.isabstract(company::Department)


def test_company::department_constructor_exists():
    assert callable(company::Department.__init__)


def test_company::department_constructor_args():
    sig = inspect.signature(company::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company::department_has_name():
    assert hasattr(company::Department, "name")
    descriptor = None
    for klass in company::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_company::company_is_not_abstract():
    assert not inspect.isabstract(company::Company)


def test_company::company_constructor_exists():
    assert callable(company::Company.__init__)


def test_company::company_constructor_args():
    sig = inspect.signature(company::Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company::company_has_name():
    assert hasattr(company::Company, "name")
    descriptor = None
    for klass in company::Company.__mro__:
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
company::Visitable_strategy = st.builds(
    company::Visitable,
)
Visitable_strategy = st.builds(
    Visitable,
)
company::Employee_strategy = st.builds(
    company::Employee,
    address=
        safe_text,
    salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
company::Department_strategy = st.builds(
    company::Department,
    name=
        safe_text
)
company::Company_strategy = st.builds(
    company::Company,
    name=
        safe_text
)

@given(instance=company::Visitable_strategy)
@settings(max_examples=50)
def test_company::visitable_instantiation(instance):
    assert isinstance(instance, company::Visitable)

@given(instance=Visitable_strategy)
@settings(max_examples=50)
def test_visitable_instantiation(instance):
    assert isinstance(instance, Visitable)

@given(instance=company::Employee_strategy)
@settings(max_examples=50)
def test_company::employee_instantiation(instance):
    assert isinstance(instance, company::Employee)

@given(instance=company::Employee_strategy)
def test_company::employee_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=company::Employee_strategy)
def test_company::employee_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=company::Employee_strategy)
def test_company::employee_salary_type(instance):
    assert isinstance(instance.salary, float)


@given(instance=company::Employee_strategy)
def test_company::employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=company::Employee_strategy)
def test_company::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=company::Employee_strategy)
def test_company::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=company::Department_strategy)
@settings(max_examples=50)
def test_company::department_instantiation(instance):
    assert isinstance(instance, company::Department)

@given(instance=company::Department_strategy)
def test_company::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=company::Department_strategy)
def test_company::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=company::Company_strategy)
@settings(max_examples=50)
def test_company::company_instantiation(instance):
    assert isinstance(instance, company::Company)

@given(instance=company::Company_strategy)
def test_company::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=company::Company_strategy)
def test_company::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
