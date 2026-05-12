import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TUWien_Student,
    TUWien_Course,
    TUWien_University,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tuwien_student_is_not_abstract():
    assert not inspect.isabstract(TUWien_Student)


def test_tuwien_student_constructor_exists():
    assert callable(TUWien_Student.__init__)


def test_tuwien_student_constructor_args():
    sig = inspect.signature(TUWien_Student.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_tuwien_student_has_id():
    assert hasattr(TUWien_Student, "id")
    descriptor = None
    for klass in TUWien_Student.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_tuwien_student_has_name():
    assert hasattr(TUWien_Student, "name")
    descriptor = None
    for klass in TUWien_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tuwien_course_is_not_abstract():
    assert not inspect.isabstract(TUWien_Course)


def test_tuwien_course_constructor_exists():
    assert callable(TUWien_Course.__init__)


def test_tuwien_course_constructor_args():
    sig = inspect.signature(TUWien_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_tuwien_course_has_name():
    assert hasattr(TUWien_Course, "name")
    descriptor = None
    for klass in TUWien_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tuwien_course_has_id():
    assert hasattr(TUWien_Course, "id")
    descriptor = None
    for klass in TUWien_Course.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_tuwien_university_is_not_abstract():
    assert not inspect.isabstract(TUWien_University)


def test_tuwien_university_constructor_exists():
    assert callable(TUWien_University.__init__)


def test_tuwien_university_constructor_args():
    sig = inspect.signature(TUWien_University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tuwien_university_has_name():
    assert hasattr(TUWien_University, "name")
    descriptor = None
    for klass in TUWien_University.__mro__:
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
TUWien_Student_strategy = st.builds(
    TUWien_Student,
    id=
        st.integers(),
    name=
        safe_text
)
TUWien_Course_strategy = st.builds(
    TUWien_Course,
    name=
        safe_text,
    id=
        safe_text
)
TUWien_University_strategy = st.builds(
    TUWien_University,
    name=
        safe_text
)

@given(instance=TUWien_Student_strategy)
@settings(max_examples=50)
def test_tuwien_student_instantiation(instance):
    assert isinstance(instance, TUWien_Student)



@given(instance=TUWien_Student_strategy)
def test_tuwien_student_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=TUWien_Student_strategy)
def test_tuwien_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TUWien_Course_strategy)
@settings(max_examples=50)
def test_tuwien_course_instantiation(instance):
    assert isinstance(instance, TUWien_Course)



@given(instance=TUWien_Course_strategy)
def test_tuwien_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=TUWien_Course_strategy)
def test_tuwien_course_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=TUWien_University_strategy)
@settings(max_examples=50)
def test_tuwien_university_instantiation(instance):
    assert isinstance(instance, TUWien_University)



@given(instance=TUWien_University_strategy)
def test_tuwien_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
