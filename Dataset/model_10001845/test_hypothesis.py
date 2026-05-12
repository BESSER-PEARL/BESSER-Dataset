import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    exam,
    subject,
    claas1,
    student,
    teachers,
    admin,
    user,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_exam_is_not_abstract():
    assert not inspect.isabstract(exam)


def test_exam_constructor_exists():
    assert callable(exam.__init__)


def test_exam_constructor_args():
    sig = inspect.signature(exam.__init__)
    params = list(sig.parameters.keys())



def test_subject_is_not_abstract():
    assert not inspect.isabstract(subject)


def test_subject_constructor_exists():
    assert callable(subject.__init__)


def test_subject_constructor_args():
    sig = inspect.signature(subject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_subject_has_id():
    assert hasattr(subject, "id")
    descriptor = None
    for klass in subject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_subject_has_name():
    assert hasattr(subject, "name")
    descriptor = None
    for klass in subject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_claas1_is_not_abstract():
    assert not inspect.isabstract(claas1)


def test_claas1_constructor_exists():
    assert callable(claas1.__init__)


def test_claas1_constructor_args():
    sig = inspect.signature(claas1.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_claas1_has_id():
    assert hasattr(claas1, "id")
    descriptor = None
    for klass in claas1.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_claas1_has_name():
    assert hasattr(claas1, "name")
    descriptor = None
    for klass in claas1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_student_is_not_abstract():
    assert not inspect.isabstract(student)


def test_student_constructor_exists():
    assert callable(student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(student.__init__)
    params = list(sig.parameters.keys())



def test_teachers_is_not_abstract():
    assert not inspect.isabstract(teachers)


def test_teachers_constructor_exists():
    assert callable(teachers.__init__)


def test_teachers_constructor_args():
    sig = inspect.signature(teachers.__init__)
    params = list(sig.parameters.keys())



def test_admin_is_not_abstract():
    assert not inspect.isabstract(admin)


def test_admin_constructor_exists():
    assert callable(admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(admin.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(user)


def test_user_constructor_exists():
    assert callable(user.__init__)


def test_user_constructor_args():
    sig = inspect.signature(user.__init__)
    params = list(sig.parameters.keys())
    assert "pas" in params, "Missing parameter 'pas'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "user_name" in params, "Missing parameter 'user_name'"

def test_user_has_pas():
    assert hasattr(user, "pas")
    descriptor = None
    for klass in user.__mro__:
        if "pas" in klass.__dict__:
            descriptor = klass.__dict__["pas"]
            break
    assert isinstance(descriptor, property)

def test_user_has_sex():
    assert hasattr(user, "sex")
    descriptor = None
    for klass in user.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)

def test_user_has_user_name():
    assert hasattr(user, "user_name")
    descriptor = None
    for klass in user.__mro__:
        if "user_name" in klass.__dict__:
            descriptor = klass.__dict__["user_name"]
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
exam_strategy = st.builds(
    exam,
)
subject_strategy = st.builds(
    subject,
    id=
        st.integers(),
    name=
        safe_text
)
claas1_strategy = st.builds(
    claas1,
    id=
        st.integers(),
    name=
        safe_text
)
student_strategy = st.builds(
    student,
)
teachers_strategy = st.builds(
    teachers,
)
admin_strategy = st.builds(
    admin,
)
user_strategy = st.builds(
    user,
    pas=
        safe_text,
    sex=
        safe_text,
    user_name=
        safe_text
)

@given(instance=exam_strategy)
@settings(max_examples=50)
def test_exam_instantiation(instance):
    assert isinstance(instance, exam)

@given(instance=subject_strategy)
@settings(max_examples=50)
def test_subject_instantiation(instance):
    assert isinstance(instance, subject)



@given(instance=subject_strategy)
def test_subject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=subject_strategy)
def test_subject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=claas1_strategy)
@settings(max_examples=50)
def test_claas1_instantiation(instance):
    assert isinstance(instance, claas1)



@given(instance=claas1_strategy)
def test_claas1_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=claas1_strategy)
def test_claas1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, student)

@given(instance=teachers_strategy)
@settings(max_examples=50)
def test_teachers_instantiation(instance):
    assert isinstance(instance, teachers)

@given(instance=admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, admin)

@given(instance=user_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, user)



@given(instance=user_strategy)
def test_user_pas_setter(instance):
    original = instance.pas
    instance.pas = original
    assert instance.pas == original



@given(instance=user_strategy)
def test_user_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=user_strategy)
def test_user_user_name_setter(instance):
    original = instance.user_name
    instance.user_name = original
    assert instance.user_name == original
