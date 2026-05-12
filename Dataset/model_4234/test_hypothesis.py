import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    cde_Department,
    cde_Company,
    cde_Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cde_department_is_not_abstract():
    assert not inspect.isabstract(cde_Department)


def test_cde_department_constructor_exists():
    assert callable(cde_Department.__init__)


def test_cde_department_constructor_args():
    sig = inspect.signature(cde_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cde_department_has_name():
    assert hasattr(cde_Department, "name")
    descriptor = None
    for klass in cde_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cde_company_is_not_abstract():
    assert not inspect.isabstract(cde_Company)


def test_cde_company_constructor_exists():
    assert callable(cde_Company.__init__)


def test_cde_company_constructor_args():
    sig = inspect.signature(cde_Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cde_company_has_name():
    assert hasattr(cde_Company, "name")
    descriptor = None
    for klass in cde_Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cde_employee_is_not_abstract():
    assert not inspect.isabstract(cde_Employee)


def test_cde_employee_constructor_exists():
    assert callable(cde_Employee.__init__)


def test_cde_employee_constructor_args():
    sig = inspect.signature(cde_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"

def test_cde_employee_has_address():
    assert hasattr(cde_Employee, "address")
    descriptor = None
    for klass in cde_Employee.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_cde_employee_has_name():
    assert hasattr(cde_Employee, "name")
    descriptor = None
    for klass in cde_Employee.__mro__:
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
cde_Department_strategy = st.builds(
    cde_Department,
    name=
        safe_text
)
cde_Company_strategy = st.builds(
    cde_Company,
    name=
        safe_text
)
cde_Employee_strategy = st.builds(
    cde_Employee,
    address=
        safe_text,
    name=
        safe_text
)

@given(instance=cde_Department_strategy)
@settings(max_examples=50)
def test_cde_department_instantiation(instance):
    assert isinstance(instance, cde_Department)



@given(instance=cde_Department_strategy)
def test_cde_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cde_Company_strategy)
@settings(max_examples=50)
def test_cde_company_instantiation(instance):
    assert isinstance(instance, cde_Company)



@given(instance=cde_Company_strategy)
def test_cde_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cde_Employee_strategy)
@settings(max_examples=50)
def test_cde_employee_instantiation(instance):
    assert isinstance(instance, cde_Employee)



@given(instance=cde_Employee_strategy)
def test_cde_employee_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=cde_Employee_strategy)
def test_cde_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
