import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    lazy_Book,
    lazy_Library,
    lazy_Writer,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lazy_book_is_not_abstract():
    assert not inspect.isabstract(lazy_Book)


def test_lazy_book_constructor_exists():
    assert callable(lazy_Book.__init__)


def test_lazy_book_constructor_args():
    sig = inspect.signature(lazy_Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "category" in params, "Missing parameter 'category'"
    assert "title" in params, "Missing parameter 'title'"

def test_lazy_book_has_pages():
    assert hasattr(lazy_Book, "pages")
    descriptor = None
    for klass in lazy_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_lazy_book_has_category():
    assert hasattr(lazy_Book, "category")
    descriptor = None
    for klass in lazy_Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_lazy_book_has_title():
    assert hasattr(lazy_Book, "title")
    descriptor = None
    for klass in lazy_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_lazy_library_is_not_abstract():
    assert not inspect.isabstract(lazy_Library)


def test_lazy_library_constructor_exists():
    assert callable(lazy_Library.__init__)


def test_lazy_library_constructor_args():
    sig = inspect.signature(lazy_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lazy_library_has_name():
    assert hasattr(lazy_Library, "name")
    descriptor = None
    for klass in lazy_Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lazy_writer_is_not_abstract():
    assert not inspect.isabstract(lazy_Writer)


def test_lazy_writer_constructor_exists():
    assert callable(lazy_Writer.__init__)


def test_lazy_writer_constructor_args():
    sig = inspect.signature(lazy_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lazy_writer_has_name():
    assert hasattr(lazy_Writer, "name")
    descriptor = None
    for klass in lazy_Writer.__mro__:
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
        "ScienceFiction",
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
lazy_Book_strategy = st.builds(
    lazy_Book,
    pages=
        safe_text,
    category=
        safe_text,
    title=
        safe_text
)
lazy_Library_strategy = st.builds(
    lazy_Library,
    name=
        safe_text
)
lazy_Writer_strategy = st.builds(
    lazy_Writer,
    name=
        safe_text
)

@given(instance=lazy_Book_strategy)
@settings(max_examples=50)
def test_lazy_book_instantiation(instance):
    assert isinstance(instance, lazy_Book)



@given(instance=lazy_Book_strategy)
def test_lazy_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=lazy_Book_strategy)
def test_lazy_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=lazy_Book_strategy)
def test_lazy_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=lazy_Library_strategy)
@settings(max_examples=50)
def test_lazy_library_instantiation(instance):
    assert isinstance(instance, lazy_Library)



@given(instance=lazy_Library_strategy)
def test_lazy_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lazy_Writer_strategy)
@settings(max_examples=50)
def test_lazy_writer_instantiation(instance):
    assert isinstance(instance, lazy_Writer)



@given(instance=lazy_Writer_strategy)
def test_lazy_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
