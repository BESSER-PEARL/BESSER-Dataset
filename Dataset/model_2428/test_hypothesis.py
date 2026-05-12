import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    database_Column,
    database_Table,
    database_ForeignKey,
    database_Database,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_database_column_is_not_abstract():
    assert not inspect.isabstract(database_Column)


def test_database_column_constructor_exists():
    assert callable(database_Column.__init__)


def test_database_column_constructor_args():
    sig = inspect.signature(database_Column.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "IsPrimaryKey" in params, "Missing parameter 'IsPrimaryKey'"

def test_database_column_has_Type():
    assert hasattr(database_Column, "Type")
    descriptor = None
    for klass in database_Column.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_database_column_has_Name():
    assert hasattr(database_Column, "Name")
    descriptor = None
    for klass in database_Column.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_database_column_has_IsPrimaryKey():
    assert hasattr(database_Column, "IsPrimaryKey")
    descriptor = None
    for klass in database_Column.__mro__:
        if "IsPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["IsPrimaryKey"]
            break
    assert isinstance(descriptor, property)



def test_database_table_is_not_abstract():
    assert not inspect.isabstract(database_Table)


def test_database_table_constructor_exists():
    assert callable(database_Table.__init__)


def test_database_table_constructor_args():
    sig = inspect.signature(database_Table.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_database_table_has_Name():
    assert hasattr(database_Table, "Name")
    descriptor = None
    for klass in database_Table.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_database_foreignkey_is_not_abstract():
    assert not inspect.isabstract(database_ForeignKey)


def test_database_foreignkey_constructor_exists():
    assert callable(database_ForeignKey.__init__)


def test_database_foreignkey_constructor_args():
    sig = inspect.signature(database_ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_database_foreignkey_has_Name():
    assert hasattr(database_ForeignKey, "Name")
    descriptor = None
    for klass in database_ForeignKey.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_database_database_is_not_abstract():
    assert not inspect.isabstract(database_Database)


def test_database_database_constructor_exists():
    assert callable(database_Database.__init__)


def test_database_database_constructor_args():
    sig = inspect.signature(database_Database.__init__)
    params = list(sig.parameters.keys())

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "String",
        "Date",
        "Int",
        "Float",
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
database_Column_strategy = st.builds(
    database_Column,
    Type=
        safe_text,
    Name=
        safe_text,
    IsPrimaryKey=
        st.booleans()
)
database_Table_strategy = st.builds(
    database_Table,
    Name=
        safe_text
)
database_ForeignKey_strategy = st.builds(
    database_ForeignKey,
    Name=
        safe_text
)
database_Database_strategy = st.builds(
    database_Database,
)

@given(instance=database_Column_strategy)
@settings(max_examples=50)
def test_database_column_instantiation(instance):
    assert isinstance(instance, database_Column)



@given(instance=database_Column_strategy)
def test_database_column_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=database_Column_strategy)
def test_database_column_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=database_Column_strategy)
def test_database_column_IsPrimaryKey_setter(instance):
    original = instance.IsPrimaryKey
    instance.IsPrimaryKey = original
    assert instance.IsPrimaryKey == original

@given(instance=database_Table_strategy)
@settings(max_examples=50)
def test_database_table_instantiation(instance):
    assert isinstance(instance, database_Table)



@given(instance=database_Table_strategy)
def test_database_table_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=database_ForeignKey_strategy)
@settings(max_examples=50)
def test_database_foreignkey_instantiation(instance):
    assert isinstance(instance, database_ForeignKey)



@given(instance=database_ForeignKey_strategy)
def test_database_foreignkey_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=database_Database_strategy)
@settings(max_examples=50)
def test_database_database_instantiation(instance):
    assert isinstance(instance, database_Database)
