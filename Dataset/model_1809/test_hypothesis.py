import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Book::Chapter,
    Book::Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_book::chapter_is_not_abstract():
    assert not inspect.isabstract(Book::Chapter)


def test_book::chapter_constructor_exists():
    assert callable(Book::Chapter.__init__)


def test_book::chapter_constructor_args():
    sig = inspect.signature(Book::Chapter.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

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
    assert "isNew" in params, "Missing parameter 'isNew'"
    assert "nPages" in params, "Missing parameter 'nPages'"
    assert "title" in params, "Missing parameter 'title'"
    assert "isMultiVolume" in params, "Missing parameter 'isMultiVolume'"

def test_book::book_has_isNew():
    assert hasattr(Book::Book, "isNew")
    descriptor = None
    for klass in Book::Book.__mro__:
        if "isNew" in klass.__dict__:
            descriptor = klass.__dict__["isNew"]
            break
    assert isinstance(descriptor, property)

def test_book::book_has_nPages():
    assert hasattr(Book::Book, "nPages")
    descriptor = None
    for klass in Book::Book.__mro__:
        if "nPages" in klass.__dict__:
            descriptor = klass.__dict__["nPages"]
            break
    assert isinstance(descriptor, property)

def test_book::book_has_title():
    assert hasattr(Book::Book, "title")
    descriptor = None
    for klass in Book::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_book::book_has_isMultiVolume():
    assert hasattr(Book::Book, "isMultiVolume")
    descriptor = None
    for klass in Book::Book.__mro__:
        if "isMultiVolume" in klass.__dict__:
            descriptor = klass.__dict__["isMultiVolume"]
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
Book::Chapter_strategy = st.builds(
    Book::Chapter,
    title=
        safe_text
)
Book::Book_strategy = st.builds(
    Book::Book,
    isNew=
        st.booleans(),
    nPages=
        st.integers(),
    title=
        safe_text,
    isMultiVolume=
        st.booleans()
)

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

@given(instance=Book::Book_strategy)
@settings(max_examples=50)
def test_book::book_instantiation(instance):
    assert isinstance(instance, Book::Book)

@given(instance=Book::Book_strategy)
def test_book::book_isNew_type(instance):
    assert isinstance(instance.isNew, bool)


@given(instance=Book::Book_strategy)
def test_book::book_isNew_setter(instance):
    original = instance.isNew
    instance.isNew = original
    assert instance.isNew == original

@given(instance=Book::Book_strategy)
def test_book::book_nPages_type(instance):
    assert isinstance(instance.nPages, int)


@given(instance=Book::Book_strategy)
def test_book::book_nPages_setter(instance):
    original = instance.nPages
    instance.nPages = original
    assert instance.nPages == original

@given(instance=Book::Book_strategy)
def test_book::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Book::Book_strategy)
def test_book::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Book::Book_strategy)
def test_book::book_isMultiVolume_type(instance):
    assert isinstance(instance.isMultiVolume, bool)


@given(instance=Book::Book_strategy)
def test_book::book_isMultiVolume_setter(instance):
    original = instance.isMultiVolume
    instance.isMultiVolume = original
    assert instance.isMultiVolume == original
