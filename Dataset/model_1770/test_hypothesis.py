import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    book_Book,
    book_DocBook,
    book_Article,
    book_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_book_book_is_not_abstract():
    assert not inspect.isabstract(book_Book)


def test_book_book_constructor_exists():
    assert callable(book_Book.__init__)


def test_book_book_constructor_args():
    sig = inspect.signature(book_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_book_book_has_title():
    assert hasattr(book_Book, "title")
    descriptor = None
    for klass in book_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_book_docbook_is_not_abstract():
    assert not inspect.isabstract(book_DocBook)


def test_book_docbook_constructor_exists():
    assert callable(book_DocBook.__init__)


def test_book_docbook_constructor_args():
    sig = inspect.signature(book_DocBook.__init__)
    params = list(sig.parameters.keys())



def test_book_article_is_not_abstract():
    assert not inspect.isabstract(book_Article)


def test_book_article_constructor_exists():
    assert callable(book_Article.__init__)


def test_book_article_constructor_args():
    sig = inspect.signature(book_Article.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_book_article_has_title():
    assert hasattr(book_Article, "title")
    descriptor = None
    for klass in book_Article.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_book_person_is_not_abstract():
    assert not inspect.isabstract(book_Person)


def test_book_person_constructor_exists():
    assert callable(book_Person.__init__)


def test_book_person_constructor_args():
    sig = inspect.signature(book_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_book_person_has_name():
    assert hasattr(book_Person, "name")
    descriptor = None
    for klass in book_Person.__mro__:
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
book_Book_strategy = st.builds(
    book_Book,
    title=
        safe_text
)
book_DocBook_strategy = st.builds(
    book_DocBook,
)
book_Article_strategy = st.builds(
    book_Article,
    title=
        safe_text
)
book_Person_strategy = st.builds(
    book_Person,
    name=
        safe_text
)

@given(instance=book_Book_strategy)
@settings(max_examples=50)
def test_book_book_instantiation(instance):
    assert isinstance(instance, book_Book)



@given(instance=book_Book_strategy)
def test_book_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=book_DocBook_strategy)
@settings(max_examples=50)
def test_book_docbook_instantiation(instance):
    assert isinstance(instance, book_DocBook)

@given(instance=book_Article_strategy)
@settings(max_examples=50)
def test_book_article_instantiation(instance):
    assert isinstance(instance, book_Article)



@given(instance=book_Article_strategy)
def test_book_article_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=book_Person_strategy)
@settings(max_examples=50)
def test_book_person_instantiation(instance):
    assert isinstance(instance, book_Person)



@given(instance=book_Person_strategy)
def test_book_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
