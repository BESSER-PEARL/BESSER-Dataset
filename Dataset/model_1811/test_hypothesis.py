import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    extlibrary_Borrower,
    extlibrary_Borrowable,
    extlibrary_Book,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_extlibrary_borrower_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Borrower)


def test_extlibrary_borrower_constructor_exists():
    assert callable(extlibrary_Borrower.__init__)


def test_extlibrary_borrower_constructor_args():
    sig = inspect.signature(extlibrary_Borrower.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary_borrowable_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Borrowable)


def test_extlibrary_borrowable_constructor_exists():
    assert callable(extlibrary_Borrowable.__init__)


def test_extlibrary_borrowable_constructor_args():
    sig = inspect.signature(extlibrary_Borrowable.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary_book_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Book)


def test_extlibrary_book_constructor_exists():
    assert callable(extlibrary_Book.__init__)


def test_extlibrary_book_constructor_args():
    sig = inspect.signature(extlibrary_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_extlibrary_book_has_title():
    assert hasattr(extlibrary_Book, "title")
    descriptor = None
    for klass in extlibrary_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "Encyclopedia",
        "Dictionary",
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
extlibrary_Borrower_strategy = st.builds(
    extlibrary_Borrower,
)
extlibrary_Borrowable_strategy = st.builds(
    extlibrary_Borrowable,
)
extlibrary_Book_strategy = st.builds(
    extlibrary_Book,
    title=
        safe_text
)

@given(instance=extlibrary_Borrower_strategy)
@settings(max_examples=50)
def test_extlibrary_borrower_instantiation(instance):
    assert isinstance(instance, extlibrary_Borrower)

@given(instance=extlibrary_Borrowable_strategy)
@settings(max_examples=50)
def test_extlibrary_borrowable_instantiation(instance):
    assert isinstance(instance, extlibrary_Borrowable)

@given(instance=extlibrary_Book_strategy)
@settings(max_examples=50)
def test_extlibrary_book_instantiation(instance):
    assert isinstance(instance, extlibrary_Book)



@given(instance=extlibrary_Book_strategy)
def test_extlibrary_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
