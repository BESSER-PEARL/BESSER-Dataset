import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    database::Table,
    database::ForeignKey,
    database::Database,
    database::Column,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_database::table_is_not_abstract():
    assert not inspect.isabstract(database::Table)


def test_database::table_constructor_exists():
    assert callable(database::Table.__init__)


def test_database::table_constructor_args():
    sig = inspect.signature(database::Table.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_database::table_has_Name():
    assert hasattr(database::Table, "Name")
    descriptor = None
    for klass in database::Table.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_database::foreignkey_is_not_abstract():
    assert not inspect.isabstract(database::ForeignKey)


def test_database::foreignkey_constructor_exists():
    assert callable(database::ForeignKey.__init__)


def test_database::foreignkey_constructor_args():
    sig = inspect.signature(database::ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_database::foreignkey_has_Name():
    assert hasattr(database::ForeignKey, "Name")
    descriptor = None
    for klass in database::ForeignKey.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_database::database_is_not_abstract():
    assert not inspect.isabstract(database::Database)


def test_database::database_constructor_exists():
    assert callable(database::Database.__init__)


def test_database::database_constructor_args():
    sig = inspect.signature(database::Database.__init__)
    params = list(sig.parameters.keys())



def test_database::column_is_not_abstract():
    assert not inspect.isabstract(database::Column)


def test_database::column_constructor_exists():
    assert callable(database::Column.__init__)


def test_database::column_constructor_args():
    sig = inspect.signature(database::Column.__init__)
    params = list(sig.parameters.keys())
    assert "IsPrimaryKey" in params, "Missing parameter 'IsPrimaryKey'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_database::column_has_IsPrimaryKey():
    assert hasattr(database::Column, "IsPrimaryKey")
    descriptor = None
    for klass in database::Column.__mro__:
        if "IsPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["IsPrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_database::column_has_Name():
    assert hasattr(database::Column, "Name")
    descriptor = None
    for klass in database::Column.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_database::column_has_Type():
    assert hasattr(database::Column, "Type")
    descriptor = None
    for klass in database::Column.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "Int",
        "Date",
        "Float",
        "String",
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
database::Table_strategy = st.builds(
    database::Table,
    Name=
        safe_text
)
database::ForeignKey_strategy = st.builds(
    database::ForeignKey,
    Name=
        safe_text
)
database::Database_strategy = st.builds(
    database::Database,
)
database::Column_strategy = st.builds(
    database::Column,
    IsPrimaryKey=
        st.booleans(),
    Name=
        safe_text,
    Type=
        safe_text
)

@given(instance=database::Table_strategy)
@settings(max_examples=50)
def test_database::table_instantiation(instance):
    assert isinstance(instance, database::Table)

@given(instance=database::Table_strategy)
def test_database::table_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=database::Table_strategy)
def test_database::table_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=database::ForeignKey_strategy)
@settings(max_examples=50)
def test_database::foreignkey_instantiation(instance):
    assert isinstance(instance, database::ForeignKey)

@given(instance=database::ForeignKey_strategy)
def test_database::foreignkey_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=database::ForeignKey_strategy)
def test_database::foreignkey_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=database::Database_strategy)
@settings(max_examples=50)
def test_database::database_instantiation(instance):
    assert isinstance(instance, database::Database)

@given(instance=database::Column_strategy)
@settings(max_examples=50)
def test_database::column_instantiation(instance):
    assert isinstance(instance, database::Column)

@given(instance=database::Column_strategy)
def test_database::column_IsPrimaryKey_type(instance):
    assert isinstance(instance.IsPrimaryKey, bool)


@given(instance=database::Column_strategy)
def test_database::column_IsPrimaryKey_setter(instance):
    original = instance.IsPrimaryKey
    instance.IsPrimaryKey = original
    assert instance.IsPrimaryKey == original

@given(instance=database::Column_strategy)
def test_database::column_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=database::Column_strategy)
def test_database::column_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=database::Column_strategy)
def test_database::column_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=database::Column_strategy)
def test_database::column_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original
