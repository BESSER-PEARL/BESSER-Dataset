import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    company::Employee,
    company::Department,
    company::Company,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_company::employee_is_not_abstract():
    assert not inspect.isabstract(company::Employee)


def test_company::employee_constructor_exists():
    assert callable(company::Employee.__init__)


def test_company::employee_constructor_args():
    sig = inspect.signature(company::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

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
    assert "budget" in params, "Missing parameter 'budget'"

def test_company::department_has_name():
    assert hasattr(company::Department, "name")
    descriptor = None
    for klass in company::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company::department_has_budget():
    assert hasattr(company::Department, "budget")
    descriptor = None
    for klass in company::Department.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
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
company::Employee_strategy = st.builds(
    company::Employee,
    name=
        safe_text
)
company::Department_strategy = st.builds(
    company::Department,
    name=
        safe_text,
    budget=
        st.integers()
)
company::Company_strategy = st.builds(
    company::Company,
)

@given(instance=company::Employee_strategy)
@settings(max_examples=50)
def test_company::employee_instantiation(instance):
    assert isinstance(instance, company::Employee)

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

@given(instance=company::Department_strategy)
def test_company::department_budget_type(instance):
    assert isinstance(instance.budget, int)


@given(instance=company::Department_strategy)
def test_company::department_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=company::Company_strategy)
@settings(max_examples=50)
def test_company::company_instantiation(instance):
    assert isinstance(instance, company::Company)
