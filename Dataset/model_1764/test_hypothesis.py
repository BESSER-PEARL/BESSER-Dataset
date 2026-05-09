import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    writers::Book,
    writers::Writer,
    writers::Catalog,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_writers::book_is_not_abstract():
    assert not inspect.isabstract(writers::Book)


def test_writers::book_constructor_exists():
    assert callable(writers::Book.__init__)


def test_writers::book_constructor_args():
    sig = inspect.signature(writers::Book.__init__)
    params = list(sig.parameters.keys())



def test_writers::writer_is_not_abstract():
    assert not inspect.isabstract(writers::Writer)


def test_writers::writer_constructor_exists():
    assert callable(writers::Writer.__init__)


def test_writers::writer_constructor_args():
    sig = inspect.signature(writers::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_writers::writer_has_name():
    assert hasattr(writers::Writer, "name")
    descriptor = None
    for klass in writers::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_writers::catalog_is_not_abstract():
    assert not inspect.isabstract(writers::Catalog)


def test_writers::catalog_constructor_exists():
    assert callable(writers::Catalog.__init__)


def test_writers::catalog_constructor_args():
    sig = inspect.signature(writers::Catalog.__init__)
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
writers::Book_strategy = st.builds(
    writers::Book,
)
writers::Writer_strategy = st.builds(
    writers::Writer,
    name=
        safe_text
)
writers::Catalog_strategy = st.builds(
    writers::Catalog,
)

@given(instance=writers::Book_strategy)
@settings(max_examples=50)
def test_writers::book_instantiation(instance):
    assert isinstance(instance, writers::Book)

@given(instance=writers::Writer_strategy)
@settings(max_examples=50)
def test_writers::writer_instantiation(instance):
    assert isinstance(instance, writers::Writer)

@given(instance=writers::Writer_strategy)
def test_writers::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=writers::Writer_strategy)
def test_writers::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=writers::Catalog_strategy)
@settings(max_examples=50)
def test_writers::catalog_instantiation(instance):
    assert isinstance(instance, writers::Catalog)
