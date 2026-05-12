import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    leftOuts,
    constraints,
    conflictCheck,
    classrooms,
    subjects,
    teachers,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_leftouts_is_not_abstract():
    assert not inspect.isabstract(leftOuts)


def test_leftouts_constructor_exists():
    assert callable(leftOuts.__init__)


def test_leftouts_constructor_args():
    sig = inspect.signature(leftOuts.__init__)
    params = list(sig.parameters.keys())
    assert "subject" in params, "Missing parameter 'subject'"
    assert "students" in params, "Missing parameter 'students'"
    assert "classroom" in params, "Missing parameter 'classroom'"
    assert "teachers" in params, "Missing parameter 'teachers'"

def test_leftouts_has_subject():
    assert hasattr(leftOuts, "subject")
    descriptor = None
    for klass in leftOuts.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_leftouts_has_students():
    assert hasattr(leftOuts, "students")
    descriptor = None
    for klass in leftOuts.__mro__:
        if "students" in klass.__dict__:
            descriptor = klass.__dict__["students"]
            break
    assert isinstance(descriptor, property)

def test_leftouts_has_classroom():
    assert hasattr(leftOuts, "classroom")
    descriptor = None
    for klass in leftOuts.__mro__:
        if "classroom" in klass.__dict__:
            descriptor = klass.__dict__["classroom"]
            break
    assert isinstance(descriptor, property)

def test_leftouts_has_teachers():
    assert hasattr(leftOuts, "teachers")
    descriptor = None
    for klass in leftOuts.__mro__:
        if "teachers" in klass.__dict__:
            descriptor = klass.__dict__["teachers"]
            break
    assert isinstance(descriptor, property)



def test_constraints_is_not_abstract():
    assert not inspect.isabstract(constraints)


def test_constraints_constructor_exists():
    assert callable(constraints.__init__)


def test_constraints_constructor_args():
    sig = inspect.signature(constraints.__init__)
    params = list(sig.parameters.keys())
    assert "doubletons" in params, "Missing parameter 'doubletons'"
    assert "singletons" in params, "Missing parameter 'singletons'"

def test_constraints_has_doubletons():
    assert hasattr(constraints, "doubletons")
    descriptor = None
    for klass in constraints.__mro__:
        if "doubletons" in klass.__dict__:
            descriptor = klass.__dict__["doubletons"]
            break
    assert isinstance(descriptor, property)

def test_constraints_has_singletons():
    assert hasattr(constraints, "singletons")
    descriptor = None
    for klass in constraints.__mro__:
        if "singletons" in klass.__dict__:
            descriptor = klass.__dict__["singletons"]
            break
    assert isinstance(descriptor, property)



def test_conflictcheck_is_not_abstract():
    assert not inspect.isabstract(conflictCheck)


def test_conflictcheck_constructor_exists():
    assert callable(conflictCheck.__init__)


def test_conflictcheck_constructor_args():
    sig = inspect.signature(conflictCheck.__init__)
    params = list(sig.parameters.keys())
    assert "subjects" in params, "Missing parameter 'subjects'"
    assert "conflict" in params, "Missing parameter 'conflict'"

def test_conflictcheck_has_subjects():
    assert hasattr(conflictCheck, "subjects")
    descriptor = None
    for klass in conflictCheck.__mro__:
        if "subjects" in klass.__dict__:
            descriptor = klass.__dict__["subjects"]
            break
    assert isinstance(descriptor, property)

def test_conflictcheck_has_conflict():
    assert hasattr(conflictCheck, "conflict")
    descriptor = None
    for klass in conflictCheck.__mro__:
        if "conflict" in klass.__dict__:
            descriptor = klass.__dict__["conflict"]
            break
    assert isinstance(descriptor, property)



def test_classrooms_is_not_abstract():
    assert not inspect.isabstract(classrooms)


def test_classrooms_constructor_exists():
    assert callable(classrooms.__init__)


def test_classrooms_constructor_args():
    sig = inspect.signature(classrooms.__init__)
    params = list(sig.parameters.keys())
    assert "subject" in params, "Missing parameter 'subject'"
    assert "teacher" in params, "Missing parameter 'teacher'"
    assert "number" in params, "Missing parameter 'number'"

def test_classrooms_has_subject():
    assert hasattr(classrooms, "subject")
    descriptor = None
    for klass in classrooms.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_classrooms_has_teacher():
    assert hasattr(classrooms, "teacher")
    descriptor = None
    for klass in classrooms.__mro__:
        if "teacher" in klass.__dict__:
            descriptor = klass.__dict__["teacher"]
            break
    assert isinstance(descriptor, property)

def test_classrooms_has_number():
    assert hasattr(classrooms, "number")
    descriptor = None
    for klass in classrooms.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_subjects_is_not_abstract():
    assert not inspect.isabstract(subjects)


def test_subjects_constructor_exists():
    assert callable(subjects.__init__)


def test_subjects_constructor_args():
    sig = inspect.signature(subjects.__init__)
    params = list(sig.parameters.keys())
    assert "classroom" in params, "Missing parameter 'classroom'"
    assert "teacher" in params, "Missing parameter 'teacher'"
    assert "Section" in params, "Missing parameter 'Section'"
    assert "name" in params, "Missing parameter 'name'"

def test_subjects_has_classroom():
    assert hasattr(subjects, "classroom")
    descriptor = None
    for klass in subjects.__mro__:
        if "classroom" in klass.__dict__:
            descriptor = klass.__dict__["classroom"]
            break
    assert isinstance(descriptor, property)

def test_subjects_has_teacher():
    assert hasattr(subjects, "teacher")
    descriptor = None
    for klass in subjects.__mro__:
        if "teacher" in klass.__dict__:
            descriptor = klass.__dict__["teacher"]
            break
    assert isinstance(descriptor, property)

def test_subjects_has_Section():
    assert hasattr(subjects, "Section")
    descriptor = None
    for klass in subjects.__mro__:
        if "Section" in klass.__dict__:
            descriptor = klass.__dict__["Section"]
            break
    assert isinstance(descriptor, property)

def test_subjects_has_name():
    assert hasattr(subjects, "name")
    descriptor = None
    for klass in subjects.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_teachers_is_not_abstract():
    assert not inspect.isabstract(teachers)


def test_teachers_constructor_exists():
    assert callable(teachers.__init__)


def test_teachers_constructor_args():
    sig = inspect.signature(teachers.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "section" in params, "Missing parameter 'section'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "classroom" in params, "Missing parameter 'classroom'"

def test_teachers_has_name():
    assert hasattr(teachers, "name")
    descriptor = None
    for klass in teachers.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_teachers_has_section():
    assert hasattr(teachers, "section")
    descriptor = None
    for klass in teachers.__mro__:
        if "section" in klass.__dict__:
            descriptor = klass.__dict__["section"]
            break
    assert isinstance(descriptor, property)

def test_teachers_has_subject():
    assert hasattr(teachers, "subject")
    descriptor = None
    for klass in teachers.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_teachers_has_classroom():
    assert hasattr(teachers, "classroom")
    descriptor = None
    for klass in teachers.__mro__:
        if "classroom" in klass.__dict__:
            descriptor = klass.__dict__["classroom"]
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
leftOuts_strategy = st.builds(
    leftOuts,
    subject=
        st.none(),
    students=
        safe_text,
    classroom=
        st.none(),
    teachers=
        st.none()
)
constraints_strategy = st.builds(
    constraints,
    doubletons=
        st.none(),
    singletons=
        st.none()
)
conflictCheck_strategy = st.builds(
    conflictCheck,
    subjects=
        safe_text,
    conflict=
        st.booleans()
)
classrooms_strategy = st.builds(
    classrooms,
    subject=
        safe_text,
    teacher=
        safe_text,
    number=
        st.integers()
)
subjects_strategy = st.builds(
    subjects,
    classroom=
        st.integers(),
    teacher=
        safe_text,
    Section=
        safe_text,
    name=
        safe_text
)
teachers_strategy = st.builds(
    teachers,
    name=
        safe_text,
    section=
        safe_text,
    subject=
        safe_text,
    classroom=
        st.integers()
)

@given(instance=leftOuts_strategy)
@settings(max_examples=50)
def test_leftouts_instantiation(instance):
    assert isinstance(instance, leftOuts)



@given(instance=leftOuts_strategy)
def test_leftouts_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=leftOuts_strategy)
def test_leftouts_students_setter(instance):
    original = instance.students
    instance.students = original
    assert instance.students == original



@given(instance=leftOuts_strategy)
def test_leftouts_classroom_setter(instance):
    original = instance.classroom
    instance.classroom = original
    assert instance.classroom == original



@given(instance=leftOuts_strategy)
def test_leftouts_teachers_setter(instance):
    original = instance.teachers
    instance.teachers = original
    assert instance.teachers == original

@given(instance=constraints_strategy)
@settings(max_examples=50)
def test_constraints_instantiation(instance):
    assert isinstance(instance, constraints)



@given(instance=constraints_strategy)
def test_constraints_doubletons_setter(instance):
    original = instance.doubletons
    instance.doubletons = original
    assert instance.doubletons == original



@given(instance=constraints_strategy)
def test_constraints_singletons_setter(instance):
    original = instance.singletons
    instance.singletons = original
    assert instance.singletons == original

@given(instance=conflictCheck_strategy)
@settings(max_examples=50)
def test_conflictcheck_instantiation(instance):
    assert isinstance(instance, conflictCheck)



@given(instance=conflictCheck_strategy)
def test_conflictcheck_subjects_setter(instance):
    original = instance.subjects
    instance.subjects = original
    assert instance.subjects == original



@given(instance=conflictCheck_strategy)
def test_conflictcheck_conflict_setter(instance):
    original = instance.conflict
    instance.conflict = original
    assert instance.conflict == original

@given(instance=classrooms_strategy)
@settings(max_examples=50)
def test_classrooms_instantiation(instance):
    assert isinstance(instance, classrooms)



@given(instance=classrooms_strategy)
def test_classrooms_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=classrooms_strategy)
def test_classrooms_teacher_setter(instance):
    original = instance.teacher
    instance.teacher = original
    assert instance.teacher == original



@given(instance=classrooms_strategy)
def test_classrooms_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=subjects_strategy)
@settings(max_examples=50)
def test_subjects_instantiation(instance):
    assert isinstance(instance, subjects)



@given(instance=subjects_strategy)
def test_subjects_classroom_setter(instance):
    original = instance.classroom
    instance.classroom = original
    assert instance.classroom == original



@given(instance=subjects_strategy)
def test_subjects_teacher_setter(instance):
    original = instance.teacher
    instance.teacher = original
    assert instance.teacher == original



@given(instance=subjects_strategy)
def test_subjects_Section_setter(instance):
    original = instance.Section
    instance.Section = original
    assert instance.Section == original



@given(instance=subjects_strategy)
def test_subjects_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=teachers_strategy)
@settings(max_examples=50)
def test_teachers_instantiation(instance):
    assert isinstance(instance, teachers)



@given(instance=teachers_strategy)
def test_teachers_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=teachers_strategy)
def test_teachers_section_setter(instance):
    original = instance.section
    instance.section = original
    assert instance.section == original



@given(instance=teachers_strategy)
def test_teachers_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=teachers_strategy)
def test_teachers_classroom_setter(instance):
    original = instance.classroom
    instance.classroom = original
    assert instance.classroom == original
