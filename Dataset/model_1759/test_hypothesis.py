import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    library_book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library_book_is_not_abstract():
    assert not inspect.isabstract(library_book)


def test_library_book_constructor_exists():
    assert callable(library_book.__init__)


def test_library_book_constructor_args():
    sig = inspect.signature(library_book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "author" in params, "Missing parameter 'author'"
    assert "published" in params, "Missing parameter 'published'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_library_book_has_title():
    assert hasattr(library_book, "title")
    descriptor = None
    for klass in library_book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library_book_has_author():
    assert hasattr(library_book, "author")
    descriptor = None
    for klass in library_book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_library_book_has_published():
    assert hasattr(library_book, "published")
    descriptor = None
    for klass in library_book.__mro__:
        if "published" in klass.__dict__:
            descriptor = klass.__dict__["published"]
            break
    assert isinstance(descriptor, property)

def test_library_book_has_pages():
    assert hasattr(library_book, "pages")
    descriptor = None
    for klass in library_book.__mro__:
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
library_book_strategy = st.builds(
    library_book,
    title=
        safe_text,
    author=
        safe_text,
    published=
        safe_text,
    pages=
        safe_text
)

@given(instance=library_book_strategy)
@settings(max_examples=50)
def test_library_book_instantiation(instance):
    assert isinstance(instance, library_book)



@given(instance=library_book_strategy)
def test_library_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=library_book_strategy)
def test_library_book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=library_book_strategy)
def test_library_book_published_setter(instance):
    original = instance.published
    instance.published = original
    assert instance.published == original



@given(instance=library_book_strategy)
def test_library_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original
