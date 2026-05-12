import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Book_Book,
    Book_Library,
    Book_Chapter,
    Book_Author,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_book_book_is_not_abstract():
    assert not inspect.isabstract(Book_Book)


def test_book_book_constructor_exists():
    assert callable(Book_Book.__init__)


def test_book_book_constructor_args():
    sig = inspect.signature(Book_Book.__init__)
    params = list(sig.parameters.keys())
    assert "isbn" in params, "Missing parameter 'isbn'"
    assert "nbpages" in params, "Missing parameter 'nbpages'"
    assert "title" in params, "Missing parameter 'title'"

def test_book_book_has_isbn():
    assert hasattr(Book_Book, "isbn")
    descriptor = None
    for klass in Book_Book.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)

def test_book_book_has_nbpages():
    assert hasattr(Book_Book, "nbpages")
    descriptor = None
    for klass in Book_Book.__mro__:
        if "nbpages" in klass.__dict__:
            descriptor = klass.__dict__["nbpages"]
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



def test_book_library_is_not_abstract():
    assert not inspect.isabstract(Book_Library)


def test_book_library_constructor_exists():
    assert callable(Book_Library.__init__)


def test_book_library_constructor_args():
    sig = inspect.signature(Book_Library.__init__)
    params = list(sig.parameters.keys())



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



def test_book_author_is_not_abstract():
    assert not inspect.isabstract(Book_Author)


def test_book_author_constructor_exists():
    assert callable(Book_Author.__init__)


def test_book_author_constructor_args():
    sig = inspect.signature(Book_Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_book_author_has_name():
    assert hasattr(Book_Author, "name")
    descriptor = None
    for klass in Book_Author.__mro__:
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
Book_Book_strategy = st.builds(
    Book_Book,
    isbn=
        safe_text,
    nbpages=
        st.integers(),
    title=
        safe_text
)
Book_Library_strategy = st.builds(
    Book_Library,
)
Book_Chapter_strategy = st.builds(
    Book_Chapter,
    title=
        safe_text
)
Book_Author_strategy = st.builds(
    Book_Author,
    name=
        safe_text
)

@given(instance=Book_Book_strategy)
@settings(max_examples=50)
def test_book_book_instantiation(instance):
    assert isinstance(instance, Book_Book)



@given(instance=Book_Book_strategy)
def test_book_book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original



@given(instance=Book_Book_strategy)
def test_book_book_nbpages_setter(instance):
    original = instance.nbpages
    instance.nbpages = original
    assert instance.nbpages == original



@given(instance=Book_Book_strategy)
def test_book_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Book_Library_strategy)
@settings(max_examples=50)
def test_book_library_instantiation(instance):
    assert isinstance(instance, Book_Library)

@given(instance=Book_Chapter_strategy)
@settings(max_examples=50)
def test_book_chapter_instantiation(instance):
    assert isinstance(instance, Book_Chapter)



@given(instance=Book_Chapter_strategy)
def test_book_chapter_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Book_Author_strategy)
@settings(max_examples=50)
def test_book_author_instantiation(instance):
    assert isinstance(instance, Book_Author)



@given(instance=Book_Author_strategy)
def test_book_author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
