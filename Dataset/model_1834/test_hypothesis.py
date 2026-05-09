import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    edatatypeColumn::Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_edatatypecolumn::book_is_not_abstract():
    assert not inspect.isabstract(edatatypeColumn::Book)


def test_edatatypecolumn::book_constructor_exists():
    assert callable(edatatypeColumn::Book.__init__)


def test_edatatypecolumn::book_constructor_args():
    sig = inspect.signature(edatatypeColumn::Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "author" in params, "Missing parameter 'author'"

def test_edatatypecolumn::book_has_pages():
    assert hasattr(edatatypeColumn::Book, "pages")
    descriptor = None
    for klass in edatatypeColumn::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_edatatypecolumn::book_has_title():
    assert hasattr(edatatypeColumn::Book, "title")
    descriptor = None
    for klass in edatatypeColumn::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_edatatypecolumn::book_has_weight():
    assert hasattr(edatatypeColumn::Book, "weight")
    descriptor = None
    for klass in edatatypeColumn::Book.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_edatatypecolumn::book_has_author():
    assert hasattr(edatatypeColumn::Book, "author")
    descriptor = None
    for klass in edatatypeColumn::Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
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
edatatypeColumn::Book_strategy = st.builds(
    edatatypeColumn::Book,
    pages=
        safe_text,
    title=
        safe_text,
    weight=
        safe_text,
    author=
        safe_text
)

@given(instance=edatatypeColumn::Book_strategy)
@settings(max_examples=50)
def test_edatatypecolumn::book_instantiation(instance):
    assert isinstance(instance, edatatypeColumn::Book)

@given(instance=edatatypeColumn::Book_strategy)
def test_edatatypecolumn::book_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=edatatypeColumn::Book_strategy)
def test_edatatypecolumn::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=edatatypeColumn::Book_strategy)
def test_edatatypecolumn::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=edatatypeColumn::Book_strategy)
def test_edatatypecolumn::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=edatatypeColumn::Book_strategy)
def test_edatatypecolumn::book_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=edatatypeColumn::Book_strategy)
def test_edatatypecolumn::book_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=edatatypeColumn::Book_strategy)
def test_edatatypecolumn::book_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=edatatypeColumn::Book_strategy)
def test_edatatypecolumn::book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original
