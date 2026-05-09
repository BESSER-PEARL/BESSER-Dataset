import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::Library,
    model::Book,
    model::Person,
    model::MappedLibrary,
    model::Location,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::library_is_not_abstract():
    assert not inspect.isabstract(model::Library)


def test_model::library_constructor_exists():
    assert callable(model::Library.__init__)


def test_model::library_constructor_args():
    sig = inspect.signature(model::Library.__init__)
    params = list(sig.parameters.keys())



def test_model::book_is_not_abstract():
    assert not inspect.isabstract(model::Book)


def test_model::book_constructor_exists():
    assert callable(model::Book.__init__)


def test_model::book_constructor_args():
    sig = inspect.signature(model::Book.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "title" in params, "Missing parameter 'title'"
    assert "tags" in params, "Missing parameter 'tags'"

def test_model::book_has_data():
    assert hasattr(model::Book, "data")
    descriptor = None
    for klass in model::Book.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_model::book_has_title():
    assert hasattr(model::Book, "title")
    descriptor = None
    for klass in model::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_model::book_has_tags():
    assert hasattr(model::Book, "tags")
    descriptor = None
    for klass in model::Book.__mro__:
        if "tags" in klass.__dict__:
            descriptor = klass.__dict__["tags"]
            break
    assert isinstance(descriptor, property)



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



def test_model::mappedlibrary_is_not_abstract():
    assert not inspect.isabstract(model::MappedLibrary)


def test_model::mappedlibrary_constructor_exists():
    assert callable(model::MappedLibrary.__init__)


def test_model::mappedlibrary_constructor_args():
    sig = inspect.signature(model::MappedLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "books" in params, "Missing parameter 'books'"

def test_model::mappedlibrary_has_books():
    assert hasattr(model::MappedLibrary, "books")
    descriptor = None
    for klass in model::MappedLibrary.__mro__:
        if "books" in klass.__dict__:
            descriptor = klass.__dict__["books"]
            break
    assert isinstance(descriptor, property)



def test_model::location_is_not_abstract():
    assert not inspect.isabstract(model::Location)


def test_model::location_constructor_exists():
    assert callable(model::Location.__init__)


def test_model::location_constructor_args():
    sig = inspect.signature(model::Location.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "id" in params, "Missing parameter 'id'"

def test_model::location_has_address():
    assert hasattr(model::Location, "address")
    descriptor = None
    for klass in model::Location.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_model::location_has_id():
    assert hasattr(model::Location, "id")
    descriptor = None
    for klass in model::Location.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
model::Library_strategy = st.builds(
    model::Library,
)
model::Book_strategy = st.builds(
    model::Book,
    data=
        safe_text,
    title=
        safe_text,
    tags=
        safe_text
)
model::Person_strategy = st.builds(
    model::Person,
    name=
        safe_text
)
model::MappedLibrary_strategy = st.builds(
    model::MappedLibrary,
    books=
        safe_text
)
model::Location_strategy = st.builds(
    model::Location,
    address=
        safe_text,
    id=
        safe_text
)

@given(instance=model::Library_strategy)
@settings(max_examples=50)
def test_model::library_instantiation(instance):
    assert isinstance(instance, model::Library)

@given(instance=model::Book_strategy)
@settings(max_examples=50)
def test_model::book_instantiation(instance):
    assert isinstance(instance, model::Book)

@given(instance=model::Book_strategy)
def test_model::book_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=model::Book_strategy)
def test_model::book_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=model::Book_strategy)
def test_model::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=model::Book_strategy)
def test_model::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=model::Book_strategy)
def test_model::book_tags_type(instance):
    assert isinstance(instance.tags, str)


@given(instance=model::Book_strategy)
def test_model::book_tags_setter(instance):
    original = instance.tags
    instance.tags = original
    assert instance.tags == original

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

@given(instance=model::MappedLibrary_strategy)
@settings(max_examples=50)
def test_model::mappedlibrary_instantiation(instance):
    assert isinstance(instance, model::MappedLibrary)

@given(instance=model::MappedLibrary_strategy)
def test_model::mappedlibrary_books_type(instance):
    assert isinstance(instance.books, str)


@given(instance=model::MappedLibrary_strategy)
def test_model::mappedlibrary_books_setter(instance):
    original = instance.books
    instance.books = original
    assert instance.books == original

@given(instance=model::Location_strategy)
@settings(max_examples=50)
def test_model::location_instantiation(instance):
    assert isinstance(instance, model::Location)

@given(instance=model::Location_strategy)
def test_model::location_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=model::Location_strategy)
def test_model::location_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=model::Location_strategy)
def test_model::location_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=model::Location_strategy)
def test_model::location_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
