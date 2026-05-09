import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    books::Title,
    books::Book,
    books::Bookstore,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_books::title_is_not_abstract():
    assert not inspect.isabstract(books::Title)


def test_books::title_constructor_exists():
    assert callable(books::Title.__init__)


def test_books::title_constructor_args():
    sig = inspect.signature(books::Title.__init__)
    params = list(sig.parameters.keys())
    assert "lan" in params, "Missing parameter 'lan'"
    assert "text" in params, "Missing parameter 'text'"

def test_books::title_has_lan():
    assert hasattr(books::Title, "lan")
    descriptor = None
    for klass in books::Title.__mro__:
        if "lan" in klass.__dict__:
            descriptor = klass.__dict__["lan"]
            break
    assert isinstance(descriptor, property)

def test_books::title_has_text():
    assert hasattr(books::Title, "text")
    descriptor = None
    for klass in books::Title.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_books::book_is_not_abstract():
    assert not inspect.isabstract(books::Book)


def test_books::book_constructor_exists():
    assert callable(books::Book.__init__)


def test_books::book_constructor_args():
    sig = inspect.signature(books::Book.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "author" in params, "Missing parameter 'author'"
    assert "price" in params, "Missing parameter 'price'"

def test_books::book_has_year():
    assert hasattr(books::Book, "year")
    descriptor = None
    for klass in books::Book.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_books::book_has_author():
    assert hasattr(books::Book, "author")
    descriptor = None
    for klass in books::Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_books::book_has_price():
    assert hasattr(books::Book, "price")
    descriptor = None
    for klass in books::Book.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_books::bookstore_is_not_abstract():
    assert not inspect.isabstract(books::Bookstore)


def test_books::bookstore_constructor_exists():
    assert callable(books::Bookstore.__init__)


def test_books::bookstore_constructor_args():
    sig = inspect.signature(books::Bookstore.__init__)
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
books::Title_strategy = st.builds(
    books::Title,
    lan=
        safe_text,
    text=
        safe_text
)
books::Book_strategy = st.builds(
    books::Book,
    year=
        safe_text,
    author=
        safe_text,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
books::Bookstore_strategy = st.builds(
    books::Bookstore,
)

@given(instance=books::Title_strategy)
@settings(max_examples=50)
def test_books::title_instantiation(instance):
    assert isinstance(instance, books::Title)

@given(instance=books::Title_strategy)
def test_books::title_lan_type(instance):
    assert isinstance(instance.lan, str)


@given(instance=books::Title_strategy)
def test_books::title_lan_setter(instance):
    original = instance.lan
    instance.lan = original
    assert instance.lan == original

@given(instance=books::Title_strategy)
def test_books::title_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=books::Title_strategy)
def test_books::title_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=books::Book_strategy)
@settings(max_examples=50)
def test_books::book_instantiation(instance):
    assert isinstance(instance, books::Book)

@given(instance=books::Book_strategy)
def test_books::book_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=books::Book_strategy)
def test_books::book_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=books::Book_strategy)
def test_books::book_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=books::Book_strategy)
def test_books::book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=books::Book_strategy)
def test_books::book_price_type(instance):
    assert isinstance(instance.price, float)


@given(instance=books::Book_strategy)
def test_books::book_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=books::Bookstore_strategy)
@settings(max_examples=50)
def test_books::bookstore_instantiation(instance):
    assert isinstance(instance, books::Bookstore)
