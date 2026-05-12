import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    imported_model_Book,
    imported_model_Library,
    E,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_imported_model_book_is_not_abstract():
    assert not inspect.isabstract(imported_model_Book)


def test_imported_model_book_constructor_exists():
    assert callable(imported_model_Book.__init__)


def test_imported_model_book_constructor_args():
    sig = inspect.signature(imported_model_Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"

def test_imported_model_book_has_pages():
    assert hasattr(imported_model_Book, "pages")
    descriptor = None
    for klass in imported_model_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_imported_model_library_is_not_abstract():
    assert not inspect.isabstract(imported_model_Library)


def test_imported_model_library_constructor_exists():
    assert callable(imported_model_Library.__init__)


def test_imported_model_library_constructor_args():
    sig = inspect.signature(imported_model_Library.__init__)
    params = list(sig.parameters.keys())

def test_e_exists():
    # Check that the Enumeration exists
    assert E is not None

def test_e_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in E]
    expected_literals = [
        "B",
        "C",
        "A",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in E"


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
imported_model_Book_strategy = st.builds(
    imported_model_Book,
    pages=
        st.integers()
)
imported_model_Library_strategy = st.builds(
    imported_model_Library,
)

@given(instance=imported_model_Book_strategy)
@settings(max_examples=50)
def test_imported_model_book_instantiation(instance):
    assert isinstance(instance, imported_model_Book)



@given(instance=imported_model_Book_strategy)
def test_imported_model_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=imported_model_Library_strategy)
@settings(max_examples=50)
def test_imported_model_library_instantiation(instance):
    assert isinstance(instance, imported_model_Library)
