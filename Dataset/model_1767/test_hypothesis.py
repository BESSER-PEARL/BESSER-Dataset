import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    elements_EObject,
    Person,
    elements_Writer,
    elements_Book,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_elements_eobject_is_not_abstract():
    assert not inspect.isabstract(elements_EObject)


def test_elements_eobject_constructor_exists():
    assert callable(elements_EObject.__init__)


def test_elements_eobject_constructor_args():
    sig = inspect.signature(elements_EObject.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_elements_writer_is_not_abstract():
    assert not inspect.isabstract(elements_Writer)


def test_elements_writer_constructor_exists():
    assert callable(elements_Writer.__init__)


def test_elements_writer_constructor_args():
    sig = inspect.signature(elements_Writer.__init__)
    params = list(sig.parameters.keys())



def test_elements_book_is_not_abstract():
    assert not inspect.isabstract(elements_Book)


def test_elements_book_constructor_exists():
    assert callable(elements_Book.__init__)


def test_elements_book_constructor_args():
    sig = inspect.signature(elements_Book.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "uuid" in params, "Missing parameter 'uuid'"
    assert "title" in params, "Missing parameter 'title'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_elements_book_has_category():
    assert hasattr(elements_Book, "category")
    descriptor = None
    for klass in elements_Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_elements_book_has_uuid():
    assert hasattr(elements_Book, "uuid")
    descriptor = None
    for klass in elements_Book.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)

def test_elements_book_has_title():
    assert hasattr(elements_Book, "title")
    descriptor = None
    for klass in elements_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
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
        "IT",
        "Biography",
        "Mystery",
        "ScienceFiction",
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
elements_EObject_strategy = st.builds(
    elements_EObject,
)
Person_strategy = st.builds(
    Person,
)
elements_Writer_strategy = st.builds(
    elements_Writer,
)
elements_Book_strategy = st.builds(
    elements_Book,
    category=
        safe_text,
    uuid=
        safe_text,
    title=
        safe_text,
    pages=
        safe_text
)

@given(instance=elements_EObject_strategy)
@settings(max_examples=50)
def test_elements_eobject_instantiation(instance):
    assert isinstance(instance, elements_EObject)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=elements_Writer_strategy)
@settings(max_examples=50)
def test_elements_writer_instantiation(instance):
    assert isinstance(instance, elements_Writer)

@given(instance=elements_Book_strategy)
@settings(max_examples=50)
def test_elements_book_instantiation(instance):
    assert isinstance(instance, elements_Book)



@given(instance=elements_Book_strategy)
def test_elements_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=elements_Book_strategy)
def test_elements_book_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original



@given(instance=elements_Book_strategy)
def test_elements_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=elements_Book_strategy)
def test_elements_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original
