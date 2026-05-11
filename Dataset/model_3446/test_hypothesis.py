import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    schol::School,
    schol::Diagram,
    schol::Student,
    schol::Classroom,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_schol::school_is_not_abstract():
    assert not inspect.isabstract(schol::School)


def test_schol::school_constructor_exists():
    assert callable(schol::School.__init__)


def test_schol::school_constructor_args():
    sig = inspect.signature(schol::School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_schol::school_has_name():
    assert hasattr(schol::School, "name")
    descriptor = None
    for klass in schol::School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_schol::diagram_is_not_abstract():
    assert not inspect.isabstract(schol::Diagram)


def test_schol::diagram_constructor_exists():
    assert callable(schol::Diagram.__init__)


def test_schol::diagram_constructor_args():
    sig = inspect.signature(schol::Diagram.__init__)
    params = list(sig.parameters.keys())



def test_schol::student_is_not_abstract():
    assert not inspect.isabstract(schol::Student)


def test_schol::student_constructor_exists():
    assert callable(schol::Student.__init__)


def test_schol::student_constructor_args():
    sig = inspect.signature(schol::Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_schol::student_has_name():
    assert hasattr(schol::Student, "name")
    descriptor = None
    for klass in schol::Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_schol::classroom_is_not_abstract():
    assert not inspect.isabstract(schol::Classroom)


def test_schol::classroom_constructor_exists():
    assert callable(schol::Classroom.__init__)


def test_schol::classroom_constructor_args():
    sig = inspect.signature(schol::Classroom.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_schol::classroom_has_name():
    assert hasattr(schol::Classroom, "name")
    descriptor = None
    for klass in schol::Classroom.__mro__:
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
schol::School_strategy = st.builds(
    schol::School,
    name=
        safe_text
)
schol::Diagram_strategy = st.builds(
    schol::Diagram,
)
schol::Student_strategy = st.builds(
    schol::Student,
    name=
        safe_text
)
schol::Classroom_strategy = st.builds(
    schol::Classroom,
    name=
        safe_text
)

@given(instance=schol::School_strategy)
@settings(max_examples=50)
def test_schol::school_instantiation(instance):
    assert isinstance(instance, schol::School)

@given(instance=schol::School_strategy)
def test_schol::school_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=schol::School_strategy)
def test_schol::school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=schol::Diagram_strategy)
@settings(max_examples=50)
def test_schol::diagram_instantiation(instance):
    assert isinstance(instance, schol::Diagram)

@given(instance=schol::Student_strategy)
@settings(max_examples=50)
def test_schol::student_instantiation(instance):
    assert isinstance(instance, schol::Student)

@given(instance=schol::Student_strategy)
def test_schol::student_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=schol::Student_strategy)
def test_schol::student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=schol::Classroom_strategy)
@settings(max_examples=50)
def test_schol::classroom_instantiation(instance):
    assert isinstance(instance, schol::Classroom)

@given(instance=schol::Classroom_strategy)
def test_schol::classroom_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=schol::Classroom_strategy)
def test_schol::classroom_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
