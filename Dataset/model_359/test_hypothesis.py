import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Asset,
    Book,
    libraryExample_SchoolBook,
    libraryExample_Asset,
    Library,
    libraryExample_SchoolLibrary,
    libraryExample_Writer,
    libraryExample_Book,
    libraryExample_Library,
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



def test_libraryexample_schoolbook_is_not_abstract():
    assert not inspect.isabstract(libraryExample_SchoolBook)


def test_libraryexample_schoolbook_constructor_exists():
    assert callable(libraryExample_SchoolBook.__init__)


def test_libraryexample_schoolbook_constructor_args():
    sig = inspect.signature(libraryExample_SchoolBook.__init__)
    params = list(sig.parameters.keys())



def test_libraryexample_asset_is_not_abstract():
    assert not inspect.isabstract(libraryExample_Asset)


def test_libraryexample_asset_constructor_exists():
    assert callable(libraryExample_Asset.__init__)


def test_libraryexample_asset_constructor_args():
    sig = inspect.signature(libraryExample_Asset.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_libraryexample_asset_has_value():
    assert hasattr(libraryExample_Asset, "value")
    descriptor = None
    for klass in libraryExample_Asset.__mro__:
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



def test_libraryexample_schoollibrary_is_not_abstract():
    assert not inspect.isabstract(libraryExample_SchoolLibrary)


def test_libraryexample_schoollibrary_constructor_exists():
    assert callable(libraryExample_SchoolLibrary.__init__)


def test_libraryexample_schoollibrary_constructor_args():
    sig = inspect.signature(libraryExample_SchoolLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_libraryexample_schoollibrary_has_location():
    assert hasattr(libraryExample_SchoolLibrary, "location")
    descriptor = None
    for klass in libraryExample_SchoolLibrary.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_libraryexample_writer_is_not_abstract():
    assert not inspect.isabstract(libraryExample_Writer)


def test_libraryexample_writer_constructor_exists():
    assert callable(libraryExample_Writer.__init__)


def test_libraryexample_writer_constructor_args():
    sig = inspect.signature(libraryExample_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "lastname" in params, "Missing parameter 'lastname'"

def test_libraryexample_writer_has_name():
    assert hasattr(libraryExample_Writer, "name")
    descriptor = None
    for klass in libraryExample_Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_libraryexample_writer_has_lastname():
    assert hasattr(libraryExample_Writer, "lastname")
    descriptor = None
    for klass in libraryExample_Writer.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)



def test_libraryexample_book_is_not_abstract():
    assert not inspect.isabstract(libraryExample_Book)


def test_libraryexample_book_constructor_exists():
    assert callable(libraryExample_Book.__init__)


def test_libraryexample_book_constructor_args():
    sig = inspect.signature(libraryExample_Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "category" in params, "Missing parameter 'category'"
    assert "title" in params, "Missing parameter 'title'"

def test_libraryexample_book_has_pages():
    assert hasattr(libraryExample_Book, "pages")
    descriptor = None
    for klass in libraryExample_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_libraryexample_book_has_category():
    assert hasattr(libraryExample_Book, "category")
    descriptor = None
    for klass in libraryExample_Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_libraryexample_book_has_title():
    assert hasattr(libraryExample_Book, "title")
    descriptor = None
    for klass in libraryExample_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_libraryexample_library_is_not_abstract():
    assert not inspect.isabstract(libraryExample_Library)


def test_libraryexample_library_constructor_exists():
    assert callable(libraryExample_Library.__init__)


def test_libraryexample_library_constructor_args():
    sig = inspect.signature(libraryExample_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_libraryexample_library_has_name():
    assert hasattr(libraryExample_Library, "name")
    descriptor = None
    for klass in libraryExample_Library.__mro__:
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
        "Biography",
        "Mystery",
        "ScienceFiction",
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
libraryExample_SchoolBook_strategy = st.builds(
    libraryExample_SchoolBook,
)
libraryExample_Asset_strategy = st.builds(
    libraryExample_Asset,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Library_strategy = st.builds(
    Library,
)
libraryExample_SchoolLibrary_strategy = st.builds(
    libraryExample_SchoolLibrary,
    location=
        safe_text
)
libraryExample_Writer_strategy = st.builds(
    libraryExample_Writer,
    name=
        safe_text,
    lastname=
        safe_text
)
libraryExample_Book_strategy = st.builds(
    libraryExample_Book,
    pages=
        st.integers(),
    category=
        safe_text,
    title=
        safe_text
)
libraryExample_Library_strategy = st.builds(
    libraryExample_Library,
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

@given(instance=libraryExample_SchoolBook_strategy)
@settings(max_examples=50)
def test_libraryexample_schoolbook_instantiation(instance):
    assert isinstance(instance, libraryExample_SchoolBook)

@given(instance=libraryExample_Asset_strategy)
@settings(max_examples=50)
def test_libraryexample_asset_instantiation(instance):
    assert isinstance(instance, libraryExample_Asset)



@given(instance=libraryExample_Asset_strategy)
def test_libraryexample_asset_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Library_strategy)
@settings(max_examples=50)
def test_library_instantiation(instance):
    assert isinstance(instance, Library)

@given(instance=libraryExample_SchoolLibrary_strategy)
@settings(max_examples=50)
def test_libraryexample_schoollibrary_instantiation(instance):
    assert isinstance(instance, libraryExample_SchoolLibrary)



@given(instance=libraryExample_SchoolLibrary_strategy)
def test_libraryexample_schoollibrary_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=libraryExample_Writer_strategy)
@settings(max_examples=50)
def test_libraryexample_writer_instantiation(instance):
    assert isinstance(instance, libraryExample_Writer)



@given(instance=libraryExample_Writer_strategy)
def test_libraryexample_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=libraryExample_Writer_strategy)
def test_libraryexample_writer_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=libraryExample_Book_strategy)
@settings(max_examples=50)
def test_libraryexample_book_instantiation(instance):
    assert isinstance(instance, libraryExample_Book)



@given(instance=libraryExample_Book_strategy)
def test_libraryexample_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=libraryExample_Book_strategy)
def test_libraryexample_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=libraryExample_Book_strategy)
def test_libraryexample_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=libraryExample_Library_strategy)
@settings(max_examples=50)
def test_libraryexample_library_instantiation(instance):
    assert isinstance(instance, libraryExample_Library)



@given(instance=libraryExample_Library_strategy)
def test_libraryexample_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
