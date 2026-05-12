import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    book_EObject,
    book_Book,
    book_BookCollection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_book_eobject_is_not_abstract():
    assert not inspect.isabstract(book_EObject)


def test_book_eobject_constructor_exists():
    assert callable(book_EObject.__init__)


def test_book_eobject_constructor_args():
    sig = inspect.signature(book_EObject.__init__)
    params = list(sig.parameters.keys())



def test_book_book_is_not_abstract():
    assert not inspect.isabstract(book_Book)


def test_book_book_constructor_exists():
    assert callable(book_Book.__init__)


def test_book_book_constructor_args():
    sig = inspect.signature(book_Book.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_book_book_has_id():
    assert hasattr(book_Book, "id")
    descriptor = None
    for klass in book_Book.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_book_book_has_name():
    assert hasattr(book_Book, "name")
    descriptor = None
    for klass in book_Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_book_bookcollection_is_not_abstract():
    assert not inspect.isabstract(book_BookCollection)


def test_book_bookcollection_constructor_exists():
    assert callable(book_BookCollection.__init__)


def test_book_bookcollection_constructor_args():
    sig = inspect.signature(book_BookCollection.__init__)
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
book_EObject_strategy = st.builds(
    book_EObject,
)
book_Book_strategy = st.builds(
    book_Book,
    id=
        st.integers(),
    name=
        safe_text
)
book_BookCollection_strategy = st.builds(
    book_BookCollection,
)

@given(instance=book_EObject_strategy)
@settings(max_examples=50)
def test_book_eobject_instantiation(instance):
    assert isinstance(instance, book_EObject)

@given(instance=book_Book_strategy)
@settings(max_examples=50)
def test_book_book_instantiation(instance):
    assert isinstance(instance, book_Book)



@given(instance=book_Book_strategy)
def test_book_book_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=book_Book_strategy)
def test_book_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=book_BookCollection_strategy)
@settings(max_examples=50)
def test_book_bookcollection_instantiation(instance):
    assert isinstance(instance, book_BookCollection)
