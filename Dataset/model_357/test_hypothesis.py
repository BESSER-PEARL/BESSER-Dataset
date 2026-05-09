import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    cascadenotall::Library,
    cascadenotall::Book,
    cascadenotall::Writer,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cascadenotall::library_is_not_abstract():
    assert not inspect.isabstract(cascadenotall::Library)


def test_cascadenotall::library_constructor_exists():
    assert callable(cascadenotall::Library.__init__)


def test_cascadenotall::library_constructor_args():
    sig = inspect.signature(cascadenotall::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cascadenotall::library_has_name():
    assert hasattr(cascadenotall::Library, "name")
    descriptor = None
    for klass in cascadenotall::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cascadenotall::book_is_not_abstract():
    assert not inspect.isabstract(cascadenotall::Book)


def test_cascadenotall::book_constructor_exists():
    assert callable(cascadenotall::Book.__init__)


def test_cascadenotall::book_constructor_args():
    sig = inspect.signature(cascadenotall::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "category" in params, "Missing parameter 'category'"

def test_cascadenotall::book_has_title():
    assert hasattr(cascadenotall::Book, "title")
    descriptor = None
    for klass in cascadenotall::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_cascadenotall::book_has_pages():
    assert hasattr(cascadenotall::Book, "pages")
    descriptor = None
    for klass in cascadenotall::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_cascadenotall::book_has_category():
    assert hasattr(cascadenotall::Book, "category")
    descriptor = None
    for klass in cascadenotall::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_cascadenotall::writer_is_not_abstract():
    assert not inspect.isabstract(cascadenotall::Writer)


def test_cascadenotall::writer_constructor_exists():
    assert callable(cascadenotall::Writer.__init__)


def test_cascadenotall::writer_constructor_args():
    sig = inspect.signature(cascadenotall::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cascadenotall::writer_has_name():
    assert hasattr(cascadenotall::Writer, "name")
    descriptor = None
    for klass in cascadenotall::Writer.__mro__:
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
cascadenotall::Library_strategy = st.builds(
    cascadenotall::Library,
    name=
        safe_text
)
cascadenotall::Book_strategy = st.builds(
    cascadenotall::Book,
    title=
        safe_text,
    pages=
        safe_text,
    category=
        safe_text
)
cascadenotall::Writer_strategy = st.builds(
    cascadenotall::Writer,
    name=
        safe_text
)

@given(instance=cascadenotall::Library_strategy)
@settings(max_examples=50)
def test_cascadenotall::library_instantiation(instance):
    assert isinstance(instance, cascadenotall::Library)

@given(instance=cascadenotall::Library_strategy)
def test_cascadenotall::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cascadenotall::Library_strategy)
def test_cascadenotall::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cascadenotall::Book_strategy)
@settings(max_examples=50)
def test_cascadenotall::book_instantiation(instance):
    assert isinstance(instance, cascadenotall::Book)

@given(instance=cascadenotall::Book_strategy)
def test_cascadenotall::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=cascadenotall::Book_strategy)
def test_cascadenotall::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=cascadenotall::Book_strategy)
def test_cascadenotall::book_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=cascadenotall::Book_strategy)
def test_cascadenotall::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=cascadenotall::Book_strategy)
def test_cascadenotall::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=cascadenotall::Book_strategy)
def test_cascadenotall::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=cascadenotall::Writer_strategy)
@settings(max_examples=50)
def test_cascadenotall::writer_instantiation(instance):
    assert isinstance(instance, cascadenotall::Writer)

@given(instance=cascadenotall::Writer_strategy)
def test_cascadenotall::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cascadenotall::Writer_strategy)
def test_cascadenotall::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
