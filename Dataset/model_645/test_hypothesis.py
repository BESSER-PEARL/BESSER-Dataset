import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::Person,
    model::BookShelf,
    model::DataBase,
    model::Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::person_is_not_abstract():
    assert not inspect.isabstract(model::Person)


def test_model::person_constructor_exists():
    assert callable(model::Person.__init__)


def test_model::person_constructor_args():
    sig = inspect.signature(model::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::person_has_name():
    assert hasattr(model::Person, "name")
    descriptor = None
    for klass in model::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::bookshelf_is_not_abstract():
    assert not inspect.isabstract(model::BookShelf)


def test_model::bookshelf_constructor_exists():
    assert callable(model::BookShelf.__init__)


def test_model::bookshelf_constructor_args():
    sig = inspect.signature(model::BookShelf.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::bookshelf_has_name():
    assert hasattr(model::BookShelf, "name")
    descriptor = None
    for klass in model::BookShelf.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::database_is_not_abstract():
    assert not inspect.isabstract(model::DataBase)


def test_model::database_constructor_exists():
    assert callable(model::DataBase.__init__)


def test_model::database_constructor_args():
    sig = inspect.signature(model::DataBase.__init__)
    params = list(sig.parameters.keys())



def test_model::book_is_not_abstract():
    assert not inspect.isabstract(model::Book)


def test_model::book_constructor_exists():
    assert callable(model::Book.__init__)


def test_model::book_constructor_args():
    sig = inspect.signature(model::Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "author" in params, "Missing parameter 'author'"
    assert "avgRating" in params, "Missing parameter 'avgRating'"

def test_model::book_has_name():
    assert hasattr(model::Book, "name")
    descriptor = None
    for klass in model::Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::book_has_author():
    assert hasattr(model::Book, "author")
    descriptor = None
    for klass in model::Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_model::book_has_avgRating():
    assert hasattr(model::Book, "avgRating")
    descriptor = None
    for klass in model::Book.__mro__:
        if "avgRating" in klass.__dict__:
            descriptor = klass.__dict__["avgRating"]
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
model::Person_strategy = st.builds(
    model::Person,
    name=
        safe_text
)
model::BookShelf_strategy = st.builds(
    model::BookShelf,
    name=
        safe_text
)
model::DataBase_strategy = st.builds(
    model::DataBase,
)
model::Book_strategy = st.builds(
    model::Book,
    name=
        safe_text,
    author=
        safe_text,
    avgRating=
        st.integers()
)

@given(instance=model::Person_strategy)
@settings(max_examples=50)
def test_model::person_instantiation(instance):
    assert isinstance(instance, model::Person)

@given(instance=model::Person_strategy)
def test_model::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Person_strategy)
def test_model::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::BookShelf_strategy)
@settings(max_examples=50)
def test_model::bookshelf_instantiation(instance):
    assert isinstance(instance, model::BookShelf)

@given(instance=model::BookShelf_strategy)
def test_model::bookshelf_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::BookShelf_strategy)
def test_model::bookshelf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::DataBase_strategy)
@settings(max_examples=50)
def test_model::database_instantiation(instance):
    assert isinstance(instance, model::DataBase)

@given(instance=model::Book_strategy)
@settings(max_examples=50)
def test_model::book_instantiation(instance):
    assert isinstance(instance, model::Book)

@given(instance=model::Book_strategy)
def test_model::book_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Book_strategy)
def test_model::book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Book_strategy)
def test_model::book_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=model::Book_strategy)
def test_model::book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=model::Book_strategy)
def test_model::book_avgRating_type(instance):
    assert isinstance(instance.avgRating, int)


@given(instance=model::Book_strategy)
def test_model::book_avgRating_setter(instance):
    original = instance.avgRating
    instance.avgRating = original
    assert instance.avgRating == original
