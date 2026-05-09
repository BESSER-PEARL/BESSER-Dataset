import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::Author,
    model::Book,
    model::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::author_is_not_abstract():
    assert not inspect.isabstract(model::Author)


def test_model::author_constructor_exists():
    assert callable(model::Author.__init__)


def test_model::author_constructor_args():
    sig = inspect.signature(model::Author.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_model::author_has_firstName():
    assert hasattr(model::Author, "firstName")
    descriptor = None
    for klass in model::Author.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_model::author_has_lastName():
    assert hasattr(model::Author, "lastName")
    descriptor = None
    for klass in model::Author.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_model::book_is_not_abstract():
    assert not inspect.isabstract(model::Book)


def test_model::book_constructor_exists():
    assert callable(model::Book.__init__)


def test_model::book_constructor_args():
    sig = inspect.signature(model::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_model::book_has_title():
    assert hasattr(model::Book, "title")
    descriptor = None
    for klass in model::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_model::library_is_not_abstract():
    assert not inspect.isabstract(model::Library)


def test_model::library_constructor_exists():
    assert callable(model::Library.__init__)


def test_model::library_constructor_args():
    sig = inspect.signature(model::Library.__init__)
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
model::Author_strategy = st.builds(
    model::Author,
    firstName=
        safe_text,
    lastName=
        safe_text
)
model::Book_strategy = st.builds(
    model::Book,
    title=
        safe_text
)
model::Library_strategy = st.builds(
    model::Library,
)

@given(instance=model::Author_strategy)
@settings(max_examples=50)
def test_model::author_instantiation(instance):
    assert isinstance(instance, model::Author)

@given(instance=model::Author_strategy)
def test_model::author_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=model::Author_strategy)
def test_model::author_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=model::Author_strategy)
def test_model::author_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=model::Author_strategy)
def test_model::author_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=model::Book_strategy)
@settings(max_examples=50)
def test_model::book_instantiation(instance):
    assert isinstance(instance, model::Book)

@given(instance=model::Book_strategy)
def test_model::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=model::Book_strategy)
def test_model::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=model::Library_strategy)
@settings(max_examples=50)
def test_model::library_instantiation(instance):
    assert isinstance(instance, model::Library)
