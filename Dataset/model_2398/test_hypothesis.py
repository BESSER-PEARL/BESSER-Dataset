import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sQL::Column,
    sQL::Table,
    sQL::Database,
    sQL::ForeignKey,
    sQL::PrimaryKey,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sql::column_is_not_abstract():
    assert not inspect.isabstract(sQL::Column)


def test_sql::column_constructor_exists():
    assert callable(sQL::Column.__init__)


def test_sql::column_constructor_args():
    sig = inspect.signature(sQL::Column.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"
    assert "notNull" in params, "Missing parameter 'notNull'"
    assert "name" in params, "Missing parameter 'name'"

def test_sql::column_has_dataType():
    assert hasattr(sQL::Column, "dataType")
    descriptor = None
    for klass in sQL::Column.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)

def test_sql::column_has_notNull():
    assert hasattr(sQL::Column, "notNull")
    descriptor = None
    for klass in sQL::Column.__mro__:
        if "notNull" in klass.__dict__:
            descriptor = klass.__dict__["notNull"]
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
    assert not inspect.isabstract(sQL::Database)


def test_sql::database_constructor_exists():
    assert callable(sQL::Database.__init__)


def test_sql::database_constructor_args():
    sig = inspect.signature(sQL::Database.__init__)
    params = list(sig.parameters.keys())



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
sQL::Column_strategy = st.builds(
    sQL::Column,
    dataType=
        safe_text,
    notNull=
        safe_text,
    name=
        safe_text
)
sQL::Table_strategy = st.builds(
    sQL::Table,
    name=
        safe_text
)
sQL::Database_strategy = st.builds(
    sQL::Database,
)
sQL::ForeignKey_strategy = st.builds(
    sQL::ForeignKey,
)
sQL::PrimaryKey_strategy = st.builds(
    sQL::PrimaryKey,
)

@given(instance=sQL::Column_strategy)
@settings(max_examples=50)
def test_sql::column_instantiation(instance):
    assert isinstance(instance, sQL::Column)

@given(instance=sQL::Column_strategy)
def test_sql::column_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=sQL::Column_strategy)
def test_sql::column_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=sQL::Column_strategy)
def test_sql::column_notNull_type(instance):
    assert isinstance(instance.notNull, str)


@given(instance=sQL::Column_strategy)
def test_sql::column_notNull_setter(instance):
    original = instance.notNull
    instance.notNull = original
    assert instance.notNull == original

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

@given(instance=sQL::Database_strategy)
@settings(max_examples=50)
def test_sql::database_instantiation(instance):
    assert isinstance(instance, sQL::Database)

@given(instance=sQL::ForeignKey_strategy)
@settings(max_examples=50)
def test_sql::foreignkey_instantiation(instance):
    assert isinstance(instance, sQL::ForeignKey)

@given(instance=sQL::PrimaryKey_strategy)
@settings(max_examples=50)
def test_sql::primarykey_instantiation(instance):
    assert isinstance(instance, sQL::PrimaryKey)
