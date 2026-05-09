import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BookStorePackage::Book,
    BookStorePackage::BookStore,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bookstorepackage::book_is_not_abstract():
    assert not inspect.isabstract(BookStorePackage::Book)


def test_bookstorepackage::book_constructor_exists():
    assert callable(BookStorePackage::Book.__init__)


def test_bookstorepackage::book_constructor_args():
    sig = inspect.signature(BookStorePackage::Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isbn" in params, "Missing parameter 'isbn'"

def test_bookstorepackage::book_has_name():
    assert hasattr(BookStorePackage::Book, "name")
    descriptor = None
    for klass in BookStorePackage::Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bookstorepackage::book_has_isbn():
    assert hasattr(BookStorePackage::Book, "isbn")
    descriptor = None
    for klass in BookStorePackage::Book.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)



def test_bookstorepackage::bookstore_is_not_abstract():
    assert not inspect.isabstract(BookStorePackage::BookStore)


def test_bookstorepackage::bookstore_constructor_exists():
    assert callable(BookStorePackage::BookStore.__init__)


def test_bookstorepackage::bookstore_constructor_args():
    sig = inspect.signature(BookStorePackage::BookStore.__init__)
    params = list(sig.parameters.keys())
    assert "owner" in params, "Missing parameter 'owner'"
    assert "location" in params, "Missing parameter 'location'"

def test_bookstorepackage::bookstore_has_owner():
    assert hasattr(BookStorePackage::BookStore, "owner")
    descriptor = None
    for klass in BookStorePackage::BookStore.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_bookstorepackage::bookstore_has_location():
    assert hasattr(BookStorePackage::BookStore, "location")
    descriptor = None
    for klass in BookStorePackage::BookStore.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
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
BookStorePackage::Book_strategy = st.builds(
    BookStorePackage::Book,
    name=
        safe_text,
    isbn=
        st.integers()
)
BookStorePackage::BookStore_strategy = st.builds(
    BookStorePackage::BookStore,
    owner=
        safe_text,
    location=
        safe_text
)

@given(instance=BookStorePackage::Book_strategy)
@settings(max_examples=50)
def test_bookstorepackage::book_instantiation(instance):
    assert isinstance(instance, BookStorePackage::Book)

@given(instance=BookStorePackage::Book_strategy)
def test_bookstorepackage::book_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BookStorePackage::Book_strategy)
def test_bookstorepackage::book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BookStorePackage::Book_strategy)
def test_bookstorepackage::book_isbn_type(instance):
    assert isinstance(instance.isbn, int)


@given(instance=BookStorePackage::Book_strategy)
def test_bookstorepackage::book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original

@given(instance=BookStorePackage::BookStore_strategy)
@settings(max_examples=50)
def test_bookstorepackage::bookstore_instantiation(instance):
    assert isinstance(instance, BookStorePackage::BookStore)

@given(instance=BookStorePackage::BookStore_strategy)
def test_bookstorepackage::bookstore_owner_type(instance):
    assert isinstance(instance.owner, str)


@given(instance=BookStorePackage::BookStore_strategy)
def test_bookstorepackage::bookstore_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original

@given(instance=BookStorePackage::BookStore_strategy)
def test_bookstorepackage::bookstore_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=BookStorePackage::BookStore_strategy)
def test_bookstorepackage::bookstore_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original
