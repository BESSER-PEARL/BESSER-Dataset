import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    eiqlibrary::Writer,
    eiqlibrary::Library,
    eiqlibrary::Book,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_eiqlibrary::writer_is_not_abstract():
    assert not inspect.isabstract(eiqlibrary::Writer)


def test_eiqlibrary::writer_constructor_exists():
    assert callable(eiqlibrary::Writer.__init__)


def test_eiqlibrary::writer_constructor_args():
    sig = inspect.signature(eiqlibrary::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eiqlibrary::writer_has_name():
    assert hasattr(eiqlibrary::Writer, "name")
    descriptor = None
    for klass in eiqlibrary::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eiqlibrary::library_is_not_abstract():
    assert not inspect.isabstract(eiqlibrary::Library)


def test_eiqlibrary::library_constructor_exists():
    assert callable(eiqlibrary::Library.__init__)


def test_eiqlibrary::library_constructor_args():
    sig = inspect.signature(eiqlibrary::Library.__init__)
    params = list(sig.parameters.keys())
    assert "internalRequestCount" in params, "Missing parameter 'internalRequestCount'"
    assert "requestCount" in params, "Missing parameter 'requestCount'"
    assert "address" in params, "Missing parameter 'address'"
    assert "sumOfPages" in params, "Missing parameter 'sumOfPages'"

def test_eiqlibrary::library_has_internalRequestCount():
    assert hasattr(eiqlibrary::Library, "internalRequestCount")
    descriptor = None
    for klass in eiqlibrary::Library.__mro__:
        if "internalRequestCount" in klass.__dict__:
            descriptor = klass.__dict__["internalRequestCount"]
            break
    assert isinstance(descriptor, property)

def test_eiqlibrary::library_has_requestCount():
    assert hasattr(eiqlibrary::Library, "requestCount")
    descriptor = None
    for klass in eiqlibrary::Library.__mro__:
        if "requestCount" in klass.__dict__:
            descriptor = klass.__dict__["requestCount"]
            break
    assert isinstance(descriptor, property)

def test_eiqlibrary::library_has_address():
    assert hasattr(eiqlibrary::Library, "address")
    descriptor = None
    for klass in eiqlibrary::Library.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_eiqlibrary::library_has_sumOfPages():
    assert hasattr(eiqlibrary::Library, "sumOfPages")
    descriptor = None
    for klass in eiqlibrary::Library.__mro__:
        if "sumOfPages" in klass.__dict__:
            descriptor = klass.__dict__["sumOfPages"]
            break
    assert isinstance(descriptor, property)



def test_eiqlibrary::book_is_not_abstract():
    assert not inspect.isabstract(eiqlibrary::Book)


def test_eiqlibrary::book_constructor_exists():
    assert callable(eiqlibrary::Book.__init__)


def test_eiqlibrary::book_constructor_args():
    sig = inspect.signature(eiqlibrary::Book.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"

def test_eiqlibrary::book_has_category():
    assert hasattr(eiqlibrary::Book, "category")
    descriptor = None
    for klass in eiqlibrary::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_eiqlibrary::book_has_pages():
    assert hasattr(eiqlibrary::Book, "pages")
    descriptor = None
    for klass in eiqlibrary::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_eiqlibrary::book_has_title():
    assert hasattr(eiqlibrary::Book, "title")
    descriptor = None
    for klass in eiqlibrary::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
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
        "Drama",
        "History",
        "Art",
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
eiqlibrary::Writer_strategy = st.builds(
    eiqlibrary::Writer,
    name=
        safe_text
)
eiqlibrary::Library_strategy = st.builds(
    eiqlibrary::Library,
    internalRequestCount=
        st.integers(),
    requestCount=
        st.integers(),
    address=
        safe_text,
    sumOfPages=
        st.integers()
)
eiqlibrary::Book_strategy = st.builds(
    eiqlibrary::Book,
    category=
        safe_text,
    pages=
        st.integers(),
    title=
        safe_text
)

@given(instance=eiqlibrary::Writer_strategy)
@settings(max_examples=50)
def test_eiqlibrary::writer_instantiation(instance):
    assert isinstance(instance, eiqlibrary::Writer)

@given(instance=eiqlibrary::Writer_strategy)
def test_eiqlibrary::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eiqlibrary::Writer_strategy)
def test_eiqlibrary::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eiqlibrary::Library_strategy)
@settings(max_examples=50)
def test_eiqlibrary::library_instantiation(instance):
    assert isinstance(instance, eiqlibrary::Library)

@given(instance=eiqlibrary::Library_strategy)
def test_eiqlibrary::library_internalRequestCount_type(instance):
    assert isinstance(instance.internalRequestCount, int)


@given(instance=eiqlibrary::Library_strategy)
def test_eiqlibrary::library_internalRequestCount_setter(instance):
    original = instance.internalRequestCount
    instance.internalRequestCount = original
    assert instance.internalRequestCount == original

@given(instance=eiqlibrary::Library_strategy)
def test_eiqlibrary::library_requestCount_type(instance):
    assert isinstance(instance.requestCount, int)


@given(instance=eiqlibrary::Library_strategy)
def test_eiqlibrary::library_requestCount_setter(instance):
    original = instance.requestCount
    instance.requestCount = original
    assert instance.requestCount == original

@given(instance=eiqlibrary::Library_strategy)
def test_eiqlibrary::library_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=eiqlibrary::Library_strategy)
def test_eiqlibrary::library_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=eiqlibrary::Library_strategy)
def test_eiqlibrary::library_sumOfPages_type(instance):
    assert isinstance(instance.sumOfPages, int)


@given(instance=eiqlibrary::Library_strategy)
def test_eiqlibrary::library_sumOfPages_setter(instance):
    original = instance.sumOfPages
    instance.sumOfPages = original
    assert instance.sumOfPages == original

@given(instance=eiqlibrary::Book_strategy)
@settings(max_examples=50)
def test_eiqlibrary::book_instantiation(instance):
    assert isinstance(instance, eiqlibrary::Book)

@given(instance=eiqlibrary::Book_strategy)
def test_eiqlibrary::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=eiqlibrary::Book_strategy)
def test_eiqlibrary::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=eiqlibrary::Book_strategy)
def test_eiqlibrary::book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=eiqlibrary::Book_strategy)
def test_eiqlibrary::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=eiqlibrary::Book_strategy)
def test_eiqlibrary::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=eiqlibrary::Book_strategy)
def test_eiqlibrary::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
