import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    book::Article,
    book::Person,
    book::Book,
    book::DocBook,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_book::article_is_not_abstract():
    assert not inspect.isabstract(book::Article)


def test_book::article_constructor_exists():
    assert callable(book::Article.__init__)


def test_book::article_constructor_args():
    sig = inspect.signature(book::Article.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_book::article_has_title():
    assert hasattr(book::Article, "title")
    descriptor = None
    for klass in book::Article.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_book::person_is_not_abstract():
    assert not inspect.isabstract(book::Person)


def test_book::person_constructor_exists():
    assert callable(book::Person.__init__)


def test_book::person_constructor_args():
    sig = inspect.signature(book::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_book::person_has_name():
    assert hasattr(book::Person, "name")
    descriptor = None
    for klass in book::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_book::book_is_not_abstract():
    assert not inspect.isabstract(book::Book)


def test_book::book_constructor_exists():
    assert callable(book::Book.__init__)


def test_book::book_constructor_args():
    sig = inspect.signature(book::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_book::book_has_title():
    assert hasattr(book::Book, "title")
    descriptor = None
    for klass in book::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_book::docbook_is_not_abstract():
    assert not inspect.isabstract(book::DocBook)


def test_book::docbook_constructor_exists():
    assert callable(book::DocBook.__init__)


def test_book::docbook_constructor_args():
    sig = inspect.signature(book::DocBook.__init__)
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
book::Article_strategy = st.builds(
    book::Article,
    title=
        safe_text
)
book::Person_strategy = st.builds(
    book::Person,
    name=
        safe_text
)
book::Book_strategy = st.builds(
    book::Book,
    title=
        safe_text
)
book::DocBook_strategy = st.builds(
    book::DocBook,
)

@given(instance=book::Article_strategy)
@settings(max_examples=50)
def test_book::article_instantiation(instance):
    assert isinstance(instance, book::Article)

@given(instance=book::Article_strategy)
def test_book::article_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=book::Article_strategy)
def test_book::article_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=book::Person_strategy)
@settings(max_examples=50)
def test_book::person_instantiation(instance):
    assert isinstance(instance, book::Person)

@given(instance=book::Person_strategy)
def test_book::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=book::Person_strategy)
def test_book::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=book::Book_strategy)
@settings(max_examples=50)
def test_book::book_instantiation(instance):
    assert isinstance(instance, book::Book)

@given(instance=book::Book_strategy)
def test_book::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=book::Book_strategy)
def test_book::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=book::DocBook_strategy)
@settings(max_examples=50)
def test_book::docbook_instantiation(instance):
    assert isinstance(instance, book::DocBook)
