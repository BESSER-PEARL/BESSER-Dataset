import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    books_Writer,
    books_Book,
    books_Catalog,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_books_writer_is_not_abstract():
    assert not inspect.isabstract(books_Writer)


def test_books_writer_constructor_exists():
    assert callable(books_Writer.__init__)


def test_books_writer_constructor_args():
    sig = inspect.signature(books_Writer.__init__)
    params = list(sig.parameters.keys())



def test_books_book_is_not_abstract():
    assert not inspect.isabstract(books_Book)


def test_books_book_constructor_exists():
    assert callable(books_Book.__init__)


def test_books_book_constructor_args():
    sig = inspect.signature(books_Book.__init__)
    params = list(sig.parameters.keys())
    assert "isbn" in params, "Missing parameter 'isbn'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"

def test_books_book_has_isbn():
    assert hasattr(books_Book, "isbn")
    descriptor = None
    for klass in books_Book.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)

def test_books_book_has_pages():
    assert hasattr(books_Book, "pages")
    descriptor = None
    for klass in books_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_books_book_has_title():
    assert hasattr(books_Book, "title")
    descriptor = None
    for klass in books_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_books_catalog_is_not_abstract():
    assert not inspect.isabstract(books_Catalog)


def test_books_catalog_constructor_exists():
    assert callable(books_Catalog.__init__)


def test_books_catalog_constructor_args():
    sig = inspect.signature(books_Catalog.__init__)
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
books_Writer_strategy = st.builds(
    books_Writer,
)
books_Book_strategy = st.builds(
    books_Book,
    isbn=
        safe_text,
    pages=
        st.integers(),
    title=
        safe_text
)
books_Catalog_strategy = st.builds(
    books_Catalog,
)

@given(instance=books_Writer_strategy)
@settings(max_examples=50)
def test_books_writer_instantiation(instance):
    assert isinstance(instance, books_Writer)

@given(instance=books_Book_strategy)
@settings(max_examples=50)
def test_books_book_instantiation(instance):
    assert isinstance(instance, books_Book)



@given(instance=books_Book_strategy)
def test_books_book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original



@given(instance=books_Book_strategy)
def test_books_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=books_Book_strategy)
def test_books_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=books_Catalog_strategy)
@settings(max_examples=50)
def test_books_catalog_instantiation(instance):
    assert isinstance(instance, books_Catalog)
