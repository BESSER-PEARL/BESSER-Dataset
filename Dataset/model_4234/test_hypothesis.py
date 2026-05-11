import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    cde::Department,
    cde::Company,
    cde::Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cde::department_is_not_abstract():
    assert not inspect.isabstract(cde::Department)


def test_cde::department_constructor_exists():
    assert callable(cde::Department.__init__)


def test_cde::department_constructor_args():
    sig = inspect.signature(cde::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cde::department_has_name():
    assert hasattr(cde::Department, "name")
    descriptor = None
    for klass in cde::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cde::company_is_not_abstract():
    assert not inspect.isabstract(cde::Company)


def test_cde::company_constructor_exists():
    assert callable(cde::Company.__init__)


def test_cde::company_constructor_args():
    sig = inspect.signature(cde::Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cde::company_has_name():
    assert hasattr(cde::Company, "name")
    descriptor = None
    for klass in cde::Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cde::employee_is_not_abstract():
    assert not inspect.isabstract(cde::Employee)


def test_cde::employee_constructor_exists():
    assert callable(cde::Employee.__init__)


def test_cde::employee_constructor_args():
    sig = inspect.signature(cde::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"

def test_cde::employee_has_name():
    assert hasattr(cde::Employee, "name")
    descriptor = None
    for klass in cde::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cde::employee_has_address():
    assert hasattr(cde::Employee, "address")
    descriptor = None
    for klass in cde::Employee.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
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
cde::Department_strategy = st.builds(
    cde::Department,
    name=
        safe_text
)
cde::Company_strategy = st.builds(
    cde::Company,
    name=
        safe_text
)
cde::Employee_strategy = st.builds(
    cde::Employee,
    name=
        safe_text,
    address=
        safe_text
)

@given(instance=cde::Department_strategy)
@settings(max_examples=50)
def test_cde::department_instantiation(instance):
    assert isinstance(instance, cde::Department)

@given(instance=cde::Department_strategy)
def test_cde::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cde::Department_strategy)
def test_cde::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cde::Company_strategy)
@settings(max_examples=50)
def test_cde::company_instantiation(instance):
    assert isinstance(instance, cde::Company)

@given(instance=cde::Company_strategy)
def test_cde::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cde::Company_strategy)
def test_cde::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cde::Employee_strategy)
@settings(max_examples=50)
def test_cde::employee_instantiation(instance):
    assert isinstance(instance, cde::Employee)

@given(instance=cde::Employee_strategy)
def test_cde::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cde::Employee_strategy)
def test_cde::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cde::Employee_strategy)
def test_cde::employee_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=cde::Employee_strategy)
def test_cde::employee_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original
