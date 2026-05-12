import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mapkey_Writer,
    mapkey_StringToWriterMapEntry,
    mapkey_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mapkey_writer_is_not_abstract():
    assert not inspect.isabstract(mapkey_Writer)


def test_mapkey_writer_constructor_exists():
    assert callable(mapkey_Writer.__init__)


def test_mapkey_writer_constructor_args():
    sig = inspect.signature(mapkey_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mapkey_writer_has_name():
    assert hasattr(mapkey_Writer, "name")
    descriptor = None
    for klass in mapkey_Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mapkey_stringtowritermapentry_is_not_abstract():
    assert not inspect.isabstract(mapkey_StringToWriterMapEntry)


def test_mapkey_stringtowritermapentry_constructor_exists():
    assert callable(mapkey_StringToWriterMapEntry.__init__)


def test_mapkey_stringtowritermapentry_constructor_args():
    sig = inspect.signature(mapkey_StringToWriterMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_mapkey_stringtowritermapentry_has_key():
    assert hasattr(mapkey_StringToWriterMapEntry, "key")
    descriptor = None
    for klass in mapkey_StringToWriterMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_mapkey_book_is_not_abstract():
    assert not inspect.isabstract(mapkey_Book)


def test_mapkey_book_constructor_exists():
    assert callable(mapkey_Book.__init__)


def test_mapkey_book_constructor_args():
    sig = inspect.signature(mapkey_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_mapkey_book_has_title():
    assert hasattr(mapkey_Book, "title")
    descriptor = None
    for klass in mapkey_Book.__mro__:
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
mapkey_Writer_strategy = st.builds(
    mapkey_Writer,
    name=
        safe_text
)
mapkey_StringToWriterMapEntry_strategy = st.builds(
    mapkey_StringToWriterMapEntry,
    key=
        safe_text
)
mapkey_Book_strategy = st.builds(
    mapkey_Book,
    title=
        safe_text
)

@given(instance=mapkey_Writer_strategy)
@settings(max_examples=50)
def test_mapkey_writer_instantiation(instance):
    assert isinstance(instance, mapkey_Writer)



@given(instance=mapkey_Writer_strategy)
def test_mapkey_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mapkey_StringToWriterMapEntry_strategy)
@settings(max_examples=50)
def test_mapkey_stringtowritermapentry_instantiation(instance):
    assert isinstance(instance, mapkey_StringToWriterMapEntry)



@given(instance=mapkey_StringToWriterMapEntry_strategy)
def test_mapkey_stringtowritermapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=mapkey_Book_strategy)
@settings(max_examples=50)
def test_mapkey_book_instantiation(instance):
    assert isinstance(instance, mapkey_Book)



@given(instance=mapkey_Book_strategy)
def test_mapkey_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
