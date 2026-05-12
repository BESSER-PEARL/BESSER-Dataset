import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ce_Company,
    ce_Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ce_company_is_not_abstract():
    assert not inspect.isabstract(ce_Company)


def test_ce_company_constructor_exists():
    assert callable(ce_Company.__init__)


def test_ce_company_constructor_args():
    sig = inspect.signature(ce_Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ce_company_has_name():
    assert hasattr(ce_Company, "name")
    descriptor = None
    for klass in ce_Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ce_employee_is_not_abstract():
    assert not inspect.isabstract(ce_Employee)


def test_ce_employee_constructor_exists():
    assert callable(ce_Employee.__init__)


def test_ce_employee_constructor_args():
    sig = inspect.signature(ce_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "department" in params, "Missing parameter 'department'"
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"

def test_ce_employee_has_department():
    assert hasattr(ce_Employee, "department")
    descriptor = None
    for klass in ce_Employee.__mro__:
        if "department" in klass.__dict__:
            descriptor = klass.__dict__["department"]
            break
    assert isinstance(descriptor, property)

def test_ce_employee_has_address():
    assert hasattr(ce_Employee, "address")
    descriptor = None
    for klass in ce_Employee.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_ce_employee_has_name():
    assert hasattr(ce_Employee, "name")
    descriptor = None
    for klass in ce_Employee.__mro__:
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
ce_Company_strategy = st.builds(
    ce_Company,
    name=
        safe_text
)
ce_Employee_strategy = st.builds(
    ce_Employee,
    department=
        safe_text,
    address=
        safe_text,
    name=
        safe_text
)

@given(instance=ce_Company_strategy)
@settings(max_examples=50)
def test_ce_company_instantiation(instance):
    assert isinstance(instance, ce_Company)



@given(instance=ce_Company_strategy)
def test_ce_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ce_Employee_strategy)
@settings(max_examples=50)
def test_ce_employee_instantiation(instance):
    assert isinstance(instance, ce_Employee)



@given(instance=ce_Employee_strategy)
def test_ce_employee_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original



@given(instance=ce_Employee_strategy)
def test_ce_employee_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=ce_Employee_strategy)
def test_ce_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
