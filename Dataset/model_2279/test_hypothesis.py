import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    lMS_Course,
    lMS_LMS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lms_course_is_not_abstract():
    assert not inspect.isabstract(lMS_Course)


def test_lms_course_constructor_exists():
    assert callable(lMS_Course.__init__)


def test_lms_course_constructor_args():
    sig = inspect.signature(lMS_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lms_course_has_name():
    assert hasattr(lMS_Course, "name")
    descriptor = None
    for klass in lMS_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lms_lms_is_not_abstract():
    assert not inspect.isabstract(lMS_LMS)


def test_lms_lms_constructor_exists():
    assert callable(lMS_LMS.__init__)


def test_lms_lms_constructor_args():
    sig = inspect.signature(lMS_LMS.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_lms_lms_has_description():
    assert hasattr(lMS_LMS, "description")
    descriptor = None
    for klass in lMS_LMS.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
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
lMS_Course_strategy = st.builds(
    lMS_Course,
    name=
        safe_text
)
lMS_LMS_strategy = st.builds(
    lMS_LMS,
    description=
        safe_text
)

@given(instance=lMS_Course_strategy)
@settings(max_examples=50)
def test_lms_course_instantiation(instance):
    assert isinstance(instance, lMS_Course)



@given(instance=lMS_Course_strategy)
def test_lms_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lMS_LMS_strategy)
@settings(max_examples=50)
def test_lms_lms_instantiation(instance):
    assert isinstance(instance, lMS_LMS)



@given(instance=lMS_LMS_strategy)
def test_lms_lms_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
