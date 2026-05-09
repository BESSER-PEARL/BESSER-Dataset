import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    elements::Book,
    elements::Writer,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_elements::book_is_not_abstract():
    assert not inspect.isabstract(elements::Book)


def test_elements::book_constructor_exists():
    assert callable(elements::Book.__init__)


def test_elements::book_constructor_args():
    sig = inspect.signature(elements::Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "category" in params, "Missing parameter 'category'"
    assert "title" in params, "Missing parameter 'title'"

def test_elements::book_has_pages():
    assert hasattr(elements::Book, "pages")
    descriptor = None
    for klass in elements::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_elements::book_has_category():
    assert hasattr(elements::Book, "category")
    descriptor = None
    for klass in elements::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_elements::book_has_title():
    assert hasattr(elements::Book, "title")
    descriptor = None
    for klass in elements::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_elements::writer_is_not_abstract():
    assert not inspect.isabstract(elements::Writer)


def test_elements::writer_constructor_exists():
    assert callable(elements::Writer.__init__)


def test_elements::writer_constructor_args():
    sig = inspect.signature(elements::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_elements::writer_has_name():
    assert hasattr(elements::Writer, "name")
    descriptor = None
    for klass in elements::Writer.__mro__:
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
        "Mystery",
        "ScienceFiction",
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
elements::Book_strategy = st.builds(
    elements::Book,
    pages=
        safe_text,
    category=
        safe_text,
    title=
        safe_text
)
elements::Writer_strategy = st.builds(
    elements::Writer,
    name=
        safe_text
)

@given(instance=elements::Book_strategy)
@settings(max_examples=50)
def test_elements::book_instantiation(instance):
    assert isinstance(instance, elements::Book)

@given(instance=elements::Book_strategy)
def test_elements::book_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=elements::Book_strategy)
def test_elements::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=elements::Book_strategy)
def test_elements::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=elements::Book_strategy)
def test_elements::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=elements::Book_strategy)
def test_elements::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=elements::Book_strategy)
def test_elements::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=elements::Writer_strategy)
@settings(max_examples=50)
def test_elements::writer_instantiation(instance):
    assert isinstance(instance, elements::Writer)

@given(instance=elements::Writer_strategy)
def test_elements::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=elements::Writer_strategy)
def test_elements::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
