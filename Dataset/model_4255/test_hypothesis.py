import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    properties_Employee,
    properties_Address,
    properties_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_properties_employee_is_not_abstract():
    assert not inspect.isabstract(properties_Employee)


def test_properties_employee_constructor_exists():
    assert callable(properties_Employee.__init__)


def test_properties_employee_constructor_args():
    sig = inspect.signature(properties_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "hasAge" in params, "Missing parameter 'hasAge'"
    assert "hasSalary" in params, "Missing parameter 'hasSalary'"

def test_properties_employee_has_hasAge():
    assert hasattr(properties_Employee, "hasAge")
    descriptor = None
    for klass in properties_Employee.__mro__:
        if "hasAge" in klass.__dict__:
            descriptor = klass.__dict__["hasAge"]
            break
    assert isinstance(descriptor, property)

def test_properties_employee_has_hasSalary():
    assert hasattr(properties_Employee, "hasSalary")
    descriptor = None
    for klass in properties_Employee.__mro__:
        if "hasSalary" in klass.__dict__:
            descriptor = klass.__dict__["hasSalary"]
            break
    assert isinstance(descriptor, property)



def test_properties_address_is_not_abstract():
    assert not inspect.isabstract(properties_Address)


def test_properties_address_constructor_exists():
    assert callable(properties_Address.__init__)


def test_properties_address_constructor_args():
    sig = inspect.signature(properties_Address.__init__)
    params = list(sig.parameters.keys())



def test_properties_person_is_not_abstract():
    assert not inspect.isabstract(properties_Person)


def test_properties_person_constructor_exists():
    assert callable(properties_Person.__init__)


def test_properties_person_constructor_args():
    sig = inspect.signature(properties_Person.__init__)
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
Person_strategy = st.builds(
    Person,
)
properties_Employee_strategy = st.builds(
    properties_Employee,
    hasAge=
        st.integers(),
    hasSalary=
        st.integers()
)
properties_Address_strategy = st.builds(
    properties_Address,
)
properties_Person_strategy = st.builds(
    properties_Person,
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=properties_Employee_strategy)
@settings(max_examples=50)
def test_properties_employee_instantiation(instance):
    assert isinstance(instance, properties_Employee)



@given(instance=properties_Employee_strategy)
def test_properties_employee_hasAge_setter(instance):
    original = instance.hasAge
    instance.hasAge = original
    assert instance.hasAge == original



@given(instance=properties_Employee_strategy)
def test_properties_employee_hasSalary_setter(instance):
    original = instance.hasSalary
    instance.hasSalary = original
    assert instance.hasSalary == original

@given(instance=properties_Address_strategy)
@settings(max_examples=50)
def test_properties_address_instantiation(instance):
    assert isinstance(instance, properties_Address)

@given(instance=properties_Person_strategy)
@settings(max_examples=50)
def test_properties_person_instantiation(instance):
    assert isinstance(instance, properties_Person)
