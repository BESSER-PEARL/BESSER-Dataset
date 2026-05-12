import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Library_Author,
    Library_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library_author_is_not_abstract():
    assert not inspect.isabstract(Library_Author)


def test_library_author_constructor_exists():
    assert callable(Library_Author.__init__)


def test_library_author_constructor_args():
    sig = inspect.signature(Library_Author.__init__)
    params = list(sig.parameters.keys())



def test_library_book_is_not_abstract():
    assert not inspect.isabstract(Library_Book)


def test_library_book_constructor_exists():
    assert callable(Library_Book.__init__)


def test_library_book_constructor_args():
    sig = inspect.signature(Library_Book.__init__)
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
Library_Author_strategy = st.builds(
    Library_Author,
)
Library_Book_strategy = st.builds(
    Library_Book,
)

@given(instance=Library_Author_strategy)
@settings(max_examples=50)
def test_library_author_instantiation(instance):
    assert isinstance(instance, Library_Author)

@given(instance=Library_Book_strategy)
@settings(max_examples=50)
def test_library_book_instantiation(instance):
    assert isinstance(instance, Library_Book)
