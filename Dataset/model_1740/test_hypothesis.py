import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_Library,
    model_Book,
    model_Person,
    model_MappedLibrary,
    model_Location,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_library_is_not_abstract():
    assert not inspect.isabstract(model_Library)


def test_model_library_constructor_exists():
    assert callable(model_Library.__init__)


def test_model_library_constructor_args():
    sig = inspect.signature(model_Library.__init__)
    params = list(sig.parameters.keys())



def test_model_book_is_not_abstract():
    assert not inspect.isabstract(model_Book)


def test_model_book_constructor_exists():
    assert callable(model_Book.__init__)


def test_model_book_constructor_args():
    sig = inspect.signature(model_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "tags" in params, "Missing parameter 'tags'"
    assert "data" in params, "Missing parameter 'data'"

def test_model_book_has_title():
    assert hasattr(model_Book, "title")
    descriptor = None
    for klass in model_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_model_book_has_tags():
    assert hasattr(model_Book, "tags")
    descriptor = None
    for klass in model_Book.__mro__:
        if "tags" in klass.__dict__:
            descriptor = klass.__dict__["tags"]
            break
    assert isinstance(descriptor, property)

def test_model_book_has_data():
    assert hasattr(model_Book, "data")
    descriptor = None
    for klass in model_Book.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



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



def test_model_mappedlibrary_is_not_abstract():
    assert not inspect.isabstract(model_MappedLibrary)


def test_model_mappedlibrary_constructor_exists():
    assert callable(model_MappedLibrary.__init__)


def test_model_mappedlibrary_constructor_args():
    sig = inspect.signature(model_MappedLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "books" in params, "Missing parameter 'books'"

def test_model_mappedlibrary_has_books():
    assert hasattr(model_MappedLibrary, "books")
    descriptor = None
    for klass in model_MappedLibrary.__mro__:
        if "books" in klass.__dict__:
            descriptor = klass.__dict__["books"]
            break
    assert isinstance(descriptor, property)



def test_model_location_is_not_abstract():
    assert not inspect.isabstract(model_Location)


def test_model_location_constructor_exists():
    assert callable(model_Location.__init__)


def test_model_location_constructor_args():
    sig = inspect.signature(model_Location.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "address" in params, "Missing parameter 'address'"

def test_model_location_has_id():
    assert hasattr(model_Location, "id")
    descriptor = None
    for klass in model_Location.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_model_location_has_address():
    assert hasattr(model_Location, "address")
    descriptor = None
    for klass in model_Location.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
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
model_Library_strategy = st.builds(
    model_Library,
)
model_Book_strategy = st.builds(
    model_Book,
    title=
        safe_text,
    tags=
        safe_text,
    data=
        safe_text
)
model_Person_strategy = st.builds(
    model_Person,
    name=
        safe_text
)
model_MappedLibrary_strategy = st.builds(
    model_MappedLibrary,
    books=
        safe_text
)
model_Location_strategy = st.builds(
    model_Location,
    id=
        safe_text,
    address=
        safe_text
)

@given(instance=model_Library_strategy)
@settings(max_examples=50)
def test_model_library_instantiation(instance):
    assert isinstance(instance, model_Library)

@given(instance=model_Book_strategy)
@settings(max_examples=50)
def test_model_book_instantiation(instance):
    assert isinstance(instance, model_Book)



@given(instance=model_Book_strategy)
def test_model_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=model_Book_strategy)
def test_model_book_tags_setter(instance):
    original = instance.tags
    instance.tags = original
    assert instance.tags == original



@given(instance=model_Book_strategy)
def test_model_book_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=model_Person_strategy)
@settings(max_examples=50)
def test_model_person_instantiation(instance):
    assert isinstance(instance, model_Person)



@given(instance=model_Person_strategy)
def test_model_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_MappedLibrary_strategy)
@settings(max_examples=50)
def test_model_mappedlibrary_instantiation(instance):
    assert isinstance(instance, model_MappedLibrary)



@given(instance=model_MappedLibrary_strategy)
def test_model_mappedlibrary_books_setter(instance):
    original = instance.books
    instance.books = original
    assert instance.books == original

@given(instance=model_Location_strategy)
@settings(max_examples=50)
def test_model_location_instantiation(instance):
    assert isinstance(instance, model_Location)



@given(instance=model_Location_strategy)
def test_model_location_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=model_Location_strategy)
def test_model_location_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original
