import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    emftest::Library,
    emftest::BookCollection,
    Book,
    emftest::ParentBook,
    emftest::ChildBook,
    emftest::Author,
    emftest::Book,
    BookType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_emftest::library_is_not_abstract():
    assert not inspect.isabstract(emftest::Library)


def test_emftest::library_constructor_exists():
    assert callable(emftest::Library.__init__)


def test_emftest::library_constructor_args():
    sig = inspect.signature(emftest::Library.__init__)
    params = list(sig.parameters.keys())



def test_emftest::bookcollection_is_not_abstract():
    assert not inspect.isabstract(emftest::BookCollection)


def test_emftest::bookcollection_constructor_exists():
    assert callable(emftest::BookCollection.__init__)


def test_emftest::bookcollection_constructor_args():
    sig = inspect.signature(emftest::BookCollection.__init__)
    params = list(sig.parameters.keys())



def test_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_book_constructor_exists():
    assert callable(Book.__init__)


def test_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())



def test_emftest::parentbook_is_not_abstract():
    assert not inspect.isabstract(emftest::ParentBook)


def test_emftest::parentbook_constructor_exists():
    assert callable(emftest::ParentBook.__init__)


def test_emftest::parentbook_constructor_args():
    sig = inspect.signature(emftest::ParentBook.__init__)
    params = list(sig.parameters.keys())



def test_emftest::childbook_is_not_abstract():
    assert not inspect.isabstract(emftest::ChildBook)


def test_emftest::childbook_constructor_exists():
    assert callable(emftest::ChildBook.__init__)


def test_emftest::childbook_constructor_args():
    sig = inspect.signature(emftest::ChildBook.__init__)
    params = list(sig.parameters.keys())



def test_emftest::author_is_not_abstract():
    assert not inspect.isabstract(emftest::Author)


def test_emftest::author_constructor_exists():
    assert callable(emftest::Author.__init__)


def test_emftest::author_constructor_args():
    sig = inspect.signature(emftest::Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emftest::author_has_name():
    assert hasattr(emftest::Author, "name")
    descriptor = None
    for klass in emftest::Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emftest::book_is_not_abstract():
    assert not inspect.isabstract(emftest::Book)


def test_emftest::book_constructor_exists():
    assert callable(emftest::Book.__init__)


def test_emftest::book_constructor_args():
    sig = inspect.signature(emftest::Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"

def test_emftest::book_has_pages():
    assert hasattr(emftest::Book, "pages")
    descriptor = None
    for klass in emftest::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_emftest::book_has_title():
    assert hasattr(emftest::Book, "title")
    descriptor = None
    for klass in emftest::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_booktype_exists():
    # Check that the Enumeration exists
    assert BookType is not None

def test_booktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookType]
    expected_literals = [
        "Parent",
        "Child",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BookType"


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
emftest::Library_strategy = st.builds(
    emftest::Library,
)
emftest::BookCollection_strategy = st.builds(
    emftest::BookCollection,
)
Book_strategy = st.builds(
    Book,
)
emftest::ParentBook_strategy = st.builds(
    emftest::ParentBook,
)
emftest::ChildBook_strategy = st.builds(
    emftest::ChildBook,
)
emftest::Author_strategy = st.builds(
    emftest::Author,
    name=
        safe_text
)
emftest::Book_strategy = st.builds(
    emftest::Book,
    pages=
        st.integers(),
    title=
        safe_text
)

@given(instance=emftest::Library_strategy)
@settings(max_examples=50)
def test_emftest::library_instantiation(instance):
    assert isinstance(instance, emftest::Library)

@given(instance=emftest::BookCollection_strategy)
@settings(max_examples=50)
def test_emftest::bookcollection_instantiation(instance):
    assert isinstance(instance, emftest::BookCollection)

@given(instance=Book_strategy)
@settings(max_examples=50)
def test_book_instantiation(instance):
    assert isinstance(instance, Book)

@given(instance=emftest::ParentBook_strategy)
@settings(max_examples=50)
def test_emftest::parentbook_instantiation(instance):
    assert isinstance(instance, emftest::ParentBook)

@given(instance=emftest::ChildBook_strategy)
@settings(max_examples=50)
def test_emftest::childbook_instantiation(instance):
    assert isinstance(instance, emftest::ChildBook)

@given(instance=emftest::Author_strategy)
@settings(max_examples=50)
def test_emftest::author_instantiation(instance):
    assert isinstance(instance, emftest::Author)

@given(instance=emftest::Author_strategy)
def test_emftest::author_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emftest::Author_strategy)
def test_emftest::author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=emftest::Author_strategy)
@settings(max_examples=30)
def test_emftest::author_writebook_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.writeBook(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.writeBook).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'writeBook' in emftest::Author is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'writeBook' in emftest::Author did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'writeBook' in emftest::Author is not implemented or raised an error")

@given(instance=emftest::Book_strategy)
@settings(max_examples=50)
def test_emftest::book_instantiation(instance):
    assert isinstance(instance, emftest::Book)

@given(instance=emftest::Book_strategy)
def test_emftest::book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=emftest::Book_strategy)
def test_emftest::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=emftest::Book_strategy)
def test_emftest::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=emftest::Book_strategy)
def test_emftest::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
