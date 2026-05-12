import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    genSql_Column,
    genSql_Table,
    genSql_DataBase,
    genSql_ForeignKey,
    genSql_PrimaryKey,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gensql_column_is_not_abstract():
    assert not inspect.isabstract(genSql_Column)


def test_gensql_column_constructor_exists():
    assert callable(genSql_Column.__init__)


def test_gensql_column_constructor_args():
    sig = inspect.signature(genSql_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "SQLType" in params, "Missing parameter 'SQLType'"
    assert "Longitud" in params, "Missing parameter 'Longitud'"

def test_gensql_column_has_name():
    assert hasattr(genSql_Column, "name")
    descriptor = None
    for klass in genSql_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gensql_column_has_SQLType():
    assert hasattr(genSql_Column, "SQLType")
    descriptor = None
    for klass in genSql_Column.__mro__:
        if "SQLType" in klass.__dict__:
            descriptor = klass.__dict__["SQLType"]
            break
    assert isinstance(descriptor, property)

def test_gensql_column_has_Longitud():
    assert hasattr(genSql_Column, "Longitud")
    descriptor = None
    for klass in genSql_Column.__mro__:
        if "Longitud" in klass.__dict__:
            descriptor = klass.__dict__["Longitud"]
            break
    assert isinstance(descriptor, property)



def test_gensql_table_is_not_abstract():
    assert not inspect.isabstract(genSql_Table)


def test_gensql_table_constructor_exists():
    assert callable(genSql_Table.__init__)


def test_gensql_table_constructor_args():
    sig = inspect.signature(genSql_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gensql_table_has_name():
    assert hasattr(genSql_Table, "name")
    descriptor = None
    for klass in genSql_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gensql_database_is_not_abstract():
    assert not inspect.isabstract(genSql_DataBase)


def test_gensql_database_constructor_exists():
    assert callable(genSql_DataBase.__init__)


def test_gensql_database_constructor_args():
    sig = inspect.signature(genSql_DataBase.__init__)
    params = list(sig.parameters.keys())



def test_gensql_foreignkey_is_not_abstract():
    assert not inspect.isabstract(genSql_ForeignKey)


def test_gensql_foreignkey_constructor_exists():
    assert callable(genSql_ForeignKey.__init__)


def test_gensql_foreignkey_constructor_args():
    sig = inspect.signature(genSql_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_gensql_primarykey_is_not_abstract():
    assert not inspect.isabstract(genSql_PrimaryKey)


def test_gensql_primarykey_constructor_exists():
    assert callable(genSql_PrimaryKey.__init__)


def test_gensql_primarykey_constructor_args():
    sig = inspect.signature(genSql_PrimaryKey.__init__)
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
genSql_Column_strategy = st.builds(
    genSql_Column,
    name=
        safe_text,
    SQLType=
        safe_text,
    Longitud=
        safe_text
)
genSql_Table_strategy = st.builds(
    genSql_Table,
    name=
        safe_text
)
genSql_DataBase_strategy = st.builds(
    genSql_DataBase,
)
genSql_ForeignKey_strategy = st.builds(
    genSql_ForeignKey,
)
genSql_PrimaryKey_strategy = st.builds(
    genSql_PrimaryKey,
)

@given(instance=genSql_Column_strategy)
@settings(max_examples=50)
def test_gensql_column_instantiation(instance):
    assert isinstance(instance, genSql_Column)



@given(instance=genSql_Column_strategy)
def test_gensql_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=genSql_Column_strategy)
def test_gensql_column_SQLType_setter(instance):
    original = instance.SQLType
    instance.SQLType = original
    assert instance.SQLType == original



@given(instance=genSql_Column_strategy)
def test_gensql_column_Longitud_setter(instance):
    original = instance.Longitud
    instance.Longitud = original
    assert instance.Longitud == original

@given(instance=genSql_Table_strategy)
@settings(max_examples=50)
def test_gensql_table_instantiation(instance):
    assert isinstance(instance, genSql_Table)



@given(instance=genSql_Table_strategy)
def test_gensql_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=genSql_DataBase_strategy)
@settings(max_examples=50)
def test_gensql_database_instantiation(instance):
    assert isinstance(instance, genSql_DataBase)

@given(instance=genSql_ForeignKey_strategy)
@settings(max_examples=50)
def test_gensql_foreignkey_instantiation(instance):
    assert isinstance(instance, genSql_ForeignKey)

@given(instance=genSql_PrimaryKey_strategy)
@settings(max_examples=50)
def test_gensql_primarykey_instantiation(instance):
    assert isinstance(instance, genSql_PrimaryKey)
