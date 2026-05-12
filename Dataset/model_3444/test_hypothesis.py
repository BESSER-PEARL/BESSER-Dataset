import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    skol_School,
    skol_Diagram,
    skol_Student,
    skol_Classroom,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_skol_school_is_not_abstract():
    assert not inspect.isabstract(skol_School)


def test_skol_school_constructor_exists():
    assert callable(skol_School.__init__)


def test_skol_school_constructor_args():
    sig = inspect.signature(skol_School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_skol_school_has_name():
    assert hasattr(skol_School, "name")
    descriptor = None
    for klass in skol_School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_skol_diagram_is_not_abstract():
    assert not inspect.isabstract(skol_Diagram)


def test_skol_diagram_constructor_exists():
    assert callable(skol_Diagram.__init__)


def test_skol_diagram_constructor_args():
    sig = inspect.signature(skol_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_skol_student_is_not_abstract():
    assert not inspect.isabstract(skol_Student)


def test_skol_student_constructor_exists():
    assert callable(skol_Student.__init__)


def test_skol_student_constructor_args():
    sig = inspect.signature(skol_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_skol_student_has_name():
    assert hasattr(skol_Student, "name")
    descriptor = None
    for klass in skol_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_skol_classroom_is_not_abstract():
    assert not inspect.isabstract(skol_Classroom)


def test_skol_classroom_constructor_exists():
    assert callable(skol_Classroom.__init__)


def test_skol_classroom_constructor_args():
    sig = inspect.signature(skol_Classroom.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_skol_classroom_has_name():
    assert hasattr(skol_Classroom, "name")
    descriptor = None
    for klass in skol_Classroom.__mro__:
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
skol_School_strategy = st.builds(
    skol_School,
    name=
        safe_text
)
skol_Diagram_strategy = st.builds(
    skol_Diagram,
)
skol_Student_strategy = st.builds(
    skol_Student,
    name=
        safe_text
)
skol_Classroom_strategy = st.builds(
    skol_Classroom,
    name=
        safe_text
)

@given(instance=skol_School_strategy)
@settings(max_examples=50)
def test_skol_school_instantiation(instance):
    assert isinstance(instance, skol_School)



@given(instance=skol_School_strategy)
def test_skol_school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=skol_Diagram_strategy)
@settings(max_examples=50)
def test_skol_diagram_instantiation(instance):
    assert isinstance(instance, skol_Diagram)

@given(instance=skol_Student_strategy)
@settings(max_examples=50)
def test_skol_student_instantiation(instance):
    assert isinstance(instance, skol_Student)



@given(instance=skol_Student_strategy)
def test_skol_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=skol_Classroom_strategy)
@settings(max_examples=50)
def test_skol_classroom_instantiation(instance):
    assert isinstance(instance, skol_Classroom)



@given(instance=skol_Classroom_strategy)
def test_skol_classroom_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
