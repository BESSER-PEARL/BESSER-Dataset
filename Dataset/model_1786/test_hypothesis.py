import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    column_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_column_book_is_not_abstract():
    assert not inspect.isabstract(column_Book)


def test_column_book_constructor_exists():
    assert callable(column_Book.__init__)


def test_column_book_constructor_args():
    sig = inspect.signature(column_Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"
    assert "author" in params, "Missing parameter 'author'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_column_book_has_pages():
    assert hasattr(column_Book, "pages")
    descriptor = None
    for klass in column_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_column_book_has_title():
    assert hasattr(column_Book, "title")
    descriptor = None
    for klass in column_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_column_book_has_author():
    assert hasattr(column_Book, "author")
    descriptor = None
    for klass in column_Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_column_book_has_weight():
    assert hasattr(column_Book, "weight")
    descriptor = None
    for klass in column_Book.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
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
column_Book_strategy = st.builds(
    column_Book,
    pages=
        safe_text,
    title=
        safe_text,
    author=
        safe_text,
    weight=
        safe_text
)

@given(instance=column_Book_strategy)
@settings(max_examples=50)
def test_column_book_instantiation(instance):
    assert isinstance(instance, column_Book)



@given(instance=column_Book_strategy)
def test_column_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=column_Book_strategy)
def test_column_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=column_Book_strategy)
def test_column_book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=column_Book_strategy)
def test_column_book_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original
