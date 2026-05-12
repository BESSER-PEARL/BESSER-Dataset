import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    entity_Writer,
    entity_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entity_writer_is_not_abstract():
    assert not inspect.isabstract(entity_Writer)


def test_entity_writer_constructor_exists():
    assert callable(entity_Writer.__init__)


def test_entity_writer_constructor_args():
    sig = inspect.signature(entity_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entity_writer_has_name():
    assert hasattr(entity_Writer, "name")
    descriptor = None
    for klass in entity_Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entity_book_is_not_abstract():
    assert not inspect.isabstract(entity_Book)


def test_entity_book_constructor_exists():
    assert callable(entity_Book.__init__)


def test_entity_book_constructor_args():
    sig = inspect.signature(entity_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_entity_book_has_title():
    assert hasattr(entity_Book, "title")
    descriptor = None
    for klass in entity_Book.__mro__:
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
entity_Writer_strategy = st.builds(
    entity_Writer,
    name=
        safe_text
)
entity_Book_strategy = st.builds(
    entity_Book,
    title=
        safe_text
)

@given(instance=entity_Writer_strategy)
@settings(max_examples=50)
def test_entity_writer_instantiation(instance):
    assert isinstance(instance, entity_Writer)



@given(instance=entity_Writer_strategy)
def test_entity_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entity_Book_strategy)
@settings(max_examples=50)
def test_entity_book_instantiation(instance):
    assert isinstance(instance, entity_Book)



@given(instance=entity_Book_strategy)
def test_entity_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
