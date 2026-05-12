import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    edatatypeColumn_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_edatatypecolumn_book_is_not_abstract():
    assert not inspect.isabstract(edatatypeColumn_Book)


def test_edatatypecolumn_book_constructor_exists():
    assert callable(edatatypeColumn_Book.__init__)


def test_edatatypecolumn_book_constructor_args():
    sig = inspect.signature(edatatypeColumn_Book.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "title" in params, "Missing parameter 'title'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_edatatypecolumn_book_has_author():
    assert hasattr(edatatypeColumn_Book, "author")
    descriptor = None
    for klass in edatatypeColumn_Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_edatatypecolumn_book_has_weight():
    assert hasattr(edatatypeColumn_Book, "weight")
    descriptor = None
    for klass in edatatypeColumn_Book.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_edatatypecolumn_book_has_title():
    assert hasattr(edatatypeColumn_Book, "title")
    descriptor = None
    for klass in edatatypeColumn_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_edatatypecolumn_book_has_pages():
    assert hasattr(edatatypeColumn_Book, "pages")
    descriptor = None
    for klass in edatatypeColumn_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
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
edatatypeColumn_Book_strategy = st.builds(
    edatatypeColumn_Book,
    author=
        safe_text,
    weight=
        safe_text,
    title=
        safe_text,
    pages=
        safe_text
)

@given(instance=edatatypeColumn_Book_strategy)
@settings(max_examples=50)
def test_edatatypecolumn_book_instantiation(instance):
    assert isinstance(instance, edatatypeColumn_Book)



@given(instance=edatatypeColumn_Book_strategy)
def test_edatatypecolumn_book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=edatatypeColumn_Book_strategy)
def test_edatatypecolumn_book_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=edatatypeColumn_Book_strategy)
def test_edatatypecolumn_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=edatatypeColumn_Book_strategy)
def test_edatatypecolumn_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original
