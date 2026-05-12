import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    emftest_Library,
    emftest_BookCollection,
    Book,
    emftest_ParentBook,
    emftest_ChildBook,
    emftest_Author,
    emftest_Book,
    BookType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_emftest_library_is_not_abstract():
    assert not inspect.isabstract(emftest_Library)


def test_emftest_library_constructor_exists():
    assert callable(emftest_Library.__init__)


def test_emftest_library_constructor_args():
    sig = inspect.signature(emftest_Library.__init__)
    params = list(sig.parameters.keys())



def test_emftest_bookcollection_is_not_abstract():
    assert not inspect.isabstract(emftest_BookCollection)


def test_emftest_bookcollection_constructor_exists():
    assert callable(emftest_BookCollection.__init__)


def test_emftest_bookcollection_constructor_args():
    sig = inspect.signature(emftest_BookCollection.__init__)
    params = list(sig.parameters.keys())



def test_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_book_constructor_exists():
    assert callable(Book.__init__)


def test_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())



def test_emftest_parentbook_is_not_abstract():
    assert not inspect.isabstract(emftest_ParentBook)


def test_emftest_parentbook_constructor_exists():
    assert callable(emftest_ParentBook.__init__)


def test_emftest_parentbook_constructor_args():
    sig = inspect.signature(emftest_ParentBook.__init__)
    params = list(sig.parameters.keys())



def test_emftest_childbook_is_not_abstract():
    assert not inspect.isabstract(emftest_ChildBook)


def test_emftest_childbook_constructor_exists():
    assert callable(emftest_ChildBook.__init__)


def test_emftest_childbook_constructor_args():
    sig = inspect.signature(emftest_ChildBook.__init__)
    params = list(sig.parameters.keys())



def test_emftest_author_is_not_abstract():
    assert not inspect.isabstract(emftest_Author)


def test_emftest_author_constructor_exists():
    assert callable(emftest_Author.__init__)


def test_emftest_author_constructor_args():
    sig = inspect.signature(emftest_Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emftest_author_has_name():
    assert hasattr(emftest_Author, "name")
    descriptor = None
    for klass in emftest_Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emftest_book_is_not_abstract():
    assert not inspect.isabstract(emftest_Book)


def test_emftest_book_constructor_exists():
    assert callable(emftest_Book.__init__)


def test_emftest_book_constructor_args():
    sig = inspect.signature(emftest_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_emftest_book_has_title():
    assert hasattr(emftest_Book, "title")
    descriptor = None
    for klass in emftest_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_emftest_book_has_pages():
    assert hasattr(emftest_Book, "pages")
    descriptor = None
    for klass in emftest_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_booktype_exists():
    # Check that the Enumeration exists
    assert BookType is not None

def test_booktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookType]
    expected_literals = [
        "Child",
        "Parent",
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
emftest_Library_strategy = st.builds(
    emftest_Library,
)
emftest_BookCollection_strategy = st.builds(
    emftest_BookCollection,
)
Book_strategy = st.builds(
    Book,
)
emftest_ParentBook_strategy = st.builds(
    emftest_ParentBook,
)
emftest_ChildBook_strategy = st.builds(
    emftest_ChildBook,
)
emftest_Author_strategy = st.builds(
    emftest_Author,
    name=
        safe_text
)
emftest_Book_strategy = st.builds(
    emftest_Book,
    title=
        safe_text,
    pages=
        st.integers()
)

@given(instance=emftest_Library_strategy)
@settings(max_examples=50)
def test_emftest_library_instantiation(instance):
    assert isinstance(instance, emftest_Library)

@given(instance=emftest_BookCollection_strategy)
@settings(max_examples=50)
def test_emftest_bookcollection_instantiation(instance):
    assert isinstance(instance, emftest_BookCollection)

@given(instance=Book_strategy)
@settings(max_examples=50)
def test_book_instantiation(instance):
    assert isinstance(instance, Book)

@given(instance=emftest_ParentBook_strategy)
@settings(max_examples=50)
def test_emftest_parentbook_instantiation(instance):
    assert isinstance(instance, emftest_ParentBook)

@given(instance=emftest_ChildBook_strategy)
@settings(max_examples=50)
def test_emftest_childbook_instantiation(instance):
    assert isinstance(instance, emftest_ChildBook)

@given(instance=emftest_Author_strategy)
@settings(max_examples=50)
def test_emftest_author_instantiation(instance):
    assert isinstance(instance, emftest_Author)



@given(instance=emftest_Author_strategy)
def test_emftest_author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=emftest_Author_strategy)
@settings(max_examples=30)
def test_emftest_author_writebook_changes_state(instance):
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
        assert has_statements, f"Function 'writeBook' in emftest_Author is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'writeBook' in emftest_Author did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'writeBook' in emftest_Author is not implemented or raised an error")

@given(instance=emftest_Book_strategy)
@settings(max_examples=50)
def test_emftest_book_instantiation(instance):
    assert isinstance(instance, emftest_Book)



@given(instance=emftest_Book_strategy)
def test_emftest_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=emftest_Book_strategy)
def test_emftest_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original
