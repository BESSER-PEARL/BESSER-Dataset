import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_Person,
    model_BookShelf,
    model_DataBase,
    model_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_person_is_not_abstract():
    assert not inspect.isabstract(model_Person)


def test_model_person_constructor_exists():
    assert callable(model_Person.__init__)


def test_model_person_constructor_args():
    sig = inspect.signature(model_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_person_has_name():
    assert hasattr(model_Person, "name")
    descriptor = None
    for klass in model_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_bookshelf_is_not_abstract():
    assert not inspect.isabstract(model_BookShelf)


def test_model_bookshelf_constructor_exists():
    assert callable(model_BookShelf.__init__)


def test_model_bookshelf_constructor_args():
    sig = inspect.signature(model_BookShelf.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_bookshelf_has_name():
    assert hasattr(model_BookShelf, "name")
    descriptor = None
    for klass in model_BookShelf.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_database_is_not_abstract():
    assert not inspect.isabstract(model_DataBase)


def test_model_database_constructor_exists():
    assert callable(model_DataBase.__init__)


def test_model_database_constructor_args():
    sig = inspect.signature(model_DataBase.__init__)
    params = list(sig.parameters.keys())



def test_model_book_is_not_abstract():
    assert not inspect.isabstract(model_Book)


def test_model_book_constructor_exists():
    assert callable(model_Book.__init__)


def test_model_book_constructor_args():
    sig = inspect.signature(model_Book.__init__)
    params = list(sig.parameters.keys())
    assert "avgRating" in params, "Missing parameter 'avgRating'"
    assert "author" in params, "Missing parameter 'author'"
    assert "name" in params, "Missing parameter 'name'"

def test_model_book_has_avgRating():
    assert hasattr(model_Book, "avgRating")
    descriptor = None
    for klass in model_Book.__mro__:
        if "avgRating" in klass.__dict__:
            descriptor = klass.__dict__["avgRating"]
            break
    assert isinstance(descriptor, property)

def test_model_book_has_author():
    assert hasattr(model_Book, "author")
    descriptor = None
    for klass in model_Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_model_book_has_name():
    assert hasattr(model_Book, "name")
    descriptor = None
    for klass in model_Book.__mro__:
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
model_Person_strategy = st.builds(
    model_Person,
    name=
        safe_text
)
model_BookShelf_strategy = st.builds(
    model_BookShelf,
    name=
        safe_text
)
model_DataBase_strategy = st.builds(
    model_DataBase,
)
model_Book_strategy = st.builds(
    model_Book,
    avgRating=
        st.integers(),
    author=
        safe_text,
    name=
        safe_text
)

@given(instance=model_Person_strategy)
@settings(max_examples=50)
def test_model_person_instantiation(instance):
    assert isinstance(instance, model_Person)



@given(instance=model_Person_strategy)
def test_model_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_BookShelf_strategy)
@settings(max_examples=50)
def test_model_bookshelf_instantiation(instance):
    assert isinstance(instance, model_BookShelf)



@given(instance=model_BookShelf_strategy)
def test_model_bookshelf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_DataBase_strategy)
@settings(max_examples=50)
def test_model_database_instantiation(instance):
    assert isinstance(instance, model_DataBase)

@given(instance=model_Book_strategy)
@settings(max_examples=50)
def test_model_book_instantiation(instance):
    assert isinstance(instance, model_Book)



@given(instance=model_Book_strategy)
def test_model_book_avgRating_setter(instance):
    original = instance.avgRating
    instance.avgRating = original
    assert instance.avgRating == original



@given(instance=model_Book_strategy)
def test_model_book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=model_Book_strategy)
def test_model_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
