import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    employee_NamedEntity,
    Department,
    employee_PoorDepartment,
    employee_RichDepartment,
    NamedEntity,
    employee_Department,
    employee_Employee,
    employee_Company,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_employee_namedentity_is_not_abstract():
    assert not inspect.isabstract(employee_NamedEntity)


def test_employee_namedentity_constructor_exists():
    assert callable(employee_NamedEntity.__init__)


def test_employee_namedentity_constructor_args():
    sig = inspect.signature(employee_NamedEntity.__init__)
    params = list(sig.parameters.keys())
    assert "wrongFeature" in params, "Missing parameter 'wrongFeature'"
    assert "name" in params, "Missing parameter 'name'"

def test_employee_namedentity_has_wrongFeature():
    assert hasattr(employee_NamedEntity, "wrongFeature")
    descriptor = None
    for klass in employee_NamedEntity.__mro__:
        if "wrongFeature" in klass.__dict__:
            descriptor = klass.__dict__["wrongFeature"]
            break
    assert isinstance(descriptor, property)

def test_employee_namedentity_has_name():
    assert hasattr(employee_NamedEntity, "name")
    descriptor = None
    for klass in employee_NamedEntity.__mro__:
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



def test_employee_poordepartment_is_not_abstract():
    assert not inspect.isabstract(employee_PoorDepartment)


def test_employee_poordepartment_constructor_exists():
    assert callable(employee_PoorDepartment.__init__)


def test_employee_poordepartment_constructor_args():
    sig = inspect.signature(employee_PoorDepartment.__init__)
    params = list(sig.parameters.keys())



def test_employee_richdepartment_is_not_abstract():
    assert not inspect.isabstract(employee_RichDepartment)


def test_employee_richdepartment_constructor_exists():
    assert callable(employee_RichDepartment.__init__)


def test_employee_richdepartment_constructor_args():
    sig = inspect.signature(employee_RichDepartment.__init__)
    params = list(sig.parameters.keys())



def test_namedentity_is_not_abstract():
    assert not inspect.isabstract(NamedEntity)


def test_namedentity_constructor_exists():
    assert callable(NamedEntity.__init__)


def test_namedentity_constructor_args():
    sig = inspect.signature(NamedEntity.__init__)
    params = list(sig.parameters.keys())



def test_employee_department_is_not_abstract():
    assert not inspect.isabstract(employee_Department)


def test_employee_department_constructor_exists():
    assert callable(employee_Department.__init__)


def test_employee_department_constructor_args():
    sig = inspect.signature(employee_Department.__init__)
    params = list(sig.parameters.keys())



def test_employee_employee_is_not_abstract():
    assert not inspect.isabstract(employee_Employee)


def test_employee_employee_constructor_exists():
    assert callable(employee_Employee.__init__)


def test_employee_employee_constructor_args():
    sig = inspect.signature(employee_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "wage" in params, "Missing parameter 'wage'"

def test_employee_employee_has_wage():
    assert hasattr(employee_Employee, "wage")
    descriptor = None
    for klass in employee_Employee.__mro__:
        if "wage" in klass.__dict__:
            descriptor = klass.__dict__["wage"]
            break
    assert isinstance(descriptor, property)



def test_employee_company_is_not_abstract():
    assert not inspect.isabstract(employee_Company)


def test_employee_company_constructor_exists():
    assert callable(employee_Company.__init__)


def test_employee_company_constructor_args():
    sig = inspect.signature(employee_Company.__init__)
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
employee_NamedEntity_strategy = st.builds(
    employee_NamedEntity,
    wrongFeature=
        st.integers(),
    name=
        safe_text
)
Department_strategy = st.builds(
    Department,
)
employee_PoorDepartment_strategy = st.builds(
    employee_PoorDepartment,
)
employee_RichDepartment_strategy = st.builds(
    employee_RichDepartment,
)
NamedEntity_strategy = st.builds(
    NamedEntity,
)
employee_Department_strategy = st.builds(
    employee_Department,
)
employee_Employee_strategy = st.builds(
    employee_Employee,
    wage=
        st.integers()
)
employee_Company_strategy = st.builds(
    employee_Company,
)

@given(instance=employee_NamedEntity_strategy)
@settings(max_examples=50)
def test_employee_namedentity_instantiation(instance):
    assert isinstance(instance, employee_NamedEntity)



@given(instance=employee_NamedEntity_strategy)
def test_employee_namedentity_wrongFeature_setter(instance):
    original = instance.wrongFeature
    instance.wrongFeature = original
    assert instance.wrongFeature == original



@given(instance=employee_NamedEntity_strategy)
def test_employee_namedentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)

@given(instance=employee_PoorDepartment_strategy)
@settings(max_examples=50)
def test_employee_poordepartment_instantiation(instance):
    assert isinstance(instance, employee_PoorDepartment)

@given(instance=employee_RichDepartment_strategy)
@settings(max_examples=50)
def test_employee_richdepartment_instantiation(instance):
    assert isinstance(instance, employee_RichDepartment)

@given(instance=NamedEntity_strategy)
@settings(max_examples=50)
def test_namedentity_instantiation(instance):
    assert isinstance(instance, NamedEntity)

@given(instance=employee_Department_strategy)
@settings(max_examples=50)
def test_employee_department_instantiation(instance):
    assert isinstance(instance, employee_Department)

@given(instance=employee_Employee_strategy)
@settings(max_examples=50)
def test_employee_employee_instantiation(instance):
    assert isinstance(instance, employee_Employee)



@given(instance=employee_Employee_strategy)
def test_employee_employee_wage_setter(instance):
    original = instance.wage
    instance.wage = original
    assert instance.wage == original

@given(instance=employee_Company_strategy)
@settings(max_examples=50)
def test_employee_company_instantiation(instance):
    assert isinstance(instance, employee_Company)
