import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sql::Column,
    sql::Table,
    sql::Database,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sql::column_is_not_abstract():
    assert not inspect.isabstract(sql::Column)


def test_sql::column_constructor_exists():
    assert callable(sql::Column.__init__)


def test_sql::column_constructor_args():
    sig = inspect.signature(sql::Column.__init__)
    params = list(sig.parameters.keys())
    assert "PrimaryKey" in params, "Missing parameter 'PrimaryKey'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_sql::column_has_PrimaryKey():
    assert hasattr(sql::Column, "PrimaryKey")
    descriptor = None
    for klass in sql::Column.__mro__:
        if "PrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["PrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_sql::column_has_name():
    assert hasattr(sql::Column, "name")
    descriptor = None
    for klass in sql::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sql::column_has_type():
    assert hasattr(sql::Column, "type")
    descriptor = None
    for klass in sql::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_sql::table_is_not_abstract():
    assert not inspect.isabstract(sql::Table)


def test_sql::table_constructor_exists():
    assert callable(sql::Table.__init__)


def test_sql::table_constructor_args():
    sig = inspect.signature(sql::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql::table_has_name():
    assert hasattr(sql::Table, "name")
    descriptor = None
    for klass in sql::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql::database_is_not_abstract():
    assert not inspect.isabstract(sql::Database)


def test_sql::database_constructor_exists():
    assert callable(sql::Database.__init__)


def test_sql::database_constructor_args():
    sig = inspect.signature(sql::Database.__init__)
    params = list(sig.parameters.keys())
    assert "TypeDB" in params, "Missing parameter 'TypeDB'"
    assert "name" in params, "Missing parameter 'name'"

def test_sql::database_has_TypeDB():
    assert hasattr(sql::Database, "TypeDB")
    descriptor = None
    for klass in sql::Database.__mro__:
        if "TypeDB" in klass.__dict__:
            descriptor = klass.__dict__["TypeDB"]
            break
    assert isinstance(descriptor, property)

def test_sql::database_has_name():
    assert hasattr(sql::Database, "name")
    descriptor = None
    for klass in sql::Database.__mro__:
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
sql::Column_strategy = st.builds(
    sql::Column,
    PrimaryKey=
        st.booleans(),
    name=
        safe_text,
    type=
        safe_text
)
sql::Table_strategy = st.builds(
    sql::Table,
    name=
        safe_text
)
sql::Database_strategy = st.builds(
    sql::Database,
    TypeDB=
        safe_text,
    name=
        safe_text
)

@given(instance=sql::Column_strategy)
@settings(max_examples=50)
def test_sql::column_instantiation(instance):
    assert isinstance(instance, sql::Column)

@given(instance=sql::Column_strategy)
def test_sql::column_PrimaryKey_type(instance):
    assert isinstance(instance.PrimaryKey, bool)


@given(instance=sql::Column_strategy)
def test_sql::column_PrimaryKey_setter(instance):
    original = instance.PrimaryKey
    instance.PrimaryKey = original
    assert instance.PrimaryKey == original

@given(instance=sql::Column_strategy)
def test_sql::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sql::Column_strategy)
def test_sql::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sql::Column_strategy)
def test_sql::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=sql::Column_strategy)
def test_sql::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sql::Table_strategy)
@settings(max_examples=50)
def test_sql::table_instantiation(instance):
    assert isinstance(instance, sql::Table)

@given(instance=sql::Table_strategy)
def test_sql::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sql::Table_strategy)
def test_sql::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sql::Database_strategy)
@settings(max_examples=50)
def test_sql::database_instantiation(instance):
    assert isinstance(instance, sql::Database)

@given(instance=sql::Database_strategy)
def test_sql::database_TypeDB_type(instance):
    assert isinstance(instance.TypeDB, str)


@given(instance=sql::Database_strategy)
def test_sql::database_TypeDB_setter(instance):
    original = instance.TypeDB
    instance.TypeDB = original
    assert instance.TypeDB == original

@given(instance=sql::Database_strategy)
def test_sql::database_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sql::Database_strategy)
def test_sql::database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
