import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mytry_Author,
    mytry_Book,
    mytry_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mytry_author_is_not_abstract():
    assert not inspect.isabstract(mytry_Author)


def test_mytry_author_constructor_exists():
    assert callable(mytry_Author.__init__)


def test_mytry_author_constructor_args():
    sig = inspect.signature(mytry_Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mytry_author_has_name():
    assert hasattr(mytry_Author, "name")
    descriptor = None
    for klass in mytry_Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mytry_book_is_not_abstract():
    assert not inspect.isabstract(mytry_Book)


def test_mytry_book_constructor_exists():
    assert callable(mytry_Book.__init__)


def test_mytry_book_constructor_args():
    sig = inspect.signature(mytry_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_mytry_book_has_title():
    assert hasattr(mytry_Book, "title")
    descriptor = None
    for klass in mytry_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_mytry_library_is_not_abstract():
    assert not inspect.isabstract(mytry_Library)


def test_mytry_library_constructor_exists():
    assert callable(mytry_Library.__init__)


def test_mytry_library_constructor_args():
    sig = inspect.signature(mytry_Library.__init__)
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
mytry_Author_strategy = st.builds(
    mytry_Author,
    name=
        safe_text
)
mytry_Book_strategy = st.builds(
    mytry_Book,
    title=
        safe_text
)
mytry_Library_strategy = st.builds(
    mytry_Library,
)

@given(instance=mytry_Author_strategy)
@settings(max_examples=50)
def test_mytry_author_instantiation(instance):
    assert isinstance(instance, mytry_Author)



@given(instance=mytry_Author_strategy)
def test_mytry_author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mytry_Book_strategy)
@settings(max_examples=50)
def test_mytry_book_instantiation(instance):
    assert isinstance(instance, mytry_Book)



@given(instance=mytry_Book_strategy)
def test_mytry_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=mytry_Library_strategy)
@settings(max_examples=50)
def test_mytry_library_instantiation(instance):
    assert isinstance(instance, mytry_Library)
