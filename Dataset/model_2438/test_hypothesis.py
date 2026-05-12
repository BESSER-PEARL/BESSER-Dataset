import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sql_ForeignKey,
    sql_PrimaryKey,
    sql_Column,
    sql_EObject,
    sql_Table,
    sql_Database,
    sql_Model,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sql_foreignkey_is_not_abstract():
    assert not inspect.isabstract(sql_ForeignKey)


def test_sql_foreignkey_constructor_exists():
    assert callable(sql_ForeignKey.__init__)


def test_sql_foreignkey_constructor_args():
    sig = inspect.signature(sql_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_sql_primarykey_is_not_abstract():
    assert not inspect.isabstract(sql_PrimaryKey)


def test_sql_primarykey_constructor_exists():
    assert callable(sql_PrimaryKey.__init__)


def test_sql_primarykey_constructor_args():
    sig = inspect.signature(sql_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_sql_column_is_not_abstract():
    assert not inspect.isabstract(sql_Column)


def test_sql_column_constructor_exists():
    assert callable(sql_Column.__init__)


def test_sql_column_constructor_args():
    sig = inspect.signature(sql_Column.__init__)
    params = list(sig.parameters.keys())
    assert "isNotNull" in params, "Missing parameter 'isNotNull'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_sql_column_has_isNotNull():
    assert hasattr(sql_Column, "isNotNull")
    descriptor = None
    for klass in sql_Column.__mro__:
        if "isNotNull" in klass.__dict__:
            descriptor = klass.__dict__["isNotNull"]
            break
    assert isinstance(descriptor, property)

def test_sql_column_has_type():
    assert hasattr(sql_Column, "type")
    descriptor = None
    for klass in sql_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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



def test_sql_eobject_is_not_abstract():
    assert not inspect.isabstract(sql_EObject)


def test_sql_eobject_constructor_exists():
    assert callable(sql_EObject.__init__)


def test_sql_eobject_constructor_args():
    sig = inspect.signature(sql_EObject.__init__)
    params = list(sig.parameters.keys())



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



def test_sql_model_is_not_abstract():
    assert not inspect.isabstract(sql_Model)


def test_sql_model_constructor_exists():
    assert callable(sql_Model.__init__)


def test_sql_model_constructor_args():
    sig = inspect.signature(sql_Model.__init__)
    params = list(sig.parameters.keys())

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "INT",
        "VARCHAR255",
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
sql_ForeignKey_strategy = st.builds(
    sql_ForeignKey,
)
sql_PrimaryKey_strategy = st.builds(
    sql_PrimaryKey,
)
sql_Column_strategy = st.builds(
    sql_Column,
    isNotNull=
        st.booleans(),
    type=
        safe_text,
    name=
        safe_text
)
sql_EObject_strategy = st.builds(
    sql_EObject,
)
sql_Table_strategy = st.builds(
    sql_Table,
    name=
        safe_text
)
sql_Database_strategy = st.builds(
    sql_Database,
)
sql_Model_strategy = st.builds(
    sql_Model,
)

@given(instance=sql_ForeignKey_strategy)
@settings(max_examples=50)
def test_sql_foreignkey_instantiation(instance):
    assert isinstance(instance, sql_ForeignKey)

@given(instance=sql_PrimaryKey_strategy)
@settings(max_examples=50)
def test_sql_primarykey_instantiation(instance):
    assert isinstance(instance, sql_PrimaryKey)

@given(instance=sql_Column_strategy)
@settings(max_examples=50)
def test_sql_column_instantiation(instance):
    assert isinstance(instance, sql_Column)



@given(instance=sql_Column_strategy)
def test_sql_column_isNotNull_setter(instance):
    original = instance.isNotNull
    instance.isNotNull = original
    assert instance.isNotNull == original



@given(instance=sql_Column_strategy)
def test_sql_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=sql_Column_strategy)
def test_sql_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sql_EObject_strategy)
@settings(max_examples=50)
def test_sql_eobject_instantiation(instance):
    assert isinstance(instance, sql_EObject)

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

@given(instance=sql_Model_strategy)
@settings(max_examples=50)
def test_sql_model_instantiation(instance):
    assert isinstance(instance, sql_Model)
