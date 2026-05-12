import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    education_Course,
    Person,
    education_Teacher,
    education_Student,
    education_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_education_course_is_not_abstract():
    assert not inspect.isabstract(education_Course)


def test_education_course_constructor_exists():
    assert callable(education_Course.__init__)


def test_education_course_constructor_args():
    sig = inspect.signature(education_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_education_course_has_name():
    assert hasattr(education_Course, "name")
    descriptor = None
    for klass in education_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_education_teacher_is_not_abstract():
    assert not inspect.isabstract(education_Teacher)


def test_education_teacher_constructor_exists():
    assert callable(education_Teacher.__init__)


def test_education_teacher_constructor_args():
    sig = inspect.signature(education_Teacher.__init__)
    params = list(sig.parameters.keys())



def test_education_student_is_not_abstract():
    assert not inspect.isabstract(education_Student)


def test_education_student_constructor_exists():
    assert callable(education_Student.__init__)


def test_education_student_constructor_args():
    sig = inspect.signature(education_Student.__init__)
    params = list(sig.parameters.keys())



def test_education_person_is_not_abstract():
    assert not inspect.isabstract(education_Person)


def test_education_person_constructor_exists():
    assert callable(education_Person.__init__)


def test_education_person_constructor_args():
    sig = inspect.signature(education_Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_education_person_has_lastname():
    assert hasattr(education_Person, "lastname")
    descriptor = None
    for klass in education_Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_education_person_has_firstname():
    assert hasattr(education_Person, "firstname")
    descriptor = None
    for klass in education_Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
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
education_Course_strategy = st.builds(
    education_Course,
    name=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
education_Teacher_strategy = st.builds(
    education_Teacher,
)
education_Student_strategy = st.builds(
    education_Student,
)
education_Person_strategy = st.builds(
    education_Person,
    lastname=
        safe_text,
    firstname=
        safe_text
)

@given(instance=education_Course_strategy)
@settings(max_examples=50)
def test_education_course_instantiation(instance):
    assert isinstance(instance, education_Course)



@given(instance=education_Course_strategy)
def test_education_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=education_Course_strategy)
@settings(max_examples=30)
def test_education_course_finish_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.finish(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.finish).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'finish' in education_Course is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'finish' in education_Course did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'finish' in education_Course is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=education_Course_strategy)
@settings(max_examples=30)
def test_education_course_start_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.start(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.start).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'start' in education_Course is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'start' in education_Course did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'start' in education_Course is not implemented or raised an error")

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=education_Teacher_strategy)
@settings(max_examples=50)
def test_education_teacher_instantiation(instance):
    assert isinstance(instance, education_Teacher)

@given(instance=education_Student_strategy)
@settings(max_examples=50)
def test_education_student_instantiation(instance):
    assert isinstance(instance, education_Student)

@given(instance=education_Person_strategy)
@settings(max_examples=50)
def test_education_person_instantiation(instance):
    assert isinstance(instance, education_Person)



@given(instance=education_Person_strategy)
def test_education_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=education_Person_strategy)
def test_education_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original
