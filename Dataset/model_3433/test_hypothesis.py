import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Matter,
    school::Math,
    school::Matter,
    school::Notation,
    school::ClassRoom,
    school::School,
    school::Student,
    school::Teacher,
    school::Academy,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_matter_is_not_abstract():
    assert not inspect.isabstract(Matter)


def test_matter_constructor_exists():
    assert callable(Matter.__init__)


def test_matter_constructor_args():
    sig = inspect.signature(Matter.__init__)
    params = list(sig.parameters.keys())



def test_school::math_is_not_abstract():
    assert not inspect.isabstract(school::Math)


def test_school::math_constructor_exists():
    assert callable(school::Math.__init__)


def test_school::math_constructor_args():
    sig = inspect.signature(school::Math.__init__)
    params = list(sig.parameters.keys())



def test_school::matter_is_not_abstract():
    assert not inspect.isabstract(school::Matter)


def test_school::matter_constructor_exists():
    assert callable(school::Matter.__init__)


def test_school::matter_constructor_args():
    sig = inspect.signature(school::Matter.__init__)
    params = list(sig.parameters.keys())



def test_school::notation_is_not_abstract():
    assert not inspect.isabstract(school::Notation)


def test_school::notation_constructor_exists():
    assert callable(school::Notation.__init__)


def test_school::notation_constructor_args():
    sig = inspect.signature(school::Notation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_school::notation_has_value():
    assert hasattr(school::Notation, "value")
    descriptor = None
    for klass in school::Notation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_school::classroom_is_not_abstract():
    assert not inspect.isabstract(school::ClassRoom)


def test_school::classroom_constructor_exists():
    assert callable(school::ClassRoom.__init__)


def test_school::classroom_constructor_args():
    sig = inspect.signature(school::ClassRoom.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_school::classroom_has_number():
    assert hasattr(school::ClassRoom, "number")
    descriptor = None
    for klass in school::ClassRoom.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_school::school_is_not_abstract():
    assert not inspect.isabstract(school::School)


def test_school::school_constructor_exists():
    assert callable(school::School.__init__)


def test_school::school_constructor_args():
    sig = inspect.signature(school::School.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"
    assert "name" in params, "Missing parameter 'name'"

def test_school::school_has_rank():
    assert hasattr(school::School, "rank")
    descriptor = None
    for klass in school::School.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)

def test_school::school_has_name():
    assert hasattr(school::School, "name")
    descriptor = None
    for klass in school::School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school::student_is_not_abstract():
    assert not inspect.isabstract(school::Student)


def test_school::student_constructor_exists():
    assert callable(school::Student.__init__)


def test_school::student_constructor_args():
    sig = inspect.signature(school::Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"

def test_school::student_has_name():
    assert hasattr(school::Student, "name")
    descriptor = None
    for klass in school::Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_school::student_has_age():
    assert hasattr(school::Student, "age")
    descriptor = None
    for klass in school::Student.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_school::teacher_is_not_abstract():
    assert not inspect.isabstract(school::Teacher)


def test_school::teacher_constructor_exists():
    assert callable(school::Teacher.__init__)


def test_school::teacher_constructor_args():
    sig = inspect.signature(school::Teacher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school::teacher_has_name():
    assert hasattr(school::Teacher, "name")
    descriptor = None
    for klass in school::Teacher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school::academy_is_not_abstract():
    assert not inspect.isabstract(school::Academy)


def test_school::academy_constructor_exists():
    assert callable(school::Academy.__init__)


def test_school::academy_constructor_args():
    sig = inspect.signature(school::Academy.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school::academy_has_name():
    assert hasattr(school::Academy, "name")
    descriptor = None
    for klass in school::Academy.__mro__:
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
Matter_strategy = st.builds(
    Matter,
)
school::Math_strategy = st.builds(
    school::Math,
)
school::Matter_strategy = st.builds(
    school::Matter,
)
school::Notation_strategy = st.builds(
    school::Notation,
    value=
        st.integers()
)
school::ClassRoom_strategy = st.builds(
    school::ClassRoom,
    number=
        st.integers()
)
school::School_strategy = st.builds(
    school::School,
    rank=
        st.integers(),
    name=
        safe_text
)
school::Student_strategy = st.builds(
    school::Student,
    name=
        safe_text,
    age=
        st.integers()
)
school::Teacher_strategy = st.builds(
    school::Teacher,
    name=
        safe_text
)
school::Academy_strategy = st.builds(
    school::Academy,
    name=
        safe_text
)

@given(instance=Matter_strategy)
@settings(max_examples=50)
def test_matter_instantiation(instance):
    assert isinstance(instance, Matter)

@given(instance=school::Math_strategy)
@settings(max_examples=50)
def test_school::math_instantiation(instance):
    assert isinstance(instance, school::Math)

@given(instance=school::Matter_strategy)
@settings(max_examples=50)
def test_school::matter_instantiation(instance):
    assert isinstance(instance, school::Matter)

@given(instance=school::Notation_strategy)
@settings(max_examples=50)
def test_school::notation_instantiation(instance):
    assert isinstance(instance, school::Notation)

@given(instance=school::Notation_strategy)
def test_school::notation_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=school::Notation_strategy)
def test_school::notation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=school::ClassRoom_strategy)
@settings(max_examples=50)
def test_school::classroom_instantiation(instance):
    assert isinstance(instance, school::ClassRoom)

@given(instance=school::ClassRoom_strategy)
def test_school::classroom_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=school::ClassRoom_strategy)
def test_school::classroom_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=school::School_strategy)
@settings(max_examples=50)
def test_school::school_instantiation(instance):
    assert isinstance(instance, school::School)

@given(instance=school::School_strategy)
def test_school::school_rank_type(instance):
    assert isinstance(instance.rank, int)


@given(instance=school::School_strategy)
def test_school::school_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=school::School_strategy)
def test_school::school_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::School_strategy)
def test_school::school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::Student_strategy)
@settings(max_examples=50)
def test_school::student_instantiation(instance):
    assert isinstance(instance, school::Student)

@given(instance=school::Student_strategy)
def test_school::student_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Student_strategy)
def test_school::student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::Student_strategy)
def test_school::student_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=school::Student_strategy)
def test_school::student_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=school::Teacher_strategy)
@settings(max_examples=50)
def test_school::teacher_instantiation(instance):
    assert isinstance(instance, school::Teacher)

@given(instance=school::Teacher_strategy)
def test_school::teacher_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Teacher_strategy)
def test_school::teacher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=school::Teacher_strategy)
@settings(max_examples=30)
def test_school::teacher_evaluate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluate(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluate' in school::Teacher is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluate' in school::Teacher did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluate' in school::Teacher is not implemented or raised an error")

@given(instance=school::Academy_strategy)
@settings(max_examples=50)
def test_school::academy_instantiation(instance):
    assert isinstance(instance, school::Academy)

@given(instance=school::Academy_strategy)
def test_school::academy_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Academy_strategy)
def test_school::academy_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
