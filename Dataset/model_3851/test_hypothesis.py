import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SimpleRDBMS::Database,
    SimpleRDBMS::Column,
    SimpleRDBMS::FKey,
    SimpleRDBMS::Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplerdbms::database_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::Database)


def test_simplerdbms::database_constructor_exists():
    assert callable(SimpleRDBMS::Database.__init__)


def test_simplerdbms::database_constructor_args():
    sig = inspect.signature(SimpleRDBMS::Database.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::column_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::Column)


def test_simplerdbms::column_constructor_exists():
    assert callable(SimpleRDBMS::Column.__init__)


def test_simplerdbms::column_constructor_args():
    sig = inspect.signature(SimpleRDBMS::Column.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_simplerdbms::column_has_id():
    assert hasattr(SimpleRDBMS::Column, "id")
    descriptor = None
    for klass in SimpleRDBMS::Column.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms::column_has_name():
    assert hasattr(SimpleRDBMS::Column, "name")
    descriptor = None
    for klass in SimpleRDBMS::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms::column_has_type():
    assert hasattr(SimpleRDBMS::Column, "type")
    descriptor = None
    for klass in SimpleRDBMS::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_simplerdbms::fkey_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::FKey)


def test_simplerdbms::fkey_constructor_exists():
    assert callable(SimpleRDBMS::FKey.__init__)


def test_simplerdbms::fkey_constructor_args():
    sig = inspect.signature(SimpleRDBMS::FKey.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::table_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::Table)


def test_simplerdbms::table_constructor_exists():
    assert callable(SimpleRDBMS::Table.__init__)


def test_simplerdbms::table_constructor_args():
    sig = inspect.signature(SimpleRDBMS::Table.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplerdbms::table_has_id():
    assert hasattr(SimpleRDBMS::Table, "id")
    descriptor = None
    for klass in SimpleRDBMS::Table.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms::table_has_name():
    assert hasattr(SimpleRDBMS::Table, "name")
    descriptor = None
    for klass in SimpleRDBMS::Table.__mro__:
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
SimpleRDBMS::Database_strategy = st.builds(
    SimpleRDBMS::Database,
)
SimpleRDBMS::Column_strategy = st.builds(
    SimpleRDBMS::Column,
    id=
        st.integers(),
    name=
        safe_text,
    type=
        safe_text
)
SimpleRDBMS::FKey_strategy = st.builds(
    SimpleRDBMS::FKey,
)
SimpleRDBMS::Table_strategy = st.builds(
    SimpleRDBMS::Table,
    id=
        st.integers(),
    name=
        safe_text
)

@given(instance=SimpleRDBMS::Database_strategy)
@settings(max_examples=50)
def test_simplerdbms::database_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::Database)

@given(instance=SimpleRDBMS::Column_strategy)
@settings(max_examples=50)
def test_simplerdbms::column_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::Column)

@given(instance=SimpleRDBMS::Column_strategy)
def test_simplerdbms::column_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=SimpleRDBMS::Column_strategy)
def test_simplerdbms::column_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=SimpleRDBMS::Column_strategy)
def test_simplerdbms::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleRDBMS::Column_strategy)
def test_simplerdbms::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleRDBMS::Column_strategy)
def test_simplerdbms::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=SimpleRDBMS::Column_strategy)
def test_simplerdbms::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=SimpleRDBMS::FKey_strategy)
@settings(max_examples=50)
def test_simplerdbms::fkey_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::FKey)

@given(instance=SimpleRDBMS::Table_strategy)
@settings(max_examples=50)
def test_simplerdbms::table_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::Table)

@given(instance=SimpleRDBMS::Table_strategy)
def test_simplerdbms::table_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=SimpleRDBMS::Table_strategy)
def test_simplerdbms::table_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=SimpleRDBMS::Table_strategy)
def test_simplerdbms::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleRDBMS::Table_strategy)
def test_simplerdbms::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
