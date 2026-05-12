import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    libraryModel_Book,
    libraryModel_Writer,
    libraryModel_Library,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_librarymodel_book_is_not_abstract():
    assert not inspect.isabstract(libraryModel_Book)


def test_librarymodel_book_constructor_exists():
    assert callable(libraryModel_Book.__init__)


def test_librarymodel_book_constructor_args():
    sig = inspect.signature(libraryModel_Book.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"

def test_librarymodel_book_has_category():
    assert hasattr(libraryModel_Book, "category")
    descriptor = None
    for klass in libraryModel_Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_librarymodel_book_has_pages():
    assert hasattr(libraryModel_Book, "pages")
    descriptor = None
    for klass in libraryModel_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_librarymodel_book_has_title():
    assert hasattr(libraryModel_Book, "title")
    descriptor = None
    for klass in libraryModel_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_librarymodel_writer_is_not_abstract():
    assert not inspect.isabstract(libraryModel_Writer)


def test_librarymodel_writer_constructor_exists():
    assert callable(libraryModel_Writer.__init__)


def test_librarymodel_writer_constructor_args():
    sig = inspect.signature(libraryModel_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_librarymodel_writer_has_name():
    assert hasattr(libraryModel_Writer, "name")
    descriptor = None
    for klass in libraryModel_Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_librarymodel_library_is_not_abstract():
    assert not inspect.isabstract(libraryModel_Library)


def test_librarymodel_library_constructor_exists():
    assert callable(libraryModel_Library.__init__)


def test_librarymodel_library_constructor_args():
    sig = inspect.signature(libraryModel_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_librarymodel_library_has_name():
    assert hasattr(libraryModel_Library, "name")
    descriptor = None
    for klass in libraryModel_Library.__mro__:
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
        "Mystery",
        "Biography",
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
libraryModel_Book_strategy = st.builds(
    libraryModel_Book,
    category=
        safe_text,
    pages=
        st.integers(),
    title=
        safe_text
)
libraryModel_Writer_strategy = st.builds(
    libraryModel_Writer,
    name=
        safe_text
)
libraryModel_Library_strategy = st.builds(
    libraryModel_Library,
    name=
        safe_text
)

@given(instance=libraryModel_Book_strategy)
@settings(max_examples=50)
def test_librarymodel_book_instantiation(instance):
    assert isinstance(instance, libraryModel_Book)



@given(instance=libraryModel_Book_strategy)
def test_librarymodel_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=libraryModel_Book_strategy)
def test_librarymodel_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=libraryModel_Book_strategy)
def test_librarymodel_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=libraryModel_Writer_strategy)
@settings(max_examples=50)
def test_librarymodel_writer_instantiation(instance):
    assert isinstance(instance, libraryModel_Writer)



@given(instance=libraryModel_Writer_strategy)
def test_librarymodel_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=libraryModel_Library_strategy)
@settings(max_examples=50)
def test_librarymodel_library_instantiation(instance):
    assert isinstance(instance, libraryModel_Library)



@given(instance=libraryModel_Library_strategy)
def test_librarymodel_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
