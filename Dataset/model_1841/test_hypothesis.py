import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    books_Title,
    books_Book,
    books_Bookstore,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_books_title_is_not_abstract():
    assert not inspect.isabstract(books_Title)


def test_books_title_constructor_exists():
    assert callable(books_Title.__init__)


def test_books_title_constructor_args():
    sig = inspect.signature(books_Title.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "lan" in params, "Missing parameter 'lan'"

def test_books_title_has_text():
    assert hasattr(books_Title, "text")
    descriptor = None
    for klass in books_Title.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_books_title_has_lan():
    assert hasattr(books_Title, "lan")
    descriptor = None
    for klass in books_Title.__mro__:
        if "lan" in klass.__dict__:
            descriptor = klass.__dict__["lan"]
            break
    assert isinstance(descriptor, property)



def test_books_book_is_not_abstract():
    assert not inspect.isabstract(books_Book)


def test_books_book_constructor_exists():
    assert callable(books_Book.__init__)


def test_books_book_constructor_args():
    sig = inspect.signature(books_Book.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "author" in params, "Missing parameter 'author'"
    assert "year" in params, "Missing parameter 'year'"

def test_books_book_has_price():
    assert hasattr(books_Book, "price")
    descriptor = None
    for klass in books_Book.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_books_book_has_author():
    assert hasattr(books_Book, "author")
    descriptor = None
    for klass in books_Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_books_book_has_year():
    assert hasattr(books_Book, "year")
    descriptor = None
    for klass in books_Book.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_books_bookstore_is_not_abstract():
    assert not inspect.isabstract(books_Bookstore)


def test_books_bookstore_constructor_exists():
    assert callable(books_Bookstore.__init__)


def test_books_bookstore_constructor_args():
    sig = inspect.signature(books_Bookstore.__init__)
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
books_Title_strategy = st.builds(
    books_Title,
    text=
        safe_text,
    lan=
        safe_text
)
books_Book_strategy = st.builds(
    books_Book,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    author=
        safe_text,
    year=
        safe_text
)
books_Bookstore_strategy = st.builds(
    books_Bookstore,
)

@given(instance=books_Title_strategy)
@settings(max_examples=50)
def test_books_title_instantiation(instance):
    assert isinstance(instance, books_Title)



@given(instance=books_Title_strategy)
def test_books_title_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=books_Title_strategy)
def test_books_title_lan_setter(instance):
    original = instance.lan
    instance.lan = original
    assert instance.lan == original

@given(instance=books_Book_strategy)
@settings(max_examples=50)
def test_books_book_instantiation(instance):
    assert isinstance(instance, books_Book)



@given(instance=books_Book_strategy)
def test_books_book_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=books_Book_strategy)
def test_books_book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=books_Book_strategy)
def test_books_book_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=books_Bookstore_strategy)
@settings(max_examples=50)
def test_books_bookstore_instantiation(instance):
    assert isinstance(instance, books_Bookstore)
