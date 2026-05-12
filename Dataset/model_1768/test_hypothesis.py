import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    library_Book,
    library_Author,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_library_author_is_not_abstract():
    assert not inspect.isabstract(library_Author)


def test_library_author_constructor_exists():
    assert callable(library_Author.__init__)


def test_library_author_constructor_args():
    sig = inspect.signature(library_Author.__init__)
    params = list(sig.parameters.keys())
    assert "first_name" in params, "Missing parameter 'first_name'"
    assert "surname" in params, "Missing parameter 'surname'"

def test_library_author_has_first_name():
    assert hasattr(library_Author, "first_name")
    descriptor = None
    for klass in library_Author.__mro__:
        if "first_name" in klass.__dict__:
            descriptor = klass.__dict__["first_name"]
            break
    assert isinstance(descriptor, property)

def test_library_author_has_surname():
    assert hasattr(library_Author, "surname")
    descriptor = None
    for klass in library_Author.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
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
library_Book_strategy = st.builds(
    library_Book,
    name=
        safe_text
)
library_Author_strategy = st.builds(
    library_Author,
    first_name=
        safe_text,
    surname=
        safe_text
)

@given(instance=library_Book_strategy)
@settings(max_examples=50)
def test_library_book_instantiation(instance):
    assert isinstance(instance, library_Book)



@given(instance=library_Book_strategy)
def test_library_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library_Author_strategy)
@settings(max_examples=50)
def test_library_author_instantiation(instance):
    assert isinstance(instance, library_Author)



@given(instance=library_Author_strategy)
def test_library_author_first_name_setter(instance):
    original = instance.first_name
    instance.first_name = original
    assert instance.first_name == original



@given(instance=library_Author_strategy)
def test_library_author_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original
