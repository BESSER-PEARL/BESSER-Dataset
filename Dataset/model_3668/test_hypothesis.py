import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    exo1::Project,
    exo1::Departement,
    exo1::Company,
    exo1::Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_exo1::project_is_not_abstract():
    assert not inspect.isabstract(exo1::Project)


def test_exo1::project_constructor_exists():
    assert callable(exo1::Project.__init__)


def test_exo1::project_constructor_args():
    sig = inspect.signature(exo1::Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "budget" in params, "Missing parameter 'budget'"

def test_exo1::project_has_name():
    assert hasattr(exo1::Project, "name")
    descriptor = None
    for klass in exo1::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_exo1::project_has_budget():
    assert hasattr(exo1::Project, "budget")
    descriptor = None
    for klass in exo1::Project.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)



def test_exo1::departement_is_not_abstract():
    assert not inspect.isabstract(exo1::Departement)


def test_exo1::departement_constructor_exists():
    assert callable(exo1::Departement.__init__)


def test_exo1::departement_constructor_args():
    sig = inspect.signature(exo1::Departement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "budget" in params, "Missing parameter 'budget'"
    assert "name" in params, "Missing parameter 'name'"

def test_exo1::departement_has_location():
    assert hasattr(exo1::Departement, "location")
    descriptor = None
    for klass in exo1::Departement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_exo1::departement_has_budget():
    assert hasattr(exo1::Departement, "budget")
    descriptor = None
    for klass in exo1::Departement.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)

def test_exo1::departement_has_name():
    assert hasattr(exo1::Departement, "name")
    descriptor = None
    for klass in exo1::Departement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_exo1::company_is_not_abstract():
    assert not inspect.isabstract(exo1::Company)


def test_exo1::company_constructor_exists():
    assert callable(exo1::Company.__init__)


def test_exo1::company_constructor_args():
    sig = inspect.signature(exo1::Company.__init__)
    params = list(sig.parameters.keys())



def test_exo1::employee_is_not_abstract():
    assert not inspect.isabstract(exo1::Employee)


def test_exo1::employee_constructor_exists():
    assert callable(exo1::Employee.__init__)


def test_exo1::employee_constructor_args():
    sig = inspect.signature(exo1::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"

def test_exo1::employee_has_salary():
    assert hasattr(exo1::Employee, "salary")
    descriptor = None
    for klass in exo1::Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_exo1::employee_has_name():
    assert hasattr(exo1::Employee, "name")
    descriptor = None
    for klass in exo1::Employee.__mro__:
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
exo1::Project_strategy = st.builds(
    exo1::Project,
    name=
        safe_text,
    budget=
        st.integers()
)
exo1::Departement_strategy = st.builds(
    exo1::Departement,
    location=
        safe_text,
    budget=
        st.integers(),
    name=
        safe_text
)
exo1::Company_strategy = st.builds(
    exo1::Company,
)
exo1::Employee_strategy = st.builds(
    exo1::Employee,
    salary=
        safe_text,
    name=
        safe_text
)

@given(instance=exo1::Project_strategy)
@settings(max_examples=50)
def test_exo1::project_instantiation(instance):
    assert isinstance(instance, exo1::Project)

@given(instance=exo1::Project_strategy)
def test_exo1::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=exo1::Project_strategy)
def test_exo1::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=exo1::Project_strategy)
def test_exo1::project_budget_type(instance):
    assert isinstance(instance.budget, int)


@given(instance=exo1::Project_strategy)
def test_exo1::project_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=exo1::Departement_strategy)
@settings(max_examples=50)
def test_exo1::departement_instantiation(instance):
    assert isinstance(instance, exo1::Departement)

@given(instance=exo1::Departement_strategy)
def test_exo1::departement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=exo1::Departement_strategy)
def test_exo1::departement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=exo1::Departement_strategy)
def test_exo1::departement_budget_type(instance):
    assert isinstance(instance.budget, int)


@given(instance=exo1::Departement_strategy)
def test_exo1::departement_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=exo1::Departement_strategy)
def test_exo1::departement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=exo1::Departement_strategy)
def test_exo1::departement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=exo1::Company_strategy)
@settings(max_examples=50)
def test_exo1::company_instantiation(instance):
    assert isinstance(instance, exo1::Company)

@given(instance=exo1::Employee_strategy)
@settings(max_examples=50)
def test_exo1::employee_instantiation(instance):
    assert isinstance(instance, exo1::Employee)

@given(instance=exo1::Employee_strategy)
def test_exo1::employee_salary_type(instance):
    assert isinstance(instance.salary, str)


@given(instance=exo1::Employee_strategy)
def test_exo1::employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=exo1::Employee_strategy)
def test_exo1::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=exo1::Employee_strategy)
def test_exo1::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
