import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    employee::NamedEntity,
    Department,
    employee::PoorDepartment,
    employee::RichDepartment,
    NamedEntity,
    employee::Department,
    employee::Employee,
    employee::Company,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_employee::namedentity_is_not_abstract():
    assert not inspect.isabstract(employee::NamedEntity)


def test_employee::namedentity_constructor_exists():
    assert callable(employee::NamedEntity.__init__)


def test_employee::namedentity_constructor_args():
    sig = inspect.signature(employee::NamedEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_employee::namedentity_has_name():
    assert hasattr(employee::NamedEntity, "name")
    descriptor = None
    for klass in employee::NamedEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())



def test_employee::poordepartment_is_not_abstract():
    assert not inspect.isabstract(employee::PoorDepartment)


def test_employee::poordepartment_constructor_exists():
    assert callable(employee::PoorDepartment.__init__)


def test_employee::poordepartment_constructor_args():
    sig = inspect.signature(employee::PoorDepartment.__init__)
    params = list(sig.parameters.keys())



def test_employee::richdepartment_is_not_abstract():
    assert not inspect.isabstract(employee::RichDepartment)


def test_employee::richdepartment_constructor_exists():
    assert callable(employee::RichDepartment.__init__)


def test_employee::richdepartment_constructor_args():
    sig = inspect.signature(employee::RichDepartment.__init__)
    params = list(sig.parameters.keys())



def test_namedentity_is_not_abstract():
    assert not inspect.isabstract(NamedEntity)


def test_namedentity_constructor_exists():
    assert callable(NamedEntity.__init__)


def test_namedentity_constructor_args():
    sig = inspect.signature(NamedEntity.__init__)
    params = list(sig.parameters.keys())



def test_employee::department_is_not_abstract():
    assert not inspect.isabstract(employee::Department)


def test_employee::department_constructor_exists():
    assert callable(employee::Department.__init__)


def test_employee::department_constructor_args():
    sig = inspect.signature(employee::Department.__init__)
    params = list(sig.parameters.keys())



def test_employee::employee_is_not_abstract():
    assert not inspect.isabstract(employee::Employee)


def test_employee::employee_constructor_exists():
    assert callable(employee::Employee.__init__)


def test_employee::employee_constructor_args():
    sig = inspect.signature(employee::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "wage" in params, "Missing parameter 'wage'"

def test_employee::employee_has_wage():
    assert hasattr(employee::Employee, "wage")
    descriptor = None
    for klass in employee::Employee.__mro__:
        if "wage" in klass.__dict__:
            descriptor = klass.__dict__["wage"]
            break
    assert isinstance(descriptor, property)



def test_employee::company_is_not_abstract():
    assert not inspect.isabstract(employee::Company)


def test_employee::company_constructor_exists():
    assert callable(employee::Company.__init__)


def test_employee::company_constructor_args():
    sig = inspect.signature(employee::Company.__init__)
    params = list(sig.parameters.keys())


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
employee::NamedEntity_strategy = st.builds(
    employee::NamedEntity,
    name=
        safe_text
)
Department_strategy = st.builds(
    Department,
)
employee::PoorDepartment_strategy = st.builds(
    employee::PoorDepartment,
)
employee::RichDepartment_strategy = st.builds(
    employee::RichDepartment,
)
NamedEntity_strategy = st.builds(
    NamedEntity,
)
employee::Department_strategy = st.builds(
    employee::Department,
)
employee::Employee_strategy = st.builds(
    employee::Employee,
    wage=
        st.integers()
)
employee::Company_strategy = st.builds(
    employee::Company,
)

@given(instance=employee::NamedEntity_strategy)
@settings(max_examples=50)
def test_employee::namedentity_instantiation(instance):
    assert isinstance(instance, employee::NamedEntity)

@given(instance=employee::NamedEntity_strategy)
def test_employee::namedentity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=employee::NamedEntity_strategy)
def test_employee::namedentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)

@given(instance=employee::PoorDepartment_strategy)
@settings(max_examples=50)
def test_employee::poordepartment_instantiation(instance):
    assert isinstance(instance, employee::PoorDepartment)

@given(instance=employee::RichDepartment_strategy)
@settings(max_examples=50)
def test_employee::richdepartment_instantiation(instance):
    assert isinstance(instance, employee::RichDepartment)

@given(instance=NamedEntity_strategy)
@settings(max_examples=50)
def test_namedentity_instantiation(instance):
    assert isinstance(instance, NamedEntity)

@given(instance=employee::Department_strategy)
@settings(max_examples=50)
def test_employee::department_instantiation(instance):
    assert isinstance(instance, employee::Department)

@given(instance=employee::Employee_strategy)
@settings(max_examples=50)
def test_employee::employee_instantiation(instance):
    assert isinstance(instance, employee::Employee)

@given(instance=employee::Employee_strategy)
def test_employee::employee_wage_type(instance):
    assert isinstance(instance.wage, int)


@given(instance=employee::Employee_strategy)
def test_employee::employee_wage_setter(instance):
    original = instance.wage
    instance.wage = original
    assert instance.wage == original

@given(instance=employee::Company_strategy)
@settings(max_examples=50)
def test_employee::company_instantiation(instance):
    assert isinstance(instance, employee::Company)
