import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    school::Book,
    school::Pupil,
    school::School,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_school::book_is_not_abstract():
    assert not inspect.isabstract(school::Book)


def test_school::book_constructor_exists():
    assert callable(school::Book.__init__)


def test_school::book_constructor_args():
    sig = inspect.signature(school::Book.__init__)
    params = list(sig.parameters.keys())



def test_school::pupil_is_not_abstract():
    assert not inspect.isabstract(school::Pupil)


def test_school::pupil_constructor_exists():
    assert callable(school::Pupil.__init__)


def test_school::pupil_constructor_args():
    sig = inspect.signature(school::Pupil.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school::pupil_has_name():
    assert hasattr(school::Pupil, "name")
    descriptor = None
    for klass in school::Pupil.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school::school_is_not_abstract():
    assert not inspect.isabstract(school::School)


def test_school::school_constructor_exists():
    assert callable(school::School.__init__)


def test_school::school_constructor_args():
    sig = inspect.signature(school::School.__init__)
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
school::Book_strategy = st.builds(
    school::Book,
)
school::Pupil_strategy = st.builds(
    school::Pupil,
    name=
        safe_text
)
school::School_strategy = st.builds(
    school::School,
)

@given(instance=school::Book_strategy)
@settings(max_examples=50)
def test_school::book_instantiation(instance):
    assert isinstance(instance, school::Book)

@given(instance=school::Pupil_strategy)
@settings(max_examples=50)
def test_school::pupil_instantiation(instance):
    assert isinstance(instance, school::Pupil)

@given(instance=school::Pupil_strategy)
def test_school::pupil_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Pupil_strategy)
def test_school::pupil_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::School_strategy)
@settings(max_examples=50)
def test_school::school_instantiation(instance):
    assert isinstance(instance, school::School)
