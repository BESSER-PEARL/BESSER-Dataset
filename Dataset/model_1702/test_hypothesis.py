import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    library_t_published,
    library_t_author,
    library_t_book,
    library_t_library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library_t_published_is_not_abstract():
    assert not inspect.isabstract(library_t_published)


def test_library_t_published_constructor_exists():
    assert callable(library_t_published.__init__)


def test_library_t_published_constructor_args():
    sig = inspect.signature(library_t_published.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"
    assert "text" in params, "Missing parameter 'text'"

def test_library_t_published_has_tagName():
    assert hasattr(library_t_published, "tagName")
    descriptor = None
    for klass in library_t_published.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)

def test_library_t_published_has_text():
    assert hasattr(library_t_published, "text")
    descriptor = None
    for klass in library_t_published.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_library_t_author_is_not_abstract():
    assert not inspect.isabstract(library_t_author)


def test_library_t_author_constructor_exists():
    assert callable(library_t_author.__init__)


def test_library_t_author_constructor_args():
    sig = inspect.signature(library_t_author.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "tagName" in params, "Missing parameter 'tagName'"

def test_library_t_author_has_text():
    assert hasattr(library_t_author, "text")
    descriptor = None
    for klass in library_t_author.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_library_t_author_has_tagName():
    assert hasattr(library_t_author, "tagName")
    descriptor = None
    for klass in library_t_author.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)



def test_library_t_book_is_not_abstract():
    assert not inspect.isabstract(library_t_book)


def test_library_t_book_constructor_exists():
    assert callable(library_t_book.__init__)


def test_library_t_book_constructor_args():
    sig = inspect.signature(library_t_book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "tagName" in params, "Missing parameter 'tagName'"
    assert "text" in params, "Missing parameter 'text'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_library_t_book_has_title():
    assert hasattr(library_t_book, "title")
    descriptor = None
    for klass in library_t_book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library_t_book_has_tagName():
    assert hasattr(library_t_book, "tagName")
    descriptor = None
    for klass in library_t_book.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)

def test_library_t_book_has_text():
    assert hasattr(library_t_book, "text")
    descriptor = None
    for klass in library_t_book.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_library_t_book_has_pages():
    assert hasattr(library_t_book, "pages")
    descriptor = None
    for klass in library_t_book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_library_t_library_is_not_abstract():
    assert not inspect.isabstract(library_t_library)


def test_library_t_library_constructor_exists():
    assert callable(library_t_library.__init__)


def test_library_t_library_constructor_args():
    sig = inspect.signature(library_t_library.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"
    assert "text" in params, "Missing parameter 'text'"

def test_library_t_library_has_tagName():
    assert hasattr(library_t_library, "tagName")
    descriptor = None
    for klass in library_t_library.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)

def test_library_t_library_has_text():
    assert hasattr(library_t_library, "text")
    descriptor = None
    for klass in library_t_library.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
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
library_t_published_strategy = st.builds(
    library_t_published,
    tagName=
        safe_text,
    text=
        safe_text
)
library_t_author_strategy = st.builds(
    library_t_author,
    text=
        safe_text,
    tagName=
        safe_text
)
library_t_book_strategy = st.builds(
    library_t_book,
    title=
        safe_text,
    tagName=
        safe_text,
    text=
        safe_text,
    pages=
        st.integers()
)
library_t_library_strategy = st.builds(
    library_t_library,
    tagName=
        safe_text,
    text=
        safe_text
)

@given(instance=library_t_published_strategy)
@settings(max_examples=50)
def test_library_t_published_instantiation(instance):
    assert isinstance(instance, library_t_published)



@given(instance=library_t_published_strategy)
def test_library_t_published_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original



@given(instance=library_t_published_strategy)
def test_library_t_published_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=library_t_author_strategy)
@settings(max_examples=50)
def test_library_t_author_instantiation(instance):
    assert isinstance(instance, library_t_author)



@given(instance=library_t_author_strategy)
def test_library_t_author_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=library_t_author_strategy)
def test_library_t_author_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=library_t_book_strategy)
@settings(max_examples=50)
def test_library_t_book_instantiation(instance):
    assert isinstance(instance, library_t_book)



@given(instance=library_t_book_strategy)
def test_library_t_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=library_t_book_strategy)
def test_library_t_book_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original



@given(instance=library_t_book_strategy)
def test_library_t_book_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=library_t_book_strategy)
def test_library_t_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=library_t_library_strategy)
@settings(max_examples=50)
def test_library_t_library_instantiation(instance):
    assert isinstance(instance, library_t_library)



@given(instance=library_t_library_strategy)
def test_library_t_library_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original



@given(instance=library_t_library_strategy)
def test_library_t_library_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original
