import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Column,
    SimpleRDBMS::PrimaryKey,
    SimpleRDBMS::Database,
    SimpleRDBMS::Column,
    SimpleRDBMS::FKey,
    SimpleRDBMS::Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::primarykey_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::PrimaryKey)


def test_simplerdbms::primarykey_constructor_exists():
    assert callable(SimpleRDBMS::PrimaryKey.__init__)


def test_simplerdbms::primarykey_constructor_args():
    sig = inspect.signature(SimpleRDBMS::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::database_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::Database)


def test_simplerdbms::database_constructor_exists():
    assert callable(SimpleRDBMS::Database.__init__)


def test_simplerdbms::database_constructor_args():
    sig = inspect.signature(SimpleRDBMS::Database.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "serverAddr" in params, "Missing parameter 'serverAddr'"
    assert "collation" in params, "Missing parameter 'collation'"

def test_simplerdbms::database_has_author():
    assert hasattr(SimpleRDBMS::Database, "author")
    descriptor = None
    for klass in SimpleRDBMS::Database.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms::database_has_serverAddr():
    assert hasattr(SimpleRDBMS::Database, "serverAddr")
    descriptor = None
    for klass in SimpleRDBMS::Database.__mro__:
        if "serverAddr" in klass.__dict__:
            descriptor = klass.__dict__["serverAddr"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms::database_has_collation():
    assert hasattr(SimpleRDBMS::Database, "collation")
    descriptor = None
    for klass in SimpleRDBMS::Database.__mro__:
        if "collation" in klass.__dict__:
            descriptor = klass.__dict__["collation"]
            break
    assert isinstance(descriptor, property)



def test_simplerdbms::column_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::Column)


def test_simplerdbms::column_constructor_exists():
    assert callable(SimpleRDBMS::Column.__init__)


def test_simplerdbms::column_constructor_args():
    sig = inspect.signature(SimpleRDBMS::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"

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

def test_simplerdbms::column_has_id():
    assert hasattr(SimpleRDBMS::Column, "id")
    descriptor = None
    for klass in SimpleRDBMS::Column.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_simplerdbms::table_has_name():
    assert hasattr(SimpleRDBMS::Table, "name")
    descriptor = None
    for klass in SimpleRDBMS::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms::table_has_id():
    assert hasattr(SimpleRDBMS::Table, "id")
    descriptor = None
    for klass in SimpleRDBMS::Table.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
Column_strategy = st.builds(
    Column,
)
SimpleRDBMS::PrimaryKey_strategy = st.builds(
    SimpleRDBMS::PrimaryKey,
)
SimpleRDBMS::Database_strategy = st.builds(
    SimpleRDBMS::Database,
    author=
        safe_text,
    serverAddr=
        safe_text,
    collation=
        safe_text
)
SimpleRDBMS::Column_strategy = st.builds(
    SimpleRDBMS::Column,
    name=
        safe_text,
    type=
        safe_text,
    id=
        st.integers()
)
SimpleRDBMS::FKey_strategy = st.builds(
    SimpleRDBMS::FKey,
)
SimpleRDBMS::Table_strategy = st.builds(
    SimpleRDBMS::Table,
    name=
        safe_text,
    id=
        st.integers()
)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=SimpleRDBMS::PrimaryKey_strategy)
@settings(max_examples=50)
def test_simplerdbms::primarykey_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::PrimaryKey)

@given(instance=SimpleRDBMS::Database_strategy)
@settings(max_examples=50)
def test_simplerdbms::database_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::Database)

@given(instance=SimpleRDBMS::Database_strategy)
def test_simplerdbms::database_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=SimpleRDBMS::Database_strategy)
def test_simplerdbms::database_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=SimpleRDBMS::Database_strategy)
def test_simplerdbms::database_serverAddr_type(instance):
    assert isinstance(instance.serverAddr, str)


@given(instance=SimpleRDBMS::Database_strategy)
def test_simplerdbms::database_serverAddr_setter(instance):
    original = instance.serverAddr
    instance.serverAddr = original
    assert instance.serverAddr == original

@given(instance=SimpleRDBMS::Database_strategy)
def test_simplerdbms::database_collation_type(instance):
    assert isinstance(instance.collation, str)


@given(instance=SimpleRDBMS::Database_strategy)
def test_simplerdbms::database_collation_setter(instance):
    original = instance.collation
    instance.collation = original
    assert instance.collation == original

@given(instance=SimpleRDBMS::Column_strategy)
@settings(max_examples=50)
def test_simplerdbms::column_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::Column)

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

@given(instance=SimpleRDBMS::Column_strategy)
def test_simplerdbms::column_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=SimpleRDBMS::Column_strategy)
def test_simplerdbms::column_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=SimpleRDBMS::FKey_strategy)
@settings(max_examples=50)
def test_simplerdbms::fkey_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::FKey)

@given(instance=SimpleRDBMS::Table_strategy)
@settings(max_examples=50)
def test_simplerdbms::table_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::Table)

@given(instance=SimpleRDBMS::Table_strategy)
def test_simplerdbms::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleRDBMS::Table_strategy)
def test_simplerdbms::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleRDBMS::Table_strategy)
def test_simplerdbms::table_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=SimpleRDBMS::Table_strategy)
def test_simplerdbms::table_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
