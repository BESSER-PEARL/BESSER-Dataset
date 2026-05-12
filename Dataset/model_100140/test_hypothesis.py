import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Column,
    dbschema_ForeignKeyColumn,
    dbschema_AttributeColumn,
    NamedElement,
    dbschema_Table,
    dbschema_Column,
    dbschema_DBSchema,
    dbschema_NamedElement,
    ColumnType,
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



def test_dbschema_foreignkeycolumn_is_not_abstract():
    assert not inspect.isabstract(dbschema_ForeignKeyColumn)


def test_dbschema_foreignkeycolumn_constructor_exists():
    assert callable(dbschema_ForeignKeyColumn.__init__)


def test_dbschema_foreignkeycolumn_constructor_args():
    sig = inspect.signature(dbschema_ForeignKeyColumn.__init__)
    params = list(sig.parameters.keys())



def test_dbschema_attributecolumn_is_not_abstract():
    assert not inspect.isabstract(dbschema_AttributeColumn)


def test_dbschema_attributecolumn_constructor_exists():
    assert callable(dbschema_AttributeColumn.__init__)


def test_dbschema_attributecolumn_constructor_args():
    sig = inspect.signature(dbschema_AttributeColumn.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_dbschema_table_is_not_abstract():
    assert not inspect.isabstract(dbschema_Table)


def test_dbschema_table_constructor_exists():
    assert callable(dbschema_Table.__init__)


def test_dbschema_table_constructor_args():
    sig = inspect.signature(dbschema_Table.__init__)
    params = list(sig.parameters.keys())



def test_dbschema_column_is_not_abstract():
    assert not inspect.isabstract(dbschema_Column)


def test_dbschema_column_constructor_exists():
    assert callable(dbschema_Column.__init__)


def test_dbschema_column_constructor_args():
    sig = inspect.signature(dbschema_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "primary" in params, "Missing parameter 'primary'"
    assert "size" in params, "Missing parameter 'size'"

def test_dbschema_column_has_type():
    assert hasattr(dbschema_Column, "type")
    descriptor = None
    for klass in dbschema_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_dbschema_column_has_primary():
    assert hasattr(dbschema_Column, "primary")
    descriptor = None
    for klass in dbschema_Column.__mro__:
        if "primary" in klass.__dict__:
            descriptor = klass.__dict__["primary"]
            break
    assert isinstance(descriptor, property)

def test_dbschema_column_has_size():
    assert hasattr(dbschema_Column, "size")
    descriptor = None
    for klass in dbschema_Column.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_dbschema_dbschema_is_not_abstract():
    assert not inspect.isabstract(dbschema_DBSchema)


def test_dbschema_dbschema_constructor_exists():
    assert callable(dbschema_DBSchema.__init__)


def test_dbschema_dbschema_constructor_args():
    sig = inspect.signature(dbschema_DBSchema.__init__)
    params = list(sig.parameters.keys())



def test_dbschema_namedelement_is_not_abstract():
    assert not inspect.isabstract(dbschema_NamedElement)


def test_dbschema_namedelement_constructor_exists():
    assert callable(dbschema_NamedElement.__init__)


def test_dbschema_namedelement_constructor_args():
    sig = inspect.signature(dbschema_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbschema_namedelement_has_name():
    assert hasattr(dbschema_NamedElement, "name")
    descriptor = None
    for klass in dbschema_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_columntype_exists():
    # Check that the Enumeration exists
    assert ColumnType is not None

def test_columntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColumnType]
    expected_literals = [
        "REAL",
        "CHAR",
        "DOUBLE",
        "DECIMAL",
        "LONGVARBINARY",
        "VARBINARY",
        "NCHAR",
        "NCLOB",
        "VARCHAR",
        "ROWID",
        "SQLXML",
        "TIME",
        "LONGNVARCHAR",
        "LONGVARCHAR",
        "TINYINT",
        "NVARCHAR",
        "JAVAOBJECT",
        "NUMERIC",
        "FLOAT",
        "TIMESTAMP",
        "NULL",
        "OTHER",
        "BIGINT",
        "INTEGER",
        "DISTINCT",
        "BIT",
        "ARRAY",
        "DATALINK",
        "CLOB",
        "DATE",
        "SMALLINT",
        "BLOB",
        "BOOLEAN",
        "REF",
        "STRUCT",
        "BINARY",
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
Column_strategy = st.builds(
    Column,
)
dbschema_ForeignKeyColumn_strategy = st.builds(
    dbschema_ForeignKeyColumn,
)
dbschema_AttributeColumn_strategy = st.builds(
    dbschema_AttributeColumn,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
dbschema_Table_strategy = st.builds(
    dbschema_Table,
)
dbschema_Column_strategy = st.builds(
    dbschema_Column,
    type=
        safe_text,
    primary=
        st.booleans(),
    size=
        st.integers()
)
dbschema_DBSchema_strategy = st.builds(
    dbschema_DBSchema,
)
dbschema_NamedElement_strategy = st.builds(
    dbschema_NamedElement,
    name=
        safe_text
)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=dbschema_ForeignKeyColumn_strategy)
@settings(max_examples=50)
def test_dbschema_foreignkeycolumn_instantiation(instance):
    assert isinstance(instance, dbschema_ForeignKeyColumn)

@given(instance=dbschema_AttributeColumn_strategy)
@settings(max_examples=50)
def test_dbschema_attributecolumn_instantiation(instance):
    assert isinstance(instance, dbschema_AttributeColumn)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=dbschema_Table_strategy)
@settings(max_examples=50)
def test_dbschema_table_instantiation(instance):
    assert isinstance(instance, dbschema_Table)

@given(instance=dbschema_Column_strategy)
@settings(max_examples=50)
def test_dbschema_column_instantiation(instance):
    assert isinstance(instance, dbschema_Column)



@given(instance=dbschema_Column_strategy)
def test_dbschema_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=dbschema_Column_strategy)
def test_dbschema_column_primary_setter(instance):
    original = instance.primary
    instance.primary = original
    assert instance.primary == original



@given(instance=dbschema_Column_strategy)
def test_dbschema_column_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=dbschema_DBSchema_strategy)
@settings(max_examples=50)
def test_dbschema_dbschema_instantiation(instance):
    assert isinstance(instance, dbschema_DBSchema)

@given(instance=dbschema_NamedElement_strategy)
@settings(max_examples=50)
def test_dbschema_namedelement_instantiation(instance):
    assert isinstance(instance, dbschema_NamedElement)



@given(instance=dbschema_NamedElement_strategy)
def test_dbschema_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
