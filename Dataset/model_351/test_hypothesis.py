import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    eavlibrary_Library,
    eavlibrary_City,
    eavlibrary_Writer,
    eavlibrary_Book,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_eavlibrary_library_is_not_abstract():
    assert not inspect.isabstract(eavlibrary_Library)


def test_eavlibrary_library_constructor_exists():
    assert callable(eavlibrary_Library.__init__)


def test_eavlibrary_library_constructor_args():
    sig = inspect.signature(eavlibrary_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eavlibrary_library_has_name():
    assert hasattr(eavlibrary_Library, "name")
    descriptor = None
    for klass in eavlibrary_Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eavlibrary_city_is_not_abstract():
    assert not inspect.isabstract(eavlibrary_City)


def test_eavlibrary_city_constructor_exists():
    assert callable(eavlibrary_City.__init__)


def test_eavlibrary_city_constructor_args():
    sig = inspect.signature(eavlibrary_City.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eavlibrary_city_has_name():
    assert hasattr(eavlibrary_City, "name")
    descriptor = None
    for klass in eavlibrary_City.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eavlibrary_writer_is_not_abstract():
    assert not inspect.isabstract(eavlibrary_Writer)


def test_eavlibrary_writer_constructor_exists():
    assert callable(eavlibrary_Writer.__init__)


def test_eavlibrary_writer_constructor_args():
    sig = inspect.signature(eavlibrary_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eavlibrary_writer_has_name():
    assert hasattr(eavlibrary_Writer, "name")
    descriptor = None
    for klass in eavlibrary_Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eavlibrary_book_is_not_abstract():
    assert not inspect.isabstract(eavlibrary_Book)


def test_eavlibrary_book_constructor_exists():
    assert callable(eavlibrary_Book.__init__)


def test_eavlibrary_book_constructor_args():
    sig = inspect.signature(eavlibrary_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "category" in params, "Missing parameter 'category'"
    assert "test" in params, "Missing parameter 'test'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_eavlibrary_book_has_title():
    assert hasattr(eavlibrary_Book, "title")
    descriptor = None
    for klass in eavlibrary_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_eavlibrary_book_has_category():
    assert hasattr(eavlibrary_Book, "category")
    descriptor = None
    for klass in eavlibrary_Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_eavlibrary_book_has_test():
    assert hasattr(eavlibrary_Book, "test")
    descriptor = None
    for klass in eavlibrary_Book.__mro__:
        if "test" in klass.__dict__:
            descriptor = klass.__dict__["test"]
            break
    assert isinstance(descriptor, property)

def test_eavlibrary_book_has_pages():
    assert hasattr(eavlibrary_Book, "pages")
    descriptor = None
    for klass in eavlibrary_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
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
eavlibrary_Library_strategy = st.builds(
    eavlibrary_Library,
    name=
        safe_text
)
eavlibrary_City_strategy = st.builds(
    eavlibrary_City,
    name=
        safe_text
)
eavlibrary_Writer_strategy = st.builds(
    eavlibrary_Writer,
    name=
        safe_text
)
eavlibrary_Book_strategy = st.builds(
    eavlibrary_Book,
    title=
        safe_text,
    category=
        safe_text,
    test=
        safe_text,
    pages=
        safe_text
)

@given(instance=eavlibrary_Library_strategy)
@settings(max_examples=50)
def test_eavlibrary_library_instantiation(instance):
    assert isinstance(instance, eavlibrary_Library)



@given(instance=eavlibrary_Library_strategy)
def test_eavlibrary_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eavlibrary_City_strategy)
@settings(max_examples=50)
def test_eavlibrary_city_instantiation(instance):
    assert isinstance(instance, eavlibrary_City)



@given(instance=eavlibrary_City_strategy)
def test_eavlibrary_city_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eavlibrary_Writer_strategy)
@settings(max_examples=50)
def test_eavlibrary_writer_instantiation(instance):
    assert isinstance(instance, eavlibrary_Writer)



@given(instance=eavlibrary_Writer_strategy)
def test_eavlibrary_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eavlibrary_Book_strategy)
@settings(max_examples=50)
def test_eavlibrary_book_instantiation(instance):
    assert isinstance(instance, eavlibrary_Book)



@given(instance=eavlibrary_Book_strategy)
def test_eavlibrary_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=eavlibrary_Book_strategy)
def test_eavlibrary_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=eavlibrary_Book_strategy)
def test_eavlibrary_book_test_setter(instance):
    original = instance.test
    instance.test = original
    assert instance.test == original



@given(instance=eavlibrary_Book_strategy)
def test_eavlibrary_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original
