import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    book::EObject,
    book::Book,
    book::BookCollection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_book::eobject_is_not_abstract():
    assert not inspect.isabstract(book::EObject)


def test_book::eobject_constructor_exists():
    assert callable(book::EObject.__init__)


def test_book::eobject_constructor_args():
    sig = inspect.signature(book::EObject.__init__)
    params = list(sig.parameters.keys())



def test_book::book_is_not_abstract():
    assert not inspect.isabstract(book::Book)


def test_book::book_constructor_exists():
    assert callable(book::Book.__init__)


def test_book::book_constructor_args():
    sig = inspect.signature(book::Book.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_book::book_has_id():
    assert hasattr(book::Book, "id")
    descriptor = None
    for klass in book::Book.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_book::book_has_name():
    assert hasattr(book::Book, "name")
    descriptor = None
    for klass in book::Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_book::bookcollection_is_not_abstract():
    assert not inspect.isabstract(book::BookCollection)


def test_book::bookcollection_constructor_exists():
    assert callable(book::BookCollection.__init__)


def test_book::bookcollection_constructor_args():
    sig = inspect.signature(book::BookCollection.__init__)
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
book::EObject_strategy = st.builds(
    book::EObject,
)
book::Book_strategy = st.builds(
    book::Book,
    id=
        st.integers(),
    name=
        safe_text
)
book::BookCollection_strategy = st.builds(
    book::BookCollection,
)

@given(instance=book::EObject_strategy)
@settings(max_examples=50)
def test_book::eobject_instantiation(instance):
    assert isinstance(instance, book::EObject)

@given(instance=book::Book_strategy)
@settings(max_examples=50)
def test_book::book_instantiation(instance):
    assert isinstance(instance, book::Book)

@given(instance=book::Book_strategy)
def test_book::book_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=book::Book_strategy)
def test_book::book_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=book::Book_strategy)
def test_book::book_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=book::Book_strategy)
def test_book::book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=book::BookCollection_strategy)
@settings(max_examples=50)
def test_book::bookcollection_instantiation(instance):
    assert isinstance(instance, book::BookCollection)
