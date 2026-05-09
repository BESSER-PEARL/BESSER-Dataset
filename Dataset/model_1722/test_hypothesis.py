import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    library::Image,
    library::Text,
    library::Content,
    library::Chapter,
    library::Book,
    library::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::image_is_not_abstract():
    assert not inspect.isabstract(library::Image)


def test_library::image_constructor_exists():
    assert callable(library::Image.__init__)


def test_library::image_constructor_args():
    sig = inspect.signature(library::Image.__init__)
    params = list(sig.parameters.keys())



def test_library::text_is_not_abstract():
    assert not inspect.isabstract(library::Text)


def test_library::text_constructor_exists():
    assert callable(library::Text.__init__)


def test_library::text_constructor_args():
    sig = inspect.signature(library::Text.__init__)
    params = list(sig.parameters.keys())



def test_library::content_is_not_abstract():
    assert not inspect.isabstract(library::Content)


def test_library::content_constructor_exists():
    assert callable(library::Content.__init__)


def test_library::content_constructor_args():
    sig = inspect.signature(library::Content.__init__)
    params = list(sig.parameters.keys())



def test_library::chapter_is_not_abstract():
    assert not inspect.isabstract(library::Chapter)


def test_library::chapter_constructor_exists():
    assert callable(library::Chapter.__init__)


def test_library::chapter_constructor_args():
    sig = inspect.signature(library::Chapter.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "name" in params, "Missing parameter 'name'"

def test_library::chapter_has_pages():
    assert hasattr(library::Chapter, "pages")
    descriptor = None
    for klass in library::Chapter.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_library::chapter_has_name():
    assert hasattr(library::Chapter, "name")
    descriptor = None
    for klass in library::Chapter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::Book)


def test_library::book_constructor_exists():
    assert callable(library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::book_has_name():
    assert hasattr(library::Book, "name")
    descriptor = None
    for klass in library::Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library::library_is_not_abstract():
    assert not inspect.isabstract(library::Library)


def test_library::library_constructor_exists():
    assert callable(library::Library.__init__)


def test_library::library_constructor_args():
    sig = inspect.signature(library::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::library_has_name():
    assert hasattr(library::Library, "name")
    descriptor = None
    for klass in library::Library.__mro__:
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
library::Image_strategy = st.builds(
    library::Image,
)
library::Text_strategy = st.builds(
    library::Text,
)
library::Content_strategy = st.builds(
    library::Content,
)
library::Chapter_strategy = st.builds(
    library::Chapter,
    pages=
        st.integers(),
    name=
        safe_text
)
library::Book_strategy = st.builds(
    library::Book,
    name=
        safe_text
)
library::Library_strategy = st.builds(
    library::Library,
    name=
        safe_text
)

@given(instance=library::Image_strategy)
@settings(max_examples=50)
def test_library::image_instantiation(instance):
    assert isinstance(instance, library::Image)

@given(instance=library::Text_strategy)
@settings(max_examples=50)
def test_library::text_instantiation(instance):
    assert isinstance(instance, library::Text)

@given(instance=library::Content_strategy)
@settings(max_examples=50)
def test_library::content_instantiation(instance):
    assert isinstance(instance, library::Content)

@given(instance=library::Chapter_strategy)
@settings(max_examples=50)
def test_library::chapter_instantiation(instance):
    assert isinstance(instance, library::Chapter)

@given(instance=library::Chapter_strategy)
def test_library::chapter_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=library::Chapter_strategy)
def test_library::chapter_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=library::Chapter_strategy)
def test_library::chapter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Chapter_strategy)
def test_library::chapter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::Book)

@given(instance=library::Book_strategy)
def test_library::book_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Book_strategy)
def test_library::book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library::Library_strategy)
@settings(max_examples=50)
def test_library::library_instantiation(instance):
    assert isinstance(instance, library::Library)

@given(instance=library::Library_strategy)
def test_library::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Library_strategy)
def test_library::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
