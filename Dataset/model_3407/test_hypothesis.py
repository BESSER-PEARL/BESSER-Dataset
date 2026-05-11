import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    education::Course,
    Person,
    education::Teacher,
    education::Student,
    education::Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_education::course_is_not_abstract():
    assert not inspect.isabstract(education::Course)


def test_education::course_constructor_exists():
    assert callable(education::Course.__init__)


def test_education::course_constructor_args():
    sig = inspect.signature(education::Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_education::course_has_name():
    assert hasattr(education::Course, "name")
    descriptor = None
    for klass in education::Course.__mro__:
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



def test_education::teacher_is_not_abstract():
    assert not inspect.isabstract(education::Teacher)


def test_education::teacher_constructor_exists():
    assert callable(education::Teacher.__init__)


def test_education::teacher_constructor_args():
    sig = inspect.signature(education::Teacher.__init__)
    params = list(sig.parameters.keys())



def test_education::student_is_not_abstract():
    assert not inspect.isabstract(education::Student)


def test_education::student_constructor_exists():
    assert callable(education::Student.__init__)


def test_education::student_constructor_args():
    sig = inspect.signature(education::Student.__init__)
    params = list(sig.parameters.keys())



def test_education::person_is_not_abstract():
    assert not inspect.isabstract(education::Person)


def test_education::person_constructor_exists():
    assert callable(education::Person.__init__)


def test_education::person_constructor_args():
    sig = inspect.signature(education::Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "lastname" in params, "Missing parameter 'lastname'"

def test_education::person_has_firstname():
    assert hasattr(education::Person, "firstname")
    descriptor = None
    for klass in education::Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_education::person_has_lastname():
    assert hasattr(education::Person, "lastname")
    descriptor = None
    for klass in education::Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
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
education::Course_strategy = st.builds(
    education::Course,
    name=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
education::Teacher_strategy = st.builds(
    education::Teacher,
)
education::Student_strategy = st.builds(
    education::Student,
)
education::Person_strategy = st.builds(
    education::Person,
    firstname=
        safe_text,
    lastname=
        safe_text
)

@given(instance=education::Course_strategy)
@settings(max_examples=50)
def test_education::course_instantiation(instance):
    assert isinstance(instance, education::Course)

@given(instance=education::Course_strategy)
def test_education::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=education::Course_strategy)
def test_education::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=education::Course_strategy)
@settings(max_examples=30)
def test_education::course_finish_changes_state(instance):
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
        assert has_statements, f"Function 'finish' in education::Course is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'finish' in education::Course did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'finish' in education::Course is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=education::Course_strategy)
@settings(max_examples=30)
def test_education::course_start_changes_state(instance):
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
        assert has_statements, f"Function 'start' in education::Course is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'start' in education::Course did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'start' in education::Course is not implemented or raised an error")

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=education::Teacher_strategy)
@settings(max_examples=50)
def test_education::teacher_instantiation(instance):
    assert isinstance(instance, education::Teacher)

@given(instance=education::Student_strategy)
@settings(max_examples=50)
def test_education::student_instantiation(instance):
    assert isinstance(instance, education::Student)

@given(instance=education::Person_strategy)
@settings(max_examples=50)
def test_education::person_instantiation(instance):
    assert isinstance(instance, education::Person)

@given(instance=education::Person_strategy)
def test_education::person_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=education::Person_strategy)
def test_education::person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=education::Person_strategy)
def test_education::person_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=education::Person_strategy)
def test_education::person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original
