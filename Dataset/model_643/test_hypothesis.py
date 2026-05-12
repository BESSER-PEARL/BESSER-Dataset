import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mm3_Film,
    mm3_Book,
    mm3_Member,
    mm3_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mm3_film_is_not_abstract():
    assert not inspect.isabstract(mm3_Film)


def test_mm3_film_constructor_exists():
    assert callable(mm3_Film.__init__)


def test_mm3_film_constructor_args():
    sig = inspect.signature(mm3_Film.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm3_film_has_name():
    assert hasattr(mm3_Film, "name")
    descriptor = None
    for klass in mm3_Film.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm3_book_is_not_abstract():
    assert not inspect.isabstract(mm3_Book)


def test_mm3_book_constructor_exists():
    assert callable(mm3_Book.__init__)


def test_mm3_book_constructor_args():
    sig = inspect.signature(mm3_Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm3_book_has_name():
    assert hasattr(mm3_Book, "name")
    descriptor = None
    for klass in mm3_Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm3_member_is_not_abstract():
    assert not inspect.isabstract(mm3_Member)


def test_mm3_member_constructor_exists():
    assert callable(mm3_Member.__init__)


def test_mm3_member_constructor_args():
    sig = inspect.signature(mm3_Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm3_member_has_name():
    assert hasattr(mm3_Member, "name")
    descriptor = None
    for klass in mm3_Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm3_library_is_not_abstract():
    assert not inspect.isabstract(mm3_Library)


def test_mm3_library_constructor_exists():
    assert callable(mm3_Library.__init__)


def test_mm3_library_constructor_args():
    sig = inspect.signature(mm3_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm3_library_has_name():
    assert hasattr(mm3_Library, "name")
    descriptor = None
    for klass in mm3_Library.__mro__:
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
mm3_Film_strategy = st.builds(
    mm3_Film,
    name=
        safe_text
)
mm3_Book_strategy = st.builds(
    mm3_Book,
    name=
        safe_text
)
mm3_Member_strategy = st.builds(
    mm3_Member,
    name=
        safe_text
)
mm3_Library_strategy = st.builds(
    mm3_Library,
    name=
        safe_text
)

@given(instance=mm3_Film_strategy)
@settings(max_examples=50)
def test_mm3_film_instantiation(instance):
    assert isinstance(instance, mm3_Film)



@given(instance=mm3_Film_strategy)
def test_mm3_film_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm3_Book_strategy)
@settings(max_examples=50)
def test_mm3_book_instantiation(instance):
    assert isinstance(instance, mm3_Book)



@given(instance=mm3_Book_strategy)
def test_mm3_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm3_Member_strategy)
@settings(max_examples=50)
def test_mm3_member_instantiation(instance):
    assert isinstance(instance, mm3_Member)



@given(instance=mm3_Member_strategy)
def test_mm3_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm3_Library_strategy)
@settings(max_examples=50)
def test_mm3_library_instantiation(instance):
    assert isinstance(instance, mm3_Library)



@given(instance=mm3_Library_strategy)
def test_mm3_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
