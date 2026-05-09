import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    book::Chapter,
    book::Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_book::chapter_is_not_abstract():
    assert not inspect.isabstract(book::Chapter)


def test_book::chapter_constructor_exists():
    assert callable(book::Chapter.__init__)


def test_book::chapter_constructor_args():
    sig = inspect.signature(book::Chapter.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "title" in params, "Missing parameter 'title'"
    assert "nbPages" in params, "Missing parameter 'nbPages'"

def test_book::chapter_has_author():
    assert hasattr(book::Chapter, "author")
    descriptor = None
    for klass in book::Chapter.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_book::chapter_has_title():
    assert hasattr(book::Chapter, "title")
    descriptor = None
    for klass in book::Chapter.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_book::chapter_has_nbPages():
    assert hasattr(book::Chapter, "nbPages")
    descriptor = None
    for klass in book::Chapter.__mro__:
        if "nbPages" in klass.__dict__:
            descriptor = klass.__dict__["nbPages"]
            break
    assert isinstance(descriptor, property)



def test_book::book_is_not_abstract():
    assert not inspect.isabstract(book::Book)


def test_book::book_constructor_exists():
    assert callable(book::Book.__init__)


def test_book::book_constructor_args():
    sig = inspect.signature(book::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_book::book_has_title():
    assert hasattr(book::Book, "title")
    descriptor = None
    for klass in book::Book.__mro__:
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
book::Chapter_strategy = st.builds(
    book::Chapter,
    author=
        safe_text,
    title=
        safe_text,
    nbPages=
        st.integers()
)
book::Book_strategy = st.builds(
    book::Book,
    title=
        safe_text
)

@given(instance=book::Chapter_strategy)
@settings(max_examples=50)
def test_book::chapter_instantiation(instance):
    assert isinstance(instance, book::Chapter)

@given(instance=book::Chapter_strategy)
def test_book::chapter_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=book::Chapter_strategy)
def test_book::chapter_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=book::Chapter_strategy)
def test_book::chapter_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=book::Chapter_strategy)
def test_book::chapter_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=book::Chapter_strategy)
def test_book::chapter_nbPages_type(instance):
    assert isinstance(instance.nbPages, int)


@given(instance=book::Chapter_strategy)
def test_book::chapter_nbPages_setter(instance):
    original = instance.nbPages
    instance.nbPages = original
    assert instance.nbPages == original

@given(instance=book::Book_strategy)
@settings(max_examples=50)
def test_book::book_instantiation(instance):
    assert isinstance(instance, book::Book)

@given(instance=book::Book_strategy)
def test_book::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=book::Book_strategy)
def test_book::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
