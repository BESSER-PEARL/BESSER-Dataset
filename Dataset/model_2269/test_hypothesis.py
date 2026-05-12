import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    university_Course,
    university_CourseCatalog,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_university_course_is_not_abstract():
    assert not inspect.isabstract(university_Course)


def test_university_course_constructor_exists():
    assert callable(university_Course.__init__)


def test_university_course_constructor_args():
    sig = inspect.signature(university_Course.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "etcs" in params, "Missing parameter 'etcs'"

def test_university_course_has_id():
    assert hasattr(university_Course, "id")
    descriptor = None
    for klass in university_Course.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_university_course_has_name():
    assert hasattr(university_Course, "name")
    descriptor = None
    for klass in university_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_university_course_has_etcs():
    assert hasattr(university_Course, "etcs")
    descriptor = None
    for klass in university_Course.__mro__:
        if "etcs" in klass.__dict__:
            descriptor = klass.__dict__["etcs"]
            break
    assert isinstance(descriptor, property)



def test_university_coursecatalog_is_not_abstract():
    assert not inspect.isabstract(university_CourseCatalog)


def test_university_coursecatalog_constructor_exists():
    assert callable(university_CourseCatalog.__init__)


def test_university_coursecatalog_constructor_args():
    sig = inspect.signature(university_CourseCatalog.__init__)
    params = list(sig.parameters.keys())


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
university_Course_strategy = st.builds(
    university_Course,
    id=
        safe_text,
    name=
        safe_text,
    etcs=
        st.integers()
)
university_CourseCatalog_strategy = st.builds(
    university_CourseCatalog,
)

@given(instance=university_Course_strategy)
@settings(max_examples=50)
def test_university_course_instantiation(instance):
    assert isinstance(instance, university_Course)



@given(instance=university_Course_strategy)
def test_university_course_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=university_Course_strategy)
def test_university_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=university_Course_strategy)
def test_university_course_etcs_setter(instance):
    original = instance.etcs
    instance.etcs = original
    assert instance.etcs == original

@given(instance=university_CourseCatalog_strategy)
@settings(max_examples=50)
def test_university_coursecatalog_instantiation(instance):
    assert isinstance(instance, university_CourseCatalog)
