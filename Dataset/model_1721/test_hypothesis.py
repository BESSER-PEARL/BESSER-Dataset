import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    library::Library,
    library::Book,
    library::Author,
    Rating,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::library_is_not_abstract():
    assert not inspect.isabstract(library::Library)


def test_library::library_constructor_exists():
    assert callable(library::Library.__init__)


def test_library::library_constructor_args():
    sig = inspect.signature(library::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::library_has_name():
    assert hasattr(library::Library, "name")
    descriptor = None
    for klass in library::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::Book)


def test_library::book_constructor_exists():
    assert callable(library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::Book.__init__)
    params = list(sig.parameters.keys())
    assert "rating" in params, "Missing parameter 'rating'"
    assert "name" in params, "Missing parameter 'name'"

def test_library::book_has_rating():
    assert hasattr(library::Book, "rating")
    descriptor = None
    for klass in library::Book.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_name():
    assert hasattr(library::Book, "name")
    descriptor = None
    for klass in library::Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library::author_is_not_abstract():
    assert not inspect.isabstract(library::Author)


def test_library::author_constructor_exists():
    assert callable(library::Author.__init__)


def test_library::author_constructor_args():
    sig = inspect.signature(library::Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::author_has_name():
    assert hasattr(library::Author, "name")
    descriptor = None
    for klass in library::Author.__mro__:
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
        "GOOD",
        "NO_RATING",
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
library::Library_strategy = st.builds(
    library::Library,
    name=
        safe_text
)
library::Book_strategy = st.builds(
    library::Book,
    rating=
        safe_text,
    name=
        safe_text
)
library::Author_strategy = st.builds(
    library::Author,
    name=
        safe_text
)

@given(instance=library::Library_strategy)
@settings(max_examples=50)
def test_library::library_instantiation(instance):
    assert isinstance(instance, library::Library)

@given(instance=library::Library_strategy)
def test_library::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Library_strategy)
def test_library::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::Book)

@given(instance=library::Book_strategy)
def test_library::book_rating_type(instance):
    assert isinstance(instance.rating, str)


@given(instance=library::Book_strategy)
def test_library::book_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original

@given(instance=library::Book_strategy)
def test_library::book_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Book_strategy)
def test_library::book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library::Author_strategy)
@settings(max_examples=50)
def test_library::author_instantiation(instance):
    assert isinstance(instance, library::Author)

@given(instance=library::Author_strategy)
def test_library::author_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Author_strategy)
def test_library::author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
