import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Subunit,
    company_Employee,
    company_Dept,
    company_Company,
    company_Person,
    company_Subunit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_subunit_is_not_abstract():
    assert not inspect.isabstract(Subunit)


def test_subunit_constructor_exists():
    assert callable(Subunit.__init__)


def test_subunit_constructor_args():
    sig = inspect.signature(Subunit.__init__)
    params = list(sig.parameters.keys())



def test_company_employee_is_not_abstract():
    assert not inspect.isabstract(company_Employee)


def test_company_employee_constructor_exists():
    assert callable(company_Employee.__init__)


def test_company_employee_constructor_args():
    sig = inspect.signature(company_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"

def test_company_employee_has_salary():
    assert hasattr(company_Employee, "salary")
    descriptor = None
    for klass in company_Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)



def test_company_dept_is_not_abstract():
    assert not inspect.isabstract(company_Dept)


def test_company_dept_constructor_exists():
    assert callable(company_Dept.__init__)


def test_company_dept_constructor_args():
    sig = inspect.signature(company_Dept.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company_dept_has_name():
    assert hasattr(company_Dept, "name")
    descriptor = None
    for klass in company_Dept.__mro__:
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



def test_company_person_is_not_abstract():
    assert not inspect.isabstract(company_Person)


def test_company_person_constructor_exists():
    assert callable(company_Person.__init__)


def test_company_person_constructor_args():
    sig = inspect.signature(company_Person.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"

def test_company_person_has_address():
    assert hasattr(company_Person, "address")
    descriptor = None
    for klass in company_Person.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_company_person_has_name():
    assert hasattr(company_Person, "name")
    descriptor = None
    for klass in company_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_company_subunit_is_not_abstract():
    assert not inspect.isabstract(company_Subunit)


def test_company_subunit_constructor_exists():
    assert callable(company_Subunit.__init__)


def test_company_subunit_constructor_args():
    sig = inspect.signature(company_Subunit.__init__)
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
Subunit_strategy = st.builds(
    Subunit,
)
company_Employee_strategy = st.builds(
    company_Employee,
    salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
company_Dept_strategy = st.builds(
    company_Dept,
    name=
        safe_text
)
company_Company_strategy = st.builds(
    company_Company,
)
company_Person_strategy = st.builds(
    company_Person,
    address=
        safe_text,
    name=
        safe_text
)
company_Subunit_strategy = st.builds(
    company_Subunit,
)

@given(instance=Subunit_strategy)
@settings(max_examples=50)
def test_subunit_instantiation(instance):
    assert isinstance(instance, Subunit)

@given(instance=company_Employee_strategy)
@settings(max_examples=50)
def test_company_employee_instantiation(instance):
    assert isinstance(instance, company_Employee)



@given(instance=company_Employee_strategy)
def test_company_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=company_Dept_strategy)
@settings(max_examples=50)
def test_company_dept_instantiation(instance):
    assert isinstance(instance, company_Dept)



@given(instance=company_Dept_strategy)
def test_company_dept_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=company_Company_strategy)
@settings(max_examples=50)
def test_company_company_instantiation(instance):
    assert isinstance(instance, company_Company)

@given(instance=company_Person_strategy)
@settings(max_examples=50)
def test_company_person_instantiation(instance):
    assert isinstance(instance, company_Person)



@given(instance=company_Person_strategy)
def test_company_person_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=company_Person_strategy)
def test_company_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=company_Subunit_strategy)
@settings(max_examples=50)
def test_company_subunit_instantiation(instance):
    assert isinstance(instance, company_Subunit)
