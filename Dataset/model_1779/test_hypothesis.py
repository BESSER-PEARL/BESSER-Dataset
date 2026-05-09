import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Books::Chapter,
    Books::Author,
    Books::Book,
    Books::System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_books::chapter_is_not_abstract():
    assert not inspect.isabstract(Books::Chapter)


def test_books::chapter_constructor_exists():
    assert callable(Books::Chapter.__init__)


def test_books::chapter_constructor_args():
    sig = inspect.signature(Books::Chapter.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_books::chapter_has_title():
    assert hasattr(Books::Chapter, "title")
    descriptor = None
    for klass in Books::Chapter.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_books::author_is_not_abstract():
    assert not inspect.isabstract(Books::Author)


def test_books::author_constructor_exists():
    assert callable(Books::Author.__init__)


def test_books::author_constructor_args():
    sig = inspect.signature(Books::Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_books::author_has_name():
    assert hasattr(Books::Author, "name")
    descriptor = None
    for klass in Books::Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_books::book_is_not_abstract():
    assert not inspect.isabstract(Books::Book)


def test_books::book_constructor_exists():
    assert callable(Books::Book.__init__)


def test_books::book_constructor_args():
    sig = inspect.signature(Books::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "collecName" in params, "Missing parameter 'collecName'"

def test_books::book_has_title():
    assert hasattr(Books::Book, "title")
    descriptor = None
    for klass in Books::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_books::book_has_collecName():
    assert hasattr(Books::Book, "collecName")
    descriptor = None
    for klass in Books::Book.__mro__:
        if "collecName" in klass.__dict__:
            descriptor = klass.__dict__["collecName"]
            break
    assert isinstance(descriptor, property)



def test_books::system_is_not_abstract():
    assert not inspect.isabstract(Books::System)


def test_books::system_constructor_exists():
    assert callable(Books::System.__init__)


def test_books::system_constructor_args():
    sig = inspect.signature(Books::System.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_books::system_has_name():
    assert hasattr(Books::System, "name")
    descriptor = None
    for klass in Books::System.__mro__:
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
Books::Chapter_strategy = st.builds(
    Books::Chapter,
    title=
        safe_text
)
Books::Author_strategy = st.builds(
    Books::Author,
    name=
        safe_text
)
Books::Book_strategy = st.builds(
    Books::Book,
    title=
        safe_text,
    collecName=
        safe_text
)
Books::System_strategy = st.builds(
    Books::System,
    name=
        safe_text
)

@given(instance=Books::Chapter_strategy)
@settings(max_examples=50)
def test_books::chapter_instantiation(instance):
    assert isinstance(instance, Books::Chapter)

@given(instance=Books::Chapter_strategy)
def test_books::chapter_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Books::Chapter_strategy)
def test_books::chapter_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Books::Author_strategy)
@settings(max_examples=50)
def test_books::author_instantiation(instance):
    assert isinstance(instance, Books::Author)

@given(instance=Books::Author_strategy)
def test_books::author_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Books::Author_strategy)
def test_books::author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Books::Book_strategy)
@settings(max_examples=50)
def test_books::book_instantiation(instance):
    assert isinstance(instance, Books::Book)

@given(instance=Books::Book_strategy)
def test_books::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Books::Book_strategy)
def test_books::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Books::Book_strategy)
def test_books::book_collecName_type(instance):
    assert isinstance(instance.collecName, str)


@given(instance=Books::Book_strategy)
def test_books::book_collecName_setter(instance):
    original = instance.collecName
    instance.collecName = original
    assert instance.collecName == original

@given(instance=Books::System_strategy)
@settings(max_examples=50)
def test_books::system_instantiation(instance):
    assert isinstance(instance, Books::System)

@given(instance=Books::System_strategy)
def test_books::system_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Books::System_strategy)
def test_books::system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
