import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    education::Student,
    education::School,
    education::Course,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_education::student_is_not_abstract():
    assert not inspect.isabstract(education::Student)


def test_education::student_constructor_exists():
    assert callable(education::Student.__init__)


def test_education::student_constructor_args():
    sig = inspect.signature(education::Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_education::student_has_name():
    assert hasattr(education::Student, "name")
    descriptor = None
    for klass in education::Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_education::school_is_not_abstract():
    assert not inspect.isabstract(education::School)


def test_education::school_constructor_exists():
    assert callable(education::School.__init__)


def test_education::school_constructor_args():
    sig = inspect.signature(education::School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"
    assert "phone" in params, "Missing parameter 'phone'"

def test_education::school_has_name():
    assert hasattr(education::School, "name")
    descriptor = None
    for klass in education::School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_education::school_has_address():
    assert hasattr(education::School, "address")
    descriptor = None
    for klass in education::School.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_education::school_has_phone():
    assert hasattr(education::School, "phone")
    descriptor = None
    for klass in education::School.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)



def test_education::course_is_not_abstract():
    assert not inspect.isabstract(education::Course)


def test_education::course_constructor_exists():
    assert callable(education::Course.__init__)


def test_education::course_constructor_args():
    sig = inspect.signature(education::Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_education::course_has_name():
    assert hasattr(education::Course, "name")
    descriptor = None
    for klass in education::Course.__mro__:
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
education::Student_strategy = st.builds(
    education::Student,
    name=
        safe_text
)
education::School_strategy = st.builds(
    education::School,
    name=
        safe_text,
    address=
        safe_text,
    phone=
        safe_text
)
education::Course_strategy = st.builds(
    education::Course,
    name=
        safe_text
)

@given(instance=education::Student_strategy)
@settings(max_examples=50)
def test_education::student_instantiation(instance):
    assert isinstance(instance, education::Student)

@given(instance=education::Student_strategy)
def test_education::student_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=education::Student_strategy)
def test_education::student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=education::School_strategy)
@settings(max_examples=50)
def test_education::school_instantiation(instance):
    assert isinstance(instance, education::School)

@given(instance=education::School_strategy)
def test_education::school_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=education::School_strategy)
def test_education::school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=education::School_strategy)
def test_education::school_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=education::School_strategy)
def test_education::school_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=education::School_strategy)
def test_education::school_phone_type(instance):
    assert isinstance(instance.phone, str)


@given(instance=education::School_strategy)
def test_education::school_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original

@given(instance=education::Course_strategy)
@settings(max_examples=50)
def test_education::course_instantiation(instance):
    assert isinstance(instance, education::Course)

@given(instance=education::Course_strategy)
def test_education::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=education::Course_strategy)
def test_education::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
