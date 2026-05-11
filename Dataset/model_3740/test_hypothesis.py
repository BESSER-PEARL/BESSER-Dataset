import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EnumItem,
    MySQL::EnumSet,
    EnumSet,
    DataBase,
    Column,
    MySQL::EnumColumn,
    MySQL::IntegerColumn,
    MySQL::ForeignColumn,
    Table,
    NamedElement,
    MySQL::Table,
    MySQL::Column,
    MySQL::EnumItem,
    MySQL::DataBase,
    MySQL::NamedElement,
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



def test_mysql::enumset_is_not_abstract():
    assert not inspect.isabstract(MySQL::EnumSet)


def test_mysql::enumset_constructor_exists():
    assert callable(MySQL::EnumSet.__init__)


def test_mysql::enumset_constructor_args():
    sig = inspect.signature(MySQL::EnumSet.__init__)
    params = list(sig.parameters.keys())



def test_enumset_is_not_abstract():
    assert not inspect.isabstract(EnumSet)


def test_enumset_constructor_exists():
    assert callable(EnumSet.__init__)


def test_enumset_constructor_args():
    sig = inspect.signature(EnumSet.__init__)
    params = list(sig.parameters.keys())



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



def test_mysql::enumcolumn_is_not_abstract():
    assert not inspect.isabstract(MySQL::EnumColumn)


def test_mysql::enumcolumn_constructor_exists():
    assert callable(MySQL::EnumColumn.__init__)


def test_mysql::enumcolumn_constructor_args():
    sig = inspect.signature(MySQL::EnumColumn.__init__)
    params = list(sig.parameters.keys())



def test_mysql::integercolumn_is_not_abstract():
    assert not inspect.isabstract(MySQL::IntegerColumn)


def test_mysql::integercolumn_constructor_exists():
    assert callable(MySQL::IntegerColumn.__init__)


def test_mysql::integercolumn_constructor_args():
    sig = inspect.signature(MySQL::IntegerColumn.__init__)
    params = list(sig.parameters.keys())
    assert "isAutoIncrement" in params, "Missing parameter 'isAutoIncrement'"

def test_mysql::integercolumn_has_isAutoIncrement():
    assert hasattr(MySQL::IntegerColumn, "isAutoIncrement")
    descriptor = None
    for klass in MySQL::IntegerColumn.__mro__:
        if "isAutoIncrement" in klass.__dict__:
            descriptor = klass.__dict__["isAutoIncrement"]
            break
    assert isinstance(descriptor, property)



def test_mysql::foreigncolumn_is_not_abstract():
    assert not inspect.isabstract(MySQL::ForeignColumn)


def test_mysql::foreigncolumn_constructor_exists():
    assert callable(MySQL::ForeignColumn.__init__)


def test_mysql::foreigncolumn_constructor_args():
    sig = inspect.signature(MySQL::ForeignColumn.__init__)
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



def test_mysql::table_is_not_abstract():
    assert not inspect.isabstract(MySQL::Table)


def test_mysql::table_constructor_exists():
    assert callable(MySQL::Table.__init__)


def test_mysql::table_constructor_args():
    sig = inspect.signature(MySQL::Table.__init__)
    params = list(sig.parameters.keys())



def test_mysql::column_is_not_abstract():
    assert not inspect.isabstract(MySQL::Column)


def test_mysql::column_constructor_exists():
    assert callable(MySQL::Column.__init__)


def test_mysql::column_constructor_args():
    sig = inspect.signature(MySQL::Column.__init__)
    params = list(sig.parameters.keys())
    assert "isPrimaryKey" in params, "Missing parameter 'isPrimaryKey'"
    assert "type" in params, "Missing parameter 'type'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_mysql::column_has_isPrimaryKey():
    assert hasattr(MySQL::Column, "isPrimaryKey")
    descriptor = None
    for klass in MySQL::Column.__mro__:
        if "isPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_mysql::column_has_type():
    assert hasattr(MySQL::Column, "type")
    descriptor = None
    for klass in MySQL::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mysql::column_has_defaultValue():
    assert hasattr(MySQL::Column, "defaultValue")
    descriptor = None
    for klass in MySQL::Column.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_mysql::column_has_comment():
    assert hasattr(MySQL::Column, "comment")
    descriptor = None
    for klass in MySQL::Column.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_mysql::enumitem_is_not_abstract():
    assert not inspect.isabstract(MySQL::EnumItem)


def test_mysql::enumitem_constructor_exists():
    assert callable(MySQL::EnumItem.__init__)


def test_mysql::enumitem_constructor_args():
    sig = inspect.signature(MySQL::EnumItem.__init__)
    params = list(sig.parameters.keys())



def test_mysql::database_is_not_abstract():
    assert not inspect.isabstract(MySQL::DataBase)


def test_mysql::database_constructor_exists():
    assert callable(MySQL::DataBase.__init__)


def test_mysql::database_constructor_args():
    sig = inspect.signature(MySQL::DataBase.__init__)
    params = list(sig.parameters.keys())



def test_mysql::namedelement_is_not_abstract():
    assert not inspect.isabstract(MySQL::NamedElement)


def test_mysql::namedelement_constructor_exists():
    assert callable(MySQL::NamedElement.__init__)


def test_mysql::namedelement_constructor_args():
    sig = inspect.signature(MySQL::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mysql::namedelement_has_name():
    assert hasattr(MySQL::NamedElement, "name")
    descriptor = None
    for klass in MySQL::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
EnumItem_strategy = st.builds(
    EnumItem,
)
MySQL::EnumSet_strategy = st.builds(
    MySQL::EnumSet,
)
EnumSet_strategy = st.builds(
    EnumSet,
)
DataBase_strategy = st.builds(
    DataBase,
)
Column_strategy = st.builds(
    Column,
)
MySQL::EnumColumn_strategy = st.builds(
    MySQL::EnumColumn,
)
MySQL::IntegerColumn_strategy = st.builds(
    MySQL::IntegerColumn,
    isAutoIncrement=
        safe_text
)
MySQL::ForeignColumn_strategy = st.builds(
    MySQL::ForeignColumn,
)
Table_strategy = st.builds(
    Table,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
MySQL::Table_strategy = st.builds(
    MySQL::Table,
)
MySQL::Column_strategy = st.builds(
    MySQL::Column,
    isPrimaryKey=
        safe_text,
    type=
        safe_text,
    defaultValue=
        safe_text,
    comment=
        safe_text
)
MySQL::EnumItem_strategy = st.builds(
    MySQL::EnumItem,
)
MySQL::DataBase_strategy = st.builds(
    MySQL::DataBase,
)
MySQL::NamedElement_strategy = st.builds(
    MySQL::NamedElement,
    name=
        safe_text
)

@given(instance=EnumItem_strategy)
@settings(max_examples=50)
def test_enumitem_instantiation(instance):
    assert isinstance(instance, EnumItem)

@given(instance=MySQL::EnumSet_strategy)
@settings(max_examples=50)
def test_mysql::enumset_instantiation(instance):
    assert isinstance(instance, MySQL::EnumSet)

@given(instance=EnumSet_strategy)
@settings(max_examples=50)
def test_enumset_instantiation(instance):
    assert isinstance(instance, EnumSet)

@given(instance=DataBase_strategy)
@settings(max_examples=50)
def test_database_instantiation(instance):
    assert isinstance(instance, DataBase)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=MySQL::EnumColumn_strategy)
@settings(max_examples=50)
def test_mysql::enumcolumn_instantiation(instance):
    assert isinstance(instance, MySQL::EnumColumn)

@given(instance=MySQL::IntegerColumn_strategy)
@settings(max_examples=50)
def test_mysql::integercolumn_instantiation(instance):
    assert isinstance(instance, MySQL::IntegerColumn)

@given(instance=MySQL::IntegerColumn_strategy)
def test_mysql::integercolumn_isAutoIncrement_type(instance):
    assert isinstance(instance.isAutoIncrement, str)


@given(instance=MySQL::IntegerColumn_strategy)
def test_mysql::integercolumn_isAutoIncrement_setter(instance):
    original = instance.isAutoIncrement
    instance.isAutoIncrement = original
    assert instance.isAutoIncrement == original

@given(instance=MySQL::ForeignColumn_strategy)
@settings(max_examples=50)
def test_mysql::foreigncolumn_instantiation(instance):
    assert isinstance(instance, MySQL::ForeignColumn)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=MySQL::Table_strategy)
@settings(max_examples=50)
def test_mysql::table_instantiation(instance):
    assert isinstance(instance, MySQL::Table)

@given(instance=MySQL::Column_strategy)
@settings(max_examples=50)
def test_mysql::column_instantiation(instance):
    assert isinstance(instance, MySQL::Column)

@given(instance=MySQL::Column_strategy)
def test_mysql::column_isPrimaryKey_type(instance):
    assert isinstance(instance.isPrimaryKey, str)


@given(instance=MySQL::Column_strategy)
def test_mysql::column_isPrimaryKey_setter(instance):
    original = instance.isPrimaryKey
    instance.isPrimaryKey = original
    assert instance.isPrimaryKey == original

@given(instance=MySQL::Column_strategy)
def test_mysql::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MySQL::Column_strategy)
def test_mysql::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MySQL::Column_strategy)
def test_mysql::column_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=MySQL::Column_strategy)
def test_mysql::column_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=MySQL::Column_strategy)
def test_mysql::column_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=MySQL::Column_strategy)
def test_mysql::column_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=MySQL::EnumItem_strategy)
@settings(max_examples=50)
def test_mysql::enumitem_instantiation(instance):
    assert isinstance(instance, MySQL::EnumItem)

@given(instance=MySQL::DataBase_strategy)
@settings(max_examples=50)
def test_mysql::database_instantiation(instance):
    assert isinstance(instance, MySQL::DataBase)

@given(instance=MySQL::NamedElement_strategy)
@settings(max_examples=50)
def test_mysql::namedelement_instantiation(instance):
    assert isinstance(instance, MySQL::NamedElement)

@given(instance=MySQL::NamedElement_strategy)
def test_mysql::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MySQL::NamedElement_strategy)
def test_mysql::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
