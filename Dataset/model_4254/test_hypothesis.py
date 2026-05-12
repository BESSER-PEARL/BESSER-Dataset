import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Organization_Employee,
    Organization_Skill,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_organization_employee_is_not_abstract():
    assert not inspect.isabstract(Organization_Employee)


def test_organization_employee_constructor_exists():
    assert callable(Organization_Employee.__init__)


def test_organization_employee_constructor_args():
    sig = inspect.signature(Organization_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "EmpID" in params, "Missing parameter 'EmpID'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"

def test_organization_employee_has_EmpID():
    assert hasattr(Organization_Employee, "EmpID")
    descriptor = None
    for klass in Organization_Employee.__mro__:
        if "EmpID" in klass.__dict__:
            descriptor = klass.__dict__["EmpID"]
            break
    assert isinstance(descriptor, property)

def test_organization_employee_has_Name():
    assert hasattr(Organization_Employee, "Name")
    descriptor = None
    for klass in Organization_Employee.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_organization_employee_has_Address():
    assert hasattr(Organization_Employee, "Address")
    descriptor = None
    for klass in Organization_Employee.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)



def test_organization_skill_is_not_abstract():
    assert not inspect.isabstract(Organization_Skill)


def test_organization_skill_constructor_exists():
    assert callable(Organization_Skill.__init__)


def test_organization_skill_constructor_args():
    sig = inspect.signature(Organization_Skill.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_organization_skill_has_Name():
    assert hasattr(Organization_Skill, "Name")
    descriptor = None
    for klass in Organization_Skill.__mro__:
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
Organization_Employee_strategy = st.builds(
    Organization_Employee,
    EmpID=
        safe_text,
    Name=
        safe_text,
    Address=
        safe_text
)
Organization_Skill_strategy = st.builds(
    Organization_Skill,
    Name=
        safe_text
)

@given(instance=Organization_Employee_strategy)
@settings(max_examples=50)
def test_organization_employee_instantiation(instance):
    assert isinstance(instance, Organization_Employee)



@given(instance=Organization_Employee_strategy)
def test_organization_employee_EmpID_setter(instance):
    original = instance.EmpID
    instance.EmpID = original
    assert instance.EmpID == original



@given(instance=Organization_Employee_strategy)
def test_organization_employee_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Organization_Employee_strategy)
def test_organization_employee_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original

@given(instance=Organization_Skill_strategy)
@settings(max_examples=50)
def test_organization_skill_instantiation(instance):
    assert isinstance(instance, Organization_Skill)



@given(instance=Organization_Skill_strategy)
def test_organization_skill_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
