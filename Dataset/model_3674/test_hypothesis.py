import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    company::Company,
    company::Department,
    company::PhonebookEntry,
    company::Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_company::department_is_not_abstract():
    assert not inspect.isabstract(company::Department)


def test_company::department_constructor_exists():
    assert callable(company::Department.__init__)


def test_company::department_constructor_args():
    sig = inspect.signature(company::Department.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_company::department_has_number():
    assert hasattr(company::Department, "number")
    descriptor = None
    for klass in company::Department.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_company::phonebookentry_is_not_abstract():
    assert not inspect.isabstract(company::PhonebookEntry)


def test_company::phonebookentry_constructor_exists():
    assert callable(company::PhonebookEntry.__init__)


def test_company::phonebookentry_constructor_args():
    sig = inspect.signature(company::PhonebookEntry.__init__)
    params = list(sig.parameters.keys())



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
company::Company_strategy = st.builds(
    company::Company,
    name=
        safe_text
)
company::Department_strategy = st.builds(
    company::Department,
    number=
        st.integers()
)
company::PhonebookEntry_strategy = st.builds(
    company::PhonebookEntry,
)
company::Employee_strategy = st.builds(
    company::Employee,
    name=
        safe_text
)

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

@given(instance=company::Department_strategy)
@settings(max_examples=50)
def test_company::department_instantiation(instance):
    assert isinstance(instance, company::Department)

@given(instance=company::Department_strategy)
def test_company::department_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=company::Department_strategy)
def test_company::department_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=company::PhonebookEntry_strategy)
@settings(max_examples=50)
def test_company::phonebookentry_instantiation(instance):
    assert isinstance(instance, company::PhonebookEntry)

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
