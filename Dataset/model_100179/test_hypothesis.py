import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Column,
    DataBase,
    Table,
    NamedElement,
    RelationalDBSchema_Table,
    RelationalDBSchema_DataBase,
    RelationalDBSchema_NamedElement,
    RelationalDBSchema_Column,
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



def test_relationaldbschema_table_is_not_abstract():
    assert not inspect.isabstract(RelationalDBSchema_Table)


def test_relationaldbschema_table_constructor_exists():
    assert callable(RelationalDBSchema_Table.__init__)


def test_relationaldbschema_table_constructor_args():
    sig = inspect.signature(RelationalDBSchema_Table.__init__)
    params = list(sig.parameters.keys())



def test_relationaldbschema_database_is_not_abstract():
    assert not inspect.isabstract(RelationalDBSchema_DataBase)


def test_relationaldbschema_database_constructor_exists():
    assert callable(RelationalDBSchema_DataBase.__init__)


def test_relationaldbschema_database_constructor_args():
    sig = inspect.signature(RelationalDBSchema_DataBase.__init__)
    params = list(sig.parameters.keys())
    assert "SGBDname" in params, "Missing parameter 'SGBDname'"

def test_relationaldbschema_database_has_SGBDname():
    assert hasattr(RelationalDBSchema_DataBase, "SGBDname")
    descriptor = None
    for klass in RelationalDBSchema_DataBase.__mro__:
        if "SGBDname" in klass.__dict__:
            descriptor = klass.__dict__["SGBDname"]
            break
    assert isinstance(descriptor, property)



def test_relationaldbschema_namedelement_is_not_abstract():
    assert not inspect.isabstract(RelationalDBSchema_NamedElement)


def test_relationaldbschema_namedelement_constructor_exists():
    assert callable(RelationalDBSchema_NamedElement.__init__)


def test_relationaldbschema_namedelement_constructor_args():
    sig = inspect.signature(RelationalDBSchema_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relationaldbschema_namedelement_has_name():
    assert hasattr(RelationalDBSchema_NamedElement, "name")
    descriptor = None
    for klass in RelationalDBSchema_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relationaldbschema_column_is_not_abstract():
    assert not inspect.isabstract(RelationalDBSchema_Column)


def test_relationaldbschema_column_constructor_exists():
    assert callable(RelationalDBSchema_Column.__init__)


def test_relationaldbschema_column_constructor_args():
    sig = inspect.signature(RelationalDBSchema_Column.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_relationaldbschema_column_has_null():
    assert hasattr(RelationalDBSchema_Column, "null")
    descriptor = None
    for klass in RelationalDBSchema_Column.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)

def test_relationaldbschema_column_has_defaultValue():
    assert hasattr(RelationalDBSchema_Column, "defaultValue")
    descriptor = None
    for klass in RelationalDBSchema_Column.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_relationaldbschema_column_has_dataType():
    assert hasattr(RelationalDBSchema_Column, "dataType")
    descriptor = None
    for klass in RelationalDBSchema_Column.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
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
RelationalDBSchema_Table_strategy = st.builds(
    RelationalDBSchema_Table,
)
RelationalDBSchema_DataBase_strategy = st.builds(
    RelationalDBSchema_DataBase,
    SGBDname=
        safe_text
)
RelationalDBSchema_NamedElement_strategy = st.builds(
    RelationalDBSchema_NamedElement,
    name=
        safe_text
)
RelationalDBSchema_Column_strategy = st.builds(
    RelationalDBSchema_Column,
    null=
        safe_text,
    defaultValue=
        safe_text,
    dataType=
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

@given(instance=RelationalDBSchema_Table_strategy)
@settings(max_examples=50)
def test_relationaldbschema_table_instantiation(instance):
    assert isinstance(instance, RelationalDBSchema_Table)

@given(instance=RelationalDBSchema_DataBase_strategy)
@settings(max_examples=50)
def test_relationaldbschema_database_instantiation(instance):
    assert isinstance(instance, RelationalDBSchema_DataBase)



@given(instance=RelationalDBSchema_DataBase_strategy)
def test_relationaldbschema_database_SGBDname_setter(instance):
    original = instance.SGBDname
    instance.SGBDname = original
    assert instance.SGBDname == original

@given(instance=RelationalDBSchema_NamedElement_strategy)
@settings(max_examples=50)
def test_relationaldbschema_namedelement_instantiation(instance):
    assert isinstance(instance, RelationalDBSchema_NamedElement)



@given(instance=RelationalDBSchema_NamedElement_strategy)
def test_relationaldbschema_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RelationalDBSchema_Column_strategy)
@settings(max_examples=50)
def test_relationaldbschema_column_instantiation(instance):
    assert isinstance(instance, RelationalDBSchema_Column)



@given(instance=RelationalDBSchema_Column_strategy)
def test_relationaldbschema_column_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original



@given(instance=RelationalDBSchema_Column_strategy)
def test_relationaldbschema_column_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=RelationalDBSchema_Column_strategy)
def test_relationaldbschema_column_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original
