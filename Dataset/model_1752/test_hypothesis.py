import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Book::Summary,
    Book::Chapter,
    Book::Book,
    Book::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_book::summary_is_not_abstract():
    assert not inspect.isabstract(Book::Summary)


def test_book::summary_constructor_exists():
    assert callable(Book::Summary.__init__)


def test_book::summary_constructor_args():
    sig = inspect.signature(Book::Summary.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "nbWords" in params, "Missing parameter 'nbWords'"

def test_book::summary_has_content():
    assert hasattr(Book::Summary, "content")
    descriptor = None
    for klass in Book::Summary.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_book::summary_has_nbWords():
    assert hasattr(Book::Summary, "nbWords")
    descriptor = None
    for klass in Book::Summary.__mro__:
        if "nbWords" in klass.__dict__:
            descriptor = klass.__dict__["nbWords"]
            break
    assert isinstance(descriptor, property)



def test_book::chapter_is_not_abstract():
    assert not inspect.isabstract(Book::Chapter)


def test_book::chapter_constructor_exists():
    assert callable(Book::Chapter.__init__)


def test_book::chapter_constructor_args():
    sig = inspect.signature(Book::Chapter.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "nbPages" in params, "Missing parameter 'nbPages'"
    assert "title" in params, "Missing parameter 'title'"

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

def test_book::chapter_has_title():
    assert hasattr(Book::Chapter, "title")
    descriptor = None
    for klass in Book::Chapter.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



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



def test_book::library_is_not_abstract():
    assert not inspect.isabstract(Book::Library)


def test_book::library_constructor_exists():
    assert callable(Book::Library.__init__)


def test_book::library_constructor_args():
    sig = inspect.signature(Book::Library.__init__)
    params = list(sig.parameters.keys())


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
Book::Summary_strategy = st.builds(
    Book::Summary,
    content=
        safe_text,
    nbWords=
        st.integers()
)
Book::Chapter_strategy = st.builds(
    Book::Chapter,
    author=
        safe_text,
    nbPages=
        st.integers(),
    title=
        safe_text
)
Book::Book_strategy = st.builds(
    Book::Book,
    title=
        safe_text
)
Book::Library_strategy = st.builds(
    Book::Library,
)

@given(instance=Book::Summary_strategy)
@settings(max_examples=50)
def test_book::summary_instantiation(instance):
    assert isinstance(instance, Book::Summary)

@given(instance=Book::Summary_strategy)
def test_book::summary_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=Book::Summary_strategy)
def test_book::summary_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=Book::Summary_strategy)
def test_book::summary_nbWords_type(instance):
    assert isinstance(instance.nbWords, int)


@given(instance=Book::Summary_strategy)
def test_book::summary_nbWords_setter(instance):
    original = instance.nbWords
    instance.nbWords = original
    assert instance.nbWords == original

@given(instance=Book::Chapter_strategy)
@settings(max_examples=50)
def test_book::chapter_instantiation(instance):
    assert isinstance(instance, Book::Chapter)

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
    assert isinstance(instance.nbPages, int)


@given(instance=Book::Chapter_strategy)
def test_book::chapter_nbPages_setter(instance):
    original = instance.nbPages
    instance.nbPages = original
    assert instance.nbPages == original

@given(instance=Book::Chapter_strategy)
def test_book::chapter_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Book::Chapter_strategy)
def test_book::chapter_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

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

@given(instance=Book::Library_strategy)
@settings(max_examples=50)
def test_book::library_instantiation(instance):
    assert isinstance(instance, Book::Library)
