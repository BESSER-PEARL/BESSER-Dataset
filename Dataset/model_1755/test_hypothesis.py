import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    extralazy_Book,
    extralazy_Writer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_extralazy_book_is_not_abstract():
    assert not inspect.isabstract(extralazy_Book)


def test_extralazy_book_constructor_exists():
    assert callable(extralazy_Book.__init__)


def test_extralazy_book_constructor_args():
    sig = inspect.signature(extralazy_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "subTitles" in params, "Missing parameter 'subTitles'"

def test_extralazy_book_has_title():
    assert hasattr(extralazy_Book, "title")
    descriptor = None
    for klass in extralazy_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_extralazy_book_has_subTitles():
    assert hasattr(extralazy_Book, "subTitles")
    descriptor = None
    for klass in extralazy_Book.__mro__:
        if "subTitles" in klass.__dict__:
            descriptor = klass.__dict__["subTitles"]
            break
    assert isinstance(descriptor, property)



def test_extralazy_writer_is_not_abstract():
    assert not inspect.isabstract(extralazy_Writer)


def test_extralazy_writer_constructor_exists():
    assert callable(extralazy_Writer.__init__)


def test_extralazy_writer_constructor_args():
    sig = inspect.signature(extralazy_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_extralazy_writer_has_name():
    assert hasattr(extralazy_Writer, "name")
    descriptor = None
    for klass in extralazy_Writer.__mro__:
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
extralazy_Book_strategy = st.builds(
    extralazy_Book,
    title=
        safe_text,
    subTitles=
        safe_text
)
extralazy_Writer_strategy = st.builds(
    extralazy_Writer,
    name=
        safe_text
)

@given(instance=extralazy_Book_strategy)
@settings(max_examples=50)
def test_extralazy_book_instantiation(instance):
    assert isinstance(instance, extralazy_Book)



@given(instance=extralazy_Book_strategy)
def test_extralazy_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=extralazy_Book_strategy)
def test_extralazy_book_subTitles_setter(instance):
    original = instance.subTitles
    instance.subTitles = original
    assert instance.subTitles == original

@given(instance=extralazy_Writer_strategy)
@settings(max_examples=50)
def test_extralazy_writer_instantiation(instance):
    assert isinstance(instance, extralazy_Writer)



@given(instance=extralazy_Writer_strategy)
def test_extralazy_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
