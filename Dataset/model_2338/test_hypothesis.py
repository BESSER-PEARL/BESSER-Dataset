import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PersonsOne_Person,
    PersonsOne_Group,
    Person,
    PersonsOne_Student,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_personsone_person_is_not_abstract():
    assert not inspect.isabstract(PersonsOne_Person)


def test_personsone_person_constructor_exists():
    assert callable(PersonsOne_Person.__init__)


def test_personsone_person_constructor_args():
    sig = inspect.signature(PersonsOne_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"

def test_personsone_person_has_name():
    assert hasattr(PersonsOne_Person, "name")
    descriptor = None
    for klass in PersonsOne_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_personsone_person_has_age():
    assert hasattr(PersonsOne_Person, "age")
    descriptor = None
    for klass in PersonsOne_Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_personsone_group_is_not_abstract():
    assert not inspect.isabstract(PersonsOne_Group)


def test_personsone_group_constructor_exists():
    assert callable(PersonsOne_Group.__init__)


def test_personsone_group_constructor_args():
    sig = inspect.signature(PersonsOne_Group.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_personsone_group_has_name():
    assert hasattr(PersonsOne_Group, "name")
    descriptor = None
    for klass in PersonsOne_Group.__mro__:
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



def test_personsone_student_is_not_abstract():
    assert not inspect.isabstract(PersonsOne_Student)


def test_personsone_student_constructor_exists():
    assert callable(PersonsOne_Student.__init__)


def test_personsone_student_constructor_args():
    sig = inspect.signature(PersonsOne_Student.__init__)
    params = list(sig.parameters.keys())
    assert "grade" in params, "Missing parameter 'grade'"

def test_personsone_student_has_grade():
    assert hasattr(PersonsOne_Student, "grade")
    descriptor = None
    for klass in PersonsOne_Student.__mro__:
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
PersonsOne_Person_strategy = st.builds(
    PersonsOne_Person,
    name=
        safe_text,
    age=
        st.integers()
)
PersonsOne_Group_strategy = st.builds(
    PersonsOne_Group,
    name=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
PersonsOne_Student_strategy = st.builds(
    PersonsOne_Student,
    grade=
        safe_text
)

@given(instance=PersonsOne_Person_strategy)
@settings(max_examples=50)
def test_personsone_person_instantiation(instance):
    assert isinstance(instance, PersonsOne_Person)



@given(instance=PersonsOne_Person_strategy)
def test_personsone_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=PersonsOne_Person_strategy)
def test_personsone_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=PersonsOne_Group_strategy)
@settings(max_examples=50)
def test_personsone_group_instantiation(instance):
    assert isinstance(instance, PersonsOne_Group)



@given(instance=PersonsOne_Group_strategy)
def test_personsone_group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=PersonsOne_Student_strategy)
@settings(max_examples=50)
def test_personsone_student_instantiation(instance):
    assert isinstance(instance, PersonsOne_Student)



@given(instance=PersonsOne_Student_strategy)
def test_personsone_student_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original
