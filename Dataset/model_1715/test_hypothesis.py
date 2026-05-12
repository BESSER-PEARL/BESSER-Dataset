import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    library3Simplified_Book,
    library3Simplified_BookInfo,
    library3Simplified_Library,
    library3Simplified_Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library3simplified_book_is_not_abstract():
    assert not inspect.isabstract(library3Simplified_Book)


def test_library3simplified_book_constructor_exists():
    assert callable(library3Simplified_Book.__init__)


def test_library3simplified_book_constructor_args():
    sig = inspect.signature(library3Simplified_Book.__init__)
    params = list(sig.parameters.keys())
    assert "dimension" in params, "Missing parameter 'dimension'"
    assert "isbn" in params, "Missing parameter 'isbn'"
    assert "download" in params, "Missing parameter 'download'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"
    assert "name" in params, "Missing parameter 'name'"
    assert "author" in params, "Missing parameter 'author'"

def test_library3simplified_book_has_dimension():
    assert hasattr(library3Simplified_Book, "dimension")
    descriptor = None
    for klass in library3Simplified_Book.__mro__:
        if "dimension" in klass.__dict__:
            descriptor = klass.__dict__["dimension"]
            break
    assert isinstance(descriptor, property)

def test_library3simplified_book_has_isbn():
    assert hasattr(library3Simplified_Book, "isbn")
    descriptor = None
    for klass in library3Simplified_Book.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)

def test_library3simplified_book_has_download():
    assert hasattr(library3Simplified_Book, "download")
    descriptor = None
    for klass in library3Simplified_Book.__mro__:
        if "download" in klass.__dict__:
            descriptor = klass.__dict__["download"]
            break
    assert isinstance(descriptor, property)

def test_library3simplified_book_has_pages():
    assert hasattr(library3Simplified_Book, "pages")
    descriptor = None
    for klass in library3Simplified_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_library3simplified_book_has_title():
    assert hasattr(library3Simplified_Book, "title")
    descriptor = None
    for klass in library3Simplified_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library3simplified_book_has_name():
    assert hasattr(library3Simplified_Book, "name")
    descriptor = None
    for klass in library3Simplified_Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_library3simplified_book_has_author():
    assert hasattr(library3Simplified_Book, "author")
    descriptor = None
    for klass in library3Simplified_Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)



def test_library3simplified_bookinfo_is_not_abstract():
    assert not inspect.isabstract(library3Simplified_BookInfo)


def test_library3simplified_bookinfo_constructor_exists():
    assert callable(library3Simplified_BookInfo.__init__)


def test_library3simplified_bookinfo_constructor_args():
    sig = inspect.signature(library3Simplified_BookInfo.__init__)
    params = list(sig.parameters.keys())



def test_library3simplified_library_is_not_abstract():
    assert not inspect.isabstract(library3Simplified_Library)


def test_library3simplified_library_constructor_exists():
    assert callable(library3Simplified_Library.__init__)


def test_library3simplified_library_constructor_args():
    sig = inspect.signature(library3Simplified_Library.__init__)
    params = list(sig.parameters.keys())



def test_library3simplified_customer_is_not_abstract():
    assert not inspect.isabstract(library3Simplified_Customer)


def test_library3simplified_customer_constructor_exists():
    assert callable(library3Simplified_Customer.__init__)


def test_library3simplified_customer_constructor_args():
    sig = inspect.signature(library3Simplified_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "borrowedBookSince" in params, "Missing parameter 'borrowedBookSince'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_library3simplified_customer_has_lastName():
    assert hasattr(library3Simplified_Customer, "lastName")
    descriptor = None
    for klass in library3Simplified_Customer.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_library3simplified_customer_has_borrowedBookSince():
    assert hasattr(library3Simplified_Customer, "borrowedBookSince")
    descriptor = None
    for klass in library3Simplified_Customer.__mro__:
        if "borrowedBookSince" in klass.__dict__:
            descriptor = klass.__dict__["borrowedBookSince"]
            break
    assert isinstance(descriptor, property)

def test_library3simplified_customer_has_firstName():
    assert hasattr(library3Simplified_Customer, "firstName")
    descriptor = None
    for klass in library3Simplified_Customer.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
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
library3Simplified_Book_strategy = st.builds(
    library3Simplified_Book,
    dimension=
        safe_text,
    isbn=
        safe_text,
    download=
        safe_text,
    pages=
        st.integers(),
    title=
        safe_text,
    name=
        safe_text,
    author=
        safe_text
)
library3Simplified_BookInfo_strategy = st.builds(
    library3Simplified_BookInfo,
)
library3Simplified_Library_strategy = st.builds(
    library3Simplified_Library,
)
library3Simplified_Customer_strategy = st.builds(
    library3Simplified_Customer,
    lastName=
        safe_text,
    borrowedBookSince=
        safe_text,
    firstName=
        safe_text
)

@given(instance=library3Simplified_Book_strategy)
@settings(max_examples=50)
def test_library3simplified_book_instantiation(instance):
    assert isinstance(instance, library3Simplified_Book)



@given(instance=library3Simplified_Book_strategy)
def test_library3simplified_book_dimension_setter(instance):
    original = instance.dimension
    instance.dimension = original
    assert instance.dimension == original



@given(instance=library3Simplified_Book_strategy)
def test_library3simplified_book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original



@given(instance=library3Simplified_Book_strategy)
def test_library3simplified_book_download_setter(instance):
    original = instance.download
    instance.download = original
    assert instance.download == original



@given(instance=library3Simplified_Book_strategy)
def test_library3simplified_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=library3Simplified_Book_strategy)
def test_library3simplified_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=library3Simplified_Book_strategy)
def test_library3simplified_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=library3Simplified_Book_strategy)
def test_library3simplified_book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=library3Simplified_BookInfo_strategy)
@settings(max_examples=50)
def test_library3simplified_bookinfo_instantiation(instance):
    assert isinstance(instance, library3Simplified_BookInfo)

@given(instance=library3Simplified_Library_strategy)
@settings(max_examples=50)
def test_library3simplified_library_instantiation(instance):
    assert isinstance(instance, library3Simplified_Library)

@given(instance=library3Simplified_Customer_strategy)
@settings(max_examples=50)
def test_library3simplified_customer_instantiation(instance):
    assert isinstance(instance, library3Simplified_Customer)



@given(instance=library3Simplified_Customer_strategy)
def test_library3simplified_customer_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=library3Simplified_Customer_strategy)
def test_library3simplified_customer_borrowedBookSince_setter(instance):
    original = instance.borrowedBookSince
    instance.borrowedBookSince = original
    assert instance.borrowedBookSince == original



@given(instance=library3Simplified_Customer_strategy)
def test_library3simplified_customer_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original
