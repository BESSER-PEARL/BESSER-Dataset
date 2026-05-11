import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sQL::ForeignKey,
    sQL::PrimaryKey,
    sQL::Column,
    sQL::Table,
    sQL::DataBase,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sql::foreignkey_is_not_abstract():
    assert not inspect.isabstract(sQL::ForeignKey)


def test_sql::foreignkey_constructor_exists():
    assert callable(sQL::ForeignKey.__init__)


def test_sql::foreignkey_constructor_args():
    sig = inspect.signature(sQL::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_sql::primarykey_is_not_abstract():
    assert not inspect.isabstract(sQL::PrimaryKey)


def test_sql::primarykey_constructor_exists():
    assert callable(sQL::PrimaryKey.__init__)


def test_sql::primarykey_constructor_args():
    sig = inspect.signature(sQL::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_sql::column_is_not_abstract():
    assert not inspect.isabstract(sQL::Column)


def test_sql::column_constructor_exists():
    assert callable(sQL::Column.__init__)


def test_sql::column_constructor_args():
    sig = inspect.signature(sQL::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "isNull" in params, "Missing parameter 'isNull'"
    assert "name" in params, "Missing parameter 'name'"

def test_sql::column_has_type():
    assert hasattr(sQL::Column, "type")
    descriptor = None
    for klass in sQL::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_sql::column_has_isNull():
    assert hasattr(sQL::Column, "isNull")
    descriptor = None
    for klass in sQL::Column.__mro__:
        if "isNull" in klass.__dict__:
            descriptor = klass.__dict__["isNull"]
            break
    assert isinstance(descriptor, property)

def test_sql::column_has_name():
    assert hasattr(sQL::Column, "name")
    descriptor = None
    for klass in sQL::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "number",
        "int",
        "boolean",
        "varchar",
        "date",
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
sQL::ForeignKey_strategy = st.builds(
    sQL::ForeignKey,
)
sQL::PrimaryKey_strategy = st.builds(
    sQL::PrimaryKey,
)
sQL::Column_strategy = st.builds(
    sQL::Column,
    type=
        safe_text,
    isNull=
        st.booleans(),
    name=
        safe_text
)
sQL::Table_strategy = st.builds(
    sQL::Table,
    name=
        safe_text
)
sQL::DataBase_strategy = st.builds(
    sQL::DataBase,
)

@given(instance=sQL::ForeignKey_strategy)
@settings(max_examples=50)
def test_sql::foreignkey_instantiation(instance):
    assert isinstance(instance, sQL::ForeignKey)

@given(instance=sQL::PrimaryKey_strategy)
@settings(max_examples=50)
def test_sql::primarykey_instantiation(instance):
    assert isinstance(instance, sQL::PrimaryKey)

@given(instance=sQL::Column_strategy)
@settings(max_examples=50)
def test_sql::column_instantiation(instance):
    assert isinstance(instance, sQL::Column)

@given(instance=sQL::Column_strategy)
def test_sql::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=sQL::Column_strategy)
def test_sql::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sQL::Column_strategy)
def test_sql::column_isNull_type(instance):
    assert isinstance(instance.isNull, bool)


@given(instance=sQL::Column_strategy)
def test_sql::column_isNull_setter(instance):
    original = instance.isNull
    instance.isNull = original
    assert instance.isNull == original

@given(instance=sQL::Column_strategy)
def test_sql::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sQL::Column_strategy)
def test_sql::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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
