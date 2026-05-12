import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    library_Library,
    library_Book,
    library_Author,
    Rating,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library_library_is_not_abstract():
    assert not inspect.isabstract(library_Library)


def test_library_library_constructor_exists():
    assert callable(library_Library.__init__)


def test_library_library_constructor_args():
    sig = inspect.signature(library_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library_library_has_name():
    assert hasattr(library_Library, "name")
    descriptor = None
    for klass in library_Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library_book_is_not_abstract():
    assert not inspect.isabstract(library_Book)


def test_library_book_constructor_exists():
    assert callable(library_Book.__init__)


def test_library_book_constructor_args():
    sig = inspect.signature(library_Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "rating" in params, "Missing parameter 'rating'"

def test_library_book_has_name():
    assert hasattr(library_Book, "name")
    descriptor = None
    for klass in library_Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_library_book_has_rating():
    assert hasattr(library_Book, "rating")
    descriptor = None
    for klass in library_Book.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)



def test_library_author_is_not_abstract():
    assert not inspect.isabstract(library_Author)


def test_library_author_constructor_exists():
    assert callable(library_Author.__init__)


def test_library_author_constructor_args():
    sig = inspect.signature(library_Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library_author_has_name():
    assert hasattr(library_Author, "name")
    descriptor = None
    for klass in library_Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rating_exists():
    # Check that the Enumeration exists
    assert Rating is not None

def test_rating_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Rating]
    expected_literals = [
        "NO_RATING",
        "GOOD",
        "BAD",
        "MEDIUM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Rating"


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
library_Library_strategy = st.builds(
    library_Library,
    name=
        safe_text
)
library_Book_strategy = st.builds(
    library_Book,
    name=
        safe_text,
    rating=
        safe_text
)
library_Author_strategy = st.builds(
    library_Author,
    name=
        safe_text
)

@given(instance=library_Library_strategy)
@settings(max_examples=50)
def test_library_library_instantiation(instance):
    assert isinstance(instance, library_Library)



@given(instance=library_Library_strategy)
def test_library_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library_Book_strategy)
@settings(max_examples=50)
def test_library_book_instantiation(instance):
    assert isinstance(instance, library_Book)



@given(instance=library_Book_strategy)
def test_library_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=library_Book_strategy)
def test_library_book_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original

@given(instance=library_Author_strategy)
@settings(max_examples=50)
def test_library_author_instantiation(instance):
    assert isinstance(instance, library_Author)



@given(instance=library_Author_strategy)
def test_library_author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
