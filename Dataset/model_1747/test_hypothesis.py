import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mytry::Author,
    mytry::Book,
    mytry::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mytry::author_is_not_abstract():
    assert not inspect.isabstract(mytry::Author)


def test_mytry::author_constructor_exists():
    assert callable(mytry::Author.__init__)


def test_mytry::author_constructor_args():
    sig = inspect.signature(mytry::Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mytry::author_has_name():
    assert hasattr(mytry::Author, "name")
    descriptor = None
    for klass in mytry::Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mytry::book_is_not_abstract():
    assert not inspect.isabstract(mytry::Book)


def test_mytry::book_constructor_exists():
    assert callable(mytry::Book.__init__)


def test_mytry::book_constructor_args():
    sig = inspect.signature(mytry::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_mytry::book_has_title():
    assert hasattr(mytry::Book, "title")
    descriptor = None
    for klass in mytry::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_mytry::library_is_not_abstract():
    assert not inspect.isabstract(mytry::Library)


def test_mytry::library_constructor_exists():
    assert callable(mytry::Library.__init__)


def test_mytry::library_constructor_args():
    sig = inspect.signature(mytry::Library.__init__)
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
mytry::Author_strategy = st.builds(
    mytry::Author,
    name=
        safe_text
)
mytry::Book_strategy = st.builds(
    mytry::Book,
    title=
        safe_text
)
mytry::Library_strategy = st.builds(
    mytry::Library,
)

@given(instance=mytry::Author_strategy)
@settings(max_examples=50)
def test_mytry::author_instantiation(instance):
    assert isinstance(instance, mytry::Author)

@given(instance=mytry::Author_strategy)
def test_mytry::author_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mytry::Author_strategy)
def test_mytry::author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mytry::Book_strategy)
@settings(max_examples=50)
def test_mytry::book_instantiation(instance):
    assert isinstance(instance, mytry::Book)

@given(instance=mytry::Book_strategy)
def test_mytry::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=mytry::Book_strategy)
def test_mytry::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=mytry::Library_strategy)
@settings(max_examples=50)
def test_mytry::library_instantiation(instance):
    assert isinstance(instance, mytry::Library)
