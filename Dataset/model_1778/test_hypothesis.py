import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    samples::Book,
    samples::Author,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_samples::book_is_not_abstract():
    assert not inspect.isabstract(samples::Book)


def test_samples::book_constructor_exists():
    assert callable(samples::Book.__init__)


def test_samples::book_constructor_args():
    sig = inspect.signature(samples::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_samples::book_has_title():
    assert hasattr(samples::Book, "title")
    descriptor = None
    for klass in samples::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_samples::author_is_not_abstract():
    assert not inspect.isabstract(samples::Author)


def test_samples::author_constructor_exists():
    assert callable(samples::Author.__init__)


def test_samples::author_constructor_args():
    sig = inspect.signature(samples::Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_samples::author_has_name():
    assert hasattr(samples::Author, "name")
    descriptor = None
    for klass in samples::Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
samples::Book_strategy = st.builds(
    samples::Book,
    title=
        safe_text
)
samples::Author_strategy = st.builds(
    samples::Author,
    name=
        safe_text
)

@given(instance=samples::Book_strategy)
@settings(max_examples=50)
def test_samples::book_instantiation(instance):
    assert isinstance(instance, samples::Book)

@given(instance=samples::Book_strategy)
def test_samples::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=samples::Book_strategy)
def test_samples::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=samples::Author_strategy)
@settings(max_examples=50)
def test_samples::author_instantiation(instance):
    assert isinstance(instance, samples::Author)

@given(instance=samples::Author_strategy)
def test_samples::author_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=samples::Author_strategy)
def test_samples::author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
