import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    university_Student,
    university_University,
    university_Certificate,
    university_Professor,
    university_Course,
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
    assert "semester" in params, "Missing parameter 'semester'"
    assert "MNR" in params, "Missing parameter 'MNR'"

def test_university_student_has_semester():
    assert hasattr(university_Student, "semester")
    descriptor = None
    for klass in university_Student.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
            break
    assert isinstance(descriptor, property)

def test_university_student_has_MNR():
    assert hasattr(university_Student, "MNR")
    descriptor = None
    for klass in university_Student.__mro__:
        if "MNR" in klass.__dict__:
            descriptor = klass.__dict__["MNR"]
            break
    assert isinstance(descriptor, property)



def test_university_university_is_not_abstract():
    assert not inspect.isabstract(university_University)


def test_university_university_constructor_exists():
    assert callable(university_University.__init__)


def test_university_university_constructor_args():
    sig = inspect.signature(university_University.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfStudents" in params, "Missing parameter 'numberOfStudents'"
    assert "averageLength" in params, "Missing parameter 'averageLength'"
    assert "name" in params, "Missing parameter 'name'"

def test_university_university_has_numberOfStudents():
    assert hasattr(university_University, "numberOfStudents")
    descriptor = None
    for klass in university_University.__mro__:
        if "numberOfStudents" in klass.__dict__:
            descriptor = klass.__dict__["numberOfStudents"]
            break
    assert isinstance(descriptor, property)

def test_university_university_has_averageLength():
    assert hasattr(university_University, "averageLength")
    descriptor = None
    for klass in university_University.__mro__:
        if "averageLength" in klass.__dict__:
            descriptor = klass.__dict__["averageLength"]
            break
    assert isinstance(descriptor, property)

def test_university_university_has_name():
    assert hasattr(university_University, "name")
    descriptor = None
    for klass in university_University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university_certificate_is_not_abstract():
    assert not inspect.isabstract(university_Certificate)


def test_university_certificate_constructor_exists():
    assert callable(university_Certificate.__init__)


def test_university_certificate_constructor_args():
    sig = inspect.signature(university_Certificate.__init__)
    params = list(sig.parameters.keys())
    assert "note" in params, "Missing parameter 'note'"

def test_university_certificate_has_note():
    assert hasattr(university_Certificate, "note")
    descriptor = None
    for klass in university_Certificate.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_university_professor_is_not_abstract():
    assert not inspect.isabstract(university_Professor)


def test_university_professor_constructor_exists():
    assert callable(university_Professor.__init__)


def test_university_professor_constructor_args():
    sig = inspect.signature(university_Professor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_university_professor_has_name():
    assert hasattr(university_Professor, "name")
    descriptor = None
    for klass in university_Professor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university_course_is_not_abstract():
    assert not inspect.isabstract(university_Course)


def test_university_course_constructor_exists():
    assert callable(university_Course.__init__)


def test_university_course_constructor_args():
    sig = inspect.signature(university_Course.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfAttendants" in params, "Missing parameter 'numberOfAttendants'"
    assert "name" in params, "Missing parameter 'name'"
    assert "gradeAverage" in params, "Missing parameter 'gradeAverage'"

def test_university_course_has_numberOfAttendants():
    assert hasattr(university_Course, "numberOfAttendants")
    descriptor = None
    for klass in university_Course.__mro__:
        if "numberOfAttendants" in klass.__dict__:
            descriptor = klass.__dict__["numberOfAttendants"]
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

def test_university_course_has_gradeAverage():
    assert hasattr(university_Course, "gradeAverage")
    descriptor = None
    for klass in university_Course.__mro__:
        if "gradeAverage" in klass.__dict__:
            descriptor = klass.__dict__["gradeAverage"]
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
    semester=
        st.integers(),
    MNR=
        safe_text
)
university_University_strategy = st.builds(
    university_University,
    numberOfStudents=
        st.integers(),
    averageLength=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
university_Certificate_strategy = st.builds(
    university_Certificate,
    note=
        st.integers()
)
university_Professor_strategy = st.builds(
    university_Professor,
    name=
        safe_text
)
university_Course_strategy = st.builds(
    university_Course,
    numberOfAttendants=
        st.integers(),
    name=
        safe_text,
    gradeAverage=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=university_Student_strategy)
@settings(max_examples=50)
def test_university_student_instantiation(instance):
    assert isinstance(instance, university_Student)



@given(instance=university_Student_strategy)
def test_university_student_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original



@given(instance=university_Student_strategy)
def test_university_student_MNR_setter(instance):
    original = instance.MNR
    instance.MNR = original
    assert instance.MNR == original

@given(instance=university_University_strategy)
@settings(max_examples=50)
def test_university_university_instantiation(instance):
    assert isinstance(instance, university_University)



@given(instance=university_University_strategy)
def test_university_university_numberOfStudents_setter(instance):
    original = instance.numberOfStudents
    instance.numberOfStudents = original
    assert instance.numberOfStudents == original



@given(instance=university_University_strategy)
def test_university_university_averageLength_setter(instance):
    original = instance.averageLength
    instance.averageLength = original
    assert instance.averageLength == original



@given(instance=university_University_strategy)
def test_university_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university_Certificate_strategy)
@settings(max_examples=50)
def test_university_certificate_instantiation(instance):
    assert isinstance(instance, university_Certificate)



@given(instance=university_Certificate_strategy)
def test_university_certificate_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=university_Professor_strategy)
@settings(max_examples=50)
def test_university_professor_instantiation(instance):
    assert isinstance(instance, university_Professor)



@given(instance=university_Professor_strategy)
def test_university_professor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university_Course_strategy)
@settings(max_examples=50)
def test_university_course_instantiation(instance):
    assert isinstance(instance, university_Course)



@given(instance=university_Course_strategy)
def test_university_course_numberOfAttendants_setter(instance):
    original = instance.numberOfAttendants
    instance.numberOfAttendants = original
    assert instance.numberOfAttendants == original



@given(instance=university_Course_strategy)
def test_university_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=university_Course_strategy)
def test_university_course_gradeAverage_setter(instance):
    original = instance.gradeAverage
    instance.gradeAverage = original
    assert instance.gradeAverage == original
