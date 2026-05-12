import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    book_Chapter,
    book_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_book_chapter_is_not_abstract():
    assert not inspect.isabstract(book_Chapter)


def test_book_chapter_constructor_exists():
    assert callable(book_Chapter.__init__)


def test_book_chapter_constructor_args():
    sig = inspect.signature(book_Chapter.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "nbPages" in params, "Missing parameter 'nbPages'"
    assert "title" in params, "Missing parameter 'title'"

def test_book_chapter_has_author():
    assert hasattr(book_Chapter, "author")
    descriptor = None
    for klass in book_Chapter.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_book_chapter_has_nbPages():
    assert hasattr(book_Chapter, "nbPages")
    descriptor = None
    for klass in book_Chapter.__mro__:
        if "nbPages" in klass.__dict__:
            descriptor = klass.__dict__["nbPages"]
            break
    assert isinstance(descriptor, property)

def test_book_chapter_has_title():
    assert hasattr(book_Chapter, "title")
    descriptor = None
    for klass in book_Chapter.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_book_book_is_not_abstract():
    assert not inspect.isabstract(book_Book)


def test_book_book_constructor_exists():
    assert callable(book_Book.__init__)


def test_book_book_constructor_args():
    sig = inspect.signature(book_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_book_book_has_title():
    assert hasattr(book_Book, "title")
    descriptor = None
    for klass in book_Book.__mro__:
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
book_Chapter_strategy = st.builds(
    book_Chapter,
    author=
        safe_text,
    nbPages=
        st.integers(),
    title=
        safe_text
)
book_Book_strategy = st.builds(
    book_Book,
    title=
        safe_text
)

@given(instance=book_Chapter_strategy)
@settings(max_examples=50)
def test_book_chapter_instantiation(instance):
    assert isinstance(instance, book_Chapter)



@given(instance=book_Chapter_strategy)
def test_book_chapter_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=book_Chapter_strategy)
def test_book_chapter_nbPages_setter(instance):
    original = instance.nbPages
    instance.nbPages = original
    assert instance.nbPages == original



@given(instance=book_Chapter_strategy)
def test_book_chapter_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=book_Book_strategy)
@settings(max_examples=50)
def test_book_book_instantiation(instance):
    assert isinstance(instance, book_Book)



@given(instance=book_Book_strategy)
def test_book_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
