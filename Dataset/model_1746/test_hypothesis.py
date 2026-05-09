import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    LibraryContent,
    library::Magazine,
    library::Book,
    library::LibraryContent,
    library::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_librarycontent_is_not_abstract():
    assert not inspect.isabstract(LibraryContent)


def test_librarycontent_constructor_exists():
    assert callable(LibraryContent.__init__)


def test_librarycontent_constructor_args():
    sig = inspect.signature(LibraryContent.__init__)
    params = list(sig.parameters.keys())



def test_library::magazine_is_not_abstract():
    assert not inspect.isabstract(library::Magazine)


def test_library::magazine_constructor_exists():
    assert callable(library::Magazine.__init__)


def test_library::magazine_constructor_args():
    sig = inspect.signature(library::Magazine.__init__)
    params = list(sig.parameters.keys())



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::Book)


def test_library::book_constructor_exists():
    assert callable(library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::Book.__init__)
    params = list(sig.parameters.keys())



def test_library::librarycontent_is_not_abstract():
    assert not inspect.isabstract(library::LibraryContent)


def test_library::librarycontent_constructor_exists():
    assert callable(library::LibraryContent.__init__)


def test_library::librarycontent_constructor_args():
    sig = inspect.signature(library::LibraryContent.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "name" in params, "Missing parameter 'name'"

def test_library::librarycontent_has_author():
    assert hasattr(library::LibraryContent, "author")
    descriptor = None
    for klass in library::LibraryContent.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_library::librarycontent_has_name():
    assert hasattr(library::LibraryContent, "name")
    descriptor = None
    for klass in library::LibraryContent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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
LibraryContent_strategy = st.builds(
    LibraryContent,
)
library::Magazine_strategy = st.builds(
    library::Magazine,
)
library::Book_strategy = st.builds(
    library::Book,
)
library::LibraryContent_strategy = st.builds(
    library::LibraryContent,
    author=
        safe_text,
    name=
        safe_text
)
library::Library_strategy = st.builds(
    library::Library,
    name=
        safe_text
)

@given(instance=LibraryContent_strategy)
@settings(max_examples=50)
def test_librarycontent_instantiation(instance):
    assert isinstance(instance, LibraryContent)

@given(instance=library::Magazine_strategy)
@settings(max_examples=50)
def test_library::magazine_instantiation(instance):
    assert isinstance(instance, library::Magazine)

@given(instance=library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::Book)

@given(instance=library::LibraryContent_strategy)
@settings(max_examples=50)
def test_library::librarycontent_instantiation(instance):
    assert isinstance(instance, library::LibraryContent)

@given(instance=library::LibraryContent_strategy)
def test_library::librarycontent_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=library::LibraryContent_strategy)
def test_library::librarycontent_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=library::LibraryContent_strategy)
def test_library::librarycontent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::LibraryContent_strategy)
def test_library::librarycontent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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
