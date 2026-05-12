import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Library_Writer,
    Library_Library,
    Library_Book,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library_writer_is_not_abstract():
    assert not inspect.isabstract(Library_Writer)


def test_library_writer_constructor_exists():
    assert callable(Library_Writer.__init__)


def test_library_writer_constructor_args():
    sig = inspect.signature(Library_Writer.__init__)
    params = list(sig.parameters.keys())



def test_library_library_is_not_abstract():
    assert not inspect.isabstract(Library_Library)


def test_library_library_constructor_exists():
    assert callable(Library_Library.__init__)


def test_library_library_constructor_args():
    sig = inspect.signature(Library_Library.__init__)
    params = list(sig.parameters.keys())



def test_library_book_is_not_abstract():
    assert not inspect.isabstract(Library_Book)


def test_library_book_constructor_exists():
    assert callable(Library_Book.__init__)


def test_library_book_constructor_args():
    sig = inspect.signature(Library_Book.__init__)
    params = list(sig.parameters.keys())

def test_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "SCIENCE_FICTION",
        "BIOGRAPHY",
        "MYSTERY",
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
Library_Writer_strategy = st.builds(
    Library_Writer,
)
Library_Library_strategy = st.builds(
    Library_Library,
)
Library_Book_strategy = st.builds(
    Library_Book,
)

@given(instance=Library_Writer_strategy)
@settings(max_examples=50)
def test_library_writer_instantiation(instance):
    assert isinstance(instance, Library_Writer)

@given(instance=Library_Library_strategy)
@settings(max_examples=50)
def test_library_library_instantiation(instance):
    assert isinstance(instance, Library_Library)

@given(instance=Library_Book_strategy)
@settings(max_examples=50)
def test_library_book_instantiation(instance):
    assert isinstance(instance, Library_Book)
