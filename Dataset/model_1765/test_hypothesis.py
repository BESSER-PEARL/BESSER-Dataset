import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    writers_Catalog,
    writers_Book,
    writers_Writer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_writers_catalog_is_not_abstract():
    assert not inspect.isabstract(writers_Catalog)


def test_writers_catalog_constructor_exists():
    assert callable(writers_Catalog.__init__)


def test_writers_catalog_constructor_args():
    sig = inspect.signature(writers_Catalog.__init__)
    params = list(sig.parameters.keys())



def test_writers_book_is_not_abstract():
    assert not inspect.isabstract(writers_Book)


def test_writers_book_constructor_exists():
    assert callable(writers_Book.__init__)


def test_writers_book_constructor_args():
    sig = inspect.signature(writers_Book.__init__)
    params = list(sig.parameters.keys())



def test_writers_writer_is_not_abstract():
    assert not inspect.isabstract(writers_Writer)


def test_writers_writer_constructor_exists():
    assert callable(writers_Writer.__init__)


def test_writers_writer_constructor_args():
    sig = inspect.signature(writers_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_writers_writer_has_name():
    assert hasattr(writers_Writer, "name")
    descriptor = None
    for klass in writers_Writer.__mro__:
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
writers_Catalog_strategy = st.builds(
    writers_Catalog,
)
writers_Book_strategy = st.builds(
    writers_Book,
)
writers_Writer_strategy = st.builds(
    writers_Writer,
    name=
        safe_text
)

@given(instance=writers_Catalog_strategy)
@settings(max_examples=50)
def test_writers_catalog_instantiation(instance):
    assert isinstance(instance, writers_Catalog)

@given(instance=writers_Book_strategy)
@settings(max_examples=50)
def test_writers_book_instantiation(instance):
    assert isinstance(instance, writers_Book)

@given(instance=writers_Writer_strategy)
@settings(max_examples=50)
def test_writers_writer_instantiation(instance):
    assert isinstance(instance, writers_Writer)



@given(instance=writers_Writer_strategy)
def test_writers_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
