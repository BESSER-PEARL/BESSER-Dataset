import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    emap_Writer,
    emap_StringToStringMapEntry,
    emap_DateToCategoryMapEntry,
    emap_WriterToStringMapEntry,
    emap_StringToWriterMapEntry,
    emap_Book,
    Category,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_emap_writer_is_not_abstract():
    assert not inspect.isabstract(emap_Writer)


def test_emap_writer_constructor_exists():
    assert callable(emap_Writer.__init__)


def test_emap_writer_constructor_args():
    sig = inspect.signature(emap_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emap_writer_has_name():
    assert hasattr(emap_Writer, "name")
    descriptor = None
    for klass in emap_Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emap_stringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(emap_StringToStringMapEntry)


def test_emap_stringtostringmapentry_constructor_exists():
    assert callable(emap_StringToStringMapEntry.__init__)


def test_emap_stringtostringmapentry_constructor_args():
    sig = inspect.signature(emap_StringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_emap_stringtostringmapentry_has_value():
    assert hasattr(emap_StringToStringMapEntry, "value")
    descriptor = None
    for klass in emap_StringToStringMapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_emap_stringtostringmapentry_has_key():
    assert hasattr(emap_StringToStringMapEntry, "key")
    descriptor = None
    for klass in emap_StringToStringMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_emap_datetocategorymapentry_is_not_abstract():
    assert not inspect.isabstract(emap_DateToCategoryMapEntry)


def test_emap_datetocategorymapentry_constructor_exists():
    assert callable(emap_DateToCategoryMapEntry.__init__)


def test_emap_datetocategorymapentry_constructor_args():
    sig = inspect.signature(emap_DateToCategoryMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_emap_datetocategorymapentry_has_value():
    assert hasattr(emap_DateToCategoryMapEntry, "value")
    descriptor = None
    for klass in emap_DateToCategoryMapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_emap_datetocategorymapentry_has_key():
    assert hasattr(emap_DateToCategoryMapEntry, "key")
    descriptor = None
    for klass in emap_DateToCategoryMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_emap_writertostringmapentry_is_not_abstract():
    assert not inspect.isabstract(emap_WriterToStringMapEntry)


def test_emap_writertostringmapentry_constructor_exists():
    assert callable(emap_WriterToStringMapEntry.__init__)


def test_emap_writertostringmapentry_constructor_args():
    sig = inspect.signature(emap_WriterToStringMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_emap_writertostringmapentry_has_value():
    assert hasattr(emap_WriterToStringMapEntry, "value")
    descriptor = None
    for klass in emap_WriterToStringMapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_emap_stringtowritermapentry_is_not_abstract():
    assert not inspect.isabstract(emap_StringToWriterMapEntry)


def test_emap_stringtowritermapentry_constructor_exists():
    assert callable(emap_StringToWriterMapEntry.__init__)


def test_emap_stringtowritermapentry_constructor_args():
    sig = inspect.signature(emap_StringToWriterMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_emap_stringtowritermapentry_has_key():
    assert hasattr(emap_StringToWriterMapEntry, "key")
    descriptor = None
    for klass in emap_StringToWriterMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_emap_book_is_not_abstract():
    assert not inspect.isabstract(emap_Book)


def test_emap_book_constructor_exists():
    assert callable(emap_Book.__init__)


def test_emap_book_constructor_args():
    sig = inspect.signature(emap_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_emap_book_has_title():
    assert hasattr(emap_Book, "title")
    descriptor = None
    for klass in emap_Book.__mro__:
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
        "Simple",
        "Complex",
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
emap_Writer_strategy = st.builds(
    emap_Writer,
    name=
        safe_text
)
emap_StringToStringMapEntry_strategy = st.builds(
    emap_StringToStringMapEntry,
    value=
        safe_text,
    key=
        safe_text
)
emap_DateToCategoryMapEntry_strategy = st.builds(
    emap_DateToCategoryMapEntry,
    value=
        safe_text,
    key=
        safe_text
)
emap_WriterToStringMapEntry_strategy = st.builds(
    emap_WriterToStringMapEntry,
    value=
        safe_text
)
emap_StringToWriterMapEntry_strategy = st.builds(
    emap_StringToWriterMapEntry,
    key=
        safe_text
)
emap_Book_strategy = st.builds(
    emap_Book,
    title=
        safe_text
)

@given(instance=emap_Writer_strategy)
@settings(max_examples=50)
def test_emap_writer_instantiation(instance):
    assert isinstance(instance, emap_Writer)



@given(instance=emap_Writer_strategy)
def test_emap_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emap_StringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_emap_stringtostringmapentry_instantiation(instance):
    assert isinstance(instance, emap_StringToStringMapEntry)



@given(instance=emap_StringToStringMapEntry_strategy)
def test_emap_stringtostringmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=emap_StringToStringMapEntry_strategy)
def test_emap_stringtostringmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=emap_DateToCategoryMapEntry_strategy)
@settings(max_examples=50)
def test_emap_datetocategorymapentry_instantiation(instance):
    assert isinstance(instance, emap_DateToCategoryMapEntry)



@given(instance=emap_DateToCategoryMapEntry_strategy)
def test_emap_datetocategorymapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=emap_DateToCategoryMapEntry_strategy)
def test_emap_datetocategorymapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=emap_WriterToStringMapEntry_strategy)
@settings(max_examples=50)
def test_emap_writertostringmapentry_instantiation(instance):
    assert isinstance(instance, emap_WriterToStringMapEntry)



@given(instance=emap_WriterToStringMapEntry_strategy)
def test_emap_writertostringmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=emap_StringToWriterMapEntry_strategy)
@settings(max_examples=50)
def test_emap_stringtowritermapentry_instantiation(instance):
    assert isinstance(instance, emap_StringToWriterMapEntry)



@given(instance=emap_StringToWriterMapEntry_strategy)
def test_emap_stringtowritermapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=emap_Book_strategy)
@settings(max_examples=50)
def test_emap_book_instantiation(instance):
    assert isinstance(instance, emap_Book)



@given(instance=emap_Book_strategy)
def test_emap_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
