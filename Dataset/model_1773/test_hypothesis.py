import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    bookOrder::Book,
    bookOrder::BookOrder,
    bookOrder::Universe,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bookorder::book_is_not_abstract():
    assert not inspect.isabstract(bookOrder::Book)


def test_bookorder::book_constructor_exists():
    assert callable(bookOrder::Book.__init__)


def test_bookorder::book_constructor_args():
    sig = inspect.signature(bookOrder::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_bookorder::book_has_title():
    assert hasattr(bookOrder::Book, "title")
    descriptor = None
    for klass in bookOrder::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_bookorder::bookorder_is_not_abstract():
    assert not inspect.isabstract(bookOrder::BookOrder)


def test_bookorder::bookorder_constructor_exists():
    assert callable(bookOrder::BookOrder.__init__)


def test_bookorder::bookorder_constructor_args():
    sig = inspect.signature(bookOrder::BookOrder.__init__)
    params = list(sig.parameters.keys())
    assert "info" in params, "Missing parameter 'info'"

def test_bookorder::bookorder_has_info():
    assert hasattr(bookOrder::BookOrder, "info")
    descriptor = None
    for klass in bookOrder::BookOrder.__mro__:
        if "info" in klass.__dict__:
            descriptor = klass.__dict__["info"]
            break
    assert isinstance(descriptor, property)



def test_bookorder::universe_is_not_abstract():
    assert not inspect.isabstract(bookOrder::Universe)


def test_bookorder::universe_constructor_exists():
    assert callable(bookOrder::Universe.__init__)


def test_bookorder::universe_constructor_args():
    sig = inspect.signature(bookOrder::Universe.__init__)
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
bookOrder::Book_strategy = st.builds(
    bookOrder::Book,
    title=
        safe_text
)
bookOrder::BookOrder_strategy = st.builds(
    bookOrder::BookOrder,
    info=
        safe_text
)
bookOrder::Universe_strategy = st.builds(
    bookOrder::Universe,
)

@given(instance=bookOrder::Book_strategy)
@settings(max_examples=50)
def test_bookorder::book_instantiation(instance):
    assert isinstance(instance, bookOrder::Book)

@given(instance=bookOrder::Book_strategy)
def test_bookorder::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bookOrder::Book_strategy)
def test_bookorder::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bookOrder::BookOrder_strategy)
@settings(max_examples=50)
def test_bookorder::bookorder_instantiation(instance):
    assert isinstance(instance, bookOrder::BookOrder)

@given(instance=bookOrder::BookOrder_strategy)
def test_bookorder::bookorder_info_type(instance):
    assert isinstance(instance.info, str)


@given(instance=bookOrder::BookOrder_strategy)
def test_bookorder::bookorder_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original

@given(instance=bookOrder::Universe_strategy)
@settings(max_examples=50)
def test_bookorder::universe_instantiation(instance):
    assert isinstance(instance, bookOrder::Universe)
