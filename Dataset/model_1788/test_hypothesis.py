import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    a_Book,
    a_A,
    a_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_book_is_not_abstract():
    assert not inspect.isabstract(a_Book)


def test_a_book_constructor_exists():
    assert callable(a_Book.__init__)


def test_a_book_constructor_args():
    sig = inspect.signature(a_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "published" in params, "Missing parameter 'published'"
    assert "author" in params, "Missing parameter 'author'"

def test_a_book_has_title():
    assert hasattr(a_Book, "title")
    descriptor = None
    for klass in a_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_a_book_has_published():
    assert hasattr(a_Book, "published")
    descriptor = None
    for klass in a_Book.__mro__:
        if "published" in klass.__dict__:
            descriptor = klass.__dict__["published"]
            break
    assert isinstance(descriptor, property)

def test_a_book_has_author():
    assert hasattr(a_Book, "author")
    descriptor = None
    for klass in a_Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)



def test_a_a_is_not_abstract():
    assert not inspect.isabstract(a_A)


def test_a_a_constructor_exists():
    assert callable(a_A.__init__)


def test_a_a_constructor_args():
    sig = inspect.signature(a_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_a_a_has_name():
    assert hasattr(a_A, "name")
    descriptor = None
    for klass in a_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_a_model_is_not_abstract():
    assert not inspect.isabstract(a_Model)


def test_a_model_constructor_exists():
    assert callable(a_Model.__init__)


def test_a_model_constructor_args():
    sig = inspect.signature(a_Model.__init__)
    params = list(sig.parameters.keys())


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
a_Book_strategy = st.builds(
    a_Book,
    title=
        safe_text,
    published=
        safe_text,
    author=
        safe_text
)
a_A_strategy = st.builds(
    a_A,
    name=
        safe_text
)
a_Model_strategy = st.builds(
    a_Model,
)

@given(instance=a_Book_strategy)
@settings(max_examples=50)
def test_a_book_instantiation(instance):
    assert isinstance(instance, a_Book)



@given(instance=a_Book_strategy)
def test_a_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=a_Book_strategy)
def test_a_book_published_setter(instance):
    original = instance.published
    instance.published = original
    assert instance.published == original



@given(instance=a_Book_strategy)
def test_a_book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=a_A_strategy)
@settings(max_examples=50)
def test_a_a_instantiation(instance):
    assert isinstance(instance, a_A)



@given(instance=a_A_strategy)
def test_a_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=a_Model_strategy)
@settings(max_examples=50)
def test_a_model_instantiation(instance):
    assert isinstance(instance, a_Model)
