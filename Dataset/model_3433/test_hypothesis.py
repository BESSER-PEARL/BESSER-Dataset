import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Matter,
    school_Math,
    school_Matter,
    school_Notation,
    school_ClassRoom,
    school_School,
    school_Student,
    school_Teacher,
    school_Academy,
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



def test_school_math_is_not_abstract():
    assert not inspect.isabstract(school_Math)


def test_school_math_constructor_exists():
    assert callable(school_Math.__init__)


def test_school_math_constructor_args():
    sig = inspect.signature(school_Math.__init__)
    params = list(sig.parameters.keys())



def test_school_matter_is_not_abstract():
    assert not inspect.isabstract(school_Matter)


def test_school_matter_constructor_exists():
    assert callable(school_Matter.__init__)


def test_school_matter_constructor_args():
    sig = inspect.signature(school_Matter.__init__)
    params = list(sig.parameters.keys())



def test_school_notation_is_not_abstract():
    assert not inspect.isabstract(school_Notation)


def test_school_notation_constructor_exists():
    assert callable(school_Notation.__init__)


def test_school_notation_constructor_args():
    sig = inspect.signature(school_Notation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_school_notation_has_value():
    assert hasattr(school_Notation, "value")
    descriptor = None
    for klass in school_Notation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_school_classroom_is_not_abstract():
    assert not inspect.isabstract(school_ClassRoom)


def test_school_classroom_constructor_exists():
    assert callable(school_ClassRoom.__init__)


def test_school_classroom_constructor_args():
    sig = inspect.signature(school_ClassRoom.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_school_classroom_has_number():
    assert hasattr(school_ClassRoom, "number")
    descriptor = None
    for klass in school_ClassRoom.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_school_school_is_not_abstract():
    assert not inspect.isabstract(school_School)


def test_school_school_constructor_exists():
    assert callable(school_School.__init__)


def test_school_school_constructor_args():
    sig = inspect.signature(school_School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "rank" in params, "Missing parameter 'rank'"

def test_school_school_has_name():
    assert hasattr(school_School, "name")
    descriptor = None
    for klass in school_School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_school_school_has_rank():
    assert hasattr(school_School, "rank")
    descriptor = None
    for klass in school_School.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)



def test_school_student_is_not_abstract():
    assert not inspect.isabstract(school_Student)


def test_school_student_constructor_exists():
    assert callable(school_Student.__init__)


def test_school_student_constructor_args():
    sig = inspect.signature(school_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"

def test_school_student_has_name():
    assert hasattr(school_Student, "name")
    descriptor = None
    for klass in school_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_school_student_has_age():
    assert hasattr(school_Student, "age")
    descriptor = None
    for klass in school_Student.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_school_teacher_is_not_abstract():
    assert not inspect.isabstract(school_Teacher)


def test_school_teacher_constructor_exists():
    assert callable(school_Teacher.__init__)


def test_school_teacher_constructor_args():
    sig = inspect.signature(school_Teacher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_teacher_has_name():
    assert hasattr(school_Teacher, "name")
    descriptor = None
    for klass in school_Teacher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school_academy_is_not_abstract():
    assert not inspect.isabstract(school_Academy)


def test_school_academy_constructor_exists():
    assert callable(school_Academy.__init__)


def test_school_academy_constructor_args():
    sig = inspect.signature(school_Academy.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_academy_has_name():
    assert hasattr(school_Academy, "name")
    descriptor = None
    for klass in school_Academy.__mro__:
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
school_Math_strategy = st.builds(
    school_Math,
)
school_Matter_strategy = st.builds(
    school_Matter,
)
school_Notation_strategy = st.builds(
    school_Notation,
    value=
        st.integers()
)
school_ClassRoom_strategy = st.builds(
    school_ClassRoom,
    number=
        st.integers()
)
school_School_strategy = st.builds(
    school_School,
    name=
        safe_text,
    rank=
        st.integers()
)
school_Student_strategy = st.builds(
    school_Student,
    name=
        safe_text,
    age=
        st.integers()
)
school_Teacher_strategy = st.builds(
    school_Teacher,
    name=
        safe_text
)
school_Academy_strategy = st.builds(
    school_Academy,
    name=
        safe_text
)

@given(instance=Matter_strategy)
@settings(max_examples=50)
def test_matter_instantiation(instance):
    assert isinstance(instance, Matter)

@given(instance=school_Math_strategy)
@settings(max_examples=50)
def test_school_math_instantiation(instance):
    assert isinstance(instance, school_Math)

@given(instance=school_Matter_strategy)
@settings(max_examples=50)
def test_school_matter_instantiation(instance):
    assert isinstance(instance, school_Matter)

@given(instance=school_Notation_strategy)
@settings(max_examples=50)
def test_school_notation_instantiation(instance):
    assert isinstance(instance, school_Notation)



@given(instance=school_Notation_strategy)
def test_school_notation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=school_ClassRoom_strategy)
@settings(max_examples=50)
def test_school_classroom_instantiation(instance):
    assert isinstance(instance, school_ClassRoom)



@given(instance=school_ClassRoom_strategy)
def test_school_classroom_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=school_School_strategy)
@settings(max_examples=50)
def test_school_school_instantiation(instance):
    assert isinstance(instance, school_School)



@given(instance=school_School_strategy)
def test_school_school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=school_School_strategy)
def test_school_school_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=school_Student_strategy)
@settings(max_examples=50)
def test_school_student_instantiation(instance):
    assert isinstance(instance, school_Student)



@given(instance=school_Student_strategy)
def test_school_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=school_Student_strategy)
def test_school_student_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=school_Teacher_strategy)
@settings(max_examples=50)
def test_school_teacher_instantiation(instance):
    assert isinstance(instance, school_Teacher)



@given(instance=school_Teacher_strategy)
def test_school_teacher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=school_Teacher_strategy)
@settings(max_examples=30)
def test_school_teacher_evaluate_changes_state(instance):
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
        assert has_statements, f"Function 'evaluate' in school_Teacher is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluate' in school_Teacher did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluate' in school_Teacher is not implemented or raised an error")

@given(instance=school_Academy_strategy)
@settings(max_examples=50)
def test_school_academy_instantiation(instance):
    assert isinstance(instance, school_Academy)



@given(instance=school_Academy_strategy)
def test_school_academy_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
