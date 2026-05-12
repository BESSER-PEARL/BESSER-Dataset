import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    library_Fiction,
    library_Library,
    library_NonFiction,
    library_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library_fiction_is_not_abstract():
    assert not inspect.isabstract(library_Fiction)


def test_library_fiction_constructor_exists():
    assert callable(library_Fiction.__init__)


def test_library_fiction_constructor_args():
    sig = inspect.signature(library_Fiction.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_library_fiction_has_Name():
    assert hasattr(library_Fiction, "Name")
    descriptor = None
    for klass in library_Fiction.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_library_library_is_not_abstract():
    assert not inspect.isabstract(library_Library)


def test_library_library_constructor_exists():
    assert callable(library_Library.__init__)


def test_library_library_constructor_args():
    sig = inspect.signature(library_Library.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_library_library_has_Name():
    assert hasattr(library_Library, "Name")
    descriptor = None
    for klass in library_Library.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_library_nonfiction_is_not_abstract():
    assert not inspect.isabstract(library_NonFiction)


def test_library_nonfiction_constructor_exists():
    assert callable(library_NonFiction.__init__)


def test_library_nonfiction_constructor_args():
    sig = inspect.signature(library_NonFiction.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_library_nonfiction_has_Name():
    assert hasattr(library_NonFiction, "Name")
    descriptor = None
    for klass in library_NonFiction.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_library_book_is_not_abstract():
    assert not inspect.isabstract(library_Book)


def test_library_book_constructor_exists():
    assert callable(library_Book.__init__)


def test_library_book_constructor_args():
    sig = inspect.signature(library_Book.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "genre" in params, "Missing parameter 'genre'"

def test_library_book_has_Name():
    assert hasattr(library_Book, "Name")
    descriptor = None
    for klass in library_Book.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_library_book_has_genre():
    assert hasattr(library_Book, "genre")
    descriptor = None
    for klass in library_Book.__mro__:
        if "genre" in klass.__dict__:
            descriptor = klass.__dict__["genre"]
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
library_Fiction_strategy = st.builds(
    library_Fiction,
    Name=
        safe_text
)
library_Library_strategy = st.builds(
    library_Library,
    Name=
        safe_text
)
library_NonFiction_strategy = st.builds(
    library_NonFiction,
    Name=
        safe_text
)
library_Book_strategy = st.builds(
    library_Book,
    Name=
        safe_text,
    genre=
        safe_text
)

@given(instance=library_Fiction_strategy)
@settings(max_examples=50)
def test_library_fiction_instantiation(instance):
    assert isinstance(instance, library_Fiction)



@given(instance=library_Fiction_strategy)
def test_library_fiction_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=library_Library_strategy)
@settings(max_examples=50)
def test_library_library_instantiation(instance):
    assert isinstance(instance, library_Library)



@given(instance=library_Library_strategy)
def test_library_library_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=library_NonFiction_strategy)
@settings(max_examples=50)
def test_library_nonfiction_instantiation(instance):
    assert isinstance(instance, library_NonFiction)



@given(instance=library_NonFiction_strategy)
def test_library_nonfiction_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=library_Book_strategy)
@settings(max_examples=50)
def test_library_book_instantiation(instance):
    assert isinstance(instance, library_Book)



@given(instance=library_Book_strategy)
def test_library_book_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=library_Book_strategy)
def test_library_book_genre_setter(instance):
    original = instance.genre
    instance.genre = original
    assert instance.genre == original
