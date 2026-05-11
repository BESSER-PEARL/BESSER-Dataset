import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DataBaseElement,
    database::Schema,
    database::ForeignKey,
    database::Column,
    database::Table,
    database::DataBaseElement,
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



def test_database::schema_is_not_abstract():
    assert not inspect.isabstract(database::Schema)


def test_database::schema_constructor_exists():
    assert callable(database::Schema.__init__)


def test_database::schema_constructor_args():
    sig = inspect.signature(database::Schema.__init__)
    params = list(sig.parameters.keys())



def test_database::foreignkey_is_not_abstract():
    assert not inspect.isabstract(database::ForeignKey)


def test_database::foreignkey_constructor_exists():
    assert callable(database::ForeignKey.__init__)


def test_database::foreignkey_constructor_args():
    sig = inspect.signature(database::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_database::column_is_not_abstract():
    assert not inspect.isabstract(database::Column)


def test_database::column_constructor_exists():
    assert callable(database::Column.__init__)


def test_database::column_constructor_args():
    sig = inspect.signature(database::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_database::column_has_type():
    assert hasattr(database::Column, "type")
    descriptor = None
    for klass in database::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_database::table_is_not_abstract():
    assert not inspect.isabstract(database::Table)


def test_database::table_constructor_exists():
    assert callable(database::Table.__init__)


def test_database::table_constructor_args():
    sig = inspect.signature(database::Table.__init__)
    params = list(sig.parameters.keys())



def test_database::databaseelement_is_not_abstract():
    assert not inspect.isabstract(database::DataBaseElement)


def test_database::databaseelement_constructor_exists():
    assert callable(database::DataBaseElement.__init__)


def test_database::databaseelement_constructor_args():
    sig = inspect.signature(database::DataBaseElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_database::databaseelement_has_name():
    assert hasattr(database::DataBaseElement, "name")
    descriptor = None
    for klass in database::DataBaseElement.__mro__:
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
        "timestamp",
        "binary",
        "time",
        "decimal",
        "boolean",
        "integer",
        "string",
        "dateTime",
        "text",
        "date",
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
database::Schema_strategy = st.builds(
    database::Schema,
)
database::ForeignKey_strategy = st.builds(
    database::ForeignKey,
)
database::Column_strategy = st.builds(
    database::Column,
    type=
        safe_text
)
database::Table_strategy = st.builds(
    database::Table,
)
database::DataBaseElement_strategy = st.builds(
    database::DataBaseElement,
    name=
        safe_text
)

@given(instance=DataBaseElement_strategy)
@settings(max_examples=50)
def test_databaseelement_instantiation(instance):
    assert isinstance(instance, DataBaseElement)

@given(instance=database::Schema_strategy)
@settings(max_examples=50)
def test_database::schema_instantiation(instance):
    assert isinstance(instance, database::Schema)

@given(instance=database::ForeignKey_strategy)
@settings(max_examples=50)
def test_database::foreignkey_instantiation(instance):
    assert isinstance(instance, database::ForeignKey)

@given(instance=database::Column_strategy)
@settings(max_examples=50)
def test_database::column_instantiation(instance):
    assert isinstance(instance, database::Column)

@given(instance=database::Column_strategy)
def test_database::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=database::Column_strategy)
def test_database::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=database::Table_strategy)
@settings(max_examples=50)
def test_database::table_instantiation(instance):
    assert isinstance(instance, database::Table)

@given(instance=database::DataBaseElement_strategy)
@settings(max_examples=50)
def test_database::databaseelement_instantiation(instance):
    assert isinstance(instance, database::DataBaseElement)

@given(instance=database::DataBaseElement_strategy)
def test_database::databaseelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=database::DataBaseElement_strategy)
def test_database::databaseelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
