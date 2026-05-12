import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DML_Value,
    DML_Column,
    DML_Registry,
    DML_InsertInto,
    DML_InsertsStatements,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dml_value_is_not_abstract():
    assert not inspect.isabstract(DML_Value)


def test_dml_value_constructor_exists():
    assert callable(DML_Value.__init__)


def test_dml_value_constructor_args():
    sig = inspect.signature(DML_Value.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dml_value_has_value():
    assert hasattr(DML_Value, "value")
    descriptor = None
    for klass in DML_Value.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dml_column_is_not_abstract():
    assert not inspect.isabstract(DML_Column)


def test_dml_column_constructor_exists():
    assert callable(DML_Column.__init__)


def test_dml_column_constructor_args():
    sig = inspect.signature(DML_Column.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_dml_column_has_columnName():
    assert hasattr(DML_Column, "columnName")
    descriptor = None
    for klass in DML_Column.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_dml_registry_is_not_abstract():
    assert not inspect.isabstract(DML_Registry)


def test_dml_registry_constructor_exists():
    assert callable(DML_Registry.__init__)


def test_dml_registry_constructor_args():
    sig = inspect.signature(DML_Registry.__init__)
    params = list(sig.parameters.keys())



def test_dml_insertinto_is_not_abstract():
    assert not inspect.isabstract(DML_InsertInto)


def test_dml_insertinto_constructor_exists():
    assert callable(DML_InsertInto.__init__)


def test_dml_insertinto_constructor_args():
    sig = inspect.signature(DML_InsertInto.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_dml_insertinto_has_tableName():
    assert hasattr(DML_InsertInto, "tableName")
    descriptor = None
    for klass in DML_InsertInto.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_dml_insertsstatements_is_not_abstract():
    assert not inspect.isabstract(DML_InsertsStatements)


def test_dml_insertsstatements_constructor_exists():
    assert callable(DML_InsertsStatements.__init__)


def test_dml_insertsstatements_constructor_args():
    sig = inspect.signature(DML_InsertsStatements.__init__)
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
DML_Value_strategy = st.builds(
    DML_Value,
    value=
        safe_text
)
DML_Column_strategy = st.builds(
    DML_Column,
    columnName=
        safe_text
)
DML_Registry_strategy = st.builds(
    DML_Registry,
)
DML_InsertInto_strategy = st.builds(
    DML_InsertInto,
    tableName=
        safe_text
)
DML_InsertsStatements_strategy = st.builds(
    DML_InsertsStatements,
)

@given(instance=DML_Value_strategy)
@settings(max_examples=50)
def test_dml_value_instantiation(instance):
    assert isinstance(instance, DML_Value)



@given(instance=DML_Value_strategy)
def test_dml_value_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DML_Column_strategy)
@settings(max_examples=50)
def test_dml_column_instantiation(instance):
    assert isinstance(instance, DML_Column)



@given(instance=DML_Column_strategy)
def test_dml_column_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DML_Registry_strategy)
@settings(max_examples=50)
def test_dml_registry_instantiation(instance):
    assert isinstance(instance, DML_Registry)

@given(instance=DML_InsertInto_strategy)
@settings(max_examples=50)
def test_dml_insertinto_instantiation(instance):
    assert isinstance(instance, DML_InsertInto)



@given(instance=DML_InsertInto_strategy)
def test_dml_insertinto_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=DML_InsertsStatements_strategy)
@settings(max_examples=50)
def test_dml_insertsstatements_instantiation(instance):
    assert isinstance(instance, DML_InsertsStatements)
