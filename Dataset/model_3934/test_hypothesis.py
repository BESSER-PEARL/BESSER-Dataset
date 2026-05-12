import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Entry,
    document_BasicEntry,
    document_FullEntry,
    document_Entry,
    document_Table,
    document_Section,
    document_Chapter,
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



def test_document_basicentry_is_not_abstract():
    assert not inspect.isabstract(document_BasicEntry)


def test_document_basicentry_constructor_exists():
    assert callable(document_BasicEntry.__init__)


def test_document_basicentry_constructor_args():
    sig = inspect.signature(document_BasicEntry.__init__)
    params = list(sig.parameters.keys())



def test_document_fullentry_is_not_abstract():
    assert not inspect.isabstract(document_FullEntry)


def test_document_fullentry_constructor_exists():
    assert callable(document_FullEntry.__init__)


def test_document_fullentry_constructor_args():
    sig = inspect.signature(document_FullEntry.__init__)
    params = list(sig.parameters.keys())



def test_document_entry_is_not_abstract():
    assert not inspect.isabstract(document_Entry)


def test_document_entry_constructor_exists():
    assert callable(document_Entry.__init__)


def test_document_entry_constructor_args():
    sig = inspect.signature(document_Entry.__init__)
    params = list(sig.parameters.keys())
    assert "isItalic" in params, "Missing parameter 'isItalic'"
    assert "isBold" in params, "Missing parameter 'isBold'"
    assert "text" in params, "Missing parameter 'text'"

def test_document_entry_has_isItalic():
    assert hasattr(document_Entry, "isItalic")
    descriptor = None
    for klass in document_Entry.__mro__:
        if "isItalic" in klass.__dict__:
            descriptor = klass.__dict__["isItalic"]
            break
    assert isinstance(descriptor, property)

def test_document_entry_has_isBold():
    assert hasattr(document_Entry, "isBold")
    descriptor = None
    for klass in document_Entry.__mro__:
        if "isBold" in klass.__dict__:
            descriptor = klass.__dict__["isBold"]
            break
    assert isinstance(descriptor, property)

def test_document_entry_has_text():
    assert hasattr(document_Entry, "text")
    descriptor = None
    for klass in document_Entry.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_document_table_is_not_abstract():
    assert not inspect.isabstract(document_Table)


def test_document_table_constructor_exists():
    assert callable(document_Table.__init__)


def test_document_table_constructor_args():
    sig = inspect.signature(document_Table.__init__)
    params = list(sig.parameters.keys())



def test_document_section_is_not_abstract():
    assert not inspect.isabstract(document_Section)


def test_document_section_constructor_exists():
    assert callable(document_Section.__init__)


def test_document_section_constructor_args():
    sig = inspect.signature(document_Section.__init__)
    params = list(sig.parameters.keys())



def test_document_chapter_is_not_abstract():
    assert not inspect.isabstract(document_Chapter)


def test_document_chapter_constructor_exists():
    assert callable(document_Chapter.__init__)


def test_document_chapter_constructor_args():
    sig = inspect.signature(document_Chapter.__init__)
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
document_BasicEntry_strategy = st.builds(
    document_BasicEntry,
)
document_FullEntry_strategy = st.builds(
    document_FullEntry,
)
document_Entry_strategy = st.builds(
    document_Entry,
    isItalic=
        st.booleans(),
    isBold=
        st.booleans(),
    text=
        safe_text
)
document_Table_strategy = st.builds(
    document_Table,
)
document_Section_strategy = st.builds(
    document_Section,
)
document_Chapter_strategy = st.builds(
    document_Chapter,
)

@given(instance=Entry_strategy)
@settings(max_examples=50)
def test_entry_instantiation(instance):
    assert isinstance(instance, Entry)

@given(instance=document_BasicEntry_strategy)
@settings(max_examples=50)
def test_document_basicentry_instantiation(instance):
    assert isinstance(instance, document_BasicEntry)

@given(instance=document_FullEntry_strategy)
@settings(max_examples=50)
def test_document_fullentry_instantiation(instance):
    assert isinstance(instance, document_FullEntry)

@given(instance=document_Entry_strategy)
@settings(max_examples=50)
def test_document_entry_instantiation(instance):
    assert isinstance(instance, document_Entry)



@given(instance=document_Entry_strategy)
def test_document_entry_isItalic_setter(instance):
    original = instance.isItalic
    instance.isItalic = original
    assert instance.isItalic == original



@given(instance=document_Entry_strategy)
def test_document_entry_isBold_setter(instance):
    original = instance.isBold
    instance.isBold = original
    assert instance.isBold == original



@given(instance=document_Entry_strategy)
def test_document_entry_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=document_Table_strategy)
@settings(max_examples=50)
def test_document_table_instantiation(instance):
    assert isinstance(instance, document_Table)

@given(instance=document_Section_strategy)
@settings(max_examples=50)
def test_document_section_instantiation(instance):
    assert isinstance(instance, document_Section)

@given(instance=document_Chapter_strategy)
@settings(max_examples=50)
def test_document_chapter_instantiation(instance):
    assert isinstance(instance, document_Chapter)
