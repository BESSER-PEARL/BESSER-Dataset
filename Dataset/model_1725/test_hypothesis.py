import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mapkey::Writer,
    mapkey::StringToWriterMapEntry,
    mapkey::Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mapkey::writer_is_not_abstract():
    assert not inspect.isabstract(mapkey::Writer)


def test_mapkey::writer_constructor_exists():
    assert callable(mapkey::Writer.__init__)


def test_mapkey::writer_constructor_args():
    sig = inspect.signature(mapkey::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mapkey::writer_has_name():
    assert hasattr(mapkey::Writer, "name")
    descriptor = None
    for klass in mapkey::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mapkey::stringtowritermapentry_is_not_abstract():
    assert not inspect.isabstract(mapkey::StringToWriterMapEntry)


def test_mapkey::stringtowritermapentry_constructor_exists():
    assert callable(mapkey::StringToWriterMapEntry.__init__)


def test_mapkey::stringtowritermapentry_constructor_args():
    sig = inspect.signature(mapkey::StringToWriterMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_mapkey::stringtowritermapentry_has_key():
    assert hasattr(mapkey::StringToWriterMapEntry, "key")
    descriptor = None
    for klass in mapkey::StringToWriterMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_mapkey::book_is_not_abstract():
    assert not inspect.isabstract(mapkey::Book)


def test_mapkey::book_constructor_exists():
    assert callable(mapkey::Book.__init__)


def test_mapkey::book_constructor_args():
    sig = inspect.signature(mapkey::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_mapkey::book_has_title():
    assert hasattr(mapkey::Book, "title")
    descriptor = None
    for klass in mapkey::Book.__mro__:
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
mapkey::Writer_strategy = st.builds(
    mapkey::Writer,
    name=
        safe_text
)
mapkey::StringToWriterMapEntry_strategy = st.builds(
    mapkey::StringToWriterMapEntry,
    key=
        safe_text
)
mapkey::Book_strategy = st.builds(
    mapkey::Book,
    title=
        safe_text
)

@given(instance=mapkey::Writer_strategy)
@settings(max_examples=50)
def test_mapkey::writer_instantiation(instance):
    assert isinstance(instance, mapkey::Writer)

@given(instance=mapkey::Writer_strategy)
def test_mapkey::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mapkey::Writer_strategy)
def test_mapkey::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mapkey::StringToWriterMapEntry_strategy)
@settings(max_examples=50)
def test_mapkey::stringtowritermapentry_instantiation(instance):
    assert isinstance(instance, mapkey::StringToWriterMapEntry)

@given(instance=mapkey::StringToWriterMapEntry_strategy)
def test_mapkey::stringtowritermapentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=mapkey::StringToWriterMapEntry_strategy)
def test_mapkey::stringtowritermapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=mapkey::Book_strategy)
@settings(max_examples=50)
def test_mapkey::book_instantiation(instance):
    assert isinstance(instance, mapkey::Book)

@given(instance=mapkey::Book_strategy)
def test_mapkey::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=mapkey::Book_strategy)
def test_mapkey::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
