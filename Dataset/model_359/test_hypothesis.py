import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Asset,
    Book,
    libraryExample::SchoolBook,
    libraryExample::Asset,
    Library,
    libraryExample::SchoolLibrary,
    libraryExample::Writer,
    libraryExample::Book,
    libraryExample::Library,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_asset_is_not_abstract():
    assert not inspect.isabstract(Asset)


def test_asset_constructor_exists():
    assert callable(Asset.__init__)


def test_asset_constructor_args():
    sig = inspect.signature(Asset.__init__)
    params = list(sig.parameters.keys())



def test_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_book_constructor_exists():
    assert callable(Book.__init__)


def test_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())



def test_libraryexample::schoolbook_is_not_abstract():
    assert not inspect.isabstract(libraryExample::SchoolBook)


def test_libraryexample::schoolbook_constructor_exists():
    assert callable(libraryExample::SchoolBook.__init__)


def test_libraryexample::schoolbook_constructor_args():
    sig = inspect.signature(libraryExample::SchoolBook.__init__)
    params = list(sig.parameters.keys())



def test_libraryexample::asset_is_not_abstract():
    assert not inspect.isabstract(libraryExample::Asset)


def test_libraryexample::asset_constructor_exists():
    assert callable(libraryExample::Asset.__init__)


def test_libraryexample::asset_constructor_args():
    sig = inspect.signature(libraryExample::Asset.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_libraryexample::asset_has_value():
    assert hasattr(libraryExample::Asset, "value")
    descriptor = None
    for klass in libraryExample::Asset.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_library_is_not_abstract():
    assert not inspect.isabstract(Library)


def test_library_constructor_exists():
    assert callable(Library.__init__)


def test_library_constructor_args():
    sig = inspect.signature(Library.__init__)
    params = list(sig.parameters.keys())



def test_libraryexample::schoollibrary_is_not_abstract():
    assert not inspect.isabstract(libraryExample::SchoolLibrary)


def test_libraryexample::schoollibrary_constructor_exists():
    assert callable(libraryExample::SchoolLibrary.__init__)


def test_libraryexample::schoollibrary_constructor_args():
    sig = inspect.signature(libraryExample::SchoolLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_libraryexample::schoollibrary_has_location():
    assert hasattr(libraryExample::SchoolLibrary, "location")
    descriptor = None
    for klass in libraryExample::SchoolLibrary.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_libraryexample::writer_is_not_abstract():
    assert not inspect.isabstract(libraryExample::Writer)


def test_libraryexample::writer_constructor_exists():
    assert callable(libraryExample::Writer.__init__)


def test_libraryexample::writer_constructor_args():
    sig = inspect.signature(libraryExample::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "name" in params, "Missing parameter 'name'"

def test_libraryexample::writer_has_lastname():
    assert hasattr(libraryExample::Writer, "lastname")
    descriptor = None
    for klass in libraryExample::Writer.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_libraryexample::writer_has_name():
    assert hasattr(libraryExample::Writer, "name")
    descriptor = None
    for klass in libraryExample::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_libraryexample::book_is_not_abstract():
    assert not inspect.isabstract(libraryExample::Book)


def test_libraryexample::book_constructor_exists():
    assert callable(libraryExample::Book.__init__)


def test_libraryexample::book_constructor_args():
    sig = inspect.signature(libraryExample::Book.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"

def test_libraryexample::book_has_category():
    assert hasattr(libraryExample::Book, "category")
    descriptor = None
    for klass in libraryExample::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_libraryexample::book_has_pages():
    assert hasattr(libraryExample::Book, "pages")
    descriptor = None
    for klass in libraryExample::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_libraryexample::book_has_title():
    assert hasattr(libraryExample::Book, "title")
    descriptor = None
    for klass in libraryExample::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_libraryexample::library_is_not_abstract():
    assert not inspect.isabstract(libraryExample::Library)


def test_libraryexample::library_constructor_exists():
    assert callable(libraryExample::Library.__init__)


def test_libraryexample::library_constructor_args():
    sig = inspect.signature(libraryExample::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_libraryexample::library_has_name():
    assert hasattr(libraryExample::Library, "name")
    descriptor = None
    for klass in libraryExample::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "ScienceFiction",
        "Biography",
        "Mystery",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BookCategory"


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
Asset_strategy = st.builds(
    Asset,
)
Book_strategy = st.builds(
    Book,
)
libraryExample::SchoolBook_strategy = st.builds(
    libraryExample::SchoolBook,
)
libraryExample::Asset_strategy = st.builds(
    libraryExample::Asset,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Library_strategy = st.builds(
    Library,
)
libraryExample::SchoolLibrary_strategy = st.builds(
    libraryExample::SchoolLibrary,
    location=
        safe_text
)
libraryExample::Writer_strategy = st.builds(
    libraryExample::Writer,
    lastname=
        safe_text,
    name=
        safe_text
)
libraryExample::Book_strategy = st.builds(
    libraryExample::Book,
    category=
        safe_text,
    pages=
        st.integers(),
    title=
        safe_text
)
libraryExample::Library_strategy = st.builds(
    libraryExample::Library,
    name=
        safe_text
)

@given(instance=Asset_strategy)
@settings(max_examples=50)
def test_asset_instantiation(instance):
    assert isinstance(instance, Asset)

@given(instance=Book_strategy)
@settings(max_examples=50)
def test_book_instantiation(instance):
    assert isinstance(instance, Book)

@given(instance=libraryExample::SchoolBook_strategy)
@settings(max_examples=50)
def test_libraryexample::schoolbook_instantiation(instance):
    assert isinstance(instance, libraryExample::SchoolBook)

@given(instance=libraryExample::Asset_strategy)
@settings(max_examples=50)
def test_libraryexample::asset_instantiation(instance):
    assert isinstance(instance, libraryExample::Asset)

@given(instance=libraryExample::Asset_strategy)
def test_libraryexample::asset_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=libraryExample::Asset_strategy)
def test_libraryexample::asset_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Library_strategy)
@settings(max_examples=50)
def test_library_instantiation(instance):
    assert isinstance(instance, Library)

@given(instance=libraryExample::SchoolLibrary_strategy)
@settings(max_examples=50)
def test_libraryexample::schoollibrary_instantiation(instance):
    assert isinstance(instance, libraryExample::SchoolLibrary)

@given(instance=libraryExample::SchoolLibrary_strategy)
def test_libraryexample::schoollibrary_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=libraryExample::SchoolLibrary_strategy)
def test_libraryexample::schoollibrary_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=libraryExample::Writer_strategy)
@settings(max_examples=50)
def test_libraryexample::writer_instantiation(instance):
    assert isinstance(instance, libraryExample::Writer)

@given(instance=libraryExample::Writer_strategy)
def test_libraryexample::writer_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=libraryExample::Writer_strategy)
def test_libraryexample::writer_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=libraryExample::Writer_strategy)
def test_libraryexample::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=libraryExample::Writer_strategy)
def test_libraryexample::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=libraryExample::Book_strategy)
@settings(max_examples=50)
def test_libraryexample::book_instantiation(instance):
    assert isinstance(instance, libraryExample::Book)

@given(instance=libraryExample::Book_strategy)
def test_libraryexample::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=libraryExample::Book_strategy)
def test_libraryexample::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=libraryExample::Book_strategy)
def test_libraryexample::book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=libraryExample::Book_strategy)
def test_libraryexample::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=libraryExample::Book_strategy)
def test_libraryexample::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=libraryExample::Book_strategy)
def test_libraryexample::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=libraryExample::Library_strategy)
@settings(max_examples=50)
def test_libraryexample::library_instantiation(instance):
    assert isinstance(instance, libraryExample::Library)

@given(instance=libraryExample::Library_strategy)
def test_libraryexample::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=libraryExample::Library_strategy)
def test_libraryexample::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
