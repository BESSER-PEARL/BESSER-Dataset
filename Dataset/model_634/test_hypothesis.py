import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mm1_Book,
    mm1_Member,
    mm1_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mm1_book_is_not_abstract():
    assert not inspect.isabstract(mm1_Book)


def test_mm1_book_constructor_exists():
    assert callable(mm1_Book.__init__)


def test_mm1_book_constructor_args():
    sig = inspect.signature(mm1_Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm1_book_has_name():
    assert hasattr(mm1_Book, "name")
    descriptor = None
    for klass in mm1_Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm1_member_is_not_abstract():
    assert not inspect.isabstract(mm1_Member)


def test_mm1_member_constructor_exists():
    assert callable(mm1_Member.__init__)


def test_mm1_member_constructor_args():
    sig = inspect.signature(mm1_Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm1_member_has_name():
    assert hasattr(mm1_Member, "name")
    descriptor = None
    for klass in mm1_Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm1_library_is_not_abstract():
    assert not inspect.isabstract(mm1_Library)


def test_mm1_library_constructor_exists():
    assert callable(mm1_Library.__init__)


def test_mm1_library_constructor_args():
    sig = inspect.signature(mm1_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm1_library_has_name():
    assert hasattr(mm1_Library, "name")
    descriptor = None
    for klass in mm1_Library.__mro__:
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
mm1_Book_strategy = st.builds(
    mm1_Book,
    name=
        safe_text
)
mm1_Member_strategy = st.builds(
    mm1_Member,
    name=
        safe_text
)
mm1_Library_strategy = st.builds(
    mm1_Library,
    name=
        safe_text
)

@given(instance=mm1_Book_strategy)
@settings(max_examples=50)
def test_mm1_book_instantiation(instance):
    assert isinstance(instance, mm1_Book)



@given(instance=mm1_Book_strategy)
def test_mm1_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm1_Member_strategy)
@settings(max_examples=50)
def test_mm1_member_instantiation(instance):
    assert isinstance(instance, mm1_Member)



@given(instance=mm1_Member_strategy)
def test_mm1_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm1_Library_strategy)
@settings(max_examples=50)
def test_mm1_library_instantiation(instance):
    assert isinstance(instance, mm1_Library)



@given(instance=mm1_Library_strategy)
def test_mm1_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
