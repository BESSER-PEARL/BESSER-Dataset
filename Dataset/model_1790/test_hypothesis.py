import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BOOKS::Book,
    BOOKS::Chapter,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_books::book_is_not_abstract():
    assert not inspect.isabstract(BOOKS::Book)


def test_books::book_constructor_exists():
    assert callable(BOOKS::Book.__init__)


def test_books::book_constructor_args():
    sig = inspect.signature(BOOKS::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_books::book_has_title():
    assert hasattr(BOOKS::Book, "title")
    descriptor = None
    for klass in BOOKS::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_books::chapter_is_not_abstract():
    assert not inspect.isabstract(BOOKS::Chapter)


def test_books::chapter_constructor_exists():
    assert callable(BOOKS::Chapter.__init__)


def test_books::chapter_constructor_args():
    sig = inspect.signature(BOOKS::Chapter.__init__)
    params = list(sig.parameters.keys())
    assert "nbPages" in params, "Missing parameter 'nbPages'"
    assert "title" in params, "Missing parameter 'title'"

def test_books::chapter_has_nbPages():
    assert hasattr(BOOKS::Chapter, "nbPages")
    descriptor = None
    for klass in BOOKS::Chapter.__mro__:
        if "nbPages" in klass.__dict__:
            descriptor = klass.__dict__["nbPages"]
            break
    assert isinstance(descriptor, property)

def test_books::chapter_has_title():
    assert hasattr(BOOKS::Chapter, "title")
    descriptor = None
    for klass in BOOKS::Chapter.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
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
BOOKS::Book_strategy = st.builds(
    BOOKS::Book,
    title=
        safe_text
)
BOOKS::Chapter_strategy = st.builds(
    BOOKS::Chapter,
    nbPages=
        st.integers(),
    title=
        safe_text
)

@given(instance=BOOKS::Book_strategy)
@settings(max_examples=50)
def test_books::book_instantiation(instance):
    assert isinstance(instance, BOOKS::Book)

@given(instance=BOOKS::Book_strategy)
def test_books::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=BOOKS::Book_strategy)
def test_books::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=BOOKS::Chapter_strategy)
@settings(max_examples=50)
def test_books::chapter_instantiation(instance):
    assert isinstance(instance, BOOKS::Chapter)

@given(instance=BOOKS::Chapter_strategy)
def test_books::chapter_nbPages_type(instance):
    assert isinstance(instance.nbPages, int)


@given(instance=BOOKS::Chapter_strategy)
def test_books::chapter_nbPages_setter(instance):
    original = instance.nbPages
    instance.nbPages = original
    assert instance.nbPages == original

@given(instance=BOOKS::Chapter_strategy)
def test_books::chapter_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=BOOKS::Chapter_strategy)
def test_books::chapter_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
