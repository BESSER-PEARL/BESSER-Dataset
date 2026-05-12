import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    education_Course,
    education_Student,
    education_School,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_education_course_is_not_abstract():
    assert not inspect.isabstract(education_Course)


def test_education_course_constructor_exists():
    assert callable(education_Course.__init__)


def test_education_course_constructor_args():
    sig = inspect.signature(education_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_education_course_has_name():
    assert hasattr(education_Course, "name")
    descriptor = None
    for klass in education_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_education_student_is_not_abstract():
    assert not inspect.isabstract(education_Student)


def test_education_student_constructor_exists():
    assert callable(education_Student.__init__)


def test_education_student_constructor_args():
    sig = inspect.signature(education_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_education_student_has_name():
    assert hasattr(education_Student, "name")
    descriptor = None
    for klass in education_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_education_school_is_not_abstract():
    assert not inspect.isabstract(education_School)


def test_education_school_constructor_exists():
    assert callable(education_School.__init__)


def test_education_school_constructor_args():
    sig = inspect.signature(education_School.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"
    assert "phone" in params, "Missing parameter 'phone'"

def test_education_school_has_address():
    assert hasattr(education_School, "address")
    descriptor = None
    for klass in education_School.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_education_school_has_name():
    assert hasattr(education_School, "name")
    descriptor = None
    for klass in education_School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_education_school_has_phone():
    assert hasattr(education_School, "phone")
    descriptor = None
    for klass in education_School.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
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
education_Course_strategy = st.builds(
    education_Course,
    name=
        safe_text
)
education_Student_strategy = st.builds(
    education_Student,
    name=
        safe_text
)
education_School_strategy = st.builds(
    education_School,
    address=
        safe_text,
    name=
        safe_text,
    phone=
        safe_text
)

@given(instance=education_Course_strategy)
@settings(max_examples=50)
def test_education_course_instantiation(instance):
    assert isinstance(instance, education_Course)



@given(instance=education_Course_strategy)
def test_education_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=education_Student_strategy)
@settings(max_examples=50)
def test_education_student_instantiation(instance):
    assert isinstance(instance, education_Student)



@given(instance=education_Student_strategy)
def test_education_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=education_School_strategy)
@settings(max_examples=50)
def test_education_school_instantiation(instance):
    assert isinstance(instance, education_School)



@given(instance=education_School_strategy)
def test_education_school_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=education_School_strategy)
def test_education_school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=education_School_strategy)
def test_education_school_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original
