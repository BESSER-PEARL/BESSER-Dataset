import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    library::Model,
    library::Person,
    Person,
    library::Author,
    library::Book,
    library::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::model_is_not_abstract():
    assert not inspect.isabstract(library::Model)


def test_library::model_constructor_exists():
    assert callable(library::Model.__init__)


def test_library::model_constructor_args():
    sig = inspect.signature(library::Model.__init__)
    params = list(sig.parameters.keys())



def test_library::person_is_not_abstract():
    assert not inspect.isabstract(library::Person)


def test_library::person_constructor_exists():
    assert callable(library::Person.__init__)


def test_library::person_constructor_args():
    sig = inspect.signature(library::Person.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_library::author_is_not_abstract():
    assert not inspect.isabstract(library::Author)


def test_library::author_constructor_exists():
    assert callable(library::Author.__init__)


def test_library::author_constructor_args():
    sig = inspect.signature(library::Author.__init__)
    params = list(sig.parameters.keys())



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::Book)


def test_library::book_constructor_exists():
    assert callable(library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::Book.__init__)
    params = list(sig.parameters.keys())



def test_library::library_is_not_abstract():
    assert not inspect.isabstract(library::Library)


def test_library::library_constructor_exists():
    assert callable(library::Library.__init__)


def test_library::library_constructor_args():
    sig = inspect.signature(library::Library.__init__)
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
library::Model_strategy = st.builds(
    library::Model,
)
library::Person_strategy = st.builds(
    library::Person,
)
Person_strategy = st.builds(
    Person,
)
library::Author_strategy = st.builds(
    library::Author,
)
library::Book_strategy = st.builds(
    library::Book,
)
library::Library_strategy = st.builds(
    library::Library,
)

@given(instance=library::Model_strategy)
@settings(max_examples=50)
def test_library::model_instantiation(instance):
    assert isinstance(instance, library::Model)

@given(instance=library::Person_strategy)
@settings(max_examples=50)
def test_library::person_instantiation(instance):
    assert isinstance(instance, library::Person)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=library::Author_strategy)
@settings(max_examples=50)
def test_library::author_instantiation(instance):
    assert isinstance(instance, library::Author)

@given(instance=library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::Book)

@given(instance=library::Library_strategy)
@settings(max_examples=50)
def test_library::library_instantiation(instance):
    assert isinstance(instance, library::Library)
