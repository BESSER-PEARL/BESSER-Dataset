import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    lib::LibSys,
    lib::Book,
    lib::Writer,
    lib::Library,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lib::libsys_is_not_abstract():
    assert not inspect.isabstract(lib::LibSys)


def test_lib::libsys_constructor_exists():
    assert callable(lib::LibSys.__init__)


def test_lib::libsys_constructor_args():
    sig = inspect.signature(lib::LibSys.__init__)
    params = list(sig.parameters.keys())



def test_lib::book_is_not_abstract():
    assert not inspect.isabstract(lib::Book)


def test_lib::book_constructor_exists():
    assert callable(lib::Book.__init__)


def test_lib::book_constructor_args():
    sig = inspect.signature(lib::Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"
    assert "category" in params, "Missing parameter 'category'"

def test_lib::book_has_pages():
    assert hasattr(lib::Book, "pages")
    descriptor = None
    for klass in lib::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_lib::book_has_title():
    assert hasattr(lib::Book, "title")
    descriptor = None
    for klass in lib::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_lib::book_has_category():
    assert hasattr(lib::Book, "category")
    descriptor = None
    for klass in lib::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_lib::writer_is_not_abstract():
    assert not inspect.isabstract(lib::Writer)


def test_lib::writer_constructor_exists():
    assert callable(lib::Writer.__init__)


def test_lib::writer_constructor_args():
    sig = inspect.signature(lib::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lib::writer_has_name():
    assert hasattr(lib::Writer, "name")
    descriptor = None
    for klass in lib::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lib::library_is_not_abstract():
    assert not inspect.isabstract(lib::Library)


def test_lib::library_constructor_exists():
    assert callable(lib::Library.__init__)


def test_lib::library_constructor_args():
    sig = inspect.signature(lib::Library.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "name" in params, "Missing parameter 'name'"

def test_lib::library_has_location():
    assert hasattr(lib::Library, "location")
    descriptor = None
    for klass in lib::Library.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_lib::library_has_name():
    assert hasattr(lib::Library, "name")
    descriptor = None
    for klass in lib::Library.__mro__:
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
        "SciFi",
        "NonFiction",
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
lib::LibSys_strategy = st.builds(
    lib::LibSys,
)
lib::Book_strategy = st.builds(
    lib::Book,
    pages=
        st.integers(),
    title=
        safe_text,
    category=
        safe_text
)
lib::Writer_strategy = st.builds(
    lib::Writer,
    name=
        safe_text
)
lib::Library_strategy = st.builds(
    lib::Library,
    location=
        safe_text,
    name=
        safe_text
)

@given(instance=lib::LibSys_strategy)
@settings(max_examples=50)
def test_lib::libsys_instantiation(instance):
    assert isinstance(instance, lib::LibSys)

@given(instance=lib::Book_strategy)
@settings(max_examples=50)
def test_lib::book_instantiation(instance):
    assert isinstance(instance, lib::Book)

@given(instance=lib::Book_strategy)
def test_lib::book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=lib::Book_strategy)
def test_lib::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=lib::Book_strategy)
def test_lib::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=lib::Book_strategy)
def test_lib::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=lib::Book_strategy)
def test_lib::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=lib::Book_strategy)
def test_lib::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=lib::Writer_strategy)
@settings(max_examples=50)
def test_lib::writer_instantiation(instance):
    assert isinstance(instance, lib::Writer)

@given(instance=lib::Writer_strategy)
def test_lib::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lib::Writer_strategy)
def test_lib::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lib::Library_strategy)
@settings(max_examples=50)
def test_lib::library_instantiation(instance):
    assert isinstance(instance, lib::Library)

@given(instance=lib::Library_strategy)
def test_lib::library_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=lib::Library_strategy)
def test_lib::library_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=lib::Library_strategy)
def test_lib::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lib::Library_strategy)
def test_lib::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
