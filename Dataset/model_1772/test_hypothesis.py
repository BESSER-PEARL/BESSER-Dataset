import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    books::Writer,
    books::Book,
    books::Catalog,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_books::writer_is_not_abstract():
    assert not inspect.isabstract(books::Writer)


def test_books::writer_constructor_exists():
    assert callable(books::Writer.__init__)


def test_books::writer_constructor_args():
    sig = inspect.signature(books::Writer.__init__)
    params = list(sig.parameters.keys())



def test_books::book_is_not_abstract():
    assert not inspect.isabstract(books::Book)


def test_books::book_constructor_exists():
    assert callable(books::Book.__init__)


def test_books::book_constructor_args():
    sig = inspect.signature(books::Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "isbn" in params, "Missing parameter 'isbn'"
    assert "title" in params, "Missing parameter 'title'"

def test_books::book_has_pages():
    assert hasattr(books::Book, "pages")
    descriptor = None
    for klass in books::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_books::book_has_isbn():
    assert hasattr(books::Book, "isbn")
    descriptor = None
    for klass in books::Book.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)

def test_books::book_has_title():
    assert hasattr(books::Book, "title")
    descriptor = None
    for klass in books::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_books::catalog_is_not_abstract():
    assert not inspect.isabstract(books::Catalog)


def test_books::catalog_constructor_exists():
    assert callable(books::Catalog.__init__)


def test_books::catalog_constructor_args():
    sig = inspect.signature(books::Catalog.__init__)
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
books::Writer_strategy = st.builds(
    books::Writer,
)
books::Book_strategy = st.builds(
    books::Book,
    pages=
        st.integers(),
    isbn=
        safe_text,
    title=
        safe_text
)
books::Catalog_strategy = st.builds(
    books::Catalog,
)

@given(instance=books::Writer_strategy)
@settings(max_examples=50)
def test_books::writer_instantiation(instance):
    assert isinstance(instance, books::Writer)

@given(instance=books::Book_strategy)
@settings(max_examples=50)
def test_books::book_instantiation(instance):
    assert isinstance(instance, books::Book)

@given(instance=books::Book_strategy)
def test_books::book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=books::Book_strategy)
def test_books::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=books::Book_strategy)
def test_books::book_isbn_type(instance):
    assert isinstance(instance.isbn, str)


@given(instance=books::Book_strategy)
def test_books::book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original

@given(instance=books::Book_strategy)
def test_books::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=books::Book_strategy)
def test_books::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=books::Catalog_strategy)
@settings(max_examples=50)
def test_books::catalog_instantiation(instance):
    assert isinstance(instance, books::Catalog)
