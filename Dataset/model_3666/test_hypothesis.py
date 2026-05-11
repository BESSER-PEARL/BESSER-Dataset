import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sample::Person,
    sample::Group,
    sample::Department,
    sample::Company,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sample::person_is_not_abstract():
    assert not inspect.isabstract(sample::Person)


def test_sample::person_constructor_exists():
    assert callable(sample::Person.__init__)


def test_sample::person_constructor_args():
    sig = inspect.signature(sample::Person.__init__)
    params = list(sig.parameters.keys())
    assert "birthdate" in params, "Missing parameter 'birthdate'"
    assert "name" in params, "Missing parameter 'name'"

def test_sample::person_has_birthdate():
    assert hasattr(sample::Person, "birthdate")
    descriptor = None
    for klass in sample::Person.__mro__:
        if "birthdate" in klass.__dict__:
            descriptor = klass.__dict__["birthdate"]
            break
    assert isinstance(descriptor, property)

def test_sample::person_has_name():
    assert hasattr(sample::Person, "name")
    descriptor = None
    for klass in sample::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sample::group_is_not_abstract():
    assert not inspect.isabstract(sample::Group)


def test_sample::group_constructor_exists():
    assert callable(sample::Group.__init__)


def test_sample::group_constructor_args():
    sig = inspect.signature(sample::Group.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sample::group_has_name():
    assert hasattr(sample::Group, "name")
    descriptor = None
    for klass in sample::Group.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sample::department_is_not_abstract():
    assert not inspect.isabstract(sample::Department)


def test_sample::department_constructor_exists():
    assert callable(sample::Department.__init__)


def test_sample::department_constructor_args():
    sig = inspect.signature(sample::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sample::department_has_name():
    assert hasattr(sample::Department, "name")
    descriptor = None
    for klass in sample::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sample::company_is_not_abstract():
    assert not inspect.isabstract(sample::Company)


def test_sample::company_constructor_exists():
    assert callable(sample::Company.__init__)


def test_sample::company_constructor_args():
    sig = inspect.signature(sample::Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sample::company_has_name():
    assert hasattr(sample::Company, "name")
    descriptor = None
    for klass in sample::Company.__mro__:
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
sample::Person_strategy = st.builds(
    sample::Person,
    birthdate=
        st.dates(),
    name=
        safe_text
)
sample::Group_strategy = st.builds(
    sample::Group,
    name=
        safe_text
)
sample::Department_strategy = st.builds(
    sample::Department,
    name=
        safe_text
)
sample::Company_strategy = st.builds(
    sample::Company,
    name=
        safe_text
)

@given(instance=sample::Person_strategy)
@settings(max_examples=50)
def test_sample::person_instantiation(instance):
    assert isinstance(instance, sample::Person)

@given(instance=sample::Person_strategy)
def test_sample::person_birthdate_type(instance):
    assert isinstance(instance.birthdate, date)


@given(instance=sample::Person_strategy)
def test_sample::person_birthdate_setter(instance):
    original = instance.birthdate
    instance.birthdate = original
    assert instance.birthdate == original

@given(instance=sample::Person_strategy)
def test_sample::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sample::Person_strategy)
def test_sample::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sample::Group_strategy)
@settings(max_examples=50)
def test_sample::group_instantiation(instance):
    assert isinstance(instance, sample::Group)

@given(instance=sample::Group_strategy)
def test_sample::group_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sample::Group_strategy)
def test_sample::group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sample::Department_strategy)
@settings(max_examples=50)
def test_sample::department_instantiation(instance):
    assert isinstance(instance, sample::Department)

@given(instance=sample::Department_strategy)
def test_sample::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sample::Department_strategy)
def test_sample::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sample::Company_strategy)
@settings(max_examples=50)
def test_sample::company_instantiation(instance):
    assert isinstance(instance, sample::Company)

@given(instance=sample::Company_strategy)
def test_sample::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sample::Company_strategy)
def test_sample::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
