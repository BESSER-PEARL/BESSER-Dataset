import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Courses::Answer,
    Courses::Assignment,
    Courses::Person,
    Courses::Course,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_courses::answer_is_not_abstract():
    assert not inspect.isabstract(Courses::Answer)


def test_courses::answer_constructor_exists():
    assert callable(Courses::Answer.__init__)


def test_courses::answer_constructor_args():
    sig = inspect.signature(Courses::Answer.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "pass_" in params, "Missing parameter 'pass_'"
    assert "id" in params, "Missing parameter 'id'"

def test_courses::answer_has_text():
    assert hasattr(Courses::Answer, "text")
    descriptor = None
    for klass in Courses::Answer.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_courses::answer_has_pass_():
    assert hasattr(Courses::Answer, "pass_")
    descriptor = None
    for klass in Courses::Answer.__mro__:
        if "pass_" in klass.__dict__:
            descriptor = klass.__dict__["pass_"]
            break
    assert isinstance(descriptor, property)

def test_courses::answer_has_id():
    assert hasattr(Courses::Answer, "id")
    descriptor = None
    for klass in Courses::Answer.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_courses::assignment_is_not_abstract():
    assert not inspect.isabstract(Courses::Assignment)


def test_courses::assignment_constructor_exists():
    assert callable(Courses::Assignment.__init__)


def test_courses::assignment_constructor_args():
    sig = inspect.signature(Courses::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "name" in params, "Missing parameter 'name'"

def test_courses::assignment_has_description():
    assert hasattr(Courses::Assignment, "description")
    descriptor = None
    for klass in Courses::Assignment.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_courses::assignment_has_mandatory():
    assert hasattr(Courses::Assignment, "mandatory")
    descriptor = None
    for klass in Courses::Assignment.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)

def test_courses::assignment_has_name():
    assert hasattr(Courses::Assignment, "name")
    descriptor = None
    for klass in Courses::Assignment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_courses::person_is_not_abstract():
    assert not inspect.isabstract(Courses::Person)


def test_courses::person_constructor_exists():
    assert callable(Courses::Person.__init__)


def test_courses::person_constructor_args():
    sig = inspect.signature(Courses::Person.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "role" in params, "Missing parameter 'role'"

def test_courses::person_has_id():
    assert hasattr(Courses::Person, "id")
    descriptor = None
    for klass in Courses::Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_courses::person_has_name():
    assert hasattr(Courses::Person, "name")
    descriptor = None
    for klass in Courses::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_courses::person_has_role():
    assert hasattr(Courses::Person, "role")
    descriptor = None
    for klass in Courses::Person.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)



def test_courses::course_is_not_abstract():
    assert not inspect.isabstract(Courses::Course)


def test_courses::course_constructor_exists():
    assert callable(Courses::Course.__init__)


def test_courses::course_constructor_args():
    sig = inspect.signature(Courses::Course.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "credit" in params, "Missing parameter 'credit'"
    assert "name" in params, "Missing parameter 'name'"

def test_courses::course_has_id():
    assert hasattr(Courses::Course, "id")
    descriptor = None
    for klass in Courses::Course.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_courses::course_has_credit():
    assert hasattr(Courses::Course, "credit")
    descriptor = None
    for klass in Courses::Course.__mro__:
        if "credit" in klass.__dict__:
            descriptor = klass.__dict__["credit"]
            break
    assert isinstance(descriptor, property)

def test_courses::course_has_name():
    assert hasattr(Courses::Course, "name")
    descriptor = None
    for klass in Courses::Course.__mro__:
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
Courses::Answer_strategy = st.builds(
    Courses::Answer,
    text=
        safe_text,
    pass_=
        st.booleans(),
    id=
        st.integers()
)
Courses::Assignment_strategy = st.builds(
    Courses::Assignment,
    description=
        safe_text,
    mandatory=
        st.booleans(),
    name=
        safe_text
)
Courses::Person_strategy = st.builds(
    Courses::Person,
    id=
        st.integers(),
    name=
        safe_text,
    role=
        safe_text
)
Courses::Course_strategy = st.builds(
    Courses::Course,
    id=
        safe_text,
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)

@given(instance=Courses::Answer_strategy)
@settings(max_examples=50)
def test_courses::answer_instantiation(instance):
    assert isinstance(instance, Courses::Answer)

@given(instance=Courses::Answer_strategy)
def test_courses::answer_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=Courses::Answer_strategy)
def test_courses::answer_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Courses::Answer_strategy)
def test_courses::answer_pass__type(instance):
    assert isinstance(instance.pass_, bool)


@given(instance=Courses::Answer_strategy)
def test_courses::answer_pass__setter(instance):
    original = instance.pass_
    instance.pass_ = original
    assert instance.pass_ == original

@given(instance=Courses::Answer_strategy)
def test_courses::answer_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=Courses::Answer_strategy)
def test_courses::answer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Courses::Assignment_strategy)
@settings(max_examples=50)
def test_courses::assignment_instantiation(instance):
    assert isinstance(instance, Courses::Assignment)

@given(instance=Courses::Assignment_strategy)
def test_courses::assignment_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=Courses::Assignment_strategy)
def test_courses::assignment_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Courses::Assignment_strategy)
def test_courses::assignment_mandatory_type(instance):
    assert isinstance(instance.mandatory, bool)


@given(instance=Courses::Assignment_strategy)
def test_courses::assignment_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=Courses::Assignment_strategy)
def test_courses::assignment_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Courses::Assignment_strategy)
def test_courses::assignment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Courses::Person_strategy)
@settings(max_examples=50)
def test_courses::person_instantiation(instance):
    assert isinstance(instance, Courses::Person)

@given(instance=Courses::Person_strategy)
def test_courses::person_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=Courses::Person_strategy)
def test_courses::person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Courses::Person_strategy)
def test_courses::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Courses::Person_strategy)
def test_courses::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Courses::Person_strategy)
def test_courses::person_role_type(instance):
    assert isinstance(instance.role, str)


@given(instance=Courses::Person_strategy)
def test_courses::person_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=Courses::Course_strategy)
@settings(max_examples=50)
def test_courses::course_instantiation(instance):
    assert isinstance(instance, Courses::Course)

@given(instance=Courses::Course_strategy)
def test_courses::course_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Courses::Course_strategy)
def test_courses::course_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Courses::Course_strategy)
def test_courses::course_credit_type(instance):
    assert isinstance(instance.credit, float)


@given(instance=Courses::Course_strategy)
def test_courses::course_credit_setter(instance):
    original = instance.credit
    instance.credit = original
    assert instance.credit == original

@given(instance=Courses::Course_strategy)
def test_courses::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Courses::Course_strategy)
def test_courses::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
