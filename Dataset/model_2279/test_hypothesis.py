import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    lMS::Course,
    lMS::LMS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lms::course_is_not_abstract():
    assert not inspect.isabstract(lMS::Course)


def test_lms::course_constructor_exists():
    assert callable(lMS::Course.__init__)


def test_lms::course_constructor_args():
    sig = inspect.signature(lMS::Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lms::course_has_name():
    assert hasattr(lMS::Course, "name")
    descriptor = None
    for klass in lMS::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lms::lms_is_not_abstract():
    assert not inspect.isabstract(lMS::LMS)


def test_lms::lms_constructor_exists():
    assert callable(lMS::LMS.__init__)


def test_lms::lms_constructor_args():
    sig = inspect.signature(lMS::LMS.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_lms::lms_has_description():
    assert hasattr(lMS::LMS, "description")
    descriptor = None
    for klass in lMS::LMS.__mro__:
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
lMS::Course_strategy = st.builds(
    lMS::Course,
    name=
        safe_text
)
lMS::LMS_strategy = st.builds(
    lMS::LMS,
    description=
        safe_text
)

@given(instance=lMS::Course_strategy)
@settings(max_examples=50)
def test_lms::course_instantiation(instance):
    assert isinstance(instance, lMS::Course)

@given(instance=lMS::Course_strategy)
def test_lms::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lMS::Course_strategy)
def test_lms::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lMS::LMS_strategy)
@settings(max_examples=50)
def test_lms::lms_instantiation(instance):
    assert isinstance(instance, lMS::LMS)

@given(instance=lMS::LMS_strategy)
def test_lms::lms_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=lMS::LMS_strategy)
def test_lms::lms_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
