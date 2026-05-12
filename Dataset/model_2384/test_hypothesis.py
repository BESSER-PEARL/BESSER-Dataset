import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tables_ForeignKey,
    tables_Column,
    tables_Table,
    tables_Database,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tables_foreignkey_is_not_abstract():
    assert not inspect.isabstract(tables_ForeignKey)


def test_tables_foreignkey_constructor_exists():
    assert callable(tables_ForeignKey.__init__)


def test_tables_foreignkey_constructor_args():
    sig = inspect.signature(tables_ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tables_foreignkey_has_name():
    assert hasattr(tables_ForeignKey, "name")
    descriptor = None
    for klass in tables_ForeignKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tables_column_is_not_abstract():
    assert not inspect.isabstract(tables_Column)


def test_tables_column_constructor_exists():
    assert callable(tables_Column.__init__)


def test_tables_column_constructor_args():
    sig = inspect.signature(tables_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_tables_column_has_type():
    assert hasattr(tables_Column, "type")
    descriptor = None
    for klass in tables_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_tables_column_has_name():
    assert hasattr(tables_Column, "name")
    descriptor = None
    for klass in tables_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tables_table_is_not_abstract():
    assert not inspect.isabstract(tables_Table)


def test_tables_table_constructor_exists():
    assert callable(tables_Table.__init__)


def test_tables_table_constructor_args():
    sig = inspect.signature(tables_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tables_table_has_name():
    assert hasattr(tables_Table, "name")
    descriptor = None
    for klass in tables_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tables_database_is_not_abstract():
    assert not inspect.isabstract(tables_Database)


def test_tables_database_constructor_exists():
    assert callable(tables_Database.__init__)


def test_tables_database_constructor_args():
    sig = inspect.signature(tables_Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tables_database_has_name():
    assert hasattr(tables_Database, "name")
    descriptor = None
    for klass in tables_Database.__mro__:
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
        "integer",
        "bool",
        "string",
        "float",
        "datetime",
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
tables_ForeignKey_strategy = st.builds(
    tables_ForeignKey,
    name=
        safe_text
)
tables_Column_strategy = st.builds(
    tables_Column,
    type=
        safe_text,
    name=
        safe_text
)
tables_Table_strategy = st.builds(
    tables_Table,
    name=
        safe_text
)
tables_Database_strategy = st.builds(
    tables_Database,
    name=
        safe_text
)

@given(instance=tables_ForeignKey_strategy)
@settings(max_examples=50)
def test_tables_foreignkey_instantiation(instance):
    assert isinstance(instance, tables_ForeignKey)



@given(instance=tables_ForeignKey_strategy)
def test_tables_foreignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tables_Column_strategy)
@settings(max_examples=50)
def test_tables_column_instantiation(instance):
    assert isinstance(instance, tables_Column)



@given(instance=tables_Column_strategy)
def test_tables_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=tables_Column_strategy)
def test_tables_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tables_Table_strategy)
@settings(max_examples=50)
def test_tables_table_instantiation(instance):
    assert isinstance(instance, tables_Table)



@given(instance=tables_Table_strategy)
def test_tables_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tables_Database_strategy)
@settings(max_examples=50)
def test_tables_database_instantiation(instance):
    assert isinstance(instance, tables_Database)



@given(instance=tables_Database_strategy)
def test_tables_database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
