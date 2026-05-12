import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sql_Column,
    sql_Table,
    sql_Database,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sql_column_is_not_abstract():
    assert not inspect.isabstract(sql_Column)


def test_sql_column_constructor_exists():
    assert callable(sql_Column.__init__)


def test_sql_column_constructor_args():
    sig = inspect.signature(sql_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "PrimaryKey" in params, "Missing parameter 'PrimaryKey'"
    assert "name" in params, "Missing parameter 'name'"

def test_sql_column_has_type():
    assert hasattr(sql_Column, "type")
    descriptor = None
    for klass in sql_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_sql_column_has_PrimaryKey():
    assert hasattr(sql_Column, "PrimaryKey")
    descriptor = None
    for klass in sql_Column.__mro__:
        if "PrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["PrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_sql_column_has_name():
    assert hasattr(sql_Column, "name")
    descriptor = None
    for klass in sql_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql_table_is_not_abstract():
    assert not inspect.isabstract(sql_Table)


def test_sql_table_constructor_exists():
    assert callable(sql_Table.__init__)


def test_sql_table_constructor_args():
    sig = inspect.signature(sql_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql_table_has_name():
    assert hasattr(sql_Table, "name")
    descriptor = None
    for klass in sql_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql_database_is_not_abstract():
    assert not inspect.isabstract(sql_Database)


def test_sql_database_constructor_exists():
    assert callable(sql_Database.__init__)


def test_sql_database_constructor_args():
    sig = inspect.signature(sql_Database.__init__)
    params = list(sig.parameters.keys())
    assert "TypeDB" in params, "Missing parameter 'TypeDB'"
    assert "name" in params, "Missing parameter 'name'"

def test_sql_database_has_TypeDB():
    assert hasattr(sql_Database, "TypeDB")
    descriptor = None
    for klass in sql_Database.__mro__:
        if "TypeDB" in klass.__dict__:
            descriptor = klass.__dict__["TypeDB"]
            break
    assert isinstance(descriptor, property)

def test_sql_database_has_name():
    assert hasattr(sql_Database, "name")
    descriptor = None
    for klass in sql_Database.__mro__:
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
sql_Column_strategy = st.builds(
    sql_Column,
    type=
        safe_text,
    PrimaryKey=
        st.booleans(),
    name=
        safe_text
)
sql_Table_strategy = st.builds(
    sql_Table,
    name=
        safe_text
)
sql_Database_strategy = st.builds(
    sql_Database,
    TypeDB=
        safe_text,
    name=
        safe_text
)

@given(instance=sql_Column_strategy)
@settings(max_examples=50)
def test_sql_column_instantiation(instance):
    assert isinstance(instance, sql_Column)



@given(instance=sql_Column_strategy)
def test_sql_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=sql_Column_strategy)
def test_sql_column_PrimaryKey_setter(instance):
    original = instance.PrimaryKey
    instance.PrimaryKey = original
    assert instance.PrimaryKey == original



@given(instance=sql_Column_strategy)
def test_sql_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sql_Table_strategy)
@settings(max_examples=50)
def test_sql_table_instantiation(instance):
    assert isinstance(instance, sql_Table)



@given(instance=sql_Table_strategy)
def test_sql_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sql_Database_strategy)
@settings(max_examples=50)
def test_sql_database_instantiation(instance):
    assert isinstance(instance, sql_Database)



@given(instance=sql_Database_strategy)
def test_sql_database_TypeDB_setter(instance):
    original = instance.TypeDB
    instance.TypeDB = original
    assert instance.TypeDB == original



@given(instance=sql_Database_strategy)
def test_sql_database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
