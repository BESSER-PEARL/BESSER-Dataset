import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    schol_School,
    schol_Diagram,
    schol_Student,
    schol_Classroom,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_schol_school_is_not_abstract():
    assert not inspect.isabstract(schol_School)


def test_schol_school_constructor_exists():
    assert callable(schol_School.__init__)


def test_schol_school_constructor_args():
    sig = inspect.signature(schol_School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_schol_school_has_name():
    assert hasattr(schol_School, "name")
    descriptor = None
    for klass in schol_School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_schol_diagram_is_not_abstract():
    assert not inspect.isabstract(schol_Diagram)


def test_schol_diagram_constructor_exists():
    assert callable(schol_Diagram.__init__)


def test_schol_diagram_constructor_args():
    sig = inspect.signature(schol_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_schol_student_is_not_abstract():
    assert not inspect.isabstract(schol_Student)


def test_schol_student_constructor_exists():
    assert callable(schol_Student.__init__)


def test_schol_student_constructor_args():
    sig = inspect.signature(schol_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_schol_student_has_name():
    assert hasattr(schol_Student, "name")
    descriptor = None
    for klass in schol_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_schol_classroom_is_not_abstract():
    assert not inspect.isabstract(schol_Classroom)


def test_schol_classroom_constructor_exists():
    assert callable(schol_Classroom.__init__)


def test_schol_classroom_constructor_args():
    sig = inspect.signature(schol_Classroom.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_schol_classroom_has_name():
    assert hasattr(schol_Classroom, "name")
    descriptor = None
    for klass in schol_Classroom.__mro__:
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
schol_School_strategy = st.builds(
    schol_School,
    name=
        safe_text
)
schol_Diagram_strategy = st.builds(
    schol_Diagram,
)
schol_Student_strategy = st.builds(
    schol_Student,
    name=
        safe_text
)
schol_Classroom_strategy = st.builds(
    schol_Classroom,
    name=
        safe_text
)

@given(instance=schol_School_strategy)
@settings(max_examples=50)
def test_schol_school_instantiation(instance):
    assert isinstance(instance, schol_School)



@given(instance=schol_School_strategy)
def test_schol_school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=schol_Diagram_strategy)
@settings(max_examples=50)
def test_schol_diagram_instantiation(instance):
    assert isinstance(instance, schol_Diagram)

@given(instance=schol_Student_strategy)
@settings(max_examples=50)
def test_schol_student_instantiation(instance):
    assert isinstance(instance, schol_Student)



@given(instance=schol_Student_strategy)
def test_schol_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=schol_Classroom_strategy)
@settings(max_examples=50)
def test_schol_classroom_instantiation(instance):
    assert isinstance(instance, schol_Classroom)



@given(instance=schol_Classroom_strategy)
def test_schol_classroom_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
