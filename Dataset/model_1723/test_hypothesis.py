import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    library::Fiction,
    library::Library,
    library::NonFiction,
    library::Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::fiction_is_not_abstract():
    assert not inspect.isabstract(library::Fiction)


def test_library::fiction_constructor_exists():
    assert callable(library::Fiction.__init__)


def test_library::fiction_constructor_args():
    sig = inspect.signature(library::Fiction.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_library::fiction_has_Name():
    assert hasattr(library::Fiction, "Name")
    descriptor = None
    for klass in library::Fiction.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_library::library_is_not_abstract():
    assert not inspect.isabstract(library::Library)


def test_library::library_constructor_exists():
    assert callable(library::Library.__init__)


def test_library::library_constructor_args():
    sig = inspect.signature(library::Library.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_library::library_has_Name():
    assert hasattr(library::Library, "Name")
    descriptor = None
    for klass in library::Library.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_library::nonfiction_is_not_abstract():
    assert not inspect.isabstract(library::NonFiction)


def test_library::nonfiction_constructor_exists():
    assert callable(library::NonFiction.__init__)


def test_library::nonfiction_constructor_args():
    sig = inspect.signature(library::NonFiction.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_library::nonfiction_has_Name():
    assert hasattr(library::NonFiction, "Name")
    descriptor = None
    for klass in library::NonFiction.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::Book)


def test_library::book_constructor_exists():
    assert callable(library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::Book.__init__)
    params = list(sig.parameters.keys())
    assert "genre" in params, "Missing parameter 'genre'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_library::book_has_genre():
    assert hasattr(library::Book, "genre")
    descriptor = None
    for klass in library::Book.__mro__:
        if "genre" in klass.__dict__:
            descriptor = klass.__dict__["genre"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_Name():
    assert hasattr(library::Book, "Name")
    descriptor = None
    for klass in library::Book.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
library::Fiction_strategy = st.builds(
    library::Fiction,
    Name=
        safe_text
)
library::Library_strategy = st.builds(
    library::Library,
    Name=
        safe_text
)
library::NonFiction_strategy = st.builds(
    library::NonFiction,
    Name=
        safe_text
)
library::Book_strategy = st.builds(
    library::Book,
    genre=
        safe_text,
    Name=
        safe_text
)

@given(instance=library::Fiction_strategy)
@settings(max_examples=50)
def test_library::fiction_instantiation(instance):
    assert isinstance(instance, library::Fiction)

@given(instance=library::Fiction_strategy)
def test_library::fiction_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=library::Fiction_strategy)
def test_library::fiction_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=library::Library_strategy)
@settings(max_examples=50)
def test_library::library_instantiation(instance):
    assert isinstance(instance, library::Library)

@given(instance=library::Library_strategy)
def test_library::library_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=library::Library_strategy)
def test_library::library_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=library::NonFiction_strategy)
@settings(max_examples=50)
def test_library::nonfiction_instantiation(instance):
    assert isinstance(instance, library::NonFiction)

@given(instance=library::NonFiction_strategy)
def test_library::nonfiction_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=library::NonFiction_strategy)
def test_library::nonfiction_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::Book)

@given(instance=library::Book_strategy)
def test_library::book_genre_type(instance):
    assert isinstance(instance.genre, str)


@given(instance=library::Book_strategy)
def test_library::book_genre_setter(instance):
    original = instance.genre
    instance.genre = original
    assert instance.genre == original

@given(instance=library::Book_strategy)
def test_library::book_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=library::Book_strategy)
def test_library::book_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
