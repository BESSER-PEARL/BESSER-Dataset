import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    extlibrary_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_extlibrary_book_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Book)


def test_extlibrary_book_constructor_exists():
    assert callable(extlibrary_Book.__init__)


def test_extlibrary_book_constructor_args():
    sig = inspect.signature(extlibrary_Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"

def test_extlibrary_book_has_pages():
    assert hasattr(extlibrary_Book, "pages")
    descriptor = None
    for klass in extlibrary_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_book_has_title():
    assert hasattr(extlibrary_Book, "title")
    descriptor = None
    for klass in extlibrary_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)


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
extlibrary_Book_strategy = st.builds(
    extlibrary_Book,
    pages=
        st.integers(),
    title=
        safe_text
)

@given(instance=extlibrary_Book_strategy)
@settings(max_examples=50)
def test_extlibrary_book_instantiation(instance):
    assert isinstance(instance, extlibrary_Book)



@given(instance=extlibrary_Book_strategy)
def test_extlibrary_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=extlibrary_Book_strategy)
def test_extlibrary_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
