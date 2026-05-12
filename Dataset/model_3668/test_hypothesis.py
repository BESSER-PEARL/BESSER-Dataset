import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    exo1_Project,
    exo1_Departement,
    exo1_Company,
    exo1_Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_exo1_project_is_not_abstract():
    assert not inspect.isabstract(exo1_Project)


def test_exo1_project_constructor_exists():
    assert callable(exo1_Project.__init__)


def test_exo1_project_constructor_args():
    sig = inspect.signature(exo1_Project.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"
    assert "name" in params, "Missing parameter 'name'"

def test_exo1_project_has_budget():
    assert hasattr(exo1_Project, "budget")
    descriptor = None
    for klass in exo1_Project.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)

def test_exo1_project_has_name():
    assert hasattr(exo1_Project, "name")
    descriptor = None
    for klass in exo1_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_exo1_departement_is_not_abstract():
    assert not inspect.isabstract(exo1_Departement)


def test_exo1_departement_constructor_exists():
    assert callable(exo1_Departement.__init__)


def test_exo1_departement_constructor_args():
    sig = inspect.signature(exo1_Departement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "location" in params, "Missing parameter 'location'"
    assert "budget" in params, "Missing parameter 'budget'"

def test_exo1_departement_has_name():
    assert hasattr(exo1_Departement, "name")
    descriptor = None
    for klass in exo1_Departement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_exo1_departement_has_location():
    assert hasattr(exo1_Departement, "location")
    descriptor = None
    for klass in exo1_Departement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_exo1_departement_has_budget():
    assert hasattr(exo1_Departement, "budget")
    descriptor = None
    for klass in exo1_Departement.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)



def test_exo1_company_is_not_abstract():
    assert not inspect.isabstract(exo1_Company)


def test_exo1_company_constructor_exists():
    assert callable(exo1_Company.__init__)


def test_exo1_company_constructor_args():
    sig = inspect.signature(exo1_Company.__init__)
    params = list(sig.parameters.keys())



def test_exo1_employee_is_not_abstract():
    assert not inspect.isabstract(exo1_Employee)


def test_exo1_employee_constructor_exists():
    assert callable(exo1_Employee.__init__)


def test_exo1_employee_constructor_args():
    sig = inspect.signature(exo1_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "salary" in params, "Missing parameter 'salary'"

def test_exo1_employee_has_name():
    assert hasattr(exo1_Employee, "name")
    descriptor = None
    for klass in exo1_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_exo1_employee_has_salary():
    assert hasattr(exo1_Employee, "salary")
    descriptor = None
    for klass in exo1_Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
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
exo1_Project_strategy = st.builds(
    exo1_Project,
    budget=
        st.integers(),
    name=
        safe_text
)
exo1_Departement_strategy = st.builds(
    exo1_Departement,
    name=
        safe_text,
    location=
        safe_text,
    budget=
        st.integers()
)
exo1_Company_strategy = st.builds(
    exo1_Company,
)
exo1_Employee_strategy = st.builds(
    exo1_Employee,
    name=
        safe_text,
    salary=
        safe_text
)

@given(instance=exo1_Project_strategy)
@settings(max_examples=50)
def test_exo1_project_instantiation(instance):
    assert isinstance(instance, exo1_Project)



@given(instance=exo1_Project_strategy)
def test_exo1_project_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original



@given(instance=exo1_Project_strategy)
def test_exo1_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=exo1_Departement_strategy)
@settings(max_examples=50)
def test_exo1_departement_instantiation(instance):
    assert isinstance(instance, exo1_Departement)



@given(instance=exo1_Departement_strategy)
def test_exo1_departement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=exo1_Departement_strategy)
def test_exo1_departement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=exo1_Departement_strategy)
def test_exo1_departement_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=exo1_Company_strategy)
@settings(max_examples=50)
def test_exo1_company_instantiation(instance):
    assert isinstance(instance, exo1_Company)

@given(instance=exo1_Employee_strategy)
@settings(max_examples=50)
def test_exo1_employee_instantiation(instance):
    assert isinstance(instance, exo1_Employee)



@given(instance=exo1_Employee_strategy)
def test_exo1_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=exo1_Employee_strategy)
def test_exo1_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original
