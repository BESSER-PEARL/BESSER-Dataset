import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    extlibrary::Borrower,
    extlibrary::Borrowable,
    extlibrary::Item,
    extlibrary::Book,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_extlibrary::borrower_is_not_abstract():
    assert not inspect.isabstract(extlibrary::Borrower)


def test_extlibrary::borrower_constructor_exists():
    assert callable(extlibrary::Borrower.__init__)


def test_extlibrary::borrower_constructor_args():
    sig = inspect.signature(extlibrary::Borrower.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary::borrowable_is_not_abstract():
    assert not inspect.isabstract(extlibrary::Borrowable)


def test_extlibrary::borrowable_constructor_exists():
    assert callable(extlibrary::Borrowable.__init__)


def test_extlibrary::borrowable_constructor_args():
    sig = inspect.signature(extlibrary::Borrowable.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary::item_is_not_abstract():
    assert not inspect.isabstract(extlibrary::Item)


def test_extlibrary::item_constructor_exists():
    assert callable(extlibrary::Item.__init__)


def test_extlibrary::item_constructor_args():
    sig = inspect.signature(extlibrary::Item.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary::book_is_not_abstract():
    assert not inspect.isabstract(extlibrary::Book)


def test_extlibrary::book_constructor_exists():
    assert callable(extlibrary::Book.__init__)


def test_extlibrary::book_constructor_args():
    sig = inspect.signature(extlibrary::Book.__init__)
    params = list(sig.parameters.keys())

def test_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
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
extlibrary::Borrower_strategy = st.builds(
    extlibrary::Borrower,
)
extlibrary::Borrowable_strategy = st.builds(
    extlibrary::Borrowable,
)
extlibrary::Item_strategy = st.builds(
    extlibrary::Item,
)
extlibrary::Book_strategy = st.builds(
    extlibrary::Book,
)

@given(instance=extlibrary::Borrower_strategy)
@settings(max_examples=50)
def test_extlibrary::borrower_instantiation(instance):
    assert isinstance(instance, extlibrary::Borrower)

@given(instance=extlibrary::Borrowable_strategy)
@settings(max_examples=50)
def test_extlibrary::borrowable_instantiation(instance):
    assert isinstance(instance, extlibrary::Borrowable)

@given(instance=extlibrary::Item_strategy)
@settings(max_examples=50)
def test_extlibrary::item_instantiation(instance):
    assert isinstance(instance, extlibrary::Item)

@given(instance=extlibrary::Book_strategy)
@settings(max_examples=50)
def test_extlibrary::book_instantiation(instance):
    assert isinstance(instance, extlibrary::Book)
