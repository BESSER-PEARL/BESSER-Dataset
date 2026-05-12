import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sample_Person,
    sample_Group,
    sample_Department,
    sample_Company,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sample_person_is_not_abstract():
    assert not inspect.isabstract(sample_Person)


def test_sample_person_constructor_exists():
    assert callable(sample_Person.__init__)


def test_sample_person_constructor_args():
    sig = inspect.signature(sample_Person.__init__)
    params = list(sig.parameters.keys())
    assert "birthdate" in params, "Missing parameter 'birthdate'"
    assert "name" in params, "Missing parameter 'name'"

def test_sample_person_has_birthdate():
    assert hasattr(sample_Person, "birthdate")
    descriptor = None
    for klass in sample_Person.__mro__:
        if "birthdate" in klass.__dict__:
            descriptor = klass.__dict__["birthdate"]
            break
    assert isinstance(descriptor, property)

def test_sample_person_has_name():
    assert hasattr(sample_Person, "name")
    descriptor = None
    for klass in sample_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sample_group_is_not_abstract():
    assert not inspect.isabstract(sample_Group)


def test_sample_group_constructor_exists():
    assert callable(sample_Group.__init__)


def test_sample_group_constructor_args():
    sig = inspect.signature(sample_Group.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sample_group_has_name():
    assert hasattr(sample_Group, "name")
    descriptor = None
    for klass in sample_Group.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sample_department_is_not_abstract():
    assert not inspect.isabstract(sample_Department)


def test_sample_department_constructor_exists():
    assert callable(sample_Department.__init__)


def test_sample_department_constructor_args():
    sig = inspect.signature(sample_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sample_department_has_name():
    assert hasattr(sample_Department, "name")
    descriptor = None
    for klass in sample_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sample_company_is_not_abstract():
    assert not inspect.isabstract(sample_Company)


def test_sample_company_constructor_exists():
    assert callable(sample_Company.__init__)


def test_sample_company_constructor_args():
    sig = inspect.signature(sample_Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sample_company_has_name():
    assert hasattr(sample_Company, "name")
    descriptor = None
    for klass in sample_Company.__mro__:
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
sample_Person_strategy = st.builds(
    sample_Person,
    birthdate=
        st.dates(),
    name=
        safe_text
)
sample_Group_strategy = st.builds(
    sample_Group,
    name=
        safe_text
)
sample_Department_strategy = st.builds(
    sample_Department,
    name=
        safe_text
)
sample_Company_strategy = st.builds(
    sample_Company,
    name=
        safe_text
)

@given(instance=sample_Person_strategy)
@settings(max_examples=50)
def test_sample_person_instantiation(instance):
    assert isinstance(instance, sample_Person)



@given(instance=sample_Person_strategy)
def test_sample_person_birthdate_setter(instance):
    original = instance.birthdate
    instance.birthdate = original
    assert instance.birthdate == original



@given(instance=sample_Person_strategy)
def test_sample_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sample_Group_strategy)
@settings(max_examples=50)
def test_sample_group_instantiation(instance):
    assert isinstance(instance, sample_Group)



@given(instance=sample_Group_strategy)
def test_sample_group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sample_Department_strategy)
@settings(max_examples=50)
def test_sample_department_instantiation(instance):
    assert isinstance(instance, sample_Department)



@given(instance=sample_Department_strategy)
def test_sample_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sample_Company_strategy)
@settings(max_examples=50)
def test_sample_company_instantiation(instance):
    assert isinstance(instance, sample_Company)



@given(instance=sample_Company_strategy)
def test_sample_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
