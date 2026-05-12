import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DataBaseElement,
    database_Schema,
    database_ForeignKey,
    database_Column,
    database_Table,
    database_DataBaseElement,
    RailsData,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_databaseelement_is_not_abstract():
    assert not inspect.isabstract(DataBaseElement)


def test_databaseelement_constructor_exists():
    assert callable(DataBaseElement.__init__)


def test_databaseelement_constructor_args():
    sig = inspect.signature(DataBaseElement.__init__)
    params = list(sig.parameters.keys())



def test_database_schema_is_not_abstract():
    assert not inspect.isabstract(database_Schema)


def test_database_schema_constructor_exists():
    assert callable(database_Schema.__init__)


def test_database_schema_constructor_args():
    sig = inspect.signature(database_Schema.__init__)
    params = list(sig.parameters.keys())



def test_database_foreignkey_is_not_abstract():
    assert not inspect.isabstract(database_ForeignKey)


def test_database_foreignkey_constructor_exists():
    assert callable(database_ForeignKey.__init__)


def test_database_foreignkey_constructor_args():
    sig = inspect.signature(database_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_database_column_is_not_abstract():
    assert not inspect.isabstract(database_Column)


def test_database_column_constructor_exists():
    assert callable(database_Column.__init__)


def test_database_column_constructor_args():
    sig = inspect.signature(database_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_database_column_has_type():
    assert hasattr(database_Column, "type")
    descriptor = None
    for klass in database_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_database_table_is_not_abstract():
    assert not inspect.isabstract(database_Table)


def test_database_table_constructor_exists():
    assert callable(database_Table.__init__)


def test_database_table_constructor_args():
    sig = inspect.signature(database_Table.__init__)
    params = list(sig.parameters.keys())



def test_database_databaseelement_is_not_abstract():
    assert not inspect.isabstract(database_DataBaseElement)


def test_database_databaseelement_constructor_exists():
    assert callable(database_DataBaseElement.__init__)


def test_database_databaseelement_constructor_args():
    sig = inspect.signature(database_DataBaseElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_database_databaseelement_has_name():
    assert hasattr(database_DataBaseElement, "name")
    descriptor = None
    for klass in database_DataBaseElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_railsdata_exists():
    # Check that the Enumeration exists
    assert RailsData is not None

def test_railsdata_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RailsData]
    expected_literals = [
        "float",
        "date",
        "text",
        "time",
        "binary",
        "string",
        "decimal",
        "timestamp",
        "dateTime",
        "boolean",
        "integer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RailsData"


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
DataBaseElement_strategy = st.builds(
    DataBaseElement,
)
database_Schema_strategy = st.builds(
    database_Schema,
)
database_ForeignKey_strategy = st.builds(
    database_ForeignKey,
)
database_Column_strategy = st.builds(
    database_Column,
    type=
        safe_text
)
database_Table_strategy = st.builds(
    database_Table,
)
database_DataBaseElement_strategy = st.builds(
    database_DataBaseElement,
    name=
        safe_text
)

@given(instance=DataBaseElement_strategy)
@settings(max_examples=50)
def test_databaseelement_instantiation(instance):
    assert isinstance(instance, DataBaseElement)

@given(instance=database_Schema_strategy)
@settings(max_examples=50)
def test_database_schema_instantiation(instance):
    assert isinstance(instance, database_Schema)

@given(instance=database_ForeignKey_strategy)
@settings(max_examples=50)
def test_database_foreignkey_instantiation(instance):
    assert isinstance(instance, database_ForeignKey)

@given(instance=database_Column_strategy)
@settings(max_examples=50)
def test_database_column_instantiation(instance):
    assert isinstance(instance, database_Column)



@given(instance=database_Column_strategy)
def test_database_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=database_Table_strategy)
@settings(max_examples=50)
def test_database_table_instantiation(instance):
    assert isinstance(instance, database_Table)

@given(instance=database_DataBaseElement_strategy)
@settings(max_examples=50)
def test_database_databaseelement_instantiation(instance):
    assert isinstance(instance, database_DataBaseElement)



@given(instance=database_DataBaseElement_strategy)
def test_database_databaseelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
