import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    library::Book,
    library::Writer,
    library::Library,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::Book)


def test_library::book_constructor_exists():
    assert callable(library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "category" in params, "Missing parameter 'category'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_library::book_has_title():
    assert hasattr(library::Book, "title")
    descriptor = None
    for klass in library::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_category():
    assert hasattr(library::Book, "category")
    descriptor = None
    for klass in library::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_pages():
    assert hasattr(library::Book, "pages")
    descriptor = None
    for klass in library::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_library::writer_is_not_abstract():
    assert not inspect.isabstract(library::Writer)


def test_library::writer_constructor_exists():
    assert callable(library::Writer.__init__)


def test_library::writer_constructor_args():
    sig = inspect.signature(library::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::writer_has_name():
    assert hasattr(library::Writer, "name")
    descriptor = None
    for klass in library::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library::library_is_not_abstract():
    assert not inspect.isabstract(library::Library)


def test_library::library_constructor_exists():
    assert callable(library::Library.__init__)


def test_library::library_constructor_args():
    sig = inspect.signature(library::Library.__init__)
    params = list(sig.parameters.keys())
    assert "sumOfPages" in params, "Missing parameter 'sumOfPages'"
    assert "address" in params, "Missing parameter 'address'"
    assert "requestCount" in params, "Missing parameter 'requestCount'"
    assert "internalRequestCount" in params, "Missing parameter 'internalRequestCount'"

def test_library::library_has_sumOfPages():
    assert hasattr(library::Library, "sumOfPages")
    descriptor = None
    for klass in library::Library.__mro__:
        if "sumOfPages" in klass.__dict__:
            descriptor = klass.__dict__["sumOfPages"]
            break
    assert isinstance(descriptor, property)

def test_library::library_has_address():
    assert hasattr(library::Library, "address")
    descriptor = None
    for klass in library::Library.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_library::library_has_requestCount():
    assert hasattr(library::Library, "requestCount")
    descriptor = None
    for klass in library::Library.__mro__:
        if "requestCount" in klass.__dict__:
            descriptor = klass.__dict__["requestCount"]
            break
    assert isinstance(descriptor, property)

def test_library::library_has_internalRequestCount():
    assert hasattr(library::Library, "internalRequestCount")
    descriptor = None
    for klass in library::Library.__mro__:
        if "internalRequestCount" in klass.__dict__:
            descriptor = klass.__dict__["internalRequestCount"]
            break
    assert isinstance(descriptor, property)

def test_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "SciFi",
        "Art",
        "History",
        "Drama",
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
library::Book_strategy = st.builds(
    library::Book,
    title=
        safe_text,
    category=
        safe_text,
    pages=
        st.integers()
)
library::Writer_strategy = st.builds(
    library::Writer,
    name=
        safe_text
)
library::Library_strategy = st.builds(
    library::Library,
    sumOfPages=
        st.integers(),
    address=
        safe_text,
    requestCount=
        st.integers(),
    internalRequestCount=
        st.integers()
)

@given(instance=library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::Book)

@given(instance=library::Book_strategy)
def test_library::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::Book_strategy)
def test_library::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library::Book_strategy)
def test_library::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=library::Book_strategy)
def test_library::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=library::Book_strategy)
def test_library::book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=library::Book_strategy)
def test_library::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=library::Writer_strategy)
@settings(max_examples=50)
def test_library::writer_instantiation(instance):
    assert isinstance(instance, library::Writer)

@given(instance=library::Writer_strategy)
def test_library::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Writer_strategy)
def test_library::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library::Library_strategy)
@settings(max_examples=50)
def test_library::library_instantiation(instance):
    assert isinstance(instance, library::Library)

@given(instance=library::Library_strategy)
def test_library::library_sumOfPages_type(instance):
    assert isinstance(instance.sumOfPages, int)


@given(instance=library::Library_strategy)
def test_library::library_sumOfPages_setter(instance):
    original = instance.sumOfPages
    instance.sumOfPages = original
    assert instance.sumOfPages == original

@given(instance=library::Library_strategy)
def test_library::library_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=library::Library_strategy)
def test_library::library_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=library::Library_strategy)
def test_library::library_requestCount_type(instance):
    assert isinstance(instance.requestCount, int)


@given(instance=library::Library_strategy)
def test_library::library_requestCount_setter(instance):
    original = instance.requestCount
    instance.requestCount = original
    assert instance.requestCount == original

@given(instance=library::Library_strategy)
def test_library::library_internalRequestCount_type(instance):
    assert isinstance(instance.internalRequestCount, int)


@given(instance=library::Library_strategy)
def test_library::library_internalRequestCount_setter(instance):
    original = instance.internalRequestCount
    instance.internalRequestCount = original
    assert instance.internalRequestCount == original
