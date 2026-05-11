import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    university::Course,
    university::CourseCatalog,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_university::course_is_not_abstract():
    assert not inspect.isabstract(university::Course)


def test_university::course_constructor_exists():
    assert callable(university::Course.__init__)


def test_university::course_constructor_args():
    sig = inspect.signature(university::Course.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "etcs" in params, "Missing parameter 'etcs'"

def test_university::course_has_id():
    assert hasattr(university::Course, "id")
    descriptor = None
    for klass in university::Course.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_university::course_has_name():
    assert hasattr(university::Course, "name")
    descriptor = None
    for klass in university::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_university::course_has_etcs():
    assert hasattr(university::Course, "etcs")
    descriptor = None
    for klass in university::Course.__mro__:
        if "etcs" in klass.__dict__:
            descriptor = klass.__dict__["etcs"]
            break
    assert isinstance(descriptor, property)



def test_university::coursecatalog_is_not_abstract():
    assert not inspect.isabstract(university::CourseCatalog)


def test_university::coursecatalog_constructor_exists():
    assert callable(university::CourseCatalog.__init__)


def test_university::coursecatalog_constructor_args():
    sig = inspect.signature(university::CourseCatalog.__init__)
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
university::Course_strategy = st.builds(
    university::Course,
    id=
        safe_text,
    name=
        safe_text,
    etcs=
        st.integers()
)
university::CourseCatalog_strategy = st.builds(
    university::CourseCatalog,
)

@given(instance=university::Course_strategy)
@settings(max_examples=50)
def test_university::course_instantiation(instance):
    assert isinstance(instance, university::Course)

@given(instance=university::Course_strategy)
def test_university::course_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=university::Course_strategy)
def test_university::course_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=university::Course_strategy)
def test_university::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=university::Course_strategy)
def test_university::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university::Course_strategy)
def test_university::course_etcs_type(instance):
    assert isinstance(instance.etcs, int)


@given(instance=university::Course_strategy)
def test_university::course_etcs_setter(instance):
    original = instance.etcs
    instance.etcs = original
    assert instance.etcs == original

@given(instance=university::CourseCatalog_strategy)
@settings(max_examples=50)
def test_university::coursecatalog_instantiation(instance):
    assert isinstance(instance, university::CourseCatalog)
