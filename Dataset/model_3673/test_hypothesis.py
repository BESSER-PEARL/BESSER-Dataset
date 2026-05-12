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
    assert "name" in params, "Missing parameter 'name'"

def test_company_employee_has_name():
    assert hasattr(company_Employee, "name")
    descriptor = None
    for klass in company_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
    assert "budget" in params, "Missing parameter 'budget'"

def test_company_department_has_name():
    assert hasattr(company_Department, "name")
    descriptor = None
    for klass in company_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company_department_has_budget():
    assert hasattr(company_Department, "budget")
    descriptor = None
    for klass in company_Department.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)



def test_company_company_is_not_abstract():
    assert not inspect.isabstract(company_Company)


def test_company_company_constructor_exists():
    assert callable(company_Company.__init__)


def test_company_company_constructor_args():
    sig = inspect.signature(company_Company.__init__)
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
company_Employee_strategy = st.builds(
    company_Employee,
    name=
        safe_text
)
company_Department_strategy = st.builds(
    company_Department,
    name=
        safe_text,
    budget=
        st.integers()
)
company_Company_strategy = st.builds(
    company_Company,
)

@given(instance=company_Employee_strategy)
@settings(max_examples=50)
def test_company_employee_instantiation(instance):
    assert isinstance(instance, company_Employee)



@given(instance=company_Employee_strategy)
def test_company_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=company_Department_strategy)
@settings(max_examples=50)
def test_company_department_instantiation(instance):
    assert isinstance(instance, company_Department)



@given(instance=company_Department_strategy)
def test_company_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=company_Department_strategy)
def test_company_department_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=company_Company_strategy)
@settings(max_examples=50)
def test_company_company_instantiation(instance):
    assert isinstance(instance, company_Company)
