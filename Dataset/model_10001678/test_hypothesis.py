import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Schedule,
    Note,
    Subject,
    Grade,
    Teacher,
    Student,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_schedule_is_not_abstract():
    assert not inspect.isabstract(Schedule)


def test_schedule_constructor_exists():
    assert callable(Schedule.__init__)


def test_schedule_constructor_args():
    sig = inspect.signature(Schedule.__init__)
    params = list(sig.parameters.keys())



def test_note_is_not_abstract():
    assert not inspect.isabstract(Note)


def test_note_constructor_exists():
    assert callable(Note.__init__)


def test_note_constructor_args():
    sig = inspect.signature(Note.__init__)
    params = list(sig.parameters.keys())



def test_subject_is_not_abstract():
    assert not inspect.isabstract(Subject)


def test_subject_constructor_exists():
    assert callable(Subject.__init__)


def test_subject_constructor_args():
    sig = inspect.signature(Subject.__init__)
    params = list(sig.parameters.keys())



def test_grade_is_not_abstract():
    assert not inspect.isabstract(Grade)


def test_grade_constructor_exists():
    assert callable(Grade.__init__)


def test_grade_constructor_args():
    sig = inspect.signature(Grade.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_grade_has_name():
    assert hasattr(Grade, "name")
    descriptor = None
    for klass in Grade.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_teacher_is_not_abstract():
    assert not inspect.isabstract(Teacher)


def test_teacher_constructor_exists():
    assert callable(Teacher.__init__)


def test_teacher_constructor_args():
    sig = inspect.signature(Teacher.__init__)
    params = list(sig.parameters.keys())
    assert "phone" in params, "Missing parameter 'phone'"
    assert "name" in params, "Missing parameter 'name'"
    assert "email" in params, "Missing parameter 'email'"
    assert "surname" in params, "Missing parameter 'surname'"

def test_teacher_has_phone():
    assert hasattr(Teacher, "phone")
    descriptor = None
    for klass in Teacher.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_teacher_has_name():
    assert hasattr(Teacher, "name")
    descriptor = None
    for klass in Teacher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_teacher_has_email():
    assert hasattr(Teacher, "email")
    descriptor = None
    for klass in Teacher.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_teacher_has_surname():
    assert hasattr(Teacher, "surname")
    descriptor = None
    for klass in Teacher.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)



def test_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_student_constructor_exists():
    assert callable(Student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "surname" in params, "Missing parameter 'surname'"
    assert "email" in params, "Missing parameter 'email'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "name" in params, "Missing parameter 'name'"

def test_student_has_surname():
    assert hasattr(Student, "surname")
    descriptor = None
    for klass in Student.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)

def test_student_has_email():
    assert hasattr(Student, "email")
    descriptor = None
    for klass in Student.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_student_has_phone():
    assert hasattr(Student, "phone")
    descriptor = None
    for klass in Student.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_student_has_name():
    assert hasattr(Student, "name")
    descriptor = None
    for klass in Student.__mro__:
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
Schedule_strategy = st.builds(
    Schedule,
)
Note_strategy = st.builds(
    Note,
)
Subject_strategy = st.builds(
    Subject,
)
Grade_strategy = st.builds(
    Grade,
    name=
        safe_text
)
Teacher_strategy = st.builds(
    Teacher,
    phone=
        safe_text,
    name=
        safe_text,
    email=
        safe_text,
    surname=
        safe_text
)
Student_strategy = st.builds(
    Student,
    surname=
        safe_text,
    email=
        safe_text,
    phone=
        safe_text,
    name=
        safe_text
)

@given(instance=Schedule_strategy)
@settings(max_examples=50)
def test_schedule_instantiation(instance):
    assert isinstance(instance, Schedule)

@given(instance=Note_strategy)
@settings(max_examples=50)
def test_note_instantiation(instance):
    assert isinstance(instance, Note)

@given(instance=Subject_strategy)
@settings(max_examples=50)
def test_subject_instantiation(instance):
    assert isinstance(instance, Subject)

@given(instance=Grade_strategy)
@settings(max_examples=50)
def test_grade_instantiation(instance):
    assert isinstance(instance, Grade)



@given(instance=Grade_strategy)
def test_grade_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Teacher_strategy)
@settings(max_examples=50)
def test_teacher_instantiation(instance):
    assert isinstance(instance, Teacher)



@given(instance=Teacher_strategy)
def test_teacher_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Teacher_strategy)
def test_teacher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Teacher_strategy)
def test_teacher_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Teacher_strategy)
def test_teacher_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, Student)



@given(instance=Student_strategy)
def test_student_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original



@given(instance=Student_strategy)
def test_student_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Student_strategy)
def test_student_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Student_strategy)
def test_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
