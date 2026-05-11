import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    organization::core::Cass,
    organization::ABase,
    ABase,
    organization::Employee,
    organization::Company,
    organization::Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_organization::core::cass_is_not_abstract():
    assert not inspect.isabstract(organization::core::Cass)


def test_organization::core::cass_constructor_exists():
    assert callable(organization::core::Cass.__init__)


def test_organization::core::cass_constructor_args():
    sig = inspect.signature(organization::core::Cass.__init__)
    params = list(sig.parameters.keys())



def test_organization::abase_is_not_abstract():
    assert not inspect.isabstract(organization::ABase)


def test_organization::abase_constructor_exists():
    assert callable(organization::ABase.__init__)


def test_organization::abase_constructor_args():
    sig = inspect.signature(organization::ABase.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_organization::abase_has_id():
    assert hasattr(organization::ABase, "id")
    descriptor = None
    for klass in organization::ABase.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_abase_is_not_abstract():
    assert not inspect.isabstract(ABase)


def test_abase_constructor_exists():
    assert callable(ABase.__init__)


def test_abase_constructor_args():
    sig = inspect.signature(ABase.__init__)
    params = list(sig.parameters.keys())



def test_organization::employee_is_not_abstract():
    assert not inspect.isabstract(organization::Employee)


def test_organization::employee_constructor_exists():
    assert callable(organization::Employee.__init__)


def test_organization::employee_constructor_args():
    sig = inspect.signature(organization::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_organization::employee_has_name():
    assert hasattr(organization::Employee, "name")
    descriptor = None
    for klass in organization::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_organization::company_is_not_abstract():
    assert not inspect.isabstract(organization::Company)


def test_organization::company_constructor_exists():
    assert callable(organization::Company.__init__)


def test_organization::company_constructor_args():
    sig = inspect.signature(organization::Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_organization::company_has_name():
    assert hasattr(organization::Company, "name")
    descriptor = None
    for klass in organization::Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_organization::department_is_not_abstract():
    assert not inspect.isabstract(organization::Department)


def test_organization::department_constructor_exists():
    assert callable(organization::Department.__init__)


def test_organization::department_constructor_args():
    sig = inspect.signature(organization::Department.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_organization::department_has_number():
    assert hasattr(organization::Department, "number")
    descriptor = None
    for klass in organization::Department.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
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
organization::core::Cass_strategy = st.builds(
    organization::core::Cass,
)
organization::ABase_strategy = st.builds(
    organization::ABase,
    id=
        safe_text
)
ABase_strategy = st.builds(
    ABase,
)
organization::Employee_strategy = st.builds(
    organization::Employee,
    name=
        safe_text
)
organization::Company_strategy = st.builds(
    organization::Company,
    name=
        safe_text
)
organization::Department_strategy = st.builds(
    organization::Department,
    number=
        st.integers()
)

@given(instance=organization::core::Cass_strategy)
@settings(max_examples=50)
def test_organization::core::cass_instantiation(instance):
    assert isinstance(instance, organization::core::Cass)

@given(instance=organization::ABase_strategy)
@settings(max_examples=50)
def test_organization::abase_instantiation(instance):
    assert isinstance(instance, organization::ABase)

@given(instance=organization::ABase_strategy)
def test_organization::abase_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=organization::ABase_strategy)
def test_organization::abase_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ABase_strategy)
@settings(max_examples=50)
def test_abase_instantiation(instance):
    assert isinstance(instance, ABase)

@given(instance=organization::Employee_strategy)
@settings(max_examples=50)
def test_organization::employee_instantiation(instance):
    assert isinstance(instance, organization::Employee)

@given(instance=organization::Employee_strategy)
def test_organization::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=organization::Employee_strategy)
def test_organization::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=organization::Company_strategy)
@settings(max_examples=50)
def test_organization::company_instantiation(instance):
    assert isinstance(instance, organization::Company)

@given(instance=organization::Company_strategy)
def test_organization::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=organization::Company_strategy)
def test_organization::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=organization::Department_strategy)
@settings(max_examples=50)
def test_organization::department_instantiation(instance):
    assert isinstance(instance, organization::Department)

@given(instance=organization::Department_strategy)
def test_organization::department_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=organization::Department_strategy)
def test_organization::department_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original
