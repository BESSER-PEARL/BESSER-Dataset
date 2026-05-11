import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PersonsOne::Person,
    PersonsOne::Group,
    Person,
    PersonsOne::Student,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_personsone::person_is_not_abstract():
    assert not inspect.isabstract(PersonsOne::Person)


def test_personsone::person_constructor_exists():
    assert callable(PersonsOne::Person.__init__)


def test_personsone::person_constructor_args():
    sig = inspect.signature(PersonsOne::Person.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"

def test_personsone::person_has_age():
    assert hasattr(PersonsOne::Person, "age")
    descriptor = None
    for klass in PersonsOne::Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_personsone::person_has_name():
    assert hasattr(PersonsOne::Person, "name")
    descriptor = None
    for klass in PersonsOne::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_personsone::group_is_not_abstract():
    assert not inspect.isabstract(PersonsOne::Group)


def test_personsone::group_constructor_exists():
    assert callable(PersonsOne::Group.__init__)


def test_personsone::group_constructor_args():
    sig = inspect.signature(PersonsOne::Group.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_personsone::group_has_name():
    assert hasattr(PersonsOne::Group, "name")
    descriptor = None
    for klass in PersonsOne::Group.__mro__:
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



def test_personsone::student_is_not_abstract():
    assert not inspect.isabstract(PersonsOne::Student)


def test_personsone::student_constructor_exists():
    assert callable(PersonsOne::Student.__init__)


def test_personsone::student_constructor_args():
    sig = inspect.signature(PersonsOne::Student.__init__)
    params = list(sig.parameters.keys())
    assert "grade" in params, "Missing parameter 'grade'"

def test_personsone::student_has_grade():
    assert hasattr(PersonsOne::Student, "grade")
    descriptor = None
    for klass in PersonsOne::Student.__mro__:
        if "grade" in klass.__dict__:
            descriptor = klass.__dict__["grade"]
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
PersonsOne::Person_strategy = st.builds(
    PersonsOne::Person,
    age=
        st.integers(),
    name=
        safe_text
)
PersonsOne::Group_strategy = st.builds(
    PersonsOne::Group,
    name=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
PersonsOne::Student_strategy = st.builds(
    PersonsOne::Student,
    grade=
        safe_text
)

@given(instance=PersonsOne::Person_strategy)
@settings(max_examples=50)
def test_personsone::person_instantiation(instance):
    assert isinstance(instance, PersonsOne::Person)

@given(instance=PersonsOne::Person_strategy)
def test_personsone::person_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=PersonsOne::Person_strategy)
def test_personsone::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=PersonsOne::Person_strategy)
def test_personsone::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PersonsOne::Person_strategy)
def test_personsone::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PersonsOne::Group_strategy)
@settings(max_examples=50)
def test_personsone::group_instantiation(instance):
    assert isinstance(instance, PersonsOne::Group)

@given(instance=PersonsOne::Group_strategy)
def test_personsone::group_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PersonsOne::Group_strategy)
def test_personsone::group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=PersonsOne::Student_strategy)
@settings(max_examples=50)
def test_personsone::student_instantiation(instance):
    assert isinstance(instance, PersonsOne::Student)

@given(instance=PersonsOne::Student_strategy)
def test_personsone::student_grade_type(instance):
    assert isinstance(instance.grade, str)


@given(instance=PersonsOne::Student_strategy)
def test_personsone::student_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original
