import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Library::Book,
    Library::Library,
    Library::Writer,
    Category,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(Library::Book)


def test_library::book_constructor_exists():
    assert callable(Library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(Library::Book.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"
    assert "blurb" in params, "Missing parameter 'blurb'"

def test_library::book_has_category():
    assert hasattr(Library::Book, "category")
    descriptor = None
    for klass in Library::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_pages():
    assert hasattr(Library::Book, "pages")
    descriptor = None
    for klass in Library::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_title():
    assert hasattr(Library::Book, "title")
    descriptor = None
    for klass in Library::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_blurb():
    assert hasattr(Library::Book, "blurb")
    descriptor = None
    for klass in Library::Book.__mro__:
        if "blurb" in klass.__dict__:
            descriptor = klass.__dict__["blurb"]
            break
    assert isinstance(descriptor, property)



def test_library::library_is_not_abstract():
    assert not inspect.isabstract(Library::Library)


def test_library::library_constructor_exists():
    assert callable(Library::Library.__init__)


def test_library::library_constructor_args():
    sig = inspect.signature(Library::Library.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_library::library_has_id():
    assert hasattr(Library::Library, "id")
    descriptor = None
    for klass in Library::Library.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_library::library_has_name():
    assert hasattr(Library::Library, "name")
    descriptor = None
    for klass in Library::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library::writer_is_not_abstract():
    assert not inspect.isabstract(Library::Writer)


def test_library::writer_constructor_exists():
    assert callable(Library::Writer.__init__)


def test_library::writer_constructor_args():
    sig = inspect.signature(Library::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_library::writer_has_name():
    assert hasattr(Library::Writer, "name")
    descriptor = None
    for klass in Library::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_library::writer_has_id():
    assert hasattr(Library::Writer, "id")
    descriptor = None
    for klass in Library::Writer.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_category_exists():
    # Check that the Enumeration exists
    assert Category is not None

def test_category_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Category]
    expected_literals = [
        "FICTION",
        "ALL",
        "SCIENCE",
        "POETRY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Category"


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
Library::Book_strategy = st.builds(
    Library::Book,
    category=
        safe_text,
    pages=
        st.integers(),
    title=
        safe_text,
    blurb=
        safe_text
)
Library::Library_strategy = st.builds(
    Library::Library,
    id=
        st.integers(),
    name=
        safe_text
)
Library::Writer_strategy = st.builds(
    Library::Writer,
    name=
        safe_text,
    id=
        st.integers()
)

@given(instance=Library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, Library::Book)

@given(instance=Library::Book_strategy)
def test_library::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=Library::Book_strategy)
def test_library::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=Library::Book_strategy)
def test_library::book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=Library::Book_strategy)
def test_library::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=Library::Book_strategy)
def test_library::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Library::Book_strategy)
def test_library::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Library::Book_strategy)
def test_library::book_blurb_type(instance):
    assert isinstance(instance.blurb, str)


@given(instance=Library::Book_strategy)
def test_library::book_blurb_setter(instance):
    original = instance.blurb
    instance.blurb = original
    assert instance.blurb == original

@given(instance=Library::Library_strategy)
@settings(max_examples=50)
def test_library::library_instantiation(instance):
    assert isinstance(instance, Library::Library)

@given(instance=Library::Library_strategy)
def test_library::library_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=Library::Library_strategy)
def test_library::library_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Library::Library_strategy)
def test_library::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Library::Library_strategy)
def test_library::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Library::Writer_strategy)
@settings(max_examples=50)
def test_library::writer_instantiation(instance):
    assert isinstance(instance, Library::Writer)

@given(instance=Library::Writer_strategy)
def test_library::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Library::Writer_strategy)
def test_library::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Library::Writer_strategy)
def test_library::writer_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=Library::Writer_strategy)
def test_library::writer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
