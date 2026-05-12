import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    school_Book,
    school_Pupil,
    school_School,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_school_book_is_not_abstract():
    assert not inspect.isabstract(school_Book)


def test_school_book_constructor_exists():
    assert callable(school_Book.__init__)


def test_school_book_constructor_args():
    sig = inspect.signature(school_Book.__init__)
    params = list(sig.parameters.keys())



def test_school_pupil_is_not_abstract():
    assert not inspect.isabstract(school_Pupil)


def test_school_pupil_constructor_exists():
    assert callable(school_Pupil.__init__)


def test_school_pupil_constructor_args():
    sig = inspect.signature(school_Pupil.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_pupil_has_name():
    assert hasattr(school_Pupil, "name")
    descriptor = None
    for klass in school_Pupil.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school_school_is_not_abstract():
    assert not inspect.isabstract(school_School)


def test_school_school_constructor_exists():
    assert callable(school_School.__init__)


def test_school_school_constructor_args():
    sig = inspect.signature(school_School.__init__)
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
school_Book_strategy = st.builds(
    school_Book,
)
school_Pupil_strategy = st.builds(
    school_Pupil,
    name=
        safe_text
)
school_School_strategy = st.builds(
    school_School,
)

@given(instance=school_Book_strategy)
@settings(max_examples=50)
def test_school_book_instantiation(instance):
    assert isinstance(instance, school_Book)

@given(instance=school_Pupil_strategy)
@settings(max_examples=50)
def test_school_pupil_instantiation(instance):
    assert isinstance(instance, school_Pupil)



@given(instance=school_Pupil_strategy)
def test_school_pupil_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school_School_strategy)
@settings(max_examples=50)
def test_school_school_instantiation(instance):
    assert isinstance(instance, school_School)
