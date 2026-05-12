import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Book_Chapter,
    Book_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_book_chapter_is_not_abstract():
    assert not inspect.isabstract(Book_Chapter)


def test_book_chapter_constructor_exists():
    assert callable(Book_Chapter.__init__)


def test_book_chapter_constructor_args():
    sig = inspect.signature(Book_Chapter.__init__)
    params = list(sig.parameters.keys())
    assert "nbPages" in params, "Missing parameter 'nbPages'"
    assert "title" in params, "Missing parameter 'title'"

def test_book_chapter_has_nbPages():
    assert hasattr(Book_Chapter, "nbPages")
    descriptor = None
    for klass in Book_Chapter.__mro__:
        if "nbPages" in klass.__dict__:
            descriptor = klass.__dict__["nbPages"]
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
    assert "authorName" in params, "Missing parameter 'authorName'"
    assert "title" in params, "Missing parameter 'title'"

def test_book_book_has_authorName():
    assert hasattr(Book_Book, "authorName")
    descriptor = None
    for klass in Book_Book.__mro__:
        if "authorName" in klass.__dict__:
            descriptor = klass.__dict__["authorName"]
            break
    assert isinstance(descriptor, property)

def test_book_book_has_title():
    assert hasattr(Book_Book, "title")
    descriptor = None
    for klass in Book_Book.__mro__:
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
Book_Chapter_strategy = st.builds(
    Book_Chapter,
    nbPages=
        st.integers(),
    title=
        safe_text
)
Book_Book_strategy = st.builds(
    Book_Book,
    authorName=
        safe_text,
    title=
        safe_text
)

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
def test_book_chapter_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Book_Book_strategy)
@settings(max_examples=50)
def test_book_book_instantiation(instance):
    assert isinstance(instance, Book_Book)



@given(instance=Book_Book_strategy)
def test_book_book_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original



@given(instance=Book_Book_strategy)
def test_book_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
