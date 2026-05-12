import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    library_Image,
    library_Text,
    library_Content,
    library_Chapter,
    library_Book,
    library_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library_image_is_not_abstract():
    assert not inspect.isabstract(library_Image)


def test_library_image_constructor_exists():
    assert callable(library_Image.__init__)


def test_library_image_constructor_args():
    sig = inspect.signature(library_Image.__init__)
    params = list(sig.parameters.keys())



def test_library_text_is_not_abstract():
    assert not inspect.isabstract(library_Text)


def test_library_text_constructor_exists():
    assert callable(library_Text.__init__)


def test_library_text_constructor_args():
    sig = inspect.signature(library_Text.__init__)
    params = list(sig.parameters.keys())



def test_library_content_is_not_abstract():
    assert not inspect.isabstract(library_Content)


def test_library_content_constructor_exists():
    assert callable(library_Content.__init__)


def test_library_content_constructor_args():
    sig = inspect.signature(library_Content.__init__)
    params = list(sig.parameters.keys())



def test_library_chapter_is_not_abstract():
    assert not inspect.isabstract(library_Chapter)


def test_library_chapter_constructor_exists():
    assert callable(library_Chapter.__init__)


def test_library_chapter_constructor_args():
    sig = inspect.signature(library_Chapter.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "name" in params, "Missing parameter 'name'"

def test_library_chapter_has_pages():
    assert hasattr(library_Chapter, "pages")
    descriptor = None
    for klass in library_Chapter.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_library_chapter_has_name():
    assert hasattr(library_Chapter, "name")
    descriptor = None
    for klass in library_Chapter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library_book_is_not_abstract():
    assert not inspect.isabstract(library_Book)


def test_library_book_constructor_exists():
    assert callable(library_Book.__init__)


def test_library_book_constructor_args():
    sig = inspect.signature(library_Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library_book_has_name():
    assert hasattr(library_Book, "name")
    descriptor = None
    for klass in library_Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library_library_is_not_abstract():
    assert not inspect.isabstract(library_Library)


def test_library_library_constructor_exists():
    assert callable(library_Library.__init__)


def test_library_library_constructor_args():
    sig = inspect.signature(library_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library_library_has_name():
    assert hasattr(library_Library, "name")
    descriptor = None
    for klass in library_Library.__mro__:
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
library_Image_strategy = st.builds(
    library_Image,
)
library_Text_strategy = st.builds(
    library_Text,
)
library_Content_strategy = st.builds(
    library_Content,
)
library_Chapter_strategy = st.builds(
    library_Chapter,
    pages=
        st.integers(),
    name=
        safe_text
)
library_Book_strategy = st.builds(
    library_Book,
    name=
        safe_text
)
library_Library_strategy = st.builds(
    library_Library,
    name=
        safe_text
)

@given(instance=library_Image_strategy)
@settings(max_examples=50)
def test_library_image_instantiation(instance):
    assert isinstance(instance, library_Image)

@given(instance=library_Text_strategy)
@settings(max_examples=50)
def test_library_text_instantiation(instance):
    assert isinstance(instance, library_Text)

@given(instance=library_Content_strategy)
@settings(max_examples=50)
def test_library_content_instantiation(instance):
    assert isinstance(instance, library_Content)

@given(instance=library_Chapter_strategy)
@settings(max_examples=50)
def test_library_chapter_instantiation(instance):
    assert isinstance(instance, library_Chapter)



@given(instance=library_Chapter_strategy)
def test_library_chapter_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=library_Chapter_strategy)
def test_library_chapter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library_Book_strategy)
@settings(max_examples=50)
def test_library_book_instantiation(instance):
    assert isinstance(instance, library_Book)



@given(instance=library_Book_strategy)
def test_library_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library_Library_strategy)
@settings(max_examples=50)
def test_library_library_instantiation(instance):
    assert isinstance(instance, library_Library)



@given(instance=library_Library_strategy)
def test_library_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
