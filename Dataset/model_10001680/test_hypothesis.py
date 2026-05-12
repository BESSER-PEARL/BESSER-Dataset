import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    library_data_base,
    Book,
    patron,
    librarian,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library_data_base_is_not_abstract():
    assert not inspect.isabstract(library_data_base)


def test_library_data_base_constructor_exists():
    assert callable(library_data_base.__init__)


def test_library_data_base_constructor_args():
    sig = inspect.signature(library_data_base.__init__)
    params = list(sig.parameters.keys())
    assert "record_patron_borrowing_book" in params, "Missing parameter 'record_patron_borrowing_book'"
    assert "list_of_books" in params, "Missing parameter 'list_of_books'"
    assert "members_information" in params, "Missing parameter 'members_information'"

def test_library_data_base_has_record_patron_borrowing_book():
    assert hasattr(library_data_base, "record_patron_borrowing_book")
    descriptor = None
    for klass in library_data_base.__mro__:
        if "record_patron_borrowing_book" in klass.__dict__:
            descriptor = klass.__dict__["record_patron_borrowing_book"]
            break
    assert isinstance(descriptor, property)

def test_library_data_base_has_list_of_books():
    assert hasattr(library_data_base, "list_of_books")
    descriptor = None
    for klass in library_data_base.__mro__:
        if "list_of_books" in klass.__dict__:
            descriptor = klass.__dict__["list_of_books"]
            break
    assert isinstance(descriptor, property)

def test_library_data_base_has_members_information():
    assert hasattr(library_data_base, "members_information")
    descriptor = None
    for klass in library_data_base.__mro__:
        if "members_information" in klass.__dict__:
            descriptor = klass.__dict__["members_information"]
            break
    assert isinstance(descriptor, property)



def test_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_book_constructor_exists():
    assert callable(Book.__init__)


def test_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())
    assert "Book_ISBN" in params, "Missing parameter 'Book_ISBN'"
    assert "Book_Author" in params, "Missing parameter 'Book_Author'"
    assert "book_name" in params, "Missing parameter 'book_name'"

def test_book_has_Book_ISBN():
    assert hasattr(Book, "Book_ISBN")
    descriptor = None
    for klass in Book.__mro__:
        if "Book_ISBN" in klass.__dict__:
            descriptor = klass.__dict__["Book_ISBN"]
            break
    assert isinstance(descriptor, property)

def test_book_has_Book_Author():
    assert hasattr(Book, "Book_Author")
    descriptor = None
    for klass in Book.__mro__:
        if "Book_Author" in klass.__dict__:
            descriptor = klass.__dict__["Book_Author"]
            break
    assert isinstance(descriptor, property)

def test_book_has_book_name():
    assert hasattr(Book, "book_name")
    descriptor = None
    for klass in Book.__mro__:
        if "book_name" in klass.__dict__:
            descriptor = klass.__dict__["book_name"]
            break
    assert isinstance(descriptor, property)



def test_patron_is_not_abstract():
    assert not inspect.isabstract(patron)


def test_patron_constructor_exists():
    assert callable(patron.__init__)


def test_patron_constructor_args():
    sig = inspect.signature(patron.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Contact_number" in params, "Missing parameter 'Contact_number'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_patron_has_Address():
    assert hasattr(patron, "Address")
    descriptor = None
    for klass in patron.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_patron_has_Contact_number():
    assert hasattr(patron, "Contact_number")
    descriptor = None
    for klass in patron.__mro__:
        if "Contact_number" in klass.__dict__:
            descriptor = klass.__dict__["Contact_number"]
            break
    assert isinstance(descriptor, property)

def test_patron_has_Name():
    assert hasattr(patron, "Name")
    descriptor = None
    for klass in patron.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_librarian_is_not_abstract():
    assert not inspect.isabstract(librarian)


def test_librarian_constructor_exists():
    assert callable(librarian.__init__)


def test_librarian_constructor_args():
    sig = inspect.signature(librarian.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "name" in params, "Missing parameter 'name'"

def test_librarian_has_username():
    assert hasattr(librarian, "username")
    descriptor = None
    for klass in librarian.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_name():
    assert hasattr(librarian, "name")
    descriptor = None
    for klass in librarian.__mro__:
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
library_data_base_strategy = st.builds(
    library_data_base,
    record_patron_borrowing_book=
        st.integers(),
    list_of_books=
        safe_text,
    members_information=
        safe_text
)
Book_strategy = st.builds(
    Book,
    Book_ISBN=
        st.integers(),
    Book_Author=
        st.integers(),
    book_name=
        safe_text
)
patron_strategy = st.builds(
    patron,
    Address=
        safe_text,
    Contact_number=
        st.integers(),
    Name=
        safe_text
)
librarian_strategy = st.builds(
    librarian,
    username=
        st.integers(),
    name=
        safe_text
)

@given(instance=library_data_base_strategy)
@settings(max_examples=50)
def test_library_data_base_instantiation(instance):
    assert isinstance(instance, library_data_base)



@given(instance=library_data_base_strategy)
def test_library_data_base_record_patron_borrowing_book_setter(instance):
    original = instance.record_patron_borrowing_book
    instance.record_patron_borrowing_book = original
    assert instance.record_patron_borrowing_book == original



@given(instance=library_data_base_strategy)
def test_library_data_base_list_of_books_setter(instance):
    original = instance.list_of_books
    instance.list_of_books = original
    assert instance.list_of_books == original



@given(instance=library_data_base_strategy)
def test_library_data_base_members_information_setter(instance):
    original = instance.members_information
    instance.members_information = original
    assert instance.members_information == original

@given(instance=Book_strategy)
@settings(max_examples=50)
def test_book_instantiation(instance):
    assert isinstance(instance, Book)



@given(instance=Book_strategy)
def test_book_Book_ISBN_setter(instance):
    original = instance.Book_ISBN
    instance.Book_ISBN = original
    assert instance.Book_ISBN == original



@given(instance=Book_strategy)
def test_book_Book_Author_setter(instance):
    original = instance.Book_Author
    instance.Book_Author = original
    assert instance.Book_Author == original



@given(instance=Book_strategy)
def test_book_book_name_setter(instance):
    original = instance.book_name
    instance.book_name = original
    assert instance.book_name == original

@given(instance=patron_strategy)
@settings(max_examples=50)
def test_patron_instantiation(instance):
    assert isinstance(instance, patron)



@given(instance=patron_strategy)
def test_patron_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=patron_strategy)
def test_patron_Contact_number_setter(instance):
    original = instance.Contact_number
    instance.Contact_number = original
    assert instance.Contact_number == original



@given(instance=patron_strategy)
def test_patron_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=librarian_strategy)
@settings(max_examples=50)
def test_librarian_instantiation(instance):
    assert isinstance(instance, librarian)



@given(instance=librarian_strategy)
def test_librarian_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=librarian_strategy)
def test_librarian_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
