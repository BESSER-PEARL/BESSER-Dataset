import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BookStorePackage_Book,
    BookStorePackage_BookStore,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bookstorepackage_book_is_not_abstract():
    assert not inspect.isabstract(BookStorePackage_Book)


def test_bookstorepackage_book_constructor_exists():
    assert callable(BookStorePackage_Book.__init__)


def test_bookstorepackage_book_constructor_args():
    sig = inspect.signature(BookStorePackage_Book.__init__)
    params = list(sig.parameters.keys())
    assert "isbn" in params, "Missing parameter 'isbn'"
    assert "name" in params, "Missing parameter 'name'"

def test_bookstorepackage_book_has_isbn():
    assert hasattr(BookStorePackage_Book, "isbn")
    descriptor = None
    for klass in BookStorePackage_Book.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)

def test_bookstorepackage_book_has_name():
    assert hasattr(BookStorePackage_Book, "name")
    descriptor = None
    for klass in BookStorePackage_Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bookstorepackage_bookstore_is_not_abstract():
    assert not inspect.isabstract(BookStorePackage_BookStore)


def test_bookstorepackage_bookstore_constructor_exists():
    assert callable(BookStorePackage_BookStore.__init__)


def test_bookstorepackage_bookstore_constructor_args():
    sig = inspect.signature(BookStorePackage_BookStore.__init__)
    params = list(sig.parameters.keys())
    assert "owner" in params, "Missing parameter 'owner'"
    assert "location" in params, "Missing parameter 'location'"

def test_bookstorepackage_bookstore_has_owner():
    assert hasattr(BookStorePackage_BookStore, "owner")
    descriptor = None
    for klass in BookStorePackage_BookStore.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_bookstorepackage_bookstore_has_location():
    assert hasattr(BookStorePackage_BookStore, "location")
    descriptor = None
    for klass in BookStorePackage_BookStore.__mro__:
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
BookStorePackage_Book_strategy = st.builds(
    BookStorePackage_Book,
    isbn=
        st.integers(),
    name=
        safe_text
)
BookStorePackage_BookStore_strategy = st.builds(
    BookStorePackage_BookStore,
    owner=
        safe_text,
    location=
        safe_text
)

@given(instance=BookStorePackage_Book_strategy)
@settings(max_examples=50)
def test_bookstorepackage_book_instantiation(instance):
    assert isinstance(instance, BookStorePackage_Book)



@given(instance=BookStorePackage_Book_strategy)
def test_bookstorepackage_book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original



@given(instance=BookStorePackage_Book_strategy)
def test_bookstorepackage_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BookStorePackage_BookStore_strategy)
@settings(max_examples=50)
def test_bookstorepackage_bookstore_instantiation(instance):
    assert isinstance(instance, BookStorePackage_BookStore)



@given(instance=BookStorePackage_BookStore_strategy)
def test_bookstorepackage_bookstore_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original



@given(instance=BookStorePackage_BookStore_strategy)
def test_bookstorepackage_bookstore_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original
