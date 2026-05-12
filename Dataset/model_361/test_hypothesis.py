import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Library_Library,
    Library_Book,
    Library_Writer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library_library_is_not_abstract():
    assert not inspect.isabstract(Library_Library)


def test_library_library_constructor_exists():
    assert callable(Library_Library.__init__)


def test_library_library_constructor_args():
    sig = inspect.signature(Library_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library_library_has_name():
    assert hasattr(Library_Library, "name")
    descriptor = None
    for klass in Library_Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library_book_is_not_abstract():
    assert not inspect.isabstract(Library_Book)


def test_library_book_constructor_exists():
    assert callable(Library_Book.__init__)


def test_library_book_constructor_args():
    sig = inspect.signature(Library_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_library_book_has_title():
    assert hasattr(Library_Book, "title")
    descriptor = None
    for klass in Library_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_library_writer_is_not_abstract():
    assert not inspect.isabstract(Library_Writer)


def test_library_writer_constructor_exists():
    assert callable(Library_Writer.__init__)


def test_library_writer_constructor_args():
    sig = inspect.signature(Library_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library_writer_has_name():
    assert hasattr(Library_Writer, "name")
    descriptor = None
    for klass in Library_Writer.__mro__:
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
Library_Library_strategy = st.builds(
    Library_Library,
    name=
        safe_text
)
Library_Book_strategy = st.builds(
    Library_Book,
    title=
        safe_text
)
Library_Writer_strategy = st.builds(
    Library_Writer,
    name=
        safe_text
)

@given(instance=Library_Library_strategy)
@settings(max_examples=50)
def test_library_library_instantiation(instance):
    assert isinstance(instance, Library_Library)



@given(instance=Library_Library_strategy)
def test_library_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Library_Book_strategy)
@settings(max_examples=50)
def test_library_book_instantiation(instance):
    assert isinstance(instance, Library_Book)



@given(instance=Library_Book_strategy)
def test_library_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Library_Writer_strategy)
@settings(max_examples=50)
def test_library_writer_instantiation(instance):
    assert isinstance(instance, Library_Writer)



@given(instance=Library_Writer_strategy)
def test_library_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
