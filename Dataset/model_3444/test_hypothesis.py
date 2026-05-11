import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    skol::School,
    skol::Diagram,
    skol::Student,
    skol::Classroom,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_skol::school_is_not_abstract():
    assert not inspect.isabstract(skol::School)


def test_skol::school_constructor_exists():
    assert callable(skol::School.__init__)


def test_skol::school_constructor_args():
    sig = inspect.signature(skol::School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_skol::school_has_name():
    assert hasattr(skol::School, "name")
    descriptor = None
    for klass in skol::School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_skol::diagram_is_not_abstract():
    assert not inspect.isabstract(skol::Diagram)


def test_skol::diagram_constructor_exists():
    assert callable(skol::Diagram.__init__)


def test_skol::diagram_constructor_args():
    sig = inspect.signature(skol::Diagram.__init__)
    params = list(sig.parameters.keys())



def test_skol::student_is_not_abstract():
    assert not inspect.isabstract(skol::Student)


def test_skol::student_constructor_exists():
    assert callable(skol::Student.__init__)


def test_skol::student_constructor_args():
    sig = inspect.signature(skol::Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_skol::student_has_name():
    assert hasattr(skol::Student, "name")
    descriptor = None
    for klass in skol::Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_skol::classroom_is_not_abstract():
    assert not inspect.isabstract(skol::Classroom)


def test_skol::classroom_constructor_exists():
    assert callable(skol::Classroom.__init__)


def test_skol::classroom_constructor_args():
    sig = inspect.signature(skol::Classroom.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_skol::classroom_has_name():
    assert hasattr(skol::Classroom, "name")
    descriptor = None
    for klass in skol::Classroom.__mro__:
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
skol::School_strategy = st.builds(
    skol::School,
    name=
        safe_text
)
skol::Diagram_strategy = st.builds(
    skol::Diagram,
)
skol::Student_strategy = st.builds(
    skol::Student,
    name=
        safe_text
)
skol::Classroom_strategy = st.builds(
    skol::Classroom,
    name=
        safe_text
)

@given(instance=skol::School_strategy)
@settings(max_examples=50)
def test_skol::school_instantiation(instance):
    assert isinstance(instance, skol::School)

@given(instance=skol::School_strategy)
def test_skol::school_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=skol::School_strategy)
def test_skol::school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=skol::Diagram_strategy)
@settings(max_examples=50)
def test_skol::diagram_instantiation(instance):
    assert isinstance(instance, skol::Diagram)

@given(instance=skol::Student_strategy)
@settings(max_examples=50)
def test_skol::student_instantiation(instance):
    assert isinstance(instance, skol::Student)

@given(instance=skol::Student_strategy)
def test_skol::student_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=skol::Student_strategy)
def test_skol::student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=skol::Classroom_strategy)
@settings(max_examples=50)
def test_skol::classroom_instantiation(instance):
    assert isinstance(instance, skol::Classroom)

@given(instance=skol::Classroom_strategy)
def test_skol::classroom_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=skol::Classroom_strategy)
def test_skol::classroom_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
