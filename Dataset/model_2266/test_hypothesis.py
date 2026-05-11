import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TUWien::Student,
    TUWien::Course,
    TUWien::University,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tuwien::student_is_not_abstract():
    assert not inspect.isabstract(TUWien::Student)


def test_tuwien::student_constructor_exists():
    assert callable(TUWien::Student.__init__)


def test_tuwien::student_constructor_args():
    sig = inspect.signature(TUWien::Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_tuwien::student_has_name():
    assert hasattr(TUWien::Student, "name")
    descriptor = None
    for klass in TUWien::Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tuwien::student_has_id():
    assert hasattr(TUWien::Student, "id")
    descriptor = None
    for klass in TUWien::Student.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_tuwien::course_is_not_abstract():
    assert not inspect.isabstract(TUWien::Course)


def test_tuwien::course_constructor_exists():
    assert callable(TUWien::Course.__init__)


def test_tuwien::course_constructor_args():
    sig = inspect.signature(TUWien::Course.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_tuwien::course_has_id():
    assert hasattr(TUWien::Course, "id")
    descriptor = None
    for klass in TUWien::Course.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_tuwien::course_has_name():
    assert hasattr(TUWien::Course, "name")
    descriptor = None
    for klass in TUWien::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tuwien::university_is_not_abstract():
    assert not inspect.isabstract(TUWien::University)


def test_tuwien::university_constructor_exists():
    assert callable(TUWien::University.__init__)


def test_tuwien::university_constructor_args():
    sig = inspect.signature(TUWien::University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tuwien::university_has_name():
    assert hasattr(TUWien::University, "name")
    descriptor = None
    for klass in TUWien::University.__mro__:
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
TUWien::Student_strategy = st.builds(
    TUWien::Student,
    name=
        safe_text,
    id=
        st.integers()
)
TUWien::Course_strategy = st.builds(
    TUWien::Course,
    id=
        safe_text,
    name=
        safe_text
)
TUWien::University_strategy = st.builds(
    TUWien::University,
    name=
        safe_text
)

@given(instance=TUWien::Student_strategy)
@settings(max_examples=50)
def test_tuwien::student_instantiation(instance):
    assert isinstance(instance, TUWien::Student)

@given(instance=TUWien::Student_strategy)
def test_tuwien::student_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TUWien::Student_strategy)
def test_tuwien::student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TUWien::Student_strategy)
def test_tuwien::student_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=TUWien::Student_strategy)
def test_tuwien::student_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=TUWien::Course_strategy)
@settings(max_examples=50)
def test_tuwien::course_instantiation(instance):
    assert isinstance(instance, TUWien::Course)

@given(instance=TUWien::Course_strategy)
def test_tuwien::course_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=TUWien::Course_strategy)
def test_tuwien::course_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=TUWien::Course_strategy)
def test_tuwien::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TUWien::Course_strategy)
def test_tuwien::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TUWien::University_strategy)
@settings(max_examples=50)
def test_tuwien::university_instantiation(instance):
    assert isinstance(instance, TUWien::University)

@given(instance=TUWien::University_strategy)
def test_tuwien::university_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TUWien::University_strategy)
def test_tuwien::university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
