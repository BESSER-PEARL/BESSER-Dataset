import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Books_Chapter,
    Books_Author,
    Books_Book,
    Books_System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_books_chapter_is_not_abstract():
    assert not inspect.isabstract(Books_Chapter)


def test_books_chapter_constructor_exists():
    assert callable(Books_Chapter.__init__)


def test_books_chapter_constructor_args():
    sig = inspect.signature(Books_Chapter.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_books_chapter_has_title():
    assert hasattr(Books_Chapter, "title")
    descriptor = None
    for klass in Books_Chapter.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_books_author_is_not_abstract():
    assert not inspect.isabstract(Books_Author)


def test_books_author_constructor_exists():
    assert callable(Books_Author.__init__)


def test_books_author_constructor_args():
    sig = inspect.signature(Books_Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_books_author_has_name():
    assert hasattr(Books_Author, "name")
    descriptor = None
    for klass in Books_Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_books_book_is_not_abstract():
    assert not inspect.isabstract(Books_Book)


def test_books_book_constructor_exists():
    assert callable(Books_Book.__init__)


def test_books_book_constructor_args():
    sig = inspect.signature(Books_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "collecName" in params, "Missing parameter 'collecName'"

def test_books_book_has_title():
    assert hasattr(Books_Book, "title")
    descriptor = None
    for klass in Books_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_books_book_has_collecName():
    assert hasattr(Books_Book, "collecName")
    descriptor = None
    for klass in Books_Book.__mro__:
        if "collecName" in klass.__dict__:
            descriptor = klass.__dict__["collecName"]
            break
    assert isinstance(descriptor, property)



def test_books_system_is_not_abstract():
    assert not inspect.isabstract(Books_System)


def test_books_system_constructor_exists():
    assert callable(Books_System.__init__)


def test_books_system_constructor_args():
    sig = inspect.signature(Books_System.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_books_system_has_name():
    assert hasattr(Books_System, "name")
    descriptor = None
    for klass in Books_System.__mro__:
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
Books_Chapter_strategy = st.builds(
    Books_Chapter,
    title=
        safe_text
)
Books_Author_strategy = st.builds(
    Books_Author,
    name=
        safe_text
)
Books_Book_strategy = st.builds(
    Books_Book,
    title=
        safe_text,
    collecName=
        safe_text
)
Books_System_strategy = st.builds(
    Books_System,
    name=
        safe_text
)

@given(instance=Books_Chapter_strategy)
@settings(max_examples=50)
def test_books_chapter_instantiation(instance):
    assert isinstance(instance, Books_Chapter)



@given(instance=Books_Chapter_strategy)
def test_books_chapter_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Books_Author_strategy)
@settings(max_examples=50)
def test_books_author_instantiation(instance):
    assert isinstance(instance, Books_Author)



@given(instance=Books_Author_strategy)
def test_books_author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Books_Book_strategy)
@settings(max_examples=50)
def test_books_book_instantiation(instance):
    assert isinstance(instance, Books_Book)



@given(instance=Books_Book_strategy)
def test_books_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Books_Book_strategy)
def test_books_book_collecName_setter(instance):
    original = instance.collecName
    instance.collecName = original
    assert instance.collecName == original

@given(instance=Books_System_strategy)
@settings(max_examples=50)
def test_books_system_instantiation(instance):
    assert isinstance(instance, Books_System)



@given(instance=Books_System_strategy)
def test_books_system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
