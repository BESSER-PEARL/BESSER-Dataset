import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    extralazy::Writer,
    extralazy::Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_extralazy::writer_is_not_abstract():
    assert not inspect.isabstract(extralazy::Writer)


def test_extralazy::writer_constructor_exists():
    assert callable(extralazy::Writer.__init__)


def test_extralazy::writer_constructor_args():
    sig = inspect.signature(extralazy::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_extralazy::writer_has_name():
    assert hasattr(extralazy::Writer, "name")
    descriptor = None
    for klass in extralazy::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_extralazy::book_is_not_abstract():
    assert not inspect.isabstract(extralazy::Book)


def test_extralazy::book_constructor_exists():
    assert callable(extralazy::Book.__init__)


def test_extralazy::book_constructor_args():
    sig = inspect.signature(extralazy::Book.__init__)
    params = list(sig.parameters.keys())
    assert "subTitles" in params, "Missing parameter 'subTitles'"
    assert "title" in params, "Missing parameter 'title'"

def test_extralazy::book_has_subTitles():
    assert hasattr(extralazy::Book, "subTitles")
    descriptor = None
    for klass in extralazy::Book.__mro__:
        if "subTitles" in klass.__dict__:
            descriptor = klass.__dict__["subTitles"]
            break
    assert isinstance(descriptor, property)

def test_extralazy::book_has_title():
    assert hasattr(extralazy::Book, "title")
    descriptor = None
    for klass in extralazy::Book.__mro__:
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
extralazy::Writer_strategy = st.builds(
    extralazy::Writer,
    name=
        safe_text
)
extralazy::Book_strategy = st.builds(
    extralazy::Book,
    subTitles=
        safe_text,
    title=
        safe_text
)

@given(instance=extralazy::Writer_strategy)
@settings(max_examples=50)
def test_extralazy::writer_instantiation(instance):
    assert isinstance(instance, extralazy::Writer)

@given(instance=extralazy::Writer_strategy)
def test_extralazy::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=extralazy::Writer_strategy)
def test_extralazy::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=extralazy::Book_strategy)
@settings(max_examples=50)
def test_extralazy::book_instantiation(instance):
    assert isinstance(instance, extralazy::Book)

@given(instance=extralazy::Book_strategy)
def test_extralazy::book_subTitles_type(instance):
    assert isinstance(instance.subTitles, str)


@given(instance=extralazy::Book_strategy)
def test_extralazy::book_subTitles_setter(instance):
    original = instance.subTitles
    instance.subTitles = original
    assert instance.subTitles == original

@given(instance=extralazy::Book_strategy)
def test_extralazy::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=extralazy::Book_strategy)
def test_extralazy::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
