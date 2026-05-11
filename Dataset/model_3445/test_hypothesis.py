import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    schul::School,
    schul::Diagram,
    schul::Student,
    schul::Classroom,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_schul::school_is_not_abstract():
    assert not inspect.isabstract(schul::School)


def test_schul::school_constructor_exists():
    assert callable(schul::School.__init__)


def test_schul::school_constructor_args():
    sig = inspect.signature(schul::School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_schul::school_has_name():
    assert hasattr(schul::School, "name")
    descriptor = None
    for klass in schul::School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_schul::diagram_is_not_abstract():
    assert not inspect.isabstract(schul::Diagram)


def test_schul::diagram_constructor_exists():
    assert callable(schul::Diagram.__init__)


def test_schul::diagram_constructor_args():
    sig = inspect.signature(schul::Diagram.__init__)
    params = list(sig.parameters.keys())



def test_schul::student_is_not_abstract():
    assert not inspect.isabstract(schul::Student)


def test_schul::student_constructor_exists():
    assert callable(schul::Student.__init__)


def test_schul::student_constructor_args():
    sig = inspect.signature(schul::Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_schul::student_has_name():
    assert hasattr(schul::Student, "name")
    descriptor = None
    for klass in schul::Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_schul::classroom_is_not_abstract():
    assert not inspect.isabstract(schul::Classroom)


def test_schul::classroom_constructor_exists():
    assert callable(schul::Classroom.__init__)


def test_schul::classroom_constructor_args():
    sig = inspect.signature(schul::Classroom.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_schul::classroom_has_name():
    assert hasattr(schul::Classroom, "name")
    descriptor = None
    for klass in schul::Classroom.__mro__:
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
schul::School_strategy = st.builds(
    schul::School,
    name=
        safe_text
)
schul::Diagram_strategy = st.builds(
    schul::Diagram,
)
schul::Student_strategy = st.builds(
    schul::Student,
    name=
        safe_text
)
schul::Classroom_strategy = st.builds(
    schul::Classroom,
    name=
        safe_text
)

@given(instance=schul::School_strategy)
@settings(max_examples=50)
def test_schul::school_instantiation(instance):
    assert isinstance(instance, schul::School)

@given(instance=schul::School_strategy)
def test_schul::school_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=schul::School_strategy)
def test_schul::school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=schul::Diagram_strategy)
@settings(max_examples=50)
def test_schul::diagram_instantiation(instance):
    assert isinstance(instance, schul::Diagram)

@given(instance=schul::Student_strategy)
@settings(max_examples=50)
def test_schul::student_instantiation(instance):
    assert isinstance(instance, schul::Student)

@given(instance=schul::Student_strategy)
def test_schul::student_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=schul::Student_strategy)
def test_schul::student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=schul::Classroom_strategy)
@settings(max_examples=50)
def test_schul::classroom_instantiation(instance):
    assert isinstance(instance, schul::Classroom)

@given(instance=schul::Classroom_strategy)
def test_schul::classroom_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=schul::Classroom_strategy)
def test_schul::classroom_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
