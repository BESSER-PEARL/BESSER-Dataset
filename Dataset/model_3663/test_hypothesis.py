import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    iOI::Department,
    Employee,
    iOI::Manager,
    iOI::Position,
    iOI::Employee,
    iOI::Company,
    iOI::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ioi::department_is_not_abstract():
    assert not inspect.isabstract(iOI::Department)


def test_ioi::department_constructor_exists():
    assert callable(iOI::Department.__init__)


def test_ioi::department_constructor_args():
    sig = inspect.signature(iOI::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioi::department_has_name():
    assert hasattr(iOI::Department, "name")
    descriptor = None
    for klass in iOI::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())



def test_ioi::manager_is_not_abstract():
    assert not inspect.isabstract(iOI::Manager)


def test_ioi::manager_constructor_exists():
    assert callable(iOI::Manager.__init__)


def test_ioi::manager_constructor_args():
    sig = inspect.signature(iOI::Manager.__init__)
    params = list(sig.parameters.keys())



def test_ioi::position_is_not_abstract():
    assert not inspect.isabstract(iOI::Position)


def test_ioi::position_constructor_exists():
    assert callable(iOI::Position.__init__)


def test_ioi::position_constructor_args():
    sig = inspect.signature(iOI::Position.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioi::position_has_name():
    assert hasattr(iOI::Position, "name")
    descriptor = None
    for klass in iOI::Position.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioi::employee_is_not_abstract():
    assert not inspect.isabstract(iOI::Employee)


def test_ioi::employee_constructor_exists():
    assert callable(iOI::Employee.__init__)


def test_ioi::employee_constructor_args():
    sig = inspect.signature(iOI::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"

def test_ioi::employee_has_salary():
    assert hasattr(iOI::Employee, "salary")
    descriptor = None
    for klass in iOI::Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_ioi::employee_has_name():
    assert hasattr(iOI::Employee, "name")
    descriptor = None
    for klass in iOI::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioi::company_is_not_abstract():
    assert not inspect.isabstract(iOI::Company)


def test_ioi::company_constructor_exists():
    assert callable(iOI::Company.__init__)


def test_ioi::company_constructor_args():
    sig = inspect.signature(iOI::Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioi::company_has_name():
    assert hasattr(iOI::Company, "name")
    descriptor = None
    for klass in iOI::Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioi::model_is_not_abstract():
    assert not inspect.isabstract(iOI::Model)


def test_ioi::model_constructor_exists():
    assert callable(iOI::Model.__init__)


def test_ioi::model_constructor_args():
    sig = inspect.signature(iOI::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioi::model_has_name():
    assert hasattr(iOI::Model, "name")
    descriptor = None
    for klass in iOI::Model.__mro__:
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
iOI::Department_strategy = st.builds(
    iOI::Department,
    name=
        safe_text
)
Employee_strategy = st.builds(
    Employee,
)
iOI::Manager_strategy = st.builds(
    iOI::Manager,
)
iOI::Position_strategy = st.builds(
    iOI::Position,
    name=
        safe_text
)
iOI::Employee_strategy = st.builds(
    iOI::Employee,
    salary=
        st.integers(),
    name=
        safe_text
)
iOI::Company_strategy = st.builds(
    iOI::Company,
    name=
        safe_text
)
iOI::Model_strategy = st.builds(
    iOI::Model,
    name=
        safe_text
)

@given(instance=iOI::Department_strategy)
@settings(max_examples=50)
def test_ioi::department_instantiation(instance):
    assert isinstance(instance, iOI::Department)

@given(instance=iOI::Department_strategy)
def test_ioi::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iOI::Department_strategy)
def test_ioi::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)

@given(instance=iOI::Manager_strategy)
@settings(max_examples=50)
def test_ioi::manager_instantiation(instance):
    assert isinstance(instance, iOI::Manager)

@given(instance=iOI::Position_strategy)
@settings(max_examples=50)
def test_ioi::position_instantiation(instance):
    assert isinstance(instance, iOI::Position)

@given(instance=iOI::Position_strategy)
def test_ioi::position_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iOI::Position_strategy)
def test_ioi::position_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iOI::Employee_strategy)
@settings(max_examples=50)
def test_ioi::employee_instantiation(instance):
    assert isinstance(instance, iOI::Employee)

@given(instance=iOI::Employee_strategy)
def test_ioi::employee_salary_type(instance):
    assert isinstance(instance.salary, int)


@given(instance=iOI::Employee_strategy)
def test_ioi::employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=iOI::Employee_strategy)
def test_ioi::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iOI::Employee_strategy)
def test_ioi::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iOI::Company_strategy)
@settings(max_examples=50)
def test_ioi::company_instantiation(instance):
    assert isinstance(instance, iOI::Company)

@given(instance=iOI::Company_strategy)
def test_ioi::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iOI::Company_strategy)
def test_ioi::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iOI::Model_strategy)
@settings(max_examples=50)
def test_ioi::model_instantiation(instance):
    assert isinstance(instance, iOI::Model)

@given(instance=iOI::Model_strategy)
def test_ioi::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iOI::Model_strategy)
def test_ioi::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
