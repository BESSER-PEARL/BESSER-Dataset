import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    library3Simplified::Book,
    library3Simplified::BookInfo,
    library3Simplified::Library,
    library3Simplified::Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library3simplified::book_is_not_abstract():
    assert not inspect.isabstract(library3Simplified::Book)


def test_library3simplified::book_constructor_exists():
    assert callable(library3Simplified::Book.__init__)


def test_library3simplified::book_constructor_args():
    sig = inspect.signature(library3Simplified::Book.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "isbn" in params, "Missing parameter 'isbn'"
    assert "title" in params, "Missing parameter 'title'"
    assert "name" in params, "Missing parameter 'name'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_library3simplified::book_has_author():
    assert hasattr(library3Simplified::Book, "author")
    descriptor = None
    for klass in library3Simplified::Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_library3simplified::book_has_isbn():
    assert hasattr(library3Simplified::Book, "isbn")
    descriptor = None
    for klass in library3Simplified::Book.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)

def test_library3simplified::book_has_title():
    assert hasattr(library3Simplified::Book, "title")
    descriptor = None
    for klass in library3Simplified::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library3simplified::book_has_name():
    assert hasattr(library3Simplified::Book, "name")
    descriptor = None
    for klass in library3Simplified::Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_library3simplified::book_has_pages():
    assert hasattr(library3Simplified::Book, "pages")
    descriptor = None
    for klass in library3Simplified::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_library3simplified::bookinfo_is_not_abstract():
    assert not inspect.isabstract(library3Simplified::BookInfo)


def test_library3simplified::bookinfo_constructor_exists():
    assert callable(library3Simplified::BookInfo.__init__)


def test_library3simplified::bookinfo_constructor_args():
    sig = inspect.signature(library3Simplified::BookInfo.__init__)
    params = list(sig.parameters.keys())



def test_library3simplified::library_is_not_abstract():
    assert not inspect.isabstract(library3Simplified::Library)


def test_library3simplified::library_constructor_exists():
    assert callable(library3Simplified::Library.__init__)


def test_library3simplified::library_constructor_args():
    sig = inspect.signature(library3Simplified::Library.__init__)
    params = list(sig.parameters.keys())



def test_library3simplified::customer_is_not_abstract():
    assert not inspect.isabstract(library3Simplified::Customer)


def test_library3simplified::customer_constructor_exists():
    assert callable(library3Simplified::Customer.__init__)


def test_library3simplified::customer_constructor_args():
    sig = inspect.signature(library3Simplified::Customer.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_library3simplified::customer_has_lastName():
    assert hasattr(library3Simplified::Customer, "lastName")
    descriptor = None
    for klass in library3Simplified::Customer.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_library3simplified::customer_has_firstName():
    assert hasattr(library3Simplified::Customer, "firstName")
    descriptor = None
    for klass in library3Simplified::Customer.__mro__:
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
library3Simplified::Book_strategy = st.builds(
    library3Simplified::Book,
    author=
        safe_text,
    isbn=
        safe_text,
    title=
        safe_text,
    name=
        safe_text,
    pages=
        st.integers()
)
library3Simplified::BookInfo_strategy = st.builds(
    library3Simplified::BookInfo,
)
library3Simplified::Library_strategy = st.builds(
    library3Simplified::Library,
)
library3Simplified::Customer_strategy = st.builds(
    library3Simplified::Customer,
    lastName=
        safe_text,
    firstName=
        safe_text
)

@given(instance=library3Simplified::Book_strategy)
@settings(max_examples=50)
def test_library3simplified::book_instantiation(instance):
    assert isinstance(instance, library3Simplified::Book)

@given(instance=library3Simplified::Book_strategy)
def test_library3simplified::book_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=library3Simplified::Book_strategy)
def test_library3simplified::book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=library3Simplified::Book_strategy)
def test_library3simplified::book_isbn_type(instance):
    assert isinstance(instance.isbn, str)


@given(instance=library3Simplified::Book_strategy)
def test_library3simplified::book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original

@given(instance=library3Simplified::Book_strategy)
def test_library3simplified::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library3Simplified::Book_strategy)
def test_library3simplified::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library3Simplified::Book_strategy)
def test_library3simplified::book_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library3Simplified::Book_strategy)
def test_library3simplified::book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library3Simplified::Book_strategy)
def test_library3simplified::book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=library3Simplified::Book_strategy)
def test_library3simplified::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=library3Simplified::BookInfo_strategy)
@settings(max_examples=50)
def test_library3simplified::bookinfo_instantiation(instance):
    assert isinstance(instance, library3Simplified::BookInfo)

@given(instance=library3Simplified::Library_strategy)
@settings(max_examples=50)
def test_library3simplified::library_instantiation(instance):
    assert isinstance(instance, library3Simplified::Library)

@given(instance=library3Simplified::Customer_strategy)
@settings(max_examples=50)
def test_library3simplified::customer_instantiation(instance):
    assert isinstance(instance, library3Simplified::Customer)

@given(instance=library3Simplified::Customer_strategy)
def test_library3simplified::customer_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=library3Simplified::Customer_strategy)
def test_library3simplified::customer_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=library3Simplified::Customer_strategy)
def test_library3simplified::customer_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=library3Simplified::Customer_strategy)
def test_library3simplified::customer_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original
