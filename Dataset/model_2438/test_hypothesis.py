import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sql::ForeignKey,
    sql::PrimaryKey,
    sql::Column,
    sql::EObject,
    sql::Table,
    sql::Database,
    sql::Model,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sql::foreignkey_is_not_abstract():
    assert not inspect.isabstract(sql::ForeignKey)


def test_sql::foreignkey_constructor_exists():
    assert callable(sql::ForeignKey.__init__)


def test_sql::foreignkey_constructor_args():
    sig = inspect.signature(sql::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_sql::primarykey_is_not_abstract():
    assert not inspect.isabstract(sql::PrimaryKey)


def test_sql::primarykey_constructor_exists():
    assert callable(sql::PrimaryKey.__init__)


def test_sql::primarykey_constructor_args():
    sig = inspect.signature(sql::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_sql::column_is_not_abstract():
    assert not inspect.isabstract(sql::Column)


def test_sql::column_constructor_exists():
    assert callable(sql::Column.__init__)


def test_sql::column_constructor_args():
    sig = inspect.signature(sql::Column.__init__)
    params = list(sig.parameters.keys())
    assert "isNotNull" in params, "Missing parameter 'isNotNull'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_sql::column_has_isNotNull():
    assert hasattr(sql::Column, "isNotNull")
    descriptor = None
    for klass in sql::Column.__mro__:
        if "isNotNull" in klass.__dict__:
            descriptor = klass.__dict__["isNotNull"]
            break
    assert isinstance(descriptor, property)

def test_sql::column_has_name():
    assert hasattr(sql::Column, "name")
    descriptor = None
    for klass in sql::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sql::column_has_type():
    assert hasattr(sql::Column, "type")
    descriptor = None
    for klass in sql::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_sql::eobject_is_not_abstract():
    assert not inspect.isabstract(sql::EObject)


def test_sql::eobject_constructor_exists():
    assert callable(sql::EObject.__init__)


def test_sql::eobject_constructor_args():
    sig = inspect.signature(sql::EObject.__init__)
    params = list(sig.parameters.keys())



def test_sql::table_is_not_abstract():
    assert not inspect.isabstract(sql::Table)


def test_sql::table_constructor_exists():
    assert callable(sql::Table.__init__)


def test_sql::table_constructor_args():
    sig = inspect.signature(sql::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql::table_has_name():
    assert hasattr(sql::Table, "name")
    descriptor = None
    for klass in sql::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql::database_is_not_abstract():
    assert not inspect.isabstract(sql::Database)


def test_sql::database_constructor_exists():
    assert callable(sql::Database.__init__)


def test_sql::database_constructor_args():
    sig = inspect.signature(sql::Database.__init__)
    params = list(sig.parameters.keys())



def test_sql::model_is_not_abstract():
    assert not inspect.isabstract(sql::Model)


def test_sql::model_constructor_exists():
    assert callable(sql::Model.__init__)


def test_sql::model_constructor_args():
    sig = inspect.signature(sql::Model.__init__)
    params = list(sig.parameters.keys())

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "VARCHAR255",
        "INT",
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
sql::ForeignKey_strategy = st.builds(
    sql::ForeignKey,
)
sql::PrimaryKey_strategy = st.builds(
    sql::PrimaryKey,
)
sql::Column_strategy = st.builds(
    sql::Column,
    isNotNull=
        st.booleans(),
    name=
        safe_text,
    type=
        safe_text
)
sql::EObject_strategy = st.builds(
    sql::EObject,
)
sql::Table_strategy = st.builds(
    sql::Table,
    name=
        safe_text
)
sql::Database_strategy = st.builds(
    sql::Database,
)
sql::Model_strategy = st.builds(
    sql::Model,
)

@given(instance=sql::ForeignKey_strategy)
@settings(max_examples=50)
def test_sql::foreignkey_instantiation(instance):
    assert isinstance(instance, sql::ForeignKey)

@given(instance=sql::PrimaryKey_strategy)
@settings(max_examples=50)
def test_sql::primarykey_instantiation(instance):
    assert isinstance(instance, sql::PrimaryKey)

@given(instance=sql::Column_strategy)
@settings(max_examples=50)
def test_sql::column_instantiation(instance):
    assert isinstance(instance, sql::Column)

@given(instance=sql::Column_strategy)
def test_sql::column_isNotNull_type(instance):
    assert isinstance(instance.isNotNull, bool)


@given(instance=sql::Column_strategy)
def test_sql::column_isNotNull_setter(instance):
    original = instance.isNotNull
    instance.isNotNull = original
    assert instance.isNotNull == original

@given(instance=sql::Column_strategy)
def test_sql::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sql::Column_strategy)
def test_sql::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sql::Column_strategy)
def test_sql::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=sql::Column_strategy)
def test_sql::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sql::EObject_strategy)
@settings(max_examples=50)
def test_sql::eobject_instantiation(instance):
    assert isinstance(instance, sql::EObject)

@given(instance=sql::Table_strategy)
@settings(max_examples=50)
def test_sql::table_instantiation(instance):
    assert isinstance(instance, sql::Table)

@given(instance=sql::Table_strategy)
def test_sql::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sql::Table_strategy)
def test_sql::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sql::Database_strategy)
@settings(max_examples=50)
def test_sql::database_instantiation(instance):
    assert isinstance(instance, sql::Database)

@given(instance=sql::Model_strategy)
@settings(max_examples=50)
def test_sql::model_instantiation(instance):
    assert isinstance(instance, sql::Model)
