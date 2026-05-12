import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    samples_Book,
    samples_Author,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_samples_book_is_not_abstract():
    assert not inspect.isabstract(samples_Book)


def test_samples_book_constructor_exists():
    assert callable(samples_Book.__init__)


def test_samples_book_constructor_args():
    sig = inspect.signature(samples_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_samples_book_has_title():
    assert hasattr(samples_Book, "title")
    descriptor = None
    for klass in samples_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_samples_author_is_not_abstract():
    assert not inspect.isabstract(samples_Author)


def test_samples_author_constructor_exists():
    assert callable(samples_Author.__init__)


def test_samples_author_constructor_args():
    sig = inspect.signature(samples_Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_samples_author_has_name():
    assert hasattr(samples_Author, "name")
    descriptor = None
    for klass in samples_Author.__mro__:
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
samples_Book_strategy = st.builds(
    samples_Book,
    title=
        safe_text
)
samples_Author_strategy = st.builds(
    samples_Author,
    name=
        safe_text
)

@given(instance=samples_Book_strategy)
@settings(max_examples=50)
def test_samples_book_instantiation(instance):
    assert isinstance(instance, samples_Book)



@given(instance=samples_Book_strategy)
def test_samples_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=samples_Author_strategy)
@settings(max_examples=50)
def test_samples_author_instantiation(instance):
    assert isinstance(instance, samples_Author)



@given(instance=samples_Author_strategy)
def test_samples_author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
