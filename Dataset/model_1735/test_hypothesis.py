import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    library_Model,
    library_Person,
    Person,
    library_Author,
    library_Book,
    library_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library_model_is_not_abstract():
    assert not inspect.isabstract(library_Model)


def test_library_model_constructor_exists():
    assert callable(library_Model.__init__)


def test_library_model_constructor_args():
    sig = inspect.signature(library_Model.__init__)
    params = list(sig.parameters.keys())



def test_library_person_is_not_abstract():
    assert not inspect.isabstract(library_Person)


def test_library_person_constructor_exists():
    assert callable(library_Person.__init__)


def test_library_person_constructor_args():
    sig = inspect.signature(library_Person.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_library_author_is_not_abstract():
    assert not inspect.isabstract(library_Author)


def test_library_author_constructor_exists():
    assert callable(library_Author.__init__)


def test_library_author_constructor_args():
    sig = inspect.signature(library_Author.__init__)
    params = list(sig.parameters.keys())



def test_library_book_is_not_abstract():
    assert not inspect.isabstract(library_Book)


def test_library_book_constructor_exists():
    assert callable(library_Book.__init__)


def test_library_book_constructor_args():
    sig = inspect.signature(library_Book.__init__)
    params = list(sig.parameters.keys())



def test_library_library_is_not_abstract():
    assert not inspect.isabstract(library_Library)


def test_library_library_constructor_exists():
    assert callable(library_Library.__init__)


def test_library_library_constructor_args():
    sig = inspect.signature(library_Library.__init__)
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
library_Model_strategy = st.builds(
    library_Model,
)
library_Person_strategy = st.builds(
    library_Person,
)
Person_strategy = st.builds(
    Person,
)
library_Author_strategy = st.builds(
    library_Author,
)
library_Book_strategy = st.builds(
    library_Book,
)
library_Library_strategy = st.builds(
    library_Library,
)

@given(instance=library_Model_strategy)
@settings(max_examples=50)
def test_library_model_instantiation(instance):
    assert isinstance(instance, library_Model)

@given(instance=library_Person_strategy)
@settings(max_examples=50)
def test_library_person_instantiation(instance):
    assert isinstance(instance, library_Person)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=library_Author_strategy)
@settings(max_examples=50)
def test_library_author_instantiation(instance):
    assert isinstance(instance, library_Author)

@given(instance=library_Book_strategy)
@settings(max_examples=50)
def test_library_book_instantiation(instance):
    assert isinstance(instance, library_Book)

@given(instance=library_Library_strategy)
@settings(max_examples=50)
def test_library_library_instantiation(instance):
    assert isinstance(instance, library_Library)
