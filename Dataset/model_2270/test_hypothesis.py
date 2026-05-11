import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    university::University,
    university::Professor,
    university::Course,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_university::university_is_not_abstract():
    assert not inspect.isabstract(university::University)


def test_university::university_constructor_exists():
    assert callable(university::University.__init__)


def test_university::university_constructor_args():
    sig = inspect.signature(university::University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_university::university_has_name():
    assert hasattr(university::University, "name")
    descriptor = None
    for klass in university::University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university::professor_is_not_abstract():
    assert not inspect.isabstract(university::Professor)


def test_university::professor_constructor_exists():
    assert callable(university::Professor.__init__)


def test_university::professor_constructor_args():
    sig = inspect.signature(university::Professor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_university::professor_has_name():
    assert hasattr(university::Professor, "name")
    descriptor = None
    for klass in university::Professor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university::course_is_not_abstract():
    assert not inspect.isabstract(university::Course)


def test_university::course_constructor_exists():
    assert callable(university::Course.__init__)


def test_university::course_constructor_args():
    sig = inspect.signature(university::Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_university::course_has_name():
    assert hasattr(university::Course, "name")
    descriptor = None
    for klass in university::Course.__mro__:
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
university::University_strategy = st.builds(
    university::University,
    name=
        safe_text
)
university::Professor_strategy = st.builds(
    university::Professor,
    name=
        safe_text
)
university::Course_strategy = st.builds(
    university::Course,
    name=
        safe_text
)

@given(instance=university::University_strategy)
@settings(max_examples=50)
def test_university::university_instantiation(instance):
    assert isinstance(instance, university::University)

@given(instance=university::University_strategy)
def test_university::university_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=university::University_strategy)
def test_university::university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university::Professor_strategy)
@settings(max_examples=50)
def test_university::professor_instantiation(instance):
    assert isinstance(instance, university::Professor)

@given(instance=university::Professor_strategy)
def test_university::professor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=university::Professor_strategy)
def test_university::professor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university::Course_strategy)
@settings(max_examples=50)
def test_university::course_instantiation(instance):
    assert isinstance(instance, university::Course)

@given(instance=university::Course_strategy)
def test_university::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=university::Course_strategy)
def test_university::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
