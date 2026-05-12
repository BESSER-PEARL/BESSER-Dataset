import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    university_Student,
    university_Course,
    university_University,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_university_student_is_not_abstract():
    assert not inspect.isabstract(university_Student)


def test_university_student_constructor_exists():
    assert callable(university_Student.__init__)


def test_university_student_constructor_args():
    sig = inspect.signature(university_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_university_student_has_name():
    assert hasattr(university_Student, "name")
    descriptor = None
    for klass in university_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_university_student_has_id():
    assert hasattr(university_Student, "id")
    descriptor = None
    for klass in university_Student.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_university_course_is_not_abstract():
    assert not inspect.isabstract(university_Course)


def test_university_course_constructor_exists():
    assert callable(university_Course.__init__)


def test_university_course_constructor_args():
    sig = inspect.signature(university_Course.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_university_course_has_id():
    assert hasattr(university_Course, "id")
    descriptor = None
    for klass in university_Course.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_university_course_has_name():
    assert hasattr(university_Course, "name")
    descriptor = None
    for klass in university_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university_university_is_not_abstract():
    assert not inspect.isabstract(university_University)


def test_university_university_constructor_exists():
    assert callable(university_University.__init__)


def test_university_university_constructor_args():
    sig = inspect.signature(university_University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_university_university_has_name():
    assert hasattr(university_University, "name")
    descriptor = None
    for klass in university_University.__mro__:
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
university_Student_strategy = st.builds(
    university_Student,
    name=
        safe_text,
    id=
        safe_text
)
university_Course_strategy = st.builds(
    university_Course,
    id=
        safe_text,
    name=
        safe_text
)
university_University_strategy = st.builds(
    university_University,
    name=
        safe_text
)

@given(instance=university_Student_strategy)
@settings(max_examples=50)
def test_university_student_instantiation(instance):
    assert isinstance(instance, university_Student)



@given(instance=university_Student_strategy)
def test_university_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=university_Student_strategy)
def test_university_student_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=university_Course_strategy)
@settings(max_examples=50)
def test_university_course_instantiation(instance):
    assert isinstance(instance, university_Course)



@given(instance=university_Course_strategy)
def test_university_course_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=university_Course_strategy)
def test_university_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university_University_strategy)
@settings(max_examples=50)
def test_university_university_instantiation(instance):
    assert isinstance(instance, university_University)



@given(instance=university_University_strategy)
def test_university_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
