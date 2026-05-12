import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    iOI_Department,
    Employee,
    iOI_Manager,
    iOI_Position,
    iOI_Employee,
    iOI_Company,
    iOI_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ioi_department_is_not_abstract():
    assert not inspect.isabstract(iOI_Department)


def test_ioi_department_constructor_exists():
    assert callable(iOI_Department.__init__)


def test_ioi_department_constructor_args():
    sig = inspect.signature(iOI_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioi_department_has_name():
    assert hasattr(iOI_Department, "name")
    descriptor = None
    for klass in iOI_Department.__mro__:
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



def test_ioi_manager_is_not_abstract():
    assert not inspect.isabstract(iOI_Manager)


def test_ioi_manager_constructor_exists():
    assert callable(iOI_Manager.__init__)


def test_ioi_manager_constructor_args():
    sig = inspect.signature(iOI_Manager.__init__)
    params = list(sig.parameters.keys())



def test_ioi_position_is_not_abstract():
    assert not inspect.isabstract(iOI_Position)


def test_ioi_position_constructor_exists():
    assert callable(iOI_Position.__init__)


def test_ioi_position_constructor_args():
    sig = inspect.signature(iOI_Position.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioi_position_has_name():
    assert hasattr(iOI_Position, "name")
    descriptor = None
    for klass in iOI_Position.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioi_employee_is_not_abstract():
    assert not inspect.isabstract(iOI_Employee)


def test_ioi_employee_constructor_exists():
    assert callable(iOI_Employee.__init__)


def test_ioi_employee_constructor_args():
    sig = inspect.signature(iOI_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"

def test_ioi_employee_has_salary():
    assert hasattr(iOI_Employee, "salary")
    descriptor = None
    for klass in iOI_Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_ioi_employee_has_name():
    assert hasattr(iOI_Employee, "name")
    descriptor = None
    for klass in iOI_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioi_company_is_not_abstract():
    assert not inspect.isabstract(iOI_Company)


def test_ioi_company_constructor_exists():
    assert callable(iOI_Company.__init__)


def test_ioi_company_constructor_args():
    sig = inspect.signature(iOI_Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioi_company_has_name():
    assert hasattr(iOI_Company, "name")
    descriptor = None
    for klass in iOI_Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioi_model_is_not_abstract():
    assert not inspect.isabstract(iOI_Model)


def test_ioi_model_constructor_exists():
    assert callable(iOI_Model.__init__)


def test_ioi_model_constructor_args():
    sig = inspect.signature(iOI_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioi_model_has_name():
    assert hasattr(iOI_Model, "name")
    descriptor = None
    for klass in iOI_Model.__mro__:
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
iOI_Department_strategy = st.builds(
    iOI_Department,
    name=
        safe_text
)
Employee_strategy = st.builds(
    Employee,
)
iOI_Manager_strategy = st.builds(
    iOI_Manager,
)
iOI_Position_strategy = st.builds(
    iOI_Position,
    name=
        safe_text
)
iOI_Employee_strategy = st.builds(
    iOI_Employee,
    salary=
        st.integers(),
    name=
        safe_text
)
iOI_Company_strategy = st.builds(
    iOI_Company,
    name=
        safe_text
)
iOI_Model_strategy = st.builds(
    iOI_Model,
    name=
        safe_text
)

@given(instance=iOI_Department_strategy)
@settings(max_examples=50)
def test_ioi_department_instantiation(instance):
    assert isinstance(instance, iOI_Department)



@given(instance=iOI_Department_strategy)
def test_ioi_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)

@given(instance=iOI_Manager_strategy)
@settings(max_examples=50)
def test_ioi_manager_instantiation(instance):
    assert isinstance(instance, iOI_Manager)

@given(instance=iOI_Position_strategy)
@settings(max_examples=50)
def test_ioi_position_instantiation(instance):
    assert isinstance(instance, iOI_Position)



@given(instance=iOI_Position_strategy)
def test_ioi_position_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iOI_Employee_strategy)
@settings(max_examples=50)
def test_ioi_employee_instantiation(instance):
    assert isinstance(instance, iOI_Employee)



@given(instance=iOI_Employee_strategy)
def test_ioi_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original



@given(instance=iOI_Employee_strategy)
def test_ioi_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iOI_Company_strategy)
@settings(max_examples=50)
def test_ioi_company_instantiation(instance):
    assert isinstance(instance, iOI_Company)



@given(instance=iOI_Company_strategy)
def test_ioi_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iOI_Model_strategy)
@settings(max_examples=50)
def test_ioi_model_instantiation(instance):
    assert isinstance(instance, iOI_Model)



@given(instance=iOI_Model_strategy)
def test_ioi_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
