import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    company::Person,
    company::Subunit,
    Subunit,
    company::Employee,
    company::Dept,
    company::Company,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_company::person_is_not_abstract():
    assert not inspect.isabstract(company::Person)


def test_company::person_constructor_exists():
    assert callable(company::Person.__init__)


def test_company::person_constructor_args():
    sig = inspect.signature(company::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"

def test_company::person_has_name():
    assert hasattr(company::Person, "name")
    descriptor = None
    for klass in company::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company::person_has_address():
    assert hasattr(company::Person, "address")
    descriptor = None
    for klass in company::Person.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_company::subunit_is_not_abstract():
    assert not inspect.isabstract(company::Subunit)


def test_company::subunit_constructor_exists():
    assert callable(company::Subunit.__init__)


def test_company::subunit_constructor_args():
    sig = inspect.signature(company::Subunit.__init__)
    params = list(sig.parameters.keys())



def test_subunit_is_not_abstract():
    assert not inspect.isabstract(Subunit)


def test_subunit_constructor_exists():
    assert callable(Subunit.__init__)


def test_subunit_constructor_args():
    sig = inspect.signature(Subunit.__init__)
    params = list(sig.parameters.keys())



def test_company::employee_is_not_abstract():
    assert not inspect.isabstract(company::Employee)


def test_company::employee_constructor_exists():
    assert callable(company::Employee.__init__)


def test_company::employee_constructor_args():
    sig = inspect.signature(company::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"

def test_company::employee_has_salary():
    assert hasattr(company::Employee, "salary")
    descriptor = None
    for klass in company::Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)



def test_company::dept_is_not_abstract():
    assert not inspect.isabstract(company::Dept)


def test_company::dept_constructor_exists():
    assert callable(company::Dept.__init__)


def test_company::dept_constructor_args():
    sig = inspect.signature(company::Dept.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company::dept_has_name():
    assert hasattr(company::Dept, "name")
    descriptor = None
    for klass in company::Dept.__mro__:
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
company::Person_strategy = st.builds(
    company::Person,
    name=
        safe_text,
    address=
        safe_text
)
company::Subunit_strategy = st.builds(
    company::Subunit,
)
Subunit_strategy = st.builds(
    Subunit,
)
company::Employee_strategy = st.builds(
    company::Employee,
    salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
company::Dept_strategy = st.builds(
    company::Dept,
    name=
        safe_text
)
company::Company_strategy = st.builds(
    company::Company,
)

@given(instance=company::Person_strategy)
@settings(max_examples=50)
def test_company::person_instantiation(instance):
    assert isinstance(instance, company::Person)

@given(instance=company::Person_strategy)
def test_company::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=company::Person_strategy)
def test_company::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=company::Person_strategy)
def test_company::person_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=company::Person_strategy)
def test_company::person_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=company::Subunit_strategy)
@settings(max_examples=50)
def test_company::subunit_instantiation(instance):
    assert isinstance(instance, company::Subunit)

@given(instance=Subunit_strategy)
@settings(max_examples=50)
def test_subunit_instantiation(instance):
    assert isinstance(instance, Subunit)

@given(instance=company::Employee_strategy)
@settings(max_examples=50)
def test_company::employee_instantiation(instance):
    assert isinstance(instance, company::Employee)

@given(instance=company::Employee_strategy)
def test_company::employee_salary_type(instance):
    assert isinstance(instance.salary, float)


@given(instance=company::Employee_strategy)
def test_company::employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=company::Dept_strategy)
@settings(max_examples=50)
def test_company::dept_instantiation(instance):
    assert isinstance(instance, company::Dept)

@given(instance=company::Dept_strategy)
def test_company::dept_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=company::Dept_strategy)
def test_company::dept_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=company::Company_strategy)
@settings(max_examples=50)
def test_company::company_instantiation(instance):
    assert isinstance(instance, company::Company)
