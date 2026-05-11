import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tables::ForeignKey,
    tables::Column,
    tables::Table,
    tables::Database,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tables::foreignkey_is_not_abstract():
    assert not inspect.isabstract(tables::ForeignKey)


def test_tables::foreignkey_constructor_exists():
    assert callable(tables::ForeignKey.__init__)


def test_tables::foreignkey_constructor_args():
    sig = inspect.signature(tables::ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tables::foreignkey_has_name():
    assert hasattr(tables::ForeignKey, "name")
    descriptor = None
    for klass in tables::ForeignKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tables::column_is_not_abstract():
    assert not inspect.isabstract(tables::Column)


def test_tables::column_constructor_exists():
    assert callable(tables::Column.__init__)


def test_tables::column_constructor_args():
    sig = inspect.signature(tables::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_tables::column_has_type():
    assert hasattr(tables::Column, "type")
    descriptor = None
    for klass in tables::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_tables::column_has_name():
    assert hasattr(tables::Column, "name")
    descriptor = None
    for klass in tables::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tables::table_is_not_abstract():
    assert not inspect.isabstract(tables::Table)


def test_tables::table_constructor_exists():
    assert callable(tables::Table.__init__)


def test_tables::table_constructor_args():
    sig = inspect.signature(tables::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tables::table_has_name():
    assert hasattr(tables::Table, "name")
    descriptor = None
    for klass in tables::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tables::database_is_not_abstract():
    assert not inspect.isabstract(tables::Database)


def test_tables::database_constructor_exists():
    assert callable(tables::Database.__init__)


def test_tables::database_constructor_args():
    sig = inspect.signature(tables::Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tables::database_has_name():
    assert hasattr(tables::Database, "name")
    descriptor = None
    for klass in tables::Database.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "bool",
        "datetime",
        "string",
        "float",
        "integer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
tables::ForeignKey_strategy = st.builds(
    tables::ForeignKey,
    name=
        safe_text
)
tables::Column_strategy = st.builds(
    tables::Column,
    type=
        safe_text,
    name=
        safe_text
)
tables::Table_strategy = st.builds(
    tables::Table,
    name=
        safe_text
)
tables::Database_strategy = st.builds(
    tables::Database,
    name=
        safe_text
)

@given(instance=tables::ForeignKey_strategy)
@settings(max_examples=50)
def test_tables::foreignkey_instantiation(instance):
    assert isinstance(instance, tables::ForeignKey)

@given(instance=tables::ForeignKey_strategy)
def test_tables::foreignkey_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tables::ForeignKey_strategy)
def test_tables::foreignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tables::Column_strategy)
@settings(max_examples=50)
def test_tables::column_instantiation(instance):
    assert isinstance(instance, tables::Column)

@given(instance=tables::Column_strategy)
def test_tables::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=tables::Column_strategy)
def test_tables::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=tables::Column_strategy)
def test_tables::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tables::Column_strategy)
def test_tables::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tables::Table_strategy)
@settings(max_examples=50)
def test_tables::table_instantiation(instance):
    assert isinstance(instance, tables::Table)

@given(instance=tables::Table_strategy)
def test_tables::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tables::Table_strategy)
def test_tables::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tables::Database_strategy)
@settings(max_examples=50)
def test_tables::database_instantiation(instance):
    assert isinstance(instance, tables::Database)

@given(instance=tables::Database_strategy)
def test_tables::database_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tables::Database_strategy)
def test_tables::database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
