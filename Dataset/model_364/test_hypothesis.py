import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    eiqlibrary_Writer,
    eiqlibrary_Library,
    eiqlibrary_Book,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_eiqlibrary_writer_is_not_abstract():
    assert not inspect.isabstract(eiqlibrary_Writer)


def test_eiqlibrary_writer_constructor_exists():
    assert callable(eiqlibrary_Writer.__init__)


def test_eiqlibrary_writer_constructor_args():
    sig = inspect.signature(eiqlibrary_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eiqlibrary_writer_has_name():
    assert hasattr(eiqlibrary_Writer, "name")
    descriptor = None
    for klass in eiqlibrary_Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eiqlibrary_library_is_not_abstract():
    assert not inspect.isabstract(eiqlibrary_Library)


def test_eiqlibrary_library_constructor_exists():
    assert callable(eiqlibrary_Library.__init__)


def test_eiqlibrary_library_constructor_args():
    sig = inspect.signature(eiqlibrary_Library.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "requestCount" in params, "Missing parameter 'requestCount'"
    assert "internalRequestCount" in params, "Missing parameter 'internalRequestCount'"
    assert "sumOfPages" in params, "Missing parameter 'sumOfPages'"

def test_eiqlibrary_library_has_address():
    assert hasattr(eiqlibrary_Library, "address")
    descriptor = None
    for klass in eiqlibrary_Library.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_eiqlibrary_library_has_requestCount():
    assert hasattr(eiqlibrary_Library, "requestCount")
    descriptor = None
    for klass in eiqlibrary_Library.__mro__:
        if "requestCount" in klass.__dict__:
            descriptor = klass.__dict__["requestCount"]
            break
    assert isinstance(descriptor, property)

def test_eiqlibrary_library_has_internalRequestCount():
    assert hasattr(eiqlibrary_Library, "internalRequestCount")
    descriptor = None
    for klass in eiqlibrary_Library.__mro__:
        if "internalRequestCount" in klass.__dict__:
            descriptor = klass.__dict__["internalRequestCount"]
            break
    assert isinstance(descriptor, property)

def test_eiqlibrary_library_has_sumOfPages():
    assert hasattr(eiqlibrary_Library, "sumOfPages")
    descriptor = None
    for klass in eiqlibrary_Library.__mro__:
        if "sumOfPages" in klass.__dict__:
            descriptor = klass.__dict__["sumOfPages"]
            break
    assert isinstance(descriptor, property)



def test_eiqlibrary_book_is_not_abstract():
    assert not inspect.isabstract(eiqlibrary_Book)


def test_eiqlibrary_book_constructor_exists():
    assert callable(eiqlibrary_Book.__init__)


def test_eiqlibrary_book_constructor_args():
    sig = inspect.signature(eiqlibrary_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "category" in params, "Missing parameter 'category'"

def test_eiqlibrary_book_has_title():
    assert hasattr(eiqlibrary_Book, "title")
    descriptor = None
    for klass in eiqlibrary_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_eiqlibrary_book_has_pages():
    assert hasattr(eiqlibrary_Book, "pages")
    descriptor = None
    for klass in eiqlibrary_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_eiqlibrary_book_has_category():
    assert hasattr(eiqlibrary_Book, "category")
    descriptor = None
    for klass in eiqlibrary_Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "Drama",
        "SciFi",
        "Art",
        "History",
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
eiqlibrary_Writer_strategy = st.builds(
    eiqlibrary_Writer,
    name=
        safe_text
)
eiqlibrary_Library_strategy = st.builds(
    eiqlibrary_Library,
    address=
        safe_text,
    requestCount=
        st.integers(),
    internalRequestCount=
        st.integers(),
    sumOfPages=
        st.integers()
)
eiqlibrary_Book_strategy = st.builds(
    eiqlibrary_Book,
    title=
        safe_text,
    pages=
        st.integers(),
    category=
        safe_text
)

@given(instance=eiqlibrary_Writer_strategy)
@settings(max_examples=50)
def test_eiqlibrary_writer_instantiation(instance):
    assert isinstance(instance, eiqlibrary_Writer)



@given(instance=eiqlibrary_Writer_strategy)
def test_eiqlibrary_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eiqlibrary_Library_strategy)
@settings(max_examples=50)
def test_eiqlibrary_library_instantiation(instance):
    assert isinstance(instance, eiqlibrary_Library)



@given(instance=eiqlibrary_Library_strategy)
def test_eiqlibrary_library_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=eiqlibrary_Library_strategy)
def test_eiqlibrary_library_requestCount_setter(instance):
    original = instance.requestCount
    instance.requestCount = original
    assert instance.requestCount == original



@given(instance=eiqlibrary_Library_strategy)
def test_eiqlibrary_library_internalRequestCount_setter(instance):
    original = instance.internalRequestCount
    instance.internalRequestCount = original
    assert instance.internalRequestCount == original



@given(instance=eiqlibrary_Library_strategy)
def test_eiqlibrary_library_sumOfPages_setter(instance):
    original = instance.sumOfPages
    instance.sumOfPages = original
    assert instance.sumOfPages == original

@given(instance=eiqlibrary_Book_strategy)
@settings(max_examples=50)
def test_eiqlibrary_book_instantiation(instance):
    assert isinstance(instance, eiqlibrary_Book)



@given(instance=eiqlibrary_Book_strategy)
def test_eiqlibrary_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=eiqlibrary_Book_strategy)
def test_eiqlibrary_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=eiqlibrary_Book_strategy)
def test_eiqlibrary_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original
