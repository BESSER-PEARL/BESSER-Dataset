import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sqlCrudGenerator::DataType,
    sqlCrudGenerator::ForeignKey,
    sqlCrudGenerator::PrimaryKey,
    sqlCrudGenerator::Column,
    sqlCrudGenerator::Table,
    sqlCrudGenerator::Schema,
    ENUM_DATA_TYPE,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sqlcrudgenerator::datatype_is_not_abstract():
    assert not inspect.isabstract(sqlCrudGenerator::DataType)


def test_sqlcrudgenerator::datatype_constructor_exists():
    assert callable(sqlCrudGenerator::DataType.__init__)


def test_sqlcrudgenerator::datatype_constructor_args():
    sig = inspect.signature(sqlCrudGenerator::DataType.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_sqlcrudgenerator::datatype_has_precision():
    assert hasattr(sqlCrudGenerator::DataType, "precision")
    descriptor = None
    for klass in sqlCrudGenerator::DataType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_sqlcrudgenerator::datatype_has_dataType():
    assert hasattr(sqlCrudGenerator::DataType, "dataType")
    descriptor = None
    for klass in sqlCrudGenerator::DataType.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_sqlcrudgenerator::foreignkey_is_not_abstract():
    assert not inspect.isabstract(sqlCrudGenerator::ForeignKey)


def test_sqlcrudgenerator::foreignkey_constructor_exists():
    assert callable(sqlCrudGenerator::ForeignKey.__init__)


def test_sqlcrudgenerator::foreignkey_constructor_args():
    sig = inspect.signature(sqlCrudGenerator::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_sqlcrudgenerator::primarykey_is_not_abstract():
    assert not inspect.isabstract(sqlCrudGenerator::PrimaryKey)


def test_sqlcrudgenerator::primarykey_constructor_exists():
    assert callable(sqlCrudGenerator::PrimaryKey.__init__)


def test_sqlcrudgenerator::primarykey_constructor_args():
    sig = inspect.signature(sqlCrudGenerator::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_sqlcrudgenerator::column_is_not_abstract():
    assert not inspect.isabstract(sqlCrudGenerator::Column)


def test_sqlcrudgenerator::column_constructor_exists():
    assert callable(sqlCrudGenerator::Column.__init__)


def test_sqlcrudgenerator::column_constructor_args():
    sig = inspect.signature(sqlCrudGenerator::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlcrudgenerator::column_has_name():
    assert hasattr(sqlCrudGenerator::Column, "name")
    descriptor = None
    for klass in sqlCrudGenerator::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlcrudgenerator::table_is_not_abstract():
    assert not inspect.isabstract(sqlCrudGenerator::Table)


def test_sqlcrudgenerator::table_constructor_exists():
    assert callable(sqlCrudGenerator::Table.__init__)


def test_sqlcrudgenerator::table_constructor_args():
    sig = inspect.signature(sqlCrudGenerator::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlcrudgenerator::table_has_name():
    assert hasattr(sqlCrudGenerator::Table, "name")
    descriptor = None
    for klass in sqlCrudGenerator::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlcrudgenerator::schema_is_not_abstract():
    assert not inspect.isabstract(sqlCrudGenerator::Schema)


def test_sqlcrudgenerator::schema_constructor_exists():
    assert callable(sqlCrudGenerator::Schema.__init__)


def test_sqlcrudgenerator::schema_constructor_args():
    sig = inspect.signature(sqlCrudGenerator::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlcrudgenerator::schema_has_name():
    assert hasattr(sqlCrudGenerator::Schema, "name")
    descriptor = None
    for klass in sqlCrudGenerator::Schema.__mro__:
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
        "BOOLEAN",
        "TIMESTAMP_M",
        "VARYING",
        "NUMERIC_M",
        "DECIMAL",
        "INT",
        "ARRAY",
        "BIGINT_M",
        "SMALLINT_M",
        "ARRAY_M",
        "VARYING_M",
        "INTEGER",
        "DATE",
        "XML_M",
        "INTEGER_M",
        "CHARACTER_M",
        "DATE_M",
        "TIMESTAMP",
        "VARBINARY_M",
        "REAL_M",
        "INTERVAL",
        "MULTISET",
        "BINARY",
        "VARCHAR_M",
        "TIME",
        "TIME_M",
        "INTERVAL_M",
        "NUMERIC",
        "CHARACTER",
        "XML",
        "FLOAT",
        "MULTISET_M",
        "VARBINARY",
        "INT_M",
        "VARCHAR",
        "SMALLINT",
        "BINARY_M",
        "FLOAT_M",
        "REAL",
        "BIGINT",
        "BOOLEAN_M",
        "DECIMAL_M",
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
sqlCrudGenerator::DataType_strategy = st.builds(
    sqlCrudGenerator::DataType,
    precision=
        st.integers(),
    dataType=
        safe_text
)
sqlCrudGenerator::ForeignKey_strategy = st.builds(
    sqlCrudGenerator::ForeignKey,
)
sqlCrudGenerator::PrimaryKey_strategy = st.builds(
    sqlCrudGenerator::PrimaryKey,
)
sqlCrudGenerator::Column_strategy = st.builds(
    sqlCrudGenerator::Column,
    name=
        safe_text
)
sqlCrudGenerator::Table_strategy = st.builds(
    sqlCrudGenerator::Table,
    name=
        safe_text
)
sqlCrudGenerator::Schema_strategy = st.builds(
    sqlCrudGenerator::Schema,
    name=
        safe_text
)

@given(instance=sqlCrudGenerator::DataType_strategy)
@settings(max_examples=50)
def test_sqlcrudgenerator::datatype_instantiation(instance):
    assert isinstance(instance, sqlCrudGenerator::DataType)

@given(instance=sqlCrudGenerator::DataType_strategy)
def test_sqlcrudgenerator::datatype_precision_type(instance):
    assert isinstance(instance.precision, int)


@given(instance=sqlCrudGenerator::DataType_strategy)
def test_sqlcrudgenerator::datatype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=sqlCrudGenerator::DataType_strategy)
def test_sqlcrudgenerator::datatype_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=sqlCrudGenerator::DataType_strategy)
def test_sqlcrudgenerator::datatype_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=sqlCrudGenerator::ForeignKey_strategy)
@settings(max_examples=50)
def test_sqlcrudgenerator::foreignkey_instantiation(instance):
    assert isinstance(instance, sqlCrudGenerator::ForeignKey)

@given(instance=sqlCrudGenerator::PrimaryKey_strategy)
@settings(max_examples=50)
def test_sqlcrudgenerator::primarykey_instantiation(instance):
    assert isinstance(instance, sqlCrudGenerator::PrimaryKey)

@given(instance=sqlCrudGenerator::Column_strategy)
@settings(max_examples=50)
def test_sqlcrudgenerator::column_instantiation(instance):
    assert isinstance(instance, sqlCrudGenerator::Column)

@given(instance=sqlCrudGenerator::Column_strategy)
def test_sqlcrudgenerator::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqlCrudGenerator::Column_strategy)
def test_sqlcrudgenerator::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqlCrudGenerator::Table_strategy)
@settings(max_examples=50)
def test_sqlcrudgenerator::table_instantiation(instance):
    assert isinstance(instance, sqlCrudGenerator::Table)

@given(instance=sqlCrudGenerator::Table_strategy)
def test_sqlcrudgenerator::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqlCrudGenerator::Table_strategy)
def test_sqlcrudgenerator::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqlCrudGenerator::Schema_strategy)
@settings(max_examples=50)
def test_sqlcrudgenerator::schema_instantiation(instance):
    assert isinstance(instance, sqlCrudGenerator::Schema)

@given(instance=sqlCrudGenerator::Schema_strategy)
def test_sqlcrudgenerator::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqlCrudGenerator::Schema_strategy)
def test_sqlcrudgenerator::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
