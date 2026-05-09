import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Library::Author,
    Library::Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::author_is_not_abstract():
    assert not inspect.isabstract(Library::Author)


def test_library::author_constructor_exists():
    assert callable(Library::Author.__init__)


def test_library::author_constructor_args():
    sig = inspect.signature(Library::Author.__init__)
    params = list(sig.parameters.keys())



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(Library::Book)


def test_library::book_constructor_exists():
    assert callable(Library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(Library::Book.__init__)
    params = list(sig.parameters.keys())


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
Library::Author_strategy = st.builds(
    Library::Author,
)
Library::Book_strategy = st.builds(
    Library::Book,
)

@given(instance=Library::Author_strategy)
@settings(max_examples=50)
def test_library::author_instantiation(instance):
    assert isinstance(instance, Library::Author)

@given(instance=Library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, Library::Book)
