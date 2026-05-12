import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_Author,
    model_Book,
    model_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_author_is_not_abstract():
    assert not inspect.isabstract(model_Author)


def test_model_author_constructor_exists():
    assert callable(model_Author.__init__)


def test_model_author_constructor_args():
    sig = inspect.signature(model_Author.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_model_author_has_firstName():
    assert hasattr(model_Author, "firstName")
    descriptor = None
    for klass in model_Author.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_model_author_has_lastName():
    assert hasattr(model_Author, "lastName")
    descriptor = None
    for klass in model_Author.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_model_book_is_not_abstract():
    assert not inspect.isabstract(model_Book)


def test_model_book_constructor_exists():
    assert callable(model_Book.__init__)


def test_model_book_constructor_args():
    sig = inspect.signature(model_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_model_book_has_title():
    assert hasattr(model_Book, "title")
    descriptor = None
    for klass in model_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_model_library_is_not_abstract():
    assert not inspect.isabstract(model_Library)


def test_model_library_constructor_exists():
    assert callable(model_Library.__init__)


def test_model_library_constructor_args():
    sig = inspect.signature(model_Library.__init__)
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
model_Author_strategy = st.builds(
    model_Author,
    firstName=
        safe_text,
    lastName=
        safe_text
)
model_Book_strategy = st.builds(
    model_Book,
    title=
        safe_text
)
model_Library_strategy = st.builds(
    model_Library,
)

@given(instance=model_Author_strategy)
@settings(max_examples=50)
def test_model_author_instantiation(instance):
    assert isinstance(instance, model_Author)



@given(instance=model_Author_strategy)
def test_model_author_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=model_Author_strategy)
def test_model_author_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=model_Book_strategy)
@settings(max_examples=50)
def test_model_book_instantiation(instance):
    assert isinstance(instance, model_Book)



@given(instance=model_Book_strategy)
def test_model_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=model_Library_strategy)
@settings(max_examples=50)
def test_model_library_instantiation(instance):
    assert isinstance(instance, model_Library)
