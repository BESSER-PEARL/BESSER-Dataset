import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    properties::Employee,
    properties::Address,
    properties::Person,
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



def test_properties::employee_is_not_abstract():
    assert not inspect.isabstract(properties::Employee)


def test_properties::employee_constructor_exists():
    assert callable(properties::Employee.__init__)


def test_properties::employee_constructor_args():
    sig = inspect.signature(properties::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "hasAge" in params, "Missing parameter 'hasAge'"
    assert "hasSalary" in params, "Missing parameter 'hasSalary'"

def test_properties::employee_has_hasAge():
    assert hasattr(properties::Employee, "hasAge")
    descriptor = None
    for klass in properties::Employee.__mro__:
        if "hasAge" in klass.__dict__:
            descriptor = klass.__dict__["hasAge"]
            break
    assert isinstance(descriptor, property)

def test_properties::employee_has_hasSalary():
    assert hasattr(properties::Employee, "hasSalary")
    descriptor = None
    for klass in properties::Employee.__mro__:
        if "hasSalary" in klass.__dict__:
            descriptor = klass.__dict__["hasSalary"]
            break
    assert isinstance(descriptor, property)



def test_properties::address_is_not_abstract():
    assert not inspect.isabstract(properties::Address)


def test_properties::address_constructor_exists():
    assert callable(properties::Address.__init__)


def test_properties::address_constructor_args():
    sig = inspect.signature(properties::Address.__init__)
    params = list(sig.parameters.keys())



def test_properties::person_is_not_abstract():
    assert not inspect.isabstract(properties::Person)


def test_properties::person_constructor_exists():
    assert callable(properties::Person.__init__)


def test_properties::person_constructor_args():
    sig = inspect.signature(properties::Person.__init__)
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
properties::Employee_strategy = st.builds(
    properties::Employee,
    hasAge=
        st.integers(),
    hasSalary=
        st.integers()
)
properties::Address_strategy = st.builds(
    properties::Address,
)
properties::Person_strategy = st.builds(
    properties::Person,
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=properties::Employee_strategy)
@settings(max_examples=50)
def test_properties::employee_instantiation(instance):
    assert isinstance(instance, properties::Employee)

@given(instance=properties::Employee_strategy)
def test_properties::employee_hasAge_type(instance):
    assert isinstance(instance.hasAge, int)


@given(instance=properties::Employee_strategy)
def test_properties::employee_hasAge_setter(instance):
    original = instance.hasAge
    instance.hasAge = original
    assert instance.hasAge == original

@given(instance=properties::Employee_strategy)
def test_properties::employee_hasSalary_type(instance):
    assert isinstance(instance.hasSalary, int)


@given(instance=properties::Employee_strategy)
def test_properties::employee_hasSalary_setter(instance):
    original = instance.hasSalary
    instance.hasSalary = original
    assert instance.hasSalary == original

@given(instance=properties::Address_strategy)
@settings(max_examples=50)
def test_properties::address_instantiation(instance):
    assert isinstance(instance, properties::Address)

@given(instance=properties::Person_strategy)
@settings(max_examples=50)
def test_properties::person_instantiation(instance):
    assert isinstance(instance, properties::Person)
