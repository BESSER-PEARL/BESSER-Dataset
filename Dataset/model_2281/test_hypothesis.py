import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_root,
    model_Response,
    model_Exercise,
    model_Delivery,
    model_Course,
    model_Student,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_root_is_not_abstract():
    assert not inspect.isabstract(model_root)


def test_model_root_constructor_exists():
    assert callable(model_root.__init__)


def test_model_root_constructor_args():
    sig = inspect.signature(model_root.__init__)
    params = list(sig.parameters.keys())



def test_model_response_is_not_abstract():
    assert not inspect.isabstract(model_Response)


def test_model_response_constructor_exists():
    assert callable(model_Response.__init__)


def test_model_response_constructor_args():
    sig = inspect.signature(model_Response.__init__)
    params = list(sig.parameters.keys())
    assert "ok" in params, "Missing parameter 'ok'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_model_response_has_ok():
    assert hasattr(model_Response, "ok")
    descriptor = None
    for klass in model_Response.__mro__:
        if "ok" in klass.__dict__:
            descriptor = klass.__dict__["ok"]
            break
    assert isinstance(descriptor, property)

def test_model_response_has_comment():
    assert hasattr(model_Response, "comment")
    descriptor = None
    for klass in model_Response.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_model_response_has_ID():
    assert hasattr(model_Response, "ID")
    descriptor = None
    for klass in model_Response.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_model_exercise_is_not_abstract():
    assert not inspect.isabstract(model_Exercise)


def test_model_exercise_constructor_exists():
    assert callable(model_Exercise.__init__)


def test_model_exercise_constructor_args():
    sig = inspect.signature(model_Exercise.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "deadline_date" in params, "Missing parameter 'deadline_date'"

def test_model_exercise_has_ID():
    assert hasattr(model_Exercise, "ID")
    descriptor = None
    for klass in model_Exercise.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_model_exercise_has_deadline_date():
    assert hasattr(model_Exercise, "deadline_date")
    descriptor = None
    for klass in model_Exercise.__mro__:
        if "deadline_date" in klass.__dict__:
            descriptor = klass.__dict__["deadline_date"]
            break
    assert isinstance(descriptor, property)



def test_model_delivery_is_not_abstract():
    assert not inspect.isabstract(model_Delivery)


def test_model_delivery_constructor_exists():
    assert callable(model_Delivery.__init__)


def test_model_delivery_constructor_args():
    sig = inspect.signature(model_Delivery.__init__)
    params = list(sig.parameters.keys())
    assert "submission_date" in params, "Missing parameter 'submission_date'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "group_number" in params, "Missing parameter 'group_number'"
    assert "answer" in params, "Missing parameter 'answer'"

def test_model_delivery_has_submission_date():
    assert hasattr(model_Delivery, "submission_date")
    descriptor = None
    for klass in model_Delivery.__mro__:
        if "submission_date" in klass.__dict__:
            descriptor = klass.__dict__["submission_date"]
            break
    assert isinstance(descriptor, property)

def test_model_delivery_has_ID():
    assert hasattr(model_Delivery, "ID")
    descriptor = None
    for klass in model_Delivery.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_model_delivery_has_group_number():
    assert hasattr(model_Delivery, "group_number")
    descriptor = None
    for klass in model_Delivery.__mro__:
        if "group_number" in klass.__dict__:
            descriptor = klass.__dict__["group_number"]
            break
    assert isinstance(descriptor, property)

def test_model_delivery_has_answer():
    assert hasattr(model_Delivery, "answer")
    descriptor = None
    for klass in model_Delivery.__mro__:
        if "answer" in klass.__dict__:
            descriptor = klass.__dict__["answer"]
            break
    assert isinstance(descriptor, property)



def test_model_course_is_not_abstract():
    assert not inspect.isabstract(model_Course)


def test_model_course_constructor_exists():
    assert callable(model_Course.__init__)


def test_model_course_constructor_args():
    sig = inspect.signature(model_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_model_course_has_name():
    assert hasattr(model_Course, "name")
    descriptor = None
    for klass in model_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_course_has_ID():
    assert hasattr(model_Course, "ID")
    descriptor = None
    for klass in model_Course.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_model_student_is_not_abstract():
    assert not inspect.isabstract(model_Student)


def test_model_student_constructor_exists():
    assert callable(model_Student.__init__)


def test_model_student_constructor_args():
    sig = inspect.signature(model_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_model_student_has_name():
    assert hasattr(model_Student, "name")
    descriptor = None
    for klass in model_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_student_has_ID():
    assert hasattr(model_Student, "ID")
    descriptor = None
    for klass in model_Student.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
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
model_root_strategy = st.builds(
    model_root,
)
model_Response_strategy = st.builds(
    model_Response,
    ok=
        st.booleans(),
    comment=
        safe_text,
    ID=
        st.integers()
)
model_Exercise_strategy = st.builds(
    model_Exercise,
    ID=
        st.integers(),
    deadline_date=
        st.dates()
)
model_Delivery_strategy = st.builds(
    model_Delivery,
    submission_date=
        st.dates(),
    ID=
        st.integers(),
    group_number=
        st.integers(),
    answer=
        safe_text
)
model_Course_strategy = st.builds(
    model_Course,
    name=
        safe_text,
    ID=
        st.integers()
)
model_Student_strategy = st.builds(
    model_Student,
    name=
        safe_text,
    ID=
        st.integers()
)

@given(instance=model_root_strategy)
@settings(max_examples=50)
def test_model_root_instantiation(instance):
    assert isinstance(instance, model_root)

@given(instance=model_Response_strategy)
@settings(max_examples=50)
def test_model_response_instantiation(instance):
    assert isinstance(instance, model_Response)



@given(instance=model_Response_strategy)
def test_model_response_ok_setter(instance):
    original = instance.ok
    instance.ok = original
    assert instance.ok == original



@given(instance=model_Response_strategy)
def test_model_response_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=model_Response_strategy)
def test_model_response_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=model_Exercise_strategy)
@settings(max_examples=50)
def test_model_exercise_instantiation(instance):
    assert isinstance(instance, model_Exercise)



@given(instance=model_Exercise_strategy)
def test_model_exercise_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=model_Exercise_strategy)
def test_model_exercise_deadline_date_setter(instance):
    original = instance.deadline_date
    instance.deadline_date = original
    assert instance.deadline_date == original

@given(instance=model_Delivery_strategy)
@settings(max_examples=50)
def test_model_delivery_instantiation(instance):
    assert isinstance(instance, model_Delivery)



@given(instance=model_Delivery_strategy)
def test_model_delivery_submission_date_setter(instance):
    original = instance.submission_date
    instance.submission_date = original
    assert instance.submission_date == original



@given(instance=model_Delivery_strategy)
def test_model_delivery_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=model_Delivery_strategy)
def test_model_delivery_group_number_setter(instance):
    original = instance.group_number
    instance.group_number = original
    assert instance.group_number == original



@given(instance=model_Delivery_strategy)
def test_model_delivery_answer_setter(instance):
    original = instance.answer
    instance.answer = original
    assert instance.answer == original

@given(instance=model_Course_strategy)
@settings(max_examples=50)
def test_model_course_instantiation(instance):
    assert isinstance(instance, model_Course)



@given(instance=model_Course_strategy)
def test_model_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_Course_strategy)
def test_model_course_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=model_Student_strategy)
@settings(max_examples=50)
def test_model_student_instantiation(instance):
    assert isinstance(instance, model_Student)



@given(instance=model_Student_strategy)
def test_model_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_Student_strategy)
def test_model_student_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original
