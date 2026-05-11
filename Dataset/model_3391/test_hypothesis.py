import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DML::Value,
    DML::Column,
    DML::Registry,
    DML::InsertInto,
    DML::InsertsStatements,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dml::value_is_not_abstract():
    assert not inspect.isabstract(DML::Value)


def test_dml::value_constructor_exists():
    assert callable(DML::Value.__init__)


def test_dml::value_constructor_args():
    sig = inspect.signature(DML::Value.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dml::value_has_value():
    assert hasattr(DML::Value, "value")
    descriptor = None
    for klass in DML::Value.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dml::column_is_not_abstract():
    assert not inspect.isabstract(DML::Column)


def test_dml::column_constructor_exists():
    assert callable(DML::Column.__init__)


def test_dml::column_constructor_args():
    sig = inspect.signature(DML::Column.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_dml::column_has_columnName():
    assert hasattr(DML::Column, "columnName")
    descriptor = None
    for klass in DML::Column.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_dml::registry_is_not_abstract():
    assert not inspect.isabstract(DML::Registry)


def test_dml::registry_constructor_exists():
    assert callable(DML::Registry.__init__)


def test_dml::registry_constructor_args():
    sig = inspect.signature(DML::Registry.__init__)
    params = list(sig.parameters.keys())



def test_dml::insertinto_is_not_abstract():
    assert not inspect.isabstract(DML::InsertInto)


def test_dml::insertinto_constructor_exists():
    assert callable(DML::InsertInto.__init__)


def test_dml::insertinto_constructor_args():
    sig = inspect.signature(DML::InsertInto.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_dml::insertinto_has_tableName():
    assert hasattr(DML::InsertInto, "tableName")
    descriptor = None
    for klass in DML::InsertInto.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_dml::insertsstatements_is_not_abstract():
    assert not inspect.isabstract(DML::InsertsStatements)


def test_dml::insertsstatements_constructor_exists():
    assert callable(DML::InsertsStatements.__init__)


def test_dml::insertsstatements_constructor_args():
    sig = inspect.signature(DML::InsertsStatements.__init__)
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
DML::Value_strategy = st.builds(
    DML::Value,
    value=
        safe_text
)
DML::Column_strategy = st.builds(
    DML::Column,
    columnName=
        safe_text
)
DML::Registry_strategy = st.builds(
    DML::Registry,
)
DML::InsertInto_strategy = st.builds(
    DML::InsertInto,
    tableName=
        safe_text
)
DML::InsertsStatements_strategy = st.builds(
    DML::InsertsStatements,
)

@given(instance=DML::Value_strategy)
@settings(max_examples=50)
def test_dml::value_instantiation(instance):
    assert isinstance(instance, DML::Value)

@given(instance=DML::Value_strategy)
def test_dml::value_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=DML::Value_strategy)
def test_dml::value_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DML::Column_strategy)
@settings(max_examples=50)
def test_dml::column_instantiation(instance):
    assert isinstance(instance, DML::Column)

@given(instance=DML::Column_strategy)
def test_dml::column_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=DML::Column_strategy)
def test_dml::column_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DML::Registry_strategy)
@settings(max_examples=50)
def test_dml::registry_instantiation(instance):
    assert isinstance(instance, DML::Registry)

@given(instance=DML::InsertInto_strategy)
@settings(max_examples=50)
def test_dml::insertinto_instantiation(instance):
    assert isinstance(instance, DML::InsertInto)

@given(instance=DML::InsertInto_strategy)
def test_dml::insertinto_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=DML::InsertInto_strategy)
def test_dml::insertinto_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=DML::InsertsStatements_strategy)
@settings(max_examples=50)
def test_dml::insertsstatements_instantiation(instance):
    assert isinstance(instance, DML::InsertsStatements)
