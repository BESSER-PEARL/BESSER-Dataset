import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ce::Company,
    ce::Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ce::company_is_not_abstract():
    assert not inspect.isabstract(ce::Company)


def test_ce::company_constructor_exists():
    assert callable(ce::Company.__init__)


def test_ce::company_constructor_args():
    sig = inspect.signature(ce::Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ce::company_has_name():
    assert hasattr(ce::Company, "name")
    descriptor = None
    for klass in ce::Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ce::employee_is_not_abstract():
    assert not inspect.isabstract(ce::Employee)


def test_ce::employee_constructor_exists():
    assert callable(ce::Employee.__init__)


def test_ce::employee_constructor_args():
    sig = inspect.signature(ce::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"
    assert "department" in params, "Missing parameter 'department'"

def test_ce::employee_has_name():
    assert hasattr(ce::Employee, "name")
    descriptor = None
    for klass in ce::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ce::employee_has_address():
    assert hasattr(ce::Employee, "address")
    descriptor = None
    for klass in ce::Employee.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_ce::employee_has_department():
    assert hasattr(ce::Employee, "department")
    descriptor = None
    for klass in ce::Employee.__mro__:
        if "department" in klass.__dict__:
            descriptor = klass.__dict__["department"]
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
ce::Company_strategy = st.builds(
    ce::Company,
    name=
        safe_text
)
ce::Employee_strategy = st.builds(
    ce::Employee,
    name=
        safe_text,
    address=
        safe_text,
    department=
        safe_text
)

@given(instance=ce::Company_strategy)
@settings(max_examples=50)
def test_ce::company_instantiation(instance):
    assert isinstance(instance, ce::Company)

@given(instance=ce::Company_strategy)
def test_ce::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ce::Company_strategy)
def test_ce::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ce::Employee_strategy)
@settings(max_examples=50)
def test_ce::employee_instantiation(instance):
    assert isinstance(instance, ce::Employee)

@given(instance=ce::Employee_strategy)
def test_ce::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ce::Employee_strategy)
def test_ce::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ce::Employee_strategy)
def test_ce::employee_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=ce::Employee_strategy)
def test_ce::employee_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=ce::Employee_strategy)
def test_ce::employee_department_type(instance):
    assert isinstance(instance.department, str)


@given(instance=ce::Employee_strategy)
def test_ce::employee_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original
