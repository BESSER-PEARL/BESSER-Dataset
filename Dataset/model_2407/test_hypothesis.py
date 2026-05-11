import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    dbschema::Column,
    dbschema::Table,
    dbschema::DBSchema,
    dbschema::NamedElement,
    Column,
    dbschema::ForeignKeyColumn,
    dbschema::AttributeColumn,
    ColumnType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_dbschema::column_is_not_abstract():
    assert not inspect.isabstract(dbschema::Column)


def test_dbschema::column_constructor_exists():
    assert callable(dbschema::Column.__init__)


def test_dbschema::column_constructor_args():
    sig = inspect.signature(dbschema::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "primary" in params, "Missing parameter 'primary'"
    assert "size" in params, "Missing parameter 'size'"

def test_dbschema::column_has_type():
    assert hasattr(dbschema::Column, "type")
    descriptor = None
    for klass in dbschema::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_dbschema::column_has_primary():
    assert hasattr(dbschema::Column, "primary")
    descriptor = None
    for klass in dbschema::Column.__mro__:
        if "primary" in klass.__dict__:
            descriptor = klass.__dict__["primary"]
            break
    assert isinstance(descriptor, property)

def test_dbschema::column_has_size():
    assert hasattr(dbschema::Column, "size")
    descriptor = None
    for klass in dbschema::Column.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_dbschema::table_is_not_abstract():
    assert not inspect.isabstract(dbschema::Table)


def test_dbschema::table_constructor_exists():
    assert callable(dbschema::Table.__init__)


def test_dbschema::table_constructor_args():
    sig = inspect.signature(dbschema::Table.__init__)
    params = list(sig.parameters.keys())



def test_dbschema::dbschema_is_not_abstract():
    assert not inspect.isabstract(dbschema::DBSchema)


def test_dbschema::dbschema_constructor_exists():
    assert callable(dbschema::DBSchema.__init__)


def test_dbschema::dbschema_constructor_args():
    sig = inspect.signature(dbschema::DBSchema.__init__)
    params = list(sig.parameters.keys())



def test_dbschema::namedelement_is_not_abstract():
    assert not inspect.isabstract(dbschema::NamedElement)


def test_dbschema::namedelement_constructor_exists():
    assert callable(dbschema::NamedElement.__init__)


def test_dbschema::namedelement_constructor_args():
    sig = inspect.signature(dbschema::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbschema::namedelement_has_name():
    assert hasattr(dbschema::NamedElement, "name")
    descriptor = None
    for klass in dbschema::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_dbschema::foreignkeycolumn_is_not_abstract():
    assert not inspect.isabstract(dbschema::ForeignKeyColumn)


def test_dbschema::foreignkeycolumn_constructor_exists():
    assert callable(dbschema::ForeignKeyColumn.__init__)


def test_dbschema::foreignkeycolumn_constructor_args():
    sig = inspect.signature(dbschema::ForeignKeyColumn.__init__)
    params = list(sig.parameters.keys())



def test_dbschema::attributecolumn_is_not_abstract():
    assert not inspect.isabstract(dbschema::AttributeColumn)


def test_dbschema::attributecolumn_constructor_exists():
    assert callable(dbschema::AttributeColumn.__init__)


def test_dbschema::attributecolumn_constructor_args():
    sig = inspect.signature(dbschema::AttributeColumn.__init__)
    params = list(sig.parameters.keys())

def test_columntype_exists():
    # Check that the Enumeration exists
    assert ColumnType is not None

def test_columntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColumnType]
    expected_literals = [
        "TIME",
        "VARBINARY",
        "INTEGER",
        "DATALINK",
        "NCHAR",
        "LONGVARCHAR",
        "BLOB",
        "BINARY",
        "BIT",
        "NULL",
        "CLOB",
        "ROWID",
        "DISTINCT",
        "OTHER",
        "DOUBLE",
        "DECIMAL",
        "LONGNVARCHAR",
        "CHAR",
        "TIMESTAMP",
        "BIGINT",
        "BOOLEAN",
        "NVARCHAR",
        "SQLXML",
        "REF",
        "FLOAT",
        "LONGVARBINARY",
        "DATE",
        "ARRAY",
        "STRUCT",
        "NCLOB",
        "TINYINT",
        "NUMERIC",
        "JAVAOBJECT",
        "REAL",
        "VARCHAR",
        "SMALLINT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColumnType"


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
NamedElement_strategy = st.builds(
    NamedElement,
)
dbschema::Column_strategy = st.builds(
    dbschema::Column,
    type=
        safe_text,
    primary=
        st.booleans(),
    size=
        st.integers()
)
dbschema::Table_strategy = st.builds(
    dbschema::Table,
)
dbschema::DBSchema_strategy = st.builds(
    dbschema::DBSchema,
)
dbschema::NamedElement_strategy = st.builds(
    dbschema::NamedElement,
    name=
        safe_text
)
Column_strategy = st.builds(
    Column,
)
dbschema::ForeignKeyColumn_strategy = st.builds(
    dbschema::ForeignKeyColumn,
)
dbschema::AttributeColumn_strategy = st.builds(
    dbschema::AttributeColumn,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=dbschema::Column_strategy)
@settings(max_examples=50)
def test_dbschema::column_instantiation(instance):
    assert isinstance(instance, dbschema::Column)

@given(instance=dbschema::Column_strategy)
def test_dbschema::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=dbschema::Column_strategy)
def test_dbschema::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=dbschema::Column_strategy)
def test_dbschema::column_primary_type(instance):
    assert isinstance(instance.primary, bool)


@given(instance=dbschema::Column_strategy)
def test_dbschema::column_primary_setter(instance):
    original = instance.primary
    instance.primary = original
    assert instance.primary == original

@given(instance=dbschema::Column_strategy)
def test_dbschema::column_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=dbschema::Column_strategy)
def test_dbschema::column_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=dbschema::Table_strategy)
@settings(max_examples=50)
def test_dbschema::table_instantiation(instance):
    assert isinstance(instance, dbschema::Table)

@given(instance=dbschema::DBSchema_strategy)
@settings(max_examples=50)
def test_dbschema::dbschema_instantiation(instance):
    assert isinstance(instance, dbschema::DBSchema)

@given(instance=dbschema::NamedElement_strategy)
@settings(max_examples=50)
def test_dbschema::namedelement_instantiation(instance):
    assert isinstance(instance, dbschema::NamedElement)

@given(instance=dbschema::NamedElement_strategy)
def test_dbschema::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbschema::NamedElement_strategy)
def test_dbschema::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=dbschema::ForeignKeyColumn_strategy)
@settings(max_examples=50)
def test_dbschema::foreignkeycolumn_instantiation(instance):
    assert isinstance(instance, dbschema::ForeignKeyColumn)

@given(instance=dbschema::AttributeColumn_strategy)
@settings(max_examples=50)
def test_dbschema::attributecolumn_instantiation(instance):
    assert isinstance(instance, dbschema::AttributeColumn)
