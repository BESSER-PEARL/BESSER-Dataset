import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    a::Book,
    a::A,
    a::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a::book_is_not_abstract():
    assert not inspect.isabstract(a::Book)


def test_a::book_constructor_exists():
    assert callable(a::Book.__init__)


def test_a::book_constructor_args():
    sig = inspect.signature(a::Book.__init__)
    params = list(sig.parameters.keys())
    assert "published" in params, "Missing parameter 'published'"
    assert "author" in params, "Missing parameter 'author'"
    assert "title" in params, "Missing parameter 'title'"

def test_a::book_has_published():
    assert hasattr(a::Book, "published")
    descriptor = None
    for klass in a::Book.__mro__:
        if "published" in klass.__dict__:
            descriptor = klass.__dict__["published"]
            break
    assert isinstance(descriptor, property)

def test_a::book_has_author():
    assert hasattr(a::Book, "author")
    descriptor = None
    for klass in a::Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_a::book_has_title():
    assert hasattr(a::Book, "title")
    descriptor = None
    for klass in a::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_a::a_is_not_abstract():
    assert not inspect.isabstract(a::A)


def test_a::a_constructor_exists():
    assert callable(a::A.__init__)


def test_a::a_constructor_args():
    sig = inspect.signature(a::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_a::a_has_name():
    assert hasattr(a::A, "name")
    descriptor = None
    for klass in a::A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_a::model_is_not_abstract():
    assert not inspect.isabstract(a::Model)


def test_a::model_constructor_exists():
    assert callable(a::Model.__init__)


def test_a::model_constructor_args():
    sig = inspect.signature(a::Model.__init__)
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
a::Book_strategy = st.builds(
    a::Book,
    published=
        safe_text,
    author=
        safe_text,
    title=
        safe_text
)
a::A_strategy = st.builds(
    a::A,
    name=
        safe_text
)
a::Model_strategy = st.builds(
    a::Model,
)

@given(instance=a::Book_strategy)
@settings(max_examples=50)
def test_a::book_instantiation(instance):
    assert isinstance(instance, a::Book)

@given(instance=a::Book_strategy)
def test_a::book_published_type(instance):
    assert isinstance(instance.published, str)


@given(instance=a::Book_strategy)
def test_a::book_published_setter(instance):
    original = instance.published
    instance.published = original
    assert instance.published == original

@given(instance=a::Book_strategy)
def test_a::book_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=a::Book_strategy)
def test_a::book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=a::Book_strategy)
def test_a::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=a::Book_strategy)
def test_a::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=a::A_strategy)
@settings(max_examples=50)
def test_a::a_instantiation(instance):
    assert isinstance(instance, a::A)

@given(instance=a::A_strategy)
def test_a::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=a::A_strategy)
def test_a::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=a::Model_strategy)
@settings(max_examples=50)
def test_a::model_instantiation(instance):
    assert isinstance(instance, a::Model)
