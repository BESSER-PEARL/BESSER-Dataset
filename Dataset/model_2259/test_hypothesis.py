import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Courses_Answer,
    Courses_Assignment,
    Courses_Person,
    Courses_Course,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_courses_answer_is_not_abstract():
    assert not inspect.isabstract(Courses_Answer)


def test_courses_answer_constructor_exists():
    assert callable(Courses_Answer.__init__)


def test_courses_answer_constructor_args():
    sig = inspect.signature(Courses_Answer.__init__)
    params = list(sig.parameters.keys())
    assert "pass_" in params, "Missing parameter 'pass_'"
    assert "text" in params, "Missing parameter 'text'"
    assert "id" in params, "Missing parameter 'id'"

def test_courses_answer_has_pass_():
    assert hasattr(Courses_Answer, "pass_")
    descriptor = None
    for klass in Courses_Answer.__mro__:
        if "pass_" in klass.__dict__:
            descriptor = klass.__dict__["pass_"]
            break
    assert isinstance(descriptor, property)

def test_courses_answer_has_text():
    assert hasattr(Courses_Answer, "text")
    descriptor = None
    for klass in Courses_Answer.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_courses_answer_has_id():
    assert hasattr(Courses_Answer, "id")
    descriptor = None
    for klass in Courses_Answer.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_courses_assignment_is_not_abstract():
    assert not inspect.isabstract(Courses_Assignment)


def test_courses_assignment_constructor_exists():
    assert callable(Courses_Assignment.__init__)


def test_courses_assignment_constructor_args():
    sig = inspect.signature(Courses_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_courses_assignment_has_name():
    assert hasattr(Courses_Assignment, "name")
    descriptor = None
    for klass in Courses_Assignment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_courses_assignment_has_description():
    assert hasattr(Courses_Assignment, "description")
    descriptor = None
    for klass in Courses_Assignment.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_courses_assignment_has_mandatory():
    assert hasattr(Courses_Assignment, "mandatory")
    descriptor = None
    for klass in Courses_Assignment.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)



def test_courses_person_is_not_abstract():
    assert not inspect.isabstract(Courses_Person)


def test_courses_person_constructor_exists():
    assert callable(Courses_Person.__init__)


def test_courses_person_constructor_args():
    sig = inspect.signature(Courses_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "role" in params, "Missing parameter 'role'"
    assert "id" in params, "Missing parameter 'id'"

def test_courses_person_has_name():
    assert hasattr(Courses_Person, "name")
    descriptor = None
    for klass in Courses_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_courses_person_has_role():
    assert hasattr(Courses_Person, "role")
    descriptor = None
    for klass in Courses_Person.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_courses_person_has_id():
    assert hasattr(Courses_Person, "id")
    descriptor = None
    for klass in Courses_Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_courses_course_is_not_abstract():
    assert not inspect.isabstract(Courses_Course)


def test_courses_course_constructor_exists():
    assert callable(Courses_Course.__init__)


def test_courses_course_constructor_args():
    sig = inspect.signature(Courses_Course.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "credit" in params, "Missing parameter 'credit'"

def test_courses_course_has_id():
    assert hasattr(Courses_Course, "id")
    descriptor = None
    for klass in Courses_Course.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_courses_course_has_name():
    assert hasattr(Courses_Course, "name")
    descriptor = None
    for klass in Courses_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_courses_course_has_credit():
    assert hasattr(Courses_Course, "credit")
    descriptor = None
    for klass in Courses_Course.__mro__:
        if "credit" in klass.__dict__:
            descriptor = klass.__dict__["credit"]
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
Courses_Answer_strategy = st.builds(
    Courses_Answer,
    pass_=
        st.booleans(),
    text=
        safe_text,
    id=
        st.integers()
)
Courses_Assignment_strategy = st.builds(
    Courses_Assignment,
    name=
        safe_text,
    description=
        safe_text,
    mandatory=
        st.booleans()
)
Courses_Person_strategy = st.builds(
    Courses_Person,
    name=
        safe_text,
    role=
        safe_text,
    id=
        st.integers()
)
Courses_Course_strategy = st.builds(
    Courses_Course,
    id=
        safe_text,
    name=
        safe_text,
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Courses_Answer_strategy)
@settings(max_examples=50)
def test_courses_answer_instantiation(instance):
    assert isinstance(instance, Courses_Answer)



@given(instance=Courses_Answer_strategy)
def test_courses_answer_pass__setter(instance):
    original = instance.pass_
    instance.pass_ = original
    assert instance.pass_ == original



@given(instance=Courses_Answer_strategy)
def test_courses_answer_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=Courses_Answer_strategy)
def test_courses_answer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Courses_Assignment_strategy)
@settings(max_examples=50)
def test_courses_assignment_instantiation(instance):
    assert isinstance(instance, Courses_Assignment)



@given(instance=Courses_Assignment_strategy)
def test_courses_assignment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Courses_Assignment_strategy)
def test_courses_assignment_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Courses_Assignment_strategy)
def test_courses_assignment_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=Courses_Person_strategy)
@settings(max_examples=50)
def test_courses_person_instantiation(instance):
    assert isinstance(instance, Courses_Person)



@given(instance=Courses_Person_strategy)
def test_courses_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Courses_Person_strategy)
def test_courses_person_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original



@given(instance=Courses_Person_strategy)
def test_courses_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Courses_Course_strategy)
@settings(max_examples=50)
def test_courses_course_instantiation(instance):
    assert isinstance(instance, Courses_Course)



@given(instance=Courses_Course_strategy)
def test_courses_course_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Courses_Course_strategy)
def test_courses_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Courses_Course_strategy)
def test_courses_course_credit_setter(instance):
    original = instance.credit
    instance.credit = original
    assert instance.credit == original
