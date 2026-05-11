import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    edu::Take::Course,
    edu::Student,
    edu::Course,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_edu::take::course_is_not_abstract():
    assert not inspect.isabstract(edu::Take::Course)


def test_edu::take::course_constructor_exists():
    assert callable(edu::Take::Course.__init__)


def test_edu::take::course_constructor_args():
    sig = inspect.signature(edu::Take::Course.__init__)
    params = list(sig.parameters.keys())



def test_edu::student_is_not_abstract():
    assert not inspect.isabstract(edu::Student)


def test_edu::student_constructor_exists():
    assert callable(edu::Student.__init__)


def test_edu::student_constructor_args():
    sig = inspect.signature(edu::Student.__init__)
    params = list(sig.parameters.keys())
    assert "date_of_birth" in params, "Missing parameter 'date_of_birth'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_edu::student_has_date_of_birth():
    assert hasattr(edu::Student, "date_of_birth")
    descriptor = None
    for klass in edu::Student.__mro__:
        if "date_of_birth" in klass.__dict__:
            descriptor = klass.__dict__["date_of_birth"]
            break
    assert isinstance(descriptor, property)

def test_edu::student_has_name():
    assert hasattr(edu::Student, "name")
    descriptor = None
    for klass in edu::Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_edu::student_has_id():
    assert hasattr(edu::Student, "id")
    descriptor = None
    for klass in edu::Student.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_edu::course_is_not_abstract():
    assert not inspect.isabstract(edu::Course)


def test_edu::course_constructor_exists():
    assert callable(edu::Course.__init__)


def test_edu::course_constructor_args():
    sig = inspect.signature(edu::Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_edu::course_has_name():
    assert hasattr(edu::Course, "name")
    descriptor = None
    for klass in edu::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_edu::course_has_id():
    assert hasattr(edu::Course, "id")
    descriptor = None
    for klass in edu::Course.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
edu::Take::Course_strategy = st.builds(
    edu::Take::Course,
)
edu::Student_strategy = st.builds(
    edu::Student,
    date_of_birth=
        st.dates(),
    name=
        safe_text,
    id=
        st.integers()
)
edu::Course_strategy = st.builds(
    edu::Course,
    name=
        safe_text,
    id=
        st.integers()
)

@given(instance=edu::Take::Course_strategy)
@settings(max_examples=50)
def test_edu::take::course_instantiation(instance):
    assert isinstance(instance, edu::Take::Course)

@given(instance=edu::Student_strategy)
@settings(max_examples=50)
def test_edu::student_instantiation(instance):
    assert isinstance(instance, edu::Student)

@given(instance=edu::Student_strategy)
def test_edu::student_date_of_birth_type(instance):
    assert isinstance(instance.date_of_birth, date)


@given(instance=edu::Student_strategy)
def test_edu::student_date_of_birth_setter(instance):
    original = instance.date_of_birth
    instance.date_of_birth = original
    assert instance.date_of_birth == original

@given(instance=edu::Student_strategy)
def test_edu::student_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=edu::Student_strategy)
def test_edu::student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=edu::Student_strategy)
def test_edu::student_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=edu::Student_strategy)
def test_edu::student_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=edu::Course_strategy)
@settings(max_examples=50)
def test_edu::course_instantiation(instance):
    assert isinstance(instance, edu::Course)

@given(instance=edu::Course_strategy)
def test_edu::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=edu::Course_strategy)
def test_edu::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=edu::Course_strategy)
def test_edu::course_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=edu::Course_strategy)
def test_edu::course_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
