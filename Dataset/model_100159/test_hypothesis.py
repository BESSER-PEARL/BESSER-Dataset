import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    EnumItem,
    MySQL_EnumSet,
    EnumSet,
    MySQL_NamedElement,
    DataBase,
    Column,
    MySQL_IntegerColumn,
    MySQL_EnumColumn,
    Table,
    NamedElement,
    MySQL_Column,
    MySQL_EnumItem,
    MySQL_Table,
    MySQL_DataBase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_enumitem_is_not_abstract():
    assert not inspect.isabstract(EnumItem)


def test_enumitem_constructor_exists():
    assert callable(EnumItem.__init__)


def test_enumitem_constructor_args():
    sig = inspect.signature(EnumItem.__init__)
    params = list(sig.parameters.keys())



def test_mysql_enumset_is_not_abstract():
    assert not inspect.isabstract(MySQL_EnumSet)


def test_mysql_enumset_constructor_exists():
    assert callable(MySQL_EnumSet.__init__)


def test_mysql_enumset_constructor_args():
    sig = inspect.signature(MySQL_EnumSet.__init__)
    params = list(sig.parameters.keys())



def test_enumset_is_not_abstract():
    assert not inspect.isabstract(EnumSet)


def test_enumset_constructor_exists():
    assert callable(EnumSet.__init__)


def test_enumset_constructor_args():
    sig = inspect.signature(EnumSet.__init__)
    params = list(sig.parameters.keys())



def test_mysql_namedelement_is_not_abstract():
    assert not inspect.isabstract(MySQL_NamedElement)


def test_mysql_namedelement_constructor_exists():
    assert callable(MySQL_NamedElement.__init__)


def test_mysql_namedelement_constructor_args():
    sig = inspect.signature(MySQL_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mysql_namedelement_has_name():
    assert hasattr(MySQL_NamedElement, "name")
    descriptor = None
    for klass in MySQL_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_database_is_not_abstract():
    assert not inspect.isabstract(DataBase)


def test_database_constructor_exists():
    assert callable(DataBase.__init__)


def test_database_constructor_args():
    sig = inspect.signature(DataBase.__init__)
    params = list(sig.parameters.keys())



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_mysql_integercolumn_is_not_abstract():
    assert not inspect.isabstract(MySQL_IntegerColumn)


def test_mysql_integercolumn_constructor_exists():
    assert callable(MySQL_IntegerColumn.__init__)


def test_mysql_integercolumn_constructor_args():
    sig = inspect.signature(MySQL_IntegerColumn.__init__)
    params = list(sig.parameters.keys())
    assert "isAutoIncrement" in params, "Missing parameter 'isAutoIncrement'"

def test_mysql_integercolumn_has_isAutoIncrement():
    assert hasattr(MySQL_IntegerColumn, "isAutoIncrement")
    descriptor = None
    for klass in MySQL_IntegerColumn.__mro__:
        if "isAutoIncrement" in klass.__dict__:
            descriptor = klass.__dict__["isAutoIncrement"]
            break
    assert isinstance(descriptor, property)



def test_mysql_enumcolumn_is_not_abstract():
    assert not inspect.isabstract(MySQL_EnumColumn)


def test_mysql_enumcolumn_constructor_exists():
    assert callable(MySQL_EnumColumn.__init__)


def test_mysql_enumcolumn_constructor_args():
    sig = inspect.signature(MySQL_EnumColumn.__init__)
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



def test_mysql_column_is_not_abstract():
    assert not inspect.isabstract(MySQL_Column)


def test_mysql_column_constructor_exists():
    assert callable(MySQL_Column.__init__)


def test_mysql_column_constructor_args():
    sig = inspect.signature(MySQL_Column.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "type" in params, "Missing parameter 'type'"
    assert "null" in params, "Missing parameter 'null'"
    assert "isPrimaryKey" in params, "Missing parameter 'isPrimaryKey'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_mysql_column_has_defaultValue():
    assert hasattr(MySQL_Column, "defaultValue")
    descriptor = None
    for klass in MySQL_Column.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_mysql_column_has_type():
    assert hasattr(MySQL_Column, "type")
    descriptor = None
    for klass in MySQL_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mysql_column_has_null():
    assert hasattr(MySQL_Column, "null")
    descriptor = None
    for klass in MySQL_Column.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)

def test_mysql_column_has_isPrimaryKey():
    assert hasattr(MySQL_Column, "isPrimaryKey")
    descriptor = None
    for klass in MySQL_Column.__mro__:
        if "isPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_mysql_column_has_comment():
    assert hasattr(MySQL_Column, "comment")
    descriptor = None
    for klass in MySQL_Column.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_mysql_enumitem_is_not_abstract():
    assert not inspect.isabstract(MySQL_EnumItem)


def test_mysql_enumitem_constructor_exists():
    assert callable(MySQL_EnumItem.__init__)


def test_mysql_enumitem_constructor_args():
    sig = inspect.signature(MySQL_EnumItem.__init__)
    params = list(sig.parameters.keys())



def test_mysql_table_is_not_abstract():
    assert not inspect.isabstract(MySQL_Table)


def test_mysql_table_constructor_exists():
    assert callable(MySQL_Table.__init__)


def test_mysql_table_constructor_args():
    sig = inspect.signature(MySQL_Table.__init__)
    params = list(sig.parameters.keys())



def test_mysql_database_is_not_abstract():
    assert not inspect.isabstract(MySQL_DataBase)


def test_mysql_database_constructor_exists():
    assert callable(MySQL_DataBase.__init__)


def test_mysql_database_constructor_args():
    sig = inspect.signature(MySQL_DataBase.__init__)
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
EnumItem_strategy = st.builds(
    EnumItem,
)
MySQL_EnumSet_strategy = st.builds(
    MySQL_EnumSet,
)
EnumSet_strategy = st.builds(
    EnumSet,
)
MySQL_NamedElement_strategy = st.builds(
    MySQL_NamedElement,
    name=
        safe_text
)
DataBase_strategy = st.builds(
    DataBase,
)
Column_strategy = st.builds(
    Column,
)
MySQL_IntegerColumn_strategy = st.builds(
    MySQL_IntegerColumn,
    isAutoIncrement=
        safe_text
)
MySQL_EnumColumn_strategy = st.builds(
    MySQL_EnumColumn,
)
Table_strategy = st.builds(
    Table,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
MySQL_Column_strategy = st.builds(
    MySQL_Column,
    defaultValue=
        safe_text,
    type=
        safe_text,
    null=
        safe_text,
    isPrimaryKey=
        safe_text,
    comment=
        safe_text
)
MySQL_EnumItem_strategy = st.builds(
    MySQL_EnumItem,
)
MySQL_Table_strategy = st.builds(
    MySQL_Table,
)
MySQL_DataBase_strategy = st.builds(
    MySQL_DataBase,
)

@given(instance=EnumItem_strategy)
@settings(max_examples=50)
def test_enumitem_instantiation(instance):
    assert isinstance(instance, EnumItem)

@given(instance=MySQL_EnumSet_strategy)
@settings(max_examples=50)
def test_mysql_enumset_instantiation(instance):
    assert isinstance(instance, MySQL_EnumSet)

@given(instance=EnumSet_strategy)
@settings(max_examples=50)
def test_enumset_instantiation(instance):
    assert isinstance(instance, EnumSet)

@given(instance=MySQL_NamedElement_strategy)
@settings(max_examples=50)
def test_mysql_namedelement_instantiation(instance):
    assert isinstance(instance, MySQL_NamedElement)



@given(instance=MySQL_NamedElement_strategy)
def test_mysql_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DataBase_strategy)
@settings(max_examples=50)
def test_database_instantiation(instance):
    assert isinstance(instance, DataBase)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=MySQL_IntegerColumn_strategy)
@settings(max_examples=50)
def test_mysql_integercolumn_instantiation(instance):
    assert isinstance(instance, MySQL_IntegerColumn)



@given(instance=MySQL_IntegerColumn_strategy)
def test_mysql_integercolumn_isAutoIncrement_setter(instance):
    original = instance.isAutoIncrement
    instance.isAutoIncrement = original
    assert instance.isAutoIncrement == original

@given(instance=MySQL_EnumColumn_strategy)
@settings(max_examples=50)
def test_mysql_enumcolumn_instantiation(instance):
    assert isinstance(instance, MySQL_EnumColumn)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=MySQL_Column_strategy)
@settings(max_examples=50)
def test_mysql_column_instantiation(instance):
    assert isinstance(instance, MySQL_Column)



@given(instance=MySQL_Column_strategy)
def test_mysql_column_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=MySQL_Column_strategy)
def test_mysql_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=MySQL_Column_strategy)
def test_mysql_column_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original



@given(instance=MySQL_Column_strategy)
def test_mysql_column_isPrimaryKey_setter(instance):
    original = instance.isPrimaryKey
    instance.isPrimaryKey = original
    assert instance.isPrimaryKey == original



@given(instance=MySQL_Column_strategy)
def test_mysql_column_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=MySQL_EnumItem_strategy)
@settings(max_examples=50)
def test_mysql_enumitem_instantiation(instance):
    assert isinstance(instance, MySQL_EnumItem)

@given(instance=MySQL_Table_strategy)
@settings(max_examples=50)
def test_mysql_table_instantiation(instance):
    assert isinstance(instance, MySQL_Table)

@given(instance=MySQL_DataBase_strategy)
@settings(max_examples=50)
def test_mysql_database_instantiation(instance):
    assert isinstance(instance, MySQL_DataBase)
