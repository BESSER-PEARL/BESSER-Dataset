import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    library::Book,
    library::BookCopy,
    library::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::Book)


def test_library::book_constructor_exists():
    assert callable(library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::Book.__init__)
    params = list(sig.parameters.keys())



def test_library::bookcopy_is_not_abstract():
    assert not inspect.isabstract(library::BookCopy)


def test_library::bookcopy_constructor_exists():
    assert callable(library::BookCopy.__init__)


def test_library::bookcopy_constructor_args():
    sig = inspect.signature(library::BookCopy.__init__)
    params = list(sig.parameters.keys())
    assert "copies" in params, "Missing parameter 'copies'"

def test_library::bookcopy_has_copies():
    assert hasattr(library::BookCopy, "copies")
    descriptor = None
    for klass in library::BookCopy.__mro__:
        if "copies" in klass.__dict__:
            descriptor = klass.__dict__["copies"]
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
library::Book_strategy = st.builds(
    library::Book,
)
library::BookCopy_strategy = st.builds(
    library::BookCopy,
    copies=
        st.integers()
)
library::Library_strategy = st.builds(
    library::Library,
    name=
        safe_text
)

@given(instance=library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::Book)

@given(instance=library::BookCopy_strategy)
@settings(max_examples=50)
def test_library::bookcopy_instantiation(instance):
    assert isinstance(instance, library::BookCopy)

@given(instance=library::BookCopy_strategy)
def test_library::bookcopy_copies_type(instance):
    assert isinstance(instance.copies, int)


@given(instance=library::BookCopy_strategy)
def test_library::bookcopy_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original

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
