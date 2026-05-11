import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Entry,
    document::FullEntry,
    document::Entry,
    document::Table,
    document::Section,
    document::Chapter,
    document::BasicEntry,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entry_is_not_abstract():
    assert not inspect.isabstract(Entry)


def test_entry_constructor_exists():
    assert callable(Entry.__init__)


def test_entry_constructor_args():
    sig = inspect.signature(Entry.__init__)
    params = list(sig.parameters.keys())



def test_document::fullentry_is_not_abstract():
    assert not inspect.isabstract(document::FullEntry)


def test_document::fullentry_constructor_exists():
    assert callable(document::FullEntry.__init__)


def test_document::fullentry_constructor_args():
    sig = inspect.signature(document::FullEntry.__init__)
    params = list(sig.parameters.keys())



def test_document::entry_is_not_abstract():
    assert not inspect.isabstract(document::Entry)


def test_document::entry_constructor_exists():
    assert callable(document::Entry.__init__)


def test_document::entry_constructor_args():
    sig = inspect.signature(document::Entry.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "isBold" in params, "Missing parameter 'isBold'"
    assert "isItalic" in params, "Missing parameter 'isItalic'"

def test_document::entry_has_text():
    assert hasattr(document::Entry, "text")
    descriptor = None
    for klass in document::Entry.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_document::entry_has_isBold():
    assert hasattr(document::Entry, "isBold")
    descriptor = None
    for klass in document::Entry.__mro__:
        if "isBold" in klass.__dict__:
            descriptor = klass.__dict__["isBold"]
            break
    assert isinstance(descriptor, property)

def test_document::entry_has_isItalic():
    assert hasattr(document::Entry, "isItalic")
    descriptor = None
    for klass in document::Entry.__mro__:
        if "isItalic" in klass.__dict__:
            descriptor = klass.__dict__["isItalic"]
            break
    assert isinstance(descriptor, property)



def test_document::table_is_not_abstract():
    assert not inspect.isabstract(document::Table)


def test_document::table_constructor_exists():
    assert callable(document::Table.__init__)


def test_document::table_constructor_args():
    sig = inspect.signature(document::Table.__init__)
    params = list(sig.parameters.keys())



def test_document::section_is_not_abstract():
    assert not inspect.isabstract(document::Section)


def test_document::section_constructor_exists():
    assert callable(document::Section.__init__)


def test_document::section_constructor_args():
    sig = inspect.signature(document::Section.__init__)
    params = list(sig.parameters.keys())



def test_document::chapter_is_not_abstract():
    assert not inspect.isabstract(document::Chapter)


def test_document::chapter_constructor_exists():
    assert callable(document::Chapter.__init__)


def test_document::chapter_constructor_args():
    sig = inspect.signature(document::Chapter.__init__)
    params = list(sig.parameters.keys())



def test_document::basicentry_is_not_abstract():
    assert not inspect.isabstract(document::BasicEntry)


def test_document::basicentry_constructor_exists():
    assert callable(document::BasicEntry.__init__)


def test_document::basicentry_constructor_args():
    sig = inspect.signature(document::BasicEntry.__init__)
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
Entry_strategy = st.builds(
    Entry,
)
document::FullEntry_strategy = st.builds(
    document::FullEntry,
)
document::Entry_strategy = st.builds(
    document::Entry,
    text=
        safe_text,
    isBold=
        st.booleans(),
    isItalic=
        st.booleans()
)
document::Table_strategy = st.builds(
    document::Table,
)
document::Section_strategy = st.builds(
    document::Section,
)
document::Chapter_strategy = st.builds(
    document::Chapter,
)
document::BasicEntry_strategy = st.builds(
    document::BasicEntry,
)

@given(instance=Entry_strategy)
@settings(max_examples=50)
def test_entry_instantiation(instance):
    assert isinstance(instance, Entry)

@given(instance=document::FullEntry_strategy)
@settings(max_examples=50)
def test_document::fullentry_instantiation(instance):
    assert isinstance(instance, document::FullEntry)

@given(instance=document::Entry_strategy)
@settings(max_examples=50)
def test_document::entry_instantiation(instance):
    assert isinstance(instance, document::Entry)

@given(instance=document::Entry_strategy)
def test_document::entry_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=document::Entry_strategy)
def test_document::entry_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=document::Entry_strategy)
def test_document::entry_isBold_type(instance):
    assert isinstance(instance.isBold, bool)


@given(instance=document::Entry_strategy)
def test_document::entry_isBold_setter(instance):
    original = instance.isBold
    instance.isBold = original
    assert instance.isBold == original

@given(instance=document::Entry_strategy)
def test_document::entry_isItalic_type(instance):
    assert isinstance(instance.isItalic, bool)


@given(instance=document::Entry_strategy)
def test_document::entry_isItalic_setter(instance):
    original = instance.isItalic
    instance.isItalic = original
    assert instance.isItalic == original

@given(instance=document::Table_strategy)
@settings(max_examples=50)
def test_document::table_instantiation(instance):
    assert isinstance(instance, document::Table)

@given(instance=document::Section_strategy)
@settings(max_examples=50)
def test_document::section_instantiation(instance):
    assert isinstance(instance, document::Section)

@given(instance=document::Chapter_strategy)
@settings(max_examples=50)
def test_document::chapter_instantiation(instance):
    assert isinstance(instance, document::Chapter)

@given(instance=document::BasicEntry_strategy)
@settings(max_examples=50)
def test_document::basicentry_instantiation(instance):
    assert isinstance(instance, document::BasicEntry)
