import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    edu_Take_Course,
    edu_Student,
    edu_Course,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_edu_take_course_is_not_abstract():
    assert not inspect.isabstract(edu_Take_Course)


def test_edu_take_course_constructor_exists():
    assert callable(edu_Take_Course.__init__)


def test_edu_take_course_constructor_args():
    sig = inspect.signature(edu_Take_Course.__init__)
    params = list(sig.parameters.keys())



def test_edu_student_is_not_abstract():
    assert not inspect.isabstract(edu_Student)


def test_edu_student_constructor_exists():
    assert callable(edu_Student.__init__)


def test_edu_student_constructor_args():
    sig = inspect.signature(edu_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "date_of_birth" in params, "Missing parameter 'date_of_birth'"

def test_edu_student_has_name():
    assert hasattr(edu_Student, "name")
    descriptor = None
    for klass in edu_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_edu_student_has_id():
    assert hasattr(edu_Student, "id")
    descriptor = None
    for klass in edu_Student.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_edu_student_has_date_of_birth():
    assert hasattr(edu_Student, "date_of_birth")
    descriptor = None
    for klass in edu_Student.__mro__:
        if "date_of_birth" in klass.__dict__:
            descriptor = klass.__dict__["date_of_birth"]
            break
    assert isinstance(descriptor, property)



def test_edu_course_is_not_abstract():
    assert not inspect.isabstract(edu_Course)


def test_edu_course_constructor_exists():
    assert callable(edu_Course.__init__)


def test_edu_course_constructor_args():
    sig = inspect.signature(edu_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_edu_course_has_name():
    assert hasattr(edu_Course, "name")
    descriptor = None
    for klass in edu_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_edu_course_has_id():
    assert hasattr(edu_Course, "id")
    descriptor = None
    for klass in edu_Course.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
edu_Take_Course_strategy = st.builds(
    edu_Take_Course,
)
edu_Student_strategy = st.builds(
    edu_Student,
    name=
        safe_text,
    id=
        st.integers(),
    date_of_birth=
        st.dates()
)
edu_Course_strategy = st.builds(
    edu_Course,
    name=
        safe_text,
    id=
        st.integers()
)

@given(instance=edu_Take_Course_strategy)
@settings(max_examples=50)
def test_edu_take_course_instantiation(instance):
    assert isinstance(instance, edu_Take_Course)

@given(instance=edu_Student_strategy)
@settings(max_examples=50)
def test_edu_student_instantiation(instance):
    assert isinstance(instance, edu_Student)



@given(instance=edu_Student_strategy)
def test_edu_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=edu_Student_strategy)
def test_edu_student_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=edu_Student_strategy)
def test_edu_student_date_of_birth_setter(instance):
    original = instance.date_of_birth
    instance.date_of_birth = original
    assert instance.date_of_birth == original

@given(instance=edu_Course_strategy)
@settings(max_examples=50)
def test_edu_course_instantiation(instance):
    assert isinstance(instance, edu_Course)



@given(instance=edu_Course_strategy)
def test_edu_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=edu_Course_strategy)
def test_edu_course_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
