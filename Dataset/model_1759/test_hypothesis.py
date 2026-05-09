import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    library::book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::book)


def test_library::book_constructor_exists():
    assert callable(library::book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::book.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "title" in params, "Missing parameter 'title'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "published" in params, "Missing parameter 'published'"

def test_library::book_has_author():
    assert hasattr(library::book, "author")
    descriptor = None
    for klass in library::book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_title():
    assert hasattr(library::book, "title")
    descriptor = None
    for klass in library::book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_pages():
    assert hasattr(library::book, "pages")
    descriptor = None
    for klass in library::book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_published():
    assert hasattr(library::book, "published")
    descriptor = None
    for klass in library::book.__mro__:
        if "published" in klass.__dict__:
            descriptor = klass.__dict__["published"]
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
library::book_strategy = st.builds(
    library::book,
    author=
        safe_text,
    title=
        safe_text,
    pages=
        safe_text,
    published=
        safe_text
)

@given(instance=library::book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::book)

@given(instance=library::book_strategy)
def test_library::book_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=library::book_strategy)
def test_library::book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=library::book_strategy)
def test_library::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::book_strategy)
def test_library::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library::book_strategy)
def test_library::book_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=library::book_strategy)
def test_library::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=library::book_strategy)
def test_library::book_published_type(instance):
    assert isinstance(instance.published, str)


@given(instance=library::book_strategy)
def test_library::book_published_setter(instance):
    original = instance.published
    instance.published = original
    assert instance.published == original
