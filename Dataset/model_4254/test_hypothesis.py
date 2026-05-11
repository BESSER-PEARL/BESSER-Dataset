import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Organization::Employee,
    Organization::Skill,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_organization::employee_is_not_abstract():
    assert not inspect.isabstract(Organization::Employee)


def test_organization::employee_constructor_exists():
    assert callable(Organization::Employee.__init__)


def test_organization::employee_constructor_args():
    sig = inspect.signature(Organization::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "EmpID" in params, "Missing parameter 'EmpID'"

def test_organization::employee_has_Name():
    assert hasattr(Organization::Employee, "Name")
    descriptor = None
    for klass in Organization::Employee.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_organization::employee_has_Address():
    assert hasattr(Organization::Employee, "Address")
    descriptor = None
    for klass in Organization::Employee.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_organization::employee_has_EmpID():
    assert hasattr(Organization::Employee, "EmpID")
    descriptor = None
    for klass in Organization::Employee.__mro__:
        if "EmpID" in klass.__dict__:
            descriptor = klass.__dict__["EmpID"]
            break
    assert isinstance(descriptor, property)



def test_organization::skill_is_not_abstract():
    assert not inspect.isabstract(Organization::Skill)


def test_organization::skill_constructor_exists():
    assert callable(Organization::Skill.__init__)


def test_organization::skill_constructor_args():
    sig = inspect.signature(Organization::Skill.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_organization::skill_has_Name():
    assert hasattr(Organization::Skill, "Name")
    descriptor = None
    for klass in Organization::Skill.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
Organization::Employee_strategy = st.builds(
    Organization::Employee,
    Name=
        safe_text,
    Address=
        safe_text,
    EmpID=
        safe_text
)
Organization::Skill_strategy = st.builds(
    Organization::Skill,
    Name=
        safe_text
)

@given(instance=Organization::Employee_strategy)
@settings(max_examples=50)
def test_organization::employee_instantiation(instance):
    assert isinstance(instance, Organization::Employee)

@given(instance=Organization::Employee_strategy)
def test_organization::employee_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Organization::Employee_strategy)
def test_organization::employee_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Organization::Employee_strategy)
def test_organization::employee_Address_type(instance):
    assert isinstance(instance.Address, str)


@given(instance=Organization::Employee_strategy)
def test_organization::employee_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original

@given(instance=Organization::Employee_strategy)
def test_organization::employee_EmpID_type(instance):
    assert isinstance(instance.EmpID, str)


@given(instance=Organization::Employee_strategy)
def test_organization::employee_EmpID_setter(instance):
    original = instance.EmpID
    instance.EmpID = original
    assert instance.EmpID == original

@given(instance=Organization::Skill_strategy)
@settings(max_examples=50)
def test_organization::skill_instantiation(instance):
    assert isinstance(instance, Organization::Skill)

@given(instance=Organization::Skill_strategy)
def test_organization::skill_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Organization::Skill_strategy)
def test_organization::skill_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
