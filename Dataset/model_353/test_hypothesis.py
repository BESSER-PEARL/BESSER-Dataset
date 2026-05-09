import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    libraryModel::Book,
    libraryModel::Writer,
    libraryModel::Library,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_librarymodel::book_is_not_abstract():
    assert not inspect.isabstract(libraryModel::Book)


def test_librarymodel::book_constructor_exists():
    assert callable(libraryModel::Book.__init__)


def test_librarymodel::book_constructor_args():
    sig = inspect.signature(libraryModel::Book.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "title" in params, "Missing parameter 'title'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_librarymodel::book_has_category():
    assert hasattr(libraryModel::Book, "category")
    descriptor = None
    for klass in libraryModel::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_librarymodel::book_has_title():
    assert hasattr(libraryModel::Book, "title")
    descriptor = None
    for klass in libraryModel::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_librarymodel::book_has_pages():
    assert hasattr(libraryModel::Book, "pages")
    descriptor = None
    for klass in libraryModel::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_librarymodel::writer_is_not_abstract():
    assert not inspect.isabstract(libraryModel::Writer)


def test_librarymodel::writer_constructor_exists():
    assert callable(libraryModel::Writer.__init__)


def test_librarymodel::writer_constructor_args():
    sig = inspect.signature(libraryModel::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_librarymodel::writer_has_name():
    assert hasattr(libraryModel::Writer, "name")
    descriptor = None
    for klass in libraryModel::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_librarymodel::library_is_not_abstract():
    assert not inspect.isabstract(libraryModel::Library)


def test_librarymodel::library_constructor_exists():
    assert callable(libraryModel::Library.__init__)


def test_librarymodel::library_constructor_args():
    sig = inspect.signature(libraryModel::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_librarymodel::library_has_name():
    assert hasattr(libraryModel::Library, "name")
    descriptor = None
    for klass in libraryModel::Library.__mro__:
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
libraryModel::Book_strategy = st.builds(
    libraryModel::Book,
    category=
        safe_text,
    title=
        safe_text,
    pages=
        st.integers()
)
libraryModel::Writer_strategy = st.builds(
    libraryModel::Writer,
    name=
        safe_text
)
libraryModel::Library_strategy = st.builds(
    libraryModel::Library,
    name=
        safe_text
)

@given(instance=libraryModel::Book_strategy)
@settings(max_examples=50)
def test_librarymodel::book_instantiation(instance):
    assert isinstance(instance, libraryModel::Book)

@given(instance=libraryModel::Book_strategy)
def test_librarymodel::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=libraryModel::Book_strategy)
def test_librarymodel::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=libraryModel::Book_strategy)
def test_librarymodel::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=libraryModel::Book_strategy)
def test_librarymodel::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=libraryModel::Book_strategy)
def test_librarymodel::book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=libraryModel::Book_strategy)
def test_librarymodel::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=libraryModel::Writer_strategy)
@settings(max_examples=50)
def test_librarymodel::writer_instantiation(instance):
    assert isinstance(instance, libraryModel::Writer)

@given(instance=libraryModel::Writer_strategy)
def test_librarymodel::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=libraryModel::Writer_strategy)
def test_librarymodel::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=libraryModel::Library_strategy)
@settings(max_examples=50)
def test_librarymodel::library_instantiation(instance):
    assert isinstance(instance, libraryModel::Library)

@given(instance=libraryModel::Library_strategy)
def test_librarymodel::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=libraryModel::Library_strategy)
def test_librarymodel::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
