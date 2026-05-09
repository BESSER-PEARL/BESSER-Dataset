import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    extlibrary::Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_extlibrary::book_is_not_abstract():
    assert not inspect.isabstract(extlibrary::Book)


def test_extlibrary::book_constructor_exists():
    assert callable(extlibrary::Book.__init__)


def test_extlibrary::book_constructor_args():
    sig = inspect.signature(extlibrary::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_extlibrary::book_has_title():
    assert hasattr(extlibrary::Book, "title")
    descriptor = None
    for klass in extlibrary::Book.__mro__:
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
extlibrary::Book_strategy = st.builds(
    extlibrary::Book,
    title=
        safe_text
)

@given(instance=extlibrary::Book_strategy)
@settings(max_examples=50)
def test_extlibrary::book_instantiation(instance):
    assert isinstance(instance, extlibrary::Book)

@given(instance=extlibrary::Book_strategy)
def test_extlibrary::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=extlibrary::Book_strategy)
def test_extlibrary::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
