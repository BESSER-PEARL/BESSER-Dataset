import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    genSql::ForeignKey,
    genSql::PrimaryKey,
    genSql::Column,
    genSql::Table,
    genSql::DataBase,
    TIPO,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gensql::foreignkey_is_not_abstract():
    assert not inspect.isabstract(genSql::ForeignKey)


def test_gensql::foreignkey_constructor_exists():
    assert callable(genSql::ForeignKey.__init__)


def test_gensql::foreignkey_constructor_args():
    sig = inspect.signature(genSql::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_gensql::primarykey_is_not_abstract():
    assert not inspect.isabstract(genSql::PrimaryKey)


def test_gensql::primarykey_constructor_exists():
    assert callable(genSql::PrimaryKey.__init__)


def test_gensql::primarykey_constructor_args():
    sig = inspect.signature(genSql::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_gensql::column_is_not_abstract():
    assert not inspect.isabstract(genSql::Column)


def test_gensql::column_constructor_exists():
    assert callable(genSql::Column.__init__)


def test_gensql::column_constructor_args():
    sig = inspect.signature(genSql::Column.__init__)
    params = list(sig.parameters.keys())
    assert "SQLType" in params, "Missing parameter 'SQLType'"
    assert "name" in params, "Missing parameter 'name'"

def test_gensql::column_has_SQLType():
    assert hasattr(genSql::Column, "SQLType")
    descriptor = None
    for klass in genSql::Column.__mro__:
        if "SQLType" in klass.__dict__:
            descriptor = klass.__dict__["SQLType"]
            break
    assert isinstance(descriptor, property)

def test_gensql::column_has_name():
    assert hasattr(genSql::Column, "name")
    descriptor = None
    for klass in genSql::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gensql::table_is_not_abstract():
    assert not inspect.isabstract(genSql::Table)


def test_gensql::table_constructor_exists():
    assert callable(genSql::Table.__init__)


def test_gensql::table_constructor_args():
    sig = inspect.signature(genSql::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gensql::table_has_name():
    assert hasattr(genSql::Table, "name")
    descriptor = None
    for klass in genSql::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gensql::database_is_not_abstract():
    assert not inspect.isabstract(genSql::DataBase)


def test_gensql::database_constructor_exists():
    assert callable(genSql::DataBase.__init__)


def test_gensql::database_constructor_args():
    sig = inspect.signature(genSql::DataBase.__init__)
    params = list(sig.parameters.keys())

def test_tipo_exists():
    # Check that the Enumeration exists
    assert TIPO is not None

def test_tipo_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TIPO]
    expected_literals = [
        "varchar",
        "number",
        "boolean",
        "int",
        "date",
        "String",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TIPO"


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
genSql::ForeignKey_strategy = st.builds(
    genSql::ForeignKey,
)
genSql::PrimaryKey_strategy = st.builds(
    genSql::PrimaryKey,
)
genSql::Column_strategy = st.builds(
    genSql::Column,
    SQLType=
        safe_text,
    name=
        safe_text
)
genSql::Table_strategy = st.builds(
    genSql::Table,
    name=
        safe_text
)
genSql::DataBase_strategy = st.builds(
    genSql::DataBase,
)

@given(instance=genSql::ForeignKey_strategy)
@settings(max_examples=50)
def test_gensql::foreignkey_instantiation(instance):
    assert isinstance(instance, genSql::ForeignKey)

@given(instance=genSql::PrimaryKey_strategy)
@settings(max_examples=50)
def test_gensql::primarykey_instantiation(instance):
    assert isinstance(instance, genSql::PrimaryKey)

@given(instance=genSql::Column_strategy)
@settings(max_examples=50)
def test_gensql::column_instantiation(instance):
    assert isinstance(instance, genSql::Column)

@given(instance=genSql::Column_strategy)
def test_gensql::column_SQLType_type(instance):
    assert isinstance(instance.SQLType, str)


@given(instance=genSql::Column_strategy)
def test_gensql::column_SQLType_setter(instance):
    original = instance.SQLType
    instance.SQLType = original
    assert instance.SQLType == original

@given(instance=genSql::Column_strategy)
def test_gensql::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=genSql::Column_strategy)
def test_gensql::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=genSql::Table_strategy)
@settings(max_examples=50)
def test_gensql::table_instantiation(instance):
    assert isinstance(instance, genSql::Table)

@given(instance=genSql::Table_strategy)
def test_gensql::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=genSql::Table_strategy)
def test_gensql::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=genSql::DataBase_strategy)
@settings(max_examples=50)
def test_gensql::database_instantiation(instance):
    assert isinstance(instance, genSql::DataBase)
