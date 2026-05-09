import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    entity::Writer,
    entity::Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entity::writer_is_not_abstract():
    assert not inspect.isabstract(entity::Writer)


def test_entity::writer_constructor_exists():
    assert callable(entity::Writer.__init__)


def test_entity::writer_constructor_args():
    sig = inspect.signature(entity::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entity::writer_has_name():
    assert hasattr(entity::Writer, "name")
    descriptor = None
    for klass in entity::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entity::book_is_not_abstract():
    assert not inspect.isabstract(entity::Book)


def test_entity::book_constructor_exists():
    assert callable(entity::Book.__init__)


def test_entity::book_constructor_args():
    sig = inspect.signature(entity::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_entity::book_has_title():
    assert hasattr(entity::Book, "title")
    descriptor = None
    for klass in entity::Book.__mro__:
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
entity::Writer_strategy = st.builds(
    entity::Writer,
    name=
        safe_text
)
entity::Book_strategy = st.builds(
    entity::Book,
    title=
        safe_text
)

@given(instance=entity::Writer_strategy)
@settings(max_examples=50)
def test_entity::writer_instantiation(instance):
    assert isinstance(instance, entity::Writer)

@given(instance=entity::Writer_strategy)
def test_entity::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entity::Writer_strategy)
def test_entity::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entity::Book_strategy)
@settings(max_examples=50)
def test_entity::book_instantiation(instance):
    assert isinstance(instance, entity::Book)

@given(instance=entity::Book_strategy)
def test_entity::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=entity::Book_strategy)
def test_entity::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
