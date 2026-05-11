import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    university::Student,
    university::University,
    university::Certificate,
    university::Professor,
    university::Course,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_university::student_is_not_abstract():
    assert not inspect.isabstract(university::Student)


def test_university::student_constructor_exists():
    assert callable(university::Student.__init__)


def test_university::student_constructor_args():
    sig = inspect.signature(university::Student.__init__)
    params = list(sig.parameters.keys())
    assert "semester" in params, "Missing parameter 'semester'"
    assert "MNR" in params, "Missing parameter 'MNR'"

def test_university::student_has_semester():
    assert hasattr(university::Student, "semester")
    descriptor = None
    for klass in university::Student.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
            break
    assert isinstance(descriptor, property)

def test_university::student_has_MNR():
    assert hasattr(university::Student, "MNR")
    descriptor = None
    for klass in university::Student.__mro__:
        if "MNR" in klass.__dict__:
            descriptor = klass.__dict__["MNR"]
            break
    assert isinstance(descriptor, property)



def test_university::university_is_not_abstract():
    assert not inspect.isabstract(university::University)


def test_university::university_constructor_exists():
    assert callable(university::University.__init__)


def test_university::university_constructor_args():
    sig = inspect.signature(university::University.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfStudents" in params, "Missing parameter 'numberOfStudents'"
    assert "name" in params, "Missing parameter 'name'"
    assert "averageLength" in params, "Missing parameter 'averageLength'"

def test_university::university_has_numberOfStudents():
    assert hasattr(university::University, "numberOfStudents")
    descriptor = None
    for klass in university::University.__mro__:
        if "numberOfStudents" in klass.__dict__:
            descriptor = klass.__dict__["numberOfStudents"]
            break
    assert isinstance(descriptor, property)

def test_university::university_has_name():
    assert hasattr(university::University, "name")
    descriptor = None
    for klass in university::University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_university::university_has_averageLength():
    assert hasattr(university::University, "averageLength")
    descriptor = None
    for klass in university::University.__mro__:
        if "averageLength" in klass.__dict__:
            descriptor = klass.__dict__["averageLength"]
            break
    assert isinstance(descriptor, property)



def test_university::certificate_is_not_abstract():
    assert not inspect.isabstract(university::Certificate)


def test_university::certificate_constructor_exists():
    assert callable(university::Certificate.__init__)


def test_university::certificate_constructor_args():
    sig = inspect.signature(university::Certificate.__init__)
    params = list(sig.parameters.keys())
    assert "note" in params, "Missing parameter 'note'"

def test_university::certificate_has_note():
    assert hasattr(university::Certificate, "note")
    descriptor = None
    for klass in university::Certificate.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_university::professor_is_not_abstract():
    assert not inspect.isabstract(university::Professor)


def test_university::professor_constructor_exists():
    assert callable(university::Professor.__init__)


def test_university::professor_constructor_args():
    sig = inspect.signature(university::Professor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_university::professor_has_name():
    assert hasattr(university::Professor, "name")
    descriptor = None
    for klass in university::Professor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university::course_is_not_abstract():
    assert not inspect.isabstract(university::Course)


def test_university::course_constructor_exists():
    assert callable(university::Course.__init__)


def test_university::course_constructor_args():
    sig = inspect.signature(university::Course.__init__)
    params = list(sig.parameters.keys())
    assert "gradeAverage" in params, "Missing parameter 'gradeAverage'"
    assert "name" in params, "Missing parameter 'name'"
    assert "numberOfAttendants" in params, "Missing parameter 'numberOfAttendants'"

def test_university::course_has_gradeAverage():
    assert hasattr(university::Course, "gradeAverage")
    descriptor = None
    for klass in university::Course.__mro__:
        if "gradeAverage" in klass.__dict__:
            descriptor = klass.__dict__["gradeAverage"]
            break
    assert isinstance(descriptor, property)

def test_university::course_has_name():
    assert hasattr(university::Course, "name")
    descriptor = None
    for klass in university::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_university::course_has_numberOfAttendants():
    assert hasattr(university::Course, "numberOfAttendants")
    descriptor = None
    for klass in university::Course.__mro__:
        if "numberOfAttendants" in klass.__dict__:
            descriptor = klass.__dict__["numberOfAttendants"]
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
university::Student_strategy = st.builds(
    university::Student,
    semester=
        st.integers(),
    MNR=
        safe_text
)
university::University_strategy = st.builds(
    university::University,
    numberOfStudents=
        st.integers(),
    name=
        safe_text,
    averageLength=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
university::Certificate_strategy = st.builds(
    university::Certificate,
    note=
        st.integers()
)
university::Professor_strategy = st.builds(
    university::Professor,
    name=
        safe_text
)
university::Course_strategy = st.builds(
    university::Course,
    gradeAverage=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    numberOfAttendants=
        st.integers()
)

@given(instance=university::Student_strategy)
@settings(max_examples=50)
def test_university::student_instantiation(instance):
    assert isinstance(instance, university::Student)

@given(instance=university::Student_strategy)
def test_university::student_semester_type(instance):
    assert isinstance(instance.semester, int)


@given(instance=university::Student_strategy)
def test_university::student_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original

@given(instance=university::Student_strategy)
def test_university::student_MNR_type(instance):
    assert isinstance(instance.MNR, str)


@given(instance=university::Student_strategy)
def test_university::student_MNR_setter(instance):
    original = instance.MNR
    instance.MNR = original
    assert instance.MNR == original

@given(instance=university::University_strategy)
@settings(max_examples=50)
def test_university::university_instantiation(instance):
    assert isinstance(instance, university::University)

@given(instance=university::University_strategy)
def test_university::university_numberOfStudents_type(instance):
    assert isinstance(instance.numberOfStudents, int)


@given(instance=university::University_strategy)
def test_university::university_numberOfStudents_setter(instance):
    original = instance.numberOfStudents
    instance.numberOfStudents = original
    assert instance.numberOfStudents == original

@given(instance=university::University_strategy)
def test_university::university_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=university::University_strategy)
def test_university::university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university::University_strategy)
def test_university::university_averageLength_type(instance):
    assert isinstance(instance.averageLength, float)


@given(instance=university::University_strategy)
def test_university::university_averageLength_setter(instance):
    original = instance.averageLength
    instance.averageLength = original
    assert instance.averageLength == original

@given(instance=university::Certificate_strategy)
@settings(max_examples=50)
def test_university::certificate_instantiation(instance):
    assert isinstance(instance, university::Certificate)

@given(instance=university::Certificate_strategy)
def test_university::certificate_note_type(instance):
    assert isinstance(instance.note, int)


@given(instance=university::Certificate_strategy)
def test_university::certificate_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=university::Professor_strategy)
@settings(max_examples=50)
def test_university::professor_instantiation(instance):
    assert isinstance(instance, university::Professor)

@given(instance=university::Professor_strategy)
def test_university::professor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=university::Professor_strategy)
def test_university::professor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university::Course_strategy)
@settings(max_examples=50)
def test_university::course_instantiation(instance):
    assert isinstance(instance, university::Course)

@given(instance=university::Course_strategy)
def test_university::course_gradeAverage_type(instance):
    assert isinstance(instance.gradeAverage, float)


@given(instance=university::Course_strategy)
def test_university::course_gradeAverage_setter(instance):
    original = instance.gradeAverage
    instance.gradeAverage = original
    assert instance.gradeAverage == original

@given(instance=university::Course_strategy)
def test_university::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=university::Course_strategy)
def test_university::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university::Course_strategy)
def test_university::course_numberOfAttendants_type(instance):
    assert isinstance(instance.numberOfAttendants, int)


@given(instance=university::Course_strategy)
def test_university::course_numberOfAttendants_setter(instance):
    original = instance.numberOfAttendants
    instance.numberOfAttendants = original
    assert instance.numberOfAttendants == original
