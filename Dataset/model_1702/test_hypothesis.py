import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    library::t::published,
    library::t::author,
    library::t::book,
    library::t::library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::t::published_is_not_abstract():
    assert not inspect.isabstract(library::t::published)


def test_library::t::published_constructor_exists():
    assert callable(library::t::published.__init__)


def test_library::t::published_constructor_args():
    sig = inspect.signature(library::t::published.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "tagName" in params, "Missing parameter 'tagName'"

def test_library::t::published_has_text():
    assert hasattr(library::t::published, "text")
    descriptor = None
    for klass in library::t::published.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_library::t::published_has_tagName():
    assert hasattr(library::t::published, "tagName")
    descriptor = None
    for klass in library::t::published.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)



def test_library::t::author_is_not_abstract():
    assert not inspect.isabstract(library::t::author)


def test_library::t::author_constructor_exists():
    assert callable(library::t::author.__init__)


def test_library::t::author_constructor_args():
    sig = inspect.signature(library::t::author.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"
    assert "text" in params, "Missing parameter 'text'"

def test_library::t::author_has_tagName():
    assert hasattr(library::t::author, "tagName")
    descriptor = None
    for klass in library::t::author.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)

def test_library::t::author_has_text():
    assert hasattr(library::t::author, "text")
    descriptor = None
    for klass in library::t::author.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_library::t::book_is_not_abstract():
    assert not inspect.isabstract(library::t::book)


def test_library::t::book_constructor_exists():
    assert callable(library::t::book.__init__)


def test_library::t::book_constructor_args():
    sig = inspect.signature(library::t::book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "text" in params, "Missing parameter 'text'"
    assert "tagName" in params, "Missing parameter 'tagName'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_library::t::book_has_title():
    assert hasattr(library::t::book, "title")
    descriptor = None
    for klass in library::t::book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library::t::book_has_text():
    assert hasattr(library::t::book, "text")
    descriptor = None
    for klass in library::t::book.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_library::t::book_has_tagName():
    assert hasattr(library::t::book, "tagName")
    descriptor = None
    for klass in library::t::book.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)

def test_library::t::book_has_pages():
    assert hasattr(library::t::book, "pages")
    descriptor = None
    for klass in library::t::book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_library::t::library_is_not_abstract():
    assert not inspect.isabstract(library::t::library)


def test_library::t::library_constructor_exists():
    assert callable(library::t::library.__init__)


def test_library::t::library_constructor_args():
    sig = inspect.signature(library::t::library.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "tagName" in params, "Missing parameter 'tagName'"

def test_library::t::library_has_text():
    assert hasattr(library::t::library, "text")
    descriptor = None
    for klass in library::t::library.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_library::t::library_has_tagName():
    assert hasattr(library::t::library, "tagName")
    descriptor = None
    for klass in library::t::library.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
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
library::t::published_strategy = st.builds(
    library::t::published,
    text=
        safe_text,
    tagName=
        safe_text
)
library::t::author_strategy = st.builds(
    library::t::author,
    tagName=
        safe_text,
    text=
        safe_text
)
library::t::book_strategy = st.builds(
    library::t::book,
    title=
        safe_text,
    text=
        safe_text,
    tagName=
        safe_text,
    pages=
        st.integers()
)
library::t::library_strategy = st.builds(
    library::t::library,
    text=
        safe_text,
    tagName=
        safe_text
)

@given(instance=library::t::published_strategy)
@settings(max_examples=50)
def test_library::t::published_instantiation(instance):
    assert isinstance(instance, library::t::published)

@given(instance=library::t::published_strategy)
def test_library::t::published_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=library::t::published_strategy)
def test_library::t::published_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=library::t::published_strategy)
def test_library::t::published_tagName_type(instance):
    assert isinstance(instance.tagName, str)


@given(instance=library::t::published_strategy)
def test_library::t::published_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=library::t::author_strategy)
@settings(max_examples=50)
def test_library::t::author_instantiation(instance):
    assert isinstance(instance, library::t::author)

@given(instance=library::t::author_strategy)
def test_library::t::author_tagName_type(instance):
    assert isinstance(instance.tagName, str)


@given(instance=library::t::author_strategy)
def test_library::t::author_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=library::t::author_strategy)
def test_library::t::author_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=library::t::author_strategy)
def test_library::t::author_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=library::t::book_strategy)
@settings(max_examples=50)
def test_library::t::book_instantiation(instance):
    assert isinstance(instance, library::t::book)

@given(instance=library::t::book_strategy)
def test_library::t::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::t::book_strategy)
def test_library::t::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library::t::book_strategy)
def test_library::t::book_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=library::t::book_strategy)
def test_library::t::book_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=library::t::book_strategy)
def test_library::t::book_tagName_type(instance):
    assert isinstance(instance.tagName, str)


@given(instance=library::t::book_strategy)
def test_library::t::book_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=library::t::book_strategy)
def test_library::t::book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=library::t::book_strategy)
def test_library::t::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=library::t::library_strategy)
@settings(max_examples=50)
def test_library::t::library_instantiation(instance):
    assert isinstance(instance, library::t::library)

@given(instance=library::t::library_strategy)
def test_library::t::library_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=library::t::library_strategy)
def test_library::t::library_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=library::t::library_strategy)
def test_library::t::library_tagName_type(instance):
    assert isinstance(instance.tagName, str)


@given(instance=library::t::library_strategy)
def test_library::t::library_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original
