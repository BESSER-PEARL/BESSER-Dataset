import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sQL::Table,
    sQL::DataBase,
    sQL::foreignKey,
    sQL::primaryKey,
    sQL::column,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sql::table_is_not_abstract():
    assert not inspect.isabstract(sQL::Table)


def test_sql::table_constructor_exists():
    assert callable(sQL::Table.__init__)


def test_sql::table_constructor_args():
    sig = inspect.signature(sQL::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql::table_has_name():
    assert hasattr(sQL::Table, "name")
    descriptor = None
    for klass in sQL::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql::database_is_not_abstract():
    assert not inspect.isabstract(sQL::DataBase)


def test_sql::database_constructor_exists():
    assert callable(sQL::DataBase.__init__)


def test_sql::database_constructor_args():
    sig = inspect.signature(sQL::DataBase.__init__)
    params = list(sig.parameters.keys())



def test_sql::foreignkey_is_not_abstract():
    assert not inspect.isabstract(sQL::foreignKey)


def test_sql::foreignkey_constructor_exists():
    assert callable(sQL::foreignKey.__init__)


def test_sql::foreignkey_constructor_args():
    sig = inspect.signature(sQL::foreignKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql::foreignkey_has_name():
    assert hasattr(sQL::foreignKey, "name")
    descriptor = None
    for klass in sQL::foreignKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql::primarykey_is_not_abstract():
    assert not inspect.isabstract(sQL::primaryKey)


def test_sql::primarykey_constructor_exists():
    assert callable(sQL::primaryKey.__init__)


def test_sql::primarykey_constructor_args():
    sig = inspect.signature(sQL::primaryKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql::primarykey_has_name():
    assert hasattr(sQL::primaryKey, "name")
    descriptor = None
    for klass in sQL::primaryKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql::column_is_not_abstract():
    assert not inspect.isabstract(sQL::column)


def test_sql::column_constructor_exists():
    assert callable(sQL::column.__init__)


def test_sql::column_constructor_args():
    sig = inspect.signature(sQL::column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_sql::column_has_name():
    assert hasattr(sQL::column, "name")
    descriptor = None
    for klass in sQL::column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sql::column_has_type():
    assert hasattr(sQL::column, "type")
    descriptor = None
    for klass in sQL::column.__mro__:
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
        "NUMERIC",
        "VARCHAR255",
        "DECIMAL",
        "VARCHAR",
        "DATE",
        "FLOAT",
        "CHAR",
        "TIME",
        "INT",
        "BOOL",
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
sQL::Table_strategy = st.builds(
    sQL::Table,
    name=
        safe_text
)
sQL::DataBase_strategy = st.builds(
    sQL::DataBase,
)
sQL::foreignKey_strategy = st.builds(
    sQL::foreignKey,
    name=
        safe_text
)
sQL::primaryKey_strategy = st.builds(
    sQL::primaryKey,
    name=
        safe_text
)
sQL::column_strategy = st.builds(
    sQL::column,
    name=
        safe_text,
    type=
        safe_text
)

@given(instance=sQL::Table_strategy)
@settings(max_examples=50)
def test_sql::table_instantiation(instance):
    assert isinstance(instance, sQL::Table)

@given(instance=sQL::Table_strategy)
def test_sql::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sQL::Table_strategy)
def test_sql::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sQL::DataBase_strategy)
@settings(max_examples=50)
def test_sql::database_instantiation(instance):
    assert isinstance(instance, sQL::DataBase)

@given(instance=sQL::foreignKey_strategy)
@settings(max_examples=50)
def test_sql::foreignkey_instantiation(instance):
    assert isinstance(instance, sQL::foreignKey)

@given(instance=sQL::foreignKey_strategy)
def test_sql::foreignkey_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sQL::foreignKey_strategy)
def test_sql::foreignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sQL::primaryKey_strategy)
@settings(max_examples=50)
def test_sql::primarykey_instantiation(instance):
    assert isinstance(instance, sQL::primaryKey)

@given(instance=sQL::primaryKey_strategy)
def test_sql::primarykey_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sQL::primaryKey_strategy)
def test_sql::primarykey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sQL::column_strategy)
@settings(max_examples=50)
def test_sql::column_instantiation(instance):
    assert isinstance(instance, sQL::column)

@given(instance=sQL::column_strategy)
def test_sql::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sQL::column_strategy)
def test_sql::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sQL::column_strategy)
def test_sql::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=sQL::column_strategy)
def test_sql::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
