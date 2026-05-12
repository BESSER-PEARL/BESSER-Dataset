import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Column,
    DataBase,
    Table,
    NamedElement,
    RelationalDBSchema::Table,
    RelationalDBSchema::DataBase,
    RelationalDBSchema::NamedElement,
    RelationalDBSchema::Column,
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



def test_database_is_not_abstract():
    assert not inspect.isabstract(DataBase)


def test_database_constructor_exists():
    assert callable(DataBase.__init__)


def test_database_constructor_args():
    sig = inspect.signature(DataBase.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_relationaldbschema::table_is_not_abstract():
    assert not inspect.isabstract(RelationalDBSchema::Table)


def test_relationaldbschema::table_constructor_exists():
    assert callable(RelationalDBSchema::Table.__init__)


def test_relationaldbschema::table_constructor_args():
    sig = inspect.signature(RelationalDBSchema::Table.__init__)
    params = list(sig.parameters.keys())



def test_relationaldbschema::database_is_not_abstract():
    assert not inspect.isabstract(RelationalDBSchema::DataBase)


def test_relationaldbschema::database_constructor_exists():
    assert callable(RelationalDBSchema::DataBase.__init__)


def test_relationaldbschema::database_constructor_args():
    sig = inspect.signature(RelationalDBSchema::DataBase.__init__)
    params = list(sig.parameters.keys())
    assert "SGBDname" in params, "Missing parameter 'SGBDname'"

def test_relationaldbschema::database_has_SGBDname():
    assert hasattr(RelationalDBSchema::DataBase, "SGBDname")
    descriptor = None
    for klass in RelationalDBSchema::DataBase.__mro__:
        if "SGBDname" in klass.__dict__:
            descriptor = klass.__dict__["SGBDname"]
            break
    assert isinstance(descriptor, property)



def test_relationaldbschema::namedelement_is_not_abstract():
    assert not inspect.isabstract(RelationalDBSchema::NamedElement)


def test_relationaldbschema::namedelement_constructor_exists():
    assert callable(RelationalDBSchema::NamedElement.__init__)


def test_relationaldbschema::namedelement_constructor_args():
    sig = inspect.signature(RelationalDBSchema::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relationaldbschema::namedelement_has_name():
    assert hasattr(RelationalDBSchema::NamedElement, "name")
    descriptor = None
    for klass in RelationalDBSchema::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relationaldbschema::column_is_not_abstract():
    assert not inspect.isabstract(RelationalDBSchema::Column)


def test_relationaldbschema::column_constructor_exists():
    assert callable(RelationalDBSchema::Column.__init__)


def test_relationaldbschema::column_constructor_args():
    sig = inspect.signature(RelationalDBSchema::Column.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"
    assert "dataType" in params, "Missing parameter 'dataType'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_relationaldbschema::column_has_null():
    assert hasattr(RelationalDBSchema::Column, "null")
    descriptor = None
    for klass in RelationalDBSchema::Column.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)

def test_relationaldbschema::column_has_dataType():
    assert hasattr(RelationalDBSchema::Column, "dataType")
    descriptor = None
    for klass in RelationalDBSchema::Column.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)

def test_relationaldbschema::column_has_defaultValue():
    assert hasattr(RelationalDBSchema::Column, "defaultValue")
    descriptor = None
    for klass in RelationalDBSchema::Column.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)


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
DataBase_strategy = st.builds(
    DataBase,
)
Table_strategy = st.builds(
    Table,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
RelationalDBSchema::Table_strategy = st.builds(
    RelationalDBSchema::Table,
)
RelationalDBSchema::DataBase_strategy = st.builds(
    RelationalDBSchema::DataBase,
    SGBDname=
        safe_text
)
RelationalDBSchema::NamedElement_strategy = st.builds(
    RelationalDBSchema::NamedElement,
    name=
        safe_text
)
RelationalDBSchema::Column_strategy = st.builds(
    RelationalDBSchema::Column,
    null=
        safe_text,
    dataType=
        safe_text,
    defaultValue=
        safe_text
)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=DataBase_strategy)
@settings(max_examples=50)
def test_database_instantiation(instance):
    assert isinstance(instance, DataBase)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=RelationalDBSchema::Table_strategy)
@settings(max_examples=50)
def test_relationaldbschema::table_instantiation(instance):
    assert isinstance(instance, RelationalDBSchema::Table)

@given(instance=RelationalDBSchema::DataBase_strategy)
@settings(max_examples=50)
def test_relationaldbschema::database_instantiation(instance):
    assert isinstance(instance, RelationalDBSchema::DataBase)

@given(instance=RelationalDBSchema::DataBase_strategy)
def test_relationaldbschema::database_SGBDname_type(instance):
    assert isinstance(instance.SGBDname, str)


@given(instance=RelationalDBSchema::DataBase_strategy)
def test_relationaldbschema::database_SGBDname_setter(instance):
    original = instance.SGBDname
    instance.SGBDname = original
    assert instance.SGBDname == original

@given(instance=RelationalDBSchema::NamedElement_strategy)
@settings(max_examples=50)
def test_relationaldbschema::namedelement_instantiation(instance):
    assert isinstance(instance, RelationalDBSchema::NamedElement)

@given(instance=RelationalDBSchema::NamedElement_strategy)
def test_relationaldbschema::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RelationalDBSchema::NamedElement_strategy)
def test_relationaldbschema::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RelationalDBSchema::Column_strategy)
@settings(max_examples=50)
def test_relationaldbschema::column_instantiation(instance):
    assert isinstance(instance, RelationalDBSchema::Column)

@given(instance=RelationalDBSchema::Column_strategy)
def test_relationaldbschema::column_null_type(instance):
    assert isinstance(instance.null, str)


@given(instance=RelationalDBSchema::Column_strategy)
def test_relationaldbschema::column_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=RelationalDBSchema::Column_strategy)
def test_relationaldbschema::column_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=RelationalDBSchema::Column_strategy)
def test_relationaldbschema::column_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=RelationalDBSchema::Column_strategy)
def test_relationaldbschema::column_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=RelationalDBSchema::Column_strategy)
def test_relationaldbschema::column_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original
