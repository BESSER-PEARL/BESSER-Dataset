import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    column::TestSchema,
    column::Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_column::testschema_is_not_abstract():
    assert not inspect.isabstract(column::TestSchema)


def test_column::testschema_constructor_exists():
    assert callable(column::TestSchema.__init__)


def test_column::testschema_constructor_args():
    sig = inspect.signature(column::TestSchema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_column::testschema_has_name():
    assert hasattr(column::TestSchema, "name")
    descriptor = None
    for klass in column::TestSchema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_column::book_is_not_abstract():
    assert not inspect.isabstract(column::Book)


def test_column::book_constructor_exists():
    assert callable(column::Book.__init__)


def test_column::book_constructor_args():
    sig = inspect.signature(column::Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"
    assert "author" in params, "Missing parameter 'author'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_column::book_has_pages():
    assert hasattr(column::Book, "pages")
    descriptor = None
    for klass in column::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_column::book_has_title():
    assert hasattr(column::Book, "title")
    descriptor = None
    for klass in column::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_column::book_has_author():
    assert hasattr(column::Book, "author")
    descriptor = None
    for klass in column::Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_column::book_has_weight():
    assert hasattr(column::Book, "weight")
    descriptor = None
    for klass in column::Book.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
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
column::TestSchema_strategy = st.builds(
    column::TestSchema,
    name=
        safe_text
)
column::Book_strategy = st.builds(
    column::Book,
    pages=
        safe_text,
    title=
        safe_text,
    author=
        safe_text,
    weight=
        safe_text
)

@given(instance=column::TestSchema_strategy)
@settings(max_examples=50)
def test_column::testschema_instantiation(instance):
    assert isinstance(instance, column::TestSchema)

@given(instance=column::TestSchema_strategy)
def test_column::testschema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=column::TestSchema_strategy)
def test_column::testschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=column::Book_strategy)
@settings(max_examples=50)
def test_column::book_instantiation(instance):
    assert isinstance(instance, column::Book)

@given(instance=column::Book_strategy)
def test_column::book_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=column::Book_strategy)
def test_column::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=column::Book_strategy)
def test_column::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=column::Book_strategy)
def test_column::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=column::Book_strategy)
def test_column::book_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=column::Book_strategy)
def test_column::book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=column::Book_strategy)
def test_column::book_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=column::Book_strategy)
def test_column::book_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original
