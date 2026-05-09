import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Library::Book,
    Library::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(Library::Book)


def test_library::book_constructor_exists():
    assert callable(Library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(Library::Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::book_has_name():
    assert hasattr(Library::Book, "name")
    descriptor = None
    for klass in Library::Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library::library_is_not_abstract():
    assert not inspect.isabstract(Library::Library)


def test_library::library_constructor_exists():
    assert callable(Library::Library.__init__)


def test_library::library_constructor_args():
    sig = inspect.signature(Library::Library.__init__)
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
Library::Book_strategy = st.builds(
    Library::Book,
    name=
        safe_text
)
Library::Library_strategy = st.builds(
    Library::Library,
)

@given(instance=Library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, Library::Book)

@given(instance=Library::Book_strategy)
def test_library::book_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Library::Book_strategy)
def test_library::book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Library::Library_strategy)
@settings(max_examples=50)
def test_library::library_instantiation(instance):
    assert isinstance(instance, Library::Library)
