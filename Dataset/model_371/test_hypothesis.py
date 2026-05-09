import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    library::Shelf,
    library::Employee,
    library::Book,
    library::Author,
    library::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::shelf_is_not_abstract():
    assert not inspect.isabstract(library::Shelf)


def test_library::shelf_constructor_exists():
    assert callable(library::Shelf.__init__)


def test_library::shelf_constructor_args():
    sig = inspect.signature(library::Shelf.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::shelf_has_name():
    assert hasattr(library::Shelf, "name")
    descriptor = None
    for klass in library::Shelf.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library::employee_is_not_abstract():
    assert not inspect.isabstract(library::Employee)


def test_library::employee_constructor_exists():
    assert callable(library::Employee.__init__)


def test_library::employee_constructor_args():
    sig = inspect.signature(library::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::employee_has_name():
    assert hasattr(library::Employee, "name")
    descriptor = None
    for klass in library::Employee.__mro__:
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
    assert "title" in params, "Missing parameter 'title'"

def test_library::book_has_title():
    assert hasattr(library::Book, "title")
    descriptor = None
    for klass in library::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
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
library::Shelf_strategy = st.builds(
    library::Shelf,
    name=
        safe_text
)
library::Employee_strategy = st.builds(
    library::Employee,
    name=
        safe_text
)
library::Book_strategy = st.builds(
    library::Book,
    title=
        safe_text
)
library::Author_strategy = st.builds(
    library::Author,
    name=
        safe_text
)
library::Library_strategy = st.builds(
    library::Library,
    name=
        safe_text
)

@given(instance=library::Shelf_strategy)
@settings(max_examples=50)
def test_library::shelf_instantiation(instance):
    assert isinstance(instance, library::Shelf)

@given(instance=library::Shelf_strategy)
def test_library::shelf_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Shelf_strategy)
def test_library::shelf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library::Employee_strategy)
@settings(max_examples=50)
def test_library::employee_instantiation(instance):
    assert isinstance(instance, library::Employee)

@given(instance=library::Employee_strategy)
def test_library::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Employee_strategy)
def test_library::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::Book)

@given(instance=library::Book_strategy)
def test_library::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::Book_strategy)
def test_library::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

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
