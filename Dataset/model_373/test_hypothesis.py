import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    elements_Writer,
    elements_Book,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_elements_writer_is_not_abstract():
    assert not inspect.isabstract(elements_Writer)


def test_elements_writer_constructor_exists():
    assert callable(elements_Writer.__init__)


def test_elements_writer_constructor_args():
    sig = inspect.signature(elements_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_elements_writer_has_name():
    assert hasattr(elements_Writer, "name")
    descriptor = None
    for klass in elements_Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_elements_book_is_not_abstract():
    assert not inspect.isabstract(elements_Book)


def test_elements_book_constructor_exists():
    assert callable(elements_Book.__init__)


def test_elements_book_constructor_args():
    sig = inspect.signature(elements_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "category" in params, "Missing parameter 'category'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_elements_book_has_title():
    assert hasattr(elements_Book, "title")
    descriptor = None
    for klass in elements_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_elements_book_has_category():
    assert hasattr(elements_Book, "category")
    descriptor = None
    for klass in elements_Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_elements_book_has_pages():
    assert hasattr(elements_Book, "pages")
    descriptor = None
    for klass in elements_Book.__mro__:
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
elements_Writer_strategy = st.builds(
    elements_Writer,
    name=
        safe_text
)
elements_Book_strategy = st.builds(
    elements_Book,
    title=
        safe_text,
    category=
        safe_text,
    pages=
        safe_text
)

@given(instance=elements_Writer_strategy)
@settings(max_examples=50)
def test_elements_writer_instantiation(instance):
    assert isinstance(instance, elements_Writer)



@given(instance=elements_Writer_strategy)
def test_elements_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=elements_Book_strategy)
@settings(max_examples=50)
def test_elements_book_instantiation(instance):
    assert isinstance(instance, elements_Book)



@given(instance=elements_Book_strategy)
def test_elements_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=elements_Book_strategy)
def test_elements_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=elements_Book_strategy)
def test_elements_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original
