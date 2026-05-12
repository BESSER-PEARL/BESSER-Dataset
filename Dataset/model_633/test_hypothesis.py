import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    library_BorrowedItem,
    library_User,
    library_Book,
    library_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library_borroweditem_is_not_abstract():
    assert not inspect.isabstract(library_BorrowedItem)


def test_library_borroweditem_constructor_exists():
    assert callable(library_BorrowedItem.__init__)


def test_library_borroweditem_constructor_args():
    sig = inspect.signature(library_BorrowedItem.__init__)
    params = list(sig.parameters.keys())
    assert "borrowDate" in params, "Missing parameter 'borrowDate'"
    assert "lastReturnDate" in params, "Missing parameter 'lastReturnDate'"

def test_library_borroweditem_has_borrowDate():
    assert hasattr(library_BorrowedItem, "borrowDate")
    descriptor = None
    for klass in library_BorrowedItem.__mro__:
        if "borrowDate" in klass.__dict__:
            descriptor = klass.__dict__["borrowDate"]
            break
    assert isinstance(descriptor, property)

def test_library_borroweditem_has_lastReturnDate():
    assert hasattr(library_BorrowedItem, "lastReturnDate")
    descriptor = None
    for klass in library_BorrowedItem.__mro__:
        if "lastReturnDate" in klass.__dict__:
            descriptor = klass.__dict__["lastReturnDate"]
            break
    assert isinstance(descriptor, property)



def test_library_user_is_not_abstract():
    assert not inspect.isabstract(library_User)


def test_library_user_constructor_exists():
    assert callable(library_User.__init__)


def test_library_user_constructor_args():
    sig = inspect.signature(library_User.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library_user_has_name():
    assert hasattr(library_User, "name")
    descriptor = None
    for klass in library_User.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library_book_is_not_abstract():
    assert not inspect.isabstract(library_Book)


def test_library_book_constructor_exists():
    assert callable(library_Book.__init__)


def test_library_book_constructor_args():
    sig = inspect.signature(library_Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "author" in params, "Missing parameter 'author'"

def test_library_book_has_name():
    assert hasattr(library_Book, "name")
    descriptor = None
    for klass in library_Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_library_book_has_author():
    assert hasattr(library_Book, "author")
    descriptor = None
    for klass in library_Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)



def test_library_library_is_not_abstract():
    assert not inspect.isabstract(library_Library)


def test_library_library_constructor_exists():
    assert callable(library_Library.__init__)


def test_library_library_constructor_args():
    sig = inspect.signature(library_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library_library_has_name():
    assert hasattr(library_Library, "name")
    descriptor = None
    for klass in library_Library.__mro__:
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
library_BorrowedItem_strategy = st.builds(
    library_BorrowedItem,
    borrowDate=
        st.dates(),
    lastReturnDate=
        st.dates()
)
library_User_strategy = st.builds(
    library_User,
    name=
        safe_text
)
library_Book_strategy = st.builds(
    library_Book,
    name=
        safe_text,
    author=
        safe_text
)
library_Library_strategy = st.builds(
    library_Library,
    name=
        safe_text
)

@given(instance=library_BorrowedItem_strategy)
@settings(max_examples=50)
def test_library_borroweditem_instantiation(instance):
    assert isinstance(instance, library_BorrowedItem)



@given(instance=library_BorrowedItem_strategy)
def test_library_borroweditem_borrowDate_setter(instance):
    original = instance.borrowDate
    instance.borrowDate = original
    assert instance.borrowDate == original



@given(instance=library_BorrowedItem_strategy)
def test_library_borroweditem_lastReturnDate_setter(instance):
    original = instance.lastReturnDate
    instance.lastReturnDate = original
    assert instance.lastReturnDate == original

@given(instance=library_User_strategy)
@settings(max_examples=50)
def test_library_user_instantiation(instance):
    assert isinstance(instance, library_User)



@given(instance=library_User_strategy)
def test_library_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library_Book_strategy)
@settings(max_examples=50)
def test_library_book_instantiation(instance):
    assert isinstance(instance, library_Book)



@given(instance=library_Book_strategy)
def test_library_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=library_Book_strategy)
def test_library_book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=library_Library_strategy)
@settings(max_examples=50)
def test_library_library_instantiation(instance):
    assert isinstance(instance, library_Library)



@given(instance=library_Library_strategy)
def test_library_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
