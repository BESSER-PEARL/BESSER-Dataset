import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BOOKS_Book,
    BOOKS_Chapter,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_books_book_is_not_abstract():
    assert not inspect.isabstract(BOOKS_Book)


def test_books_book_constructor_exists():
    assert callable(BOOKS_Book.__init__)


def test_books_book_constructor_args():
    sig = inspect.signature(BOOKS_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_books_book_has_title():
    assert hasattr(BOOKS_Book, "title")
    descriptor = None
    for klass in BOOKS_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_books_chapter_is_not_abstract():
    assert not inspect.isabstract(BOOKS_Chapter)


def test_books_chapter_constructor_exists():
    assert callable(BOOKS_Chapter.__init__)


def test_books_chapter_constructor_args():
    sig = inspect.signature(BOOKS_Chapter.__init__)
    params = list(sig.parameters.keys())
    assert "nbPages" in params, "Missing parameter 'nbPages'"
    assert "title" in params, "Missing parameter 'title'"

def test_books_chapter_has_nbPages():
    assert hasattr(BOOKS_Chapter, "nbPages")
    descriptor = None
    for klass in BOOKS_Chapter.__mro__:
        if "nbPages" in klass.__dict__:
            descriptor = klass.__dict__["nbPages"]
            break
    assert isinstance(descriptor, property)

def test_books_chapter_has_title():
    assert hasattr(BOOKS_Chapter, "title")
    descriptor = None
    for klass in BOOKS_Chapter.__mro__:
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
BOOKS_Book_strategy = st.builds(
    BOOKS_Book,
    title=
        safe_text
)
BOOKS_Chapter_strategy = st.builds(
    BOOKS_Chapter,
    nbPages=
        st.integers(),
    title=
        safe_text
)

@given(instance=BOOKS_Book_strategy)
@settings(max_examples=50)
def test_books_book_instantiation(instance):
    assert isinstance(instance, BOOKS_Book)



@given(instance=BOOKS_Book_strategy)
def test_books_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=BOOKS_Chapter_strategy)
@settings(max_examples=50)
def test_books_chapter_instantiation(instance):
    assert isinstance(instance, BOOKS_Chapter)



@given(instance=BOOKS_Chapter_strategy)
def test_books_chapter_nbPages_setter(instance):
    original = instance.nbPages
    instance.nbPages = original
    assert instance.nbPages == original



@given(instance=BOOKS_Chapter_strategy)
def test_books_chapter_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
