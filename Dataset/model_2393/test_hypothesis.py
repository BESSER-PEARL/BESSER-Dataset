import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sQL_ForeignKey,
    sQL_PrimaryKey,
    sQL_Column,
    sQL_Table,
    sQL_DataBase,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sql_foreignkey_is_not_abstract():
    assert not inspect.isabstract(sQL_ForeignKey)


def test_sql_foreignkey_constructor_exists():
    assert callable(sQL_ForeignKey.__init__)


def test_sql_foreignkey_constructor_args():
    sig = inspect.signature(sQL_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_sql_primarykey_is_not_abstract():
    assert not inspect.isabstract(sQL_PrimaryKey)


def test_sql_primarykey_constructor_exists():
    assert callable(sQL_PrimaryKey.__init__)


def test_sql_primarykey_constructor_args():
    sig = inspect.signature(sQL_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_sql_column_is_not_abstract():
    assert not inspect.isabstract(sQL_Column)


def test_sql_column_constructor_exists():
    assert callable(sQL_Column.__init__)


def test_sql_column_constructor_args():
    sig = inspect.signature(sQL_Column.__init__)
    params = list(sig.parameters.keys())
    assert "isNull" in params, "Missing parameter 'isNull'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_sql_column_has_isNull():
    assert hasattr(sQL_Column, "isNull")
    descriptor = None
    for klass in sQL_Column.__mro__:
        if "isNull" in klass.__dict__:
            descriptor = klass.__dict__["isNull"]
            break
    assert isinstance(descriptor, property)

def test_sql_column_has_name():
    assert hasattr(sQL_Column, "name")
    descriptor = None
    for klass in sQL_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sql_column_has_type():
    assert hasattr(sQL_Column, "type")
    descriptor = None
    for klass in sQL_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



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

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "boolean",
        "int",
        "number",
        "date",
        "varchar",
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
sQL_ForeignKey_strategy = st.builds(
    sQL_ForeignKey,
)
sQL_PrimaryKey_strategy = st.builds(
    sQL_PrimaryKey,
)
sQL_Column_strategy = st.builds(
    sQL_Column,
    isNull=
        st.booleans(),
    name=
        safe_text,
    type=
        safe_text
)
sQL_Table_strategy = st.builds(
    sQL_Table,
    name=
        safe_text
)
sQL_DataBase_strategy = st.builds(
    sQL_DataBase,
)

@given(instance=sQL_ForeignKey_strategy)
@settings(max_examples=50)
def test_sql_foreignkey_instantiation(instance):
    assert isinstance(instance, sQL_ForeignKey)

@given(instance=sQL_PrimaryKey_strategy)
@settings(max_examples=50)
def test_sql_primarykey_instantiation(instance):
    assert isinstance(instance, sQL_PrimaryKey)

@given(instance=sQL_Column_strategy)
@settings(max_examples=50)
def test_sql_column_instantiation(instance):
    assert isinstance(instance, sQL_Column)



@given(instance=sQL_Column_strategy)
def test_sql_column_isNull_setter(instance):
    original = instance.isNull
    instance.isNull = original
    assert instance.isNull == original



@given(instance=sQL_Column_strategy)
def test_sql_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sQL_Column_strategy)
def test_sql_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

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
