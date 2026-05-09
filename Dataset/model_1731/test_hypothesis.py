import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    resourceunload::Library,
    resourceunload::Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_resourceunload::library_is_not_abstract():
    assert not inspect.isabstract(resourceunload::Library)


def test_resourceunload::library_constructor_exists():
    assert callable(resourceunload::Library.__init__)


def test_resourceunload::library_constructor_args():
    sig = inspect.signature(resourceunload::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_resourceunload::library_has_name():
    assert hasattr(resourceunload::Library, "name")
    descriptor = None
    for klass in resourceunload::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_resourceunload::book_is_not_abstract():
    assert not inspect.isabstract(resourceunload::Book)


def test_resourceunload::book_constructor_exists():
    assert callable(resourceunload::Book.__init__)


def test_resourceunload::book_constructor_args():
    sig = inspect.signature(resourceunload::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_resourceunload::book_has_title():
    assert hasattr(resourceunload::Book, "title")
    descriptor = None
    for klass in resourceunload::Book.__mro__:
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
resourceunload::Library_strategy = st.builds(
    resourceunload::Library,
    name=
        safe_text
)
resourceunload::Book_strategy = st.builds(
    resourceunload::Book,
    title=
        safe_text
)

@given(instance=resourceunload::Library_strategy)
@settings(max_examples=50)
def test_resourceunload::library_instantiation(instance):
    assert isinstance(instance, resourceunload::Library)

@given(instance=resourceunload::Library_strategy)
def test_resourceunload::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=resourceunload::Library_strategy)
def test_resourceunload::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=resourceunload::Book_strategy)
@settings(max_examples=50)
def test_resourceunload::book_instantiation(instance):
    assert isinstance(instance, resourceunload::Book)

@given(instance=resourceunload::Book_strategy)
def test_resourceunload::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=resourceunload::Book_strategy)
def test_resourceunload::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
