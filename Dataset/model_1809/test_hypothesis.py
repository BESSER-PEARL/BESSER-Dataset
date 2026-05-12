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
    assert "title" in params, "Missing parameter 'title'"

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
    assert "nPages" in params, "Missing parameter 'nPages'"
    assert "isMultiVolume" in params, "Missing parameter 'isMultiVolume'"
    assert "isNew" in params, "Missing parameter 'isNew'"

def test_book_book_has_title():
    assert hasattr(Book_Book, "title")
    descriptor = None
    for klass in Book_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_book_book_has_nPages():
    assert hasattr(Book_Book, "nPages")
    descriptor = None
    for klass in Book_Book.__mro__:
        if "nPages" in klass.__dict__:
            descriptor = klass.__dict__["nPages"]
            break
    assert isinstance(descriptor, property)

def test_book_book_has_isMultiVolume():
    assert hasattr(Book_Book, "isMultiVolume")
    descriptor = None
    for klass in Book_Book.__mro__:
        if "isMultiVolume" in klass.__dict__:
            descriptor = klass.__dict__["isMultiVolume"]
            break
    assert isinstance(descriptor, property)

def test_book_book_has_isNew():
    assert hasattr(Book_Book, "isNew")
    descriptor = None
    for klass in Book_Book.__mro__:
        if "isNew" in klass.__dict__:
            descriptor = klass.__dict__["isNew"]
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
    title=
        safe_text
)
Book_Book_strategy = st.builds(
    Book_Book,
    title=
        safe_text,
    nPages=
        st.integers(),
    isMultiVolume=
        st.booleans(),
    isNew=
        st.booleans()
)

@given(instance=Book_Chapter_strategy)
@settings(max_examples=50)
def test_book_chapter_instantiation(instance):
    assert isinstance(instance, Book_Chapter)



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



@given(instance=Book_Book_strategy)
def test_book_book_nPages_setter(instance):
    original = instance.nPages
    instance.nPages = original
    assert instance.nPages == original



@given(instance=Book_Book_strategy)
def test_book_book_isMultiVolume_setter(instance):
    original = instance.isMultiVolume
    instance.isMultiVolume = original
    assert instance.isMultiVolume == original



@given(instance=Book_Book_strategy)
def test_book_book_isNew_setter(instance):
    original = instance.isNew
    instance.isNew = original
    assert instance.isNew == original
