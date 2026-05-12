import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sQL_Table,
    sQL_DataBase,
    sQL_foreignKey,
    sQL_primaryKey,
    sQL_column,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sql_table_is_not_abstract():
    assert not inspect.isabstract(sQL_Table)


def test_sql_table_constructor_exists():
    assert callable(sQL_Table.__init__)


def test_sql_table_constructor_args():
    sig = inspect.signature(sQL_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql_table_has_name():
    assert hasattr(sQL_Table, "name")
    descriptor = None
    for klass in sQL_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql_database_is_not_abstract():
    assert not inspect.isabstract(sQL_DataBase)


def test_sql_database_constructor_exists():
    assert callable(sQL_DataBase.__init__)


def test_sql_database_constructor_args():
    sig = inspect.signature(sQL_DataBase.__init__)
    params = list(sig.parameters.keys())



def test_sql_foreignkey_is_not_abstract():
    assert not inspect.isabstract(sQL_foreignKey)


def test_sql_foreignkey_constructor_exists():
    assert callable(sQL_foreignKey.__init__)


def test_sql_foreignkey_constructor_args():
    sig = inspect.signature(sQL_foreignKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql_foreignkey_has_name():
    assert hasattr(sQL_foreignKey, "name")
    descriptor = None
    for klass in sQL_foreignKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql_primarykey_is_not_abstract():
    assert not inspect.isabstract(sQL_primaryKey)


def test_sql_primarykey_constructor_exists():
    assert callable(sQL_primaryKey.__init__)


def test_sql_primarykey_constructor_args():
    sig = inspect.signature(sQL_primaryKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql_primarykey_has_name():
    assert hasattr(sQL_primaryKey, "name")
    descriptor = None
    for klass in sQL_primaryKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql_column_is_not_abstract():
    assert not inspect.isabstract(sQL_column)


def test_sql_column_constructor_exists():
    assert callable(sQL_column.__init__)


def test_sql_column_constructor_args():
    sig = inspect.signature(sQL_column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_sql_column_has_name():
    assert hasattr(sQL_column, "name")
    descriptor = None
    for klass in sQL_column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sql_column_has_type():
    assert hasattr(sQL_column, "type")
    descriptor = None
    for klass in sQL_column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "FLOAT",
        "DATE",
        "NUMERIC",
        "VARCHAR255",
        "DECIMAL",
        "BOOL",
        "CHAR",
        "VARCHAR",
        "INT",
        "TIME",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"


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
sQL_Table_strategy = st.builds(
    sQL_Table,
    name=
        safe_text
)
sQL_DataBase_strategy = st.builds(
    sQL_DataBase,
)
sQL_foreignKey_strategy = st.builds(
    sQL_foreignKey,
    name=
        safe_text
)
sQL_primaryKey_strategy = st.builds(
    sQL_primaryKey,
    name=
        safe_text
)
sQL_column_strategy = st.builds(
    sQL_column,
    name=
        safe_text,
    type=
        safe_text
)

@given(instance=sQL_Table_strategy)
@settings(max_examples=50)
def test_sql_table_instantiation(instance):
    assert isinstance(instance, sQL_Table)



@given(instance=sQL_Table_strategy)
def test_sql_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sQL_DataBase_strategy)
@settings(max_examples=50)
def test_sql_database_instantiation(instance):
    assert isinstance(instance, sQL_DataBase)

@given(instance=sQL_foreignKey_strategy)
@settings(max_examples=50)
def test_sql_foreignkey_instantiation(instance):
    assert isinstance(instance, sQL_foreignKey)



@given(instance=sQL_foreignKey_strategy)
def test_sql_foreignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sQL_primaryKey_strategy)
@settings(max_examples=50)
def test_sql_primarykey_instantiation(instance):
    assert isinstance(instance, sQL_primaryKey)



@given(instance=sQL_primaryKey_strategy)
def test_sql_primarykey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sQL_column_strategy)
@settings(max_examples=50)
def test_sql_column_instantiation(instance):
    assert isinstance(instance, sQL_column)



@given(instance=sQL_column_strategy)
def test_sql_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sQL_column_strategy)
def test_sql_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
