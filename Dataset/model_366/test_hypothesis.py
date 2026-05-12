import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    lib_LibSys,
    lib_Book,
    lib_Writer,
    lib_Library,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lib_libsys_is_not_abstract():
    assert not inspect.isabstract(lib_LibSys)


def test_lib_libsys_constructor_exists():
    assert callable(lib_LibSys.__init__)


def test_lib_libsys_constructor_args():
    sig = inspect.signature(lib_LibSys.__init__)
    params = list(sig.parameters.keys())



def test_lib_book_is_not_abstract():
    assert not inspect.isabstract(lib_Book)


def test_lib_book_constructor_exists():
    assert callable(lib_Book.__init__)


def test_lib_book_constructor_args():
    sig = inspect.signature(lib_Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "category" in params, "Missing parameter 'category'"
    assert "title" in params, "Missing parameter 'title'"

def test_lib_book_has_pages():
    assert hasattr(lib_Book, "pages")
    descriptor = None
    for klass in lib_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_lib_book_has_category():
    assert hasattr(lib_Book, "category")
    descriptor = None
    for klass in lib_Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_lib_book_has_title():
    assert hasattr(lib_Book, "title")
    descriptor = None
    for klass in lib_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_lib_writer_is_not_abstract():
    assert not inspect.isabstract(lib_Writer)


def test_lib_writer_constructor_exists():
    assert callable(lib_Writer.__init__)


def test_lib_writer_constructor_args():
    sig = inspect.signature(lib_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lib_writer_has_name():
    assert hasattr(lib_Writer, "name")
    descriptor = None
    for klass in lib_Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lib_library_is_not_abstract():
    assert not inspect.isabstract(lib_Library)


def test_lib_library_constructor_exists():
    assert callable(lib_Library.__init__)


def test_lib_library_constructor_args():
    sig = inspect.signature(lib_Library.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "name" in params, "Missing parameter 'name'"

def test_lib_library_has_location():
    assert hasattr(lib_Library, "location")
    descriptor = None
    for klass in lib_Library.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_lib_library_has_name():
    assert hasattr(lib_Library, "name")
    descriptor = None
    for klass in lib_Library.__mro__:
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
        "GeneralFiction",
        "Biography",
        "NonFiction",
        "SciFi",
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
lib_LibSys_strategy = st.builds(
    lib_LibSys,
)
lib_Book_strategy = st.builds(
    lib_Book,
    pages=
        st.integers(),
    category=
        safe_text,
    title=
        safe_text
)
lib_Writer_strategy = st.builds(
    lib_Writer,
    name=
        safe_text
)
lib_Library_strategy = st.builds(
    lib_Library,
    location=
        safe_text,
    name=
        safe_text
)

@given(instance=lib_LibSys_strategy)
@settings(max_examples=50)
def test_lib_libsys_instantiation(instance):
    assert isinstance(instance, lib_LibSys)

@given(instance=lib_Book_strategy)
@settings(max_examples=50)
def test_lib_book_instantiation(instance):
    assert isinstance(instance, lib_Book)



@given(instance=lib_Book_strategy)
def test_lib_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=lib_Book_strategy)
def test_lib_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=lib_Book_strategy)
def test_lib_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=lib_Writer_strategy)
@settings(max_examples=50)
def test_lib_writer_instantiation(instance):
    assert isinstance(instance, lib_Writer)



@given(instance=lib_Writer_strategy)
def test_lib_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lib_Library_strategy)
@settings(max_examples=50)
def test_lib_library_instantiation(instance):
    assert isinstance(instance, lib_Library)



@given(instance=lib_Library_strategy)
def test_lib_library_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=lib_Library_strategy)
def test_lib_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
