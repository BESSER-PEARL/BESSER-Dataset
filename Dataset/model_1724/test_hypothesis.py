import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    hbmapkeys::City,
    hbmapkeys::WriterToCityMapEntry,
    hbmapkeys::StringToWriterMapEntry,
    hbmapkeys::Book,
    hbmapkeys::Writer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hbmapkeys::city_is_not_abstract():
    assert not inspect.isabstract(hbmapkeys::City)


def test_hbmapkeys::city_constructor_exists():
    assert callable(hbmapkeys::City.__init__)


def test_hbmapkeys::city_constructor_args():
    sig = inspect.signature(hbmapkeys::City.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hbmapkeys::city_has_name():
    assert hasattr(hbmapkeys::City, "name")
    descriptor = None
    for klass in hbmapkeys::City.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hbmapkeys::writertocitymapentry_is_not_abstract():
    assert not inspect.isabstract(hbmapkeys::WriterToCityMapEntry)


def test_hbmapkeys::writertocitymapentry_constructor_exists():
    assert callable(hbmapkeys::WriterToCityMapEntry.__init__)


def test_hbmapkeys::writertocitymapentry_constructor_args():
    sig = inspect.signature(hbmapkeys::WriterToCityMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_hbmapkeys::stringtowritermapentry_is_not_abstract():
    assert not inspect.isabstract(hbmapkeys::StringToWriterMapEntry)


def test_hbmapkeys::stringtowritermapentry_constructor_exists():
    assert callable(hbmapkeys::StringToWriterMapEntry.__init__)


def test_hbmapkeys::stringtowritermapentry_constructor_args():
    sig = inspect.signature(hbmapkeys::StringToWriterMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_hbmapkeys::stringtowritermapentry_has_key():
    assert hasattr(hbmapkeys::StringToWriterMapEntry, "key")
    descriptor = None
    for klass in hbmapkeys::StringToWriterMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_hbmapkeys::book_is_not_abstract():
    assert not inspect.isabstract(hbmapkeys::Book)


def test_hbmapkeys::book_constructor_exists():
    assert callable(hbmapkeys::Book.__init__)


def test_hbmapkeys::book_constructor_args():
    sig = inspect.signature(hbmapkeys::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_hbmapkeys::book_has_title():
    assert hasattr(hbmapkeys::Book, "title")
    descriptor = None
    for klass in hbmapkeys::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_hbmapkeys::writer_is_not_abstract():
    assert not inspect.isabstract(hbmapkeys::Writer)


def test_hbmapkeys::writer_constructor_exists():
    assert callable(hbmapkeys::Writer.__init__)


def test_hbmapkeys::writer_constructor_args():
    sig = inspect.signature(hbmapkeys::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hbmapkeys::writer_has_name():
    assert hasattr(hbmapkeys::Writer, "name")
    descriptor = None
    for klass in hbmapkeys::Writer.__mro__:
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
hbmapkeys::City_strategy = st.builds(
    hbmapkeys::City,
    name=
        safe_text
)
hbmapkeys::WriterToCityMapEntry_strategy = st.builds(
    hbmapkeys::WriterToCityMapEntry,
)
hbmapkeys::StringToWriterMapEntry_strategy = st.builds(
    hbmapkeys::StringToWriterMapEntry,
    key=
        safe_text
)
hbmapkeys::Book_strategy = st.builds(
    hbmapkeys::Book,
    title=
        safe_text
)
hbmapkeys::Writer_strategy = st.builds(
    hbmapkeys::Writer,
    name=
        safe_text
)

@given(instance=hbmapkeys::City_strategy)
@settings(max_examples=50)
def test_hbmapkeys::city_instantiation(instance):
    assert isinstance(instance, hbmapkeys::City)

@given(instance=hbmapkeys::City_strategy)
def test_hbmapkeys::city_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=hbmapkeys::City_strategy)
def test_hbmapkeys::city_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hbmapkeys::WriterToCityMapEntry_strategy)
@settings(max_examples=50)
def test_hbmapkeys::writertocitymapentry_instantiation(instance):
    assert isinstance(instance, hbmapkeys::WriterToCityMapEntry)

@given(instance=hbmapkeys::StringToWriterMapEntry_strategy)
@settings(max_examples=50)
def test_hbmapkeys::stringtowritermapentry_instantiation(instance):
    assert isinstance(instance, hbmapkeys::StringToWriterMapEntry)

@given(instance=hbmapkeys::StringToWriterMapEntry_strategy)
def test_hbmapkeys::stringtowritermapentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=hbmapkeys::StringToWriterMapEntry_strategy)
def test_hbmapkeys::stringtowritermapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=hbmapkeys::Book_strategy)
@settings(max_examples=50)
def test_hbmapkeys::book_instantiation(instance):
    assert isinstance(instance, hbmapkeys::Book)

@given(instance=hbmapkeys::Book_strategy)
def test_hbmapkeys::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=hbmapkeys::Book_strategy)
def test_hbmapkeys::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=hbmapkeys::Writer_strategy)
@settings(max_examples=50)
def test_hbmapkeys::writer_instantiation(instance):
    assert isinstance(instance, hbmapkeys::Writer)

@given(instance=hbmapkeys::Writer_strategy)
def test_hbmapkeys::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=hbmapkeys::Writer_strategy)
def test_hbmapkeys::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
