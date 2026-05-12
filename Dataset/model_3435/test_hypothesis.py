import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    school_School,
    school_Diagram,
    school_Student,
    school_Classroom,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_school_school_is_not_abstract():
    assert not inspect.isabstract(school_School)


def test_school_school_constructor_exists():
    assert callable(school_School.__init__)


def test_school_school_constructor_args():
    sig = inspect.signature(school_School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_school_has_name():
    assert hasattr(school_School, "name")
    descriptor = None
    for klass in school_School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school_diagram_is_not_abstract():
    assert not inspect.isabstract(school_Diagram)


def test_school_diagram_constructor_exists():
    assert callable(school_Diagram.__init__)


def test_school_diagram_constructor_args():
    sig = inspect.signature(school_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_school_student_is_not_abstract():
    assert not inspect.isabstract(school_Student)


def test_school_student_constructor_exists():
    assert callable(school_Student.__init__)


def test_school_student_constructor_args():
    sig = inspect.signature(school_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_student_has_name():
    assert hasattr(school_Student, "name")
    descriptor = None
    for klass in school_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school_classroom_is_not_abstract():
    assert not inspect.isabstract(school_Classroom)


def test_school_classroom_constructor_exists():
    assert callable(school_Classroom.__init__)


def test_school_classroom_constructor_args():
    sig = inspect.signature(school_Classroom.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_classroom_has_name():
    assert hasattr(school_Classroom, "name")
    descriptor = None
    for klass in school_Classroom.__mro__:
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
school_School_strategy = st.builds(
    school_School,
    name=
        safe_text
)
school_Diagram_strategy = st.builds(
    school_Diagram,
)
school_Student_strategy = st.builds(
    school_Student,
    name=
        safe_text
)
school_Classroom_strategy = st.builds(
    school_Classroom,
    name=
        safe_text
)

@given(instance=school_School_strategy)
@settings(max_examples=50)
def test_school_school_instantiation(instance):
    assert isinstance(instance, school_School)



@given(instance=school_School_strategy)
def test_school_school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school_Diagram_strategy)
@settings(max_examples=50)
def test_school_diagram_instantiation(instance):
    assert isinstance(instance, school_Diagram)

@given(instance=school_Student_strategy)
@settings(max_examples=50)
def test_school_student_instantiation(instance):
    assert isinstance(instance, school_Student)



@given(instance=school_Student_strategy)
def test_school_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school_Classroom_strategy)
@settings(max_examples=50)
def test_school_classroom_instantiation(instance):
    assert isinstance(instance, school_Classroom)



@given(instance=school_Classroom_strategy)
def test_school_classroom_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
