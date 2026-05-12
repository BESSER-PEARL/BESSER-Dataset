import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sqlCrudGenerator_DataType,
    sqlCrudGenerator_ForeignKey,
    sqlCrudGenerator_PrimaryKey,
    sqlCrudGenerator_Column,
    sqlCrudGenerator_Table,
    sqlCrudGenerator_Schema,
    ENUM_DATA_TYPE,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sqlcrudgenerator_datatype_is_not_abstract():
    assert not inspect.isabstract(sqlCrudGenerator_DataType)


def test_sqlcrudgenerator_datatype_constructor_exists():
    assert callable(sqlCrudGenerator_DataType.__init__)


def test_sqlcrudgenerator_datatype_constructor_args():
    sig = inspect.signature(sqlCrudGenerator_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_sqlcrudgenerator_datatype_has_precision():
    assert hasattr(sqlCrudGenerator_DataType, "precision")
    descriptor = None
    for klass in sqlCrudGenerator_DataType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_sqlcrudgenerator_datatype_has_dataType():
    assert hasattr(sqlCrudGenerator_DataType, "dataType")
    descriptor = None
    for klass in sqlCrudGenerator_DataType.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_sqlcrudgenerator_foreignkey_is_not_abstract():
    assert not inspect.isabstract(sqlCrudGenerator_ForeignKey)


def test_sqlcrudgenerator_foreignkey_constructor_exists():
    assert callable(sqlCrudGenerator_ForeignKey.__init__)


def test_sqlcrudgenerator_foreignkey_constructor_args():
    sig = inspect.signature(sqlCrudGenerator_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_sqlcrudgenerator_primarykey_is_not_abstract():
    assert not inspect.isabstract(sqlCrudGenerator_PrimaryKey)


def test_sqlcrudgenerator_primarykey_constructor_exists():
    assert callable(sqlCrudGenerator_PrimaryKey.__init__)


def test_sqlcrudgenerator_primarykey_constructor_args():
    sig = inspect.signature(sqlCrudGenerator_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_sqlcrudgenerator_column_is_not_abstract():
    assert not inspect.isabstract(sqlCrudGenerator_Column)


def test_sqlcrudgenerator_column_constructor_exists():
    assert callable(sqlCrudGenerator_Column.__init__)


def test_sqlcrudgenerator_column_constructor_args():
    sig = inspect.signature(sqlCrudGenerator_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlcrudgenerator_column_has_name():
    assert hasattr(sqlCrudGenerator_Column, "name")
    descriptor = None
    for klass in sqlCrudGenerator_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlcrudgenerator_table_is_not_abstract():
    assert not inspect.isabstract(sqlCrudGenerator_Table)


def test_sqlcrudgenerator_table_constructor_exists():
    assert callable(sqlCrudGenerator_Table.__init__)


def test_sqlcrudgenerator_table_constructor_args():
    sig = inspect.signature(sqlCrudGenerator_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlcrudgenerator_table_has_name():
    assert hasattr(sqlCrudGenerator_Table, "name")
    descriptor = None
    for klass in sqlCrudGenerator_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlcrudgenerator_schema_is_not_abstract():
    assert not inspect.isabstract(sqlCrudGenerator_Schema)


def test_sqlcrudgenerator_schema_constructor_exists():
    assert callable(sqlCrudGenerator_Schema.__init__)


def test_sqlcrudgenerator_schema_constructor_args():
    sig = inspect.signature(sqlCrudGenerator_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlcrudgenerator_schema_has_name():
    assert hasattr(sqlCrudGenerator_Schema, "name")
    descriptor = None
    for klass in sqlCrudGenerator_Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_enum_data_type_exists():
    # Check that the Enumeration exists
    assert ENUM_DATA_TYPE is not None

def test_enum_data_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ENUM_DATA_TYPE]
    expected_literals = [
        "DATE",
        "BIGINT_M",
        "ARRAY",
        "REAL",
        "TIMESTAMP",
        "VARYING",
        "SMALLINT",
        "DECIMAL",
        "VARBINARY",
        "ARRAY_M",
        "BOOLEAN",
        "NUMERIC",
        "VARCHAR_M",
        "DATE_M",
        "CHARACTER_M",
        "INTEGER",
        "BINARY",
        "TIME",
        "VARBINARY_M",
        "DECIMAL_M",
        "TIME_M",
        "XML",
        "VARYING_M",
        "FLOAT",
        "BINARY_M",
        "XML_M",
        "NUMERIC_M",
        "MULTISET_M",
        "TIMESTAMP_M",
        "CHARACTER",
        "FLOAT_M",
        "BOOLEAN_M",
        "INTERVAL",
        "INTERVAL_M",
        "REAL_M",
        "INT",
        "BIGINT",
        "INTEGER_M",
        "INT_M",
        "MULTISET",
        "VARCHAR",
        "SMALLINT_M",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ENUM_DATA_TYPE"


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
sqlCrudGenerator_DataType_strategy = st.builds(
    sqlCrudGenerator_DataType,
    precision=
        st.integers(),
    dataType=
        safe_text
)
sqlCrudGenerator_ForeignKey_strategy = st.builds(
    sqlCrudGenerator_ForeignKey,
)
sqlCrudGenerator_PrimaryKey_strategy = st.builds(
    sqlCrudGenerator_PrimaryKey,
)
sqlCrudGenerator_Column_strategy = st.builds(
    sqlCrudGenerator_Column,
    name=
        safe_text
)
sqlCrudGenerator_Table_strategy = st.builds(
    sqlCrudGenerator_Table,
    name=
        safe_text
)
sqlCrudGenerator_Schema_strategy = st.builds(
    sqlCrudGenerator_Schema,
    name=
        safe_text
)

@given(instance=sqlCrudGenerator_DataType_strategy)
@settings(max_examples=50)
def test_sqlcrudgenerator_datatype_instantiation(instance):
    assert isinstance(instance, sqlCrudGenerator_DataType)



@given(instance=sqlCrudGenerator_DataType_strategy)
def test_sqlcrudgenerator_datatype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=sqlCrudGenerator_DataType_strategy)
def test_sqlcrudgenerator_datatype_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=sqlCrudGenerator_ForeignKey_strategy)
@settings(max_examples=50)
def test_sqlcrudgenerator_foreignkey_instantiation(instance):
    assert isinstance(instance, sqlCrudGenerator_ForeignKey)

@given(instance=sqlCrudGenerator_PrimaryKey_strategy)
@settings(max_examples=50)
def test_sqlcrudgenerator_primarykey_instantiation(instance):
    assert isinstance(instance, sqlCrudGenerator_PrimaryKey)

@given(instance=sqlCrudGenerator_Column_strategy)
@settings(max_examples=50)
def test_sqlcrudgenerator_column_instantiation(instance):
    assert isinstance(instance, sqlCrudGenerator_Column)



@given(instance=sqlCrudGenerator_Column_strategy)
def test_sqlcrudgenerator_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqlCrudGenerator_Table_strategy)
@settings(max_examples=50)
def test_sqlcrudgenerator_table_instantiation(instance):
    assert isinstance(instance, sqlCrudGenerator_Table)



@given(instance=sqlCrudGenerator_Table_strategy)
def test_sqlcrudgenerator_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqlCrudGenerator_Schema_strategy)
@settings(max_examples=50)
def test_sqlcrudgenerator_schema_instantiation(instance):
    assert isinstance(instance, sqlCrudGenerator_Schema)



@given(instance=sqlCrudGenerator_Schema_strategy)
def test_sqlcrudgenerator_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
