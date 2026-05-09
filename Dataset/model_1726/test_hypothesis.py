import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    emap::Writer,
    emap::DateToCategoryMapEntry,
    emap::WriterToStringMapEntry,
    emap::StringToStringMapEntry,
    emap::StringToWriterMapEntry,
    emap::Book,
    Category,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_emap::writer_is_not_abstract():
    assert not inspect.isabstract(emap::Writer)


def test_emap::writer_constructor_exists():
    assert callable(emap::Writer.__init__)


def test_emap::writer_constructor_args():
    sig = inspect.signature(emap::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emap::writer_has_name():
    assert hasattr(emap::Writer, "name")
    descriptor = None
    for klass in emap::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emap::datetocategorymapentry_is_not_abstract():
    assert not inspect.isabstract(emap::DateToCategoryMapEntry)


def test_emap::datetocategorymapentry_constructor_exists():
    assert callable(emap::DateToCategoryMapEntry.__init__)


def test_emap::datetocategorymapentry_constructor_args():
    sig = inspect.signature(emap::DateToCategoryMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_emap::datetocategorymapentry_has_value():
    assert hasattr(emap::DateToCategoryMapEntry, "value")
    descriptor = None
    for klass in emap::DateToCategoryMapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_emap::datetocategorymapentry_has_key():
    assert hasattr(emap::DateToCategoryMapEntry, "key")
    descriptor = None
    for klass in emap::DateToCategoryMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_emap::writertostringmapentry_is_not_abstract():
    assert not inspect.isabstract(emap::WriterToStringMapEntry)


def test_emap::writertostringmapentry_constructor_exists():
    assert callable(emap::WriterToStringMapEntry.__init__)


def test_emap::writertostringmapentry_constructor_args():
    sig = inspect.signature(emap::WriterToStringMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_emap::writertostringmapentry_has_value():
    assert hasattr(emap::WriterToStringMapEntry, "value")
    descriptor = None
    for klass in emap::WriterToStringMapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_emap::stringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(emap::StringToStringMapEntry)


def test_emap::stringtostringmapentry_constructor_exists():
    assert callable(emap::StringToStringMapEntry.__init__)


def test_emap::stringtostringmapentry_constructor_args():
    sig = inspect.signature(emap::StringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_emap::stringtostringmapentry_has_key():
    assert hasattr(emap::StringToStringMapEntry, "key")
    descriptor = None
    for klass in emap::StringToStringMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_emap::stringtostringmapentry_has_value():
    assert hasattr(emap::StringToStringMapEntry, "value")
    descriptor = None
    for klass in emap::StringToStringMapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_emap::stringtowritermapentry_is_not_abstract():
    assert not inspect.isabstract(emap::StringToWriterMapEntry)


def test_emap::stringtowritermapentry_constructor_exists():
    assert callable(emap::StringToWriterMapEntry.__init__)


def test_emap::stringtowritermapentry_constructor_args():
    sig = inspect.signature(emap::StringToWriterMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_emap::stringtowritermapentry_has_key():
    assert hasattr(emap::StringToWriterMapEntry, "key")
    descriptor = None
    for klass in emap::StringToWriterMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_emap::book_is_not_abstract():
    assert not inspect.isabstract(emap::Book)


def test_emap::book_constructor_exists():
    assert callable(emap::Book.__init__)


def test_emap::book_constructor_args():
    sig = inspect.signature(emap::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_emap::book_has_title():
    assert hasattr(emap::Book, "title")
    descriptor = None
    for klass in emap::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_category_exists():
    # Check that the Enumeration exists
    assert Category is not None

def test_category_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Category]
    expected_literals = [
        "Complex",
        "Simple",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Category"


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
emap::Writer_strategy = st.builds(
    emap::Writer,
    name=
        safe_text
)
emap::DateToCategoryMapEntry_strategy = st.builds(
    emap::DateToCategoryMapEntry,
    value=
        safe_text,
    key=
        safe_text
)
emap::WriterToStringMapEntry_strategy = st.builds(
    emap::WriterToStringMapEntry,
    value=
        safe_text
)
emap::StringToStringMapEntry_strategy = st.builds(
    emap::StringToStringMapEntry,
    key=
        safe_text,
    value=
        safe_text
)
emap::StringToWriterMapEntry_strategy = st.builds(
    emap::StringToWriterMapEntry,
    key=
        safe_text
)
emap::Book_strategy = st.builds(
    emap::Book,
    title=
        safe_text
)

@given(instance=emap::Writer_strategy)
@settings(max_examples=50)
def test_emap::writer_instantiation(instance):
    assert isinstance(instance, emap::Writer)

@given(instance=emap::Writer_strategy)
def test_emap::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emap::Writer_strategy)
def test_emap::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emap::DateToCategoryMapEntry_strategy)
@settings(max_examples=50)
def test_emap::datetocategorymapentry_instantiation(instance):
    assert isinstance(instance, emap::DateToCategoryMapEntry)

@given(instance=emap::DateToCategoryMapEntry_strategy)
def test_emap::datetocategorymapentry_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=emap::DateToCategoryMapEntry_strategy)
def test_emap::datetocategorymapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=emap::DateToCategoryMapEntry_strategy)
def test_emap::datetocategorymapentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=emap::DateToCategoryMapEntry_strategy)
def test_emap::datetocategorymapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=emap::WriterToStringMapEntry_strategy)
@settings(max_examples=50)
def test_emap::writertostringmapentry_instantiation(instance):
    assert isinstance(instance, emap::WriterToStringMapEntry)

@given(instance=emap::WriterToStringMapEntry_strategy)
def test_emap::writertostringmapentry_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=emap::WriterToStringMapEntry_strategy)
def test_emap::writertostringmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=emap::StringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_emap::stringtostringmapentry_instantiation(instance):
    assert isinstance(instance, emap::StringToStringMapEntry)

@given(instance=emap::StringToStringMapEntry_strategy)
def test_emap::stringtostringmapentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=emap::StringToStringMapEntry_strategy)
def test_emap::stringtostringmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=emap::StringToStringMapEntry_strategy)
def test_emap::stringtostringmapentry_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=emap::StringToStringMapEntry_strategy)
def test_emap::stringtostringmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=emap::StringToWriterMapEntry_strategy)
@settings(max_examples=50)
def test_emap::stringtowritermapentry_instantiation(instance):
    assert isinstance(instance, emap::StringToWriterMapEntry)

@given(instance=emap::StringToWriterMapEntry_strategy)
def test_emap::stringtowritermapentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=emap::StringToWriterMapEntry_strategy)
def test_emap::stringtowritermapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=emap::Book_strategy)
@settings(max_examples=50)
def test_emap::book_instantiation(instance):
    assert isinstance(instance, emap::Book)

@given(instance=emap::Book_strategy)
def test_emap::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=emap::Book_strategy)
def test_emap::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
