import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    schul_School,
    schul_Diagram,
    schul_Student,
    schul_Classroom,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_schul_school_is_not_abstract():
    assert not inspect.isabstract(schul_School)


def test_schul_school_constructor_exists():
    assert callable(schul_School.__init__)


def test_schul_school_constructor_args():
    sig = inspect.signature(schul_School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_schul_school_has_name():
    assert hasattr(schul_School, "name")
    descriptor = None
    for klass in schul_School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_schul_diagram_is_not_abstract():
    assert not inspect.isabstract(schul_Diagram)


def test_schul_diagram_constructor_exists():
    assert callable(schul_Diagram.__init__)


def test_schul_diagram_constructor_args():
    sig = inspect.signature(schul_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_schul_student_is_not_abstract():
    assert not inspect.isabstract(schul_Student)


def test_schul_student_constructor_exists():
    assert callable(schul_Student.__init__)


def test_schul_student_constructor_args():
    sig = inspect.signature(schul_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_schul_student_has_name():
    assert hasattr(schul_Student, "name")
    descriptor = None
    for klass in schul_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_schul_classroom_is_not_abstract():
    assert not inspect.isabstract(schul_Classroom)


def test_schul_classroom_constructor_exists():
    assert callable(schul_Classroom.__init__)


def test_schul_classroom_constructor_args():
    sig = inspect.signature(schul_Classroom.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_schul_classroom_has_name():
    assert hasattr(schul_Classroom, "name")
    descriptor = None
    for klass in schul_Classroom.__mro__:
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
schul_School_strategy = st.builds(
    schul_School,
    name=
        safe_text
)
schul_Diagram_strategy = st.builds(
    schul_Diagram,
)
schul_Student_strategy = st.builds(
    schul_Student,
    name=
        safe_text
)
schul_Classroom_strategy = st.builds(
    schul_Classroom,
    name=
        safe_text
)

@given(instance=schul_School_strategy)
@settings(max_examples=50)
def test_schul_school_instantiation(instance):
    assert isinstance(instance, schul_School)



@given(instance=schul_School_strategy)
def test_schul_school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=schul_Diagram_strategy)
@settings(max_examples=50)
def test_schul_diagram_instantiation(instance):
    assert isinstance(instance, schul_Diagram)

@given(instance=schul_Student_strategy)
@settings(max_examples=50)
def test_schul_student_instantiation(instance):
    assert isinstance(instance, schul_Student)



@given(instance=schul_Student_strategy)
def test_schul_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=schul_Classroom_strategy)
@settings(max_examples=50)
def test_schul_classroom_instantiation(instance):
    assert isinstance(instance, schul_Classroom)



@given(instance=schul_Classroom_strategy)
def test_schul_classroom_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
