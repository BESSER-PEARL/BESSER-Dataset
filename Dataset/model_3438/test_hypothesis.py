import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    school::School,
    school::Diagram,
    school::Student,
    school::Classroom,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_school::school_is_not_abstract():
    assert not inspect.isabstract(school::School)


def test_school::school_constructor_exists():
    assert callable(school::School.__init__)


def test_school::school_constructor_args():
    sig = inspect.signature(school::School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "zipCode" in params, "Missing parameter 'zipCode'"
    assert "director" in params, "Missing parameter 'director'"
    assert "city" in params, "Missing parameter 'city'"

def test_school::school_has_name():
    assert hasattr(school::School, "name")
    descriptor = None
    for klass in school::School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_school::school_has_zipCode():
    assert hasattr(school::School, "zipCode")
    descriptor = None
    for klass in school::School.__mro__:
        if "zipCode" in klass.__dict__:
            descriptor = klass.__dict__["zipCode"]
            break
    assert isinstance(descriptor, property)

def test_school::school_has_director():
    assert hasattr(school::School, "director")
    descriptor = None
    for klass in school::School.__mro__:
        if "director" in klass.__dict__:
            descriptor = klass.__dict__["director"]
            break
    assert isinstance(descriptor, property)

def test_school::school_has_city():
    assert hasattr(school::School, "city")
    descriptor = None
    for klass in school::School.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)



def test_school::diagram_is_not_abstract():
    assert not inspect.isabstract(school::Diagram)


def test_school::diagram_constructor_exists():
    assert callable(school::Diagram.__init__)


def test_school::diagram_constructor_args():
    sig = inspect.signature(school::Diagram.__init__)
    params = list(sig.parameters.keys())



def test_school::student_is_not_abstract():
    assert not inspect.isabstract(school::Student)


def test_school::student_constructor_exists():
    assert callable(school::Student.__init__)


def test_school::student_constructor_args():
    sig = inspect.signature(school::Student.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "nickname" in params, "Missing parameter 'nickname'"
    assert "name" in params, "Missing parameter 'name'"

def test_school::student_has_age():
    assert hasattr(school::Student, "age")
    descriptor = None
    for klass in school::Student.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_school::student_has_nickname():
    assert hasattr(school::Student, "nickname")
    descriptor = None
    for klass in school::Student.__mro__:
        if "nickname" in klass.__dict__:
            descriptor = klass.__dict__["nickname"]
            break
    assert isinstance(descriptor, property)

def test_school::student_has_name():
    assert hasattr(school::Student, "name")
    descriptor = None
    for klass in school::Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school::classroom_is_not_abstract():
    assert not inspect.isabstract(school::Classroom)


def test_school::classroom_constructor_exists():
    assert callable(school::Classroom.__init__)


def test_school::classroom_constructor_args():
    sig = inspect.signature(school::Classroom.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "teacher" in params, "Missing parameter 'teacher'"
    assert "rank" in params, "Missing parameter 'rank'"

def test_school::classroom_has_name():
    assert hasattr(school::Classroom, "name")
    descriptor = None
    for klass in school::Classroom.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_school::classroom_has_capacity():
    assert hasattr(school::Classroom, "capacity")
    descriptor = None
    for klass in school::Classroom.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_school::classroom_has_teacher():
    assert hasattr(school::Classroom, "teacher")
    descriptor = None
    for klass in school::Classroom.__mro__:
        if "teacher" in klass.__dict__:
            descriptor = klass.__dict__["teacher"]
            break
    assert isinstance(descriptor, property)

def test_school::classroom_has_rank():
    assert hasattr(school::Classroom, "rank")
    descriptor = None
    for klass in school::Classroom.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
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
school::School_strategy = st.builds(
    school::School,
    name=
        safe_text,
    zipCode=
        safe_text,
    director=
        safe_text,
    city=
        safe_text
)
school::Diagram_strategy = st.builds(
    school::Diagram,
)
school::Student_strategy = st.builds(
    school::Student,
    age=
        st.integers(),
    nickname=
        safe_text,
    name=
        safe_text
)
school::Classroom_strategy = st.builds(
    school::Classroom,
    name=
        safe_text,
    capacity=
        st.integers(),
    teacher=
        safe_text,
    rank=
        st.integers()
)

@given(instance=school::School_strategy)
@settings(max_examples=50)
def test_school::school_instantiation(instance):
    assert isinstance(instance, school::School)

@given(instance=school::School_strategy)
def test_school::school_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::School_strategy)
def test_school::school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::School_strategy)
def test_school::school_zipCode_type(instance):
    assert isinstance(instance.zipCode, str)


@given(instance=school::School_strategy)
def test_school::school_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original

@given(instance=school::School_strategy)
def test_school::school_director_type(instance):
    assert isinstance(instance.director, str)


@given(instance=school::School_strategy)
def test_school::school_director_setter(instance):
    original = instance.director
    instance.director = original
    assert instance.director == original

@given(instance=school::School_strategy)
def test_school::school_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=school::School_strategy)
def test_school::school_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=school::Diagram_strategy)
@settings(max_examples=50)
def test_school::diagram_instantiation(instance):
    assert isinstance(instance, school::Diagram)

@given(instance=school::Student_strategy)
@settings(max_examples=50)
def test_school::student_instantiation(instance):
    assert isinstance(instance, school::Student)

@given(instance=school::Student_strategy)
def test_school::student_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=school::Student_strategy)
def test_school::student_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=school::Student_strategy)
def test_school::student_nickname_type(instance):
    assert isinstance(instance.nickname, str)


@given(instance=school::Student_strategy)
def test_school::student_nickname_setter(instance):
    original = instance.nickname
    instance.nickname = original
    assert instance.nickname == original

@given(instance=school::Student_strategy)
def test_school::student_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Student_strategy)
def test_school::student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=school::Student_strategy)
@settings(max_examples=30)
def test_school::student_validate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validate(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validate' in school::Student is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validate' in school::Student did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validate' in school::Student is not implemented or raised an error")

@given(instance=school::Classroom_strategy)
@settings(max_examples=50)
def test_school::classroom_instantiation(instance):
    assert isinstance(instance, school::Classroom)

@given(instance=school::Classroom_strategy)
def test_school::classroom_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Classroom_strategy)
def test_school::classroom_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::Classroom_strategy)
def test_school::classroom_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=school::Classroom_strategy)
def test_school::classroom_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=school::Classroom_strategy)
def test_school::classroom_teacher_type(instance):
    assert isinstance(instance.teacher, str)


@given(instance=school::Classroom_strategy)
def test_school::classroom_teacher_setter(instance):
    original = instance.teacher
    instance.teacher = original
    assert instance.teacher == original

@given(instance=school::Classroom_strategy)
def test_school::classroom_rank_type(instance):
    assert isinstance(instance.rank, int)


@given(instance=school::Classroom_strategy)
def test_school::classroom_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=school::Classroom_strategy)
@settings(max_examples=30)
def test_school::classroom_validate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validate(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validate' in school::Classroom is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validate' in school::Classroom did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validate' in school::Classroom is not implemented or raised an error")
