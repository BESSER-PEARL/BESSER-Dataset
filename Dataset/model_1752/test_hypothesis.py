import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Book_Summary,
    Book_Chapter,
    Book_Book,
    Book_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_book_summary_is_not_abstract():
    assert not inspect.isabstract(Book_Summary)


def test_book_summary_constructor_exists():
    assert callable(Book_Summary.__init__)


def test_book_summary_constructor_args():
    sig = inspect.signature(Book_Summary.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "nbWords" in params, "Missing parameter 'nbWords'"

def test_book_summary_has_content():
    assert hasattr(Book_Summary, "content")
    descriptor = None
    for klass in Book_Summary.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_book_summary_has_nbWords():
    assert hasattr(Book_Summary, "nbWords")
    descriptor = None
    for klass in Book_Summary.__mro__:
        if "nbWords" in klass.__dict__:
            descriptor = klass.__dict__["nbWords"]
            break
    assert isinstance(descriptor, property)



def test_book_chapter_is_not_abstract():
    assert not inspect.isabstract(Book_Chapter)


def test_book_chapter_constructor_exists():
    assert callable(Book_Chapter.__init__)


def test_book_chapter_constructor_args():
    sig = inspect.signature(Book_Chapter.__init__)
    params = list(sig.parameters.keys())
    assert "nbPages" in params, "Missing parameter 'nbPages'"
    assert "author" in params, "Missing parameter 'author'"
    assert "title" in params, "Missing parameter 'title'"

def test_book_chapter_has_nbPages():
    assert hasattr(Book_Chapter, "nbPages")
    descriptor = None
    for klass in Book_Chapter.__mro__:
        if "nbPages" in klass.__dict__:
            descriptor = klass.__dict__["nbPages"]
            break
    assert isinstance(descriptor, property)

def test_book_chapter_has_author():
    assert hasattr(Book_Chapter, "author")
    descriptor = None
    for klass in Book_Chapter.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_book_chapter_has_title():
    assert hasattr(Book_Chapter, "title")
    descriptor = None
    for klass in Book_Chapter.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_book_book_is_not_abstract():
    assert not inspect.isabstract(Book_Book)


def test_book_book_constructor_exists():
    assert callable(Book_Book.__init__)


def test_book_book_constructor_args():
    sig = inspect.signature(Book_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_book_book_has_title():
    assert hasattr(Book_Book, "title")
    descriptor = None
    for klass in Book_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_book_library_is_not_abstract():
    assert not inspect.isabstract(Book_Library)


def test_book_library_constructor_exists():
    assert callable(Book_Library.__init__)


def test_book_library_constructor_args():
    sig = inspect.signature(Book_Library.__init__)
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
Book_Summary_strategy = st.builds(
    Book_Summary,
    content=
        safe_text,
    nbWords=
        st.integers()
)
Book_Chapter_strategy = st.builds(
    Book_Chapter,
    nbPages=
        st.integers(),
    author=
        safe_text,
    title=
        safe_text
)
Book_Book_strategy = st.builds(
    Book_Book,
    title=
        safe_text
)
Book_Library_strategy = st.builds(
    Book_Library,
)

@given(instance=Book_Summary_strategy)
@settings(max_examples=50)
def test_book_summary_instantiation(instance):
    assert isinstance(instance, Book_Summary)



@given(instance=Book_Summary_strategy)
def test_book_summary_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=Book_Summary_strategy)
def test_book_summary_nbWords_setter(instance):
    original = instance.nbWords
    instance.nbWords = original
    assert instance.nbWords == original

@given(instance=Book_Chapter_strategy)
@settings(max_examples=50)
def test_book_chapter_instantiation(instance):
    assert isinstance(instance, Book_Chapter)



@given(instance=Book_Chapter_strategy)
def test_book_chapter_nbPages_setter(instance):
    original = instance.nbPages
    instance.nbPages = original
    assert instance.nbPages == original



@given(instance=Book_Chapter_strategy)
def test_book_chapter_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=Book_Chapter_strategy)
def test_book_chapter_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Book_Book_strategy)
@settings(max_examples=50)
def test_book_book_instantiation(instance):
    assert isinstance(instance, Book_Book)



@given(instance=Book_Book_strategy)
def test_book_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Book_Library_strategy)
@settings(max_examples=50)
def test_book_library_instantiation(instance):
    assert isinstance(instance, Book_Library)
