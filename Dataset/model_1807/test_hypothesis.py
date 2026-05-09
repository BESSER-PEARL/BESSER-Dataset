import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Book,
    Book::Chapter,
    Chapter,
    Book::Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_book_constructor_exists():
    assert callable(Book.__init__)


def test_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())



def test_book::chapter_is_not_abstract():
    assert not inspect.isabstract(Book::Chapter)


def test_book::chapter_constructor_exists():
    assert callable(Book::Chapter.__init__)


def test_book::chapter_constructor_args():
    sig = inspect.signature(Book::Chapter.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "author" in params, "Missing parameter 'author'"
    assert "nbPages" in params, "Missing parameter 'nbPages'"

def test_book::chapter_has_title():
    assert hasattr(Book::Chapter, "title")
    descriptor = None
    for klass in Book::Chapter.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_book::chapter_has_author():
    assert hasattr(Book::Chapter, "author")
    descriptor = None
    for klass in Book::Chapter.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_book::chapter_has_nbPages():
    assert hasattr(Book::Chapter, "nbPages")
    descriptor = None
    for klass in Book::Chapter.__mro__:
        if "nbPages" in klass.__dict__:
            descriptor = klass.__dict__["nbPages"]
            break
    assert isinstance(descriptor, property)



def test_chapter_is_not_abstract():
    assert not inspect.isabstract(Chapter)


def test_chapter_constructor_exists():
    assert callable(Chapter.__init__)


def test_chapter_constructor_args():
    sig = inspect.signature(Chapter.__init__)
    params = list(sig.parameters.keys())



def test_book::book_is_not_abstract():
    assert not inspect.isabstract(Book::Book)


def test_book::book_constructor_exists():
    assert callable(Book::Book.__init__)


def test_book::book_constructor_args():
    sig = inspect.signature(Book::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_book::book_has_title():
    assert hasattr(Book::Book, "title")
    descriptor = None
    for klass in Book::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
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
Book_strategy = st.builds(
    Book,
)
Book::Chapter_strategy = st.builds(
    Book::Chapter,
    title=
        safe_text,
    author=
        safe_text,
    nbPages=
        safe_text
)
Chapter_strategy = st.builds(
    Chapter,
)
Book::Book_strategy = st.builds(
    Book::Book,
    title=
        safe_text
)

@given(instance=Book_strategy)
@settings(max_examples=50)
def test_book_instantiation(instance):
    assert isinstance(instance, Book)

@given(instance=Book::Chapter_strategy)
@settings(max_examples=50)
def test_book::chapter_instantiation(instance):
    assert isinstance(instance, Book::Chapter)

@given(instance=Book::Chapter_strategy)
def test_book::chapter_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Book::Chapter_strategy)
def test_book::chapter_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Book::Chapter_strategy)
def test_book::chapter_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=Book::Chapter_strategy)
def test_book::chapter_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=Book::Chapter_strategy)
def test_book::chapter_nbPages_type(instance):
    assert isinstance(instance.nbPages, str)


@given(instance=Book::Chapter_strategy)
def test_book::chapter_nbPages_setter(instance):
    original = instance.nbPages
    instance.nbPages = original
    assert instance.nbPages == original

@given(instance=Chapter_strategy)
@settings(max_examples=50)
def test_chapter_instantiation(instance):
    assert isinstance(instance, Chapter)

@given(instance=Book::Book_strategy)
@settings(max_examples=50)
def test_book::book_instantiation(instance):
    assert isinstance(instance, Book::Book)

@given(instance=Book::Book_strategy)
def test_book::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Book::Book_strategy)
def test_book::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
